import assert from 'node:assert/strict';
import fs from 'node:fs';
import { DatabaseSync } from 'node:sqlite';
import { SignJWT, generateKeyPair } from 'jose';
import { createWorker } from '../cloudflare/worker.mjs';
import { verifyGoogleToken } from '../server/google-auth.mjs';

const sql = new DatabaseSync(':memory:');
for (const file of fs.readdirSync('cloudflare/migrations').sort()) sql.exec(fs.readFileSync('cloudflare/migrations/' + file, 'utf8'));
class Statement {
  constructor(query) { this.query = query; this.args = []; }
  bind(...args) { this.args = args; return this; }
  async first() { return sql.prepare(this.query).get(...this.args) || null; }
  async all() { return { results: sql.prepare(this.query).all(...this.args) }; }
  async run() { return sql.prepare(this.query).run(...this.args); }
}
const db = { prepare: q => new Statement(q), batch: statements => Promise.all(statements.map(s => s.run())) };
const env = { DB: db, GOOGLE_CLIENT_ID: 'atlas-test-client', FRONTEND_ORIGIN: 'https://2319bli.github.io' };
const { privateKey, publicKey } = await generateKeyPair('RS256');
const worker = createWorker((token, client, nonce) => verifyGoogleToken(token, client, nonce, publicKey));
const request = (path, { origin = env.FRONTEND_ORIGIN, token, method = 'GET', data, headers = {} } = {}, vars = env) => worker.fetch(new Request('https://atlas-api.example' + path, {
  method, headers: { ...(origin ? { Origin: origin } : {}), ...(token ? { Authorization: 'Bearer ' + token } : {}), ...(data ? { 'Content-Type': 'application/json' } : {}), ...headers },
  ...(data ? { body: JSON.stringify(data) } : {})
}), vars);
const jwt = (nonce, subject = 'alice', overrides = {}) => new SignJWT({ email: 'same@example.com', email_verified: true, name: 'Test', nonce, ...overrides })
  .setProtectedHeader({ alg: 'RS256' }).setSubject(subject).setIssuer('https://accounts.google.com').setAudience(env.GOOGLE_CLIENT_ID).setIssuedAt().setExpirationTime('5m').sign(privateKey);

assert.equal((await request('/api/account', { origin: 'https://evil.example' })).status, 403);
assert.equal((await request('/api/account', { origin: null })).status, 403);
assert.equal((await request('/api/account', { headers: { 'oai-authenticated-user-id': 'attacker', 'oai-authenticated-user-email': 'test@example.com' } }).then(r => r.json())).user, null);
assert.equal((await request('/api/sync')).status, 401);
assert.equal((await request('/api/account', { token: 'f'.repeat(64) }).then(r=>r.json())).sessionExpired, true);
const preflight = await request('/api/sync', { method: 'OPTIONS', headers: { 'Access-Control-Request-Method': 'POST', 'Access-Control-Request-Headers': 'authorization,content-type' } });
assert.equal(preflight.status, 204); assert.equal(preflight.headers.get('access-control-allow-origin'), env.FRONTEND_ORIGIN);
assert.equal(preflight.headers.get('access-control-allow-credentials'), null);
assert.equal((await request('/api/sync', { method: 'OPTIONS', headers: { 'Access-Control-Request-Method': 'DELETE' } })).status, 403);
assert.equal((await request('/auth/challenge', { method: 'POST' }, { ...env, GOOGLE_CLIENT_ID: '' })).status, 503);

const challenge = await request('/auth/challenge', { method: 'POST' }).then(r => r.json());
const bad = await jwt('wrong-nonce');
assert.equal((await request('/auth/google/session', { method: 'POST', data: { nonce: challenge.nonce, credential: bad } })).status, 401);
const credential = await jwt(challenge.nonce);
const signIn = await request('/auth/google/session', { method: 'POST', data: { nonce: challenge.nonce, credential } });
assert.equal(signIn.status, 200);
const { token } = await signIn.json(); assert.match(token, /^[a-f0-9]{64}$/);
assert.equal(signIn.headers.get('set-cookie'), null);
assert.equal(sql.prepare('SELECT token_hash FROM google_sessions').get().token_hash === token, false);
assert.equal((await request('/auth/google/session', { method: 'POST', data: { nonce: challenge.nonce, credential } })).status, 401);
const alice = await request('/api/account', { token }).then(r => r.json());
assert.equal(alice.user.provider, 'google');
const save = await request('/api/sync', { token, method: 'POST', data: { accountId: alice.user.id, papers: [], progress: { example: { saved: true, status: 'solved' } } }, headers: { 'Sec-Fetch-Site': 'cross-site' } });
assert.equal(save.status, 200);
assert.equal((await request('/api/sync', { token }).then(r => r.json())).progress.example.status, 'solved');
assert.equal((await request('/api/sync', { token, origin: 'https://evil.example', method: 'POST', data: { accountId: alice.user.id, papers: [], progress: {} } })).status, 403);
assert.equal((await request('/api/sync', { token, method: 'POST', data: { accountId: 'someone-else', papers: [], progress: {} } })).status, 409);
const nextChallenge = await request('/auth/challenge', { method: 'POST' }).then(r => r.json());
const bob = await request('/auth/google/session', { method: 'POST', data: { nonce: nextChallenge.nonce, credential: await jwt(nextChallenge.nonce, 'bob') } }).then(r => r.json());
assert.notEqual((await request('/api/account', { token: bob.token }).then(r => r.json())).user.id, alice.user.id);
assert.deepEqual((await request('/api/sync', { token: bob.token }).then(r => r.json())).progress, {});
const expired = await request('/auth/challenge', { method: 'POST' }).then(r => r.json());
sql.exec('UPDATE atlas_login_challenges SET expires_at = 0');
assert.equal((await request('/auth/google/session', { method: 'POST', data: { nonce: expired.nonce, credential: await jwt(expired.nonce) } })).status, 401);
assert.equal((await request('/auth/logout', { token, method: 'POST' })).status, 200);
assert.equal((await request('/api/account', { token }).then(r=>r.json())).sessionExpired, true);
assert.equal((await request('/api/account', { token: bob.token })).status, 200);
sql.exec('UPDATE google_sessions SET expires_at = 0');
assert.equal((await request('/api/account', { token: bob.token }).then(r=>r.json())).sessionExpired, true);
console.log('Passed standalone backend: CORS, forged identity rejection, Google signatures/nonces, replay/expiry, hashed bearer sessions, cross-origin sync, account isolation and logout.');
