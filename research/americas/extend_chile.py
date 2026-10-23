import json
from pathlib import Path
p=Path('/workspace/sites/olympiad-atlas');url='https://www.olimpiadadematematica.cl/index.php/pruebas-movil/category/17-pruebas-2021?download=47%3Afinal-2021-mayor';new=[]
def add(n,r,t,tags,s,sol,reason):new.append(dict(id=f'cl-onm-major-2021-{n}',country='Chile',competition='ONM Final — Senior',year=2021,number=str(n),statement=s,solution=sol,sourceUrl=url,solutionUrl='',solutionKind='original-exposition',topic=t,tags=tags.split('|'),difficulty=r,ratingReason=reason,reviewStatus='individually-assessed',notes='Official organizer paper recovered through its indexed text; organizer server intermittently returns 503/timeouts. Statement restated and solution independently derived.'))
add(2,4,'Combinatorics','Counting|Parity|Symmetry|Casework',r'Nine fixed positions form an X: a central position and four other positions on each of its two diagonals. Place the digits $1,2,\ldots,9$ in these positions, each once. Call the arrangement balanced when the sums on the two diagonals are equal. How many balanced arrangements are there? Rotations and reflections are counted as different arrangements.',r'''Let $c$ be the centre digit. The other eight digits split into two four-element sets with equal sum $(45-c)/2$, so $c$ must be odd. For $c=1,3,5$, the possible unordered splits can be represented by the following sets, with the complement supplying the other diagonal:

- $c=1$: $2389,2479,2569,2578$.
- $c=3$: $1479,1569,1578$.
- $c=5$: $1289,1379,1469,1478$.

Here, for example, $2389$ denotes $\{2,3,8,9\}$. These lists are obtained by requiring the displayed set to contain the smallest available digit and solving the required four-term sum; they exhaust all splits. Replacing each digit $d$ with $10-d$ gives four splits for $c=9$ and three for $c=7$.

Thus there are $4+3+4+3+4=18$ unordered splits across all possible centres. Choose which diagonal receives which set in $2$ ways, then order the four digits along each diagonal in $4!$ ways. The answer is $18\cdot2\cdot(4!)^2=\boxed{20736}$.''','The shared centre cancels from the balance condition, but its parity controls the count. A short, exhaustive subset-sum enumeration followed by diagonal assignment and ordering completes the count without overcounting symmetric placements.')
add(3,4.5,'Algebra','Polynomial identities|Lowest coefficient|Substitution',r'Find all polynomials $p$ with real coefficients such that $4p(x^2)=4p(x)^2+4p(x)-1$ for every real $x$.',r'''Put $q(x)=p(x)+\tfrac12$. The identity becomes $q(x^2)=q(x)^2$. The zero polynomial $q$ works. Otherwise write $q(x)=x^m h(x)$, where $m\ge0$ and $h(0)\ne0$. Cancelling $x^{2m}$ in the polynomial identity gives $h(x^2)=h(x)^2$. At zero, $h(0)=h(0)^2$, so $h(0)=1$.

Suppose $h$ is nonconstant, and let $cx^j$, $c\ne0$, be its lowest nonconstant term. On the right, the coefficient of $x^j$ is $2c$. On the left it is zero: if $j$ is odd there is no such power, and if $j$ is even the relevant coefficient in $h$ has smaller positive exponent $j/2$. This contradiction proves $h=1$.

Therefore the answers are $p(x)=-\tfrac12$ and $p(x)=x^m-\tfrac12$ for integers $m\ge0$. Direct substitution verifies them.''','A constant shift removes the linear term and reveals a multiplicative polynomial identity. After factoring out the lowest power of x, comparing the first nonconstant coefficient rules out every extra term; this also handles constants and the zero case cleanly.')
new[0]['appearances']=[dict(country='Chile',competition='ONM Final — Senior',year=2021,number='2'),dict(country='Chile',competition='ONM Final — Junior',year=2021,number='4')]
data=json.loads((p/'data/americas.json').read_text());ids={x['id'] for x in new};data=[x for x in data if x['id'] not in ids]+new
(p/'data/americas.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
c=json.loads((p/'research/americas-coverage.json').read_text());c['partiallyScreened']=[x for x in c['partiallyScreened'] if not(x['competition'].startswith('ONM Final') and x['year']==2021)]
c['partiallyScreened'] += [dict(competition='ONM Final — Senior',country='Chile',year=2021,ratings={'1':2.5,'2':4,'3':4.5},pending=['4'],source=url),dict(competition='ONM Final — Junior',country='Chile',year=2021,ratings={'1':2.5,'2':3,'4':4},pending=['3'],source=url.replace('47%3Afinal-2021-mayor','48%3Afinal-2021-menor'))]
c['problemAppearancesScreened']=sum(len(x['ratings']) for x in c['fullyScreened']+c['partiallyScreened']);c['uniqueIncluded']=len(data)
c['gaps'][-1]='Latin-American gaps: Chile 2021 junior/senior finals partially screened from indexed official papers; other Chile papers are blocked by intermittent organizer timeouts/503. Colombia, Peru, Venezuela, other national competitions, Ibero-American and Central American/Caribbean competitions remain pending. Cono Sur 2024 fully screened; other years pending.'
(p/'research/americas-coverage.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');print('Total',len(data))
