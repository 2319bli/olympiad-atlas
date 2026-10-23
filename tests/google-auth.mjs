import assert from 'node:assert/strict';import fs from 'node:fs';import {DatabaseSync} from 'node:sqlite';import {SignJWT,generateKeyPair} from 'jose';
import {beginGoogle,finishGoogle,getGoogleUser,endGoogle,beginChatGPT,verifyGoogleToken,googleEnabled,SESSION_COOKIE,SITE_ORIGIN,REDIRECT_URI} from '../server/google-auth.mjs';
const sql=new DatabaseSync(':memory:');for(const f of fs.readdirSync('drizzle').filter(x=>x.endsWith('.sql')).sort())sql.exec(fs.readFileSync('drizzle/'+f,'utf8'));
class Stmt{constructor(q){this.q=q}bind(...args){this.args=args;return this}async first(){return sql.prepare(this.q).get(...this.args)||null}async run(){return sql.prepare(this.q).run(...this.args)}}
const db={prepare:q=>new Stmt(q),batch:async list=>Promise.all(list.map(s=>s.run()))};const env={DB:db,GOOGLE_CLIENT_ID:'test-client',GOOGLE_CLIENT_SECRET:'test-secret'};
const {privateKey,publicKey}=await generateKeyPair('RS256');
const token=(claims={})=>new SignJWT({nonce:'nonce',email:'test@example.com',email_verified:true,...claims}).setProtectedHeader({alg:'RS256'}).setSubject('google-subject').setIssuer('https://accounts.google.com').setAudience('test-client').setIssuedAt().setExpirationTime('5m').sign(privateKey);
const valid=await token();assert.equal((await verifyGoogleToken(valid,'test-client','nonce',publicKey)).subject,'google-subject');
await assert.rejects(()=>verifyGoogleToken(valid,'wrong-client','nonce',publicKey));await assert.rejects(()=>verifyGoogleToken(valid,'test-client','wrong-nonce',publicKey));await assert.rejects(async()=>verifyGoogleToken(await token({email_verified:false}),'test-client','nonce',publicKey));
const wrongKey=(await generateKeyPair('RS256')).publicKey;await assert.rejects(()=>verifyGoogleToken(valid,'test-client','nonce',wrongKey));
const expired=await new SignJWT({nonce:'nonce',email:'test@example.com',email_verified:true}).setProtectedHeader({alg:'RS256'}).setSubject('sub').setIssuer('https://accounts.google.com').setAudience('test-client').setIssuedAt(1).setExpirationTime(2).sign(privateKey);await assert.rejects(()=>verifyGoogleToken(expired,'test-client','nonce',publicKey));
assert(!googleEnabled({DB:db}));assert.match((await beginGoogle(new Request(SITE_ORIGIN+'/auth/google/start'),{},null)).headers.get('location'),/unavailable/);
async function flow(linkUser=null,subject='first-google',callbackUser=linkUser){
 const start=await beginGoogle(new Request(SITE_ORIGIN+'/auth/google/start'+(linkUser?'?link=1':''),{headers:{'sec-fetch-site':'same-origin'}}),env,linkUser);
 const auth=new URL(start.headers.get('location'));assert.equal(auth.searchParams.get('redirect_uri'),REDIRECT_URI);assert.equal(auth.searchParams.get('code_challenge_method'),'S256');assert.equal(auth.searchParams.get('scope'),'openid email profile');
 const browserCookie=start.headers.get('set-cookie').split(';')[0];const state=auth.searchParams.get('state');const req=new Request(REDIRECT_URI+'?state='+state+'&code=test-code',{headers:{cookie:browserCookie}});
 const fetcher=async(url,options)=>{assert.equal(url,'https://oauth2.googleapis.com/token');assert.equal(options.body.get('redirect_uri'),REDIRECT_URI);assert(options.body.get('code_verifier'));return Response.json({id_token:'verified-in-test'})};
 const verify=async(t,client,nonce)=>{assert.equal(client,'test-client');assert.equal(nonce,auth.searchParams.get('nonce'));return {subject,email:'same@example.com',name:'Test'}};
 const response=await finishGoogle(req,env,callbackUser,{fetcher,verify});return {response,req,fetcher,verify};
}
const first=await flow();assert.match(first.response.headers.get('location'),/success/);const session=first.response.headers.getSetCookie().find(c=>c.startsWith(SESSION_COOKIE+'=')).split(';')[0];assert.match(first.response.headers.getSetCookie().join(';'),/Secure; HttpOnly; SameSite=Lax/);
const user=await getGoogleUser(new Request(SITE_ORIGIN,{headers:{cookie:session}}),db);assert(user.userId.startsWith('google-'));
assert.match((await finishGoogle(first.req,env,null,{fetcher:first.fetcher,verify:first.verify})).headers.get('location'),/expired/);
const other=await flow(null,'second-google');const otherCookie=other.response.headers.getSetCookie().find(c=>c.startsWith(SESSION_COOKIE+'=')).split(';')[0];assert.notEqual((await getGoogleUser(new Request(SITE_ORIGIN,{headers:{cookie:otherCookie}}),db)).userId,user.userId);
const linked=await flow({userId:'original-chatgpt-user',provider:'chatgpt'},'linked-google');assert.match(linked.response.headers.get('location'),/linked/);const linkedCookie=linked.response.headers.getSetCookie().find(c=>c.startsWith(SESSION_COOKIE+'=')).split(';')[0];assert.equal((await getGoogleUser(new Request(SITE_ORIGIN,{headers:{cookie:linkedCookie}}),db)).userId,'original-chatgpt-user');
assert.match((await flow({userId:'attacker',provider:'chatgpt'},'linked-google')).response.headers.get('location'),/already_linked/);
assert.match((await flow({userId:'original-user',provider:'chatgpt'},'third-google',{userId:'different-user'})).response.headers.get('location'),/link_required/);
const logout=await endGoogle(new Request(SITE_ORIGIN+'/auth/logout',{headers:{cookie:session,'sec-fetch-site':'same-origin'}}),db);assert.match(logout.headers.get('location'),/signout-with-chatgpt/);assert.equal(await getGoogleUser(new Request(SITE_ORIGIN,{headers:{cookie:session}}),db),null);
const switchBack=await beginChatGPT(new Request(SITE_ORIGIN+'/auth/chatgpt/start',{headers:{cookie:linkedCookie}}),db);assert.match(switchBack.headers.get('location'),/signin-with-chatgpt/);assert.equal(await getGoogleUser(new Request(SITE_ORIGIN,{headers:{cookie:linkedCookie}}),db),null);
console.log('Passed Google auth: JWT signature/audience/nonce/expiry, disabled setup, PKCE, single-use state, separate same-email accounts, explicit linking, collision protection, account-switch rejection and session revocation.');
