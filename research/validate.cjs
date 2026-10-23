const fs = require('node:fs');
const katex = require('../public/vendor/katex/katex.min.js');
const problems = JSON.parse(fs.readFileSync('public/data/problems.json', 'utf8'));
const errors = [], warnings = [], images = new Map();
let expressions = 0;
for (const p of problems) {
  if(!Number.isFinite(p.difficulty)||p.difficulty<1||p.difficulty>10||!Number.isInteger(p.difficulty*2)) errors.push({id:p.id,error:'Invalid numerical rating'});
  if(p.reviewStatus!=='individually-assessed'||!p.statement?.trim()||!p.ratingReason?.trim()) errors.push({id:p.id,error:'Missing statement or individual review'});
  if (!Array.isArray(p.subtopics) || !p.subtopics.length || p.subtopics.some(t=>typeof t!=='string'||!t.trim()) || new Set(p.subtopics).size!==p.subtopics.length) errors.push({id:p.id,error:'Missing, invalid or duplicate subtopics'});
  for (const key of ['sourceUrl','solutionUrl']) {
    if (p[key] && !/^https?:\/\//.test(p[key])) errors.push({id:p.id, key, error:'Not an absolute web URL'});
  }
  for (const key of ['statement','solution','ratingReason']) {
    const s = p[key] || '';
    for (const m of s.matchAll(/\$\$([\s\S]*?)\$\$|\\\[([\s\S]*?)\\\]|\$([^$\n]+?)\$|\\\(([\s\S]*?)\\\)/g)) {
      const tex = m[1] ?? m[2] ?? m[3] ?? m[4];
      expressions++;
      try { katex.renderToString(tex, {displayMode:m[1]!==undefined||m[2]!==undefined,throwOnError:true, strict:'ignore', trust:false,macros:{'\\overparen':'\\overset{\\frown}{#1}','\\lcm':'\\operatorname{lcm}'}}); }
      catch (e) { errors.push({id:p.id,key,tex,error:e.message}); }
    }
    for(const m of s.matchAll(/!\[[^\]]*\]\(([^)]+)\)/g)) {
      if(!images.has(m[1]))images.set(m[1],[]);
      images.get(m[1]).push({id:p.id,key});
    }
    if(/[\u0000-\u0008\u000b\u000c\u000e-\u001f\ufffd]/.test(s)) warnings.push({id:p.id,key,warning:'Control or replacement character'});
    if(/\bProblem\s+Problem\b/i.test(s))warnings.push({id:p.id,key,warning:'Repeated problem label'});
  }
  if((p.ratingReason||'').length<40) warnings.push({id:p.id,warning:'Unusually short difficulty justification'});
}
const report = {problems:problems.length,expressions,errors,warnings,images:Object.fromEntries(images)};
for (const [url,entries] of images) {
  if (!url.startsWith('assets/') && !url.startsWith('https://')) errors.push({url,entries,error:'Figure URL is not supported by the page renderer'});
  if (url.startsWith('assets/') && !fs.existsSync('public/'+url)) errors.push({url,entries,error:'Local diagram file is missing'});
}
fs.writeFileSync('research/validation-report.json',JSON.stringify(report,null,2));
console.log(JSON.stringify({problems:problems.length,expressions,errors,warnings,images:images.size},null,2));
process.exitCode = errors.length ? 1 : 0;
