from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');raw=p/'international-raw';r=json.loads((p/'international-reviews.json').read_text())
def add(year,num,topic,rating,reason,statement,solution='',tags=None,solution_url=None,note=None):
 slug=f'imo_{year}_official_p{num}'
 d={'id':slug,'competition_code':'IMO','competition':'IMO','year':year,'problem_number':str(num),'primary_domain':topic,'topics':[[topic,t] for t in (tags or [])],'problem_markdown':statement,'solutions_markdown':[solution],'officialSourceUrl':f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf','officialSolutionUrl':solution_url or f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf','reviewNote':note or 'Official released statement checked; worked exposition independently written and mathematically assessed.'}
 (raw/(slug+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2));r[slug]=[rating,reason]
add(1971,1,'Algebra',5,'Order the variables and pair the alternating-sign terms for the two valid sizes. Repeated variables then isolate a single negative term to build counterexamples for all other sizes.',r'''For $n>2$, let $E_n=\sum_{i=1}^n\prod_{j\ne i}(a_i-a_j)$. Prove that $E_n\geq0$ for every real tuple $(a_1,\ldots,a_n)$ exactly when $n=3$ or $5$.''',r'''For $n=3$ or $5$, reorder so $a_1\geq a_2\geq\cdots\geq a_n$. Denote the summands by $T_i$.

The first two satisfy
$$T_1+T_2=(a_1-a_2)\left(\prod_{j=3}^n(a_1-a_j)-\prod_{j=3}^n(a_2-a_j)\right)\geq0,$$
since corresponding factors are nonnegative and those in the first product are larger. For $n=3$, the remaining summand is also nonnegative.

For $n=5$, the middle term $T_3$ has two nonpositive and two nonnegative factors, hence is nonnegative. At the lower end,
$$T_4+T_5=(a_4-a_5)\left(\prod_{j=1}^3(a_j-a_5)-\prod_{j=1}^3(a_j-a_4)\right)\geq0.$$
Thus both asserted sizes work, including repeated-variable cases.

For even $n$, take $a_1=-1$ and all other entries zero. Only $T_1$ survives, and it equals $-1$. For odd $n\geq7$, take one entry zero, three entries $-1$, and the remaining $n-4$ entries $1$. Every repeated-entry term vanishes. The zero entry contributes $1^3(-1)^{n-4}=-1$. These counterexamples exclude every other $n>2$.''',['Symmetric expressions','Ordering','Counterexamples'],solution_url='https://prase.cz/kalva/imo/isoln/isoln711.html')
add(1971,2,'Geometry',4,'All nine translates fit inside one doubled copy by convexity. Their total volume exceeds that container’s volume, forcing interior overlap.',r'''A convex polyhedron $P$ has nine vertices $A_1,\ldots,A_9$. For each $i$, translate $P$ by the vector $\overrightarrow{A_1A_i}$ to obtain $P_i$ (so $P_1=P$). Prove that two of these polyhedra have a common interior point.''',r'''Take $A_1$ as the origin. A point of $P_i$ has the form $x+A_i$ with $x\in P$. By convexity, $(x+A_i)/2\in P$. Hence every $P_i$ lies in the dilation $2P$.

Let $V>0$ be the volume of $P$. The nine translates each have volume $V$, whereas $2P$ has volume $8V$. If their interiors were pairwise disjoint, their union would have volume $9V$: boundaries of polyhedra have zero volume. But that union is contained in $2P$, a contradiction. Thus some pair has an interior point in common.''',['Convexity','Volume','Packing'])
add(1971,3,'Number theory',4.5,'Use induction on a selected finite set and choose the next exponent so the new term is minus one modulo the product of all previous terms.',r'Prove that the numbers $2^k-3$, for integers $k\geq2$, contain an infinite subset whose distinct members are pairwise coprime.',r'''Start with $2^3-3=5$. Suppose distinct pairwise coprime terms $b_1,\ldots,b_s$ have been chosen, and let $M=b_1\cdots b_s$. All these numbers are odd, so $\gcd(2,M)=1$. Euler's theorem gives $2^{\varphi(M)}\equiv1\pmod M$.

Choose an integer $t$ sufficiently large that $k=1+t\varphi(M)$ exceeds every previously used exponent. Then
$$2^k-3\equiv2-3\equiv-1\pmod M.$$
Thus the new term is coprime to $M$, and therefore to every previous term. It is also larger than all of them. Repeating this finite extension indefinitely constructs the desired infinite subset.''',['Coprimality','Euler’s theorem','Inductive construction'])
add(1971,4,'Geometry',7.5,'Unfolding four faces converts the path to a moving-endpoint straight segment, but the holonomy condition and boundary nonattainment require a substantial spatial optimisation argument. Above the target band.',r'''All faces of tetrahedron $ABCD$ are acute. Consider closed paths $XYZTX$ with $X,Y,Z,T$ strictly inside edges $AB,BC,CD,DA$, respectively. Prove that no shortest path exists if $\angle DAB+\angle BCD\ne\angle CDA+\angle ABC$. If equality holds, prove that infinitely many shortest paths exist and have length $2AC\sin(\alpha/2)$, where $\alpha=\angle BAC+\angle CAD+\angle DAB$.''',solution_url='https://prase.cz/kalva/imo/isoln/isoln714.html',note='Official statement and the complete unfolding/boundary argument in the authored Scholes solution were read for assessment; excluded as above the target difficulty band.')
add(1971,5,'Combinatorics',5,'Build the desired unit-distance graph inductively by adjoining a translated copy. The key is proving that a generic unit translation creates only the intended new neighbour for each point.',r'For every positive integer $m$, prove that there is a finite set of points in the plane such that each point has exactly $m$ other points at distance one.',r'''We induct on $m$, beginning with a one-point set for $m=0$. Suppose a finite set $S$ has exactly $m$ unit-distance neighbours at each point.

Choose a unit vector $v$ and consider $S\cup(S+v)$. Each $a\in S$ acquires the intended neighbour $a+v$. We choose $v$ to prevent any coincidence or additional unit distance between the two copies.

There are only finitely many forbidden choices. A coincidence $a=b+v$ fixes $v=a-b$. For distinct $a,b\in S$, an unwanted cross distance requires $|a-b-v|=1$ with $|v|=1$. Squaring gives the line equation
$$2(a-b)\cdot v=|a-b|^2.$$
That line meets the unit circle in at most two points. Thus all such restrictions exclude only finitely many unit vectors, while infinitely many remain available.

For an allowed choice, the copies are disjoint, all original unit distances are retained within them, and the only cross unit distances are the matched pairs $a,a+v$. Every point therefore has exactly $m+1$ unit-distance neighbours. Induction proves the assertion for all $m$.''',['Unit distances','Induction','Generic construction'])
add(1971,6,'Combinatorics',4.5,'Choose the smallest row or column sum. Its zero positions force large sums in the perpendicular direction, while integrality bounds how many nonzero positions it can have.',r'''An $n\times n$ matrix has nonnegative integer entries. Whenever an entry is zero, the sum of its row and the sum of its column together are at least $n$. Prove the total of all entries is at least $n^2/2$.''',r'''Let $x$ be the smallest of all row and column sums. If $x\geq n/2$, summing the rows proves the result. Otherwise, transpose if necessary so that a row has sum $x<n/2$.

Let $y$ be the number of nonzero entries in that row. Since each is an integer at least one, $y\leq x<n/2$. The $y$ columns through those entries have sums at least $x$ by minimality. The other $n-y$ columns pass through zero entries, so their sums are at least $n-x$ by the hypothesis.

The total $T$ therefore satisfies
$$T\geq xy+(n-y)(n-x)=\frac{n^2}{2}+\frac{(n-2x)(n-2y)}2>\frac{n^2}{2}.$$
This completes both cases.''',['Extremal principle','Matrices','Counting'],solution_url='https://prase.cz/kalva/imo/isoln/isoln716.html')
add(1972,1,'Combinatorics',3.5,'There are 1024 subsets but at most 991 possible sums. Equal-sum subsets become disjoint by removing their intersection.',r'Among ten distinct two-digit positive integers, prove that two disjoint nonempty subsets have equal sums.')
add(1972,2,'Geometry',6.5,'Construct a four-piece cyclic dissection with one isosceles trapezoid, then subdivide that piece arbitrarily. The delicate step is proving the four rays meet the intended sides rather than their extensions.',r'For every integer $n\geq4$, prove that any convex cyclic quadrilateral can be dissected into $n$ convex cyclic quadrilaterals.',r'''We first dissect the quadrilateral into four cyclic quadrilaterals, one an isosceles trapezoid. Subdividing that trapezoid by lines parallel to its bases into $n-3$ smaller isosceles trapezoids then gives exactly $n$ pieces.

Write the consecutive angles of $ABCD$ as $\alpha,\beta,\gamma,\delta$, so $\alpha+\gamma=\beta+\delta=180^\circ$. Use coordinates with $D$ at the origin, ray $DC$ horizontal, and ray $DA$ making angle $\delta$ above it. Choose an angle
$$\max(0,\delta-\alpha)<\theta<\min(\delta,180^\circ-\alpha).$$
This interval is nonempty because $0<\alpha,\delta<180^\circ$. Choose $P$ on the ray from $D$ at angle $\theta$, sufficiently close to $D$.

From $P$, draw rays in the directions
$$\delta,\quad0,\quad-\alpha,\quad\delta-\alpha-180^\circ,$$
meeting $AB,BC,CD,DA$ at $K,L,M,N$, respectively. For small enough $DP$, the first two intersections lie inside $AB,BC$ near $A,C$. To check the latter two explicitly, write $DP=t$. Elementary line intersection gives
$$DM=\frac{t\sin(\alpha+\theta)}{\sin\alpha},\qquad DN=\frac{t\sin(\alpha+\theta-\delta)}{\sin\alpha}.$$
Our choice of $\theta$ makes both positive; by shrinking $t$ they are smaller than $DC,DA$. Thus all four intersections are on the intended side interiors and the rays partition the quadrilateral into four convex pieces.

The consecutive clockwise angles at $P$ are
$$\angle KPL=\delta,\quad\angle LPM=\alpha,\quad\angle MPN=\beta,\quad\angle NPK=\gamma.$$
Each is supplementary to the opposite original corner angle. Hence $BKPL$, $CLPM$, $DMPN$, and $AKPN$ are cyclic.

Moreover $KP\parallel AD$, so $AKPN$ is a cyclic trapezoid, and therefore isosceles. Parallel cuts through this piece produce as many isosceles trapezoids as desired; each is cyclic. This completes the construction for every $n\geq4$.''',['Dissection','Cyclic quadrilaterals','Construction'],solution_url='https://prase.cz/kalva/imo/isoln/isoln722.html',note='Official statement checked. Four-piece/trapezoid idea checked against Scholes; the ray-angle interval and exact intersection formulas were independently supplied to justify admissibility.')
add(1972,3,'Number theory',4.5,'Legendre’s factorial formula reduces every prime valuation to a floor inequality. The two fractional parts must cross one half whenever their sum crosses one.',r'For all nonnegative integers $m,n$, prove that $\dfrac{(2m)!(2n)!}{m!\,n!\,(m+n)!}$ is an integer.',r'''Fix a prime $p$. By Legendre's formula, its exponent in the displayed rational number is
$$\sum_{j\geq1}\left(\left\lfloor\frac{2m}{p^j}\right\rfloor+\left\lfloor\frac{2n}{p^j}\right\rfloor-\left\lfloor\frac m{p^j}\right\rfloor-\left\lfloor\frac n{p^j}\right\rfloor-\left\lfloor\frac{m+n}{p^j}\right\rfloor\right).$$
Every summand is nonnegative. To see this for a positive divisor parameter $d=p^j$, write $m/d=a+x$, $n/d=b+y$, with integers $a,b$ and $0\leq x,y<1$. The expression reduces to
$$\lfloor2x\rfloor+\lfloor2y\rfloor-\lfloor x+y\rfloor.$$
If $x+y<1$, the last floor is zero. If $x+y\geq1$, at least one of $x,y$ is at least $1/2$, so the first two floors sum to at least one, matching the last floor. Thus every prime has nonnegative exponent in the ratio, proving it is an integer. The argument includes $m=0$ or $n=0$.''',['Factorials','Valuations','Floor functions'])
add(1972,4,'Algebra',5.5,'Summing the five constraints reveals a hidden sum-of-squares identity. Positivity of the variables then propagates equality around the cyclic indices.',r'''Find all positive real five-tuples satisfying, with indices read modulo five,
$$(x_i^2-x_{i+2}x_{i+4})(x_{i+1}^2-x_{i+2}x_{i+4})\leq0\qquad(i=1,2,3,4,5).$$''',r'''Exactly the constant positive tuples $(t,t,t,t,t)$ work.

Let $S$ be the sum of the five left-hand sides, so $S\leq0$. Expanding and regrouping gives the identity
$$2S=\sum_{i=1}^5x_i^2\left((x_{i+1}-x_{i+3})^2+(x_{i+2}-x_{i+4})^2\right),$$
with subscripts modulo five. One can verify it by comparing the squared-product terms and the terms of the form $x_i^2x_jx_k$; each appears with the same coefficient on both sides.

The right side is nonnegative. Therefore it is zero, and since every $x_i>0$, all its squared differences vanish. In particular $x_{i+1}=x_{i+3}$ for every $i$. Stepping by two runs through all five indices, so every variable equals the same positive number. Conversely a constant positive tuple makes all five original products zero.''',['Cyclic inequalities','Sum of squares','Equality cases'],solution_url='https://prase.cz/kalva/imo/isoln/isoln724.html',note='Official system checked. The sum-of-squares identity was independently verified by exact polynomial coefficient comparison; the factor 2 omitted in some informal descriptions is included.')
add(1972,5,'Algebra',4,'Use the actual supremum of the bounded nonzero function. Inputs approaching that supremum turn the functional equation into a sharp bound on the multiplier, without any regularity assumption.',r'''Real-valued functions $f,g$ on $\mathbb R$ satisfy $f(x+y)+f(x-y)=2f(x)g(y)$ for all real $x,y$. Suppose $f$ is not identically zero and $|f(x)|\leq1$ everywhere. Prove $|g(y)|\leq1$ everywhere.''',r'''Let $M=\sup_{x\in\mathbb R}|f(x)|$. The hypotheses give $0<M\leq1$. Fix any real $y$. The functional equation and triangle inequality imply
$$2|f(x)||g(y)|\leq|f(x+y)|+|f(x-y)|\leq2M$$
for every $x$.

Choose a sequence of inputs $x_j$ with $|f(x_j)|\to M$, as permitted by the definition of supremum. Passing to the limit in $|f(x_j)||g(y)|\leq M$ gives $M|g(y)|\leq M$. Since $M>0$, we obtain $|g(y)|\leq1$. The choice of $y$ was arbitrary, proving the assertion.''',['Functional equations','Supremum','Boundedness'])
add(1972,6,'Geometry',5,'Encode a regular tetrahedron by four symmetric vectors. Every four prescribed heights with zero sum arise as their projections onto a suitable vector; scaling and rotation realise the planes.',r'Given four distinct parallel planes in space, prove that a regular tetrahedron exists with one vertex on each plane.',r'''Take the common normal direction as vertical, and let the four plane heights be $h_1,h_2,h_3,h_4$. Subtract their mean $\bar h$ and write $z_i=h_i-\bar h$, so $\sum z_i=0$.

Use the four vertex vectors of a regular tetrahedron
$$v_1=(1,1,1),\ v_2=(1,-1,-1),\ v_3=(-1,1,-1),\ v_4=(-1,-1,1).$$
They satisfy $v_i\cdot v_i=3$ and $v_i\cdot v_j=-1$ for $i\ne j$. Define
$$w=\frac14\sum_{i=1}^4z_iv_i.$$
Then
$$w\cdot v_j=\frac14\left(3z_j-\sum_{i\ne j}z_i\right)=z_j.$$
The vector $w$ is nonzero, since otherwise all the distinct heights would equal their mean.

Scale this regular tetrahedron by $|w|$ and rotate it so that the direction $w/|w|$ becomes vertical. The height of its $j$th vertex after this operation is $|w|v_j\cdot(w/|w|)=z_j$. Translate vertically by $\bar h$. Its four heights are now exactly $h_1,h_2,h_3,h_4$, as required. Scaling, rotation and translation preserve regularity.''',['Solid geometry','Vectors','Projection'])
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
