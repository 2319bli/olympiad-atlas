from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');r=json.loads((p/'international-reviews.json').read_text());slug='imo_1967_official_p4'
statement=r'''Two acute triangles $A_0B_0C_0$ and $A_1B_1C_1$ are given. Among triangles $ABC$ similar to $A_1B_1C_1$ under the corresponding vertex labels, with $A_0\in BC$, $B_0\in CA$, $C_0\in AB$, determine and construct one of maximum area.'''
solution=r'''Write $\alpha=\angle A_1$, $\beta=\angle B_1$, and put $p=\cot\alpha$, $q=\cot\beta$. Place $C_0$ at the origin, with vectors $a=A_0$, $b=B_0$ oriented so that $D=\det(a,b)>0$. Let $J$ denote rotation through $90^\circ$ counterclockwise and construct
$$W=a-b-pJb-qJa.$$
Take the line through $C_0$ parallel to $W$ as $AB$. Through $B_0$ draw the line making angle $\alpha$ with the positive direction of $W$, and through $A_0$ the line making angle $180^\circ-\beta$ with it. These are $AC,BC$ and determine the required triangle. All the vector sums, rotations and cotangent scalings are straightedge-and-compass constructions from the given angles.

Here is the maximality argument. For an arbitrary oriented unit direction $u$ of $AB$, put $n=Ju$. Intersecting the two other prescribed side lines with $AB$ gives the coordinates
$$A\cdot u=b\cdot u-p(b\cdot n),\qquad B\cdot u=a\cdot u+q(a\cdot n).$$
Hence its signed side length is
$$AB=(a-b)\cdot u+(pb+qa)\cdot n=W\cdot u\leq|W|.$$
Equality occurs at the constructed direction $u=W/|W|$. Since all the triangles have the same angles, their areas are proportional to $AB^2$.

We must also check that the constructed side lines really enclose the three prescribed points. This is where both acute-angle assumptions matter. Write $s=a\cdot b$. Acuteness of $A_0B_0C_0$ gives
$$s>0,\quad |a|^2-s>0,\quad |b|^2-s>0,$$
and acuteness of the target triangle gives $p,q>0$ and $pq<1$. For $u=W/|W|$, the two lengths from $C_0$ to $A,B$ have positive numerators
$$(1+p^2)|b|^2+(pq-1)s+(p+q)D,$$
$$(1+q^2)|a|^2+(pq-1)s+(p+q)D,$$
respectively, when multiplied by $|W|$. They are positive by the inequalities above. Thus $C_0$ lies inside $AB$.

The heights of $B_0,A_0$ above $AB$ have numerators $D+p|b|^2+qs$ and $D+ps+q|a|^2$, so both are positive. The height of $C$ is $|W|/(p+q)$. Its difference from the height of $B_0$, multiplied by the positive factor $|W|(p+q)$, equals
$$(1+q^2)(|a|^2-s)+(1-pq)(|b|^2-s)+(p+q)D>0.$$
For $A_0$ the analogous numerator is
$$(1-pq)(|a|^2-s)+(1+p^2)(|b|^2-s)+(p+q)D>0.$$
Therefore $B_0,A_0$ lie strictly between the appropriate vertices on $AC,BC$. The constructed triangle is admissible and attains the global upper bound.

Equivalently, construct the circle through $B_0,C_0$ on which the angle subtended by $B_0C_0$ is $\alpha$, using its centre on the side away from $A_0$, and the analogous circle through $A_0,C_0$ with angle $\beta$. Their centre difference is $W/2$, so $AB$ is parallel to the line joining these centres.'''
d={'id':slug,'competition_code':'IMO','competition':'IMO','year':1967,'problem_number':'4','primary_domain':'Geometry','topics':[['Geometry',t] for t in ['Construction','Optimisation','Similar triangles']],'problem_markdown':statement,'solutions_markdown':[solution],'officialSourceUrl':'https://www.imo-official.org/assets/documents/problems/1967/1967_eng.pdf','officialSolutionUrl':'https://prase.cz/kalva/imo/isoln/isoln674.html','reviewNote':'Official statement checked. Scholes’s circle-centre construction was independently verified by a vector maximum argument; the acute-angle admissibility check is supplied in full.'}
(p/'international-raw'/f'{slug}.json').write_text(json.dumps(d,ensure_ascii=False,indent=2));r[slug]=[6.5,'The right construction maximises a projection between two fixed circle centres. A complete solution must also prove the extremal triangle encloses the prescribed contact triangle; both acuteness assumptions enter that feasibility check.'];(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
