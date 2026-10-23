import json,pathlib
p=pathlib.Path('research/asia/reviews.json');r=json.loads(p.read_text())
def add(k,d,reason,sol=None,**kw):
 r['chn_2012_'+k]={'difficulty':d,'reason':reason,**kw}
 if sol:r['chn_2012_'+k]['solutionOverride']=sol
add('18fed6',4,'Interprets each company’s network as a forest, obtains a global edge bound, and constructs a sharp two-path example.',r'''Color each edge of the complete graph by its airline. The hypothesis says that neither color contains a cycle, so each color forms a forest and has at most $n-1$ edges. Therefore
$$\binom n2\le2(n-1),$$
which gives $n\le4$.

For four cities numbered $1,2,3,4$, give one airline the edges $12,23,34$ and the other the edges $13,14,24$. Each color is a path and has no cycle. Thus every round trip using at least three distinct cities uses both colors. The maximum is $\boxed4$.''',topic='Combinatorics')
add('44159d',4.5,'Reduces the universal divisibility to a prime modulus and applies Fermat to classify whether neither or one variable vanishes.',r'''The pairs are exactly those for which $a,b$ have opposite parity, or $a\equiv b\equiv1\pmod3$.

Indeed, let $p$ be a prime factor of a permissible $d$. If both $a,b$ vanish modulo $p$, the condition fails. If exactly one vanishes, use $n=p-1$: Fermat gives $2\equiv0\pmod p$, so $p=2$ and $a,b$ have opposite parity. If neither vanishes, the same exponent gives $3\equiv0\pmod p$, so $p=3$. The case $n=1$ then gives $a+b\equiv2\pmod3$; since both are nonzero residues, each must be $1$.

Conversely, opposite parity makes $a^n+b^n+1$ even for every positive $n$, and $a\equiv b\equiv1\pmod3$ makes it divisible by $3$ for every $n$.''')
add('4d98f1',3,'Separate sign comparisons of the two root differences locate the first possible integer immediately.')
add('5c8b00',4,'The task is a construction: a purposeful search among triangular numbers gives three successive block sums in ratio ten.',r'''One suitable triple is $\boxed{(l,m,n)=(3,11,36)}$. Indeed,
$$\sum_{k=1}^3k=6,\qquad\sum_{k=4}^{11}k=66-6=60,\qquad\sum_{k=12}^{36}k=666-66=600.$$
These positive sums have common ratio $10$, and $1<3<11<36$.''')
add('6eee7c',4.5,'Coordinates on the altitude turn the perpendicular-bisector condition into exactly the required circle equation.',r'''Choose $D=(0,0)$, $A=(0,a)$ and let $BC$ be the horizontal axis. Write $O=(u,v)$ and $H=(0,h)$. The standard orthocenter relation in these coordinates is $h=a-2v$; it also follows by equating circumcenter distances and writing the altitude from $B$.

Let $E=(e,0)$. Since $EA=EO$, we have
$$2eu=u^2+v^2-a^2.$$
The circle through $A,D,E$ has equation $x^2+y^2-ex-ay=0$. The midpoint $N$ of $OH$ is $(u/2,(a-v)/2)$. Substituting its coordinates into the circle equation gives
$$\frac14\big(u^2+v^2-a^2-2eu\big)=0.$$
Hence $N$ lies on the required circle. The noncollinearity assumption ensures $u\ne0$, so the construction is nondegenerate.''')
add('71f280',6,'Double-counts asymmetric pairs across all reflection axes, refines the average using parity, and shows how one swap repairs the resulting axis.',r'''Let $b\le6$ be the number of stones of the less frequent color, called black. For each of the $13$ reflection axes, let $t$ count reflected pairs of opposite colors. Every black-white pair is paired by exactly one reflection, so the sum of these thirteen values is $b(13-b)$.

If the fixed vertex of an axis is black, then $t\equiv b-1\pmod2$; otherwise $t\equiv b\pmod2$. Suppose every $t$ were at least $3$. If $b$ is odd, the $b$ axes through black vertices have $t\ge4$, so the sum is at least $39+b>b(13-b)$ for $b=1,3,5$. If $b$ is even, the other $13-b$ axes have $t\ge4$, giving sum at least $52-b>b(13-b)$ for $b=0,2,4,6$. Both are impossible. Thus some axis has $t\le2$.

If $t=2$, exchange a black stone in one mismatched pair with a white stone in the other; both pairs become matched. If $t=1$, exchange the fixed-vertex stone with the opposite-colored stone in the mismatched pair. If $t=0$, exchange two stones of the same color. In every case one exchange produces symmetry about this axis.''',topic='Combinatorics')
add('8ed82f',7,'Combines prime-modulus binomial coefficients with a precise count of binary carries for divisibility by four.',r'''Since $2012=4\cdot503$ and $503$ is prime, first count indices for which $4$ divides the binomial coefficient. The binary expansion of $2012$ is $11111011100$, with eight $1$ bits. The standard factorial valuation formula gives
$$v_2\binom Nk=s_2(k)+s_2(N-k)-s_2(N),$$
equivalently the number of carries when adding $k$ and $N-k$ in base two.

There are $2^8=256$ indices with no carry. For exactly one carry, it must start at a zero bit followed immediately by a one bit. In this expansion the only possibilities are positions $1$ and $5$ (positions start at zero). The initiating bit of $k$ is $1$, the next bit is $0$, and the other seven one-bit positions are free. Each position gives $2^7=128$ choices. Thus exactly $512$ coefficients fail divisibility by $4$, leaving $2013-512=1501$ divisible by $4$.

Modulo $503$, the identity $(1+X)^{2012}\equiv(1+X^{503})^4$ shows that only the five indices $0,503,1006,1509,2012$ fail divisibility by $503$. The endpoints are already excluded by the factor $4$ condition. For the other three indices, the binary valuation formula gives respectively $7,8,7$, so all three must be removed from the count $1501$. Therefore the answer is $\boxed{1498}$.''',topic='Number Theory')
add('8fb70f',5.5,'Two carefully arranged cotangent identities relate the given altitude length to the requested angle.')
add('98c085',5,'Represents a laminar family as a rooted inclusion tree and bounds its internal nodes by its singleton leaves.',r'''We may enlarge the family by adding $E$ and every singleton, preserving its property. Arrange the sets as a rooted inclusion tree with root $E$, each set joined to its smallest strict superset in the family. Its leaves are exactly the $n$ singletons. Every nonleaf has at least two children: maximal proper submembers are disjoint and cover the parent, since all singleton subsets are present.

If there are $I$ internal nodes and $n$ leaves, the tree has $I+n-1$ edges but at least $2I$ edges, so $I\le n-1$. Hence $k\le2n-1$.

Equality is attained by all $n$ singletons together with the $n-1$ sets $\{1,2\},\{1,2,3\},\ldots,\{1,\ldots,n\}$ after labeling $E$. Thus the maximum is $\boxed{2n-1}$.''',topic='Combinatorics')
add('993c53',4,'Chooses a residue and exponent simultaneously so Fermat turns the two terms into 1 and −1.',r'''The answer is every odd prime. For $p=2$, if $n$ is even the second summand is odd and the first even; if $n$ is odd the reverse holds. Thus the sum is never divisible by $2$.

For an odd prime $p$, take
$$n=p-2+t\,p(p-1),\qquad t=0,1,2,\ldots.$$
Then $n\equiv-2\pmod p$, $n+1\equiv-1\pmod p$, $p-1\mid n+1$, and $n$ is odd. Fermat therefore gives
$$n^{n+1}+(n+1)^n\equiv(-2)^{n+1}+(-1)^n\equiv1-1=0\pmod p.$$
These are infinitely many positive integers $n$.''')
add('99ff6c',5,'A reciprocal substitution turns the nonlinear growth into a nearly unit descent, allowing two sharp crossing bounds.',r'''Set $b_n=2012/a_n$. The recurrence becomes
$$b_{n+1}=b_n-1+\frac1{b_n+1},\qquad b_0=4024.$$
Thus $b_n$ strictly decreases and each decrease is less than $1$. In particular $b_{2012}>4024-2012=2012$, so $a_{2012}<1$.

Suppose $b_{2013}\ge2012$. Then $b_i\ge2012$ for $0\le i\le2012$, with strict inequality for earlier indices. Summing the recurrence gives
$$b_{2013}=4024-2013+\sum_{i=0}^{2012}\frac1{b_i+1}<2011+\frac{2013}{2013}=2012,$$
a contradiction. Hence $a_{2013}>1$. Monotonicity now gives the unique answer $\boxed{k=2012}$.''')
add('a05f33',2,'As displayed, the exponentially negative difference prevents any fixed m from working.',omitReason='For unbounded primes p, 9^p−29^p tends to negative infinity, so no fixed m can satisfy the displayed inequality. The source record has no solution and likely lost exponent/divisibility notation; withheld.')
add('a30f60',6,'A cleverly weighted combination of three evaluations bounds the objective, and global nonpositivity determines the unique remaining coefficient.',r'''Evaluate at $0,\pi,\pi/3$. Their weighted combination gives
$$a+b-c+d=f(0)+\tfrac23f(\pi)+\tfrac43f(\pi/3)\le3.$$
Equality requires all three evaluations to equal $1$. Solving these linear equations yields $a=1$, $c=-1$ and $b+d=1$.

Write $t=\cos x$. For these values,
$$f(x)-1=-2(1-t^2)\big(4dt^2-2t+1-d\big).$$
Thus the quadratic in parentheses must be nonnegative on $(-1,1)$. At $t=1/2$ it is zero, so its derivative there must vanish: $4d-2=0$. Hence $d=b=1/2$. Conversely with these values the quadratic is $2(t-1/2)^2$, which is nonnegative. Therefore the unique maximizing quadruple is
$$\boxed{(a,b,c,d)=(1,1/2,-1,1/2)},$$
and the maximum objective value is $3$.''')
add('a41233',4.5,'Pairs multiples of six by a digitwise complement, forcing exactly one digit sum in each pair to be divisible by six.')
add('b348db',3.5,'Parity forces n even, and reduction modulo three identifies the third-smallest divisor and the full family.')
add('b4de15',6.5,'A recursive parity argument separates paths according to visits to the central vertex and pairs repeated visits by reflection.',r'''The answer is $\boxed{10}$. If $m\ge11$, the path contains vertices $1$ and $2013$, and exactly one $2012$-step walk joins them: every step moves right. Thus larger $m$ fail.

We prove by induction that on a path with $2^m-1$ vertices every walk count of length $k\ge2^m-1$ is even. The case $m=1$ is immediate. In the induction step let $c=2^{m-1}$ be the central vertex and $L=c-1$ the number of vertices on either side.

Walks that never visit $c$ are counted evenly by induction. For walks that visit $c$ exactly once, fix the visit time and the adjacent vertices. The segments before and after the visit have total length $k-2\ge2L-1$, so at least one has length at least $L$ and is counted evenly by induction. If the sole visit is an endpoint, the remaining segment has length $k-1\ge L$.

Finally pair every walk visiting $c$ at least twice with the walk obtained by reflecting the segment between its first two visits across $c$. This is an involution without fixed walks. Hence these are counted evenly too.

For $m=10$, $2012\ge1023=2^{10}-1$, so the claim applies and completes the proof.''',topic='Combinatorics')
add('bd05d8',3,'Writing each term as a difference of consecutive products makes the inequality telescope immediately.')
add('c41503',6,'Assuming distinct distances from each selected vertex gives a rigid squared-distance sum; a vector identity would place three circle points on a line.',r'''Scale the circumcircle to unit radius and represent its vertices by vectors. Put $N=2n-1$. From any vertex of the regular $N$-gon there are exactly $n-1$ possible positive distances, each represented by two vertices.

Suppose the selected set $S$ of $n$ vertices contains no isosceles triangle. From each selected vertex $P$, the other $n-1$ selected vertices must then realize all these distances exactly once. The sum of squared distances from $P$ to all $N$ polygon vertices is $2N$, because their vector sum is zero. Therefore
$$\sum_{Q\in S}|P-Q|^2=N.$$
Let $Z=\sum_{Q\in S}Q$. Since all selected vectors have length $1$, the left side is $2n-2P\cdot Z$. As $N=2n-1$, this gives $P\cdot Z=1/2$ for every selected vertex. Thus $Z\ne0$ and all selected vertices lie on one line. A line meets the unit circle in at most two points, contradicting $n\ge3$.''',topic='Geometry')
add('e47881',4,'A first-crossing argument combines integrality with the nondecreasing denominators.',r'''Because $r=(k+1)a_r$, there is an index with $s\ge k a_s$. Let $s$ be the least such positive index. If $s=1$, then $1\ge k a_1\ge1$, giving equality. If $s>1$, minimality and integrality imply
$$s-1<k a_{s-1}\quad\Longrightarrow\quad s\le k a_{s-1}\le k a_s\le s,$$
where the middle inequality uses monotonicity. Every inequality is therefore an equality, so $s/a_s=k$.''')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2));print(len(r))
