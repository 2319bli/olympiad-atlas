import '../public/paper-engine.js';
import { questionAliases } from './question-aliases.mjs';
function canonicalProgress(progress) {
 const result = Object.fromEntries(Object.entries(progress).filter(([id]) => !questionAliases[id]));
 for (const [id, value] of Object.entries(progress)) { const target = questionAliases[id]; if (target && !Object.hasOwn(result, target)) result[target] = value; }
 return result;
}
const PaperEngine=globalThis.PaperEngine;
const NO_CACHE={'Content-Type':'application/json','Cache-Control':'private, no-store','Vary':'Cookie'};
const reply=(data,status=200)=>new Response(JSON.stringify(data),{status,headers:NO_CACHE});
const object=v=>v&&typeof v==='object'&&!Array.isArray(v);
const validId=v=>typeof v==='string'&&v.length>0&&v.length<=200&&!/[\u0000-\u001f\u007f]/.test(v)&&!['__proto__','constructor','prototype'].includes(v);
export function validPaper(p){return object(p)&&PaperEngine.validateSaved(p)&&p.questions.every(q=>validId(q.id))}
export function normalizePaper(p){return PaperEngine.normalizeSaved(p)}
export async function handleSync(request,db,user,{allowedOrigin=null,maxRecords=520}={}){
 if(!user?.userId)return reply({error:'Sign in to sync your account.'},401);
 if(!db)return reply({error:'Account storage is temporarily unavailable.'},503);
 const uid=user.userId;
 try{
  if(request.method==='GET'){
   const [papers,progress]=await Promise.all([
    db.prepare('SELECT payload FROM account_papers WHERE user_id = ? ORDER BY created_at, paper_id').bind(uid).all(),
    db.prepare('SELECT problem_id, saved, status FROM account_progress WHERE user_id = ?').bind(uid).all()
   ]);
   return reply({version:1,papers:papers.results.map(p=>JSON.parse(p.payload)),progress:canonicalProgress(Object.fromEntries(progress.results.map(p=>[p.problem_id,{saved:!!p.saved,status:p.status}])))});
  }
  if(request.method!=='POST')return reply({error:'Method not allowed.'},405);
  const origin=request.headers.get('origin'),url=new URL(request.url);
  if(!origin||origin!==(allowedOrigin||url.origin)||!allowedOrigin&&request.headers.get('sec-fetch-site')==='cross-site')return reply({error:'This request must come from the Atlas site.'},403);
  if(!request.headers.get('content-type')?.startsWith('application/json'))return reply({error:'JSON is required.'},415);
  const max=2*1024*1024;
  if(Number(request.headers.get('content-length')||0)>max)return reply({error:'Sync request is too large.'},413);
  // Bound streamed requests as well as Content-Length.
  const reader=request.body?.getReader();let size=0,chunks=[];
  if(reader)for(;;){const {done,value}=await reader.read();if(done)break;size+=value.length;if(size>max){await reader.cancel();return reply({error:'Sync request is too large.'},413)}chunks.push(value)}
  const bytes=new Uint8Array(size);let offset=0;for(const c of chunks){bytes.set(c,offset);offset+=c.length}
  let data;try{data=JSON.parse(new TextDecoder().decode(bytes))}catch{return reply({error:'Invalid JSON.'},400)}
  if(data?.accountId!==uid)return reply({error:'Your signed-in account changed. Reload before syncing.'},409);
  if(!object(data)||!Array.isArray(data.papers)||data.papers.length>20||!object(data.progress)||Object.keys(data.progress).length>500||!data.papers.every(validPaper))return reply({error:'Invalid paper or sync batch.'},400);
  if(data.papers.length+Object.keys(data.progress).length>maxRecords)return reply({error:'Sync batch is too large. Please use smaller batches.'},400);
  if(!Object.entries(data.progress).every(([id,p])=>validId(id)&&object(p)&&typeof p.saved==='boolean'&&['new','attempted','solved'].includes(p.status)))return reply({error:'Invalid practice progress.'},400);
  const now=Date.now(),statements=[];
  for(const p of data.papers)statements.push(db.prepare('INSERT INTO account_papers (user_id, paper_id, payload, created_at) VALUES (?, ?, ?, ?) ON CONFLICT(user_id, paper_id) DO NOTHING').bind(uid,p.id,JSON.stringify(normalizePaper(p)),now));
  for(const [id,p]of Object.entries(canonicalProgress(data.progress)))statements.push(db.prepare('INSERT INTO account_progress (user_id, problem_id, saved, status, updated_at) VALUES (?, ?, ?, ?, ?) ON CONFLICT(user_id, problem_id) DO UPDATE SET saved=excluded.saved, status=excluded.status, updated_at=excluded.updated_at').bind(uid,id,p.saved?1:0,p.status,now));
  // Each retry is idempotent; a partial infrastructure failure can safely be retried.
  for(let i=0;i<statements.length;i+=100)await db.batch(statements.slice(i,i+100));
  return reply({ok:true,syncedAt:new Date(now).toISOString()});
 }catch{return reply({error:'Sync failed. Your browser copy has been retained; please try again.'},503)}
}
