/* Pure selection and snapshot logic. Individual ratings are never generated. */
(function(root){
'use strict';
const TOPICS=['Algebra','Geometry','Number Theory','Combinatorics'];
const mean=qs=>qs.length&&qs.every(q=>Number.isFinite(q.difficulty))?qs.reduce((s,q)=>s+q.difficulty,0)/qs.length:null;
const fingerprint=p=>String(p.statement||'').toLowerCase().replace(/[^a-z0-9]/g,'');
function isBritish(p){
 const appearances=[p,...(p.appearances||[]),...(p.alternateOrigins||[])];
 return /^bmo[12]?-|^fist-/i.test(p.id||'')||appearances.some(a=>typeof a==='string'?/\bBMO[12]\b|British Mathematical Olympiad|\bFIST\b/i.test(a):/\bBMO[12]\b|British Mathematical Olympiad|\bFIST\b/i.test(a.competition||'')||(/^(BMO|British Mathematical Olympiad)$/i.test(a.competition||'')&&/United Kingdom|Britain|British/i.test(a.country||p.country||'')))||(p.originCompetitions||[]).some(c=>/^BMO[12]$|British Mathematical Olympiad|^FIST$/i.test(c));
}
function settings(input={}){
 const preset=input.preset??'bmo1';
 if(!['bmo1','bmo2','custom'].includes(preset))throw Error('Choose a valid paper preset.');
 const custom=preset==='custom';
 const s={preset,questionCount:custom?(input.questionCount??6):preset==='bmo2'?4:6,
 durationMinutes:custom?(input.durationMinutes??210):210,marksPerQuestion:custom?(input.marksPerQuestion??10):10,
 minDifficulty:custom?(input.minDifficulty??4):preset==='bmo1'?2.5:1,maxDifficulty:custom?(input.maxDifficulty??7):preset==='bmo1'?7:10,
 profile:custom?(input.profile??'rising'):'template',tolerance:custom?(input.tolerance??0.5):0.5,
 topics:custom?(input.topics??TOPICS.slice()):TOPICS.slice(),topicMix:custom?(input.topicMix??'balanced'):'template',
 maxPerCountry:custom?(input.maxPerCountry??2):2,maxPerCompetition:custom?(input.maxPerCompetition??0):0,
 countries:custom?(input.countries??[]):[],minYear:custom?(input.minYear??null):null,maxYear:custom?(input.maxYear??null):null,
 excludeAdvanced:custom?(input.excludeAdvanced??true):true,allowDiagrams:custom?(input.allowDiagrams??true):true,
 avoidPrevious:input.avoidPrevious??true,avoidAttempted:input.avoidAttempted??true,requireSolutions:input.requireSolutions??false};
 const integer=(v,a,b)=>Number.isInteger(v)&&v>=a&&v<=b;
 if(!integer(s.questionCount,4,10))throw Error('Choose between 4 and 10 questions.');
 if(!integer(s.durationMinutes,15,600))throw Error('Time must be a whole number from 15 to 600 minutes.');
 if(!integer(s.marksPerQuestion,1,20))throw Error('Marks per question must be a whole number from 1 to 20.');
 if(![s.minDifficulty,s.maxDifficulty].every(v=>Number.isFinite(v)&&v>=1&&v<=10&&v*2===Math.round(v*2))||s.minDifficulty>s.maxDifficulty)throw Error('Choose an ordered difficulty range from 1 to 10 in half-point steps.');
 if(!['rising','steady','random','template'].includes(s.profile)||custom&&s.profile==='template'||![0,0.5,1].includes(s.tolerance))throw Error('Choose a valid difficulty progression and tolerance.');
 if(!Array.isArray(s.topics)||!s.topics.length||s.topics.some(t=>!TOPICS.includes(t))||new Set(s.topics).size!==s.topics.length)throw Error('Choose at least one topic, with no duplicates.');
 if(!['balanced','random','template'].includes(s.topicMix)||custom&&s.topicMix==='template')throw Error('Choose a valid topic mix.');
 if(!integer(s.maxPerCountry,0,10)||!integer(s.maxPerCompetition,0,10))throw Error('Source limits must be from 0 (unlimited) to 10.');
 if(!Array.isArray(s.countries)||s.countries.length>150||s.countries.some(c=>typeof c!=='string'||!c||c.length>150))throw Error('Choose valid source countries.');
 if([s.minYear,s.maxYear].some(v=>v!==null&&!integer(v,1900,2100))||s.minYear!==null&&s.maxYear!==null&&s.minYear>s.maxYear)throw Error('Choose an ordered source-year range from 1900 to 2100.');
 for(const k of ['excludeAdvanced','allowDiagrams','avoidPrevious','avoidAttempted','requireSolutions'])if(typeof s[k]!=='boolean')throw Error('Invalid selection toggle.');
 return s;
}
function eligible(p,britishIds=new Set(),britishPrints=new Set(),s=settings()){
 const methods=[...(p.subtopics||[]),...(p.tags||[])].join(' ');
 return p.reviewStatus==='individually-assessed'&&Number.isFinite(p.difficulty)&&p.difficulty>=s.minDifficulty&&p.difficulty<=s.maxDifficulty&&p.statement?.trim()&&TOPICS.includes(p.topic)&&!isBritish(p)&&!britishIds.has(p.id)&&!britishPrints.has(fingerprint(p))&&(!s.excludeAdvanced||!/calculus|linear algebra|projective|conics|complex numbers|matrices|determinants|eigenvalue|integrals|derivatives/i.test(methods))&&!/(?:choose|select) (?:the|one|an?) (?:correct|right) (?:answer|option)|multiple.choice/i.test(p.statement)&&s.topics.includes(p.topic)&&(!s.countries.length||s.countries.includes(p.country))&&(s.minYear===null||p.year>=s.minYear)&&(s.maxYear===null||p.year<=s.maxYear)&&(s.allowDiagrams||!/!\[[^\]]*\]\(|<img\b/i.test(p.statement))&&(!s.requireSolutions||!!(p.solution?.trim()||p.solutionUrl?.trim()));
}
function candidatePool(problems,options={}){
 const s=settings(options.settings||options),excluded=new Set(options.excludeIds||[]),british=problems.filter(isBritish),ids=new Set(british.map(p=>p.id)),prints=new Set(british.map(fingerprint));
 return problems.filter(p=>!excluded.has(p.id)&&eligible(p,ids,prints,s));
}
function shuffled(a,rng){return a.map(x=>({x,r:rng()})).sort((a,b)=>a.r-b.r).map(o=>o.x)}
function generate(problems,calibration,options={}){
 const rng=options.rng||Math.random,s=settings(options.settings||options),pool=candidatePool(problems,{settings:s,excludeIds:options.excludeIds}),n=s.questionCount;
 let templates;
 if(s.preset==='custom'){
  const targets=Array.from({length:n},(_,i)=>s.profile==='random'?null:Math.round(2*(s.profile==='steady'?(s.minDifficulty+s.maxDifficulty)/2:s.minDifficulty+(s.maxDifficulty-s.minDifficulty)*i/(n-1)))/2);
  templates=Array.from({length:24},()=>{const topics=shuffled(s.topics,rng);return {id:null,archiveYear:null,difficulties:targets,topics:s.topicMix==='balanced'?shuffled(Array.from({length:n},(_,i)=>topics[i%topics.length]),rng):Array(n).fill(null)}});
 }else{
  const c=s.preset==='bmo2'?(calibration.calibrationBmo2||calibration.bmo2):calibration.calibration||calibration.bmo1||calibration;
  if(!c?.templates?.length)throw Error('This preset’s calibration could not load. Reload the page and try again.');
  templates=shuffled(c.templates.filter(t=>t.difficulties.length===n&&t.topics.length===n),rng);
 }
 let budget=60000;
 for(const template of templates){
  const choices=template.topics.map((topic,i)=>shuffled(pool.filter(p=>(topic===null||p.topic===topic)&&(template.difficulties[i]===null||Math.abs(p.difficulty-template.difficulties[i])<=s.tolerance)),rng).sort((a,b)=>template.difficulties[i]===null?0:Math.abs(a.difficulty-template.difficulties[i])-Math.abs(b.difficulty-template.difficulties[i])));
  if(choices.some(c=>!c.length))continue;
  const order=Array.from({length:n},(_,i)=>i).sort((a,b)=>choices[a].length-choices[b].length),selected=Array(n),used=new Set(),prints=new Set(),countries=new Map(),competitions=new Map();let attempts=0;
  function pick(depth){if(depth===n)return true;if(++attempts>5000||--budget<0)return false;const i=order[depth];for(const p of choices[i]){const fp=fingerprint(p),country=p.country||'Unknown',competition=country+'|'+p.competition,c=countries.get(country)||0,k=competitions.get(competition)||0;if(used.has(p.id)||prints.has(fp)||s.maxPerCountry&&c>=s.maxPerCountry||s.maxPerCompetition&&k>=s.maxPerCompetition)continue;selected[i]=p;used.add(p.id);prints.add(fp);countries.set(country,c+1);competitions.set(competition,k+1);if(pick(depth+1))return true;used.delete(p.id);prints.delete(fp);countries.set(country,c);competitions.set(competition,k);if(budget<0||attempts>5000)break}return false}
  if(pick(0)){
   // Ascending output remains genuinely ascending even when target bands overlap.
   const slots=selected.map((p,i)=>({p,target:template.difficulties[i]}));
   if(s.profile==='rising')slots.sort((a,b)=>a.p.difficulty-b.p.difficulty);
   return {questions:slots.map(x=>x.p),rating:mean(selected),templateId:template.id,templateYear:template.archiveYear,targets:slots.map(x=>x.target),topics:slots.map(x=>x.p.topic),eligibleCount:pool.length,settings:s};
  }
 }
 throw Error(`There are not enough matching questions to complete this paper within the selection search (${pool.length} pass the basic filters). Widen the difficulty or source filters, increase the source limits, or allow earlier/attempted questions. No partial paper has been saved.`);
}
const presetOf=p=>p.version===2?p.generationSettings?.preset||'custom':'bmo1';
const label=p=>({bmo1:'BMO1',bmo2:'BMO2',custom:'Custom'}[presetOf(p)]);
function snapshot(selection,meta){const s=settings(selection.settings||{});return normalizeSaved({version:2,id:meta.id,kind:'generated',title:meta.title,createdAt:meta.createdAt,generationSettings:JSON.parse(JSON.stringify(s)),questionCount:s.questionCount,durationMinutes:s.durationMinutes,totalMarks:s.questionCount*s.marksPerQuestion,templateId:selection.templateId,templateYear:selection.templateYear,targets:selection.targets,questions:JSON.parse(JSON.stringify(selection.questions)),generatorVersion:2})}
function validateSaved(p){
 if(!p||![1,2].includes(p.version)||p.kind!=='generated'||typeof p.id!=='string'||!/^mock-[a-z0-9-]{1,100}$/i.test(p.id)||typeof p.title!=='string'||!p.title.trim()||p.title.length>160||typeof p.createdAt!=='string'||!Number.isFinite(Date.parse(p.createdAt))||!Array.isArray(p.questions))return false;
 let s;try{if(p.version===2&&(!p.generationSettings||typeof p.generationSettings!=='object'||Array.isArray(p.generationSettings)))return false;s=p.version===1?settings():settings(p.generationSettings)}catch{return false}
 if(p.questions.length!==s.questionCount||new Set(p.questions.map(q=>q?.id)).size!==s.questionCount||p.version===2&&(p.questionCount!==s.questionCount||p.durationMinutes!==s.durationMinutes||p.totalMarks!==s.questionCount*s.marksPerQuestion))return false;
 return p.questions.every(q=>q&&typeof q.id==='string'&&q.id.length>0&&q.id.length<=200&&!/[\u0000-\u001f\u007f]/.test(q.id)&&typeof q.statement==='string'&&q.statement.length>0&&q.statement.length<100000&&TOPICS.includes(q.topic)&&Number.isFinite(q.difficulty)&&q.difficulty>=1&&q.difficulty<=10&&['subtopics','tags','originCompetitions'].every(k=>q[k]===undefined||Array.isArray(q[k])&&q[k].every(v=>typeof v==='string'))&&['appearances','alternateOrigins'].every(k=>q[k]===undefined||Array.isArray(q[k])&&q[k].every(v=>typeof v==='string'||v&&typeof v==='object'))&&['sourceUrl','solutionUrl','solution','ratingReason','country','competition','solutionCredit','solutionKind'].every(k=>q[k]==null||typeof q[k]==='string')&&!isBritish(q));
}
function normalizeSaved(p){const s=p.version===1?settings():settings(p.generationSettings);return {...p,...(p.version===2?{generationSettings:s}:{}),questionCount:s.questionCount,durationMinutes:s.durationMinutes,totalMarks:s.questionCount*s.marksPerQuestion,complete:true,rating:mean(p.questions),questions:p.questions.map((q,i)=>({...q,paperNumber:i+1,marks:s.marksPerQuestion}))}}
const api={TOPICS,settings,candidatePool,presetOf,label,normalizeSaved,mean,fingerprint,isBritish,eligible,generate,snapshot,validateSaved};if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.PaperEngine=api;
})(typeof window!=='undefined'?window:globalThis);
