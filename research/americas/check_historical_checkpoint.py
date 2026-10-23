"""Final local cleanup, exact archive inventory and independent finite proof checks.
Does not infer or assign ratings; all ratings are explicit in the review scripts.
Run after complete_jmo_2010_2014.py and the five complete_cmo_*.py batches.
"""
import json,re,sys
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import isqrt
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research'))
from subtopics import TAXONOMY
D=json.loads((R/'data/americas.json').read_text());C=json.loads((R/'research/americas-coverage.json').read_text())
for p in D:
 if p['id']=='ca-cmo-2002-2':p['subtopics']=['Divisibility & GCD']
 if p['id']=='ca-cmo-1979-3':p['subtopics']=['Divisibility & GCD','Induction','Extremal arguments']
 if p['id']=='ca-cmo-1984-2':p['solution']=p['solution'].replace('no nonidentity rotation or reflection preserves the colouring','no rotation or reflection that permutes the key positions nontrivially preserves the colouring')
 # Normalize accidental missing spaces in the newly written English prose, leaving math intact.
 if p['competition']=='CMO' and p['year']<=1993:
  for field in ['statement','solution','ratingReason','notes']:
   pieces=p[field].split('$')
   for i in range(0,len(pieces),2):
    pieces[i]=re.sub(r'(?<=[A-Za-z])(?=\d)|(?<=\d)(?=[A-Za-z])',' ',pieces[i])
   p[field]='$'.join(pieces)
assert len({p['id'] for p in D})==len(D)
for p in D:
 assert 4<=p['difficulty']<=7 and p['difficulty']*2==int(p['difficulty']*2),p['id']
 assert p.get('reviewStatus')=='individually-assessed',p['id']
 if p.get('subtopics'):assert set(p['subtopics'])<=set(TAXONOMY[p['topic']]),(p['id'],p['subtopics'])
for group in ['fullyScreened','partiallyScreened']:
 assert len({(p['competition'],p['year'],p.get('section')) for p in C[group]})==len(C[group])
# Finite angle case analysis used in the original proof of CMO1987Q3.
AA=[(2,1,0,1),(1,-1,0,0),(1,2,0,1)];BB=[(0,1,-1,0),(0,2,1,1),(0,1,2,1)];CC=[(2,1,1,1),(1,2,2,1),(1,-1,-1,0)]
angle_cases=[]
for ijk in product(range(3),repeat=3):
 M=[[F(x) for x in row] for row in [AA[ijk[0]],BB[ijk[1]],CC[ijk[2]]]]
 for col in range(3):
  pivot=next(i for i in range(col,3) if M[i][col]);M[pivot],M[col]=M[col],M[pivot]
  div=M[col][col];M[col]=[x/div for x in M[col]]
  for i in range(3):
   if i!=col:
    div=M[i][col];M[i]=[a-div*b for a,b in zip(M[i],M[col])]
 angles=[M[i][3] for i in range(3)]
 if min(angles)>0 and sum(angles)<1:angle_cases.append({'case':[i+1 for i in ijk],'anglesDegrees':[str(180*x) for x in angles]})
assert len(angle_cases)==7
# The finite square checks in CMO1993Q1 and explicit arrangements in CMO1992Q5.
triples=[(h,s,isqrt(s*s-h*h)) for h in range(1,28) for s in range(h+1,h+4) if isqrt(s*s-h*h)**2==s*s-h*h]
assert triples==[(3,5,4),(4,5,3),(8,10,6),(12,13,5),(12,15,9),(15,17,8),(24,25,7),(24,26,10)]
rows={3:[2,3,2,0,3,1,1],4:[2,4,2,3,0,4,3,1,1],7:[5,7,2,6,2,5,4,0,7,6,4,3,1,1,3],8:[7,8,4,2,6,2,4,7,0,8,6,5,3,1,1,3,5]}
for n,row in rows.items():
 assert len(row)==2*n+1 and row[n]==0
 for k in range(1,n+1):
  ix=[i for i,x in enumerate(row) if x==k];assert len(ix)==2 and ix[1]-ix[0]==k
# Inventory is exact to question number, even for papers not yet assessed.
index={(p['competition'],p['year']):p for p in C['fullyScreened']+C['partiallyScreened'] if p['competition'] in ['USAMO','USAJMO','CMO','CJMO']}
full={(p['competition'],p['year']) for p in C['fullyScreened']}
cmocount={1969:10,1970:10,1971:10,1972:10,1973:7,1974:7,1975:8,1976:8,1977:7,1978:6}
rows_inventory=[]
for comp,start in [('USAMO',1972),('USAJMO',2010),('CMO',1969),('CJMO',2020)]:
 for year in range(start,2027):
  count=(5 if year<=1995 else 6) if comp=='USAMO' else 6 if comp=='USAJMO' else cmocount.get(year,5) if comp=='CMO' else 5
  expected=[str(n) for n in range(1,count+1)];entry=index.get((comp,year));ratings=entry['ratings'] if entry else {}
  if isinstance(ratings,list):ratings={str(i+1):v for i,v in enumerate(ratings)}
  missing=[n for n in expected if n not in ratings]
  if (comp,year) in full:assert not missing,(comp,year,missing)
  assert set(ratings)<=set(expected),(comp,year)
  source=entry.get('source') if entry else (f'https://prase.cz/kalva/usa/usa{year%100:02d}.html' if year<=1995 else f'https://web.evanchen.cc/exams/USAMO-{year}-notes.pdf')
  rows_inventory.append({'competition':comp,'year':year,'questionCount':count,'assessedNumbers':sorted(ratings,key=int),'unratedNumbers':missing,'status':'complete' if not missing else 'partially-assessed' if ratings else 'not-yet-assessed','source':source,'sourceStatus':'reviewed' if entry else 'located in verified archive index; mathematical assessment pending'})
C['gaps'][1]='US: all USAJMO 2010–2026 and USAMO 2006–2025 papers fully screened. USAMO 1972–1995 Q1–5 and 1996–2005 Q1–6 remain unassessed (180 questions in34 papers), with usable historical archives located. USAMO2026 Q1 and Q3 remain held for incomplete source proofs. See research/americas/historical-inventory.json for exact year-by-year inventory.'
C['papersScreened']=len(C['fullyScreened']);C['problemAppearancesScreened']=sum(len(p['ratings']) for p in C['fullyScreened']+C['partiallyScreened']);C['uniqueIncluded']=len(D)
summary={'uniqueIncludedBeforeRootDuplicateMerge':len(D),'numericAssessments':C['problemAppearancesScreened'],'fullyAssessedPapers':C['papersScreened'],'priorityPapers':len(rows_inventory),'priorityQuestionTotal':sum(p['questionCount'] for p in rows_inventory),'priorityNumericAssessments':sum(len(p['assessedNumbers']) for p in rows_inventory),'priorityUnrated':sum(len(p['unratedNumbers']) for p in rows_inventory)}
inv={'asOf':'2026-10-23','scope':'USAMO1972–2026,USAJMO2010–2026,CMO1969–2026,CJMO2020–2026','summary':summary,'sources':[{'url':'https://cms.math.ca/competitions/cmo/','role':'Official papers for every CMO year and every CJMO year; worked-solution links from1994 onward.'},{'url':'https://prase.cz/kalva/usa.html','role':'John Scholes historical archive; index verifies five-question USAMO format1972–1995, six questions from1996, and links every year1972–2003. Independent wording and solutions, not an official MAA archive.'},{'url':'https://web.evanchen.cc/problems.html','role':'Author-maintained solution-note archive1996–2026 and all USAJMO years. Explicitly personal notes, not official committee solutions.'}],'papers':rows_inventory,'heldQuestions':{'CMO1969Q1':'Permitted zero denominator in published assertion.','CMO1974Q7':'Unstated common constant speed and junction/terminus interpretation need source clarification.','CMO1990Q5':'Conjectured run-length description not yet proved; no rating assigned.','CMO2001Q5':'At t=2sin15° or2sin75°, relevant points coincide and x/y is0/0.','USAMO2026Q1':'Source explicitly withdraws key argument.','USAMO2026Q3':'Source supplies no proof.'},'duplicateReview':{'exactForRootMerge':[{'newId':'ca-cmo-1971-10','existingId':'irmo-1989-7','reason':'Identical one-way information-sharing telephone model and2n−2 optimum.'}],'nearVariantNotMerged':[{'id1':'ca-cmo-1970-10','id2':'fist-1990-q1','reason':'Same factor-theorem idea but distinct forbidden value differences3 and7; not an exact affine transformation preserving arbitrary integer coefficients.'}]},'finiteProofChecks':{'CMO1987Q3':angle_cases,'CMO1993Q1':[list(x) for x in triples],'CMO1992Q5':'All four displayed arrangements verified position-by-position.'},'reproductionOrder':['complete_jmo_2010_2014.py','complete_cmo_2004_2009.py','complete_cmo_1996_2003.py','complete_cmo_1994_1995.py','complete_cmo_1969_1980.py','complete_cmo_1981_1993.py','check_historical_checkpoint.py']}
(R/'data/americas.json').write_text(json.dumps(D,ensure_ascii=False,indent=2)+'\n');(R/'research/americas-coverage.json').write_text(json.dumps(C,ensure_ascii=False,indent=2)+'\n');(R/'research/americas/historical-inventory.json').write_text(json.dumps(inv,ensure_ascii=False,indent=2)+'\n');print(json.dumps(summary));print('Canonical subtopics, assessment bounds, all complete paper inventories, 27 angle cases, finite triangle list and four card arrangements verified.')
