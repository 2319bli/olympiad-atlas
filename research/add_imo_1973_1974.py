from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');raw=p/'international-raw';r=json.loads((p/'international-reviews.json').read_text())
def add(year,num,topic,rating,reason,statement,solution='',tags=None,solution_url=None,note=None):
 slug=f'imo_{year}_official_p{num}'
 d={'id':slug,'competition_code':'IMO','competition':'IMO','year':year,'problem_number':str(num),'primary_domain':topic,'topics':[[topic,t] for t in (tags or [])],'problem_markdown':statement,'solutions_markdown':[solution],'officialSourceUrl':f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf','officialSolutionUrl':solution_url or f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf','reviewNote':note or 'Official released statement checked; worked exposition independently written and mathematically assessed.'}
 (raw/(slug+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2));r[slug]=[rating,reason]
add(1973,1,'Geometry',4.5,'Project onto the median unit-vector direction. Pair the directions on opposite sides of the median; the semicircle condition ensures each pair has a nonnegative projection.',r'An odd number of unit vectors lie in one closed half-plane bounded by a line through their common origin. Prove that their vector sum has length at least one.',r'''Write their directions in order as $\theta_1\leq\cdots\leq\theta_{2m+1}$ in an interval of length $\pi$. Project every vector onto the unit direction $\theta_{m+1}$.

The median vector contributes one. Pair the vectors with indices $i$ and $2m+2-i$ for $1\leq i\leq m$. Their deviations from the median direction are $-u$ and $v$, with $u,v\geq0$ and $u+v\leq\pi$. Their total projection is
$$\cos u+\cos v=2\cos\frac{u+v}{2}\cos\frac{u-v}{2}\geq0.$$
Thus the whole sum has projection at least one onto a unit vector. Its length is at least the magnitude of that projection, proving the claim.''',['Vectors','Ordering','Projection'])
add(1973,2,'Geometry',5,'Combine two centrally symmetric planar examples along a common diameter. Central reflection supplies parallel partners for cross-plane pairs while the hexagon handles diameters.',r'Does there exist a finite noncoplanar set of points in space such that for every pair $A,B$, two other points $C,D$ can be chosen with $AB$ and $CD$ parallel and distinct?',r'''Yes. Take two regular hexagons of the same size, centred at $O$, in perpendicular planes, sharing one pair of opposite vertices. Their union has ten points and is not coplanar.

First, a regular hexagon itself has the required property. For a pair which is not opposite, central reflection gives two other endpoints and a parallel distinct chord. For opposite vertices, their long diagonal is parallel to a side not using either endpoint.

Now consider a pair from the union. If both points lie in one hexagon, use the preceding planar property. Otherwise one point belongs exclusively to each hexagon. Their central reflections $A'=-A$, $B'=-B$ are also in the union and distinct from $A,B$. The lines $AB$ and $A'B'$ are parallel. If they coincided, their common line would pass through $O$, forcing $A,B$ to be antipodal points on the common circumradius sphere. But antipodes lie in the same hexagon, contradicting the chosen cross-plane pair. Hence these lines are distinct, proving the construction works.''',['Construction','Central symmetry','Solid geometry'],solution_url='https://prase.cz/kalva/imo/isoln/isoln732.html')
add(1973,3,'Algebra',4.5,'The reciprocal polynomial reduces to a quadratic in $x+1/x$. Cauchy–Schwarz then minimises the coefficient norm over the feasible parameter range.',r'Among real $a,b$ for which $x^4+ax^3+bx^2+ax+1=0$ has a real root, find the least possible value of $a^2+b^2$.',r'''A root is nonzero. Divide by $x^2$ and put $t=x+1/x$, so $|t|\geq2$. The equation becomes
$$t^2+at+b-2=0.$$
Cauchy–Schwarz gives
$$a^2+b^2\geq\frac{(at+b)^2}{t^2+1}=\frac{(t^2-2)^2}{t^2+1}.$$
For $u=t^2\geq4$,
$$\frac{(u-2)^2}{u+1}-\frac45=\frac{(u-4)(5u-4)}{5(u+1)}\geq0.$$
Thus $a^2+b^2\geq4/5$.

Equality is attained at $(a,b)=(-4/5,-2/5)$, where $x=1$ is a root, and at $(a,b)=(4/5,-2/5)$, where $x=-1$ is a root. Therefore the required minimum is $4/5$.''',['Reciprocal polynomials','Cauchy–Schwarz','Optimisation'])
add(1973,4,'Geometry',5.5,'The two far vertices impose a shortest route through two disks. Symmetry identifies the first contact, and convexity of segment neighbourhoods verifies that the optimal route actually covers the entire triangle.',r'''A detector senses every point within distance half the altitude of an equilateral triangle. Starting at one vertex, a person must follow a path whose detector covers the entire triangle. Determine a path of minimum length.''',r'''Scale the triangle to side one and label the starting vertex $A$, the others $B,C$. Set $r=\sqrt3/4$, the detector radius. Let $E$ be the midpoint of $AC$, and $X$ the midpoint of $BE$. Thus $BX=EX=r$. On $XC$, choose $Y$ with $CY=r$. The optimal route is $A\to X\to Y$, or its reflection exchanging $B,C$, with length
$$AX+XY=\frac{2\sqrt7-\sqrt3}{4}.$$
For side length $s$, multiply this length by $s$.

To prove the lower bound, any valid route must enter the radius-$r$ disks centred at $B$ and $C$. Suppose it reaches the $B$ disk first, at $U$. The travel up to $U$ and then to the $C$ disk is at least
$$AU+UC-r.$$
Use coordinates with $AC$ horizontal and $E$ its midpoint. Every point $U$ of the $B$ disk has height at least $r$ above $AC$. If that height is $h$, the sum $AU+UC$ is minimised at horizontal coordinate $E$, by reflection and the triangle inequality, and is at least $2\sqrt{1/4+h^2}$. Therefore it is at least $2\sqrt{1/4+r^2}=\sqrt7/2$. Equality occurs at $U=X$, giving the stated bound and route.

Finally verify coverage, not just the two vertices. The set within distance $r$ of a segment is convex. The neighbourhood of $AX$ contains $A,B,E$, because $B,E$ are both distance $r$ from $X$; hence it contains triangle $ABE$. The neighbourhood of $XY$ contains $B,E,C$, using $CY=r$; hence it contains triangle $BCE$. Those triangles fill $ABC$. Thus the proposed path detects the whole region and attains the lower bound.''',['Optimisation','Covering','Reflection'],solution_url='https://prase.cz/kalva/imo/isoln/isoln734.html',note='Official statement checked. The shortest-route argument was checked against Scholes; full-region coverage is explicitly proved using convex segment neighbourhoods.')
add(1973,5,'Algebra',4.5,'A commutator has slope one and must have a fixed point, so it is the identity. Commutativity then transports one unique fixed point to itself under every group element.',r'''A set $G$ of nonconstant real affine functions $f(x)=ax+b$ is closed under composition and taking inverses. Every member has a real fixed point. Prove that all members share one fixed point.''',r'''If $G$ is empty or consists only of the identity, any real number works. Otherwise choose a nonidentity $f\in G$.

For any $u,v\in G$, their commutator $u\circ v\circ u^{-1}\circ v^{-1}$ belongs to $G$. Its slope is one, so it is a translation $x\mapsto x+c$. The fixed-point hypothesis forces $c=0$. Thus every commutator is the identity and all functions in $G$ commute.

The chosen nonidentity $f$ cannot have slope one, because a nonidentity translation has no fixed point. It therefore has a unique fixed point $k$. For any $g\in G$, commutativity gives
$$f(g(k))=g(f(k))=g(k).$$
So $g(k)$ is also a fixed point of $f$, and uniqueness implies $g(k)=k$. Hence this $k$ is fixed by every member of $G$.''',['Affine functions','Fixed points','Group structure'])
add(1973,6,'Algebra',5,'Smooth the data with a two-sided geometric kernel. Separate the contributions on either side of each index to control adjacent ratios, then use the geometric-series sum for the total bound.',r'''Given positive $a_1,\ldots,a_n$ and $0<q<1$, construct positive $b_1,\ldots,b_n$ such that $b_k>a_k$, $q<b_{k+1}/b_k<1/q$, and
$$\sum_{k=1}^nb_k<\frac{1+q}{1-q}\sum_{k=1}^na_k.$$''',r'''Set $c_i=\sum_{j=1}^na_jq^{|i-j|}$. For every $i<n$,
$$c_{i+1}-qc_i=(1-q^2)\sum_{j=i+1}^na_jq^{j-i-1}>0,$$
and
$$c_i-qc_{i+1}=(1-q^2)\sum_{j=1}^ia_jq^{i-j}>0.$$
Thus $q<c_{i+1}/c_i<1/q$.

Also $c_i\geq a_i$, and reversing the finite sums gives
$$\sum_i c_i=\sum_j a_j\sum_{i=1}^nq^{|i-j|}<\sum_j a_j\left(1+2\sum_{k=1}^{\infty}q^k\right)=\frac{1+q}{1-q}\sum_j a_j.$$
The inequality is strict because each finite inner sum omits some positive terms from the infinite two-sided series.

Choose $\varepsilon>0$ sufficiently small that multiplying the left side by $1+\varepsilon$ still preserves this strict total bound, and put $b_i=(1+\varepsilon)c_i$. Then $b_i>a_i$, the adjacent ratios are unchanged, and the total has the desired bound. This also handles $n=1$, when there are no ratio conditions.''',['Constructive inequalities','Geometric series','Smoothing'])
add(1974,1,'Combinatorics',4,'Use the total count to fix the number of rounds, then extremal individual totals restrict the three card values to two possibilities. The last-round condition then determines both earlier deals.',r'''Three cards carry integers $0<p<q<r$. In each round they are shuffled and dealt one each to players $A,B,C$, who receive that many counters and keep all previous counters. After at least two rounds, their totals are $20,10,9$, respectively. In the last round $B$ receives $r$. Who received $q$ in the first round?''',r'''The total is $39$, so the number $t\geq2$ of rounds divides $39$. Since $p+q+r\geq6$, we have $t\leq6$, leaving $t=3$ and $p+q+r=13$.

Player $A$'s total requires $r\geq7$. Player $B$ receives $r$ last and at least $p$ in each earlier round, so $r+2p\leq10$. Thus $p=1$ and $r$ is seven or eight. The possibilities are $(p,q,r)=(1,5,7)$ or $(1,4,8)$.

The first is impossible: all three card values are odd, so a total after three rounds must be odd, whereas $A$ has 20. Hence the cards are $1,4,8$.

The totals force $A$ to receive $8,8,4$; $B$ to receive $1,1,8$; and $C$ to receive $4,4,1$. Since $B$ gets eight last, the final deal is $(A,B,C)=(4,8,1)$. Both earlier deals are $(8,1,4)$. Therefore $C$ received $q=4$ in the first round.''',['Integer constraints','Parity','Case analysis'])
add(1974,2,'Geometry',4.5,'Stewart’s theorem converts the distance condition into a reciprocal sum with a fixed total. Its minimum is given by Cauchy–Schwarz, and half-angle identities connect the resulting side condition to the stated one.',r'''Prove that triangle $ABC$ has a point $D$ on $AB$ with $CD^2=AD\cdot DB$ if and only if $\sin A\sin B\leq\sin^2(C/2)$.''',r'''Write $BC=a$, $CA=b$, $AB=c$, and $AD=x$, $DB=y$, so $x+y=c$. Stewart's theorem gives
$$a^2x+b^2y=c(CD^2+xy).$$
Thus $CD^2=xy$ is equivalent to
$$\frac{a^2}{y}+\frac{b^2}{x}=2c.$$
For positive $x,y$ summing to $c$, Cauchy–Schwarz says the left side has minimum $(a+b)^2/c$, attained when $y:x=a:b$. It is continuous and tends to infinity at either endpoint. Therefore the required $D$ exists exactly when $a+b\leq\sqrt2c$.

By the sine rule and sum-to-product identity,
$$\frac{a+b}{c}=\frac{\cos((A-B)/2)}{\sin(C/2)}.$$
Also
$$\sin A\sin B=\cos^2((A-B)/2)-\sin^2(C/2).$$
Consequently $a+b\leq\sqrt2c$ is equivalent to $\sin A\sin B\leq\sin^2(C/2)$, as asserted. A solution cannot be an endpoint because $CD>0$, so the positive $x,y$ analysis covers every possible solution.''',['Stewart’s theorem','Cauchy–Schwarz','Existence conditions'])
add(1974,3,'Number theory',5,'Extract odd binomial terms with conjugate radicals, derive an integer recurrence, and establish a short nonzero residue cycle modulo five.',r'Prove that $\displaystyle S_n=\sum_{k=0}^n\binom{2n+1}{2k+1}2^{3k}$ is not divisible by five for any integer $n\geq0$.',r'''The binomial theorem gives
$$S_n=\frac{(1+\sqrt8)^{2n+1}-(1-\sqrt8)^{2n+1}}{2\sqrt8}.$$
The two squared bases have sum $18$ and product $49$, so
$$S_{n+2}=18S_{n+1}-49S_n,$$
with $S_0=1$, $S_1=11$. Reducing modulo five, the recurrence is
$$S_{n+2}\equiv3S_{n+1}+S_n\pmod5.$$
Starting from $(1,1)$, its first fourteen residues are
$$1,1,4,3,3,2,4,4,1,2,2,3,1,1.$$
The last pair repeats the first. Since each pair determines all subsequent terms, the first twelve residues repeat periodically. None is zero, proving that five never divides $S_n$.''',['Binomial coefficients','Recurrences','Modular arithmetic'])
layout=json.loads((p/'international-official/imo1974p4-tilings.json').read_text())
sol=r'''The maximum is $p=7$, and the possible white-square counts are
$$(1,2,3,4,5,7,10),\quad(1,2,3,4,5,8,9),$$
$$(1,2,3,4,6,7,9),\quad(1,2,3,5,6,7,8).$$

A grid rectangle contains equal numbers of the two colours exactly when its area is even. Hence the positive distinct integers $a_i$ sum to 32. Since $1+\cdots+8=36>32$, there can be at most seven pieces.

For seven pieces, put $d_i=a_i-i$. These are nonnegative nondecreasing integers with sum four. The five partitions of four yield the four sequences above and $(1,2,3,4,5,6,11)$. The latter would need a rectangle of area 22, whose only integer side lengths are $1,22$ or $2,11$, so it cannot fit on an eight-by-eight board.

Here are explicit tilings for the other four possibilities. Number columns and rows from 1 to 8. Each tuple below means (white-square count, first column, first row, width, height). In each list the rectangles are disjoint and fill the board; every area is twice its first entry, so its colours balance.

'''
for k,item in enumerate(layout,1):
 sol+=f"{k}. "+'; '.join('$('+','.join(map(str,t))+')$' for t in item['rectangles'])+'.\n\n'
add(1974,4,'Combinatorics',5,'The distinct even areas give a sharp partition bound, but one formal size list is geometrically impossible. Four explicit tilings are needed to prove all remaining lists attainable.',r'''Partition an $8\times8$ chessboard into nonoverlapping grid rectangles, each with equal numbers of black and white squares. Let their white-square counts be distinct, ordered $a_1<\cdots<a_p$. Determine the largest $p$ and all possible sequences at that value.''',sol,['Tiling','Integer partitions','Construction'],solution_url='https://prase.cz/kalva/imo/isoln/isoln744.html',note='Official statement checked. All five numerical partitions were enumerated (one is omitted from the prose of a secondary solution). The four valid tilings were independently constructed and checked with exact grid coordinates.')
add(1974,5,'Algebra',4,'Simple denominator comparisons give strict bounds, but determining the entire range also requires two different limiting families and continuity.',r'Find the complete range, for positive $a,b,c,d$, of $\dfrac a{a+b+d}+\dfrac b{a+b+c}+\dfrac c{b+c+d}+\dfrac d{a+c+d}$.',r'''The range is the open interval $(1,2)$.

Writing $T=a+b+c+d$, each denominator is less than $T$, so the sum $S$ is greater than $(a+b+c+d)/T=1$. On the other hand,
$$\frac a{a+b+d}+\frac b{a+b+c}<\frac a{a+b}+\frac b{a+b}=1,$$
and similarly the last two terms sum to less than one. Hence $S<2$.

For $a=1$, $b=t$, $c=d=t^2$, letting $t\downarrow0$ gives $S\to1$. For $a=c=1$, $b=d=t$, the same limit gives $S\to2$. Every intermediate value is attained: given $s\in(1,2)$, choose a positive tuple from the first family with $S<s$ and one from the second with $S>s$. The line segment between these tuples stays in the positive orthant, and $S$ is continuous on it. The intermediate value theorem supplies a tuple with $S=s$.''',['Inequalities','Range','Continuity'])
add(1974,6,'Number theory',4,'Choose the least integer at which the polynomial is plus or minus one. The polynomial difference divisibility restricts every opposite-sign occurrence to the next two integers.',r'''For a nonconstant polynomial $P$ with integer coefficients, let $N$ count the integers $k$ such that $P(k)^2=1$. Prove $N\leq\deg P+2$.''',r'''Let $d=\deg P$. If there are no such integers the claim is immediate. Otherwise choose the smallest one, $r$, and put $\varepsilon=P(r)\in\{1,-1\}$.

The polynomial $P(x)-\varepsilon$ has degree $d$, so at most $d$ distinct integer zeros. If instead $P(s)=-\varepsilon$, then $s>r$ and integer-coefficient polynomial divisibility gives
$$s-r\mid P(s)-P(r)=-2\varepsilon.$$
Thus $s-r$ is either one or two. The opposite-sign equation contributes at most the two integers $r+1,r+2$. Together there are at most $d+2$ occurrences, as required.''',['Polynomial divisibility','Roots','Extremal principle'],solution_url='https://prase.cz/kalva/imo/isoln/isoln746.html')
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
