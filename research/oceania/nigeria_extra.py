add(2019,1,5.5,'Number Theory',['sum of two squares','Wilson theorem','pigeonhole principle','Pythagorean triples'],r'Prove that every prime congruent to $1$ modulo $4$ is the hypotenuse of a right triangle with positive integer side lengths.',r'''Let $p\equiv1\pmod4$. We first prove $p=u^2+v^2$ with positive integers $u,v$.

Pairing each nonzero residue modulo $p$ with its multiplicative inverse proves Wilson's congruence $(p-1)!\equiv-1\pmod p$. Pairing instead $j$ with $p-j$, for $1\le j\le(p-1)/2$, shows that
$$r=\left(\frac{p-1}{2}\right)!\quad\text{satisfies}\quad r^2\equiv-1\pmod p,$$
because $(p-1)/2$ is even.

Put $m=\lfloor\sqrt p\rfloor$. Among the $(m+1)^2>p$ residues $a+rb$ with $0\le a,b\le m$, two coincide. Their differences $u,v$ are not both zero, satisfy $|u|,|v|\le m$, and obey $u+rv\equiv0\pmod p$. Hence $p\mid u^2+v^2$. But
$$0<u^2+v^2\le2m^2<2p,$$
so $u^2+v^2=p$. Neither coordinate is zero, since $p$ is not square; replace each by its absolute value.

Finally,
$$(u^2-v^2)^2+(2uv)^2=(u^2+v^2)^2=p^2.$$
The two legs $|u^2-v^2|$ and $2uv$ are positive integers, since $u=v$ would make the odd prime $p=2u^2$.''','The result requires a substantive sum-of-two-squares lemma; a modular square root of−1 and a lattice-style pigeonhole argument construct it before the Pythagorean identity.')
skip(2019,2,3.5,'Multiply the desired expression by4t²: modulo p² it becomes(2t²−1)². Since p is odd and coprime to t,4t² is invertible, proving the divisibility.')
add(2019,3,4.5,'Geometry',['homothety','tangent circles','composition of transformations'],r'Three circles $\Omega_a,\Omega_b,\Omega_c$ are pairwise externally tangent at $D\in\Omega_a\cap\Omega_b$, $E\in\Omega_b\cap\Omega_c$ and $F\in\Omega_c\cap\Omega_a$. Start with $P\in\Omega_a$ distinct from $D,F$. Extend $PD$ to meet $\Omega_b$ again at $B$, extend $BE$ to meet $\Omega_c$ again at $C$, and extend $CF$ to meet $\Omega_a$ again at $A$. Prove that $PA$ is a diameter of $\Omega_a$.',r'''Let the circle radii be $r_a,r_b,r_c$. The homothety centred at the external tangency point $D$, with ratio $-r_b/r_a$, takes $\Omega_a$ to $\Omega_b$ and therefore takes $P$ to $B$. Similarly, the homotheties centred at $E,F$, with respective ratios $-r_c/r_b$ and $-r_a/r_c$, take $B$ to $C$ and $C$ to $A$.

Their composition has ratio
$$\left(-\frac{r_b}{r_a}\right)\left(-\frac{r_c}{r_b}\right)\left(-\frac{r_a}{r_c}\right)=-1.$$
A composition of homotheties with ratio $-1$ is a half-turn. It takes $\Omega_a$ onto itself, so its centre is the centre of $\Omega_a$. Thus it takes every point to its antipode, and in particular $P,A$ are the endpoints of a diameter.''','Recognizing the three successive chord constructions as negative homotheties turns a complicated-looking diagram into a composition with ratio−1.')
skip(2019,4,3,'The iterated squaring gives f_n(t)=t(t^(2^n−1)−1); n|N implies2^n−1 divides2^N−1, and the difference-of-powers factorization finishes.')
add(2019,5,4,'Algebra',['cyclic inequalities','substitution','sum of squares'],r'''For positive real numbers $a,b,c$ with $abc=1$, prove
$$\frac{1+a+ab}{1+b+ab}+\frac{1+b+bc}{1+c+bc}+\frac{1+c+ca}{1+a+ca}\ge3.$$''',r'''Write $a=x/y,b=y/z,c=z/x$ with positive $x,y,z$. The three numerators become the common symmetric expression $xy+yz+zx$, divided respectively by $yz,zx,xy$. The denominators reduce to $(x+y+z)/z$, $(x+y+z)/x$, $(x+y+z)/y$.

Consequently the original sum equals
$$\frac{xy+yz+zx}{x+y+z}\left(\frac1x+\frac1y+\frac1z\right)
=\frac{(xy+yz+zx)^2}{xyz(x+y+z)}.$$
Set $u=xy,v=yz,w=zx$. The needed bound is $(u+v+w)^2\ge3(uv+vw+wu)$, which follows from
$$u^2+v^2+w^2-uv-vw-wu=\frac12\bigl((u-v)^2+(v-w)^2+(w-u)^2\bigr)\ge0.$$
Equality holds when $x=y=z$, or $a=b=c=1$.''','The product constraint suggests a cyclic ratio substitution; after that the asymmetric fractions unexpectedly combine into one symmetric square.')
skip(2019,6,3,'If a sum of three squares is divisible by4, all three variables are even. Repeatedly divide by4; the remaining value7 modulo8 cannot be a sum of three square residues0,1,4.')
skip(2020,1,None,'The stated quartic t⁴=27(t²+t+1) has only two real roots, contradicting x1<x2<x3<x4. For|t|≤4,27(t²+t+1)−t⁴≥11t²+27t+27>0; on each exterior interval the quartic is strictly monotone and has exactly one root.','withheld-malformed')
add(2020,2,5,'Geometry',['projective geometry','collinearity','Desargues theorem'],r'Let $D$ lie inside triangle $ABC$. Put $E=BD\cap AC$, $F=CD\cap AB$ and $G=EF\cap BC$. Choose $H$ on line $AD$, and set $I=HF\cap BD$, $J=HE\cap CD$. Prove that $G,I,J$ are collinear whenever the named intersections form a nondegenerate configuration.',r'''Apply the converse of Desargues' theorem to triangles $BIF$ and $CJE$, with corresponding vertices $B\leftrightarrow C$, $I\leftrightarrow J$, $F\leftrightarrow E$. The corresponding sides meet at
$$BI\cap CJ=D,\qquad BF\cap CE=A,\qquad IF\cap JE=H.$$
These points are collinear, so the three joining lines $BC,IJ,FE$ concur. The first and third meet at $G$, proving the claim.

Here is a coordinate verification that does not assume the theorem. Use homogeneous barycentric coordinates, rescaled so that
$$A=(1:0:0),\ B=(0:1:0),\ C=(0:0:1),\ D=(1:1:1).$$
Such a rescaling is possible because $D$ is interior and all three barycentric coordinates are nonzero. Then
$$E=(1:0:1),\ F=(1:1:0),\ G=(0:1:-1),\ H=(h:k:k).$$
The equation of $HF$ is $-kX+kY+(h-k)Z=0$, while $BD$ has $X=Z$. Hence $I=(k:2k-h:k)$. Interchanging the last two coordinates gives $J=(k:k:2k-h)$. Their representing vectors differ by a multiple of $(0,1,-1)$, so $G,I,J$ are collinear.''','The construction hides two triangles whose corresponding side intersections lie on AD; finding that correspondence or constructing a suitable homogeneous coordinate system is the main difficulty.')
skip(2020,3,2.5,'Double-count unordered pairs of distinct lines. Each pair lies in exactly one parallel class or meets at exactly one intersection point; each n-fold class/point contributes binomial(n,2).')
add(2020,4,7,'Number Theory',['sum of two squares','primality criteria','Gaussian integer method'],r'For an integer $N\ge2$, prove that $4n(N-n)+1$ is never a perfect square for any integer $1\le n<N$ if and only if $N^2+1$ is prime.',r'''First suppose $N$ is odd. Then $N^2+1$ is composite, and $n=(N-1)/2$ makes $4n(N-n)+1=N^2$, so both sides of the equivalence are false. We may assume $N$ is even.

We use the following elementary lemma: every prime $p\equiv1\pmod4$ has a representation $p=r^2+s^2$ with positive integers $r,s$. To prove it, Wilson's theorem gives a residue $w$ with $w^2\equiv-1\pmod p$: take $w=((p-1)/2)!$. Among the $(m+1)^2>p$ numbers $a+wb$ with $0\le a,b\le m=\lfloor\sqrt p\rfloor$, two are congruent. Their nonzero difference pair has squared norm divisible by $p$, positive and less than $2p$, so the norm is $p$.

Suppose first that $P=N^2+1$ is prime and that some $4n(N-n)+1=b^2$. Put $a=N-2n$. Then
$$a^2+b^2=P,\qquad |a|<N.$$
Modulo $P$, the identity $(Na-b)(Na+b)\equiv-(a^2+b^2)\equiv0$ lets us choose the sign of $b$ so that $P\mid Na+b$. It also follows that $P\mid Nb-a$. The exact identity
$$(Na+b)^2+(Nb-a)^2=P^2$$
therefore forces one of these two multiples of $P$ to be zero and the other to be $\pm P$. Solving gives only $(a,b)=(\pm N,\pm1)$ or $(\pm1,\pm N)$, with the appropriate signs. The first alternatives violate $|a|<N$; the second violate the fact that $a=N-2n$ is even. Thus no such square occurs.

Conversely, suppose $N^2+1$ is composite and let $p$ be its smallest prime factor. Then $p\le\sqrt{N^2+1}<N+1$, so $p\le N$. Since $N^2\equiv-1\pmod p$, the prime $p$ is $1$ modulo4: Fermat's theorem rules out $p\equiv3\pmod4$, and $p$ is odd. By the lemma write $p=r^2+s^2$, choosing positive $r,s$ with their order such that $Nr\equiv-s\pmod p$. This order is available: if $Nr\equiv s$, interchanging $r,s$ changes the sign of the corresponding ratio, because $(s/r)(r/s)=1$ and $(s/r)^2\equiv-1$.

The numbers
$$u=\frac{Nr+s}{p},\qquad v=\frac{r-Ns}{p}$$
are integers and satisfy
$$N=ru-sv,\qquad1=su+rv.$$
Moreover $u>Nr/p\ge r$, so $u\ge2$, while $v<0$. Now put
$$a=ru+sv,\qquad b=rv-su=1-2su.$$
Then $a^2+b^2=(r^2+s^2)(u^2+v^2)=N^2+1$. Also $|b|\ge3$, and $a$ is even, as seen from
$$a=\frac{N(r^2-s^2)+2rs}{p}.$$
We cannot have $a=0$, since $N^2+1$ is not a square; hence $0<|a|<N$. Taking $n=(N-|a|)/2$ gives an integer $1\le n<N$ and
$$4n(N-n)+1=N^2-a^2+1=b^2.$$
This completes both directions.''','This is an upper-band problem: the square condition must be recast as a second sum-of-two-squares representation, and the composite direction needs a constructive factor-conjugation argument plus the prime representation lemma.')
skip(2020,5,2.5,'Apply AM-GM to three copies of(3+2x)/3 and four copies of(4−x)/2, whose sum is11. Equality gives x=6/7 and maximum(33/7)^3(22/7)^4.')
skip(2020,6,2.5,'Since ED is parallel to BC, AE/EB=AD/DC. Ceva in triangleABC forces BF=FC; similarity of the two triangles then makes AG bisectED too.')
