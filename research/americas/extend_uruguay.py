import json
from pathlib import Path
p=Path('/workspace/sites/olympiad-atlas');new=[]
sources={(2017,'V'):'https://drive.google.com/file/d/1rWAk6EkR96oxj-XoQDycsXRJY1j9W8kW/view',(2017,'IV'):'https://drive.google.com/file/d/113mP5KbUDldF0i7Ef1MfV_O7t3f9wMnp/view',(2016,'V'):'https://drive.google.com/file/d/1-x0dZV1RDSgy8ZPmwmTkPZHiyOxEGDs4/view'}
def add(y,l,n,r,t,tags,s,sol,reason,note=''):
 src=sources[y,l]
 new.append(dict(id=f'uy-onm-final-{l.lower()}-{y}-{n}',country='Uruguay',competition=f'Uruguayan National Mathematical Olympiad Final Level {l}',year=y,number=str(n),statement=s,solution=sol,sourceUrl=src,solutionUrl=src,solutionKind='original-exposition',topic=t,tags=tags.split('|'),difficulty=r,ratingReason=reason,reviewStatus='individually-assessed',notes='Primary organizer paper linked from https://www.fonmat.org.uy/nacional/final/nivel-'+l+'. Statement restated and solution independently derived. '+note))
add(2017,'V',2,5.5,'Combinatorics','Pascal triangle|Binary representation|Parity|Generating functions',r'Write Pascal’s triangle from row $0$, consisting of a single $1$, through row $2047$, whose entries are $\binom{2047}{k}$. How many odd entries are written?',r'''The answer is $\boxed{3^{11}=177147}$.

Over coefficients modulo $2$, repeated squaring gives $(1+x)^{2^j}=1+x^{2^j}$. If the binary expansion of $n$ has its $1$ digits in a set $J$, then
$$(1+x)^n=\prod_{j\in J}(1+x^{2^j})\pmod2.$$
The exponents obtained by choosing terms in this product are all distinct, since binary expansions are unique. Hence row $n$ has exactly $2^{|J|}$ odd entries.

The integers from $0$ through $2047=2^{11}-1$ correspond to every choice of eleven binary digits. Summing the odd-entry counts therefore gives
$$\sum_{J\subseteq\{0,\ldots,10\}}2^{|J|}=(1+2)^{11}=3^{11}.$$''','The central discovery is the binary structure of binomial coefficients modulo 2. Proving that structure by polynomial factorization and then summing across all eleven-bit rows gives a compact but nonroutine solution.','The original diagram was inspected to verify that its “row 5” is the row 1,5,10,10,5,1, so row numbering begins at 0.')
add(2017,'V',3,5.5,'Geometry','Excircles|Power of a point|Heron formula|Coordinates',r'Let $I$ be the incentre of an acute triangle $ABC$. Its excircle opposite $C$ touches $AB$ at $D$. The line $DI$ meets this excircle again at $S$, and $P$ is the midpoint of $DI$. Prove that $P,A,S,B$ are concyclic.',r'''Put $a=BC$, $b=CA$, $c=AB$, and $s=(a+b+c)/2$. Let the inradius be $r$, the radius of the excircle opposite $C$ be $R$, and the triangle’s area be $\Delta$. Tangent lengths and Heron’s formula give
$$DA\cdot DB=(s-a)(s-b)=\frac{\Delta^2}{s(s-c)}=rR.$$

Choose coordinates $D=(0,0)$ with $AB$ horizontal and $C$ above it. The excentre is $(0,-R)$ and the incentre is $I=(u,r)$ for some real $u$. The excircle has equation
$$x^2+y^2+2Ry=0.$$
The points on $DI$ are $(tu,tr)$. Besides $t=0$, the circle intersection satisfies
$$t=-\frac{2Rr}{u^2+r^2}.$$
Thus $S$ lies on the opposite ray from $I$, and, since $P=I/2$,
$$DS\cdot DP=\frac{2Rr}{\sqrt{u^2+r^2}}\cdot\frac{\sqrt{u^2+r^2}}2=rR=DA\cdot DB.$$
The points $A,B$ lie on opposite sides of $D$, as do $P,S$. The converse of the intersecting-chords theorem now proves the required concyclicity.''','The useful invariant is the product DA·DB=rR, involving both the incircle and the excircle. Once paired with the second intersection of DI and the excircle, power of a point turns the midpoint condition into the desired cyclicity.')
add(2017,'V',4,4,'Number theory','Consecutive primes|Telescoping sums',r'For each integer $n\ge2$, let $a_n$ be the largest prime at most $n$ and $b_n$ the smallest prime greater than $n$. Evaluate $\displaystyle\sum_{n=2}^{2016}\frac1{a_nb_n}$.',r'''If $p<q$ are consecutive primes, then $a_n=p$ and $b_n=q$ for each $n=p,p+1,\ldots,q-1$. The contribution of this complete block is
$$\frac{q-p}{pq}=\frac1p-\frac1q.$$
The integer $2017$ is prime: trial division by the primes $2,3,5,7,11,13,17,19,23,29,31,37,41,43$, the primes at most $\sqrt{2017}$, verifies this. Thus the interval $2\le n\le2016$ consists of complete consecutive-prime blocks, starting at $2$ and ending immediately before $2017$. Their sum telescopes to
$$\boxed{\frac12-\frac1{2017}=\frac{2015}{4034}}.$$''','Direct summation is misleading because the denominators repeat. Grouping terms between consecutive primes makes each block a difference of reciprocals and collapses the entire sum.')
add(2017,'IV',3,4.5,'Geometry','Circle arcs|Modular arithmetic|Pigeonhole principle',r'An equilateral triangle and a square are inscribed in a circle of circumference $1$, with no vertex shared by the two polygons. Their seven vertices divide the circle into seven arcs. Prove that at least one arc has length at most $1/24$.',r'''Measure positions around the circle modulo $1$. Place the triangle vertices at $i/3$ for $i=0,1,2$, and the square vertices at $t+j/4$ for $j=0,1,2,3$.

The twelve differences
$$\frac i3-\frac j4=\frac{4i-3j}{12}\pmod1$$
are all distinct. Indeed, equality modulo $1$ implies $4(i-i')\equiv3(j-j')\pmod{12}$; reducing modulo $3$ and modulo $4$ forces $i=i'$ and $j=j'$. Therefore these differences are exactly the twelve multiples of $1/12$ around the circle.

Every point on a circle is within circular distance $1/24$ of one of twelve equally spaced points. Choose such a multiple nearest to $t$. The corresponding triangle vertex and square vertex are at circular distance at most $1/24$. Their shorter connecting arc contains one or more of the seven arcs in the question, so at least one of those arcs also has length at most $1/24$.''','The ordinary seven-arc pigeonhole bound is too weak. One needs to compare all twelve triangle–square vertex differences and notice their uniform spacing, using the coprimality of 3 and 4.')
add(2017,'IV',4,4.5,'Algebra','Continued fractions|Recurrences|Linearization',r'Express as a single fraction the finite continued fraction $\displaystyle 1+\frac2{1+\frac2{1+\cdots+\frac2{1}}}$ containing exactly $2017$ numerators equal to $2$.',r'''Let $x_0=1$ and $x_{k+1}=1+2/x_k$. We seek $x_{2017}$. Write $x_k=A_{k+1}/A_k$, where $A_0=A_1=1$. The relation for $x_k$ is equivalent to
$$A_{k+2}=A_{k+1}+2A_k.$$
The formula
$$A_k=\frac{2^{k+1}+(-1)^k}{3}$$
holds for $k=0,1$ and satisfies this recurrence, so induction proves it for all $k$. Hence
$$x_{2017}=\frac{A_{2018}}{A_{2017}}=\boxed{\frac{2^{2019}+1}{2^{2018}-1}}.$$''','A direct expansion becomes unwieldy. Passing to numerator and denominator sequences linearizes the fractional recurrence; solving or guessing the two-term recurrence then yields the exact expression.')
add(2016,'V',1,4,'Number theory','Polynomial differences|Congruences|Divisibility',r'Let $P(x)=x^3+ax+b$, where $a,b$ are integers. Suppose that some integers $y,z$ make $P(y)-P(z)$ divisible by $3$ but not by $9$. Prove that $3\nmid a$.',r'''Suppose instead that $3\mid a$. Since $t^3\equiv t\pmod3$ for every integer $t$, the divisibility of $P(y)-P(z)$ by $3$ implies $y\equiv z\pmod3$.

Now factor:
$$P(y)-P(z)=(y-z)(y^2+yz+z^2+a).$$
The first factor is divisible by $3$. Using $y\equiv z\pmod3$ and $3\mid a$, the second is congruent to $3z^2\equiv0\pmod3$. Their product is divisible by $9$, contradicting the hypothesis. Thus $3\nmid a$.''','The proof combines the cubic identity modulo 3 with a factorization that upgrades divisibility from 3 to 9. The contradiction requires recognizing that both factors gain a factor of 3.')
add(2016,'V',2,5.5,'Geometry','Incircle|Isosceles triangle|Coordinates|Chord parametrization',r'Let $ABC$ be isosceles with $AB=AC$. Its incircle touches $BC,CA,AB$ at $X,Y,Z$, respectively. The line $CZ$ meets the incircle again at $L$, and the line $YL$ meets $BC$ at $M$. Prove that $XM=MC$.',r'''Scale and position the triangle so that $X=(0,0)$, $B=(-1,0)$ and $C=(1,0)$. If the inradius is $r$, the incircle has equation $x^2+y^2=2ry$. Its points other than $X$ can be parametrized by
$$T(t)=\left(\frac{2rt}{1+t^2},\frac{2r}{1+t^2}\right).$$
Direct substitution shows that the chord joining $T(s)$ and $T(t)$ has equation
$$(s+t)x+(1-st)y=2r.$$
The same formula with $s=t$ gives the tangent at $T(t)$.

The tangent at $Z$ passes through $B=(-1,0)$, so the tangent equation forces $Z=T(-r)$. By symmetry, $Y=T(r)$. Write $L=T(\ell)$. Since $C=(1,0)$ lies on the chord $ZL$, its equation gives $\ell-r=2r$, so $\ell=3r$. Therefore the chord $YL$ has equation
$$4rx+(1-3r^2)y=2r.$$
Its intersection with $BC$, where $y=0$, is $M=(1/2,0)$. Thus $XM=MC=1/2$, as required.''','The second circle intersection and the isosceles symmetry suggest a projective relation among chords. A rational parametrization gives a controlled coordinate proof: tangency fixes two parameters, the first secant fixes the third, and the final chord produces the midpoint.')
add(2016,'V',3,5,'Number theory','Binomial coefficients|Primality criterion|Prime divisibility',r'Prove that an integer $n\ge2$ is prime if and only if $n$ divides $\binom nm$ for every $m=1,2,\ldots,n-1$.',r'''If $n$ is prime, then for $1\le m<n$ the identity
$$m\binom nm=n\binom{n-1}{m-1}$$
and $\gcd(m,n)=1$ show that $n\mid\binom nm$.

Conversely, suppose that $n$ is composite and choose a prime divisor $p$ of $n$. Then $p<n$. If $n\mid\binom np$, write $\binom np=nk$. Applying the same identity with $m=p$ gives
$$p k=\binom{n-1}{p-1}.$$
But
$$(p-1)!\binom{n-1}{p-1}=(n-1)(n-2)\cdots(n-p+1)$$
is congruent modulo $p$ to $(-1)^{p-1}(p-1)!$, which is nonzero modulo $p$. Thus $\binom{n-1}{p-1}$ is not divisible by $p$, a contradiction. At least one intermediate coefficient therefore fails the divisibility condition when $n$ is composite.''','The forward direction is standard; the reverse direction requires choosing the coefficient indexed by a prime divisor and comparing its p-divisibility with that of n. This avoids having to classify all prime-power factors of the binomial coefficients.','The source says “positive integer n”, which leaves n=1 as a vacuous counterexample. The bank explicitly corrects the intended domain to n≥2.')
add(2016,'V',4,4,'Combinatorics','Pigeonhole principle|Multisets|Counting polynomials',r'A list contains $2016$ polynomials of degree $4$. Every root and every leading coefficient belongs to $\{1,2,3,4,5,6\}$. Repetitions are allowed. What is the greatest number of occurrences of one identical polynomial that is guaranteed in every such list?',r'''A polynomial is determined by its leading coefficient and the multiset of its four roots, counted with multiplicity. There are $6$ choices for the leading coefficient. The number of four-element multisets from six choices is
$$\binom{4+6-1}{4}=\binom94=126.$$
Thus there are exactly $6\cdot126=756$ possible polynomials.

Since $2016>2\cdot756$, the pigeonhole principle guarantees that some polynomial occurs at least three times. Three is the best guarantee: take each of the $756$ polynomials twice, and take $504$ of them once more. This gives $2016$ entries, with none occurring more than three times. The answer is $\boxed3$.''','Counting ordered root lists overcounts repeated polynomials. The main step is to count root multisets, then use pigeonhole together with an explicit distribution showing that the bound is sharp.')
ids={x['id'] for x in new};data=json.loads((p/'data/americas.json').read_text());data=[x for x in data if x['id'] not in ids]+new
(p/'data/americas.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
c=json.loads((p/'research/americas-coverage.json').read_text())
for (y,l),rates in [((2017,'V'),[1.5,5.5,5.5,4]),((2017,'IV'),[2,2,4.5,4.5]),((2016,'V'),[4,5.5,5,4])]:
 comp=f'Uruguayan National Mathematical Olympiad Final Level {l}'
 c['fullyScreened']=[x for x in c['fullyScreened'] if not(x['competition']==comp and x['year']==y)]
 c['fullyScreened'].append(dict(competition=comp,year=y,ratings={str(i+1):r for i,r in enumerate(rates)},source=sources[y,l],exclusionNotes={'1':'2017 Level V: changing logarithm bases makes the sum log(2017!)/log(2017!)=1. 2017 Level IV: common chords are perpendicular to their centre lines, and the centre triangle is 3-4-5.','2':'2017 Level IV: gcd(2n+3,n+7)=gcd(n+7,11), so count n≡4 modulo 11.'} if y==2017 else {}))
c['papersScreened']=len(c['fullyScreened']);c['problemAppearancesScreened']=sum(len(x['ratings']) for x in c['fullyScreened']+c['partiallyScreened']);c['uniqueIncluded']=len(data)
c['gaps'].append('Uruguay: official national final Level V 2016/2017 and Level IV 2017 fully screened from real PDFs linked on the organizer’s level-specific archive. Its generic newer past-paper page contains placeholder links. Other years/levels remain pending.')
c['qualityNotes'].append('Uruguay 2016 Level V Q3 domain corrected transparently from n positive to n≥2, since n=1 makes the published equivalence false. Uruguay 2017 Level V Pascal-triangle diagram visually checked for row numbering.')
(p/'research/americas-coverage.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');print('Total',len(data))
