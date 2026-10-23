import { env } from 'cloudflare:workers';
import { getChatGPTUser } from './chatgpt-auth';
import { cookie, SESSION_COOKIE, getGoogleUser } from '../server/google-auth.mjs';
export async function getAtlasUser(request: Request){
 if(cookie(request,SESSION_COOKIE))return getGoogleUser(request,env.DB);
 const user=await getChatGPTUser();return user?{...user,provider:'chatgpt'}:null;
}
