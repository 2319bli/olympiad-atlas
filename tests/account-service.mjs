import assert from 'node:assert/strict';
import { DatabaseSync } from 'node:sqlite';
import fs from 'node:fs';
import vm from 'node:vm';
import { handleSync } from '../server/account-service.mjs';
const sql=new DatabaseSync(':memory:');
for(const file of fs.readdirSync('drizzle').filter(f=>f.endsWith('.sql')).sort())sql.exec(fs.readFileSync('drizzle/'+file,'utf8'));
class Stmt{constructor(query){this.query=query}bind(...args){this.args=args;return this}async all(){return {results:sql.prepare(this.query).all(...this.args)}}run(){return sql.prepare(this.query).run(...this.args)}}
const db={prepare:q=>new Stmt(q),batch:async statements=>{sql.exec('BEGIN');try{const r=statements.map(s=>s.run());sql.exec('COMMIT');return r}catch(e){sql.exec('ROLLBACK');throw e}}};
const a={userId:'alice'},b={userId:'bob'},origin='https://atlas.example';
const get=u=>handleSync(new Request(origin+'/api/sync'),db,u);
const post=(u,data,otherOrigin=origin)=>handleSync(new Request(origin+'/api/sync',{method:'POST',headers:{origin:otherOrigin,'content-type':'application/json'},body:JSON.stringify({accountId:u?.userId,papers:[],progress:{},...data})}),db,u);
assert.equal((await get(null)).status,401);assert.equal((await post(null,{})).status,401);
assert.equal((await post(a,{},'https://evil.example')).status,403);
assert.equal((await post(b,{accountId:'alice'})).status,409);
const context={module:{exports:{}}};vm.runInNewContext(fs.readFileSync('public/paper-engine.js','utf8'),context);const E=context.module.exports;
const all=JSON.parse(fs.readFileSync('public/data/problems.json')),catalog=JSON.parse(fs.readFileSync('public/data/papers.json'));
const paper=E.snapshot(E.generate(all,catalog.calibration),{id:'mock-account-test',title:'Account test',createdAt:new Date().toISOString()});
assert.equal((await post(a,{papers:[paper],progress:{'problem-1':{saved:true,status:'solved'}}})).status,200);
let alice=await (await get(a)).json(),bob=await (await get(b)).json();assert.equal(alice.papers.length,1);assert.equal(Object.keys(bob.progress).length,0);assert.equal(bob.papers.length,0);
assert.equal((await post(b,{papers:[{...paper,title:'Bob version'}],progress:{'problem-1':{saved:false,status:'attempted'}}})).status,200);
assert.equal((await (await get(a)).json()).papers[0].title,'Account test');assert.equal((await (await get(b)).json()).papers[0].title,'Bob version');
await post(a,{papers:[{...paper,title:'Retry must not replace snapshot'}]});assert.equal((await (await get(a)).json()).papers[0].title,'Account test');
await Promise.all([post(a,{progress:{'problem-2':{saved:false,status:'attempted'}}}),post(a,{progress:{'problem-3':{saved:true,status:'new'}}})]);
alice=await (await get(a)).json();assert.equal(Object.keys(alice.progress).length,3);assert.equal(alice.progress['problem-1'].status,'solved');
assert.equal((await post(a,{papers:[{...paper,questions:[]}]})).status,400);
assert.equal((await post(a,{progress:{"bad\u0000id":{saved:true,status:'new'}}})).status,400);
assert.equal((await post(a,{progress:{'problem-1':{saved:true,status:'nonsense'}}})).status,400);
assert.equal((await post(a,{papers:[],padding:'x'.repeat(2100000)})).status,413);
assert.equal((await post(a,{progress:{'baltic-lithuania-2026-Grades-9–10-1':{saved:true,status:'attempted'},'ve-ojm-final-Year 3-2023-3':{saved:false,status:'solved'}}})).status,200);
assert.equal((await get(a)).headers.get('cache-control'),'private, no-store');
console.log('Passed account API: authentication, ownership isolation, account-switch rejection, CSRF, immutable/idempotent papers, record-level progress merging and validation.');
// Both new formats and legacy six-question snapshots survive server normalization.
for(const [preset,count] of [['bmo2',4],['custom',10]]){
 const selection=E.generate(all,catalog,{preset,questionCount:count,profile:'random',maxPerCountry:0});
 const p=E.snapshot(selection,{id:'mock-sync-'+preset,title:preset,createdAt:new Date().toISOString()});
 assert.equal((await post(a,{papers:[p]})).status,200);
 const roundtrip=(await (await get(a)).json()).papers.find(x=>x.id===p.id);
 assert.equal(roundtrip.questionCount,count);assert.equal(roundtrip.questions.length,count);assert.equal(roundtrip.totalMarks,count*10);assert.equal(roundtrip.generationSettings.preset,preset);
 assert.equal((await post(a,{papers:[{...p,questionCount:count+1}]})).status,400);
}
const legacy={...paper,id:'mock-sync-legacy',version:1};delete legacy.generationSettings;
assert.equal((await post(a,{papers:[legacy]})).status,200);
assert.equal((await (await get(a)).json()).papers.find(x=>x.id===legacy.id).questionCount,6);
console.log('Passed account round trips for BMO2, ten-question custom and legacy papers.');
