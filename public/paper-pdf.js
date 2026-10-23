/* A4 exam PDFs generated entirely in the browser. Question pages are rendered
 * at 240 dpi so KaTeX and source diagrams retain their mathematical layout. */
'use strict';
let pdfLibraryPromise;
function loadPdfLibraries(){if(!pdfLibraryPromise)pdfLibraryPromise=Promise.all(['vendor/html2canvas.min.js','vendor/jspdf.umd.min.js'].map(src=>new Promise((resolve,reject)=>{const s=document.createElement('script');s.src=src;s.onload=resolve;s.onerror=()=>reject(Error('PDF tools could not load. Please reload and try again.'));document.head.append(s)}))).catch(e=>{pdfLibraryPromise=null;throw e});return pdfLibraryPromise}
async function readyPaperImages(host){const images=[...host.querySelectorAll('img')];await Promise.all(images.map(img=>{img.loading='eager';if(img.complete){if(!img.naturalWidth)throw Error('A question diagram could not load. Try again before exporting.');return}return new Promise((resolve,reject)=>{const timer=setTimeout(()=>reject(Error('A diagram is taking too long to load. Please try again.')),15000);img.onload=()=>{clearTimeout(timer);resolve()};img.onerror=()=>{clearTimeout(timer);reject(Error('A question diagram could not load. Please try again.'))}})}))}
function examIdentity(p){
 if(p.legacy)return {heading:'British Mathematical Olympiad',round:'',running:'British Mathematical Olympiad'};
 const preset=p.kind==='generated'?PaperEngine.presetOf(p):'bmo1';
 if(preset==='custom')return {heading:'Olympiad Practice Paper',round:'',running:'Olympiad Practice Paper'};
 const round=preset==='bmo2'?'Round 2':'Round 1';return {heading:'British Mathematical Olympiad',round,running:'British Mathematical Olympiad '+round};
}
function pdfPage(host,p){const page=document.createElement('section');page.className='exam-page';page.innerHTML=`<header class="exam-running"><span>${examIdentity(p).running}</span><span>${esc(p.title)}</span></header><div class="exam-body"></div><div class="exam-footer"></div>`;host.append(page);return page}
function examQuestion(q,showMarks=false){const block=document.createElement('div');block.className='exam-question';block.innerHTML=`<div class="exam-number">${esc(q.paperNumber)}.</div><div class="exam-statement">${md(q.statement)}${showMarks&&q.marks?`<p class="exam-marks">[${q.marks} marks]</p>`:''}</div>`;return block}
function examInstructions(p,questions,duration){
 const uniformMarks=questions.length&&questions.every(q=>q.marks===questions[0].marks)&&questions[0].marks;
 const historical=p.kind==='official'&&(p.legacy||p.archiveYear===2021);
 return `<h3>Instructions</h3><ol>
 <li>Time available: <strong>${duration}.</strong></li>
 <li><strong>Present full proofs, rather than answers alone.</strong> Explain and justify every claim clearly. Plan your argument in rough, then write a legible final solution; keep rough work separate.${historical?' Follow any answer-only sections specified in the original paper.':''}</li>
 <li><strong>Finish a proof before collecting partial attempts.</strong> A few fully solved problems are more valuable than unfinished work on many questions.</li>
 <li>${uniformMarks?`<strong>There are ${uniformMarks} marks available per question.</strong>`:'<strong>Check the mark allocation for each question.</strong>'} ${historical?'Use the original paper for its section choices and marking rules.':'Read the questions and choose where to begin; difficulty need not rise with question number.'}</li>
 <li><strong>No calculators, protractors or computer assistance.</strong> You may use a ruler, set square and compasses. For geometry, draw a large, accurate figure with these instruments.</li>
 <li><strong>Begin each solution on a fresh sheet.</strong> Use ordinary plain or lined paper for this practice session.</li>
 <li>Label every sheet with its question number and the page number within that solution, including any continuation sheets.</li>
 <li><strong>Use only one side of each sheet.</strong> Make all writing and diagrams dark enough to read easily.</li>
 <li>Put your completed work in question order, leaving out unused sheets.</li>
 <li>Work on your own until the time is up. Leave source credits, solutions and difficulty information until after your attempt.</li>
 <li><strong>Keep the question pages closed until your timed session begins.</strong></li>
 </ol>${p.kind==='official'?`<p class="exam-historical">${esc(p.formatNote||'For the original examination instructions, use the official paper linked in Atlas.')}</p>`:''}`;
}
async function buildExamPages(p,questions){
 const host=document.createElement('div');host.className='exam-export';document.body.append(host);
 try{
 const cover=pdfPage(host,p);cover.classList.add('exam-cover');
 const duration=p.durationMinutes===210?'3½ hours':p.durationMinutes===150?'2½ hours':p.durationMinutes?`${p.durationMinutes} minutes`:'as stated in the original paper';
 const uniformMarks=questions.length&&questions.every(q=>q.marks===questions[0].marks)&&questions[0].marks;
 cover.querySelector('.exam-body').innerHTML=`<div class="exam-brand"><span class="exam-brandmark" aria-hidden="true"><i></i><i></i><i></i></span><span>Olympiad Atlas</span></div><h1>${examIdentity(p).heading}${examIdentity(p).round?'<br><span>'+examIdentity(p).round+'</span>':''}</h1><h2>${esc(p.title)}</h2><p class="exam-edition">${p.kind==='generated'?'Unofficial practice paper':'Reformatted past paper'} · ${questions.length} questions${p.totalMarks?` · ${p.totalMarks} marks`:''}</p><p class="exam-unofficial">${p.kind==='generated'?'An independent mock paper, not produced or endorsed by UKMT.':'An Atlas transcription. The original organisers retain their rights.'}</p><div class="exam-instructions">${examInstructions(p,questions,duration)}</div><div class="exam-cover-note"><p>Practice guidance adapted from British Mathematical Olympiad papers.<br>Original competition instructions and papers: bmos.ukmt.org.uk</p><p class="exam-site">2319bli.github.io/olympiad-atlas</p></div>`;
 await document.fonts.ready;
 if(cover.querySelector('.exam-body').scrollHeight>cover.querySelector('.exam-body').clientHeight)cover.classList.add('exam-cover-compact');
 if(cover.querySelector('.exam-body').scrollHeight>cover.querySelector('.exam-body').clientHeight)throw Error('The cover text is too long. Please shorten the paper name.');
 let page=pdfPage(host,p),body=page.querySelector('.exam-body');
 for(const q of questions){const block=examQuestion(q,!uniformMarks);body.append(block);await document.fonts.ready;await readyPaperImages(block);
  if(body.scrollHeight>body.clientHeight&&body.children.length>1){block.remove();page=pdfPage(host,p);body=page.querySelector('.exam-body');body.append(block)}
  if(body.scrollHeight>body.clientHeight){
   // Rare long statements receive their own page. Reduce only as far as 11pt.
   block.style.fontSize='14.67px';await document.fonts.ready;
   if(body.scrollHeight>body.clientHeight){
    const parts=[...block.querySelector('.exam-statement').children];block.remove();let current=examQuestion({...q,statement:'',marks:null}),statement=current.querySelector('.exam-statement');current.style.fontSize='14.67px';body.append(current);
    for(const part of parts){statement.append(part);if(body.scrollHeight>body.clientHeight&&statement.children.length>1){part.remove();page=pdfPage(host,p);body=page.querySelector('.exam-body');current=examQuestion({...q,paperNumber:q.paperNumber+' (continued)',statement:'',marks:null});current.style.fontSize='14.67px';statement=current.querySelector('.exam-statement');body.append(current);statement.append(part)}if(body.scrollHeight>body.clientHeight)throw Error(`A paragraph in question ${q.paperNumber} exceeds the printable page. Please use the source link.`)}
   }
  }
  if([...body.querySelectorAll('.exam-statement')].some(el=>el.scrollWidth>el.clientWidth+2))throw Error(`A formula in question ${q.paperNumber} is too wide for this PDF layout. Please use the source link.`);
 }
 // Spread short question sets down the page, without adding a gap at the top.
 for(const questionPage of [...host.children].slice(1)){const b=questionPage.querySelector('.exam-body');if(b.children.length>1)b.classList.add('exam-question-list')}
 const sources=pdfPage(host,p);sources.classList.add('exam-sources');sources.querySelector('.exam-body').innerHTML=`<h2>Question sources</h2><p>Source information is kept separate from the question pages so it does not suggest a method while you work.</p>${questions.map(q=>`<div class="exam-credit"><b>${esc(q.paperNumber)}.</b> ${esc(problemLabel(q))}, ${esc(problemNumber(q))}.<br><span>${esc(q.sourceUrl||'')}</span></div>`).join('')}<p class="exam-copyright">Original organisers and problem authors retain their rights. Statements may be translated, paraphrased or reformatted. MathNet-derived material is attributed to Shaden Alshammari and colleagues, MathNet (2026), under CC BY 4.0 where applicable; original contest rights are retained. Individual source and translation notes are available in Olympiad Atlas.</p><p>Generated by Olympiad Atlas. No worked solutions or difficulty ratings are included in this PDF.</p>`;
 const sourceBlocks=[...sources.querySelector('.exam-body').children];sources.querySelector('.exam-body').replaceChildren();let sourceBody=sources.querySelector('.exam-body');for(const block of sourceBlocks){sourceBody.append(block);if(sourceBody.scrollHeight>sourceBody.clientHeight&&sourceBody.children.length>1){block.remove();const next=pdfPage(host,p);next.classList.add('exam-sources');sourceBody=next.querySelector('.exam-body');sourceBody.append(block)}}
 const pages=[...host.children];pages.forEach((page,i)=>{page.querySelector('.exam-footer').innerHTML=`<span>Olympiad Atlas · ${p.kind==='generated'?'Unofficial practice':'Reformatted paper'}</span><span>${i===0?'Instructions':page.classList.contains('exam-sources')?'Sources':'Questions'} · ${i+1} / ${pages.length}</span>`});await document.fonts.ready;await readyPaperImages(host);return host;
 }catch(e){host.remove();throw e}
}
async function downloadPaperPdf(p,questions){const button=$('#download-paper-pdf'),status=$('#pdf-status');let host;button.disabled=true;status.textContent='Preparing the PDF…';try{
 if(questions.some(q=>q.missing))throw Error('The transcription is incomplete. Download the original official PDF instead.');
 await loadPdfLibraries();host=await buildExamPages(p,questions);const pdf=new jspdf.jsPDF({orientation:'portrait',unit:'mm',format:'a4',compress:true});pdf.setProperties({title:p.title,subject:p.kind==='generated'?'Unofficial '+PaperEngine.label(p)+' practice paper':'Reformatted BMO1 paper',author:'Olympiad Atlas'});
 for(let i=0;i<host.children.length;i++){status.textContent=`Creating page ${i+1} of ${host.children.length}…`;const page=host.children[i];const canvas=await html2canvas(page,{scale:2.5,backgroundColor:'#ffffff',logging:false,useCORS:true,windowWidth:1000,windowHeight:1200,scrollX:0,scrollY:0,onclone:(_doc,clonedPage)=>{const container=clonedPage.parentElement;container.style.cssText='position:absolute;left:0;top:0;width:794px;background:#fff;z-index:1';for(const sibling of container.children)if(sibling!==clonedPage)sibling.style.display='none'}});if(i)pdf.addPage();pdf.addImage(canvas,'PNG',0,0,210,297,undefined,'FAST');canvas.width=1;canvas.height=1}
const blob=new Blob([pdf.output('arraybuffer')],{type:'application/pdf'}),url=URL.createObjectURL(blob),link=document.createElement('a');link.href=url;link.download=(p.title.replace(/[^a-z0-9 -]/gi,'').trim().replace(/\s+/g,'-')||p.id)+'.pdf';link.textContent='Save PDF file';const preview=document.createElement('a');preview.href=url;preview.target='_blank';preview.rel='noopener';preview.textContent='Preview PDF';preview.style.marginLeft='16px';status.replaceChildren(link,preview);link.click();setTimeout(()=>URL.revokeObjectURL(url),600000);
 }catch(e){status.textContent=e.message;status.setAttribute('role','alert')}finally{host?.remove();button.disabled=false}}
