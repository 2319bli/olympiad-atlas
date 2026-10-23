from international_completion_helpers import add,save,coverage
add(1989,1,'Combinatorics',5,'Build a balanced partition of the first 351 integers into triples using two complementary parity ranges, then distribute equal-sum pairs to reach seventeen elements per group.',r'Partition $\{1,\ldots,1989\}$ into 117 disjoint sets of seventeen elements, all having the same sum.',r'''For $1\le i\le117$, define a triple beginning with $i$. If $i\le59$, complete it with $i+175$ and $353-2i$. If $i\ge60$, complete it with $i+58$ and $470-2i$.

Every triple sums to 528. Their first entries cover 1 through 117. Their second entries cover 176 through 234 in the first case and 118 through 175 in the second. Their third entries cover the odd integers 235 through 351 and the even integers 236 through 350. Hence the triples partition 1 through 351.

Pair the remaining integers 352 through 1989 by pairing $j$ with $2341-j$. There are 819 disjoint pairs, each of sum 2341. Give any seven pairs to each of the 117 triples, using every pair once. Every resulting set has $3+14=17$ elements and sum $528+7\cdot2341=16915$, as required.''',['Construction','Partitions','Parity','Magic sums'])
add(1989,2,'Geometry',6,'Arc midpoints bisect the incenter–excenter segments, giving the exact area identity; reflected orthocenters and maximal chord heights then establish the area inequality.',r'In acute triangle $ABC$, the internal angle bisectors meet its circumcircle again at $A_1,B_1,C_1$. Let $A_0,B_0,C_0$ be the corresponding excenters. Prove $[A_0B_0C_0]=2[AC_1BA_1CB_1]\ge4[ABC]$.',r'''Let $I$ be the incenter. The arc-midpoint lemma gives $A_1B=A_1C=A_1I=A_1A_0$; in particular $A_1$ is the midpoint of $IA_0$. One proof uses $\angle IBA_0=\angle ICA_0=90^\circ$, placing $B,C$ on the circle with diameter $IA_0$, whose centre lies on $AA_0$ and on the perpendicular bisector of $BC$, hence at $A_1$ when the two lines are distinct. In the isosceles case the same midpoint identity follows by continuity from non-isosceles triangles.

Therefore $[IBA_0C]=2[IBA_1C]$, and the two cyclic versions also hold. Summing these three area decompositions of the excentral triangle and the hexagon proves the identity.

Let $H$ be the orthocenter, which lies inside $ABC$. Its reflection across $BC$ lies on the circumcircle on the arc $BC$ away from $A$. The arc midpoint $A_1$ maximises the perpendicular distance to $BC$ on that arc. Hence $[BCH]\le[BCA_1]$. Summing the three versions gives
$$[ABC]\le[BCA_1]+[CAB_1]+[ABC_1].$$
The hexagon is the original triangle plus these three exterior caps, so its area is at least $2[ABC]$. The claimed second inequality follows from the identity.''',['Triangle centres','Circles','Area','Reflection','Geometric inequalities'])
add(1989,3,'Combinatorics',5,'Count isosceles triples by their apex and by their base; no three collinear points limits each perpendicular bisector to two possible apexes.',r'A set $S$ of $n$ plane points has no three collinear. From every point, at least $k$ other points are at one common distance. Prove $k<1/2+\sqrt{2n}$.',r'''Count pairs $(P,\{A,B\})$ of distinct points of $S$ with $PA=PB$. For each apex $P$, the hypothesis supplies at least $\binom k2$ such unordered bases, so the count is at least $n\binom k2$.

For each base $\{A,B\}$, possible apexes lie on its perpendicular bisector. At most two points of $S$ lie on that line, since no three are collinear. Thus the count is at most $2\binom n2=n(n-1)$.

Consequently $k(k-1)\le2(n-1)$, or $(k-1/2)^2\le2n-7/4<2n$. Since $k\ge1$, taking square roots proves $k<1/2+\sqrt{2n}$.''',['Double counting','Combinatorial geometry','Isosceles triangles'])
add(1989,5,'Number Theory',4,'A squared factorial makes every term split into two coprime nontrivial factors, which rules out prime powers as well as primes.',r'For each positive integer $n$, prove there are $n$ consecutive positive integers none of which is a positive integral power of a prime.',r'''Set $L=(n+1)!$ and take $L^2+2,L^2+3,\ldots,L^2+n+1$. For each $2\le r\le n+1$, write $L=rs$. Then
$$L^2+r=r(rs^2+1).$$
Both factors exceed one, and $\gcd(r,rs^2+1)=1$. Therefore the product has at least two distinct prime divisors and cannot be a prime power. The displayed list has exactly $n$ consecutive positive terms, proving the claim.''',['Factorials','Coprimality','Primes','Construction'])
add(1989,6,'Combinatorics',5,'Use the first two inclusion–exclusion terms for adjacent complementary pairs; block counting gives an explicit lower bound already exceeding half of all permutations.',r'Among permutations $(x_1,\ldots,x_{2n})$ of $\{1,\ldots,2n\}$, prove more have an adjacent pair with $|x_i-x_{i+1}|=n$ than have none.',r'''Let $E_j$ be the event that $j$ and $j+n$ are adjacent. Treating the pair as a block in either order gives $|E_j|=2(2n-1)!$. For $j\ne k$, treating both pairs as blocks gives $|E_j\cap E_k|=4(2n-2)!$.

The two-term inclusion–exclusion bound gives
$$\left|\bigcup_{j=1}^nE_j\right|\ge2n(2n-1)!-4\binom n2(2n-2)!=2n^2(2n-2)!.$$
This exceeds half of $(2n)!$, because
$$2n^2-n(2n-1)=n>0.$$
Thus the required property holds for a strict majority. The lower bound itself follows pointwise: an object belonging to $r$ events contributes $r-\binom r2\le1$ when $r\ge1$, and zero when $r=0$.''',['Inclusion-exclusion','Counting','Permutations','Bounds'])
add(1989,4,'Geometry',6.5,'Interpret the distance conditions as three externally tangent disks, prove the small disk is confined by the quadrilateral, and maximise its radius inside the gap between two disks and their common tangent.',r'Let $ABCD$ be a convex quadrilateral with $AB=AD+BC$. An interior point $P$ has distance $h$ from the line $CD$ and satisfies $AP=AD+h$ and $BP=BC+h$. Prove $1/\sqrt h\ge1/\sqrt{AD}+1/\sqrt{BC}$.',r'''Write $a=AD$ and $b=BC$. The disks centred at $A$ and $B$ with radii $a,b$ are externally tangent, since $AB=a+b$. The disk centred at $P$ with radius $h$ is externally tangent to both and tangent to the line $CD$.

The open disk at $P$ meets none of the quadrilateral's sides: $AD$ and $BC$ lie in the first two disks, $AB$ is covered by those disks, and $CD$ lies on a tangent line. Because $P$ is inside the quadrilateral, its entire disk is contained in the quadrilateral. All four vertices belong to the convex hull of the first two disks, so the disk at $P$ is contained in that hull as well.

On the side of $AB$ containing $P$, the part of this hull outside the first two disks is the bounded gap between their arcs and their common external tangent $t$. Among disks in this gap tangent to both original disks, choose one of maximum radius $r$. Such a maximum exists by compactness. It must also touch $t$: otherwise increase $r$ slightly and move its centre along the continuous intersection of the circles of radii $a+r,b+r$ about $A,B$, on the same side of $AB$. The strict clearance from $t$ persists, contradicting maximality. The two centres exist continuously for every positive radius because the triangle inequalities are strict.

Let $D_0,C_0$ be the contact points of the original disks with $t$, and let $E$ be the contact point of the maximum disk. The confinement places $E$ between $D_0,C_0$. Applying Pythagoras to each pair of centres gives
$$D_0C_0=2\sqrt{ab},\qquad D_0E=2\sqrt{ar},\qquad EC_0=2\sqrt{br}.$$
Thus $\sqrt{ab}=\sqrt r(\sqrt a+\sqrt b)$, so $r=ab/(\sqrt a+\sqrt b)^2$. Since $h\le r$, taking reciprocal square roots proves the claimed inequality.''',['Circles','Tangency','Extremal principle','Geometric inequalities'])
coverage['deferred']=[d for d in coverage['deferred'] if d['id']!='imo_1989_official_p4']
save()
