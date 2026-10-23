import json,re
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text());base='https://ance.gov.md/sites/default/files/'
urls={(9,1):'omrm_matem_9_solutii_ziua_1_2023_115.pdf',(9,2):'omrm_matem_9_solutii_ziua_2_2023_115.pdf',(10,1):'omrm_matem_10_solutii_ziua_1_2023.pdf',(10,2):'omrm_matem_10_solutii_ziua_2_2023.pdf',(11,1):'orm2023_solutii_ziua1.pdf',(11,2):'orm2023_solutii_ziua2.pdf',(12,1):'orm_matem_12_solutii_ziua_1.pdf',(12,2):'orm_matem_12_solutii_ziua_2.pdf'}
rows={
'0cc3f1':(2,'Number theory','The sum formula reduces this to even factor pairs of 392, with three short cases.'),
'1dd141':(2.5,'Geometry','Coordinate direction vectors give the cosine by one dot product; the synthetic solution is longer but routine.'),
'237afd':(3,'Geometry','Similar triangles give diagonal ratios; perpendicularity and Pythagoras determine the four sides.'),
'2d08c1':(2,'Algebra','Use a>b,c and the triangle inequality to make the quadratic discriminant strictly positive.'),
'2fe8df':(3,'Number theory','Irrationality forces a squared equal to bc, and the desired divisibility is the identity with factor b-a+c.'),
'382deb':(1.5,'Number theory','Reduce m to minus n modulo m+n; one direct congruence proves the assertion.'),
'44633a':(2,'Algebra','Positivity and monotonicity give a limit; substitution in the recurrence forces zero.'),
'5cb985':(3.5,'Geometry','Recognize the midpoint-altitude-foot triangle as equilateral and apply the constant sum of distances identity.'),
'658a9a':(2,'Geometry','One Pythagorean equation gives radius 5a/8; comparing with the square perimeter is immediate.'),
'7e2b80':(3,'Algebra','A piecewise-linear graph has three intersections only when the line passes through one of two vertices.'),
'81a4d4':(None,'Algebra','Inspected: derivative of the reciprocal product gives 1+log squared; solving the resulting differential equation requires calculus outside the BMO prerequisite scope.'),
'994b3b':(4,'Number theory','The essential idea is the unique denominator with maximal power of two; clearing the least common denominator leaves an odd numerator.'),
'a250cf':(None,'Algebra','Inspected: monotone convergence followed by reciprocal differences and the derivative at zero gives the limit 1 via Stolz-Cesaro; calculus prerequisites are outside BMO scope.'),
'a9d917':(1.5,'Algebra','Expand the square of the sum and use the sum of squared differences; equality has all three variables equal.'),
'b28f6a':(2.5,'Algebra','Evaluate at zero and minus 2023 to find P(0),P(-1), then interpolate the linear remainder.'),
'b5f7e9':(3,'Algebra','Recognize the complex argument as 75 degrees, apply de Moivre, and reduce the exponent modulo 24.'),
'b9f7c8':(3,'Algebra','Expand into four reciprocal pairs, each between 2 and 10/3, and check simultaneous equality.'),
'ba034e':(3,'Geometry','Subtract squared distances to show H and C have the same projection onto AB, then repeat cyclically.'),
'bfcba9':(2.5,'Algebra','At zero one factor vanishes; shifting that zero forces a=b, after which a negative square is impossible.'),
'c834fa':(2.5,'Algebra','Divide by the two common positive factors; the inequality becomes two direct applications of (a+b)^2>=4ab.'),
'dfee3a':(None,'Algebra','Inspected: half-angle substitution and periodicity evaluate the integral as 2 times the square root of 2; integration is outside BMO scope.'),
'e25e14':(4.5,'Number theory','Take a square root in the quadratic integer ring and use its norm minus one to turn the rational coefficient into a square minus one.'),
'e6fe19':(3,'Number theory','Three successive digit-sum bounds reduce the answer below 14; the residue modulo nine then forces 7.'),
'e7a0f3':(3,'Algebra','Substitute the nonnegative square root, then count nonnegative roots using discriminant and Vieta signs.'),
'e9dd66':(4,'Algebra','Subtract the affine solution and iterate the inverse affine map toward its fixed point; continuity kills the remaining function.'),
'f6abd0':(2,'Algebra','Elementary trigonometric identities factor the equation into three standard angle classes.'),
'f713e2':(3,'Geometry','Affine coordinates or Menelaus and similar triangles give both ratios; the raw statement has a side-label typo, so it is not republished.'),
'f9cc8a':(None,'Algebra','Inspected: reflect x to minus x, add the integrals, and obtain log 2; integration is outside BMO scope.'),
'fc2107':(3.5,'Geometry','The equal lateral edges locate the circumcentre projection; standard three-dimensional vectors or a prism-volume ratio compute the skew distance.'),
'fd0db6':(4,'Algebra','Introduce the missing positive variable 1-sum(a_i), making the expression symmetric; multiply the n+1 AM-GM inequalities.')}
for suf,(v,t,why) in rows.items():
 slug='mda_2023_'+suf;d=json.loads((p/(slug+'.json')).read_text());g,n=map(int,re.findall(r'\d+',d['problem_number']));day=1 if n<=4 else 2;src=base+urls[g,day]
 r[slug]={'difficulty':v,'topic':t,'tags':[],'reason':why,'section':f'National Final — Grade {g}, Day {day}','number':str(n),'sourceUrl':src,'solutionUrl':src,'sourceName':'Moldova ANCE — official 2023 solutions','license':'Original contest rights retained; original English mathematical exposition.'}
 if v is None:r[slug]['outOfScope']=True

def include(s,statement,solution,tags):
 r['mda_2023_'+s].update(statement=statement,solution=solution,solutionKind='original-exposition',tags=tags)
include('994b3b',r'For positive integers $n<m$, prove that $\sum_{k=n}^{m}1/k$ is not an integer.',r'Let $2^a$ be the largest power of two dividing any denominator in the interval. Exactly one denominator has this power: between two odd multiples of $2^a$ lies a multiple of $2^{a+1}$. Let $L$ be the least common multiple of all the denominators. In $\sum L/k$, exactly one summand is odd and the others are even. The numerator is therefore odd, while $L$ is even, so the sum cannot be an integer.',['valuations','parity','harmonic sums'])
include('e25e14',r'Write $(3+\sqrt8)^{2023}=a+b\sqrt8$ with integers $a,b$. Prove that $a$ is the product of two positive integers differing by two.',r'Write $(1+\sqrt2)^{2023}=u+v\sqrt2$, where $u,v$ are positive integers. Conjugating and multiplying gives $u^2-2v^2=-1$. Squaring the first identity gives $a=u^2+2v^2=4v^2-1=(2v-1)(2v+1)$, as required.',['quadratic integers','conjugates','factorization'])
include('e9dd66',r'Find every continuous function $f:\mathbb R\to\mathbb R$ satisfying $3f(2x+1)=f(x)+5x$ for every real $x$.',r'The function $f(x)=x-3/2$ works. For any solution put $g(x)=f(x)-x+3/2$. Then $3g(2x+1)=g(x)$, so iteration gives $$g(x)=3^{-n}g\!\left(-1+\frac{x+1}{2^n}\right).$$ The argument tends to $-1$, and continuity makes the values of $g$ bounded there. The right side tends to zero, hence $g(x)=0$ for all $x$.',['functional equations','iteration','continuity'])
include('fd0db6',r'Let $a_1,\ldots,a_n>0$ and $s=a_1+\cdots+a_n<1$. Prove $$\frac{s}{a_1\cdots a_n}\frac{(1-a_1)\cdots(1-a_n)}{1-s}\ge n^{n+1}.$$ ',r'Set $a_{n+1}=1-s$ and $P=\prod_{i=1}^{n+1}a_i$. Each complement is the sum of the other $n$ positive variables, so AM-GM gives $$1-a_i\ge n(P/a_i)^{1/n}.$$ Multiplying over all $n+1$ indices yields $\prod(1-a_i)\ge n^{n+1}P$, which is exactly the required inequality. Equality occurs when all $n+1$ variables equal $1/(n+1)$.',['inequalities','AM-GM','auxiliary variable'])
# Restore the two questions absent from the corpus; both have been read in the official solution paper.
missing=[(11,7,3,'Algebra','Vieta and the strict inequalities between symmetric means give a>b>c; no derivative is needed.',r'The polynomial $X^3-3aX^2+3b^2X-c^3$ has three distinct positive roots, where $a,b,c>0$. Prove $a>b>c$.'),(12,4,None,'Algebra','Inspected: factor column entries then apply the Vandermonde determinant, obtaining exactly the product of the odd factorials. Determinants are outside the BMO prerequisite scope.',r'For the 1012 by 1012 matrix with entry $j^{2i-1}$ in row $i$, column $j$, prove its determinant is divisible by $1!3!\cdots2023!$.')]
for g,n,v,t,why,st in missing:
 slug=f'mda_2023_grade{g}_{n}';src=base+urls[g,1 if n<=4 else 2];(p/(slug+'.json')).write_text(json.dumps({'country':'Moldova','competition':'Moldova Mathematical Olympiad','year':2023,'section':f'National Final — Grade {g}, Day {1 if n<=4 else 2}','problem_number':str(n),'problem_markdown':st,'solutions_markdown':[]},indent=2));r[slug]={'difficulty':v,'topic':t,'tags':[],'reason':why,'sourceUrl':src,'outOfScope':v is None}
# The complete Grade 7 and Grade 8 papers were read, including every worked solution.
lower={7:[(1.5,'Algebra','The square-root domains force a=-2023; the final digit of 4^2024 is immediate.'),(2.5,'Combinatorics','Either all five residue classes occur or one has at least five entries; each case supplies the required sum.'),(3.5,'Geometry','The ordered congruence gives an isosceles triangle; the perpendicular conditions force an auxiliary equilateral triangle and perimeter 30.'),(2.5,'Number theory','Four divisors forces pq or p cubed; modulo p rules out the latter and (p-1)(q-1)=2 gives 6.'),(3,'Geometry','Identify E as an orthocentre, then use the midpoint line to force AB perpendicular AC.'),(2.5,'Number theory','Subtract the inverse-proportion equations to obtain equal digits or a zero digit; none of the resulting three-digit forms is a cube.'),(2.5,'Number theory','Division gives m=7n+3-20/(7n-3), reducing to the finite signed divisor list of 20.'),(2.5,'Number theory','Squaring makes the square root of pq rational, forcing the two primes equal and then n=p.')],8:[(2.5,'Algebra','A weighted sum of the two quadratics factors as (pq-1)(2p+q); substitution evaluates the ratio.'),(2.5,'Number theory','Separate one-digit and two-digit x; place-value congruences yield the least value 43.'),(2.5,'Geometry','Reflect E in the midpoint D; the resulting parallelogram gives an isosceles triangle and ratio 2.'),(2.5,'Combinatorics','The six distinct row sums omit two of 0 through 7; divisibility by 7 forces their sum 7 and each column sum 3.'),(2,'Algebra','Nonnegativity forces the square (2x-y)^2 to vanish, leaving y=2x with 0<=x<=8.'),(2,'Number theory','Parity forces m+n=30; enumerate the few prime pairs and check the two linear combinations.'),(2.5,'Geometry','Perpendicular-bisector symmetry and elementary 30/60-degree angle chasing give 45 degrees.'),(3,'Combinatorics','Express the change in total as six integer count differences summing to 202; pigeonhole gives at least 34.')]}
for g,items in lower.items():
 for n,(v,t,why) in enumerate(items,1):
  slug=f'mda_2023_grade{g}_{n}';day=1 if n<=4 else 2;fn=f'omrm_matem_{g}_solutii'+('_rom' if g==8 else '')+f'_ziua_{day}_2023'+('_115' if g==8 else '')+'.pdf';src=base+fn
  (p/(slug+'.json')).write_text(json.dumps({'country':'Moldova','competition':'Moldova Mathematical Olympiad','year':2023,'section':f'National Final — Grade {g}, Day {day}','problem_number':str(n),'problem_markdown':'See the official paper for the full statement.','solutions_markdown':[]},indent=2));r[slug]={'difficulty':v,'topic':t,'tags':[],'reason':why,'sourceUrl':src}
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
