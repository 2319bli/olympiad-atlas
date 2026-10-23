import json,re,collections,sys
sys.path.insert(0,str(__import__("pathlib").Path(__file__).resolve().parents[1]))
from subtopics import classify
from pathlib import Path
p=Path(__file__).parent
reviews=json.loads((p/'reviews.json').read_text())
out=[]; decisions=[]
for slug,r in reviews.items():
 f=p/(slug+'.json')
 if not f.exists():continue
 d=json.loads(f.read_text()); v=r['difficulty']
 if d['country']=='Soviet Union' and r.get('competition',d['competition'])=='CIS Mathematical Olympiad':d['country']='Commonwealth of Independent States'
 incl=v is not None and 1<=v<=10 and not r.get('quarantine') and not r.get('duplicateOf')
 status='included' if incl else 'duplicate-appearance' if r.get('duplicateOf') else 'outside-BMO-prerequisites' if r.get('outOfScope') else 'quarantined' if r.get('quarantine') or v is None else 'below-target' if v<4 else 'above-target'
 decisions.append({'id':slug,'country':d['country'],'competition':r.get('competition',d['competition']),'year':d['year'],'section':r.get('section',d.get('section')),'number':r.get('number',d.get('problem_number')),'difficulty':v,'included':incl,'reason':r['reason'],'status':status,'duplicateOf':r.get('duplicateOf'),'sourceUrl':r.get('sourceUrl','https://mathnet.mit.edu/explorer.html?p='+slug),'notes':r.get('notes','')})
 if not incl:continue
 if not r.get('statement',d.get('problem_markdown','')).strip() or 'See the official paper for the full statement' in r.get('statement',d.get('problem_markdown','')):raise ValueError('Missing statement: '+slug)
 solution='\n\n'.join(d.get('solutions_markdown',[])[:1])
 # Remove non-essential supporting figures; every included diagram-dependent statement needs an explicit override.
 solution=re.sub(r'!\[[^]]*\]\([^)]*\)\s*(?:Figure[^\n]*\n)?','',solution)
 statement=r.get('statement',d['problem_markdown']).replace(r'\varangle',r'\angle')
 if re.search(r'!\[',statement):raise ValueError('Statement needs a figure review: '+slug)
 if d.get('booklet_copyright_holder') and not r.get('statement'):raise ValueError('Copyright review needed: '+slug)
 solution=r.get('solution',solution)
 solution=solution.replace(r'{r@{\quad}l}',r'{rl}').replace(r'\varangle',r'\angle')
 solution=re.sub(r'(?m)^\s*(?:Fig\.|Figure|Рис\.)\s*\d+[^\n]*$','',solution)
 solution=re.sub(r'\s*\((?:Fig\.|Figure|Рис\.)\s*\d+\)','',solution)
 title=d.get('booklet_title') or d.get('competition_raw') or d['competition']
 notes=r.get('notes','')

 out.append({'id':slug,'country':d['country'],'competition':r.get('competition',d['competition']),'year':d['year'],'section':r.get('section',d.get('section')),'number':r.get('number',d['problem_number']),'statement':statement,'solution':solution,'sourceUrl':r.get('sourceUrl','https://mathnet.mit.edu/explorer.html?p='+slug),'solutionUrl':None if r.get('noSolutionLink') else r.get('solutionUrl','https://mathnet.mit.edu/explorer.html?p='+slug),'sourceName':r.get('sourceName','MathNet transcription of '+title),'solutionKind':r.get('solutionKind','original-exposition' if 'solution' in r else 'sourced'),'topic':r['topic'],'tags':r['tags'],'difficulty':v,'ratingReason':r['reason'],'reviewStatus':'individually-assessed','notes':notes.strip(),'license':r.get('license','MathNet CC BY4.0; original contest rights retained where asserted'),'provenance':{'booklet':title,'organization':d.get('booklet_organization'),'sourceRecord':r.get('sourceUrl') or 'https://mathnet.mit.edu/data_v2/full/'+next(x[1] for x in json.loads((p/'queue.json').read_text()) if x[0]==slug)+'/'+slug+'.json.gz'}})
for item in out:
 item['topic']={'Number theory':'Number Theory','Combinatorics':'Combinatorics'}.get(item['topic'],item['topic'])
 item['subtopics']=reviews[item['id']].get('subtopics') or classify(item)
 item['appearances']=[]
 for dup,review in reviews.items():
  if review.get('duplicateOf')==item['id']:
   dd=json.loads((p/(dup+'.json')).read_text())
   item['appearances'].append({'competition':review.get('competition',dd['competition']),'country':dd['country'],'year':dd['year'],'section':review.get('section',dd.get('section')),'number':review.get('number',dd['problem_number']),'sourceUrl':review.get('sourceUrl','https://mathnet.mit.edu/explorer.html?p='+dup)})
(p.parent.parent/'data/europe.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
exec((p/'coverage_inventory.py').read_text())
print(len(decisions),'inspected appearances;',coverage['distinctRatedCount'],'distinct rated;',len(out),'included')
