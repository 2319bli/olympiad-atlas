import json,pathlib
p=pathlib.Path('research/asia/reviews.json');r=json.loads(p.read_text());raw=pathlib.Path('research/raw/asia')
def add(k,d,reason,sol=None,**kw):
 r['chn_2021_'+k]={'difficulty':d,'reason':reason,**kw}
 if sol:r['chn_2021_'+k]['solutionOverride']=sol
low={
'0b5291':(2.5,'Two successive conjugate recurrences give multiplication by i and a short periodic calculation.'),
'0d950e':(2.5,'An elementary trigonometric substitution reduces the maximum to AM-GM.'),
'0e568a':(1.5,'Substitute x=1 and x=2, then apply Vieta to the resulting quadratic.'),
'10eebb':(3,'The absolute-value sum equals twice the range; count the three possible extreme pairs.'),
'13a5c8':(1,'Direct enumeration of two three-element sets.'),
'186484':(1.5,'Divide the two geometric-sequence identities to find one plus the ratio.'),
'2228bf':(2,'Taking logarithms cancels the mixed term and gives the desired ratio immediately.'),
'237717':(2,'A brief case split on adjacent vertices, or parity classes, shows that the event is certain.'),
'248190':(2.5,'The two branches of the absolute logarithm determine all needed logarithmic ratios.'),
'2c1d5f':(2.5,'Count nonempty intersection choices and subtract eight forbidden supersets.'),
'37f22b':(1,'Expand one complex product, solve its real-part condition and compute a modulus.'),
'412508':(3,'The sine rule and an angle subtraction determine a tangent; double-angle formulas give the area.'),
'48a00b':(1,'A direct substitution into the arithmetic progression formula.'),
'4a44dc':(2.5,'The absolute-log branches force the requested expression to be constant.'),
'4b6337':(3,'The centroid coordinates and a single three-dimensional distance calculation determine the sine.'),
'854f88':(2,'Treat set coincidences carefully; a quadratic lower bound excludes all but one overlap.'),
'8c05bb':(2.5,'A double-angle identity reduces the hypothesis to two cosine values and two evaluations.'),
'96c04e':(2,'Rewrite as a shifted sine and inspect its range on the given interval.'),
'978de9':(3,'Use period two and reduce three logarithms to their unit intervals.'),
'9b5b06':(1,'Solve two linear equations for the first term and common difference.'),
'a4c6f5':(2,'The line identifies the hyperbola vertex and a substitution gives the eccentricity.'),
'b756ec':(1.5,'Substitute t=2^m, expand the dot product and complete the square.'),
'bbdb1f':(3,'A sign split forces the minimum onto the boundary, where a standard sine-cosine bound applies.'),
'bf8435':(1.5,'Enumerate two short arithmetic collections and sum their intersection.'),
'c23377':(3.5,'Reflect coordinates in y=x+m and compare the resulting parabola coefficients.'),
'c80eaf':(2,'Vieta and the tangent addition formula give the remaining triangle angle.'),
'cd38a1':(1,'Rationalize the complex fraction and solve two linear inequalities.'),
'cdff12':(2,'The vector cosine identity and arithmetic progression condition give one linear ratio.'),
'cee5ec':(3,'Sine-rule elimination gives an angle cosine, then the cosine rule gives one positive quadratic root.'),
'd67357':(2,'Determine f(1),f(2) by substitution and use AM-GM on the resulting reciprocal sum.'),
'd99a22':(3,'Parameterize a parabola point and its tangent; the two focal distances determine the parameters.'),
'df58ee':(2,'Substitute the secant line into the parabola and calculate two triangle areas.'),
'eae290':(2,'Subtract one to turn the recurrence into repeated factorial multiplication.'),
'f08ba9':(1,'Two uses of oddness evaluate the composition.')}
for k,(d,reason) in low.items():add(k,d,reason)
add('1dfd0a',4.5,'Real coefficients constrain the square orientation; Vieta and equal diagonals then determine the roots’ moduli.',r'''The two root pairs have common midpoint $-a/2$ on the real axis. All four roots cannot be real; if both pairs were nonreal, all four would have real part $-a/2$ and be collinear. Thus one pair is real and the other is a conjugate nonreal pair. They form the two diagonals of the square.

Since $b\le0$ would make both discriminants nonnegative, $b>0$. The real pair therefore comes from $z^2+az+b$, and the nonreal pair from $z^2+az+2b$. Each diagonal has length $\sqrt2$, giving
$$a^2-4b=2,\qquad8b-a^2=2.$$
Hence $b=1$ and $a^2=6$. The real roots have the same sign and their absolute values sum to $|a|=\sqrt6$. Each nonreal root has modulus $\sqrt{2b}=\sqrt2$. The required sum is $\boxed{\sqrt6+2\sqrt2}$.''')
ellipse=r'''Write $P=(x,y)$, where $x,y>0$ and $x^2+2y^2=2$. The foci are $F_1=(-1,0)$ and $F_2=(1,0)$. Substituting the line $PF_1$ into the ellipse and applying Vieta to its two intersection ordinates gives
$$y_1=-\frac{y}{3+2x}.$$
Likewise $y_2=-y/(3-2x)$, so
$$y_1-y_2=\frac{4xy}{9-4x^2}.$$
The ellipse equation gives $9-4x^2=x^2/2+9y^2\ge3\sqrt2xy$. Hence $y_1-y_2\le2\sqrt2/3$, with equality when $x^2/2=9y^2$. The point $(x,y)=(3/\sqrt5,1/\sqrt{10})$ meets both conditions and lies in the first quadrant. The maximum is therefore $\boxed{2\sqrt2/3}$.'''
add('450852',5,'Vieta for two focal secants produces a rational expression whose optimal bound uses the ellipse equation.',ellipse)
add('53d162',4.5,'Separating real and imaginary parts reveals a shifted squaring recurrence with doubly exponential exponents.')
add('6f1064',4,'Must distinguish equal arcs within one circle from equal arcs across the two circles, then verify all candidate secants.')
add('772f15',4,'Counts permutations by their last value and the independent swaps of equal-distance pairs.',r'''Fix the last value $a_{21}=k$. The first twenty values must occur in nondecreasing order of their distance from $k$. For each distance represented on both sides of $k$, the two corresponding values may be placed in either order, independently. There are $\min(k-1,21-k)$ such pairs; all other placements are forced. Thus the total is
$$\sum_{k=1}^{21}2^{\min(k-1,21-k)}=2\sum_{j=0}^{9}2^j+2^{10}=\boxed{3070}.$$''',topic='Combinatorics')
add('8d7d03',4,'Combines coprime prime-power allocation with reciprocal pairing to count reduced fractions.')
add('8d836b',6,'First converts two inradii to a difference of secant ordinates, then optimizes that difference using Vieta and AM-GM.',r'''Write $P=(x,y)$ and $Q_i=(x_i,y_i)$. The ellipse has foci $(-1,0),(1,0)$ and focal sum $2\sqrt2$. Because $F_2$ lies on $PQ_2$, the perimeter of $PF_1Q_2$ is $4\sqrt2$; similarly for $PF_2Q_1$. Their areas are respectively $y-y_2$ and $y-y_1$. Therefore
$$r_1-r_2=\frac{y_1-y_2}{2\sqrt2}.$$
Substitute the two focal secants into the ellipse and use Vieta to obtain
$$y_1=-\frac{y}{3+2x},\qquad y_2=-\frac{y}{3-2x}.$$
Thus
$$r_1-r_2=\frac{\sqrt2xy}{9-4x^2}.$$
Since $x^2+2y^2=2$, the denominator equals $x^2/2+9y^2\ge3\sqrt2xy$. The maximum is consequently $\boxed{1/3}$, attained at $P=(3/\sqrt5,1/\sqrt{10})$.''')
add('9df506',5,'The algebraic conditions conceal an isosceles right triangle; a rotation then reduces the maximum to Cauchy-Schwarz.',r'''Let $U=(x,b)$ and $V=(a,y)$. The conditions give $|U|=1$, $|V|=\sqrt2$ and $U\cdot V=1$. Hence $U\cdot(V-U)=0$ and $|V-U|=1$: the vectors $U,V-U$ are perpendicular unit vectors. Since $a\le x$ and $y\ge b$, we must have $V-U=(-b,x)$, so $a=x-b$ and $y=x+b$.

Consequently $x+y=2x+b\le\sqrt5\sqrt{x^2+b^2}=\sqrt5$. Equality occurs at $x=2/\sqrt5$, $b=1/\sqrt5$, $a=1/\sqrt5$, $y=3/\sqrt5$, which satisfies all the original conditions. The maximum is $\boxed{\sqrt5}$.''',topic='Algebra')
add('afa575',4.5,'Combines the piecewise graph with Vieta and root-location conditions; the distinctness and sign restrictions are essential.',r'''For $x\ge0$ the graph is $y=1$; for $x<0$ it is $y=(x+1)/(1-x)$. A horizontal line cannot supply three distinct abscissas summing to zero. Thus write the line as $y=kx+b$ with $k\ne0$.

Its three intersections must consist of two negative roots $u,v$ of
$$kx^2+(b+1-k)x+1-b=0$$
and one positive root $w=(1-b)/k$ on the horizontal branch. Vieta and $u+v+w=0$ give $k=2b$. Since $w>0$, this forces $0<b<1$.

The quadratic is now $2bx^2+(1-b)x+1-b=0$. Its roots are distinct exactly when $(1-b)(1-9b)>0$, so $0<b<1/9$. In this interval their product is positive and their sum negative, hence both are negative, as required. Conversely every such $b$ supplies the three intersections. Therefore the slope range is $\boxed{0<k<2/9}$.''')
add('bba8ea',3.5,'A difference of consecutive three-term sums produces a geometric telescoping sum.',omitReason='The statement only sets a1=a2=a3, whereas the source solution assumes they equal 1. The value of a100 is not uniquely determined as displayed; withheld.')
add('bbc783',4,'A tangent-line discriminant or derivative gives the opposite-branch intersection, followed by a sharp reciprocal bound.',r'''Let $Q=(-a,1/a)$ with $a>0$. The tangent to $y=-1/x$ there is $y=(x+2a)/a^2$ (this follows either by differentiation or by requiring a double intersection). Intersecting it with $y=1/x$ gives the positive solution $x_P=(\sqrt2-1)a$. The horizontal separation of $P,Q$ is $\sqrt2a$, and the slope is $1/a^2$, so
$$|PQ|^2=2a^2(1+a^{-4})=2(a^2+a^{-2})\ge4.$$
Equality holds at $a=1$. Thus the minimum length is $\boxed2$.''')
add('bd790a',5.5,'Vieta converts root separation into a coefficient constraint; optimizing an absolute-value expression requires a sharp boundary case.',r'''Let the common value be $c$. The three points are roots of $X^3+aX^2+bX-c$, so Vieta gives
$$a^2-3b=\tfrac12\big((x_1-x_2)^2+(x_2-x_3)^2+(x_3-x_1)^2\big)\ge3.$$
Put $t=|a|$. If $t\ge\sqrt3$, then $|a|+2|b|\ge\sqrt3$. If $0\le t\le\sqrt3$, then $b\le t^2/3-1\le0$, whence
$$|a|+2|b|\ge t+2-\frac{2t^2}{3}.$$
This concave quadratic is at least the smaller of its endpoint values $2$ and $\sqrt3$. Thus the desired minimum is at least $\sqrt3$.

Take $a=\sqrt3$, $b=0$ and $x_1=-1-1/\sqrt3$, $x_2=-1/\sqrt3$, $x_3=1-1/\sqrt3$. The gaps equal $1$ and direct substitution gives the same cubic value at all three points. Hence the minimum is $\boxed{\sqrt3}$.''')
add('c198eb',6,'A useful three-dimensional parametrization enables different sharp lower and upper perimeter bounds, each with its own equality configuration.')
add('d90250',4.5,'The intended focal-dot-product constraint would lead to a quadratic interval for the eccentricity.',omitReason='Most geometric hypotheses are missing: the statement only specifies an arbitrary ellipse, while the solution relies on points A,B,F,P,Q and an absent dot-product equality. Withheld.')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2));print(len(r))
