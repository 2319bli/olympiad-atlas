const assert=require('node:assert/strict'),fs=require('node:fs'),vm=require('node:vm');
const data=JSON.parse(fs.readFileSync('public/data/study-guide.json','utf8'));
const bank=JSON.parse(fs.readFileSync('public/data/problems.json','utf8'));
const context={};vm.createContext(context);vm.runInContext(fs.readFileSync('public/study-guide.js','utf8')+'\nglobalThis.guide=StudyGuide;',context);
const katexContext={};vm.createContext(katexContext);vm.runInContext(fs.readFileSync('public/vendor/katex/katex.min.js','utf8'),katexContext);
assert.equal(new Set(data.entries.map(e=>e.id)).size,data.entries.length);
assert.deepEqual([...new Set(data.entries.flatMap(e=>e.subtopics))].sort(),[...new Set(bank.flatMap(p=>p.subtopics||[]))].sort(),'Every live taxonomy label needs an explanation.');
let formulas=0;
for(const e of data.entries){
 assert(/^[a-z0-9-]+$/.test(e.id));assert(data.groups.some(g=>g.id===e.group));assert(data.levels.some(l=>l.id===e.level));assert.equal(e.subtopics.length,1,'Practice deep links apply one exact subtopic.');
 for(const key of ['overview','questions','techniques','example','pitfall']){
  assert(typeof e[key]==='string'&&e[key].length>50,`${e.id} lacks substantive ${key}`);
  for(const m of e[key].matchAll(/\$([^$]+)\$/g)){katexContext.katex.renderToString(m[1],{throwOnError:true,strict:'error'});formulas++;}
 }
 const matched=context.guide.problems(e,bank);assert(matched.length>0,e.id+' has no practice questions');
 assert(matched.every(p=>p.subtopics.includes(e.title)));assert(matched.every((p,i)=>!i||matched[i-1].difficulty<=p.difficulty));
}
const search=(query,group='',level='')=>context.guide.matchEntries(data,{query,group,level}).map(e=>e.id);
assert(search('Vieta').includes('polynomials'));assert(search('vieta jumping').includes('descent'));
assert(!search('Vieta','geometry').length);assert(search('perpendicular','geometry').length>0);
assert.equal(search('unlikely-no-match').length,0);assert.equal(search('', '', 'foundation').length,data.entries.filter(e=>e.level==='foundation').length);
for(const s of data.sources)assert.equal(new URL(s.url).protocol,'https:');
console.log(`Passed ${data.entries.length} topic guides: complete bank taxonomy, real practice matches, search/filter combinations and ${formulas} valid TeX expressions.`);
