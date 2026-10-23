/* Pure selection and snapshot logic; ratings are retained, never generated. */
(function(root){
'use strict';
const mean=questions=>questions.length&&questions.every(q=>Number.isFinite(q.difficulty))?questions.reduce((n,q)=>n+q.difficulty,0)/questions.length:null;
const fingerprint=p=>String(p.statement||'').toLowerCase().replace(/[^a-z0-9]/g,'');
function isBritish(p){
 const appearances=[p,...(p.appearances||[]),...(p.alternateOrigins||[])];
 return /^bmo[12]?-|^fist-/i.test(p.id||'')||appearances.some(a=>typeof a==='string'?/\bBMO[12]\b|British Mathematical Olympiad|\bFIST\b/i.test(a):/\bBMO[12]\b|British Mathematical Olympiad|\bFIST\b/i.test(a.competition||'')||(/^(BMO|British Mathematical Olympiad)$/i.test(a.competition||'')&&/United Kingdom|Britain|British/i.test(a.country||p.country||'')))||(p.originCompetitions||[]).some(c=>/^BMO[12]$|British Mathematical Olympiad|^FIST$/i.test(c));
}
function eligible(p,britishIds=new Set(),britishPrints=new Set()){
 const methods=[...(p.subtopics||[]),...(p.tags||[])].join(' ');
 return p.reviewStatus==='individually-assessed'&&Number.isFinite(p.difficulty)&&p.difficulty>=2.5&&p.difficulty<=7&&p.statement?.trim()&&!isBritish(p)&&!britishIds.has(p.id)&&!britishPrints.has(fingerprint(p))&&!/calculus|linear algebra|projective|conics|complex numbers|matrices|determinants|eigenvalue|integrals|derivatives/i.test(methods)&&!/(?:choose|select) (?:the|one|an?) (?:correct|right) (?:answer|option)|multiple.choice/i.test(p.statement);
}
function shuffled(a,rng){return a.map(x=>({x,r:rng()})).sort((a,b)=>a.r-b.r).map(o=>o.x)}
function generate(problems,calibration,options={}){
 const rng=options.rng||Math.random,excluded=new Set(options.excludeIds||[]),british=problems.filter(isBritish),britishIds=new Set(british.map(p=>p.id)),britishPrints=new Set(british.map(fingerprint));
 const pool=problems.filter(p=>eligible(p,britishIds,britishPrints)&&!excluded.has(p.id)&&(!options.requireSolutions||p.solution||p.solutionUrl));
 const templates=shuffled(calibration.templates.filter(t=>t.difficulties.length===6&&t.topics.length===6),rng);
 for(const template of templates){
  const choices=template.topics.map((topic,i)=>shuffled(pool.filter(p=>p.topic===topic&&Math.abs(p.difficulty-template.difficulties[i])<=0.5),rng).sort((a,b)=>Math.abs(a.difficulty-template.difficulties[i])-Math.abs(b.difficulty-template.difficulties[i])));
  const selected=[],used=new Set(),prints=new Set(),countries=new Map();let attempts=0;
  function pick(i){if(i===6)return true;if(++attempts>5000)return false;for(const p of choices[i]){const fp=fingerprint(p),count=countries.get(p.country)||0;if(used.has(p.id)||prints.has(fp)||count>=2)continue;selected.push(p);used.add(p.id);prints.add(fp);countries.set(p.country,count+1);if(pick(i+1))return true;selected.pop();used.delete(p.id);prints.delete(fp);countries.set(p.country,count)}return false}
  if(pick(0))return {questions:selected,rating:mean(selected),templateId:template.id,templateYear:template.archiveYear,targets:template.difficulties,topics:template.topics,eligibleCount:pool.length};
 }
 throw Error('There are not enough unused matching questions for a complete BMO1 mock. Allow questions from earlier mocks or attempted questions, or turn off the solution requirement. No partial paper has been saved.');
}
function snapshot(selection,meta){return {version:1,id:meta.id,kind:'generated',title:meta.title,createdAt:meta.createdAt,questionCount:6,durationMinutes:210,totalMarks:60,complete:true,rating:mean(selection.questions),templateId:selection.templateId,templateYear:selection.templateYear,targets:selection.targets,questions:selection.questions.map((p,i)=>({...JSON.parse(JSON.stringify(p)),paperNumber:i+1,marks:10})),generatorVersion:1}}
function validateSaved(p){return p&&p.version===1&&p.kind==='generated'&&typeof p.id==='string'&&/^mock-[a-z0-9-]+$/i.test(p.id)&&typeof p.title==='string'&&p.title.length<=160&&typeof p.createdAt==='string'&&Number.isFinite(Date.parse(p.createdAt))&&Array.isArray(p.questions)&&p.questions.length===6&&new Set(p.questions.map(q=>q?.id)).size===6&&p.questions.every(q=>q&&typeof q.id==='string'&&typeof q.statement==='string'&&q.statement.length>0&&q.statement.length<100000&&['Algebra','Geometry','Number Theory','Combinatorics'].includes(q.topic)&&Number.isFinite(q.difficulty)&&q.difficulty>=1&&q.difficulty<=10&&['subtopics','tags','originCompetitions'].every(k=>q[k]===undefined||Array.isArray(q[k])&&q[k].every(v=>typeof v==='string'))&&['appearances','alternateOrigins'].every(k=>q[k]===undefined||Array.isArray(q[k])&&q[k].every(v=>typeof v==='string'||v&&typeof v==='object'))&&['sourceUrl','solutionUrl','solution','ratingReason','country','competition','solutionCredit','solutionKind'].every(k=>q[k]==null||typeof q[k]==='string')&&!isBritish(q))}
function normalizeSaved(p){return {...p,questionCount:6,durationMinutes:210,totalMarks:60,complete:true,rating:mean(p.questions),questions:p.questions.map((q,i)=>({...q,paperNumber:i+1,marks:10}))}}
const api={normalizeSaved,mean,fingerprint,isBritish,eligible,generate,snapshot,validateSaved};if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.PaperEngine=api;
})(typeof window!=='undefined'?window:globalThis);
