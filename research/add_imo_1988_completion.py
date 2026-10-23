from international_completion_helpers import add,save
add(1988,1,'Geometry',4.5,'Coordinates at the chord midpoint make the moving point’s second intersection explicit and the squared-distance sum cancel; orthogonal projection identifies the full midpoint locus.',r'Concentric circles have radii $R>r$, and $P$ is fixed on the smaller. A variable line through $P$ cuts the larger circle at $B,C$; its perpendicular through $P$ meets the smaller circle again at $A$, allowing $A=P$ in the tangent case. Find the values of $AB^2+BC^2+CA^2$ and the locus of the midpoint of $BC$.',r'''Let $M$ be the midpoint of $BC$. Use coordinates $M=(0,0)$, $P=(p,0)$, $O=(0,h)$, $B=(t,0)$, $C=(-t,0)$. Then $p^2+h^2=r^2$, $t^2+h^2=R^2$, and the second smaller-circle intersection is $A=(p,2h)$, including $h=0$.

Therefore
$$AB^2+AC^2+BC^2=(p-t)^2+4h^2+(p+t)^2+4h^2+4t^2=6R^2+2r^2.$$
The set of values is this singleton.

Since $OM\perp PM$, the midpoint $M$ lies on the circle with diameter $OP$. Conversely every point of that circle is the perpendicular projection of $O$ onto a line through $P$ and hence is a corresponding chord midpoint. The endpoint $P$ arises from the line through $P$ perpendicular to $OP$, and $O$ from line $OP$. Thus the entire circle is attained.''',['Coordinates','Circles','Locus','Algebraic identities'])
add(1988,2,'Combinatorics',5,'The intersection assumptions force the elements to correspond exactly to edges of a complete graph; the handshake parity obstruction and a cyclic regular subgraph give necessity and sufficiency.',r'Subsets $A_1,\ldots,A_{2n+1}$ of $B$ each contain $2n$ elements, every pair intersects in exactly one element, and every element of $B$ lies in at least two subsets. For which $n$ can the elements be labelled zero or one with exactly $n$ zeros in each $A_i$?',r'''Fix $A_i$. Its $2n$ elements must each belong to another subset, while the $2n$ other subsets each intersect it only once. Thus every element belongs to exactly two subsets, and there is one element for every pair $\{i,j\}$. Regard that element as an edge of the complete graph on $2n+1$ vertices.

Zero-labelled edges would form a graph of degree $n$ at every vertex. Its degree sum $n(2n+1)$ must be even, forcing $n$ even.

Conversely suppose $n$ is even. Number the vertices modulo $2n+1$ and label an edge zero precisely when its cyclic difference is one of $\pm1,\ldots,\pm n/2$. Each vertex then meets exactly $n$ zero edges; label the rest one. Therefore precisely the positive even integers $n$ work.''',['Graph theory','Double counting','Parity','Construction'])
add(1988,3,'Algebra',6,'Recognise and prove binary digit reversal from the recursive formulas, then count binary palindromes with a careful cutoff at 1988.',r'Define $f(1)=1$, $f(3)=3$, $f(2n)=f(n)$, $f(4n+1)=2f(2n+1)-f(n)$, and $f(4n+3)=3f(2n+1)-2f(n)$ for positive integers $n$. How many $n\le1988$ satisfy $f(n)=n$?',r'''Let $R(n)$ be the integer obtained by reversing the binary digits of $n$, discarding leading zeros. Then $R(2n)=R(n)$. If $n$ has $\ell$ binary digits, $R(2n+1)=2^\ell+R(n)$. Consequently
$$R(4n+1)=2^{\ell+1}+R(n)=2R(2n+1)-R(n),$$
$$R(4n+3)=2^{\ell+1}+R(2n+1)=3R(2n+1)-2R(n).$$
Together with $R(1)=1,R(3)=3$, these prove by induction that $f=R$.

The fixed points are therefore exactly the binary palindromes. With $L$ digits their count is $2^{\lceil L/2\rceil-1}$: the first digit is one and the remaining first-half digits determine the rest. For lengths 1 through 10 the counts sum to $1+1+2+2+4+4+8+8+16+16=62$. There are 32 eleven-digit palindromes up to 2047, and exactly two exceed 1988: $2015=(11111011111)_2$ and $2047=(11111111111)_2$. Hence the answer is $62+30=92$.''',['Recurrences','Binary digits','Counting','Induction'])
add(1988,4,'Algebra',5.5,'Monotonicity locates one endpoint in each pole interval; clearing denominators and applying Vieta determines the sum of all interval lengths without solving for the endpoints.',r'Prove that the real solution set of $\sum_{k=1}^{70}k/(x-k)\ge5/4$ is a union of disjoint intervals whose total length is 1988.',r'''Let $F(x)=\sum_{k=1}^{70}k/(x-k)$. On each interval between consecutive poles it is strictly decreasing, with limits $+\infty$ and $-\infty$. On $(70,\infty)$ it decreases from $+\infty$ to zero, and for $x<1$ it is negative. Thus $F(x)=5/4$ has one root $r_k\in(k,k+1)$ for $k<70$ and one $r_{70}>70$. The solution intervals are $(k,r_k]$.

Put $P(x)=\prod_{j=1}^{70}(x-j)$ and $S=1+\cdots+70=2485$. Their endpoints are all 70 roots of
$$Q(x)=\tfrac54P(x)-\sum_{k=1}^{70}k\frac{P(x)}{x-k}.$$
The leading coefficients of $Q$ are $5/4$ and $-(5/4)S-S=-(9/4)S$. Vieta gives $\sum r_k=9S/5$. Therefore the total interval length is $\sum(r_k-k)=4S/5=1988$.''',['Polynomials','Vieta','Monotonicity','Rational inequalities'])
add(1988,5,'Geometry',5,'The incenter coordinate formulas reveal that their joining line cuts equal lengths on the two legs, both equal to the altitude; the area bound then reduces to a²+b²≥2ab.',r'In a triangle $ABC$ right-angled at $A$, let $D$ be the altitude foot on $BC$. The line joining the incenters of $ABD$ and $ACD$ meets $AB,AC$ at $K,L$. Prove $[ABC]\ge2[AKL]$.',r'''Take $A=(0,0)$, $B=(c,0)$, $C=(0,b)$, and write $s=\sqrt{b^2+c^2}$, $h=bc/s=AD$. Then
$$D=(b^2c/s^2,bc^2/s^2),\qquad BD=c^2/s.$$
The incenter $J$ of $ABD$ is the side-length-weighted average
$$J=\frac{hB+cD}{h+c+c^2/s}.$$
Adding its coordinates and simplifying gives $J_x+J_y=h$. Interchanging $b,c$ shows the incenter of $ACD$ also lies on $x+y=h$. Hence their joining line meets the axes at $K=(h,0)$ and $L=(0,h)$.

Thus $[AKL]=h^2/2$ and $[ABC]=bc/2$. The claim is equivalent to
$$bc\ge2h^2=\frac{2b^2c^2}{b^2+c^2},$$
which follows from $b^2+c^2\ge2bc$. Equality holds exactly for $b=c$.''',['Coordinates','Triangle centres','Area','Geometric inequalities'])
add(1988,6,'Number Theory',7.5,'A minimal-solution Vieta jump must preserve integrality and establish a nonnegative second root; the decisive shifted-product positivity argument makes the descent work but requires substantial discovery.',r'If positive integers $a,b$ satisfy $ab+1\mid a^2+b^2$, prove that $(a^2+b^2)/(ab+1)$ is a square.',r'''Set $k=(a^2+b^2)/(ab+1)$. Among positive solutions $A^2+B^2=k(AB+1)$ choose one with the smaller coordinate minimal, and label it $B\le A$.

As a quadratic in $A$, its other root is the integer $C=kB-A$, with $AC=B^2-k$. Hence $C<B$. Also
$$(A+1)(C+1)=AC+A+C+1=B^2+(B-1)k+1>0.$$
Since $A+1>0$, we obtain $C>-1$, so the integer $C\ge0$.

If $C>0$, the pair $(C,B)$ is another positive solution for the same $k$ with a smaller minimum coordinate, a contradiction. Therefore $C=0$, and $AC=B^2-k$ gives $k=B^2$. Thus the original quotient is a perfect square.''',['Vieta jumping','Descent','Diophantine equations','Extremal principle'])
save()
