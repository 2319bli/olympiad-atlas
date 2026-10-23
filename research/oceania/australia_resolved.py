# Newly completed proof assessments replace explicit pending records.
resolved={(2019,8),(2022,7),(2022,8)}
ledger[:]=[r for r in ledger if (r['year'],int(r['number'])) not in resolved]
add(2019,8,5.5,'Number Theory',['cyclotomic factorization','exponent divisibility','pseudoprimes'],r'For a positive integer $r$, set $n=16^{3^r}-4^{3^r}+1$. Prove that $n$ divides $2^{n-1}-1$.',r'''Put $y=4^{3^r}$, so $n=y^2-y+1$. The factorization
$$(y+1)n=y^3+1=2^{2\cdot3^{r+1}}+1$$
gives $2^{4\cdot3^{r+1}}\equiv1\pmod n$.

It remains to show that this exponent divides $n-1=y(y-1)$. Certainly $4\mid y$. Repeated difference-of-cubes factorization gives
$$4^{3^r}-1=(4-1)\prod_{i=0}^{r-1}\left(16^{3^i}+4^{3^i}+1\right).$$
Every factor displayed is divisible by $3$, so $3^{r+1}\mid y-1$. Hence $4\cdot3^{r+1}\mid n-1$. Raising the earlier congruence to the resulting integer power proves the claim.''','A cyclotomic factorization supplies a usable exponent modulo n; a separate repeated-cubing factorization must show that exponent divides n−1.')
add(2022,7,6,'Number Theory',['iteration','powers of two','minimality','descent'],r'For a positive integer $n$, let $f(n)$ be its distance from the nearest power of $2$, and let $S(n)$ be the number of iterations of $f$ first needed to reach $0$. Find (a) the smallest $n$ with $S(n)=2022$; (b) the largest possible number of consecutive positive integers having the same stopping time.',r'''For (a), the answer is $(2^{4043}+1)/3$. Let $m_k$ be the smallest number of stopping time $k$. We have $m_1=1$. For a positive distance $d$, let $P$ be the smallest power of two at least $2d$. The smallest positive integer whose distance from its nearest power of two is $d$ is $P+d$: in every smaller interval between consecutive powers, the maximum distance is less than $d$, and within the next interval $P+d$ is the first point attaining it. Thus this smallest preimage is an increasing function of $d$.

It follows inductively that
$$m_k=\frac{2^{2k-1}+1}{3}.$$
Indeed, for $d=m_{k-1}$ the power $P$ above is $2^{2k-3}$, so $m_k=P+m_{k-1}$. No smaller preimage can have stopping time $k$, because its image would be at least $m_{k-1}$ and the smallest-preimage function is increasing.

For (b), the answer is three, attained by $5,6,7$, whose images are $1,2,1$. Suppose four consecutive integers of equal stopping time exist, and choose such a block with smallest first term. Its stopping time cannot be one, and the block cannot contain a power of two. It therefore lies strictly between consecutive powers $2^a,2^{a+1}$.

The function $f$ increases by one up to the midpoint $M=3\cdot2^{a-1}$ and decreases by one afterwards. If the block does not straddle this midpoint, its four images are four consecutive smaller positive integers of equal stopping time, contradicting minimality. If it straddles the midpoint, it contains $M$ and a neighbour. For $a\ge3$, their images are $2^{a-1}$ and $2^{a-1}-1$, of stopping times one and two respectively, again impossible. For $a\le2$, the open interval between the two powers contains at most three integers. This exhausts the cases.''','The exact minimum needs a monotone inverse-distance argument; the consecutive-run bound needs a second descent argument with careful treatment of midpoint folds.')
add(2022,8,6.5,'Geometry',['orthocentres','angle bisectors','tangents','coordinates'],r'Let $ABC$ be an acute scalene triangle with orthocentre $H$. The altitudes from $B,C$ meet the internal bisector of $\angle BAC$ at $D,E$, respectively. The tangents at $D,E$ to circle $DEH$ meet at $X$. Prove $BX=CX$.',r'''Put $A=(0,0)$ and use the angle bisector as the horizontal axis. Write
$$B=(uc,us),\quad C=(vc,-vs),\quad c^2+s^2=1,$$
where $u,v>0$, $c,s>0$, and $t=c^2-s^2>0$ because angle $A$ is acute. The stated nondegenerate configuration requires $u\ne v$. The altitude equations are $cx-sy=ut$ and $cx+sy=vt$, giving
$$D=(ut/c,0),\ E=(vt/c,0),\ H=(h,q),$$
where $h=(u+v)t/(2c)$ and $q=(v-u)t/(2s)$.

The centre of circle $DEH$ has form $(h,k)$. Put $d=(v-u)t/(2c)$, the signed half-length of $DE$. Equality of the squared radii to $D$ and $H$ gives
$$d^2+k^2=(q-k)^2,\qquad k=\frac{(v-u)t^2}{4sc^2}.$$
The tangents at the two horizontally symmetric points $D,E$ meet on $x=h$. The tangent equation at $D$ then gives $-k(X_y-k)=d^2+k^2$, so
$$X=(h,-d^2/k)=\left(\frac{(u+v)t}{2c},(u-v)s\right).$$
Finally,
$$2X\cdot(B-C)=(u^2-v^2)(t+2s^2)=u^2-v^2=|B|^2-|C|^2.$$
Expanding $|X-B|^2-|X-C|^2$ now gives zero, proving $BX=CX$.''','The internal bisector supplies symmetric coordinates, but the altitude intersection, circle centre and tangent intersection must all be computed coherently.')
