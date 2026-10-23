import json,pathlib
p=pathlib.Path('research/asia/reviews.json');r=json.loads(p.read_text())
def add(k,d,reason,sol=None,**kw):
 r['ind_2010_'+k]={'difficulty':d,'reason':reason,**kw}
 if sol:r['ind_2010_'+k]['solutionOverride']=sol
add('051b62',6,'Choosing a largest entry and averaging all 81 complementary cross-products gives the sharp constant.')
add('28fd09',7.5,'Requires harmonic division, tangent/symmedian ratios and a substantial chain of projective or metric identities.')
add('29c22a',4.5,'Coordinates on the altitude turn the reflection into a midpoint identity, followed by a standard orthocenter relation.',r'''Choose coordinates $K=(0,0)$, $A=(0,a)$, $H=(0,h)$ and $O=(u,v)$, with $BC$ horizontal. Since $P$ is equidistant from $K$ and $H$, its second coordinate is $h/2$. Also $P$ lies on the perpendicular bisector of $OH$. Reflection in $OH$ therefore gives $P+Q=O+H$, so the second coordinate of $Q$ is $v+h/2$.

Write $B=(b,0)$ and $C=(c,0)$. The circumcenter has $u=(b+c)/2$. Equating its squared distances to $A$ and $B$ gives $2av=a^2+bc$. The altitude from $B$, being perpendicular to $AC$, meets $AK$ at height $h=-bc/a$. Thus $2v+h=a$ and the height of $Q$ is $a/2$. This is exactly the horizontal line through the midpoints of $AB$ and $AC$.''')
add('2c94b5',2.5,'A small minimum-sum search after excluding a smallest entry of one settles the problem.')
add('40601c',4.5,'A factorization converts the two product equations into equality in three elementary quadratic inequalities.')
add('42678e',5,'Uses the largest entry to force one parity class to be constant, then counts the remaining cases without double-counting.')
add('479d5d',4,'Recognizes that a symmetric expression obeys the original recurrence; doubling indices then gives the divisibility claim.')
add('62401a',6,'Extracts a square-length identity from Brocard-angle similarity, parameterizes the concurrent cevians and applies Cauchy-Schwarz.')
add('674c3e',3,'The intended nested-floor sequence can be analyzed by intervals between squares.',omitReason='Transcribed denominator lacks the inner floor: the displayed a_n=floor(n/sqrt(n)) is nondecreasing and contradicts the supplied solution. Withheld pending original-paper verification.')
add('7485ca',6,'A Pell-equation family supplies consecutive odd integers, with a coordinated choice of the second coefficient.',r'''Let $r,t$ satisfy $r^2-3t^2=1$, with $t$ a positive even integer. Set $p=t-1$, $q=t+1$, and $m=r^2+1$. Then $p,q$ are consecutive positive odd integers and
$$p^2+pq+q^2=3t^2+1=r^2.$$
Also
$$p^2+mpq+q^2=2t^2+2+(r^2+1)(t^2-1)=r^2t^2,$$
where the last equality uses $r^2=3t^2+1$.

There are infinitely many such $r,t$: start with $(r,t)=(7,4)$ and repeatedly replace them by $(7r+12t,4r+7t)$. The Pell relation is preserved, $t$ remains positive and even, and both coordinates strictly increase. Thus the resulting $m$ and pairs $(p,q)$ are all distinct, proving the assertion.''')
add('80ee68',6,'Several circle-angle similarities must be organized into the particular side ratio that proves the requested parallelism.')
add('903840',2.5,'Grouping the four possible even final digits gives one qualifying residue in each group.')
add('9d1e5d',5.5,'A chain of multiplicative-order restrictions forces divisibility successively by 17 and 4, then produces a parity contradiction.',r'''Suppose such $n$ exists. Reducing the congruence modulo $103$ gives $2^{2n}\equiv1\pmod{103}$. By Fermat, the order of $2$ divides $102=6\cdot17$. It cannot divide $6$, since $2^6=64\not\equiv1\pmod{103}$. Hence $17$ divides the order and therefore divides $n$.

Reducing modulo $17$ now gives $2^{2n}\equiv1\pmod{17}$. The order of $2$ modulo $17$ is $8$: $2^4\equiv-1$ and $2^8\equiv1$. Thus $8\mid2n$, so $4\mid n$. But $2^{2n+1}-2\equiv2\pmod4$, contradicting its divisibility by $n$. No such positive integer exists.''')
add('ad80f7',6,'Requires a complete structural classification of composite n, bounding prime-power valuations and checking the exceptional small powers.')
add('c294d1',5,'The intended argument uses a quadratic relation for one root and parity in the cubic coefficients.',omitReason='The statement omits the assumption that c is odd used by the solution. As displayed, x^3=0 gives alpha=beta=gamma=0 and contradicts beta!=gamma; withheld.')
add('cdcaa7',3.5,'The three opposite area ratios multiply to one; substituting the two given geometric means immediately yields the third.')
add('e08d56',6,'The key construction creates two circles with a shared radical axis; a third cyclic quadrilateral places T on that axis.')
add('e99aaf',4.5,'Cyclic differences of the three equal values yield a positive-definite quadratic identity.',r'''Set $A=a-b$, $B=b-c$, $C=c-a$, so $A+B+C=0$. Subtracting successive equal polynomial values gives
$$A\alpha^2-B\alpha-C=0,\quad B\alpha^2-C\alpha-A=0,\quad C\alpha^2-A\alpha-B=0.$$
Multiply these by $A,B,C$, respectively, and add. With $S=A^2+B^2+C^2$ and $AB+BC+CA=-S/2$, the result is
$$S\left(\alpha^2+\frac{\alpha+1}{2}\right)=0.$$
The second factor is $(\alpha+1/4)^2+7/16>0$, so $S=0$. Hence $A=B=C=0$ and $a=b=c$.''')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2));print(len(r))
