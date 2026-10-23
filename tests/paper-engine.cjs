const assert=require('node:assert/strict'),fs=require('node:fs');
const vm=require('node:vm');const context={module:{exports:{}}};vm.runInNewContext(fs.readFileSync('public/paper-engine.js','utf8'),context);const E=context.module.exports,problems=JSON.parse(fs.readFileSync('public/data/problems.json')),catalog=JSON.parse(fs.readFileSync('public/data/papers.json'));
let seed=4181;const rng=()=>((seed=(Math.imul(1664525,seed)+1013904223)>>>0)/4294967296);
for(let n=0;n<300;n++){
 const out=E.generate(problems,catalog.calibration,{rng,requireSolutions:true});
 assert.equal(out.questions.length,6);assert.equal(new Set(out.questions.map(q=>q.id)).size,6);
 const counts={};out.questions.forEach((q,i)=>{assert(!E.isBritish(q));assert.equal(q.topic,out.topics[i]);assert(Math.abs(q.difficulty-out.targets[i])<=.5);assert(q.solution||q.solutionUrl);counts[q.country]=(counts[q.country]||0)+1});assert(Math.max(...Object.values(counts))<=2);
 assert.equal(out.rating,out.questions.reduce((s,q)=>s+q.difficulty,0)/6);
}
let excluded=[];for(let n=0;n<25;n++){const s=E.generate(problems,catalog.calibration,{excludeIds:excluded,rng});for(const q of s.questions)assert(!excluded.includes(q.id));excluded.push(...s.questions.map(q=>q.id))}
assert.throws(()=>E.generate(problems,catalog.calibration,{excludeIds:problems.map(q=>q.id),rng}),/not enough/);
assert(E.isBritish({id:'other',country:'Canada',competition:'CMO',appearances:[{competition:'BMO1',country:'United Kingdom'}]}));
assert(!E.isBritish({id:'bmo_2020_abc',competition:'BMO',country:'Balkan Olympiad'}));
const s=E.generate(problems,catalog.calibration,{rng}),p=E.snapshot(s,{id:'mock-test',title:'Test paper',createdAt:new Date().toISOString()});assert(E.validateSaved(p));const original=p.questions[0].difficulty;s.questions[0]={...s.questions[0],difficulty:10};assert.equal(p.questions[0].difficulty,original);
assert(!E.validateSaved({...p,questions:p.questions.slice(0,5)}));assert(!E.validateSaved({...p,questions:[{...p.questions[0],competition:'BMO1'},...p.questions.slice(1)]}));
const allIds=new Set(problems.map(p=>p.id));for(const paper of catalog.official){assert(!/BMO2|FIST/.test(paper.competition));assert.equal(paper.questions.length,paper.questionCount);paper.questions.forEach(q=>{if(q.bankId)assert(allIds.has(q.bankId))});if(paper.complete)assert.equal(paper.rating,E.mean(paper.questions));else assert.equal(paper.rating,null)}
assert(!E.validateSaved({...p,questions:[null,...p.questions.slice(1)]}));
assert(!E.validateSaved({...p,questions:[{...p.questions[0],subtopics:'bad'},...p.questions.slice(1)]}));
assert.equal(E.normalizeSaved({...p,rating:99,questionCount:42}).rating,E.mean(p.questions));
console.log('Passed: 300 calibrated selections, 25 non-repeating mocks, exclusion/failure/snapshot cases and all 54 official papers.');
