from pathlib import Path
import json,re,collections
p=Path('/workspace/sites/olympiad-atlas/research');raw=p/'international-raw';reviews=json.loads((p/'international-reviews.json').read_text());published={d['id']:d for d in json.loads((p.parent/'data/international.json').read_text())};coverage=json.loads((p/'international-coverage.json').read_text())
actual_exclusions={'imo_2022_34151b':('IMO','6'),'imo_2023_d4d6f3':('IMO','3'),'imo_2023_1fa49d':('IMO','6'),'imo_2024_95e706':('IMO','3'),'imo_2024_7579e8':('IMO','5'),'imo_2024_55cccf':('IMO','6'),'bmo_2023_e5c358':('Balkan Mathematical Olympiad','3'),'bmo_2023_be5fcc':('Balkan Mathematical Olympiad','4')}
names={'OIM':'Ibero-American Mathematical Olympiad','IZhO':'International Zhautykov Olympiad','RMM':'Romanian Master of Mathematics','BMO-SL':'Balkan MO Shortlist','IMO-SL':'IMO Shortlist','BW-SL':'Baltic Way Shortlist'}
body_names={'APMO':'Asia-Pacific','EGMO':'European Girls’ Olympiad','Balkan Mathematical Olympiad':'Balkan Olympiad','Balkan MO Shortlist':'Balkan Olympiad','JBMO':'Junior Balkan Olympiad','IMO':'International Mathematical Olympiad','IMO Shortlist':'International Mathematical Olympiad','Baltic Way':'Baltic Way','Baltic Way Shortlist':'Baltic Way','MEMO':'Middle European Olympiad','BxMO':'Benelux Olympiad','NMC':'Nordic Olympiad','Romanian Master of Mathematics':'Romanian Master of Mathematics','International Zhautykov Olympiad':'Zhautykov Olympiad','Ibero-American Mathematical Olympiad':'Ibero-American Olympiad'}
ledger=[]
for slug,(rating,reason) in reviews.items():
 d=json.loads((raw/(slug+'.json')).read_text());pub=published.get(slug)
 c=d.get('competition_code') or d.get('competition');n=(d.get('problem_number') or '').rstrip('.')
 c=names.get(c,c);n=re.sub(r'^(?:Problem\s*|P|№)(\d+)$',r'\1',n)
 if slug.startswith('jbm_2023_'):c='JBMO'
 if slug.startswith('bmo_2024_'):
  c='Balkan MO Shortlist'
  if n=='A6':c,n='Balkan Mathematical Olympiad','4'
 if slug in actual_exclusions:c,n=actual_exclusions[slug]
 if pub:c,n=pub['competition'],pub['number']
 ledger.append({'id':slug,'country':body_names.get(c,c),'competition':c,'year':d.get('year'),'section':'','number':n,'difficulty':rating,'decision':'included' if pub else 'outside-difficulty-band','ratingReason':reason,'sourceUrl':pub['sourceUrl'] if pub else d.get('officialSourceUrl','https://mathnet.mit.edu/explorer.html?p='+slug)})
papers=collections.defaultdict(list)
for d in ledger:papers[(d['competition'],d['year'])].append(d)
paper_sizes={'APMO':5,'EGMO':6,'BxMO':4,'JBMO':4,'NMC':4,'Romanian Master of Mathematics':6,'International Zhautykov Olympiad':6,'Ibero-American Mathematical Olympiad':6,'Balkan Mathematical Olympiad':4,'IMO':6,'Baltic Way':20}
paper_rows=[]
for (c,y),items in sorted(papers.items(),key=lambda q:(str(q[0][0]),str(q[0][1]))):
 nums={str(d['number']) for d in items};size=(7 if c=='IMO' and y in (1960,1962) else paper_sizes.get(c));expected={str(i) for i in range(1,size+1)} if size else None
 paper_rows.append({'competition':c,'year':y,'assessedNumbers':sorted(nums,key=lambda n:(not n.isdigit(),int(n) if n.isdigit() else n)),'assessedCount':len(items),'includedCount':sum(d['decision']=='included' for d in items),'expectedPaperSize':size,'paperFullyAssessed':bool(expected and expected<=nums),'remainingNumbers':sorted(expected-nums,key=int) if expected else None})
deferred={
'nmo_2019_c7777e':'Supplied regular-polygon proof makes an unsupported independent-set claim; not individually rated.',
'nmo_2017_af213c':'Regular-polygon solution still requires complete verification.',
'mem_2023_7ca8e4':'Figure-dependent chord construction requires additional original-source verification.',
'bmo_2024_eb762b':'Statement names the wrong moving line (XY versus ZT); original needed.',
'bmo_2024_5d4e8e':'Undefined points and inconsistent geometry in the extraction.',
'bmo_2024_16732a':'Inversion proof has unresolved extraction errors.',
'imo_2024_8acaec':'Supplied solution is for an entirely different set-divisibility problem.',
'btw_2023_39a6fd':'Grasshopper maximisation extraction omits the sharp bound and construction.',
'btw_2023_e551de':'Geometry statement is inconsistent: the alleged variable circle condition is automatic under the extracted midpoint hypotheses.',
'btw_2023_a662f5':'Geometry proof omits initial cyclicity steps needed for verification.',
'ibe_2001_461dd2':'Official spacecraft game statement located; no complete worked solution verified yet.',
'ibe_2001_94c52e':'Official five-congruent-squares covering question verified; the supplied solution has a fatal gap and is withheld pending a real proof.',
'ibe_2000_73ec10':'Official question asks for area below 3/2, whereas the extracted statement asks for the exact supremum; source proof omits required cases. Needs corrected complete assessment.'}
deferred_rows=[]
for slug,reason in deferred.items():
 if slug in reviews:continue
 f=raw/(slug+'.json');d=json.loads(f.read_text()) if f.exists() else {}
 deferred_rows.append({'id':slug,'competition':names.get(d.get('competition_code'),d.get('competition_code')),'year':d.get('year'),'number':d.get('problem_number'),'status':'pending-verification','reason':reason})
coverage.update({'decisions':ledger,'papers':[{'country':body_names.get(x['competition'],x['competition']),'competition':x['competition'],'year':x['year'],'section':'','complete':True} for x in paper_rows if x['paperFullyAssessed']], 'assessmentLedger':ledger,'excluded':[d for d in ledger if d['decision']!='included'],'paperCoverage':paper_rows,'fullyAssessedPapers':[{'competition':x['competition'],'year':x['year'],'questionCount':x['expectedPaperSize']} for x in paper_rows if x['paperFullyAssessed']],'deferred':deferred_rows,'downloadedRawCount':len(list(raw.glob('*.json'))),'solutionWithheldIds':[x['id'] for x in published.values() if not x.get('solution')],'discoveredArchivesPending':[{'competition':'Olympiade Francophone de Mathématiques','url':'https://ofm-officiel.org/historique/','status':'discovered-not-screened'},{'competition':'Historical IMO released papers','url':'https://www.imo-official.org/problems/','range':'1959 onward','status':'systematic historical screening in progress; not yet complete'}],'complete':False})
(p/'international-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
