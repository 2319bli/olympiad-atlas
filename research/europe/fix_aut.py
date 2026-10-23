import json
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text())
for f in p.glob('aut_2024_*.json'):
 d=json.loads(f.read_text());s=f.stem
 if s not in r:continue
 n=int(d['problem_number']);typ='JRW' if n<=4 else 'GWF' if n<=8 else 'ZWF' if n<=12 else 'BWF'
 # Official junior URL checked separately; leave existing link for its unchanged numbering.
 r[s]['number']=str(n if n<=4 else n-4 if n<=8 else n-8 if n<=12 else n-12)
 r[s]['notes']='Original question number verified against the official round paper.'
 if n>4:
  r[s]['sourceUrl']='https://www.math.aau.at/OeMO/problems/'+typ+'/2024';r[s]['solutionUrl']='https://www.math.aau.at/OeMO/solutions/'+typ+'/2024';r[s]['sourceName']='Austrian Mathematical Olympiad — official round paper'
 if n>12:r[s]['section']='National Competition—Final Round (Day '+str(1 if n<=15 else 2)+')'
s='aut_2024_final5';(p/(s+'.json')).write_text(json.dumps({'country':'Austria','competition':'Austrian Mathematical Olympiad','year':2024,'section':'National Competition—Final Round (Day 2)','problem_number':'5','problem_markdown':r'Positive integers $z_1,\ldots,z_n$ satisfy $z_j\le j$ and have even sum. Prove that signs can be chosen so that $z_1\pm z_2\pm\cdots\pm z_n=0$.','solutions_markdown':[],'booklet_title':'Official national final, Day 2'}))
r[s]={'difficulty':4,'topic':'Combinatorics','tags':['induction','signed sums'],'reason':'Induct by replacing the last two entries by their absolute difference; the bounds and parity survive.','sourceUrl':'https://www.math.aau.at/OeMO/problems/BWF/2024','solutionUrl':'https://www.math.aau.at/OeMO/solutions/BWF/2024#page=4','sourceName':'Austrian Mathematical Olympiad — official final solutions','solution':r'Induct on the list length; the empty list has sum zero. If the last two entries are equal, remove them and apply induction, then give them opposite signs. Otherwise replace them by their positive absolute difference. This is at most $n-1$, and the new total is still even, so induction applies to the resulting list of length $n-1$. Expanding the signed difference gives the required signs for the original two entries. Finally reverse all signs if necessary to make the first sign positive.'}
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
f=p/'build.py';t=f.read_text();t=t.replace(" if d['country']=='Austria':notes+=' Problem numbering follows the source booklet’s continuous numbering; the round is shown separately.'",'');f.write_text(t)
