import { createRemoteJWKSet, jwtVerify } from 'jose';
export const SITE_ORIGIN='https://olympiad-atlas.pr141.chatgpt.site';
export const REDIRECT_URI=SITE_ORIGIN+'/auth/google/callback';
export const SESSION_COOKIE='__Host-atlas_google';
const STATE_COOKIE='__Host-atlas_oauth';
const JWKS=createRemoteJWKSet(new URL('https://www.googleapis.com/oauth2/v3/certs'));
const random=()=>Array.from(crypto.getRandomValues(new Uint8Array(32)),x=>x.toString(16).padStart(2,'0')).join('');
export const hash=async s=>Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s))),x=>x.toString(16).padStart(2,'0')).join('');
const challenge=async s=>btoa(String.fromCharCode(...new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s))))).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
export function cookie(request,name){return (request.headers.get('cookie')||'').split(';').map(x=>x.trim()).find(x=>x.startsWith(name+'='))?.slice(name.length+1)||''}
const setCookie=(name,value,age)=>`${name}=${value}; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=${age}`;
const redirect=(path,cookies=[])=>{const headers=new Headers({'Location':path,'Cache-Control':'no-store','Referrer-Policy':'no-referrer'});for(const c of cookies)headers.append('Set-Cookie',c);return new Response(null,{status:303,headers})};
const fail=(code='failed')=>redirect('/?google_auth='+code+'#account',[setCookie(STATE_COOKIE,'',0)]);
export const googleEnabled=env=>!!(env.GOOGLE_CLIENT_ID&&env.GOOGLE_CLIENT_SECRET&&env.DB);
export async function verifyGoogleToken(token,clientId,nonce,key=JWKS){
 const {payload}=await jwtVerify(token,key,{algorithms:['RS256'],issuer:['https://accounts.google.com','accounts.google.com'],audience:clientId,requiredClaims:['exp','iat','sub','nonce'],maxTokenAge:'10m',clockTolerance:30});
 if(payload.nonce!==nonce||(payload.azp||Array.isArray(payload.aud)&&payload.aud.length>1)&&payload.azp!==clientId||typeof payload.sub!=='string'||!payload.sub||payload.sub.length>255||payload.email_verified!==true||typeof payload.email!=='string')throw Error('Invalid Google identity');
 return {subject:payload.sub,email:payload.email,name:typeof payload.name==='string'?payload.name:payload.email};
}
export async function getGoogleUser(request,db){
 const token=cookie(request,SESSION_COOKIE);if(!token||!db||!/^[a-f0-9]{64}$/.test(token))return null;
 const row=await db.prepare('SELECT s.user_id, i.email, i.name FROM google_sessions s JOIN google_identities i ON i.user_id = s.user_id WHERE s.token_hash = ? AND s.expires_at > ?').bind(await hash(token),Date.now()).first();
 return row?{userId:row.user_id,email:row.email,displayName:row.name,provider:'google'}:null;
}
export async function beginGoogle(request,env,currentUser){
 if(!googleEnabled(env))return fail('unavailable');
 const link=new URL(request.url).searchParams.get('link')==='1';
 if(link&&(!currentUser||currentUser.provider==='google'||request.headers.get('sec-fetch-site')!=='same-origin'))return fail('link_required');
 const state=random(),browser=random(),verifier=random(),nonce=random(),now=Date.now();
 await env.DB.batch([
  env.DB.prepare('DELETE FROM google_states WHERE expires_at < ?').bind(now),
  env.DB.prepare('DELETE FROM google_sessions WHERE expires_at < ?').bind(now),
  env.DB.prepare('INSERT INTO google_states (state_hash, browser_hash, verifier, nonce, link_user_id, expires_at) VALUES (?, ?, ?, ?, ?, ?)').bind(await hash(state),await hash(browser),verifier,nonce,link?currentUser.userId:null,now+600000)
 ]);
 const query=new URLSearchParams({client_id:env.GOOGLE_CLIENT_ID,redirect_uri:REDIRECT_URI,response_type:'code',scope:'openid email profile',state,nonce,code_challenge:await challenge(verifier),code_challenge_method:'S256',prompt:'select_account'});
 return redirect('https://accounts.google.com/o/oauth2/v2/auth?'+query,[setCookie(STATE_COOKIE,browser,600)]);
}
export async function finishGoogle(request,env,chatgptUser,{fetcher=fetch,verify=verifyGoogleToken}={}){
 if(!googleEnabled(env))return fail('unavailable');
 const url=new URL(request.url),state=url.searchParams.get('state'),browser=cookie(request,STATE_COOKIE);
 if(!state||!/^[a-f0-9]{64}$/.test(state)||!/^[a-f0-9]{64}$/.test(browser))return fail('expired');
 // A single atomic consume prevents callback replay, even across concurrent requests.
 const row=await env.DB.prepare('DELETE FROM google_states WHERE state_hash = ? AND browser_hash = ? AND expires_at > ? RETURNING verifier, nonce, link_user_id').bind(await hash(state),await hash(browser),Date.now()).first();
 if(!row)return fail('expired');
 if(url.searchParams.has('error'))return fail('cancelled');
 const code=url.searchParams.get('code');if(!code||code.length>4096)return fail();
 if(row.link_user_id&&chatgptUser?.userId!==row.link_user_id)return fail('link_required');
 try{
  const response=await fetcher('https://oauth2.googleapis.com/token',{method:'POST',headers:{'Content-Type':'application/x-www-form-urlencoded'},body:new URLSearchParams({client_id:env.GOOGLE_CLIENT_ID,client_secret:env.GOOGLE_CLIENT_SECRET,redirect_uri:REDIRECT_URI,grant_type:'authorization_code',code,code_verifier:row.verifier}),signal:AbortSignal.timeout(15000)});
  if(!response.ok)return fail();const tokens=await response.json();if(typeof tokens.id_token!=='string')return fail();
  const identity=await verify(tokens.id_token,env.GOOGLE_CLIENT_ID,row.nonce);
  let existing=await env.DB.prepare('SELECT user_id FROM google_identities WHERE subject = ?').bind(identity.subject).first();
  if(row.link_user_id&&existing&&existing.user_id!==row.link_user_id)return fail('already_linked');
  const userId=existing?.user_id||row.link_user_id||'google-'+await hash(identity.subject);
  await env.DB.prepare('INSERT INTO google_identities (subject, user_id, email, name) VALUES (?, ?, ?, ?) ON CONFLICT(subject) DO UPDATE SET email=excluded.email, name=excluded.name').bind(identity.subject,userId,identity.email,identity.name).run();
  existing=await env.DB.prepare('SELECT user_id FROM google_identities WHERE subject = ?').bind(identity.subject).first();
  if(existing.user_id!==userId)return fail('already_linked');
  const token=random();await env.DB.prepare('INSERT INTO google_sessions (token_hash, user_id, expires_at) VALUES (?, ?, ?)').bind(await hash(token),userId,Date.now()+30*86400000).run();
  return redirect('/?google_auth='+ (row.link_user_id?'linked':'success')+'#account',[setCookie(STATE_COOKIE,'',0),setCookie(SESSION_COOKIE,token,30*86400)]);
 }catch{return fail()}
}
export async function endGoogle(request,db){
 if(request.headers.get('sec-fetch-site')==='cross-site')return new Response('Please sign out from the Account page.',{status:403});
 const token=cookie(request,SESSION_COOKIE);if(token&&db)await db.prepare('DELETE FROM google_sessions WHERE token_hash = ?').bind(await hash(token)).run();
 return redirect('/signout-with-chatgpt?return_to=%2F%23account',[setCookie(SESSION_COOKIE,'',0),setCookie(STATE_COOKIE,'',0)]);
}
export async function beginChatGPT(request,db){
 const token=cookie(request,SESSION_COOKIE);if(token&&db)await db.prepare('DELETE FROM google_sessions WHERE token_hash = ?').bind(await hash(token)).run();
 return redirect('/signin-with-chatgpt?return_to=%2F%23account',[setCookie(SESSION_COOKIE,'',0)]);
}
