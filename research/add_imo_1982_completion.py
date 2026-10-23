from international_completion_helpers import add,save
add(1982,1,'Algebra',5,'Superadditivity forces exact values on multiples of three up to the prescribed endpoint; tripling the requested input then squeezes its value between consecutive integers.',r'A function $f:\mathbb Z_{>0}\to\mathbb Z_{\ge0}$ has $f(m+n)-f(m)-f(n)\in\{0,1\}$, $f(2)=0$, $f(3)>0$, and $f(9999)=3333$. Determine $f(1982)$.',r'''The condition at $1+1$ gives $f(1)=0$, and then $f(3)=1$. Repeated superadditivity gives $f(3k)\ge k$. If this were strict for any $k\le3333$, adding $3333-k$ further threes would contradict $f(9999)=3333$. Thus $f(3k)=k$ throughout that range.

Now $1982=1980+2$ gives $f(1982)\ge f(1980)=660$. On the other hand,
$$3f(1982)\le f(5946)=1982,$$
so the integer $f(1982)\le660$. Hence it equals $660$. The data are consistent, for example with $f(n)=\lfloor n/3\rfloor$.''',['Functional equations','Superadditivity','Integer bounds'])
add(1982,2,'Geometry',7,'Represent the incircle contacts by unit complex numbers to prove the reflected-contact triangle is homothetic to the original; Euler’s radius inequality rules out the exceptional parallel-line case.',r'In a scalene triangle $A_1A_2A_3$, let $M_i$ be the midpoint of the side opposite $A_i$ and $T_i$ its incircle contact. Reflect $T_i$ in the internal angle bisector at $A_i$ to obtain $S_i$. Prove that $M_1S_1,M_2S_2,M_3S_3$ are concurrent.',r'''Scale the incircle to the unit circle centred at zero, and use complex coordinates $t_1,t_2,t_3$ for its contacts. The intersection of tangents at $t_j,t_k$ is
$$a_i=\frac{2t_jt_k}{t_j+t_k}.$$
Reflection in the angle-bisector line through zero and $a_i$ sends $t_i$ to
$$s_i=\frac{a_i}{\bar a_i}\bar t_i=\frac{t_jt_k}{t_i}.$$
Consequently direct subtraction gives, for each pair $i,j$,
$$s_i-s_j=K(a_i-a_j),\qquad K=\frac{(t_1+t_2)(t_2+t_3)(t_3+t_1)}{2t_1t_2t_3}.$$
Conjugating the expression shows $K$ is real. Thus $s_i=Ka_i+v$ for a fixed $v$.

The midpoint coordinates satisfy $m_i=(a_1+a_2+a_3-a_i)/2$, so $s_i=\lambda m_i+w$ with real $\lambda=-2K$ and fixed $w$. The circumradius of the $S$-triangle is one, while that of the midpoint triangle is $R/2$, where $R$ is the original circumradius. Hence $|\lambda|=2/R<1$, by the strict Euler inequality $R>2r=2$ for a nonequilateral triangle. In particular $\lambda\ne1$.

The fixed point $h=w/(1-\lambda)$ satisfies $s_i-h=\lambda(m_i-h)$, so all three lines pass through $h$. In a scalene triangle $S_i\ne M_i$: equality would put the side midpoint on the incircle, forcing it to be the contact and the two adjacent sides equal. Thus all three lines are well-defined.''',['Complex numbers','Homothety','Concurrency','Triangle centres','Circles'])
add(1982,3,'Algebra',4.5,'A square identity supplies a telescoping lower bound when the sequence tends to zero; a positive limiting value instead forces divergence. A geometric sequence attains the limiting constant.',r'Let $1=x_0\ge x_1\ge x_2\ge\cdots>0$. Prove some partial sum $\sum_{i=0}^{n-1}x_i^2/x_{i+1}$ is at least $3.999$, and construct such a sequence for which every partial sum is below four.',r'''Since $(x_i-2x_{i+1})^2\ge0$,
$$\frac{x_i^2}{x_{i+1}}\ge4(x_i-x_{i+1}).$$
Summing gives a lower bound $4(1-x_n)$. If the decreasing sequence tends to zero, this bound exceeds $3.999$ for sufficiently large $n$. If its limit is $\ell>0$, every summand is at least $x_i\ge\ell$, so the partial sums diverge and again exceed $3.999$.

For the construction take $x_i=2^{-i}$. The partial sum is $2+1+\cdots+2^{2-n}=4(1-2^{-n})<4$ for every $n$.''',['Inequalities','Telescoping','Sequences','Geometric series'])
add(1982,4,'Number Theory',4.5,'Find an order-three linear transformation preserving the cubic form, then analyse its possible residues modulo nine to rule out the specified value.',r'If $x^3-3xy^2+y^3=n$ has an integer solution for a positive integer $n$, prove it has at least three. Show that $n=2891$ has none.',r'''The transformation $T(x,y)=(y-x,-x)$ preserves the cubic form by expansion, and $T^2(x,y)=(-y,x-y)$, $T^3(x,y)=(x,y)$. A fixed point of either nontrivial power must satisfy $x=y=0$, whose cubic value is zero. Thus any solution for positive $n$ lies in an orbit of three distinct solutions.

Modulo nine, if either variable is divisible by three, the form has residue $0,1$ or $-1$. Otherwise choose $s_x,s_y\in\{1,-1\}$ representing $x,y$ modulo three. Then $x^3\equiv s_x$, $y^3\equiv s_y$ and $3xy^2\equiv3s_x\pmod9$. The form is therefore congruent to $s_y-2s_x\in\{-3,-1,1,3\}$. Since $2891\equiv2\pmod9$, no solution exists.''' ,['Diophantine equations','Modular arithmetic','Transformations'])
add(1982,5,'Geometry',4,'Affine coordinates turn both equal division ratios into linear point formulas; a determinant for collinearity reduces to a single quadratic.',r'In regular hexagon $ABCDEF$, points $M\in AC$ and $N\in CE$ satisfy $AM/AC=CN/CE=r$, with $0<r<1$. Determine $r$ when $B,M,N$ are collinear.',r'''Use coordinates $A=(1,0)$, $B=(1/2,\sqrt3/2)$, $C=(-1/2,\sqrt3/2)$ and $E=(-1/2,-\sqrt3/2)$. Then
$$M=(1-3r/2,\sqrt3r/2),\qquad N=(-1/2,\sqrt3(1-2r)/2).$$
The determinant of $M-B$ and $N-B$ equals
$$(1/2-3r/2)(-\sqrt3r)-(\sqrt3(r-1)/2)(-1)=\frac{\sqrt3}{2}(3r^2-1).$$
It vanishes exactly when $r=\pm1/\sqrt3$. The required interior value is $r=1/\sqrt3$, and substituting it verifies collinearity.''',['Coordinates','Collinearity','Polygons'])
add(1982,6,'Geometry',6.5,'Split the path at its first approach to an adjacent corner. A last-covered-point argument on the opposite side, using compactness, produces two nearby points separated by a long excursion.',r'A simple polygonal path with distinct endpoints lies inside a square of side 100. Every boundary point of the square is within $1/2$ of the path. Prove that two path points at Euclidean distance at most one are separated along the path by length at least 198.',r'''Parametrise the path in traversal order. Let $A$ be the first square corner whose closed radius-$1/2$ disk the path reaches. Of its neighbouring corners, label the one reached first $B$ and the other $D$. Let $Z$ be the first path point within $1/2$ of $B$, and split the path at $Z$ into an initial and a final part.

On side $AD$, choose the last point $U$ toward $D$ that is within $1/2$ of the initial part. It exists because this covered set is compact and contains $A$; it is not $D$. Every point just beyond $U$ is therefore covered by the final part. Compactness of that part implies that $U$ also lies within $1/2$ of it.

Choose $X$ on the initial part and $Y$ on the final part with $UX,UY\le1/2$. Then $XY\le1$. Also $UB\ge100$ and $BZ\le1/2$, so $XZ\ge99$ and $YZ\ge99$. The subpath from $X$ to $Y$ passes through $Z$ and has length at least $XZ+ZY\ge198$.''',['Combinatorial geometry','Extremal arguments','Covering','Path length'])
save()
