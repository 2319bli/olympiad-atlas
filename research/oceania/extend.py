import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from subtopics import classify
ROOT=Path(__file__).resolve().parents[2]
data=json.loads((ROOT/'data/oceania-africa.json').read_text())
cov=json.loads((ROOT/'research/oceania-africa-coverage.json').read_text())
def add(year,number,rating,reason,title=None,statement=None,solution=None,topic=None,tags=None,competition='Australian Mathematical Olympiad',source=None,kind='original'):
 ident=f'aus_{"amo" if competition=="Australian Mathematical Olympiad" else "amoc"}_{year}_{number}'
 source=source or f'https://enrichedmaths.maths.uwa.edu.au/Olympiad/AMO/AMO{year}.pdf'
 old=next((p for p in cov['ledger'] if p['id']==ident),None)
 entry={'id':ident,'country':'Australia','competition':competition,'year':year,'section':'','number':str(number),'difficulty':rating,'status':'reviewed' if rating is not None else 'pending-solution-review','included':rating is not None and 1<=rating<=10 and (bool(statement) or any(x['id']==ident for x in data)),'reason':reason,'sourceUrl':source}
 if old:old.update(entry)
 else:cov['ledger'].append(entry)
 if entry['included'] and not statement:
  return  # Preserve the already restored canonical statement and solution.
 if entry['included']:
  assert all([title,statement,solution,topic,tags])
  p={k:entry[k] for k in ['id','country','competition','year','section','number','difficulty','sourceUrl']}
  p.update(title=title,statement=statement,solution=solution,solutionUrl=source,topic=topic,tags=tags,ratingReason=reason,reviewStatus='individually-assessed',solutionKind=kind,notes='Statement paraphrased from the UWA archive. Difficulty is an individual editorial assessment on the 1–10 half-step scale.',provenance={'archive':'University of Western Australia olympiad archive','originalOrganisation':'Australian Mathematics Trust'})
  p['subtopics']=classify(p);assert p['subtopics']
  existing=next((x for x in data if x['id']==ident),None)
  if existing:existing.update(p)
  else:data.append(p)
def finish():
 from collections import Counter
 for p in data:
  if not p.get('subtopics'):p['subtopics']=classify(p)
 cov['updated']='2026-10-23';cov['includedCount']=len(data)
 cov['countsByReviewStatus']=dict(Counter(p['status'] for p in cov['ledger']))
 cov['availableCorpusCount']=len(cov['ledger']);cov['deferredCount']=sum(p['status'].startswith('deferred') for p in cov['ledger'])
 cov['screenedCount']=len(cov['ledger'])-cov['deferredCount']
 cov['numericallyRatedCount']=sum(p.get('difficulty') is not None for p in cov['ledger'])
 assessed=lambda p: p.get('difficulty') is not None and p['status'] in ('reviewed','duplicate-appearance')
 cov['reviewedCount']=sum(assessed(p) for p in cov['ledger'])
 for paper in cov['papers']:
  entries=[p for p in cov['ledger'] if p['country']==paper['country'] and p['competition']==paper['competition'] and p['year']==paper['year'] and p.get('section','')==paper.get('section','')]
  paper['screenedCount']=len(entries);paper['reviewedCount']=sum(assessed(p) for p in entries)
  paper['numericallyRatedCount']=sum(p.get('difficulty') is not None for p in entries)
  paper['complete']=len({p['number'] for p in entries})==paper['expectedCount'] and len(entries)==paper['expectedCount'] and all(assessed(p) for p in entries)
 (ROOT/'data/oceania-africa.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 (ROOT/'research/oceania-africa-coverage.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2)+'\n')
def paper(year,n=8,competition='Australian Mathematical Olympiad'):
 if not any(p['competition']==competition and p['year']==year for p in cov['papers']):cov['papers'].append({'country':'Australia','competition':competition,'year':year,'section':'','complete':False,'statementComplete':True,'expectedCount':n,'screenedCount':n,'reviewedCount':0})
def pamo(year,number,rating,reason,title=None,statement=None,solution=None,topic=None,tags=None):
 ident=f'pamo_{year}_{number}';source=f'https://www.pamoofficial.org/problems/#pamo-{year}'
 entry=next(p for p in cov['ledger'] if p['id']==ident)
 entry.update(difficulty=rating,status='reviewed',included=1<=rating<=10 and (bool(statement) or any(x['id']==ident for x in data)),reason=reason)
 if entry['included'] and not statement:
  return  # Preserve the already restored canonical statement and solution.
 if entry['included']:
  p={k:entry[k] for k in ['id','country','competition','year','section','number','difficulty','sourceUrl']}
  p.update(title=title,statement=statement,solution=solution,solutionUrl=entry['sourceUrl'],topic=topic,tags=tags,ratingReason=reason,reviewStatus='individually-assessed',solutionKind='original',notes='Statement paraphrased from the official PAMO archive; proof independently checked. Individual editorial half-step difficulty rating.',provenance={'archive':'Official PAMO problem archive','originalOrganisation':'Pan-African Mathematics Olympiad'})
  p['subtopics']=classify(p);assert p['subtopics']
  existing=next((x for x in data if x['id']==ident),None)
  if existing:existing.update(p)
  else:data.append(p)
