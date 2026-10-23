import json,re,pathlib,collections,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from subtopics import classify
ROOT=pathlib.Path('/workspace/sites/olympiad-atlas'); P=ROOT/'research'/'asia'; raw=ROOT/'research'/'raw'/'asia'
reviews=json.loads((P/'reviews.json').read_text()); manifest=json.loads((P/'manifest.json').read_text()); bank=[]; screened=[]
for slug,v in reviews.items():
 rawpath=raw/(slug+'.json')
 if not rawpath.exists():rawpath=P/'extra'/(slug+'.json')
 d=json.loads(rawpath.read_text())
 comp=d['competition']; title=d.get('booklet_title') or ''; actual=d.get('competition_raw') or ''
 if 'selection of Indian Team' in title or re.search(r'Indija TS',actual,re.I): comp='Indian team selection tests'
 section=v.get('sectionOverride',d.get('section') or '')
 if 'Regional Mathematical Olympiad' in title and 'National Mathematical Olympiad' not in section: comp='Indian Regional Mathematical Olympiad (RMO)'
 if 'National Mathematical Olympiad' in section: comp='Indian National Mathematical Olympiad (INMO)'
 if d['country']=='Mongolia' and re.search(r'Round \d+',actual): comp='Mongolian Mathematical Olympiad — '+re.search(r'Round \d+',actual).group()
 comp=v.get('competitionOverride',comp)
 number=str(v.get('numberOverride',d['problem_number'])).strip().rstrip('.')
 country=d['country']; difficulty=v['difficulty']; included=difficulty is not None and 1<=difficulty<=10 and not v.get('omitReason')
 decision={'id':slug,'country':country,'competition':comp,'year':d['year'],'number':number,'section':section,'difficulty':difficulty,'included':bool(included),'reason':v.get('omitReason') or v['reason'],'sourceUrl':v.get('sourceUrl','https://mathnet.mit.edu/explorer.html?p='+slug),'reviewStatus':'held-unrated' if difficulty is None else 'individually-assessed','proofConfidence':v.get('proofConfidence','checked')}
 if v.get('duplicateOf'):decision['duplicateOf']=v['duplicateOf']
 screened.append(decision)
 if not included: continue
 statement=v.get('statementOverride',d['problem_markdown']); sol=v.get('solutionOverride',(d.get('solutions_markdown') or [''])[0]); kind='original-exposition' if v.get('solutionOverride') else 'sourced'
 if slug=='chn_2025_d18489': sol=sol.split('**Proof 2:**')[0].rstrip()+'\n$$'
 if slug=='chn_2021_978de9': sol=sol.replace('\\frac{17}{16}.\n$$','\\frac{17}{16}.\n\\end{aligned}\n$$')
 if slug=='chn_2022_e97c48': sol=re.sub(r"a'_(\d)\^2",r"{a'_\1}^2",sol)
 if (v.get('solutionKind')=='source-link' and not v.get('solutionOverride')) or (d.get('booklet_copyright_holder') and not v.get('solutionOverride')) or not sol: sol='';kind='source-link'
 statement=re.sub(r'\]\(images/','](https://mathnet.mit.edu/images/',statement); sol=re.sub(r'\]\(images/','](https://mathnet.mit.edu/images/',sol)
 topic=v.get('topic') or d.get('primary_domain') or (d.get('domains') or ['Other'])[0]
 if topic=='Analysis': topic='Algebra'
 if slug in ['chn_2025_d8572e','ind_2000_430770','ind_2007_02d2c2']:topic='Combinatorics'
 tags=v.get('tags',list(dict.fromkeys(x[-1] for x in d.get('topics',[]) if x)))
 notes=['Individually assessed from the statement and a solution or independent reasoning.', ('Source: MathNet transcription of ' if d.get('sourceDataset','MathNet')=='MathNet' else 'Source: ')+(title or comp)+'.']
 if v.get('note'):notes.append(v['note'])
 if v.get('solutionOverride'):notes.append('Worked solution rewritten and mathematically checked; transcription slips corrected.')
 if kind=='source-link':notes.append('Worked-solution link supplied; the source exposition has not been reproduced.')
 bank.append({'id':slug,'country':country,'competition':comp,'year':d['year'],'number':number,'section':section,'statement':statement,'solution':sol,'solutionKind':kind,'sourceUrl':decision['sourceUrl'],'solutionUrl':v.get('solutionUrl',decision['sourceUrl']),'topic':topic,'tags':tags,'difficulty':difficulty,'ratingReason':v['reason'],'reviewStatus':'individually-assessed','proofConfidence':v.get('proofConfidence','checked'),'subtopics':v.get('subtopics',[]),'notes':notes,'sourceDataset':d.get('sourceDataset','MathNet'),'sourceLicense':d.get('sourceLicense','MathNet CC BY 4.0; original national rights may apply'),'sourceBooklet':title or None})
# Preserve documented alternate paper appearances, including newly published levels.
by_id={x['id']:x for x in screened}
for row in bank:
 row['subtopics']=classify(row)
 for duplicate in screened:
  if duplicate.get('duplicateOf')==row['id']:
   appearance={k:duplicate[k] for k in ['country','competition','year','section','number','sourceUrl']}
   if appearance not in row.setdefault('appearances',[]):row['appearances'].append(appearance)
oldbank={x['id']:x for x in json.loads((ROOT/'data'/'asia.json').read_text())} if (ROOT/'data'/'asia.json').exists() else {}
for row in bank:
 old=oldbank.get(row['id'],{})
 for key in ['subtopics','alternateAppearances','diagram','diagramUrl']:
  if old.get(key) and not row.get(key):row[key]=old[key]
(ROOT/'data').mkdir(exist_ok=True);(ROOT/'data'/'asia.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2))
papers=collections.defaultdict(list)
for d in screened:
 if d['country']=='Malaysia':
  appearances=re.search(r'Original appearance: \d+ IMONST 2, (.*?)\.',reviews[d['id']].get('note',''))
  if appearances:
   for appearance in appearances.group(1).split(' / '):
    category,num=appearance.rsplit(' ',1)
    papers[('Malaysia','IMONST 2 — '+category,d['year'],category)].append(dict(d,number=num))
   continue
 papers[(d['country'],d['competition'],d['year'],d['section'])].append(d)
# Identical tasks appear in several grade papers; count each documented appearance
# for paper coverage while keeping only one question-bank entry.
kaz9q6=next((d for d in screened if d['id']=='kaz_2024_national_g9_q6'),None)
if kaz9q6:
 papers[('Kazakhstan','Kazakhstan National Mathematical Olympiad — Grade 10',2024,'Grade 10')].append(dict(kaz9q6,number='5'))
 papers[('Kazakhstan','Kazakhstan National Mathematical Olympiad — Grade 11',2024,'Grade 11')]=list(papers[('Kazakhstan','Kazakhstan National Mathematical Olympiad — Grade 10',2024,'Grade 10')])
paperlist=[]
for k,rows in sorted(papers.items()):
 complete=(k[0]=='Malaysia' and len(rows)==6) or (k[0]=='Kazakhstan' and k[2]==2024 and len(rows)==6) or (k[0]=='Indonesia' and ((k[2] in [2021,2022] and len(rows)==8) or (k[2]==2024 and len(rows)==(4 if k[3]=='Provincial proof' else 8)))) or (k[0]=='Israel' and k[1]=='Gillis Mathematical Olympiad' and k[2]==2023 and len(rows)==7) or (k[0]=='Sri Lanka' and k[2]==2018 and len(rows)==30) or (k[0]=='India' and k[1]=='Indian National Mathematical Olympiad (INMO)' and k[2] in [2012,2013,2014,2015,2017,2019,2020,2021,2023,2024] and set(re.sub(r'[^0-9]','',d['number']) for d in rows)==set(map(str,range(1,7))))
 complete=complete and all(d['difficulty'] is not None for d in rows)
 if k[0]=='Japan' and k[2] in [2023,2024]:
  expected=12 if k[3].lower()=='first round' else 5 if k[3].lower()=='final round' else None
  complete=expected is not None and set(d['number'] for d in rows)==set(map(str,range(1,expected+1))) and all(d['difficulty'] is not None for d in rows)
 paperlist.append({'country':k[0],'competition':k[1],'year':k[2],'section':k[3],'assessed':sum(d['difficulty'] is not None for d in rows),'reviewedRecords':len(rows),'heldUnrated':sum(d['difficulty'] is None for d in rows),'included':sum(d['included'] for d in rows),'reviewedQuestionNumbers':[d['number'] for d in rows],'complete':complete,'scope':'All tasks in the original paper/section individually mathematically assessed, including exclusions. Identical appearances may share one bank entry.' if complete else 'Available records reviewed individually; original-paper completeness not asserted.'})
# Manifest scope can contain either row arrays or dictionaries; preserve exact pending IDs.
ids=[x[0] if isinstance(x,list) else x.get('slug',x.get('id')) for x in manifest]
coverage={'region':'Asia','ratingScale':'1–10 in half-point steps; all reviewed difficulties included, with 4–7 the preferred browsing range','reviewMethod':'Each decision was made after reading the individual statement and solution or independently deriving the key argument. No rating inferred from position, contest name, text length, or source labels.','discoveredRecords':len(ids),'inspectedCount':len(reviews),'reviewedCount':sum(v['difficulty'] is not None for v in reviews.values()),'unratedCount':sum(v['difficulty'] is None for v in reviews.values()),'includedCount':len(bank),'reviewedRecords':len(reviews),'assessedRecords':sum(v['difficulty'] is not None for v in reviews.values()),'heldUnratedRecords':sum(v['difficulty'] is None for v in reviews.values()),'includedRecords':len(bank),'pendingRecords':len(set(ids)-set(reviews)),'status':'In progress: comprehensive coverage is not yet achieved.','papers':paperlist,'decisions':screened,'pendingIds':sorted(set(ids)-set(reviews)),'knownGaps':['China 2024 CMO: Q4 absent; the five available questions are individually assessed.','China Girls 2002: Q4 is absent; Q2 transcription contains only part (1) and is held unrated as incomplete.','Japan 2022: first-round Q3 and Q6 and final Q5 absent from the discovered transcription; final Q3 is held unrated for a centre-identification gap.','South Korea 2023 national final: Q3 and Q4 absent from the discovered transcription.','Known MathNet backlog remains; full national histories are not claimed. Exact available-paper and country inventory is in research/asia/archive-inventory.json.','India 2003 available archive has five INMO problems; Q6 absent.','China 2025 archive has 23 selection-test problems; completeness of original 24-problem sequence not established.','Generic MathNet competition labels misidentify some Indian selection papers as INMO; corrected using original booklet title.','Some transcriptions are withheld for false or incomplete statements; exact exclusions are recorded.']}
# Historical completeness checks and download inventory must survive a range-policy rebuild.
preserved=json.loads((P/'coverage-preserved.json').read_text()) if (P/'coverage-preserved.json').exists() else {}
key=lambda x:(x.get('country'),x.get('competition'),x.get('year'),x.get('section') or '')
completion={key(x):x for x in preserved.pop('paperCompletion',[])}
for paper in coverage['papers']:
 if key(paper) in completion:
  paper['complete']=completion[key(paper)]['complete']
  if completion[key(paper)].get('scope'):paper['scope']=completion[key(paper)]['scope']
coverage.update(preserved)
for paper in coverage.get('completeDownloadedPaperSets',[]):
 paper['includedRecords']=sum(1 for row in bank if key(row)==key(paper))
(ROOT/'research'/'asia-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2));print('inspected',len(reviews),'assessed',coverage['assessedRecords'],'held',coverage['heldUnratedRecords'],'included',len(bank),'pending',coverage['pendingRecords'])
