import { hash, verifyGoogleToken } from '../server/google-auth.mjs';
import { handleSync } from '../server/account-service.mjs';

const random = () => Array.from(crypto.getRandomValues(new Uint8Array(32)), b => b.toString(16).padStart(2, '0')).join('');
const validToken = value => typeof value === 'string' && /^[a-f0-9]{64}$/.test(value);
const json = (body, status = 200) => Response.json(body, { status, headers: { 'Cache-Control': 'private, no-store' } });
const enabled = env => Boolean(env.DB && env.GOOGLE_CLIENT_ID);

async function body(request) {
  if (!request.headers.get('content-type')?.startsWith('application/json')) throw new Error('JSON required');
  const reader = request.body?.getReader();
  if (!reader) throw new Error('Missing body');
  let length = 0; const chunks = [];
  for (;;) {
    const { done, value } = await reader.read(); if (done) break;
    length += value.length;
    if (length > 20000) { await reader.cancel(); throw new Error('Body too large'); }
    chunks.push(value);
  }
  const bytes = new Uint8Array(length); let offset = 0;
  for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
  return JSON.parse(new TextDecoder().decode(bytes));
}

async function identity(request, db) {
  const token = request.headers.get('authorization')?.match(/^Bearer ([a-f0-9]{64})$/)?.[1];
  if (!token || !db) return null;
  const row = await db.prepare('SELECT s.user_id, i.email, i.name FROM google_sessions s JOIN google_identities i ON i.user_id = s.user_id WHERE s.token_hash = ? AND s.expires_at > ?')
    .bind(await hash(token), Date.now()).first();
  return row ? { userId: row.user_id, email: row.email, displayName: row.name, provider: 'google' } : null;
}

// Injection is only for local tests; deployed requests always use Google's public keys.
export function createWorker(verify = verifyGoogleToken) {
  return {
    async fetch(request, env) {
      const path = new URL(request.url).pathname;
      if (path === '/health' && request.method === 'GET') return json({ ok: true, googleEnabled: enabled(env) });
      const origin = request.headers.get('origin');
      if (!env.FRONTEND_ORIGIN || origin !== env.FRONTEND_ORIGIN) return json({ error: 'Origin not allowed.' }, 403);
      const cors = response => {
        const headers = new Headers(response.headers);
        headers.set('Access-Control-Allow-Origin', origin);
        headers.set('Vary', 'Origin');
        headers.set('Cache-Control', 'private, no-store');
        headers.set('X-Content-Type-Options', 'nosniff');
        return new Response(response.body, { status: response.status, headers });
      };
      if (request.method === 'OPTIONS') {
        const method = request.headers.get('access-control-request-method');
        const headers = (request.headers.get('access-control-request-headers') || '').toLowerCase().split(',').map(s => s.trim()).filter(Boolean);
        if (!['GET', 'POST'].includes(method) || headers.some(h => !['authorization', 'content-type'].includes(h))) return cors(json({ error: 'Preflight not allowed.' }, 403));
        return cors(new Response(null, { status: 204, headers: { 'Access-Control-Allow-Methods': 'GET, POST', 'Access-Control-Allow-Headers': 'Authorization, Content-Type' } }));
      }
      try {
        if (path === '/auth/challenge' && request.method === 'POST') {
          if (!enabled(env)) return cors(json({ error: 'Google sign-in is awaiting activation.' }, 503));
          const nonce = random(), now = Date.now();
          await env.DB.batch([
            env.DB.prepare('DELETE FROM atlas_login_challenges WHERE expires_at < ?').bind(now),
            env.DB.prepare('DELETE FROM google_sessions WHERE expires_at < ?').bind(now),
            env.DB.prepare('INSERT INTO atlas_login_challenges (nonce_hash, expires_at) VALUES (?, ?)').bind(await hash(nonce), now + 600000)
          ]);
          return cors(json({ nonce, clientId: env.GOOGLE_CLIENT_ID }));
        }
        if (path === '/auth/google/session' && request.method === 'POST') {
          if (!enabled(env)) return cors(json({ error: 'Google sign-in is awaiting activation.' }, 503));
          let data; try { data = await body(request); } catch { return cors(json({ error: 'Invalid sign-in request.' }, 400)); }
          if (!validToken(data?.nonce) || typeof data.credential !== 'string' || data.credential.length > 16000) return cors(json({ error: 'Invalid sign-in request.' }, 400));
          let google;
          try { google = await verify(data.credential, env.GOOGLE_CLIENT_ID, data.nonce); } catch { return cors(json({ error: 'Google sign-in could not be verified.' }, 401)); }
          const challenge = await env.DB.prepare('DELETE FROM atlas_login_challenges WHERE nonce_hash = ? AND expires_at > ? RETURNING nonce_hash').bind(await hash(data.nonce), Date.now()).first();
          if (!challenge) return cors(json({ error: 'Sign-in expired. Please try again.' }, 401));
          const userId = 'google-' + await hash(google.subject);
          await env.DB.prepare('INSERT INTO google_identities (subject, user_id, email, name) VALUES (?, ?, ?, ?) ON CONFLICT(subject) DO UPDATE SET email=excluded.email, name=excluded.name')
            .bind(google.subject, userId, google.email, google.name).run();
          // Retain a previously linked ID if this is a migrated database. Never merge by email.
          const user = await env.DB.prepare('SELECT user_id FROM google_identities WHERE subject = ?').bind(google.subject).first();
          const token = random(), expiresAt = Date.now() + 30 * 86400000;
          await env.DB.prepare('INSERT INTO google_sessions (token_hash, user_id, expires_at) VALUES (?, ?, ?)').bind(await hash(token), user.user_id, expiresAt).run();
          return cors(json({ token, expiresAt }));
        }
        const user = await identity(request, env.DB);
        if (path === '/api/account' && request.method === 'GET') {
          return cors(json({ sessionExpired: request.headers.has('authorization') && !user, user: user ? { id: user.userId, name: user.displayName, email: user.email, provider: 'google' } : null, googleEnabled: enabled(env), googleClientId: env.GOOGLE_CLIENT_ID || null, signInUrl: null, signOutUrl: null }));
        }
        if (path === '/auth/logout' && request.method === 'POST') {
          const token = request.headers.get('authorization')?.slice(7);
          if (validToken(token) && env.DB) await env.DB.prepare('DELETE FROM google_sessions WHERE token_hash = ?').bind(await hash(token)).run();
          return cors(json({ ok: true }));
        }
        if (path === '/api/sync') return cors(await handleSync(request, env.DB, user, { allowedOrigin: env.FRONTEND_ORIGIN, maxRecords: 40 }));
        return cors(json({ error: 'Not found.' }, 404));
      } catch { return cors(json({ error: 'Account service is temporarily unavailable. Your browser data is retained.' }, 503)); }
    }
  };
}
export default createWorker();
