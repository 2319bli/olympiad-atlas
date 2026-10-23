/* Topic explanations are original teaching material; bank tags supply practice links. */
'use strict';
const StudyGuide = {
 matchEntries(data,{query='',group='',level=''}={}) {
  const words=query.trim().toLowerCase().split(/\s+/).filter(Boolean);
  return data.entries.filter(e=>(!group||e.group===group)&&(!level||e.level===level)&&words.every(w=>[e.title,e.overview,e.questions,e.techniques,e.example,e.keywords,...e.subtopics].join(' ').toLowerCase().includes(w)));
 },
 problems(entry,problems) {return problems.filter(p=>entry.subtopics.some(s=>(p.subtopics||[]).includes(s))).sort((a,b)=>a.difficulty-b.difficulty||String(a.id).localeCompare(String(b.id)));}
};
let studyData,studyLoading,studyReturnHash='#learn';
const studyFilters={query:'',group:'',level:''};
async function loadStudyGuide(){
 if(studyData)return studyData;
 if(!studyLoading)studyLoading=fetch('data/study-guide.json').then(r=>{if(!r.ok)throw Error('Guide unavailable');return r.json()}).then(d=>studyData=d).catch(e=>{studyLoading=null;throw e});
 return studyLoading;
}
function studyLevel(id){return studyData.levels.find(l=>l.id===id)}
function studyEntryLink(e){return '#learn='+encodeURIComponent(e.id)}
async function renderStudyGuide(){
 const target=$('#learn-view'),requested=location.hash;
 target.innerHTML='<div class="study-page"><p role="status">Loading the topic guide…</p></div>';
 try{
  await loadStudyGuide();if(state.view!=='learn'||location.hash!==requested)return;
  studyReturnHash=requested;
  const id=requested.startsWith('#learn=')?requested.slice(7):'';
  if(id){const entry=studyData.entries.find(e=>e.id===id);if(entry)renderStudyEntry(entry);else target.innerHTML='<div class="study-page empty-state"><h1>Guide not found</h1><p>This topic link is not in the current guide.</p><a class="button secondary" href="#learn">Browse the topic guide</a></div>';return;}
  renderStudyHome();
 }catch(e){if(state.view==='learn'){target.innerHTML='<div class="study-page empty-state"><h1>The guide could not load.</h1><p>Please try again. Your papers and practice marks are unaffected.</p><button class="button secondary" id="retry-study">Try again</button></div>';$('#retry-study').onclick=renderStudyGuide;}}
}
function renderStudyHome(){
 const data=studyData;
 $('#learn-view').innerHTML=`<div class="study-page"><header class="study-heading"><div><p class="eyebrow">THE OLYMPIAD TOOLKIT</p><h1>Know the ideas.<br><em>Find your way in.</em></h1><p class="study-lead">A topic-by-topic guide to what olympiad questions ask, how to approach them, and why the techniques work.</p></div><div class="study-index-note"><strong>${data.entries.length}</strong><span>subtopic guides</span><p>Four mathematical areas.<br>Proof methods that connect them.</p></div></header>
 <div class="study-topic-grid">${data.groups.map(g=>`<button class="study-topic-tile" data-study-group="${g.id}" aria-pressed="${studyFilters.group===g.id}"><span class="study-symbol">${esc(g.symbol)}</span><strong>${esc(g.name)}</strong><span>${data.entries.filter(e=>e.group===g.id).length} guides <b aria-hidden="true">↗</b></span></button>`).join('')}</div>
 <details class="study-orientation"><summary>Where to begin, and how to use this guide</summary><div><p>Start with a topic you recognise. Read the explanation, try to reproduce the worked example, then open a matching question and attempt it before revealing its solution. Afterward, write down the clue that made the technique useful.</p><p>For BMO preparation, make the foundations fluent before chasing specialist theorems. A hard problem can use a very simple idea; the labels below describe a learning sequence, not question difficulty or an official syllabus.</p><div class="study-level-key">${data.levels.map(l=>`<p><strong>${esc(l.name)}</strong> ${esc(l.description)}</p>`).join('')}</div><p>The guide covers every subtopic label currently in Atlas, including wider national and historical material. It is an overview, not an exhaustive list of every possible olympiad idea. Examples here are short teaching examples, not quoted contest questions.</p><p>Practice counts use the full bank at all difficulties and can overlap. A technique may occur in several main topics; each guide has one home to keep this index manageable.</p></div></details>
 <div class="study-controls"><label class="study-search">Search topics and techniques<input id="study-search" type="search" placeholder="Try Vieta, colouring, tangency…" value="${esc(studyFilters.query)}"></label><label>Area<select id="study-group"><option value="">All areas</option>${data.groups.map(g=>`<option value="${g.id}" ${studyFilters.group===g.id?'selected':''}>${esc(g.name)}</option>`).join('')}</select></label><label>Learning stage<select id="study-level"><option value="">All stages</option>${data.levels.map(l=>`<option value="${l.id}" ${studyFilters.level===l.id?'selected':''}>${esc(l.name)}</option>`).join('')}</select></label><button class="text-button" id="study-reset">Clear filters</button></div>
 <p class="study-results-count" id="study-result-count" role="status"></p><div id="study-results"></div>
 <aside class="study-reading"><h2>Continue with original papers</h2><p>Use the linked problems for practice, and the organisers’ materials for full papers and further preparation.</p>${data.sources.map(s=>`<a href="${esc(goodUrl(s.url))}" target="_blank" rel="noopener noreferrer">${esc(s.title)} ↗</a>`).join('')}</aside></div>`;
 $('#study-search').oninput=e=>{studyFilters.query=e.target.value;renderStudyResults()};
 $('#study-group').onchange=e=>{studyFilters.group=e.target.value;renderStudyResults()};
 $('#study-level').onchange=e=>{studyFilters.level=e.target.value;renderStudyResults()};
 $('#study-reset').onclick=()=>{Object.assign(studyFilters,{query:'',group:'',level:''});$('#study-search').value='';$('#study-group').value='';$('#study-level').value='';renderStudyResults()};
 $$('[data-study-group]').forEach(b=>b.onclick=()=>{studyFilters.group=studyFilters.group===b.dataset.studyGroup?'':b.dataset.studyGroup;$('#study-group').value=studyFilters.group;renderStudyResults();$('#study-group').focus()});
 renderStudyResults();
}
function renderStudyResults(){
 const entries=StudyGuide.matchEntries(studyData,studyFilters);
 $('#study-result-count').textContent=`${entries.length} of ${studyData.entries.length} guides${studyFilters.query?' matching “'+studyFilters.query+'”':''}`;
 $$('[data-study-group]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.studyGroup===studyFilters.group)));
 $('#study-results').innerHTML=entries.length?studyData.groups.map(g=>{
  const groupEntries=entries.filter(e=>e.group===g.id);if(!groupEntries.length)return '';
  return `<section class="study-group-section"><header><span class="study-symbol" aria-hidden="true">${esc(g.symbol)}</span><div><h2>${esc(g.name)}</h2><p>${esc(g.intro)}</p><p class="study-start"><strong>A starting point:</strong> ${esc(g.start)}</p></div></header><div class="study-card-grid">${groupEntries.map(e=>`<article class="study-card"><div class="study-card-meta"><span class="study-level ${e.level}">${esc(studyLevel(e.level).name)}</span><span>${StudyGuide.problems(e,state.problems).length.toLocaleString()} matching problems</span></div><h3><a href="${studyEntryLink(e)}">${esc(e.title)} <span aria-hidden="true">→</span></a></h3><div class="math-content">${md(e.overview)}</div><a class="study-read-link" href="${studyEntryLink(e)}" aria-label="Read ${esc(e.title)} guide">Explore the ideas →</a></article>`).join('')}</div></section>`;
 }).join(''):'<div class="empty-state"><h2>No guides match those filters.</h2><p>Try a broader technique name or clear the area and learning-stage filters.</p><button class="button secondary" id="study-empty-reset">Show all guides</button></div>';
 if($('#study-empty-reset'))$('#study-empty-reset').onclick=()=>$('#study-reset').click();
}
function renderStudyEntry(entry){
 const group=studyData.groups.find(g=>g.id===entry.group),level=studyLevel(entry.level),pool=StudyGuide.problems(entry,state.problems);
 const examples=[...new Set([pool[0],pool[Math.floor(pool.length/2)],pool[pool.length-1]].filter(Boolean))];
 const siblings=studyData.entries.filter(e=>e.group===entry.group),index=siblings.indexOf(entry);
 $('#learn-view').innerHTML=`<article class="study-page study-article"><a class="study-back" href="#learn">← All topic guides</a><header class="study-article-heading"><p class="eyebrow">${esc(group.name.toUpperCase())} · TOPIC GUIDE</p><h1>${esc(entry.title)}</h1><span class="study-level ${entry.level}">${esc(level.name)}</span><p class="study-stage-note">${esc(level.description)}</p><div class="study-lead math-content">${md(entry.overview)}</div></header>
 <div class="study-article-layout"><div class="study-explanation"><section><h2>What questions ask</h2><div class="math-content">${md(entry.questions)}</div></section><section><h2>Useful techniques</h2><div class="math-content">${md(entry.techniques)}</div></section><section class="study-example"><p class="eyebrow">A SHORT WORKED EXAMPLE</p><div class="math-content">${md(entry.example)}</div><p class="study-example-note">A teaching example to isolate the idea; contest problems may combine several ideas.</p></section><section class="study-pitfall"><h2>A common trap</h2><div class="math-content">${md(entry.pitfall)}</div></section><section><h2>Turn the idea into a proof</h2><p>Identify which condition lets you use the technique. State that step precisely, carry the argument through, and check any equality cases, domain restrictions or converse needed by the question.</p></section></div>
 <aside class="study-practice-panel"><h2>Put it into practice</h2><p><strong>${pool.length.toLocaleString()}</strong> matching problems across all difficulties.</p><a class="button primary" href="#study-practice=${entry.id}">Browse matching questions →</a><p class="study-practice-note">Opens the library with this subtopic selected, all other filters cleared, and easier questions first. Topic labels can suggest methods.</p><h3>A few places to try</h3><p class="study-practice-note">A spread from the current bank, ordered by estimated difficulty. Read the easier example first.</p>${examples.map(p=>`<button class="study-problem-link" data-open="${esc(p.id)}"><span>${esc(problemLabel(p))}<small>${esc(problemNumber(p))} · ${esc(p.topic)}</small></span><b>${p.difficulty.toFixed(1)}<small>/ 10</small></b></button>`).join('')}<p class="study-practice-note">Solutions remain hidden until you reveal them in the problem viewer.</p></aside></div>
 <nav class="study-next" aria-label="Other guides in this area">${index>0?`<a href="${studyEntryLink(siblings[index-1])}"><small>Previous in ${esc(group.name)}</small>← ${esc(siblings[index-1].title)}</a>`:'<span></span>'}${index<siblings.length-1?`<a href="${studyEntryLink(siblings[index+1])}"><small>Next in ${esc(group.name)}</small>${esc(siblings[index+1].title)} →</a>`:'<a href="#learn">Back to all guides →</a>'}</nav></article>`;
 $('#learn-view').scrollIntoView({block:'start'});
}
async function openStudyPractice(id){
 const requested=location.hash;
 try{
  const data=await loadStudyGuide();if(location.hash!==requested)return;
  const entry=data.entries.find(e=>e.id===id);if(!entry){location.hash='learn';return;}
  state.topic='All topics';['#search','#country-filter','#competition-filter','#year-filter','#status-filter'].forEach(s=>$(s).value='');
  $('#solution-filter').checked=false;$('#difficulty-min').value='1';$('#difficulty-max').value='10';$('#sort').value='difficulty-asc';
  renderTopics();renderSubtopics();$('#subtopic-filter').value=entry.subtopics[0];changeView('library');
  // Keep this deep link so reload/back can restore the exact guide practice filter.
  $('#library-view').scrollIntoView({block:'start'});
 }catch(e){changeView('learn');}
}
