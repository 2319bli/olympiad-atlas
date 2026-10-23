import json
from pathlib import Path
p=Path('/workspace/sites/olympiad-atlas')
src='https://oc.uan.edu.co/images/Olimpiadas/Matematicas/documentos/2020/nspSel.pdf'
new=[]
def add(n,r,t,tags,s,sol,reason):
 new.append(dict(id=f'co-ocm-selectiva-superior-2017-{n}',country='Colombia',competition='Colombian Mathematical Olympiad, Superior Selection Round',year=2017,number=str(n),statement=s,solution=sol,sourceUrl=src,solutionUrl=src,solutionKind='original-exposition',topic=t,tags=tags.split('|'),difficulty=r,ratingReason=reason,reviewStatus='individually-assessed',notes='Primary organizer PDF is dated 4 April 2017 despite its website directory being named 2020. This is the selection round, not the national final. Originally a numerical-answer problem; statement restated and proof independently supplied.'))
add(10,4,'Number theory','Digit sums|Congruences|Decimal carries',r'Two consecutive positive integers both have digit sums divisible by $7$. What is the smallest possible number of digits in the smaller integer?',r'''Let the smaller integer $N$ end in exactly $k$ nines. Increasing it by one changes its digit sum by $1-9k$, including when all its digits are nines. Thus
$$1-9k\equiv0\pmod7,$$
so $k\equiv4\pmod7$ and in particular $k\ge4$.

An integer of fewer than four digits is impossible. The only four-digit candidate is $9999$, whose digit sum is $36$, not divisible by $7$. Five digits suffice: $69999$ has digit sum $42$, while $70000$ has digit sum $7$. The answer is therefore $\boxed5$.''','The key is to express the change in digit sum using the number of trailing nines, then solve a congruence and check the boundary case. The proof is short once the decimal-carry invariant is found.')
add(12,5,'Combinatorics','Truth tellers and liars|Binary recurrence|Extremal principle',r'An island has $2017$ inhabitants, each either always truthful or always lying. More than $1000$ of them attend a banquet, sitting around a circular table. Every guest says: “Of my two neighbours, one is truthful and the other is a liar.” What is the product of the digits of the greatest possible number of truthful inhabitants on the island?',r'''Write $x_i=1$ for a truthful guest and $x_i=0$ for a liar, with indices taken cyclically. The guest's statement is true exactly when the two neighbours have different types. Thus, working modulo $2$,
$$x_i=x_{i-1}+x_{i+1},\qquad x_{i+1}=x_{i-1}+x_i.$$
The recurrence gives $x_{i+3}=x_i$. Starting with two zeros gives all zeros; every other starting pair gives a cyclic repetition of $011$. Consequently a banquet containing any truthful guests has a number of guests divisible by $3$, with exactly one third of them liars.

The smallest multiple of $3$ greater than $1000$ is $1002$, so such a banquet requires at least $334$ liars. A banquet consisting entirely of liars requires at least $1001$ liars and cannot improve this bound. Hence the island has at most $2017-334=1683$ truthful inhabitants.

This bound is attained by seating $1002$ guests in the repeating pattern liar–truthful–truthful and making all $1015$ inhabitants outside the banquet truthful. The requested product is $1\cdot6\cdot8\cdot3=\boxed{144}$.''','Turning the logical statements into a binary recurrence reveals a period-three classification. One must then distinguish the all-liar case and optimize the number of required liars among banquet sizes greater than 1000.')
data=json.loads((p/'data/americas.json').read_text());ids={x['id'] for x in new};data=[x for x in data if x['id'] not in ids]+new
(p/'data/americas.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
c=json.loads((p/'research/americas-coverage.json').read_text())
c['fullyScreened']=[x for x in c['fullyScreened'] if x['competition']!='Colombian Mathematical Olympiad, Superior Selection Round']
c['fullyScreened'].append(dict(competition='Colombian Mathematical Olympiad, Superior Selection Round',year=2017,ratings={str(i+1):r for i,r in enumerate([2,1,2.5,3.5,2,2.5,2.5,2.5,2,4,3.5,5])},source=src,exclusionNotes={'1':'Two 60-degree sectors; routine area fraction.','2':'Direct scale conversion.','3':'The fractional-linear recurrence repeats after three terms.','4':'List powers of two between 100 and 999 and count digit pairs by their sum.','5':'Four corner tetrahedra each have one eighth of the original volume.','6':'Pythagoras determines the hypotenuse; the perimeter then determines the leg product.','7':'A short sign split in two absolute-value equations.','8':'Check the three possible truth/lie patterns against a two-digit number.','9':'The centre triangle has side lengths 30, 40, 50.','11':'Relative to the central value the total offset is even and at most 12 in magnitude; this forces the centre to be 56.'}))
c['papersScreened']=len(c['fullyScreened']);c['problemAppearancesScreened']=sum(len(x['ratings']) for x in c['fullyScreened']+c['partiallyScreened']);c['uniqueIncluded']=len(data)
c['gaps'][6]='Latin-American gaps: Chile 2021 junior/senior finals partially screened from indexed official papers; other Chile papers are blocked by intermittent organizer timeouts/503. Bolivia and other national competitions remain pending except as separately listed. Cono Sur 2024 fully screened; Ibero-American 2024/2025 partially screened. Other regional years pending.'
c['gaps'].append('Colombia: official Superior Selection Round 2017 fully screened (12 questions). National final rounds and other selection years remain pending. The archive URL directory says 2020, but the examination itself unambiguously says 4 April 2017.')
(p/'research/americas-coverage.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
print('Total',len(data))
