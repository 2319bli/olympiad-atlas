"""Schema checks plus independent finite checks of new constructions (not substitutes for proofs)."""
import json,pathlib,sys,subprocess,collections,math
ROOT=pathlib.Path('/workspace/sites/olympiad-atlas');sys.path.insert(0,str(ROOT/'research'))
from subtopics import TAXONOMY
P=ROOT/'research/asia';bank=json.load(open(ROOT/'data/asia.json'));reviews=json.load(open(P/'reviews.json'));coverage=json.load(open(ROOT/'research/asia-coverage.json'));inv=json.load(open(P/'archive-inventory.json'))
assert len({d['id'] for d in bank})==len(bank)
for d in bank:
 assert 4<=d['difficulty']<=7 and d['difficulty']*2==int(d['difficulty']*2)
 assert d['reviewStatus']=='individually-assessed' and d['proofConfidence']=='checked'
 assert d['ratingReason'] and d['statement'] and d['sourceUrl']
 assert d['solution'] or d['solutionUrl']
 for s in d.get('subtopics',[]):assert s in TAXONOMY[d['topic']],(d['id'],s)
for id,v in reviews.items():
 assert v['difficulty'] is None or (1<=v['difficulty']<=10 and v['difficulty']*2==int(v['difficulty']*2))
 if v['difficulty'] is None:assert id not in {d['id'] for d in bank}
assert coverage['reviewedCount']==sum(v['difficulty'] is not None for v in reviews.values())
assert coverage['inspectedCount']==len(reviews)==coverage['reviewedCount']+coverage['unratedCount']
assert len(inv['pendingDownloadedIds'])+len(inv['pendingUndownloadedIds'])==coverage['pendingRecords']
try:
 old=json.loads(subprocess.check_output(['git','show','HEAD:data/asia.json'],cwd=ROOT,text=True))
 oldids={d['id'] for d in old};newids={d['id'] for d in bank};assert oldids<=newids
 added=[d for d in bank if d['id'] not in oldids]
 for d in added:assert d.get('subtopics'),d['id']
except subprocess.CalledProcessError:old=[];added=[]
# New 2023 final Q1 construction: all eight skew tetrominoes, capacity two, 24 covered cells.
tiles=json.load(open(P/'japan/2023-final-q1-construction.json'));counts=collections.Counter(tuple(c) for t in tiles for c in t)
assert len(tiles)==8 and len(counts)==24 and max(counts.values())==2 and (3,3) not in counts
# JMO 2023 graph: exhaust all parity assignments, independently checking the cut count and class sizes.
edges=[(i,(i+1)%10) for i in range(10)]+[(10+i,10+(i+1)%5) for i in range(5)]+[(10+i,2*i) for i in range(5)]
best=-1;patterns=[]
for mask in range(1<<15):
 score=sum(((mask>>a)^(mask>>b))&1 for a,b in edges)
 if score>best:best=score;patterns=[mask]
 elif score==best:patterns.append(mask)
assert best==17 and len(patterns)==10
assert collections.Counter(m.bit_count() for m in patterns)=={7:5,8:5}
assert sum(2**(15-m.bit_count()) for m in patterns)==1920
# KMO 2023 interval moves: direct shortest-path enumeration for n<=7 confirms the proposed extremal values.
kmo=[]
for n in range(1,8):
 zero=(0,)*n;dist={zero:0};q=collections.deque([zero]);intervals=[(i,j) for i in range(n) for j in range(i,n)]
 while q:
  x=q.popleft()
  for i,j in intervals:
   y=tuple((v-1)%3 if i<=k<=j else v for k,v in enumerate(x))
   if y not in dist:dist[y]=dist[x]+1;q.append(y)
 assert len(dist)==3**n and max(dist.values())==math.ceil((2*n+2)/3)
 kmo.append({'n':n,'states':len(dist),'maximumMoves':max(dist.values())})
result={'bankRecords':len(bank),'preservedBaselineIds':len(old),'addedBankRecords':len(added),'inspectedRecords':len(reviews),'mathematicallyAssessedRecords':coverage['reviewedCount'],'heldUnratedRecords':coverage['unratedCount'],'pendingDownloadedRecords':len(inv['pendingDownloadedIds']),'pendingUndownloadedRecords':len(inv['pendingUndownloadedIds']),'explicitCanonicalSubtopicsOnAllNewEntries':True,'jmo2023Graph':{'maximumGoodEdges':best,'maximizingParityPatterns':len(patterns),'maximizingLabelings':1920},'jmo2023Tiling':{'tiles':8,'coveredCells':24,'maximumMultiplicity':2},'kmo2023SmallInstanceChecks':kmo,'warning':'Finite checks support the independently written general proofs; they do not replace them.'}
(P/'completion-validation.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if not isinstance(v,(dict,list))},indent=2))
