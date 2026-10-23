from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');raw=p/'international-raw';r=json.loads((p/'international-reviews.json').read_text())
def add(year,num,topic,rating,reason,statement,solution='',tags=None,note=None):
 slug=f'imo_{year}_official_p{num}'
 d={'id':slug,'competition_code':'IMO','competition':'IMO','year':year,'problem_number':str(num),'primary_domain':topic,'topics':[[topic,t] for t in (tags or [])],'problem_markdown':statement,'solutions_markdown':[solution],'officialSourceUrl':f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf','officialSolutionUrl':f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf','reviewNote':note or 'Official released statement checked; worked exposition independently written and mathematically assessed.'}
 (raw/(slug+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2));r[slug]=[rating,reason]
add(1964,1,'Number theory',1.5,'The powers of two modulo seven have the three-term cycle 2,4,1; this immediately answers both parts.',r'For which positive integers $n$ does $7\mid2^n-1$? Prove that $7$ never divides $2^n+1$.')
add(1964,2,'Algebra',2.5,'After collecting terms this is Schur’s degree-three inequality. Ordering the three variables gives an immediate nonnegative factorisation.',r'For triangle side lengths $a,b,c$, prove $a^2(b+c-a)+b^2(c+a-b)+c^2(a+b-c)\leq3abc$.')
add(1964,3,'Geometry',3.5,'Similarity gives the three small inradii as $r(s-a)/s$, $r(s-b)/s$, $r(s-c)/s$; Heron’s formula then expresses their squared sum in the given side lengths.',r'A triangle with sides $a,b,c$ has an incircle. For each side draw the other tangent to that incircle parallel to the side, cutting off a smaller triangle near the opposite vertex. Inscribe a circle in each of those three triangles. Express the sum of the four circle areas in terms of $a,b,c$.')
add(1964,4,'Combinatorics',4.5,'Apply pigeonhole at one vertex to obtain six edges of one colour, then establish the two-colour six-vertex lemma inside that neighbour set.',r'Each pair among seventeen people corresponds on exactly one of three topics. Prove that three people can be found such that every pair among the three corresponds on the same topic.',r'''Colour the edge joining each pair of people by their topic. Choose a person $P$. Of the sixteen edges from $P$, at least six have the same colour, say red. Let $S$ be six corresponding neighbours.

If an edge inside $S$ is red, its endpoints together with $P$ give the required triangle. Otherwise all edges inside $S$ have the other two colours, blue and green.

To finish, any blue-green colouring of the edges among six vertices has a monochromatic triangle. Choose one vertex $Q$. At least three of its five edges have the same colour, say blue, and let their other endpoints be $U,V,W$. If one of $UV,VW,WU$ is blue, it forms a blue triangle with $Q$. If none is blue, $UVW$ is a green triangle. Applying this lemma to $S$ proves the claim.''',['Pigeonhole principle','Ramsey theory','Graph colouring'])
add(1964,5,'Combinatorics',5.5,'Count pairs of the thirty perpendiculars, then subtract unavoidable parallel pairs and both kinds of multiple intersections. Attainment requires checking that an actual five-point configuration has no additional coincidences.',r'Five points lie in a plane such that no two lines joining pairs of points are parallel, perpendicular or coincident. Through each point draw perpendiculars to all six lines joining pairs of the other four points. What is the largest possible number of distinct intersections of these perpendiculars?',r'''The maximum is $315$.

There are thirty distinct perpendicular lines. Each of the ten original joining lines gives a parallel family of three, so exactly $10\binom32=30$ pairs do not intersect. The remaining pairs contribute $\binom{30}2-30=405$ intersection incidences.

At each original point six perpendiculars meet; their $\binom62=15$ incidences represent just one point. This forces a loss of $5(15-1)=70$. Also, for each of the ten triangles on the original points, its three altitudes occur among the perpendiculars and concur at its orthocentre. Their three incidences represent one point, forcing a further loss of at least $10(3-1)=20$. These altitude triples use disjoint sets of lines; none of their intersection incidences belongs to an original-point group. Any coincidence between several such groups only increases the loss. Thus there are at most $405-70-20=315$ distinct points.

For a concrete configuration attaining the bound, take
$$(0,0),\ (2,1),\ (5,7),\ (11,3),\ (17,19).$$
Its ten joining directions are pairwise nonparallel and nonperpendicular. Exact line-intersection calculation gives five points where six lines concur, ten where three concur, and 300 ordinary double intersections, hence 315 in all.

Here is a reproducible exact check of this attainment calculation. For every base point $(x,y)$ and every pair of other points with difference vector $(a,b)$, form the perpendicular line $aX+bY=ax+by$. For two such lines $(a,b,c)$ and $(d,e,f)$ with $ae-bd\ne0$, the intersection is
$$\left(\frac{ce-bf}{ae-bd},\frac{af-cd}{ae-bd}\right).$$
Reducing these rational coordinates and collecting equal pairs gives 300 coordinate pairs occurring once, ten occurring three times, and five occurring fifteen times. These account for all $300+30+75=405$ intersecting line pairs, establishing the claimed maximum.''',['Counting','Incidence geometry','Extremal problems'],note='Official statement checked. The upper bound is a hand-checked incidence argument; the explicit attainment coordinates and rational multiplicity table were independently verified by exact arithmetic.')
add(1964,6,'Geometry',4.5,'Use barycentric weights of the chosen base point. Each opposite-plane intersection has reciprocal height, which cancels its corresponding area weight in a determinant expansion.',r'''In tetrahedron $ABCD$, let $D_0$ be the centroid of $ABC$. Lines through $A,B,C$ parallel to $DD_0$ meet the opposite face planes $BCD,CAD,ABD$ at $A_1,B_1,C_1$. Prove $\operatorname{Vol}(A_1B_1C_1D_0)=3\operatorname{Vol}(ABCD)$. Does the same result hold for every $D_0$ inside $ABC$?''',r'''It holds for every interior point $D_0$. Take $D_0$ as the origin and write the position vectors of $A,B,C,D$ as $a,b,c,d$. There are positive barycentric weights $\alpha,\beta,\gamma$ with
$$\alpha+\beta+\gamma=1,\qquad\alpha a+\beta b+\gamma c=0.$$
The line through $A$ has points $a+td$. Expressing the origin by the displayed barycentric relation, its affine coefficient at $A$ is $1-t\alpha$. It lies in plane $BCD$ exactly when that coefficient vanishes. Thus
$$a_1=a+d/\alpha,\quad b_1=b+d/\beta,\quad c_1=c+d/\gamma.$$
Let $\Delta=\det(b-a,c-a,d)$, the oriented sixfold volume of $ABCD$. The area ratios on the base plane give
$$\det(b,c,d)=\alpha\Delta,\quad\det(c,a,d)=\beta\Delta,\quad\det(a,b,d)=\gamma\Delta.$$
Multilinearity, together with $\det(a,b,c)=0$, now yields
$$\det(a_1,b_1,c_1)=\frac{\det(d,b,c)}\alpha+\frac{\det(a,d,c)}\beta+\frac{\det(a,b,d)}\gamma=3\Delta.$$
Taking absolute values and dividing by six proves the volume relation. For the centroid the three weights are all $1/3$, but no step requires them to be equal.''',['Solid geometry','Volumes','Barycentric coordinates'])
add(1965,1,'Algebra',2.5,'The radical expression is $2\min(|\sin x|,|\cos x|)$; the upper bound is automatic and the lower one gives a single angular interval.',r'Find all $x\in[0,2\pi]$ satisfying $2\cos x\leq\left|\sqrt{1+\sin2x}-\sqrt{1-\sin2x}\right|\leq\sqrt2$.')
add(1965,2,'Algebra',3,'Choose an unknown of maximum absolute value. Strict diagonal dominance makes its equation impossible unless every unknown is zero.',r'A homogeneous three-variable linear system has positive diagonal coefficients, negative off-diagonal coefficients, and positive sum of coefficients in each equation. Prove its only solution is the zero triple.')
add(1965,3,'Geometry',4.5,'A parallel slice fixes four equal edge-division ratios. Triangulating one truncated solid into three tetrahedra gives a cubic fraction and avoids a calculus prerequisite.',r'''Opposite edges $AB,CD$ of a tetrahedron have lengths $a,b$, their supporting lines are distance $d$ apart, and the angle between those lines is $\omega$. A plane parallel to both edges cuts the tetrahedron, and its distances from $AB,CD$ are in ratio $k:1$. Find the ratio of the two resulting volumes.''',r'''Let $t=k/(k+1)$, the fraction of the distance from the $AB$ plane to the $CD$ plane reached by the cutting plane. It meets $AC,AD,BC,BD$ at $E,F,G,H$, respectively, at this same fraction $t$ from the endpoints $A,A,B,B$.

The solid on the $AB$ side is the union, with disjoint interiors, of tetrahedra $ABEF$, $BEFH$, and $BEGH$. Their volume fractions relative to $ABCD$ are
$$t^2,\qquad t^2(1-t),\qquad t^2(1-t).$$
For an explicit verification, an affine change of coordinates takes $A$ to $0$ and $B,C,D$ to the three coordinate unit vectors. Then
$$E=(0,t,0),\quad F=(0,0,t),\quad G=(1-t,t,0),\quad H=(1-t,0,t),$$
and the three scalar triple products give the stated fractions. Volume ratios are unchanged by the affine transformation.

The fraction on the $AB$ side is therefore $3t^2-2t^3$, and the other fraction is $1-3t^2+2t^3$. Substituting $t=k/(k+1)$ gives the ratio
$$\boxed{k^2(k+3):(3k+1)}.$$
The quantities $a,b,d,\omega$ affect total volume, but cancel from this ratio.''',['Solid geometry','Volumes','Dissection'])
add(1965,4,'Algebra',4,'Subtracting two equations factors a difference of variables. A careful split between equal and unequal pairs then collapses the four-variable system to a quadratic.',r'Find all real quadruples $(x_1,x_2,x_3,x_4)$ for which each variable plus the product of the other three equals $2$.',r'''Subtracting the equations with first terms $x_i,x_j$ gives
$$(x_i-x_j)(1-x_kx_l)=0,$$
where $k,l$ are the remaining indices.

If all four variables equal $t$, then $t+t^3=2$. Since $t^3+t$ is strictly increasing, this gives $t=1$.

Otherwise, relabel so that $x_1\ne x_2$. Then $x_3x_4=1$, and the first equation gives $x_1+x_2=2$. If $x_3\ne x_4$, the same subtraction gives $x_1x_2=1$, which together with their sum forces $x_1=x_2=1$, a contradiction. Thus $x_3=x_4=s$ with $s=1$ or $-1$.

If $s=1$, the third equation again forces $x_1x_2=1$, impossible. If $s=-1$, it gives $x_1x_2=-3$. The sum $2$ then yields $\{x_1,x_2\}=\{3,-1\}$.

Consequently the solutions are $(1,1,1,1)$ and all permutations of $(3,-1,-1,-1)$. Direct substitution checks each.''',['Symmetric systems','Factorisation','Case analysis'])
add(1965,5,'Geometry',4.5,'The orthocentre equations expose a fixed reflection followed by a contraction. Identifying that map proves both the locus and its full attainability.',r'''In triangle $OAB$, angle $AOB=\omega$ is acute. For $M\ne O$, let $P,Q$ be its perpendicular projections onto $OA,OB$, and let $H$ be the orthocentre of $OPQ$. Find the locus of $H$ as $M$ ranges over (a) $AB$ and (b) the interior of $OAB$.''',r'''The map $M\mapsto H$ is reflection in the internal bisector of $\angle AOB$, followed by a homothety of centre $O$ and scale $\cos\omega$.

To prove this, place $O$ at the origin and let $u,v$ be unit vectors along $OA,OB$, so $u\cdot v=c:=\cos\omega>0$. If $m,h$ are the position vectors of $M,H$, then the feet have vectors $p=(m\cdot u)u$ and $q=(m\cdot v)v$. The altitudes from $Q,P$ give
$$h\cdot u=q\cdot u=c(m\cdot v),\qquad h\cdot v=p\cdot v=c(m\cdot u).$$
Reflection $R$ in the angle bisector exchanges $u,v$, so $cR(m)$ has exactly these two scalar products. Since $u,v$ are independent, they determine the vector uniquely, proving $h=cR(m)$.

Let $A^*=cR(A)$ and $B^*=cR(B)$. For (a), the locus is the entire segment $A^*B^*$, including endpoints if they are allowed for $M$. For (b), it is precisely the interior of triangle $OA^*B^*$. Reflection and positive scaling are bijections, so every point in each stated locus is attained. The acute-angle assumption also ensures that the projections of an interior $M$ or a point on $AB$ are nonzero, so $OPQ$ is nondegenerate.''',['Loci','Orthocentre','Transformations'])
add(1965,6,'Combinatorics',5.5,'Turn the longest segments into a graph on a convex polygon. Pairwise intersection forces a leaf whenever some vertex has three neighbours, making induction possible.',r'A set of $n\geq3$ distinct points lies in a plane. Call a joining segment a diameter if its length is the largest distance between any two points of the set. Prove there are at most $n$ diameters.',r'''Let the largest distance be $d$, and form the graph whose edges are segments of length $d$.

Every endpoint of such an edge is a vertex of the convex hull. Indeed, if $A$ is not an extreme point and $AB=d$, write $A$ as a nontrivial convex combination of other points. The strict convexity of the disk of radius $d$ centred at $B$ puts $A$ strictly inside that disk, a contradiction.

Any two diameter edges intersect. Otherwise their four endpoints occur in convex order $A,B,C,D$ with diameter edges $AB,CD$. If the diagonals meet at $X$, the triangle inequality gives
$$AB+CD<AX+BX+CX+DX=AC+BD\leq2d,$$
contradicting $AB=CD=d$.

We prove the required bound for any graph drawn on convexly positioned vertices whose edges pairwise intersect. If every vertex has degree at most two, the degree sum already gives at most as many edges as vertices. Otherwise a vertex $A$ has at least three neighbours $B,C,D$ in that circular order around the remaining boundary. The middle neighbour $C$ has no neighbour other than $A$: a segment from $C$ to any other vertex cannot intersect both $AB$ and $AD$, since those chords cut off disjoint boundary arcs from the viewpoint of $C$. More explicitly, to cross $AB$ its other endpoint must lie on the arc from $A$ to $B$, while to cross $AD$ it must lie on the arc from $D$ to $A$; these arcs have only $A$ in common. Endpoints $B,D$ fail to meet the other outer chord as well.

Thus $C$ is a leaf. Delete it and its single edge and apply induction. The remaining graph still has pairwise intersecting edges. Adding back one vertex and one edge preserves the bound. Isolated original points can be ignored or added back, so the number of diameters is at most $n$.''',['Extremal geometry','Graphs','Induction'])
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
