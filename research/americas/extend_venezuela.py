import json
from pathlib import Path
p=Path('/workspace/sites/olympiad-atlas');new=[];src='https://acmfiles.s3.amazonaws.com/A%C3%B1o%202023/ojm2023%20problemas%20y%20soluciones.pdf'
def add(n,comp,r,t,tags,s,sol,reason,appearances=None):
 d=dict(id=f've-ojm-final-{comp}-{2023}-{n}',country='Venezuela',competition='OJM Final '+comp,year=2023,number=str(n),statement=s,solution=sol,sourceUrl=src,solutionUrl=src,solutionKind='original-exposition',topic=t,tags=tags.split('|'),difficulty=r,ratingReason=reason,reviewStatus='individually-assessed',notes='Statement restated. The official ACM 2023 problem-and-solution volume, pages 68–71, was reviewed.')
 if appearances:d['appearances']=appearances
 new.append(d)
add(3,'Year 3',4,'Number theory','Digit sums|Carries|Congruences',r'Find the least positive integer $n$ for which both the decimal digit sum of $n$ and that of $n+1$ are multiples of 13.',r'''Let $s(m)$ denote digit sum. If $n$ ends in exactly $k$ nines, write $n=a10^k+(10^k-1)$, where $a$ does not end in 9. Then
$$s(n)=s(a)+9k,\qquad s(n+1)=s(a)+1.$$
Thus $9k-1\equiv0\pmod{13}$, or $k\equiv3\pmod{13}$. In particular $k\ge3$; the next possibility after 3 is 16, which would give a much larger number than the candidate below.

For $k=3$, we need $s(a)\equiv12\pmod{13}$ and $a$ must not end in 9. The least such $a$ is 48: a single digit cannot have sum 12; the smaller two-digit possibility 39 ends in 9. Hence the least candidate is $\boxed{48999}$. Its digit sum is 39, and $49000$ has digit sum 13, so it works.''','The main observation is that adding one changes digit sum according to the trailing run of nines. A congruence determines the shortest possible carry chain, then a small digit-minimisation argument is needed to prove global minimality.',[{'competition':'OJM Final Years 4–5','year':2023,'number':'2','country':'Venezuela'}])
add(4,'Year 3',4.5,'Combinatorics','Recurrences|Fibonacci numbers|Digit strings',r'How many ten-digit positive integers use only the digits $1,2,3,4$ and have every pair of adjacent digits differing by exactly 1?',r'''Let $a_n$ count valid strings of length $n$ ending in 1 or 4, and let $b_n$ count those ending in 2 or 3. Every outer-ending string has one continuation, with an inner digit; every inner-ending string has one continuation of each kind. Therefore
$$a_{n+1}=b_n,\qquad b_{n+1}=a_n+b_n,$$
with $a_1=b_1=2$. Iterating gives
$$(a_n,b_n)=(2,2),(2,4),(4,6),(6,10),(10,16),$$
$$ (16,26),(26,42),(42,68),(68,110),(110,178).$$
Thus there are $110+178=\boxed{288}$ ten-digit integers. No leading-zero restriction is needed because all allowed digits are nonzero.''','The apparent four-state adjacency problem collapses to two states by pairing the outer and inner digits. Discovering those states gives a coupled Fibonacci recurrence and a clean exhaustive count.')
add(4,'Years 4–5',4,'Algebra','Functional equations|Backward substitution|Powers of two',r'A function $f$ satisfies $f(a)+f(b)=n^2$ whenever positive integers $a,b,n$ satisfy $a+b=2^n$. Determine $f(2023)$.',r'''Choose complementary arguments which successively shrink to 1:
$$1+1=2,\quad7+1=8,\quad25+7=32,\quad2023+25=2048.$$
Consequently
$$2f(1)=1,\quad f(7)=9-f(1)=\frac{17}{2},$$
$$f(25)=25-f(7)=\frac{33}{2},$$
and finally
$$f(2023)=121-f(25)=\boxed{\frac{209}{2}}.$$
The successive complements 25,7,1 make it unnecessary to determine the entire function.''','The information is only given for pairs summing to powers of two. Working backwards from 2023 through successive complements 25,7,1 produces the required chain; the ensuing algebra is short.')
data=json.loads((p/'data/americas.json').read_text());ids={x['id'] for x in new};data=[x for x in data if x['id'] not in ids]+new;(p/'data/americas.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
c=json.loads((p/'research/americas-coverage.json').read_text())
for comp,rs in [('OJM Final Year 3',[3.5,2,4,4.5]),('OJM Final Years 4–5',[2,4,3.5,4])]:
 c['fullyScreened']=[x for x in c['fullyScreened'] if not(x['competition']==comp and x['year']==2023)];c['fullyScreened'].append(dict(competition=comp,year=2023,ratings=rs,source=src))
c['papersScreened']=len(c['fullyScreened']);c['problemAppearancesScreened']=sum(len(x['ratings']) for x in c['fullyScreened']+c['partiallyScreened']);c['uniqueIncluded']=len(data);c['gaps'].append('Venezuela: OJM Final 2023 Year 3 and shared Years 4–5 papers fully screened. The shared digit-sum question is one bank entry with both appearances. Other years and levels pending.')
(p/'research/americas-coverage.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');print('Total',len(data))
