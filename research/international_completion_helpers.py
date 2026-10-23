import json,collections,sys
from pathlib import Path
ROOT=Path('/workspace/sites/olympiad-atlas'); R=ROOT/'research'
sys.path.insert(0,str(R));from subtopics import classify
rows=json.loads((ROOT/'data/international.json').read_text());reviews=json.loads((R/'international-reviews.json').read_text());coverage=json.loads((R/'international-coverage.json').read_text());ledger=coverage['assessmentLedger']
def add(year,num,topic,rating,reason,statement,solution,tags,proof_url=None):
 slug=f'imo_{year}_official_p{num}'; url=f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf'; proof_url=proof_url or f'https://prase.cz/kalva/imo/isoln/isoln{str(year)[2:]}{num}.html'
 if slug in reviews:return
 raw={'id':slug,'competition_code':'IMO','competition':'IMO','year':year,'problem_number':str(num),'primary_domain':topic,'topics':[[topic,t] for t in tags],'problem_markdown':statement,'solutions_markdown':[solution],'officialSourceUrl':url,'officialSolutionUrl':proof_url,'reviewNote':'Official released paper checked. Mathematical statement paraphrased; original worked exposition checked independently, with John Scholes’s worked solution as a comparison source.'}
 (R/'international-raw'/f'{slug}.json').write_text(json.dumps(raw,ensure_ascii=False,indent=2));reviews[slug]=[rating,reason]
 decision={'id':slug,'country':'International Mathematical Olympiad','competition':'IMO','year':year,'section':'Main paper','number':str(num),'difficulty':rating,'decision':'included' if 4<=rating<=7 else 'outside-difficulty-band','ratingReason':reason,'reviewStatus':'individually-assessed','sourceUrl':url,'solutionUrl':proof_url,'assessmentEvidence':solution}
 ledger.append(decision)
 if 4<=rating<=7:
  row={'id':slug,'country':'International','competition':'IMO','year':year,'section':'Main paper','number':str(num),'statement':statement,'solution':solution,'sourceUrl':url,'solutionUrl':proof_url,'topic':topic,'tags':tags,'difficulty':rating,'ratingReason':reason,'reviewStatus':'individually-assessed','notes':raw['reviewNote'],'provenance':{'collection':'Official contest archive','bookletTitle':f'International Mathematical Olympiad {year}','section':'Main paper','originalExposition':True}}
  row['subtopics']=classify(row);assert row['subtopics'],slug;rows.append(row)
def save():
 (ROOT/'data/international.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2));(R/'international-reviews.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2))
 groups=collections.defaultdict(list)
 for d in ledger:groups[(d['competition'],d['year'])].append(d)
 sizes={'APMO':5,'EGMO':6,'BxMO':4,'JBMO':4,'NMC':4,'Romanian Master of Mathematics':6,'International Zhautykov Olympiad':6,'Ibero-American Mathematical Olympiad':6,'Balkan Mathematical Olympiad':4,'IMO':6,'Baltic Way':20}
 papers=[]
 for (c,y),items in sorted(groups.items(),key=lambda x:(str(x[0][0]),str(x[0][1]))):
  nums={str(d['number']) for d in items};size=7 if c=='IMO' and y in (1960,1962) else 8 if c=='EGMO' and y==2012 else sizes.get(c);expected={str(i) for i in range(1,size+1)} if size else None
  papers.append({'competition':c,'year':y,'assessedNumbers':sorted(nums,key=lambda n:(not n.isdigit(),int(n) if n.isdigit() else n)),'assessedCount':len(items),'includedCount':sum(d['decision']=='included' for d in items),'expectedPaperSize':size,'paperFullyAssessed':bool(expected and expected<=nums),'remainingNumbers':sorted(expected-nums,key=int) if expected else None})
 coverage.update({'reviewedCount':len(ledger),'includedCount':len(rows),'assessmentLedger':ledger,'decisions':ledger,'reviewedIds':[d['id'] for d in ledger],'excluded':[d for d in ledger if d['decision']!='included'],'paperCoverage':papers,'fullyAssessedPapers':[{'competition':x['competition'],'year':x['year'],'questionCount':x['expectedPaperSize']} for x in papers if x['paperFullyAssessed']],'papers':[{'country':'International','competition':x['competition'],'year':x['year'],'section':'','complete':True} for x in papers if x['paperFullyAssessed']],'byCompetition':dict(collections.Counter(d['competition'] for d in rows)),'complete':False})
 (R/'international-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
 if (R/'international_inventory.py').exists():
  import runpy
  runpy.run_path(str(R/'international_inventory.py'))
 print({'reviewed':len(ledger),'included':len(rows),'completePapers':sum(x['paperFullyAssessed'] for x in papers)})
