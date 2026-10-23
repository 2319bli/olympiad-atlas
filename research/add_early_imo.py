from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');raw=p/'international-raw';r=json.loads((p/'international-reviews.json').read_text())
def add(year,num,topic,rating,reason,statement,solution='',tags=None,solution_url=None,note=None):
 slug=f'imo_{year}_official_p{num}'
 d={'id':slug,'competition_code':'IMO','competition':'IMO','year':year,'problem_number':str(num),'primary_domain':topic,'topics':[[topic,t] for t in (tags or [])],'problem_markdown':statement,'solutions_markdown':[solution],'officialSourceUrl':f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf','officialSolutionUrl':solution_url or f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf','reviewNote':note or 'Statement checked against the official released paper; worked exposition independently written and checked.'}
 (raw/(slug+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2));r[slug]=[rating,reason]
add(1959,1,'Number theory',1.5,'A single integer linear combination of numerator and denominator equals one, immediately forcing coprimality.',r'For every positive integer $n$, prove that $(21n+4)/(14n+3)$ is in lowest terms.')
add(1959,2,'Algebra',2.5,'Squaring once reduces the radical sum to $2x+2|x-1|$, followed by a short domain and interval check.',r'Solve $\sqrt{x+\sqrt{2x-1}}+\sqrt{x-\sqrt{2x-1}}=A$ over the reals when $A=\sqrt2,1,2$, with principal square roots.')
add(1959,3,'Algebra',3.5,'Eliminate $\cos x$ using the double-angle formula and square once; the special case needs attention to the extra sign choices introduced by squaring.',r'Given $a\cos^2x+b\cos x+c=0$, form the associated quadratic equation in $\cos2x$ using $a,b,c$. Compare the two equations when $(a,b,c)=(4,2,-1)$.',note='The official wording says the equations have the same roots; the elimination necessarily may introduce extra solutions in x, which the comparison must discuss. Excluded from the target band after assessment.')
add(1959,4,'Geometry',3,'The hypotenuse median is half the hypotenuse; the geometric-mean condition gives $\sin2A=1/2$, leaving a standard 15-degree construction.',r'Construct a right triangle with prescribed hypotenuse $c$ whose median to the hypotenuse is the geometric mean of its two legs.')
add(1959,5,'Geometry',4.5,'One coordinate choice handles the circle intersection, reveals the fixed radical-axis point and then identifies the entire midpoint locus.',r'''Choose $M$ inside a fixed segment $AB$. On the same side of $AB$, construct squares $AMCD$ and $MBEF$. Their circumcircles, centred at $P,Q$, intersect at $M,N$. Let $N'=AF\cap BC$.

Prove $N=N'$, find a fixed point through which $MN$ always passes, and determine the locus of the midpoint of $PQ$.''',r'''Scale and place $A=(0,0)$, $B=(1,0)$, $M=(t,0)$, where $0<t<1$. Then $C=(t,t)$ and $F=(t,1-t)$. Put $D_0=t^2+(1-t)^2$. Solving the two line equations gives
$$N'=\left(\frac{t^2}{D_0},\frac{t(1-t)}{D_0}\right).$$
The first circumcircle has equation $x^2+y^2-tx-ty=0$. The second has equation
$$x^2+y^2-(1+t)x-(1-t)y+t=0.$$
Substitution shows that $N'$ lies on both. Its positive second coordinate shows $N'\ne M$, proving $N'=N$.

Subtracting the circle equations gives their radical axis
$$x-(2t-1)y-t=0.$$
It always passes through $S=(1/2,-1/2)$, the point one half of $AB$ below its midpoint. Thus every line $MN$ passes through $S$.

Finally,
$$P=(t/2,t/2),\qquad Q=((1+t)/2,(1-t)/2).$$
The midpoint of $PQ$ is $((1+2t)/4,1/4)$. As $t$ runs through $(0,1)$, these points fill the open segment parallel to $AB$, at distance $AB/4$ above it, between the perpendiculars through the quarter-points of $AB$.''',['Coordinates','Radical axis','Loci'])
add(1959,6,'Geometry',5.5,'First reduce the two-plane construction to one plane. The tangency condition then becomes a circle-line intersection, with a genuine existence condition and two configurations.',r'''Planes $P,Q$ meet in a line $p$. Points $A\in P$ and $C\in Q$ are given, neither on $p$. Construct an isosceles trapezoid $ABCD$ with $AB\parallel CD$, $B\in P$, $D\in Q$, which has an incircle. Discuss when the construction is possible.''',r'''The required plane must be the plane $T$ through $A,C$ parallel to $p$: the two parallel bases lie in $P,Q$, so their direction must be parallel to $P\cap Q$. In $T$, draw the parallel lines through $A,C$. Choose coordinates $A=(0,0)$, $C=(u,h)$, with $h>0$ and with the direction of the first axis chosen so that $u\geq0$.

In an isosceles trapezoid write $B=(b,0)$, $D=(d,h)$. Equality of the base midpoints gives $d=b-u$, while the base lengths are $b=u+d$ and $c=u-d$. Thus their sum is $2u$. A tangential quadrilateral has the same sum for each pair of opposite sides, so the equal legs must have length $u$. Consequently
$$AD^2=d^2+h^2=u^2.$$
There is a solution precisely when $u\geq h$. Construct $D$ as either intersection of the line through $C$ parallel to $p$ with the circle of centre $A$ and radius $u$. Reflect $A$ in the perpendicular bisector of $CD$ to obtain $B$. Since $|d|<u$, both bases have positive length. There are two choices if $u>h$ and one, a square, if $u=h$.

For completeness the resulting trapezoid really has an incircle. The point on its symmetry axis halfway between the base lines is at distance $h/2$ from each base. Its distance from either leg is also $h/2$: the area of the triangle formed with that leg equals $uh/4$, and the leg has length $u$. The circle of radius $h/2$ about this point therefore touches all four sides. If $u<h$, the equation $d^2+h^2=u^2$ proves impossibility.''',['Construction','Solid geometry','Tangency'])
add(1960,1,'Number theory',4.5,'Divisibility by eleven creates two digit cases. A parity observation and a square bound reduce the second case to two candidates without a brute-force search.',r'Find all three-digit positive integers $N$ such that $11\mid N$ and $N/11$ is the sum of the squares of the decimal digits of $N$.',r'''Write $N=100a+10b+c$, with $1\leq a\leq9$ and $0\leq b,c\leq9$. The divisibility test gives $a-b+c=0$ or $11$.

If $b=a+c$, then $N/11=10a+c$. Comparing parity with $a^2+b^2+c^2$ shows that $c=2d$ is even. The equation simplifies to
$$a^2+(2d-5)a+4d^2-d=0.$$
For $d=0$ this gives $a=5$. For $d=1$ the discriminant is negative. For $d=2$ the left side is $a^2-a+14>0$, and for $d\geq3$ every coefficient is positive. This case gives $N=550$.

If $b=a+c-11$, then $N/11=10a+c-10$. In particular
$$a^2+c^2\leq10a+c-10\leq10a-1,$$
so $(a-5)^2+c^2\leq24$ and $c\leq4$. The requirement $a+c\geq11$ also gives $c\geq2$. Parity now makes $c$ odd, so $c=3$ and $a=8$ or $9$. Checking these leaves $a=8,b=0$, giving $N=803$.

Both $550/11=50=5^2+5^2$ and $803/11=73=8^2+3^2$ verify the answers.''',['Digits','Divisibility','Bounds'])
add(1960,2,'Algebra',2.5,'Rationalising cancels the apparent fraction and leaves one square-root inequality; retain the excluded value $x=0$.',r'Solve $\dfrac{4x^2}{(1-\sqrt{1+2x})^2}<2x+9$ over the reals.')
add(1960,3,'Geometry',3,'Coordinates on the hypotenuse give the tangent of the angle as cross product divided by dot product; the right-angle identity supplies the desired denominator.',r'In right triangle $ABC$, divide hypotenuse $BC$ of length $a$ into $n$ equal pieces, where $n\geq3$ is odd. The middle piece subtends angle $\alpha$ at $A$. If the altitude from $A$ is $h$, prove $\tan\alpha=4nh/((n^2-1)a)$.')
add(1960,4,'Geometry',4.5,'The given median locates a line at the given altitude; the second altitude becomes an Apollonius ratio, reducing the construction to two standard loci.',r'Construct a triangle from the lengths of its altitudes $h_a,h_b$ from $A,B$ and the length $m_a$ of its median from $A$.',r'''Let $M$ be the midpoint of $BC$. Construct $A,M$ with $AM=m_a$, and draw a line $\ell$ through $M$ at distance $h_a$ from $A$. This is possible only if $m_a\geq h_a$; the two symmetric choices are equivalent.

The area identity $BC\cdot h_a=AC\cdot h_b$, together with $BC=2MC$, says
$$\frac{MC}{AC}=\frac{h_b}{2h_a}=:k.$$
Construct the locus of points $C$ with this ratio. For $k\ne1$ it is the Apollonius circle determined by $A,M,k$; for $k=1$ it is the perpendicular bisector of $AM$. Intersect this locus with $\ell$. For each intersection $C$, reflect $C$ in $M$ to obtain $B$.

These constructions use only straightedge and compasses: an Apollonius circle is obtained from the internal and external division points of $AM$ in the prescribed ratio, as endpoints of a diameter. All intersections are admissible, since $k>0$ ensures $C\ne M$ and $h_a>0$ makes the triangle nondegenerate.

Conversely, every desired triangle has its midpoint $M$ on just such a line and its vertex $C$ on just such a ratio locus. Thus the construction finds all solutions and detects nonexistence when the loci do not meet. More explicitly, solutions exist if $m_a>h_a$ and $h_b\leq2m_a$, or if $m_a=h_a$ and $h_b<2m_a$. To verify this last condition, write $A=(0,h_a)$, $M=(v,0)$ with $v^2+h_a^2=m_a^2$, and $C=(v+t,0)$; the ratio equation is a quadratic whose discriminant has the sign of $m_a^2-h_b^2/4$. When $v=0$ and $k=1$, that equation has no solution.''',['Construction','Apollonius circle','Areas'])
add(1960,5,'Geometry',2.5,'Both loci are affine images of two perpendicular segments, hence a square and a rectangle with immediately determined dimensions.',r'In cube $ABCDA\prime B\prime C\prime D\prime$, let $X\in AC$ and $Y\in B\prime D\prime$. Find the loci of the midpoint of $XY$, and of $Z\in XY$ with $ZY=2XZ$.')
add(1960,6,'Geometry',4.5,'The cone and insphere formulas reduce the volume ratio to one dimensionless variable; a sharp AM–GM inequality identifies the unique extremal shape and its constructible apex angle.',r'''A right circular cone contains a sphere tangent to its base and curved surface. Circumscribe a cylinder about the sphere with one cylinder base in the cone's base plane. If the respective volumes are $V_1,V_2$, prove $V_1\ne V_2$, determine the minimum of $V_1/V_2$, and construct the apex angle of an axial section in the equality case.''',r'''Let the cone have base radius $R$, height $H$ and slant height $l=\sqrt{R^2+H^2}$. Its axial section has inradius
$$r=\frac{RH}{R+l}.$$
The cylinder has radius $r$ and height $2r$, so
$$\frac{V_1}{V_2}=\frac{\pi R^2H/3}{2\pi r^3}=\frac{(R+l)^3}{6RH^2}.$$
Set $t=l/R>1$ and use $H^2=R^2(t^2-1)$. The ratio becomes
$$\frac{(t+1)^2}{6(t-1)}=\frac{(t-1)+4+4/(t-1)}6\geq\frac43,$$
by AM–GM, with equality precisely when $t-1=2$. Thus the minimum is $4/3$, and equality of the two volumes is impossible.

At the minimum, $l=3R$. If $\phi$ is half the axial apex angle, then $\sin\phi=R/l=1/3$. Construct a right triangle with hypotenuse three units and one leg one unit; double the angle opposite the one-unit leg. This constructs the required angle $2\arcsin(1/3)$.''',['Solid geometry','Inequalities','Optimisation'])
add(1960,7,'Geometry',3.5,'The two right-angle conditions coincide by symmetry and reduce to $y(h-y)=ac/4$; its discriminant settles all cases.',r'An isosceles trapezoid has bases $a,c$ and height $h$. Find the points on its symmetry axis from which each leg subtends a right angle, their distances to the bases, and the conditions for existence.')
add(1961,1,'Algebra',3.5,'Eliminating $xy$ determines $z$ and a quadratic for $x,y$; the discriminant and signs provide the complete parameter conditions.',r'Solve $x+y+z=a$, $x^2+y^2+z^2=b^2$, $xy=z^2$ over the reals, and determine when the three unknowns are distinct and positive.')
add(1961,2,'Geometry',2.5,'Weitzenböck’s inequality follows directly from Heron’s formula and a sum-of-squares identity, with equality only for the equilateral triangle.',r'For a triangle with side lengths $a,b,c$ and area $T$, prove $a^2+b^2+c^2\geq4\sqrt3T$ and identify equality.')
add(1961,3,'Algebra',3,'A short split into odd and even exponents, using $|\sin x|,|\cos x|\leq1$, settles all powers; the first power is a separate elementary trig equation.',r'For each positive integer $n$, solve $\cos^n x-\sin^n x=1$ over real $x$.')
add(1961,4,'Geometry',2.5,'Area coordinates sum to one, so one is at most one third and another at least one third; the cevian ratios are their complementary ratios.',r'Let $P$ be inside triangle $P_1P_2P_3$, and let $P_iP$ meet the opposite side at $Q_i$. Prove that among $P_iP/PQ_i$ there is a value at most $2$ and a value at least $2$.')
add(1961,5,'Geometry',4.5,'Introduce the median and half-base as two unknown lengths; the cosine rule determines their squares and product, leading to a constructible quadratic and an exact existence boundary.',r'''Construct triangle $ABC$ from $AC=b$, $AB=c$ and $\angle AMB=\omega$, where $M$ is the midpoint of $BC$ and $0<\omega<90^\circ$. Prove that this is possible exactly when $b\tan(\omega/2)\leq c<b$, and explain the equality case.''',r'''Put $x=AM$, $y=BM=CM$. Applying the cosine rule to $AMB$ and $AMC$ gives
$$c^2=x^2+y^2-2xy\cos\omega,\qquad b^2=x^2+y^2+2xy\cos\omega.$$
Thus
$$x^2+y^2=S:=\frac{b^2+c^2}{2},\qquad xy=P:=\frac{b^2-c^2}{4\cos\omega}.$$
Positive $x,y$ exist precisely when $P>0$ and $S\geq2P$. The first condition is $c<b$; rearranging the second gives
$$c^2(1+\cos\omega)\geq b^2(1-\cos\omega),$$
equivalent to $c\geq b\tan(\omega/2)$.

When these conditions hold, construct
$$x+y=\sqrt{S+2P},\qquad |x-y|=\sqrt{S-2P},$$
then take their half-sum and half-difference for $x,y$ (either order). These are standard straightedge-and-compass operations. At $M$, draw rays making angle $\omega$, place $A,B$ at distances $x,y$, and reflect $B$ in $M$ to obtain $C$. The two cosine-rule identities verify $AB=c,AC=b$.

Equality in the lower bound means $x=y$. Then $AM=BM=CM$, so $M$ is the circumcentre of $ABC$ and $BC$ a diameter: the angle at $A$ is right. Conversely a right angle at $A$ gives $AM=BM$ and equality.''',['Construction','Cosine rule','Existence conditions'])
add(1961,6,'Geometry',2.5,'The centroid is an affine average of three fixed and three freely varying points; choosing the three varying points equal proves the whole parallel plane is attained.',r'Points $A,B,C$ are noncollinear and on the same side of a plane $\varepsilon$, and their plane is not parallel to it. Choose $A\prime,B\prime,C\prime$ freely on $\varepsilon$. Let $L,M,N$ be the midpoints of $AA\prime,BB\prime,CC\prime$. Find the locus of the centroid of nondegenerate triangles $LMN$.')
add(1962,1,'Number theory',3.5,'Writing the digit rotation algebraically reduces the task to powers of ten modulo thirteen; the first suitable exponent gives 153846.',r'Find the smallest positive integer ending in digit $6$ such that moving this last digit to the front multiplies the integer by four.')
add(1962,2,'Algebra',2.5,'The radical difference is strictly decreasing on its domain; two controlled squarings find the single boundary value.',r'Solve $\sqrt{3-x}-\sqrt{x+1}>1/2$ over real $x$.')
add(1962,3,'Geometry',2.5,'During each quarter of the motion both endpoints move linearly; their midpoint traces four readily computed sides of a rhombus.',r'In cube $ABCDA\prime B\prime C\prime D\prime$, points $X,Y$ start at $A,B\prime$ and move at the same constant speed around $ABCDA$ and $B\prime C\prime CBB\prime$. Determine the locus of the midpoint of $XY$.')
add(1962,4,'Algebra',3,'Double-angle formulas turn the equation into $2t(2t-1)(t+1)=0$ for $t=\cos2x$, followed by elementary trigonometric solutions.',r'Solve $\cos^2x+\cos^2(2x)+\cos^2(3x)=1$ over real $x$.')
add(1962,5,'Geometry',5.5,'Combine the opposite-side tangency condition with the supplementary-angle cosine rule. This determines the two unknown sides by their difference and product and makes the cyclic construction explicit.',r'Three distinct points $A,B,C$ lie on a circle. Using straightedge and compasses, construct a fourth point $D$ on the circle so that the convex quadrilateral $ABCD$ has an incircle.',r'''Put $p=AB$, $q=BC$, $\beta=\angle ABC$, and $d=p-q$. Suppose $u=AD$, $v=CD$. Pitot's condition for a tangential quadrilateral is $p+v=q+u$, or $u-v=d$.

Because opposite angles in a cyclic quadrilateral are supplementary, the cosine rule in the two triangles gives
$$AC^2=d^2+4pq\sin^2(\beta/2)=(u-v)^2+4uv\cos^2(\beta/2).$$
Thus the required lengths must satisfy
$$u-v=d,\qquad uv=K:=pq\tan^2(\beta/2).$$
Construct the positive lengths
$$u=\frac{\sqrt{d^2+4K}+d}{2},\qquad v=\frac{\sqrt{d^2+4K}-d}{2}.$$
They are constructible from the given triangle. Construct $D$ by intersecting the circle of centre $A$ and radius $u$ with the circle of centre $C$ and radius $v$, taking the intersection on the opposite side of $AC$ from $B$.

These circles intersect: $|u-v|=|p-q|<AC$, while
$$(u+v)^2=d^2+4pq\tan^2(\beta/2)>d^2+4pq\sin^2(\beta/2)=AC^2.$$
The cosine rule now gives $\angle ADC=180^\circ-\beta$, so $D$ lies on the original circle. The quadrilateral is convex and satisfies $AB+CD=BC+AD$. The converse of Pitot's theorem therefore supplies its incircle, completing the construction.''',['Construction','Cyclic quadrilaterals','Tangency'],solution_url='https://www.imo-official.org/assets/documents/problems/1962/1962_eng.pdf',note='Official statement verified. Independent cosine-rule construction; the final standard converse of Pitot is documented, for example, in K. Kedlaya, Geometry Unbound, section 8.3 (https://kskedlaya.org/geometryunbound/gu-060118.pdf).')
add(1962,6,'Geometry',2.5,'An axial coordinate calculation in an isosceles triangle proves Euler’s inradius–circumradius identity with little additional invention.',r'An isosceles triangle has circumradius $R$, inradius $r$, and distance $d$ between those centres. Prove $d^2=R(R-2r)$.')
add(1962,7,'Geometry',6.5,'The crucial step classifies all possible edge-tangent spheres using planar incircles and excircles. Equal tangent lengths then force regularity, and the converse needs an explicit spatial construction.',r'''A tetrahedron admits five distinct spheres, each tangent to all six lines containing its edges. Prove that the tetrahedron is regular. Conversely, prove that every regular tetrahedron admits five such spheres.''',r'''A plane through any face cuts an edge-tangent sphere in an incircle or excircle of that face. If a contact point on $SA$ lies beyond $A$, the face $SAB$ forces the contacts on $AB$ to be internal and on $SB$ to lie beyond $B$. Using $SAC$ and $SBC$ similarly shows that the contacts on $AB,BC,CA$ are internal and those on $SA,SB,SC$ external. Therefore the only patterns are: all six contacts internal; or the three contacts on one face internal and the other three external.

Each pattern determines at most one sphere: its circular sections in two adjacent faces are prescribed incircles or excircles, and two such noncoplanar circles determine a sphere uniquely. Five spheres therefore realise all five patterns.

Label the vertices $V_1,V_2,V_3,V_4$. For the wholly internal sphere, let the tangent length from $V_i$ be $a_i$. Then $V_iV_j=a_i+a_j$. For the sphere external on the three edges from $V_1$, the tangent lengths from $V_1$ are $a_1+2a_2$, $a_1+2a_3$, $a_1+2a_4$: its contacts on the opposite face are those of the same face incircle. Equal tangents force $a_2=a_3=a_4$. The corresponding sphere opposite $V_2$ gives $a_1=a_3=a_4$. Every edge is consequently equal.

For the converse, scale a regular tetrahedron to vertices
$$(1,1,1),\ (1,-1,-1),\ (-1,1,-1),\ (-1,-1,1).$$
The origin is at distance $1$ from every edge line. In addition, for each vertex vector $V_i$, the point $-2V_i$ is at distance $3$ from all six edge lines. To check this for $V_1$, an incident line has equations $x=1,y=z$, giving squared distance $9$ from $(-2,-2,-2)$; a nonincident line has equations $z=-1,x+y=0$, giving squared distance $1+8=9$. Symmetry handles the other lines and vertices. Hence the spheres with these five centres and radii $1,3,3,3,3$ have the required tangencies.''',['Solid geometry','Tangency','Classification'],solution_url='https://prase.cz/kalva/imo/isoln/isoln627.html',note='Official statement checked. Classification argument checked against S. Greitzer, International Mathematical Olympiads 1959–1977, solution 1962/7; equal-tangent reduction also in John Scholes’s solution. Exposition rewritten, with an independently checked coordinate converse.')
add(1963,1,'Algebra',1.5,'For the nested radical printed in the official English paper, squaring immediately gives $2\sqrt{x^2-1}=p$; the domain completes the solution.',r'For a real parameter $p$, solve $\sqrt{x^2-p+2\sqrt{x^2-1}}=x$.',note='Follows the nested radical visible in the official English PDF. Some secondary transcriptions instead print two separate outer radicals, a different problem.')
add(1963,2,'Geometry',4.5,'Replace the moving point on the segment by a parameter. The perpendicularity expression is linear in that parameter, so opposite endpoint signs give a precise three-dimensional region between two diameter spheres.',r'A point $A$ and a segment $BC$ are given in space. Determine all possible vertices of a right angle whose one arm passes through $A$ and whose other arm meets $BC$.',r'''Let $\Sigma_B,\Sigma_C$ be the closed balls with diameters $AB,AC$. The locus consists of the points lying inside or on one of their boundary spheres and outside or on the other. Boundary points common to both are included.

For a candidate vertex $X$, put
$$F_B=(X-A)\cdot(X-B),\qquad F_C=(X-A)\cdot(X-C).$$
A point $Q=(1-t)B+tC$, $0\leq t\leq1$, satisfies $XA\perp XQ$ exactly when
$$0=(X-A)\cdot(X-Q)=(1-t)F_B+tF_C.$$
Such a $t$ exists precisely when $F_BF_C\leq0$. But
$$F_B=\left|X-\frac{A+B}{2}\right|^2-\frac{|A-B|^2}{4},$$
so $F_B\leq0$ means $X\in\Sigma_B$, and similarly for $C$. This proves the stated description, including both boundary spheres where appropriate.

If $X=A$ or $X\in BC$, one of the arms may meet its required point at the vertex itself; choose the other arm perpendicular to the specified one. These cases are also included by the same closed-locus convention. If a convention requires the specified points to differ from the angle vertex, omit just those degenerate incidences.''',['Loci','Solid geometry','Vectors'])
add(1963,3,'Geometry',5.5,'Closure of the equiangular polygon is rewritten in terms of successive side-length drops. All regular-polygon prefix vectors lie in one open half-plane, so nonnegative drops cannot cancel.',r'An equiangular polygon has consecutive side lengths $a_1\geq a_2\geq\cdots\geq a_n$. Prove that all its side lengths are equal.',r'''Orient the polygon counterclockwise and identify its plane with the complex plane. Consecutive unit side directions are
$$u_j=e^{2\pi i(j-1)/n},\qquad 1\leq j\leq n,$$
after a rotation. Closure gives $\sum a_ju_j=0$, while $\sum u_j=0$.

Set $d_k=a_k-a_{k+1}\geq0$ for $1\leq k<n$, and $S_k=u_1+\cdots+u_k$. Summation by parts gives
$$0=\sum_{j=1}^n a_ju_j=\sum_{k=1}^{n-1}d_kS_k.$$
The finite geometric sum is
$$S_k=\frac{\sin(k\pi/n)}{\sin(\pi/n)}e^{(k-1)\pi i/n}.$$
Its positive factor does not affect its direction. Thus the arguments of $S_1,\ldots,S_{n-1}$ range from $0$ to $(n-2)\pi/n$, an interval strictly shorter than $\pi$. Their projections onto the direction with argument $(n-2)\pi/(2n)$ are all strictly positive.

Project the identity $\sum d_kS_k=0$ onto that direction. Every summand is nonnegative, and it can vanish only if $d_k=0$. Hence every successive difference is zero, giving $a_1=\cdots=a_n$.''',['Polygons','Complex numbers','Summation by parts'])
add(1963,4,'Algebra',4.5,'Summing isolates one exceptional parameter. Combining neighbouring equations on the zero-sum subspace then yields a quadratic for the remaining exceptional parameters and a two-parameter solution family.',r'''For each real $y$, find all real five-tuples satisfying
$$x_5+x_2=yx_1,\quad x_1+x_3=yx_2,\quad x_2+x_4=yx_3,\quad x_3+x_5=yx_4,\quad x_4+x_1=yx_5.$$''',r'''The zero tuple is always a solution. Summing the equations gives $(2-y)(x_1+\cdots+x_5)=0$.

When $y=2$, the recurrence $x_{i+1}-x_i=x_i-x_{i-1}$ makes the consecutive differences constant, with subscripts read cyclically. Their sum is zero, so all $x_i$ are equal. Thus the solutions are $(a,a,a,a,a)$.

Suppose $y\ne2$. Then $\sum x_i=0$. Apply the recurrence twice:
$$y^2x_i=y(x_{i-1}+x_{i+1})=x_{i-2}+2x_i+x_{i+2}.$$
The zero-sum condition gives $x_{i-2}+x_{i+2}=-x_i-(x_{i-1}+x_{i+1})=-(1+y)x_i$, so
$$(y^2+y-1)x_i=0.$$
Nonzero solutions can therefore occur only at $y=(-1\pm\sqrt5)/2$.

For either of these values, choose $x_1=a,x_2=b$ arbitrarily and use the recurrence and $y^2=1-y$ to obtain
$$(x_1,x_2,x_3,x_4,x_5)=(a,b,yb-a,-y(a+b),ya-b).$$
Direct substitution verifies all five equations, so this is the full family. At every other parameter, only the zero tuple occurs.''',['Linear systems','Recurrences','Parameters'])
add(1963,5,'Algebra',3,'Multiplication by $2\sin(\pi/7)$ makes the sine terms telescope, leaving a standard trigonometric identity.',r'Prove $\cos(\pi/7)-\cos(2\pi/7)+\cos(3\pi/7)=1/2$.')
add(1963,6,'Combinatorics',3.5,'There are only three possible choices of two disjoint consecutive pairs in the second prediction; treating each as a block gives a short finite case check and the order EDACB.',r'''Five contestants are named $A,B,C,D,E$. The prediction $ABCDE$ gets no position correct and no ordered consecutive pair correct. The prediction $DAECB$ gets exactly two positions correct and two disjoint ordered consecutive pairs correct. Determine the actual finishing order.''',note='Consecutive pairs are read in their predicted order; this interpretation yields EDACB, while treating pairs as unordered is inconsistent.')
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
