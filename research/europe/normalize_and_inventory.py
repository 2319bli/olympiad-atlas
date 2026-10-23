import json,re
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text())
for slug,x in r.items():
 d=json.loads((p/(slug+'.json')).read_text());c=d['country'];sec=x.get('section',d.get('section')) or ''
 if c=='Germany':x['competition']='German IMO Selection Tests';x['section']='Selection test '+('2' if '2' in sec else '1')
 if c=='Netherlands':x['competition']='Dutch Team Selection Tests'
 if c=='Poland':
  for a,b in [('10 lutego 2023 r. (pierwszy dzień zawodów)','Second round, day 1 (10 February 2023)'),('11 lutego 2023 r. (drugi dzień zawodów)','Second round, day 2 (11 February 2023)'),('29 marca 2023 r. (pierwszy dzień zawodów)','Final round, day 1 (29 March 2023)'),('30 marca 2023 r. (drugi dzień zawodów)','Final round, day 2 (30 March 2023)')]:
   if sec==a:x['section']=b
 if c=='Serbia':x['section']={'Први дан':'Day 1','Други дан':'Day 2'}.get(sec,sec)
 if c=='Romania':
  g=re.search(r'(\d+)(?:th|st|nd|rd)',sec,re.I)
  if g:x['section']='National Final — Grade '+g[1]
 if c=='Slovenia' and 'Technical Schools' in x.get('competition',d['competition']):x['sourceUrl']='https://mathnet.mit.edu/explorer.html?p='+slug
 if slug=='rus_2025_cd1fbb':x['difficulty']=None;x['reason']='Unrated and withheld: a layered distance count gives an upper bound, but the sole sharp Hamilton-cycle construction is a diagram not yet independently verified.'
 n=str(x.get('number',d['problem_number']));n=re.sub(r'^(Problem|Opgave|Aufgabe)\s+','',n,flags=re.I);n=re.sub(r'\.\s*$','',n);x['number']=n
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
