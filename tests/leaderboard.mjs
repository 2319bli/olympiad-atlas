import assert from 'node:assert/strict';
import fs from 'node:fs';
import { DatabaseSync } from 'node:sqlite';
import { createWorker } from '../cloudflare/worker.mjs';
import { hash } from '../server/google-auth.mjs';
const sql = new DatabaseSync(':memory:');
for (const file of fs.readdirSync('cloudflare/migrations').sort()) sql.exec(fs.readFileSync('cloudflare/migrations/' + file, 'utf8'));
sql.exec(fs.readFileSync('cloudflare/leaderboard-catalog.sql', 'utf8'));
class Statement {
  constructor(query) { this.query = query; this.args = []; }
  bind(...args) { this.args = args; return this; }
  async first() { return sql.prepare(this.query).get(...this.args) || null; }
  async all() { return { results: sql.prepare(this.query).all(...this.args) }; }
  run() { return sql.prepare(this.query).run(...this.args); }
}
const db = { prepare: q => new Statement(q), batch: async statements => {
  sql.exec('BEGIN'); try { const result = statements.map(s => s.run()); sql.exec('COMMIT'); return result; } catch (e) { sql.exec('ROLLBACK'); throw e; }
}};
const env = { DB: db, GOOGLE_CLIENT_ID: 'test', FRONTEND_ORIGIN: 'https://2319bli.github.io' };
const worker = createWorker();
const request = (path, { token, method = 'GET', data, origin = env.FRONTEND_ORIGIN } = {}) => worker.fetch(new Request('https://atlas.example' + path, {
  method, headers: { Origin: origin, ...(token ? { Authorization: 'Bearer ' + token } : {}), ...(data ? { 'Content-Type': 'application/json' } : {}) }, ...(data ? { body: JSON.stringify(data) } : {})
}), env);
const get = async (metric = 'solved', token, offset = 0) => {
  const r = await request('/api/leaderboard?metric=' + metric + '&offset=' + offset, { token }); assert.equal(r.status, 200); return r.json();
};
const alice = 'a'.repeat(64), bob = 'b'.repeat(64), carol = 'c'.repeat(64);
for (const [id, token] of [['alice', alice], ['bob', bob], ['carol', carol]]) {
  sql.prepare('INSERT INTO google_identities (subject,user_id,email,name) VALUES (?,?,?,?)').run(id, id, id+'@private.example', 'Private real name');
  sql.prepare('INSERT INTO google_sessions (token_hash,user_id,expires_at) VALUES (?,?,?)').run(await hash(token), id, Date.now()+600000);
}
const profile = (id, token, displayName, listed = true) => request('/api/leaderboard/profile', { token, method: 'POST', data: { accountId: id, displayName, listed } });
const sync = async (id, token, progress) => { const r = await request('/api/sync', { token, method: 'POST', data: { accountId: id, papers: [], progress } }); assert.equal(r.status, 200); };
const solved = { saved: false, status: 'solved' }, attempted = { saved: true, status: 'attempted' };
const bank = JSON.parse(fs.readFileSync('public/data/problems.json','utf8'));
const easy = bank.filter(p=>p.difficulty===1).slice(0,2), hard = bank.find(p=>p.difficulty===10);
assert.equal((await get()).entries.length, 0);
assert.equal((await get('solved', alice)).me.listed, false);
assert.equal((await profile('alice', null, 'Public A')).status,401);
assert.equal((await profile('alice', bob, 'Steal')).status,409);
for (const name of ['x', '<script>', 'name@example.com', '\u202eHidden', 'x'.repeat(31)]) assert.equal((await profile('alice', alice, name)).status,400);
assert.equal((await request('/api/leaderboard/profile', { token: alice, origin:'https://evil.example', method:'POST', data:{accountId:'alice',displayName:'Steal',listed:true} })).status,403);
await sync('alice', alice, Object.fromEntries(easy.map(p=>[p.id,solved])));
assert.equal((await get()).participants,0,'Private users must not be listed');
assert.equal((await get('solved',alice)).me.solved,2,'Existing solves count before opting in');
await profile('alice',alice,'Public A'); await profile('bob',bob,'Public B'); await profile('carol',carol,'Public C');
await sync('bob', bob, {[hard.id]:solved});
assert.deepEqual((await get()).entries.map(e=>e.displayName),['Public A','Public B']);
assert.deepEqual((await get('weighted')).entries.map(e=>e.displayName),['Public B','Public A']);
assert.equal((await get('weighted')).entries[0].weighted,11);
await sync('alice',alice,Object.fromEntries(easy.map(p=>[p.id,solved])));
await sync('alice',alice,{fake:{...solved,difficulty:100000},[hard.id]:attempted});
assert.equal((await get('solved',alice)).me.solved,2,'Retries, unknown questions and attempts must not inflate totals');
await sync('carol',carol,{[easy[0].id]:solved});
assert.deepEqual((await get()).entries.map(e=>e.rank),[1,2,2]);
await sync('carol',carol,{[easy[1].id]:solved});
assert.deepEqual((await get()).entries.map(e=>e.rank),[1,1,3]);
assert.deepEqual((await get('weighted')).entries.map(e=>e.rank),[1,2,2]);
const before = (await get('solved',alice)).me.solved;
sql.prepare('INSERT INTO account_progress (user_id,problem_id,saved,status,updated_at) VALUES (?,?,?,?,?)').run('alice','irmo-1990-2',0,'solved',Date.now());
await sync('alice',alice,{'fist-1982-q2':solved});
assert.equal((await get('solved',alice)).me.solved,before+1,'Aliases count only once');
await sync('alice',alice,{'fist-1982-q2':attempted});
assert.equal((await get('solved',alice)).me.solved,before,'Stale aliases must not restore a corrected solve');
const synced=await request('/api/sync',{token:alice}).then(r=>r.json());
assert.equal(synced.progress['fist-1982-q2'].status,'attempted'); assert(!synced.progress['irmo-1990-2']);
await sync('alice',alice,{'irmo-1990-2':solved});
assert.equal((await get('solved',alice)).me.solved,before+1,'Retired IDs normalize on new syncs');
await profile('alice',alice,'Renamed solver');
assert.equal((await get('solved',alice)).me.displayName,'Renamed solver');
await profile('alice',alice,'Renamed solver',false);
assert(!(await get()).entries.some(e=>e.displayName==='Renamed solver'));
assert.equal((await get('solved',alice)).me.solved,before+1,'Leaving retains private progress');
const publicJson = JSON.stringify(await get());
assert(!/private.example|Private real name|user_id|token_hash|subject/.test(publicJson));
assert.equal((await get('solved',bob)).entries.filter(e=>e.isYou).length,1);
assert((await get()).entries.every(e=>!e.isYou));
for (let i=0;i<55;i++) {
 const id='extra-'+i;
 sql.prepare('INSERT INTO atlas_leaderboard_profiles VALUES (?,?,?,?)').run(id,'Solver '+String(i).padStart(2,'0'),1,Date.now());
 sql.prepare('INSERT INTO account_progress VALUES (?,?,?,?,?)').run(id,easy[0].id,0,'solved',Date.now());
}
const page1=await get(),page2=await get('solved',bob,50);
assert.equal(page1.entries.length,50);assert(page1.hasMore);assert.equal(page2.entries.length,7);assert(!page2.hasMore);
assert.equal(page2.me.rank,2,'Personal rank remains available off-page');
assert.equal(new Set([...page1.entries,...page2.entries].map(e=>e.displayName)).size,57);
assert.equal(page2.entries[0].rank,2,'Ties span page boundaries');
assert.equal((await request('/api/leaderboard?metric=evil')).status,400);
assert.equal((await request('/api/leaderboard?offset=-1')).status,400);
assert.equal((await request('/api/leaderboard?offset=0%20OR%201')).status,400);
assert.equal((await request('/api/leaderboard?metric=solved')).headers.get('access-control-allow-origin'),env.FRONTEND_ORIGIN);
console.log('Passed leaderboards: distinct solves, retry idempotency, aliases and corrections, trusted weights, both rankings, ties, pagination, profile privacy, authentication and CORS.');
