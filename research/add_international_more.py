from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');raw=p/'international-raw';r=json.loads((p/'international-reviews.json').read_text());o=json.loads((p/'international-extra-solutions.json').read_text())
r.update({
'rou_2025_e406cf':[4.5,'Choose the largest index among a point and its ten nearest neighbours; the ordering hypothesis and triangle inequality then bound the entire cluster.'],
'rou_2025_daceb6':[6.5,'The key invariant is strict increase of the largest prime factor; proving it combines multiplicative order with an odd valuation preserved by lifting the exponent.'],
'rou_2025_742b0e':[8.5,'The sharp multivariate degree bound requires a roots-of-unity obstruction, generic linear combinations, star decompositions of trees and an interpolation correction.'],
'rou_2025_fb3b41':[6.5,'Multiplicative factorisation identities first remove the constant shift, then an adjacent-square identity forces constant second differences and polynomial behaviour.'],
'rou_2025_9e5c95':[8,'The proof uses inversion combined with reflection, a rotational homothety between auxiliary circles and a final directed-angle argument.'],
'rou_2025_b5cc5a':[8,'A sharp intersecting-family bound needs a carefully balanced representation by odd cycles and a uniform multiplicity double count.'],
'btw_2023_3ab5ed':[5.5,'Radical axes convert the property into concurrency of three diagonals; the converse uses signed power and the fact that the concurrency point is inside the original circle.'],
'btw_2023_aa63a1':[5.5,'Isogonality of circumcentre and orthocentre turns the collinearity assumption into two angle-bisector ratios, forcing equal distances from two vertices.'],
'btw_2023_df10b2':[7,'Several auxiliary projections and contact-triangle angle chases are needed to place both pairs of altitude feet on the same line.'],
'btw_2023_82adde':[6.5,'Successive cyclic quadrilaterals identify an auxiliary orthocentre and angle bisector; a final symmetry of a diameter circle yields concurrency.'],
'btw_2023_f6a9be':[6.5,'Power of a point places five auxiliary points on one circle; angle chasing then produces an angle-bisector ratio matching a tangent ratio from the original triangle.'],
'btw_2023_2782d4':[6,'Reflect the original circumcircle and introduce the second intersection of KF; two cyclic quadrilaterals then make A the radical centre.'],
'bmo_2023_bc3f7d':[5.5,'Ordering the variables identifies the useful opposite-pair product; harmonic-mean and interval bounds reduce the reciprocal constraint to a squared difference.'],
'bmo_2023_423d32':[6.5,'A periodic/nonperiodic dichotomy is essential; in the nonperiodic branch a hypothetical nonzero root creates a period before oddness forces the identity.'],
'bmo_2023_2ac979':[7,'Sorting a long block converts separation into reciprocal gap bounds; an extremal count of repeated indices and a harmonic-sum limit improve the three-quarter threshold.'],
'bmo_2023_bfc001':[6.5,'The construction designs one polynomial with no roots and another with exactly one root, while prescribing the level sets needed for the two composition counts.'],
'bmo_2023_a23af0':[7.5,'After establishing bijectivity, the inverse equation must be composed in two orders to create arbitrary translations on an unbounded positive domain.'],
'bmo_2023_5e97b2':[5.5,'Translate swaps into connectivity of a square-sum graph; a descent to three small exceptional vertices identifies the sharp threshold.'],
'bmo_2023_3cf7b2':[5.5,'A longest path forces its last vertex to have degree two; reversing its terminal cycle rules out extra neighbours at a second vertex sharing a friend.'],
'bmo_2023_4f2ba4':[8,'The upper bound is an adaptive adversary argument using Hall deficiency and induction on the remaining query budget.'],
'bmo_2023_5e5234':[6.5,'Midpoint parallels reveal an auxiliary circle with centre X; a converse butterfly argument then turns the equal halves of CD into a perpendicular bisector.'],
'bmo_2023_fea5bb':[7,'A signed inversion about the orthocentre exchanges the difficult intersections with side midpoints; the Euler line then puts the remaining image on one simple circle.'],
'bmo_2023_e7a0b1':[7.5,'The construction requires multiple cyclicities, Simson or Miquel geometry, and either a harmonic-bundle argument or a final radical-centre configuration.'],
'bmo_2023_0bb743':[7.5,'The side conditions hide a congruent-triangle construction and an unexpected auxiliary circumcentre, followed by a complete-quadrilateral projection lemma.'],
'bmo_2023_82c96f':[6.5,'Coprimality and a quadratic residue give the necessary prime restriction; the reverse construction uses a square root of minus one and adjacent values of b,c to force the exact gcd.']
})
o['rou_2025_e406cf']=r'''Put $d_i=f_{10}(i,n)$. Fix $i<n$ and consider the set consisting of $A_i$ and its ten nearest neighbours. Every point in this eleven-point set is at distance at most $d_i$ from $A_i$. Let $A_j$ be its point with largest index. Then $j\geq11$, and its other ten points have indices below $j$.

If $j=i$, all ten nearest neighbours already occur before $i$, so
$$d_i=f_{10}(i,i-1)\geq f_{10}(n,i-1)\geq f_{10}(n,n)=d_n.$$
Otherwise each of the other ten points is within $2d_i$ of $A_j$, by the triangle inequality. Consequently
$$2d_i\geq f_{10}(j,j-1)\geq f_{10}(n,j-1)\geq f_{10}(n,n)=d_n.$$
The middle inequality is the hypothesis; the last uses the fact that adding more candidate points cannot increase the tenth smallest distance. Both cases prove the desired bound.'''
o['btw_2023_3ab5ed']=r'''Let $\Gamma$ be the circle through the six vertices. We show that an admissible point is fantastic precisely when the three diagonals $AD,BE,CF$ are concurrent.

Suppose the three circles through $P$ have a second common point $Q$. Let $S=AD\cap BE$, which is inside $\Gamma$ because these two diagonals cross inside a convex hexagon. The radical-axis theorem for $\Gamma,(ADP),(BEP)$ places $S$ on $PQ$. Since the circle $(CFP)$ also passes through $Q$, the radical-axis theorem with $\Gamma,(ADP),(CFP)$ puts $S$ on $CF$ too. The intersections are unique because $P$ is on none of the three diagonals.

Conversely, suppose the diagonals meet at $S$. Their common signed power in $\Gamma$ is negative. Each of $(ADP),(BEP),(CFP)$ therefore has the same negative power at $S$. On line $SP$, its other intersection is the point $Q$ uniquely determined by
$$\overline{SP}\,\overline{SQ}=\operatorname{Pow}_{\Gamma}(S).$$
Because the product is negative, $P$ and $Q$ lie on opposite sides of $S$ and are distinct. Thus all three circles contain exactly the same two points $P,Q$, as required.'''
o['btw_2023_2782d4']=r'''Reflect the circle $(PBC)$ in $BC$; the resulting circle is $(KBC)$. Let $G$ be the second intersection of line $KF$ with this reflected circle, counting $G=K$ in the tangent case. If $F=K$, the conclusion is already immediate.

Using directed angles, reflection in $BC$, cyclicity of $P,B,C,D$, and reflection of $P$ to $M$ in $AB$, we obtain
$$\angle BGF=\angle BGK=\angle BCK=\angle PCB=\angle PDB=\angle BDM=\angle BDF.$$
Thus $B,G,F,D$ are concyclic. In the tangent case the same first identity is the tangent-chord theorem. The symmetric argument using $P,B,C,E$ and the reflection to $L$ gives that $C,G,F,E$ are concyclic.

Now take the circles $(BGFD)$, $(CGFE)$ and $(BDCE)=(PBC)$. Their radical axes are respectively $GF$, $BD=AB$ and $CE=AC$. The latter two meet at $A$, so the radical-axis theorem gives $A\in GF=KF$. Hence $A,F,K$ are collinear.'''
s=json.loads((raw/'btw_2023_aa63a1.json').read_text())['solutions_markdown'][0]
o['btw_2023_aa63a1']='If two of $I,O,H$ coincide, the triangle is equilateral, so these cases cannot produce a scalene example.\n\n'+s.replace('$BH$ and $AO$','$BH$ and $BO$')
s=json.loads((raw/'btw_2023_f6a9be.json').read_text())['solutions_markdown'][0].replace('Shortlist: Keep confidential!','Let $O$ be the circumcentre, and let $M,N$ be the midpoints of $AB,AC$, respectively.')
s=s.replace('Notice that $\\triangle XAO$', 'Since $A,P,X,T$ and $A,Q,Y,T$ are cyclic, Step 2 gives $\\angle ATX=\\angle YTA$. The angle-bisector theorem in triangle $XTY$ therefore gives $TX/TY=AX/AY$ (with the external version if needed).\n\nNotice that $\\triangle XAO$')
o['btw_2023_f6a9be']=s
s=json.loads((raw/'bmo_2023_fea5bb.json').read_text())['solutions_markdown'][0]
s=s.replace('the inversion centered at $H$ which sends $A$ to $D$', 'the signed inversion centered at $H$ which sends $A$ to $D$ (its power is the directed product $\\overline{HA}\\,\\overline{HD}$; a negative power means ordinary inversion followed by a half-turn)')
o['bmo_2023_fea5bb']=s
s=json.loads((raw/'bmo_2023_82c96f.json').read_text())['solutions_markdown'][0]
s=s.replace('All positive integers with all prime divisors', 'All integers $n>1$ with all prime divisors').replace('Let us first prove', 'The value $n=1$ is impossible because $a+b+c\\geq3$.\n\nLet us first prove',1)
o['bmo_2023_82c96f']=s
s=json.loads((raw/'bmo_2023_423d32.json').read_text())['solutions_markdown'][0].replace('from the condition $f(0) = 0$', 'from the condition $f(f(0)) = 0$, obtained by setting $x=0$')
o['bmo_2023_423d32']=s
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));(p/'international-extra-solutions.json').write_text(json.dumps(o,ensure_ascii=False,indent=2))
