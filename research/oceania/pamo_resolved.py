resolved={(2008,2),(2006,6),(2012,1),(2016,4),(2016,5),(2017,6),(2022,3),(2021,4)}
ledger[:]=[r for r in ledger if (r['year'],int(r['number'])) not in resolved]
add(2008,2,4.5,'Geometry',['circle equations','tangents','dot products'],r'Let $AB$ be a nondiameter chord of a circle with centre $O$, and let $M$ be its midpoint. A point $T$ lies on the circle with diameter $OM$. The tangent to this smaller circle at $T$ meets the original circle at $P$. Prove $PA^2+PB^2=4PT^2$.',r'''Take $O$ as origin, let the original radius be $R$, and write $M=(m,0)$ and $T=(t,u)$. The smaller circle equation is $t^2+u^2=mt$. Its tangent at $T$ has normal vector $(t-m/2,u)$, so the fact that $P$ lies on it gives
$$P\cdot T-\frac m2P_x=\frac m2t.$$
Consequently
$$PT^2=R^2+mt-2P\cdot T=R^2-mP_x.$$
On the other hand, $A+B=2M$ and $|A|^2=|B|^2=|P|^2=R^2$. Expanding the two squared distances therefore gives
$$PA^2+PB^2=4R^2-2P\cdot(A+B)=4(R^2-mP_x)=4PT^2.$$''','The chord midpoint and small-circle tangent must be encoded together; a dot-product identity then relates three apparently unrelated distances.')
add(2006,6,4.5,'Geometry',['incentres','right triangles','coordinates'],r'Triangle $ABC$ is right-angled at $A$, and $D$ is the foot of its altitude to $BC$. Let $I_1,I_2$ be the incentres of $ADB,ADC$. The circle centred at $A$ of radius $AD$ meets rays $AB,AC$ at $K,L$. Prove that $I_1,I_2,K,L$ are collinear.',r'''Set $A=(0,0),B=(b,0),C=(0,c)$ and $a=\sqrt{b^2+c^2}$. The altitude length is $h=bc/a$, so $K=(h,0),L=(0,h)$ and their line is $x+y=h$.

The altitude foot is $D=(bc^2/a^2,b^2c/a^2)$. In triangle $ADB$, the side lengths opposite $A,D,B$ are respectively $b^2/a,b,h$. The usual incenter formula as a weighted mean of vertices gives
$$I_1=\frac{bD+hB}{b^2/a+b+h}.$$
The sum of its coordinates is
$$\frac{b^2c(b+c)/a^2+b^2c/a}{b(a+b+c)/a}=\frac{bc}{a}=h.$$
Thus $I_1$ lies on $KL$. Interchanging $b,c$ and the two axes gives the identical conclusion for $I_2$.''','Recognizing the target line as x+y equal to the altitude reduces the claim to a carefully weighted incenter computation.')
add(2012,1,4,'Geometry',['power of a point','orthogonal projection','chords'],r'In a circle with centre $O$, let $AB$ be a chord and $T$ a point of segment $OB$. The perpendicular to $OB$ through $T$ meets line $AB$ at $C$ and the circle at $D,E$. Let $S$ be the perpendicular projection of $T$ onto $AB$. Prove $AS\cdot BC=TE\cdot TD$.',r'''Write the radius as $R$, put $O=(0,0),B=(R,0),T=(t,0)$, and let $AB=\ell$. The unit vector from $B$ towards $A$ has horizontal component $-\ell/(2R)$, because $A$ lies on the circle.

Projection onto this unit vector gives $BS=(R-t)\ell/(2R)$ and hence $AS=(R+t)\ell/(2R)$. The point $C$ has horizontal coordinate $t$, so $BC=2R(R-t)/\ell$. Their product is $R^2-t^2$.

The vertical chord through $T$ is bisected at $T$ and has half-length $\sqrt{R^2-t^2}$, so $TE\cdot TD=R^2-t^2$ as well.''','A projection-length relation and the power of the interior point give the same product through different chords.')
add(2016,4,4,'Algebra',['inequalities','cyclic sums','substitution'],r'For positive $x,y,z$ with $xyz=1$, prove that $\displaystyle\frac1{(x+1)^2+y^2+1}+\frac1{(y+1)^2+z^2+1}+\frac1{(z+1)^2+x^2+1}\le\frac12$.',r'''Since $(x-y)^2\ge0$, we have
$$(x+1)^2+y^2+1\ge2(xy+x+1).$$
The corresponding two cyclic inequalities also hold. Now write $x=a/b,y=b/c,z=c/a$ for positive $a,b,c$. Then
$$\frac1{1+x+xy}=\frac{bc}{ab+bc+ca},\quad
\frac1{1+y+yz}=\frac{ca}{ab+bc+ca},\quad
\frac1{1+z+zx}=\frac{ab}{ab+bc+ca}.$$
Their sum is exactly one, which proves the desired bound. Equality in all three initial bounds forces $x=y=z=1$, and this choice attains equality.''','A cyclic denominator estimate must be matched to the exact reciprocal identity supplied by the product-one condition.')
add(2016,5,4,'Geometry',['area bisection','trapezoids','affine coordinates'],r'In convex trapezoid $ABCD$, suppose $AB\parallel CD$ and $AB>CD$. Points $M\in AB,N\in BC$ are such that each of $CM,AN$ bisects the trapezoid area. Prove $MN$ passes through the midpoint of $BD$.',r'''Use coordinates $A=(0,0),B=(b,0),D=(d,h),C=(d+c,h)$ with $b>c>0$. The trapezoid area is $(b+c)h/2$.

Write $M=(m,0)$. The area of triangle $BMC$ is $(b-m)h/2$, and it is half the trapezoid area, so $m=(b-c)/2$. Write $N=B+\lambda(C-B)$. The same condition on triangle $ABN$ gives $b\lambda h/2=(b+c)h/4$, hence $\lambda=(b+c)/(2b)$.

Thus $N-M=\lambda(d+c,h)$. The point on $MN$ at height $h/2$ is
$$M+\frac1{2\lambda}(N-M)=\left(\frac{b+d}{2},\frac h2\right),$$
which is exactly the midpoint of $BD$.''','The two area-bisecting conditions determine distinct affine parameters, which then combine into the diagonal midpoint relation.')
add(2017,6,5,'Geometry',['radical axes','orthocentres','diameter circles'],r'Let $H$ be the orthocentre of triangle $ABC$. The circles with diameter $AC$ and through $A,B,H$ meet again at $K$. Prove that $CK$ meets $BH$ at its midpoint.',r'''Choose $A=(0,0),C=(1,0),B=(u,v)$ with $v\ne0$. Then $H=(u,u(1-u)/v)$. Write the midpoint of $BH$ as $M=(u,w)$, where
$$w=\frac{v^2+u-u^2}{2v}.$$
The circle through $A,B,H$ has equation
$$x^2+y^2+(1-2u)x-2wy=0,$$
as substitution of the three points verifies. The diameter circle has equation $x^2+y^2-x=0$. Subtraction shows that their common chord $AK$ lies on
$$(1-u)x-wy=0.$$
Its direction vector $(w,1-u)$ is perpendicular to $CM$, whose direction vector is $(u-1,w)$. Also, because $K$ lies on the circle with diameter $AC$, $AK\perp CK$. Hence $CK$ and $CM$ are the same line, proving the claim.''','Combining the two circle equations identifies the common chord direction, which must then be connected to both the midpoint and the diameter-angle theorem.')
add(2022,3,4.5,'Algebra',['cyclic products','pairing','fractional transformations'],r'Let positive $a_1,\ldots,a_{2n}$ have product $2$, and extend them periodically. For $1\le k\le2n$, define $\displaystyle A_k=\frac{1+a_k+a_ka_{k+1}+\cdots+a_k\cdots a_{k+n-2}}{1+a_k+a_ka_{k+1}+\cdots+a_k\cdots a_{k+2n-2}}$. If all $A_k$ are distinct, prove that exactly $n$ of them are smaller than $\sqrt2-1$.',r'''Pair index $k$ with $k+n$, working modulo $2n$. Let $U$ be the sum of the $n$ initial partial products beginning at $a_k$, including the empty product one; define $V$ similarly beginning at $a_{k+n}$. Put $P=a_k\cdots a_{k+n-1}$. Splitting each denominator into its first and last $n$ terms gives
$$A_k=\frac{U}{U+PV},\qquad A_{k+n}=\frac{V}{V+(2/P)U}.$$
Writing $t=U/(PV)>0$, these become $t/(1+t)$ and $1/(1+2t)$. The first is smaller than $\sqrt2-1$ precisely when $t<1/\sqrt2$, while the second is smaller precisely when $t>1/\sqrt2$.

The remaining possibility $t=1/\sqrt2$ would make the paired values equal, contrary to the hypothesis. Thus each of the $n$ pairs contributes exactly one value below the threshold.''','The cyclic expressions must be paired halfway around the sequence; splitting their denominators uncovers two complementary fractional transformations.')
add(2021,4,5.5,'Number Theory',['integer fractions','bounding','case analysis'],r'Find all integer pairs $(m,n)$ for which both $\displaystyle\frac{m^2+n}{n^2-m}$ and $\displaystyle\frac{n^2+m}{m^2-n}$ are defined and integers.',r'''The solutions are $(t,-t)$ for every integer $|t|\ge2$, together with
$$(-1,-1),\ (\pm1,0),\ (0,\pm1),\ (1,2),\ (2,1),\ (2,2),\ (2,3),\ (3,2),\ (3,3).$$
The condition is symmetric in $m,n$. First suppose both absolute values are at least two. If $|m|\ge|n|+2$, then
$$|n^2+m|\le n^2+|m|<m^2-|n|\le m^2-n.$$
The second fraction therefore lies strictly between $-1$ and $1$, and must be zero. This gives $m=-n^2$. The first fraction then equals $(n^3+1)/(2n)$, whose integrality forces $n\mid1$, a contradiction. By symmetry the two absolute values differ by at most one.

If $|m|=|n|=t\ge2$, write $m=\varepsilon t,n=\delta t$ with signs $\varepsilon,\delta$. The fractions become $(t+\delta)/(t-\varepsilon)$ and $(t+\varepsilon)/(t-\delta)$. Opposite signs always work; two negative signs never do; two positive signs work only for $t=2,3$.

For absolute values differing by one, symmetry lets us write $m=\varepsilon(t+1),n=\delta t$, $t\ge2$. The second fraction is
$$\frac{t^2+\varepsilon(t+1)}{(t+1)^2-\delta t}.$$
Unless both signs are positive, this is strictly between zero and one. With both positive it is one, and the first fraction is $1+(4t+2)/(t^2-t-1)$. Checking $t=2,3,4,5$, and observing that the extra fraction is between zero and one for $t\ge6$, leaves only $t=2$.

Finally suppose one absolute value is at most one, and by symmetry take $n=0,1,-1$. For $n=0$, integrality of the second fraction $1/m$ gives $m=\pm1$. For $n=1$, the nonzero denominators allow cancellation to $1/(m-1)$, giving $m=0,2$. For $n=-1$, the second fraction is $(m+1)/(m^2+1)$; its only possibilities compatible with the other denominator are $m=-1,0$. Including swaps yields the finite list above. Direct substitution verifies every listed pair.''','Absolute-value bounds reduce infinitely many integer pairs to equal or adjacent magnitudes, after which signs and small exceptional denominators must all be handled.')
