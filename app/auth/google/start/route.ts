import { env } from 'cloudflare:workers';
import { getAtlasUser } from '../../../atlas-auth';
import { beginGoogle } from '../../../../server/google-auth.mjs';
export const dynamic='force-dynamic';
export async function GET(request: Request){return beginGoogle(request,env,await getAtlasUser(request))}
