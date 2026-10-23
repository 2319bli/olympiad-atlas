import { env } from 'cloudflare:workers';
import { getAtlasUser } from '../../atlas-auth';
import { googleEnabled } from '../../../server/google-auth.mjs';
export const dynamic = 'force-dynamic';
export async function GET(request: Request){
 const user=await getAtlasUser(request);
 const linked=user&&env.DB?await env.DB.prepare('SELECT email FROM google_identities WHERE user_id = ?').bind(user.userId).first<{email:string}>():null;
 return Response.json({user:user?{id:user.userId,name:user.displayName,email:user.email,provider:user.provider}:null,googleEnabled:googleEnabled(env),googleLinkedEmail:linked?.email||null,googleSignInUrl:'/auth/google/start',googleLinkUrl:'/auth/google/start?link=1',signInUrl:'/auth/chatgpt/start',signOutUrl:'/auth/logout'},{headers:{'Cache-Control':'private, no-store','Vary':'Cookie'}});
}
