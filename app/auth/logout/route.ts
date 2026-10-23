import { env } from 'cloudflare:workers';
import { endGoogle } from '../../../server/google-auth.mjs';
export const dynamic='force-dynamic';
export async function GET(request: Request){return endGoogle(request,env.DB)}
