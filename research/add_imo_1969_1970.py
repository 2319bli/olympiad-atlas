from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');raw=p/'international-raw';r=json.loads((p/'international-reviews.json').read_text())
def add(year,num,topic,rating,reason,statement,solution='',tags=None,solution_url=None,note=None):
 slug=f'imo_{year}_official_p{num}'
 d={'id':slug,'competition_code':'IMO','competition':'IMO','year':year,'problem_number':str(num),'primary_domain':topic,'topics':[[topic,t] for t in (tags or [])],'problem_markdown':statement,'solutions_markdown':[solution],'officialSourceUrl':f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf','officialSolutionUrl':solution_url or f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf','reviewNote':note or 'Official released statement checked; worked exposition independently written and mathematically assessed.'}
 (raw/(slug+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2));r[slug]=[rating,reason]
add(1969,1,'Number theory',4,'Discover a family matched to Sophie Germain’s factorisation, then check that neither factor can degenerate to one.',r'Prove that infinitely many positive integers $a$ have the property that $n^4+a$ is composite for every positive integer $n$.',r'''Choose $a=4m^4$ for any integer $m\geq2$. Sophie Germain's identity gives
$$n^4+4m^4=(n^2-2mn+2m^2)(n^2+2mn+2m^2).$$
The first factor is $(n-m)^2+m^2\geq m^2>1$, and the second is still larger. Thus every $n^4+a$ is composite. The distinct choices $m=2,3,\ldots$ give infinitely many such $a$.''',['Factorisation','Composite numbers','Construction'])
add(1969,2,'Algebra',4,'Combine the phase-shifted cosines into one sinusoid. The dominant first coefficient is essential to rule out the identically zero function.',r'''For arbitrary real $a_1,\ldots,a_n$, define $f(x)=\sum_{j=1}^n2^{1-j}\cos(a_j+x)$. If $f(x_1)=f(x_2)=0$, prove that $x_2-x_1$ is an integer multiple of $\pi$.''',r'''Write
$$Z=\sum_{j=1}^n2^{1-j}e^{ia_j},\qquad f(x)=\operatorname{Re}(Ze^{ix}).$$
The first summand has modulus one, while the others have total modulus at most
$$\frac12+\cdots+\frac1{2^{n-1}}=1-\frac1{2^{n-1}}<1.$$
The reverse triangle inequality therefore gives $|Z|\geq2^{1-n}>0$.

Write $Z=Re^{i\phi}$ with $R>0$. Then $f(x)=R\cos(x+\phi)$, whose zeros are exactly $x+\phi=\pi/2+k\pi$. Any two zeros differ by an integer multiple of $\pi$. The same argument can be expressed with the real sine and cosine coefficients instead of complex numbers.''',['Trigonometry','Complex numbers','Triangle inequality'])
add(1969,3,'Geometry',5.5,'Classify the two possible placements of two exceptional edges, obtain exact nondegeneracy intervals, and use reciprocal scaling for four and five edges. The three-edge case needs a separate construction.',r'For each $k=1,2,3,4,5$, determine exactly which $a>0$ allow a nondegenerate tetrahedron with $k$ edge lengths equal to $a$ and the other $6-k$ equal to $1$.',r'''The ranges are
$$\begin{array}{c|c}k&\text{admissible }a\\\hline
1&(0,\sqrt3)\\
2&(0,\sqrt{2+\sqrt3})\\
3&(0,\infty)\\
4&(\sqrt{2-\sqrt3},\infty)\\
5&(1/\sqrt3,\infty).
\end{array}$$
For $k=1$, take $AB=a$. The two equilateral triangles $ACD,BCD$ have unit sides. Their vertices $A,B$ lie on the circle perpendicular to $CD$ through its midpoint, of radius $\sqrt3/2$. Their chord length can be any number strictly between $0$ and $\sqrt3$; the endpoints give a degenerate tetrahedron. This proves the first range.

For $k=2$, either the exceptional edges are opposite or adjacent. In the opposite case $AB=CD=a$, place
$$A=(-a/2,0,0),\ B=(a/2,0,0),\ C=(0,-a/2,h),\ D=(0,a/2,h).$$
All cross edges are one exactly when $h^2=1-a^2/2$. Conversely the equal cross edges force the midpoint line perpendicular to both equal opposite edges, and their directions perpendicular to one another, so this condition is necessary. The range is $0<a<\sqrt2$.

For the adjacent case let $AC=AD=a$, with all other edges one. Place
$$C=(-1/2,0,0),\ D=(1/2,0,0),\ B=(0,\sqrt3/2,0),\ A=(0,y,z).$$
The equations $AC=a$ and $AB=1$ give
$$y=\frac{a^2-1/2}{\sqrt3},\qquad z^2=\frac{-a^4+4a^2-1}{3}.$$
A nondegenerate tetrahedron exists exactly when $z^2>0$, or $2-\sqrt3<a^2<2+\sqrt3$. Combining this interval with the opposite-edge interval proves the second row.

For $k=3$ and $a\leq1$, use an equilateral base of side $a$ and three unit edges to its apex; its height squared is $1-a^2/3>0$. For $a\geq1$, use a unit equilateral base and three edges of length $a$; its height squared is $a^2-1/3>0$. Thus every positive $a$ works.

Finally scaling every length by $1/a$ exchanges $k$ with $6-k$ and $a$ with $1/a$. The first two rows therefore give the last two.''',['Solid geometry','Classification','Construction'],solution_url='https://prase.cz/kalva/imo/isoln/isoln693.html',note='Official statement checked; configurations independently derived by coordinates, confirming the published classification. At a=1, the assignment of distinguished edges is formal, and the regular tetrahedron is allowed.')
add(1969,4,'Geometry',5.5,'Compute the two auxiliary radii using the semicircle tangency condition. The unexpected key is that the original incenter is the midpoint of the other two centres, giving a common tangent by reflection.',r'''Let $C$ lie strictly on the semicircle with diameter $AB$, and let $D$ be its perpendicular foot on $AB$. Consider the incircle of $ABC$, and the two circles inside the semicircle tangent to $AB$, $CD$ and the semicircular arc, one on each side of $CD$. Prove the three circles share a tangent other than $AB$.''',r'''Write $BC=a$, $CA=b$, $AB=c$, so $a^2+b^2=c^2$. Put $A=(0,0)$, $B=(c,0)$, and $D=(d,0)$, where $d=b^2/c$. Let the left and right auxiliary radii be $u,v$. Their centres are
$$L=(d-u,u),\qquad R=(d+v,v).$$
Internal tangency to the circle of centre $(c/2,0)$ and radius $c/2$ gives
$$(d-u-c/2)^2+u^2=(c/2-u)^2.$$
After simplifying, $u^2+2(c-d)u-d(c-d)=0$. Its positive root is
$$u=\sqrt{c(c-d)}-(c-d)=a-a^2/c.$$
The symmetric calculation gives $v=b-b^2/c$. Hence
$$L=(c-a,a-a^2/c),\qquad R=(b,b-b^2/c).$$
The incircle has radius $r=(a+b-c)/2$ and centre
$$I=((b+c-a)/2,r).$$
Since $a^2+b^2=c^2$, the midpoint of $L,R$ is exactly $I$.

Reflect the line $AB$ in the line $LR$. Each of the three centres is fixed by this reflection, so its circle is preserved. The reflected line is consequently tangent to all three circles. It differs from $AB$: the line $LR$ is not $AB$, since both auxiliary radii are positive, and it is not perpendicular to $AB$, since the difference of its endpoint abscissas is $a+b-c>0$. This supplies the second common tangent.''',['Circles','Coordinates','Reflection'],solution_url='https://prase.cz/kalva/imo/isoln/isoln694.html')
add(1969,5,'Combinatorics',5.5,'First prove the five-point convex-quadrilateral lemma, then double-count its occurrences in five-element subsets. An integer polynomial comparison turns the resulting stronger bound into the requested one.',r'For $n>4$ points in the plane with no three collinear, prove that at least $\binom{n-3}{2}$ of their four-point subsets form convex quadrilaterals.',r'''Any five such points contain a convex quadrilateral. If their convex hull has at least four vertices, choose four of those. Otherwise the hull is a triangle $ABC$ with two interior points $D,E$. The line $DE$ leaves two of $A,B,C$ on one side and the third on the other. Those two vertices together with $D,E$ form a convex quadrilateral. The original hull vertices remain extreme points. Neither $D$ nor $E$ can lie in the triangle formed by the other three selected points: the supporting line $DE$ meets that triangle only at its other endpoint. Thus all four selected points are extreme.

Let $Q$ count the convex quadrilaterals. Every five-point subset contains one, while each fixed quadrilateral belongs to exactly $n-4$ five-point subsets. Therefore
$$Q(n-4)\geq\binom n5,\qquad Q\geq\frac{n(n-1)(n-2)(n-3)}{120}.$$
For integer $n\geq5$,
$$n(n-1)(n-2)-60(n-4)=(n-5)(n-6)(n+8)\geq0.$$
The preceding lower bound is consequently at least $(n-3)(n-4)/2=\binom{n-3}{2}$, as required.''',['Convexity','Double counting','Extremal geometry'],solution_url='https://prase.cz/kalva/imo/isoln/isoln695.html')
add(1969,6,'Algebra',4.5,'Rewrite the mixed determinant terms as a positive square plus two reciprocal terms, then apply AM–GM twice. Track equality through all three steps.',r'''Suppose $x_1,x_2>0$ and $A_i=x_iy_i-z_i^2>0$ for $i=1,2$. Prove
$$\frac8{(x_1+x_2)(y_1+y_2)-(z_1+z_2)^2}\leq\frac1{A_1}+\frac1{A_2},$$
and determine the equality conditions.''',r'''Write $D=(x_1+x_2)(y_1+y_2)-(z_1+z_2)^2$. Substituting $y_i=(A_i+z_i^2)/x_i$ gives
$$D=A_1+A_2+\frac{x_1A_2}{x_2}+\frac{x_2A_1}{x_1}+\left(\sqrt{\frac{x_1}{x_2}}z_2-\sqrt{\frac{x_2}{x_1}}z_1\right)^2.$$
Consequently
$$D\geq A_1+A_2+2\sqrt{A_1A_2}\geq4\sqrt{A_1A_2}>0.$$
Taking reciprocals and applying AM–GM once more yields
$$\frac8D\leq\frac2{\sqrt{A_1A_2}}\leq\frac1{A_1}+\frac1{A_2}.$$
For equality, the last inequality requires $A_1=A_2$. Equality in the first pair of reciprocal terms then gives $x_1=x_2$, and the square term gives $z_1=z_2$. The definition of $A_i$ now gives $y_1=y_2$. Conversely equal triples clearly give equality. Thus equality holds exactly when $(x_1,y_1,z_1)=(x_2,y_2,z_2)$.''',['Inequalities','AM–GM','Positive quadratic forms'])
add(1970,1,'Geometry',3.5,'Express the inradius-to-opposite-exradius ratio as the product of two half-angle tangents. The two angles at the dividing point are supplementary, so their factors cancel.',r'''Let $M$ lie inside $AB$ in triangle $ABC$. Denote the inradii of $AMC,BMC,ABC$ by $r_1,r_2,r$, and their exradii opposite vertex $C$ by $q_1,q_2,q$. Prove $(r_1/q_1)(r_2/q_2)=r/q$.''')
add(1970,2,'Algebra',3,'Normalise both numeral values by the leading power of the base. The resulting sum of nonnegative negative powers is strictly decreasing, which determines the ratio order.',r'''The same digit strings $x_nx_{n-1}\cdots x_0$ and $x_{n-1}\cdots x_0$, with $x_n,x_{n-1}>0$, are valid in integer bases $a,b>1$. Let their values be $A_n,A_{n-1}$ in base $a$ and $B_n,B_{n-1}$ in base $b$. Prove $A_{n-1}/A_n<B_{n-1}/B_n$ if and only if $a>b$.''')
add(1970,3,'Algebra',4.5,'Bound each summand by a telescoping difference of reciprocal square roots. The sharpness part needs a geometric sequence with ratio approaching one, not just equality analysis.',r'''Let $1=a_0\leq a_1\leq a_2\leq\cdots$ and define
$$b_n=\sum_{k=1}^n\left(1-\frac{a_{k-1}}{a_k}\right)\frac1{\sqrt{a_k}}.$$
Prove $0\leq b_n<2$. Also prove that for every $0\leq c<2$ a sequence of this kind exists with $b_n>c$ for all sufficiently large $n$.''',r'''Put $y=1/\sqrt{a_{k-1}}$, $x=1/\sqrt{a_k}$, so $0<x\leq y$. With $t=x/y\leq1$,
$$\left(1-\frac{a_{k-1}}{a_k}\right)\frac1{\sqrt{a_k}}=y\,t(1-t^2)\leq2y(1-t)=2(y-x),$$
since $t(1+t)\leq2$. Summing telescopically gives
$$0\leq b_n\leq2\left(1-\frac1{\sqrt{a_n}}\right)<2.$$

To approach the bound, choose $t>1$ and set $a_k=t^{2k}$. Then
$$b_n=(1-t^{-2})\sum_{k=1}^nt^{-k}=\frac{t+1}{t^2}(1-t^{-n}).$$
As $t$ decreases to one, $(t+1)/t^2$ tends to two. Given $c<2$, choose $t>1$ so that this quantity exceeds $c$, then choose $n$ sufficiently large that $b_n>c$. Since this expression increases with $n$, it remains above $c$ thereafter.''',['Inequalities','Telescoping','Sharp bounds'])
add(1970,4,'Number theory',4,'A prime at least seven can occur in only one of the six terms. Restricting the remaining prime factors and examining the three odd terms then forces an impossible small case.',r'Find all positive integers $n$ for which $\{n,n+1,\ldots,n+5\}$ can be split into two subsets with equal products.',r'''There are no such integers.

If a prime $p\geq7$ divided one of the six consecutive integers, it could divide none of the others. Whichever subset contained that integer would have product divisible by $p$, while the other would not. Hence every prime divisor of all six integers must belong to $\{2,3,5\}$.

Exactly three of the six integers are odd. Among those three, at most one is divisible by three and at most one by five. Therefore at least one of them has no prime divisor at all and must equal one. This forces $n=1$.

But $\{1,2,3,4,5,6\}$ contains exactly one number divisible by five, again making equal subset products impossible. Thus no $n$ works.''',['Prime factors','Consecutive integers','Pigeonhole principle'],solution_url='https://prase.cz/kalva/imo/isoln/isoln704.html')
add(1970,5,'Geometry',4,'The projection hypothesis turns the right angle into three pairwise perpendicular edges. Pythagoras and Cauchy–Schwarz then give the inequality and equality case.',r'''In tetrahedron $ABCD$, $\angle BDC=90^\circ$. The perpendicular projection of $D$ onto plane $ABC$ is the orthocentre of $ABC$. Prove
$$(AB+BC+CA)^2\leq6(AD^2+BD^2+CD^2),$$
and determine equality.''',r'''Let $H$ be the given projection. Since $AH\perp BC$ and $DH$ is perpendicular to the whole base plane, $AD\perp BC$. Similarly $BD\perp AC$ and $CD\perp AB$.

Put $D$ at the origin and denote the other vertex vectors by $a,b,c$. The given right angle says $b\cdot c=0$. Since $BD\perp AC$, we have $b\cdot(c-a)=0$, hence $a\cdot b=0$. Likewise $CD\perp AB$ gives $a\cdot c=0$. Thus the three edges from $D$ are mutually perpendicular.

Writing $x=AD^2$, $y=BD^2$, $z=CD^2$, Pythagoras gives
$$AB=\sqrt{x+y},\quad BC=\sqrt{y+z},\quad CA=\sqrt{z+x}.$$
Cauchy–Schwarz yields
$$(AB+BC+CA)^2\leq3((x+y)+(y+z)+(z+x))=6(x+y+z).$$
Equality holds exactly when the three square roots are equal, or $x=y=z$. Thus equality occurs precisely when the three mutually perpendicular edges $DA,DB,DC$ also have equal lengths.''',['Solid geometry','Orthocentre','Cauchy–Schwarz'])
add(1970,6,'Combinatorics',4.5,'A four-point geometric obstruction gives a 75% bound. Applying it to five points and using integrality improves it to 70%, which a second double count transfers to the full set.',r'Among all triangles determined by 100 points in the plane, with no three collinear, prove that at most 70% are acute.',r'''Any four points determine a nonacute triangle. If they form a convex quadrilateral, at least one of its interior angles is at least $90^\circ$, and its two adjacent vertices complete such a triangle. If one point lies inside the triangle of the other three, the three angles about that interior point sum to $360^\circ$; one is at least $120^\circ$, again giving a nonacute triangle.

Now choose any five points. Each of their five four-point subsets has at most three acute triangles. Every triangle belongs to exactly two of those four-point subsets. If $T_5$ is the number of acute triangles, then $2T_5\leq15$. Since $T_5$ is an integer, $T_5\leq7$ out of the ten possible triangles.

Finally let $T$ be the number of acute triangles among all 100 points. Count pairs consisting of an acute triangle and a five-point subset containing it. Each triangle occurs in $\binom{97}{2}$ such subsets, while each five-point subset contributes at most seven. Thus
$$T\binom{97}{2}\leq7\binom{100}{5}=\frac7{10}\binom{100}{3}\binom{97}{2}.$$
Cancel the positive common factor to obtain the required 70% bound.''',['Double counting','Geometry','Integrality'],solution_url='https://prase.cz/kalva/imo/isoln/isoln706.html')
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
