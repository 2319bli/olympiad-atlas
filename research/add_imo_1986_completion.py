from international_completion_helpers import add,save
add(1986,1,'Number Theory',4,'The obstruction appears only after using the full square-residue set modulo sixteen; the three proposed square conditions eliminate complementary residue classes for d.',r'For every positive integer $d\notin\{2,5,13\}$, prove some distinct $a,b\in\{2,5,13,d\}$ make $ab-1$ nonsquare.',r'''Suppose $2d-1,5d-1,13d-1$ were all squares. Squares modulo sixteen lie in $\{0,1,4,9\}$. The first condition forces $d\equiv1,5,9,13\pmod{16}$. For $d\equiv1$ or 13, $13d-1$ has residue 12 or 8, impossible for a square. For $d\equiv5$ or 9, $5d-1$ has residue 8 or 12, also impossible. Hence at least one of the three products involving $d$ is nonsquare. Its two factors are distinct by the hypothesis on $d$.''',['Modular arithmetic','Squares','Case analysis'])
add(1986,2,'Geometry',4.5,'Compose one block of three rotations as a translation; returning after 662 blocks forces that translation to vanish, and its complex coefficient identifies an equilateral triangle.',r'Start from any plane point $P_0$. Repeatedly rotate $120^\circ$ clockwise about $A_1,A_2,A_3,A_1,\ldots$ to obtain $P_1,P_2,\ldots$. If $P_{1986}=P_0$, prove triangle $A_1A_2A_3$ is equilateral.',r'''Use complex coordinates and put $\omega=e^{-2\pi i/3}$. Rotation about $a$ sends $z$ to $\omega z+(1-\omega)a$. Composing the three rotations sends
$$z\longmapsto z+t,\qquad t=(1-\omega)(\omega^2a_1+\omega a_2+a_3),$$
because $\omega^3=1$. After 1986 steps there have been 662 identical blocks, so $P_{1986}=P_0$ forces $662t=0$, hence $t=0$.

Using $1+\omega+\omega^2=0$, this becomes
$$a_3-a_1=-\omega(a_2-a_1).$$
The multiplier $-\omega$ has modulus one and angle $60^\circ$. Thus $A_1A_3=A_1A_2$ and their included angle is $60^\circ$, so all three sides are equal.''',['Complex numbers','Rotation','Transformations'])
add(1986,3,'Combinatorics',6.5,'The invariant positive total makes a quadratic expression decrease at every legal move; discovering the combination of single-entry and adjacent-pair squares supplies termination for every move order.',r'Integers on a pentagon have positive total. Whenever three consecutive labels are $x,y,z$ with $y<0$, one may replace them by $x+y,-y,z+y$. Must repeated legal moves always stop?',r'''Yes. Let the cyclic labels be $a_1,\ldots,a_5$ and their total be $S>0$, which the operation preserves. Define the nonnegative integer
$$V=\sum_{i=1}^5a_i^2+\sum_{i=1}^5(a_i+a_{i+1})^2,$$
with cyclic indices. Suppose the operated negative label is $a_1=a$, with neighbours $a_5=e,a_2=b$, and remaining labels $c,d$.

The change in the first sum is $2a(a+b+e)$. The adjacent pair sums change from $a+b,b+c,c+d,d+e,e+a$ to $b,a+b+c,c+d,d+e+a,e$, so their squared-sum change is $2a(c+d)$. Therefore
$$V_{\rm new}-V=2aS<0.$$
A nonnegative integer cannot decrease strictly infinitely often. Thus every sequence of legal moves terminates, necessarily with all labels nonnegative.''',['Monovariants','Invariants','Termination','Algebraic identities'])
add(1986,4,'Geometry',6.5,'Analyse one transition around a vertex using the adjacent-side parameters; the rigid triangle’s apex stays on the angle bisector, and a quadratic constraint gives the exact excursion beyond the centre.',r'Let $A,B$ be adjacent vertices of a regular $n$-gon with centre $O$, where $n\ge5$. A rigid triangle $XYZ$, initially $OAB$, moves continuously with $Y,Z$ on the polygon boundary, each traversing that boundary, and $X$ inside. Determine the locus of $X$.',r'''Let the polygon side be $s$, circumradius $R$, and $\alpha=\pi/n$. The locus is the union of $n$ radial segments beginning at $O$, each directed away from a polygon vertex, of length $R(\sec\alpha-1)$.

Scale $s$ to two. Two boundary points at distance two can lie on the same side only as its endpoints; otherwise they are on adjacent sides. For nonadjacent sides, take their shorter boundary chain and project onto its central direction: that of the middle intervening side, or halfway between the two middle directions. The end segments and all intervening sides have nonnegative projection. A single middle side contributes two; two middle sides contribute $4\cos\alpha>2$. Equality can occur only at the nearest endpoints of sides separated by one side. Thus no other nonadjacent positions have distance two.

During a transition about a vertex $V$, choose coordinates with $V=(0,0)$ and its inward bisector the positive vertical axis. Write
$$Y=p(-\cos\alpha,\sin\alpha),\quad Z=q(\cos\alpha,\sin\alpha),\quad0\le p,q\le2.$$
The fixed-base constraint is
$$4=(p+q)^2\cos^2\alpha+(p-q)^2\sin^2\alpha.$$
The inward apex of the congruent triangle is $X=(0,(p+q)/(2\sin\alpha))$. Along the continuous transition, $p+q$ runs from 2 to $2\sec\alpha$ and back to 2. Since $O=(0,\csc\alpha)$, this traces exactly the claimed segment. Its far endpoint remains inside the polygon because $\sec\alpha-1<\cos\alpha$ for $\alpha\le\pi/5$, placing the segment within the incircle. The other vertices give the rotated segments. Restoring scale gives the displayed length.''',['Locus','Coordinates','Trigonometry','Polygons'])
add(1986,5,'Algebra',5.5,'Use the functional equation to identify the full zero set; comparing the zero thresholds in x on both sides determines every positive value without assuming continuity.',r'Find all $f:[0,\infty)\to[0,\infty)$ satisfying $f(xf(y))f(y)=f(x+y)$, $f(2)=0$, and $f(t)>0$ for $0\le t<2$.',r'''Putting $y=2$ shows $f(x+2)=0$ for all $x\ge0$. Thus the zero set is exactly $[2,\infty)$.

Fix $0\le y<2$, so $f(y)>0$. For every $x\ge0$, the equation implies
$$x\ge2-y\quad\Longleftrightarrow\quad f(x+y)=0\quad\Longleftrightarrow\quad xf(y)\ge2.$$
The two closed half-line thresholds must agree, giving $f(y)=2/(2-y)$.

Therefore the only candidate is $f(t)=2/(2-t)$ for $t<2$, and zero for $t\ge2$. If $y\ge2$, both sides of the equation vanish. If $y<2$ and $x+y\ge2$, both vanish again. Otherwise direct substitution gives
$$f(xf(y))f(y)=\frac{2-y}{2-y-x}\frac2{2-y}=\frac2{2-x-y}=f(x+y).$$
Hence this candidate works and is unique.''',['Functional equations','Zero sets','Threshold argument'])
add(1986,6,'Combinatorics',4.5,'Pair points separately in every row and column; the union of the two matchings consists of paths and even cycles, so alternating colours balance every pair.',r'Given finitely many integer-coordinate points in the plane, can they always be coloured red and white so that every horizontal or vertical line has colour counts differing by at most one?',r'''Yes. In each horizontal line, pair its points arbitrarily, leaving at most one unpaired. Do the same independently in each vertical line. Form a graph whose vertices are the given points and whose edges are these pairs.

Each vertex has at most one horizontal edge and at most one vertical edge, so every component is a path, an isolated vertex, or a cycle. On a cycle the edge types alternate, so the cycle has even length. Therefore every component can be coloured alternately red and white, making the endpoints of every pair different colours.

On any horizontal line all its paired points cancel in the colour difference, leaving at most its one unpaired point. The same holds on every vertical line. Hence all required differences are at most one.''',['Graph theory','Colouring','Matchings','Construction'])
save()
