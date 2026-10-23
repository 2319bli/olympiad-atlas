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
// Presets must retain empirical profiles; custom settings are hard constraints.
for(let i=0;i<60;i++){
 const out=E.generate(problems,catalog,{preset:'bmo2',rng,requireSolutions:true});assert.equal(out.questions.length,4);assert.match(out.templateId,/^bmo2-/);
 out.questions.forEach((q,j)=>{assert(!E.isBritish(q));assert.equal(q.topic,out.topics[j]);assert(Math.abs(q.difficulty-out.targets[j])<=.5)});
 const saved=E.snapshot(out,{id:'mock-bmo2-'+i,title:'Round 2',createdAt:new Date().toISOString()});assert(E.validateSaved(saved));assert.equal(E.normalizeSaved(saved).totalMarks,40);assert.equal(saved.durationMinutes,210);
}
for(let n=4;n<=10;n++)for(const profile of ['rising','steady','random']){
 const config={preset:'custom',questionCount:n,minDifficulty:3,maxDifficulty:8,profile,topics:['Number Theory','Algebra'],topicMix:'balanced',durationMinutes:95,marksPerQuestion:7,maxPerCountry:2,maxPerCompetition:1,minYear:2000,maxYear:2025,requireSolutions:true,allowDiagrams:false};
 const out=E.generate(problems,catalog,{settings:config,rng});assert.equal(out.questions.length,n);
 const topics={},countries={},competitions={};out.questions.forEach((q,i)=>{assert(q.difficulty>=3&&q.difficulty<=8);assert(config.topics.includes(q.topic));assert(q.year>=2000&&q.year<=2025);assert(q.solution||q.solutionUrl);assert(!/!\[[^\]]*\]\(/.test(q.statement));topics[q.topic]=(topics[q.topic]||0)+1;countries[q.country]=(countries[q.country]||0)+1;const k=q.country+q.competition;competitions[k]=(competitions[k]||0)+1;if(profile==='rising'&&i)assert(q.difficulty>=out.questions[i-1].difficulty)});
 assert(Math.abs(topics.Algebra-topics['Number Theory'])<=1);assert(Math.max(...Object.values(countries))<=2);assert.equal(Math.max(...Object.values(competitions)),1);
 const saved=E.snapshot(out,{id:'mock-custom-'+n+'-'+profile,title:'Custom',createdAt:new Date().toISOString()});assert(E.validateSaved(saved));assert.equal(saved.totalMarks,n*7);assert.equal(E.normalizeSaved(saved).durationMinutes,95);assert.equal(E.normalizeSaved(saved).questionCount,n);
 assert(!E.validateSaved({...saved,questionCount:n+1}));assert(!E.validateSaved({...saved,generationSettings:{...saved.generationSettings,questionCount:11}}));
}
const old={...p,version:1};delete old.generationSettings;assert(E.validateSaved(old));assert.equal(E.normalizeSaved(old).questionCount,6);assert.equal(E.normalizeSaved(old).totalMarks,60);
for(const bad of [{questionCount:3},{questionCount:11},{topics:[]},{topics:['Arithmetic']},{minDifficulty:8,maxDifficulty:2},{minYear:2026,maxYear:2000},{durationMinutes:0},{marksPerQuestion:100},{profile:'template'}])assert.throws(()=>E.settings({preset:'custom',...bad}));
const us=E.generate(problems,catalog,{preset:'custom',profile:'random',topicMix:'random',questionCount:10,countries:['United States'],maxPerCountry:0,maxPerCompetition:0,rng});assert(us.questions.every(q=>q.country==='United States'));
assert.throws(()=>E.generate(problems,catalog,{preset:'custom',questionCount:4,countries:['United States'],maxPerCountry:2,rng}),/not enough/);
const exact=E.generate(problems,catalog,{preset:'custom',profile:'steady',minDifficulty:5,maxDifficulty:5,tolerance:0,rng});assert(exact.questions.every(q=>q.difficulty===5));
const british={...problems.find(q=>E.isBritish(q)),reviewStatus:'individually-assessed',difficulty:5};
const copy={...british,id:'disguised',competition:'Other',country:'Elsewhere',appearances:[],alternateOrigins:[],originCompetitions:[]};
assert.equal(E.candidatePool([british,copy],{preset:'custom',minDifficulty:1,maxDifficulty:10}).length,0);
const advanced={...copy,id:'advanced',statement:'Prove a new assertion.',subtopics:['Calculus'],tags:[]};
assert.equal(E.candidatePool([advanced],{preset:'custom',excludeAdvanced:true}).length,0);assert.equal(E.candidatePool([advanced],{preset:'custom',excludeAdvanced:false}).length,1);
console.log('Passed BMO2, custom 4–10, topic balance, difficulty/order/source constraints, snapshots, legacy backups and strict failure cases.');
for(const t of catalog.calibrationBmo2.templates){
 assert.equal(t.topics.length,4);t.difficulties.forEach((d,i)=>{const q=problems.find(q=>q.id===`bmo2-${t.archiveYear}-q${i+1}`);assert(q);assert.equal(q.difficulty,d);assert.equal(q.topic,t.topics[i])});
}
const pdfContext={PaperEngine:E};vm.runInNewContext(fs.readFileSync('public/paper-pdf.js','utf8'),pdfContext);
assert.equal(pdfContext.examIdentity({...p,generationSettings:{...p.generationSettings,preset:'bmo2'}}).round,'Round 2');
assert.equal(pdfContext.examIdentity({...p,generationSettings:{...p.generationSettings,preset:'custom'}}).heading,'Olympiad Practice Paper');
assert.equal(pdfContext.examIdentity(old).round,'Round 1');
console.log('Passed source-derived BMO2 calibration and PDF format identities.');
