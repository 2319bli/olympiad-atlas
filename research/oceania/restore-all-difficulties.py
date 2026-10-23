"""Restore reviewed out-of-band questions without assigning any new ratings."""
import json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(R/'research'))
from subtopics import classify
bank=json.loads((R/'data/oceania-africa.json').read_text())
coverage=json.loads((R/'research/oceania-africa-coverage.json').read_text())
ids={p['id'] for p in bank}
fixes=json.loads((R/'research/oceania/fixes.json').read_text())
topic_fixes={
 'nzl_2019_00434c':'Combinatorics','nzl_2019_f86e01':'Combinatorics',
 'nzl_2020_97b090':'Number Theory','nzl_2021_808aa5':'Number Theory',
 'nzl_2022_53ca7a':'Combinatorics','nzl_2023_8e18b1':'Number Theory',
 'nzl_2023_e4670b':'Number Theory','nzl_2024_3bea94':'Number Theory',
 'zaf_2010_da2c8f':'Number Theory','zaf_2015_f14502':'Number Theory',
 'zaf_2016_dbac7f':'Number Theory','zaf_2019_edda11':'Combinatorics',
 'zaf_2021_4c44fd':'Number Theory','zaf_2022_0249f3':'Combinatorics',
}
explicit={
 'nzl_2019_00434c':['Counting','Divisibility & GCD'],
 'nzl_2019_f86e01':['Counting','Digits & bases'],
 'nzl_2020_97b090':['Valuations','Factorials & binomial coefficients'],
 'nzl_2021_808aa5':['Diophantine equations','Primes','Divisibility & GCD'],
 'nzl_2022_53ca7a':['Pairing','Modular arithmetic','Algorithms & constructions'],
 'nzl_2023_8e18b1':['Factorials & binomial coefficients','Squares & powers'],
 'nzl_2023_e4670b':['Integer polynomials','Modular arithmetic','Primes'],
 'nzl_2024_3bea94':['Digits & bases','Diophantine equations'],
 'zaf_2010_da2c8f':['Digits & bases','Diophantine equations'],
 'zaf_2015_f14502':['Primes','Modular arithmetic'],
 'zaf_2016_dbac7f':['Digits & bases','Fractions & approximation'],
 'zaf_2019_edda11':['Counting','Extremal arguments'],
 'zaf_2021_4c44fd':['Digits & bases','Modular arithmetic'],
 'zaf_2022_0249f3':['Counting','Combinatorial geometry'],
}
def clean(s):return re.sub(r'\]\(images/','](https://mathnet.mit.edu/images/',s or '')
for review in coverage['ledger']:
 ident=review['id']
 if ident in ids or review['status']!='reviewed' or review.get('difficulty') is None:continue
 raw=R/'research/oceania/full'/f'{ident}.json'
 if not raw.exists():continue
 source=json.loads(raw.read_text())
 tags=list(dict.fromkeys(t for path in source.get('topics',[]) for t in path[2:]))
 problem={k:review[k] for k in ['id','country','competition','year','section','number','difficulty','sourceUrl'] if k in review}
 problem.update(statement=clean(source['problem_markdown']),solution=clean('\n\n'.join(source.get('solutions_markdown',[]))),
  solutionUrl=review['sourceUrl'],topic=topic_fixes.get(ident,source['primary_domain']),tags=tags,
  ratingReason=review['reason'],reviewStatus='individually-assessed',solutionKind='sourced',
  notes='MathNet transcription; original competition organiser credited in the source. Individual difficulty assessment retained unchanged; restored after removal of the 4–7 publication cutoff.',
  provenance={'archive':'MathNet','slug':ident,'originalOrganisation':'NZMOC' if review['country']=='New Zealand' else 'SAMF'})
 if ident in fixes:problem.update(fixes[ident])
 if ident=='nzl_2024_250d62':problem['statement']='A shop sells two golf balls for 25 cents, a hat for one dollar, and a club for ten dollars. Ross buys exactly 100 items for 100 dollars, including at least one item of each type. How many hats does he buy?'
 if ident=='zaf_2016_2858c2':
  problem['statement']=r'For real $a,b$ with $b>0$, the roots of $x^2+ax+a=b$ together with those of $x^2+ax+a=-b$ are four consecutive integers. Determine all possible pairs $(a,b)$.'
 if ident=='zaf_2016_3fc13e':
  problem['statement']=r'The incircle of $ABC$ has centre $I$ and touches $BC,CA,AB$ at $D,E,F$. A point $P$, on the same side of $FE$ as $A$, satisfies $\angle PFE=\angle BCA$ and $\angle PEF=\angle ABC$. Prove that $P,I,D$ are collinear.'
 if source.get('booklet_copyright_holder'):
  problem['solution']=None;problem['solutionKind']='source-link'
 if ident in explicit:problem['subtopics']=explicit[ident]
 if not problem.get('subtopics'):problem['subtopics']=classify(problem)
 bank.append(problem);ids.add(ident)

for extra in sorted((R/'research/oceania').glob('restored-*-statements.json')):
 for problem in json.loads(extra.read_text()):
  ident=problem['id'];review=next(x for x in coverage['ledger'] if x['id']==ident)
  assert review['status']=='reviewed' and review['difficulty'] is not None
  p={k:review[k] for k in ['id','country','competition','year','section','number','difficulty','sourceUrl'] if k in review}
  p.update(problem)
  if p.get('ratingReasonOverride') and review['reason']!=p['ratingReasonOverride']:
   review.setdefault('originalReasonBeforeSourceCorrection',review['reason']);review['reason']=p['ratingReasonOverride']
  p['difficulty']=review['difficulty'];p['ratingReason']=p.pop('ratingReasonOverride',review['reason']);p['reviewStatus']='individually-assessed'
  if p.get('solution'):p.setdefault('solutionKind','original-exposition')
  elif p.get('solutionUrl'):p['solutionKind']='source-link'
  p.setdefault('notes','Mathematical statement independently paraphrased from the linked paper. Individual numerical assessment retained unchanged from the review ledger.')
  assert p.get('statement') and p.get('subtopics')
  if ident in ids:bank=[p if x['id']==ident else x for x in bank]
  else:bank.append(p);ids.add(ident)

for p in bank:
 if p['id']=='nzl_2024_0eee35':p.update(topic='Combinatorics',subtopics=['Colouring','Extremal arguments'])
 if p['id']=='zaf_2020_93adcb':p.update(topic='Combinatorics',subtopics=['Invariants','Sequences & recurrences'])
 if p['id']=='zaf_2024_d17f15':p.update(topic='Algebra',subtopics=['Inequalities','Algebraic identities'])
 assert isinstance(p['difficulty'],(int,float)) and 1<=p['difficulty']<=10
for review in coverage['ledger']:review['included']=review['id'] in ids
coverage['includedCount']=len(bank)
coverage['rangeRestoration']={'baselineIncludedCount':291,'restoredCount':len(bank)-291,'preferredRange':[4,7],'eligibleRange':[1,10],'ratingsChanged':0,'remainingReviewedStatementRecoveries':0,'numericSourceHolds':['nzl_2021_e1429c','nzl_2025_855484','zaf_2014_5b73c0','zaf_2015_481919'],'duplicateAppearance':'pamo_2022_1'}
coverage['scale']='1–10 in half steps; all individually assessed questions are eligible. Preferred browsing range 4–7: 4=lower hard BMO1;5–6=core hard BMO1;7=upper accessible BMO2. Editorial estimates, not measured empirical ratings.'
coverage['countDefinitions']['includedCount']='Unique published problem records, across the full 1–10 scale; 4–7 is only the preferred browsing range.'
coverage['restorationPendingIds']=[x['id'] for x in coverage['ledger'] if x['status']=='reviewed' and x.get('difficulty') is not None and x['id'] not in ids]
(R/'data/oceania-africa.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n')
(R/'research/oceania-africa-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+'\n')
print('Published',len(bank),'Remaining reviewed statement recoveries',len(coverage['restorationPendingIds']))
