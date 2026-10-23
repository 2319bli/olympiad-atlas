from international_completion_helpers import add,save
add(1984,1,'Algebra',4,'A cubic product identity centres the expression at one quarter; a sign case is essential before applying AM–GM to the transformed factors.',r'For nonnegative $x,y,z$ with $x+y+z=1$, prove $0\le xy+yz+zx-2xyz\le7/27$.',r'''Write $F=xy+yz+zx-2xyz$. Since $xyz\le xy$ and $xyz\le xz$, we have $F\ge yz\ge0$.

Expanding and using the sum condition gives
$$4F-1=(1-2x)(1-2y)(1-2z).$$
If one variable exceeds $1/2$, exactly one factor is negative and the others nonnegative, so $F\le1/4<7/27$. Otherwise all three factors are nonnegative and their sum is one. AM–GM bounds their product by $1/27$, yielding $F\le(1+1/27)/4=7/27$. The upper bound is attained at $x=y=z=1/3$, and the lower at $(1,0,0)$ and its permutations.''',['Inequalities','AM-GM','Algebraic identities','Case analysis'])
add(1984,2,'Number Theory',4,'Factor the seventh-power difference to isolate a squared quadratic, then choose a small exact value of that quadratic equal to 7 cubed.',r'Find positive integers $a,b$ such that $7\nmid ab(a+b)$ but $7^7\mid (a+b)^7-a^7-b^7$.',r'''Take $(a,b)=(18,1)$. The identity
$$(a+b)^7-a^7-b^7=7ab(a+b)(a^2+ab+b^2)^2$$
follows by expansion. Here $a^2+ab+b^2=324+18+1=343=7^3$, while $ab(a+b)=18\cdot19=342\equiv-1\pmod7$. Thus the required difference is exactly $7^7\cdot342$, and the first condition also holds.''',['Factorisation','Valuations','Construction'])
add(1984,3,'Combinatorics',5.5,'Apply pigeonhole to the finite sets of colours appearing on concentric circles, then tune an angle so that a point on the smaller circle generates the larger one.',r'Fix distinct plane points $O,A$. For $X\ne O$, let $\alpha(X)\in[0,2\pi)$ be the counterclockwise angle from $OA$ to $OX$, and let $C(X)$ have centre $O$ and radius $OX+\alpha(X)/OX$. Prove that every finite colouring of the plane has a point $Y$ with $\alpha(Y)>0$ whose colour occurs on $C(Y)$.',r'''Suppose there are $k$ colours. For each radius $r\in[1,2]$, record the nonempty set of colours appearing on the circle centred at $O$ of radius $r$. There are at most $2^k$ such sets, so among $2^k+1$ distinct radii two, say $r<R$, have the same colour set.

Choose $Y$ at radius $r$ and angle $\theta=r(R-r)$. This angle is strictly positive and less than two, hence less than $2\pi$. By definition, $C(Y)$ has radius $r+\theta/r=R$. The colour of $Y$ appears on the smaller circle and therefore on the larger circle because their colour sets are identical. This is exactly the desired conclusion.''',['Pigeonhole principle','Colouring','Sets','Construction'])
add(1984,4,'Geometry',4.5,'Express tangency as the ratio of half-chord length to midpoint distance from the intersection of the supporting lines; equality of the two ratios is exactly the intercept theorem.',r'A convex quadrilateral $ABCD$ has line $CD$ tangent to the circle with diameter $AB$. Prove that line $AB$ is tangent to the circle with diameter $CD$ exactly when $BC\parallel AD$.',r'''If $AB\parallel CD$, their distance equals $AB/2$ by the given tangency. The reverse tangency holds exactly when $CD=AB$, which for this convex quadrilateral is exactly the parallelogram condition $BC\parallel AD$.

Otherwise let the supporting lines meet at $O$. Convexity puts each segment on one ray from $O$; reversing the vertex labels if necessary, their orders are $O,A,B$ and $O,D,C$. Let $\theta$ be the angle between the rays. The given tangency says that the distance of the midpoint of $AB$ to line $CD$ equals $AB/2$, namely
$$\sin\theta=\frac{OB-OA}{OB+OA}.$$
The reverse tangency is equivalent to
$$\sin\theta=\frac{OC-OD}{OC+OD}.$$
These two equations are equivalent to $OA/OB=OD/OC$. By the intercept theorem this is equivalent to $AD\parallel BC$.''',['Tangency','Similarity','Ratios','Quadrilaterals'])
add(1984,5,'Geometry',6,'The lower bound comes from summing strict triangle inequalities for crossing diagonals; the upper bound requires counting boundary arcs separately for odd and even vertex counts.',r'A convex $n$-gon, $n>3$, has perimeter $p$ and total diagonal length $d$. Prove $n-3<2d/p<\lfloor n/2\rfloor\lfloor(n+1)/2\rfloor-2$.',r'''Number vertices cyclically. For each diagonal $A_iA_j$, the shifted diagonal $A_{i+1}A_{j+1}$ crosses it. Splitting at their intersection and applying triangle inequalities gives
$$|A_iA_j|+|A_{i+1}A_{j+1}|>|A_iA_{i+1}|+|A_jA_{j+1}|.$$
Sum over all oriented diagonals. Each diagonal length appears four times and each side $2(n-3)$ times, so $4d>2(n-3)p$.

For the upper bound, the sum over $i$ of chords $|A_iA_{i+r}|$ is strictly less than $rp$, by comparing each chord with its $r$-side boundary arc.

If $n=2m+1$, taking $r=2,\ldots,m$ counts every diagonal once. Hence $d<\sum_{r=2}^m rp=[m(m+1)/2-1]p$.

If $n=2m$, take $r=2,\ldots,m-1$ for the nonopposite diagonals. Each of the $m$ opposite-vertex diagonals is shorter than either half-boundary arc and therefore shorter than $p/2$. Thus $d<[\sum_{r=2}^{m-1}r+m/2]p=(m^2/2-1)p$. These are exactly the stated upper bounds.''',['Geometric inequalities','Double counting','Polygons','Triangle inequality'])
add(1984,6,'Number Theory',6,'Compare the two power-of-two sums, then use the exact 2-adic behaviour of b−a and b+a to force their sum to be a single power of two and finish by oddness.',r'Odd integers satisfy $0<a<b<c<d$, $ad=bc$, $a+d=2^k$, and $b+c=2^m$. Prove $a=1$.',r'''Since $d=bc/a$,
$$a+d-b-c=\frac{(b-a)(c-a)}a>0,$$
so $k>m$. Substituting the sums into $ad=bc$ yields
$$(b-a)(b+a)=2^m(b-2^{k-m}a).$$
The parenthesis on the right is odd. Of the two even numbers $b-a,b+a$, exactly one is divisible by four, since their difference $2a$ is twice an odd number. Hence one factor is divisible by $2^{m-1}$.

But $0<b-a<b<2^{m-1}$ because $b<c$ and $b+c=2^m$. Therefore $2^{m-1}\mid b+a$. Also $0<b+a<2b<2^m$, forcing $b+a=2^{m-1}$.

Consequently $b=2^{m-1}-a$, $c=2^{m-1}+a$. The product relation becomes $a(2^k-a)=2^{2m-2}-a^2$, so $a2^k=2^{2m-2}$. Since $a$ is positive and odd, $a=1$.''',['Valuations','Diophantine equations','Powers','Parity'])
save()
