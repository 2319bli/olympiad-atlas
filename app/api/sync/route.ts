import { env } from 'cloudflare:workers';
import { getAtlasUser } from '../../atlas-auth';
import { handleSync } from '../../../server/account-service.mjs';
export const dynamic = 'force-dynamic';
export async function GET(request: Request){return handleSync(request,env.DB,await getAtlasUser(request))}
export async function POST(request: Request){return handleSync(request,env.DB,await getAtlasUser(request))}
