from international_completion_helpers import add,save
add(1985,1,'Geometry',5,'Express the tangent lengths and centre distances using the angles at the endpoints of the diameter-side; cyclicity supplies supplementary angles and a half-angle identity completes the length equality.',r'A circle has centre on side $AB$ of cyclic quadrilateral $ABCD$ and touches each of $BC,CD,DA$. Prove $AD+BC=AB$.',r'''Let the circle have centre $O$, radius $r$, and contacts $L\in AD$, $M\in CD$, $N\in BC$. Write $\angle A=\alpha$ and $\angle B=\beta$. The right triangles at the tangencies give $AL=r\cot\alpha$, $BN=r\cot\beta$, $AO=r\csc\alpha$, and $BO=r\csc\beta$.

Cyclicity gives $\angle C=\pi-\alpha$ and $\angle D=\pi-\beta$. Since a circle's centre lies on the angle bisector between its two tangents, the other tangent lengths are
$$CN=CM=r\cot(\angle C/2)=r\tan(\alpha/2),$$
$$DL=DM=r\tan(\beta/2).$$
Using $\cot t+\tan(t/2)=\csc t$, we obtain
$$AD+BC=(AL+LD)+(BN+NC)=r(\csc\alpha+\csc\beta)=AO+OB=AB.$$''',['Tangency','Cyclic quadrilaterals','Trigonometry'])
add(1985,2,'Number Theory',4.5,'The two colour invariances combine into invariance under adding k modulo n; coprimality makes the nonzero multiples of k visit every required residue.',r'Let $1\le k<n$ with $\gcd(k,n)=1$. Colour $1,\ldots,n-1$ with two colours so that $i,n-i$ always agree and, for $i\ne k$, $i,|i-k|$ agree. Prove all numbers have the same colour.',r'''Let $r_j$ be the least positive residue of $jk$ modulo $n$, for $1\le j\le n-1$. Coprimality makes these a permutation of $1,\ldots,n-1$.

For $1\le j\le n-2$, put $r=r_j,s=r_{j+1}$. If $s=r+k<n$, then $s$ and $s-k=r$ have the same colour. If $s=r+k-n$, then $n-r=k-s>0$. The first rule equates the colours of $r$ and $n-r$; the second equates those of $s$ and $k-s=n-r$. Thus consecutive residues $r_j,r_{j+1}$ always agree. The entire permutation, and hence every number, has one colour.''',['Modular arithmetic','Coprimality','Colouring'])
add(1985,3,'Algebra',6.5,'Work modulo two and split the exponents at their largest binary place; disjoint coefficient blocks double the weight in one case, while the Hamming-weight triangle inequality handles cancellation in the other.',r'Let $w(P)$ count the odd coefficients of an integer polynomial $P$, and put $Q_i=(1+x)^i$. For $0\le i_1<\cdots<i_n$, prove $w(Q_{i_1}+\cdots+Q_{i_n})\ge w(Q_{i_1})$.',r'''Reduce coefficients modulo two, so $w$ counts nonzero coefficients. For a power of two $h$, repeated squaring gives $(1+x)^h=1+x^h$. Induct on the largest exponent, with exponent zero immediate.

Let $h$ be its largest power-of-two place. If $i_1\ge h$, factor the sum as $(1+x)^hB$ with $\deg B<h$. Its coefficient blocks are $B$ and $x^hB$, so its weight is $2w(B)$. The induction hypothesis gives $w(B)\ge w((1+x)^{i_1-h})$, and the same disjoint-block identity doubles that last weight to $w(Q_{i_1})$.

If $i_1<h$, split the terms into $A+(1+x)^hB$, where $A$ collects exponents below $h$ and $\deg A,\deg B<h$. The weight is $w(A+B)+w(B)$. Coefficientwise, every nonzero coefficient of $A$ must occur in at least one of $A+B,B$, hence this sum is at least $w(A)$. Induction gives $w(A)\ge w(Q_{i_1})$. Both cases prove the claim.''',['Polynomials','Binary digits','Induction','Parity'])
add(1985,4,'Number Theory',5.5,'Apply pigeonhole twice to parity vectors of nine prime exponents: first create many disjoint pairs with square products, then pair their square roots to obtain a fourth power.',r'A set contains 1985 distinct positive integers, with no prime divisor greater than 26. Prove that four distinct members have product equal to an integer fourth power.',r'''Only the nine primes $2,3,5,7,11,13,17,19,23$ can occur. Assign each integer the nine-bit vector of its prime-exponent parities. There are $2^9=512$ vectors, so any 513 available integers contain a pair whose product is a square.

Choose 513 disjoint such pairs successively. This is possible: even after 512 pairs have been removed, $1985-1024=961>512$ integers remain. Write the pair products as $b_1^2,\ldots,b_{513}^2$.

Apply the same parity-vector pigeonhole argument to the 513 integers $b_i$. Two, say $b_i,b_j$, have product $c^2$. The four original integers in those two disjoint pairs then have product $b_i^2b_j^2=c^4$. Their distinctness is guaranteed by the disjoint pairing.''' ,['Pigeonhole principle','Prime exponents','Squares','Parity'])
add(1985,5,'Geometry',5.5,'Write the two circles through B as quadratic equations with zero constant term; the centre of the third circle is the average of their linear coefficient vectors, making the desired dot product vanish.',r'A circle with centre $O$ meets sides $AB,BC$ of triangle $ABC$ at $A,K$ and $C,N$, respectively, with $K,N$ distinct interior points. The circumcircles of $ABC$ and $KBN$ meet at $B$ and a distinct point $M$. Prove $OM\perp BM$.',r'''Take $B$ as vector origin, and let unit vectors $u,v$ point toward $A,C$. Write $A=au$, $K=ku$, $C=cv$, $N=nv$. The two circumcircles through the origin have equations
$$|x|^2-l\cdot x=0,\qquad |x|^2-h\cdot x=0,$$
where $l\cdot u=a,l\cdot v=c$ and $h\cdot u=k,h\cdot v=n$.

The circle through $A,K,C,N$ has equation $|x|^2-2o\cdot x+t=0$, where $o$ represents $O$. Restricting to the line in direction $u$ gives a quadratic with roots $a,k$, so $2o\cdot u=a+k$. Likewise $2o\cdot v=c+n$. Since $u,v$ are linearly independent, $2o=l+h$.

At the second intersection $m$, both circle equations give $l\cdot m=h\cdot m=|m|^2$. Therefore $(o-m)\cdot m=0$. These are the vectors $MO$ and $BM$, so the required perpendicularity follows.''',['Coordinates','Circles','Dot products','Power of a point'])
add(1985,6,'Algebra',7,'Define nested intervals of initial values using increasing polynomial iterates; strict endpoint nesting proves existence, while convexity squeezes their widths to zero and proves uniqueness.',r'For a real initial value $x_1$, define $x_{n+1}=x_n(x_n+1/n)$. Prove that exactly one initial value produces $0<x_n<x_{n+1}<1$ for every $n\ge1$.',r'''Let $F_n(t)$ be the $n$th term starting at $t$. Each $F_n$ is a strictly increasing polynomial on $[0,\infty)$ with nonnegative coefficients and $F_n(0)=0$. Define $a_n,b_n$ by $F_n(a_n)=1-1/n$ and $F_n(b_n)=1$; thus $a_1=0,b_1=1$.

The recurrence gives $F_{n+1}(a_n)=1-1/n<1-1/(n+1)$ and $F_{n+1}(b_n)=1+1/n>1$. Hence $a_n<a_{n+1}<b_{n+1}<b_n$. The nested closed intervals have a common point $t$, which lies strictly between every pair of endpoints. Therefore $1-1/n<F_n(t)<1$, giving positivity and $F_{n+1}(t)>F_n(t)$.

For uniqueness, convexity and $F_n(0)=0$ imply
$$1-1/n=F_n(a_n)\le\frac{a_n}{b_n}F_n(b_n)=\frac{a_n}{b_n}.$$
Thus $b_n-a_n\le b_n/n\le1/n$, so their common intersection is a single point. Conversely any initial value satisfying the requested inequalities must have $x_n>1-1/n$, hence belong to every interval. This proves exactly one exists.''',['Recurrences','Continuity','Convexity','Nested intervals'])
save()
