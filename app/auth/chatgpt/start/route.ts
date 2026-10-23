import { env } from 'cloudflare:workers';
import { beginChatGPT } from '../../../../server/google-auth.mjs';
export const dynamic='force-dynamic';
export async function GET(request: Request){return beginChatGPT(request,env.DB)}
