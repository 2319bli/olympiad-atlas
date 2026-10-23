import { env } from 'cloudflare:workers';
import { getChatGPTUser } from '../../../chatgpt-auth';
import { finishGoogle } from '../../../../server/google-auth.mjs';
export const dynamic='force-dynamic';
export async function GET(request: Request){return finishGoogle(request,env,await getChatGPTUser())}
