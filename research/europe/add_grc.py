import json
from pathlib import Path
p=Path(__file__).parent;R=json.loads((p/'reviews.json').read_text())
def put(s,d,t,ts,why,**kw):R['grc_2024_'+s]={'difficulty':d,'topic':t,'tags':ts.split(','),'reason':why,**kw}
put('10e94f',None,'Combinatorics','signed sums,sequences','Statement inspected, but no complete proof is available in the record; withheld pending a solution-based difficulty assessment.',quarantine=True)
put('16e818',4.5,'Geometry','circle angles,orthocentre,angle bisectors','A central-angle relation reveals that AB bisects the angle between two equal radii; this identifies two altitudes and hence the orthocentre.',statement=r'''An acute triangle $ABC$ has circumcircle $\omega$. A circle centred at $A$ meets the minor arcs $AB$ and $AC$ at $D,E$, respectively. Suppose $K=BE\cap CD$ also lies on the circle centred at $A$. Prove $AK\perp BC$.''',solution=r'''Use directed angles. Since $D,E,K$ lie on a circle centred at $A$,
$$\angle DAK=2\angle DEK.$$
Because $E,K,B$ are collinear and $A,B,D,E$ are cyclic, $\angle DEK=\angle DEB=\angle DAB$. Thus $AB$ bisects the angle between $AD$ and $AK$. As $AD=AK$, this bisector is perpendicular to $DK=DC$. Similarly $AC\perp EK=EB$. Therefore $K$ is the orthocentre of triangle $ABC$, and its third altitude is $AK\perp BC$.''',notes='The source transcription mislabels a central angle; the corrected argument is written explicitly.')
put('227681',2.5,'Algebra','sum of squares,reciprocals','Part A is the standard three-variable sum of squares, and the suggested reciprocal substitution proves part B directly.')
put('290a85',None,'Geometry','circumcentres,midpoints','Statement inspected; no complete source proof is present, so difficulty remains unassigned.',quarantine=True)
put('36735e',5,'Geometry','radical centre,power of a point,inversion','The three-circle radical centre identifies M on BD; equal inversion products then give the requested cyclic quadrilateral.',solution=r'''Let $r$ be the radius of $\Gamma_2$. The right angles at $E,F$ show that $B,E,D,F$ are cyclic; call this circle $\Gamma_3$. The radical axes of $(\Gamma_2,\Gamma_3)$ and $(\Gamma_1,\Gamma_2)$ are $EF$ and $KG$, meeting at $M$. Thus $M$ is on the third radical axis $BD$.

Use directed lengths on the relevant lines. Equality of the powers of $M$ with respect to $\Gamma_2$ and $\Gamma_3$ gives $MD^2-r^2=MD\cdot MB$, and hence $DM\cdot DB=r^2$. Similarly, equality of the powers of $N$ with respect to $\Gamma_2$ and $\Gamma_1$ gives $ND^2-r^2=ND\cdot NC$, hence $DN\cdot DC=r^2$. Therefore $DB\cdot DM=DC\cdot DN$, which by the converse of the secant-power theorem proves that $B,C,N,M$ are cyclic.''')
put('3ac059',None,'Geometry','tangent circles','The statement introduces an undefined circle kappa and the transcribed proof has missing angle labels; quarantined pending the original paper.',quarantine=True)
put('43eb6b',5,'Number Theory','Vieta jumping,Diophantine equations,infinite construction','Viewing the equation as a quadratic allows a root replacement; the construction must prove the new coordinate strictly exceeds the previous maximum.',solution=r'''Treat the equation as a quadratic in $z$:
$$z^2-(6xy-x-y)z+(x^2+y^2+xy)=0.$$
Its other root is $z'=6xy-x-y-z$, an integer, and $zz'=x^2+y^2+xy$. Starting from $(1,1,1)$, root replacement gives $(3,1,1)$ and then $(13,3,1)$.

Now suppose $x>y>z>0$ is a solution. Replace its smallest coordinate $z$ by $z'$. Then
$$z'-x=\frac{x(x-z)+y^2+xy}{z}>0.$$
Thus $(z',x,y)$ is a positive integer solution with a strictly larger maximum. Repeating produces infinitely many distinct solutions.''',notes='The exposition corrects an extra squared factor in the transcribed quadratic rearrangement.')
put('54bc9e',2.5,'Algebra','reciprocal inequalities,substitution','The denominators sum to twice the left denominator, so the second part is exactly the two-variable inequality supplied in part I.')
put('65644e',4.5,'Number Theory','Egyptian fractions,construction,common multiples','Taking a=(k+1)b parametrises a family; one must then choose a common multiple that makes more than 2024 distinct pairs integral.',solution=r'''Choose $n=\prod_{k=1}^{2025}k(k+1)$. For each $k=1,\ldots,2025$, set
$$b_k=n+\frac{n}{k(k+1)},\qquad a_k=(k+1)b_k.$$
These are positive integers. Direct calculation gives
$$\frac1{a_k-b_k}-\frac1{a_k}+\frac1{b_k}=\frac1{b_k}\left(1+\frac1{k(k+1)}\right)=\frac1n.$$
The pairs are distinct because their ratios $a_k/b_k=k+1$ are distinct. Hence this $n$ has at least 2025 solutions.''')
put('710a5d',3.5,'Algebra','quadratics,integer in interval','The discriminant is eight times a sum of squared differences; showing the two roots are more than one apart gives an integer between them.')
put('733b8c',3,'Combinatorics','double counting,Cauchy-Schwarz','Count triples as the sum of squared row sizes, then apply Cauchy-Schwarz and the immediate bound on distinct differences.')
put('76c633',None,'Algebra','functional inequalities','The available record has no proof; withheld until the strict-inequality condition can be fully assessed.',quarantine=True)
put('97ff5b',3,'Combinatorics','grid colouring,majority','A monochromatic 4-by-4 square contradicts one of the row or column majority counts; a small explicit colouring gives side 3.')
put('b671e8',2.5,'Number Theory','difference of squares,divisors','Completing the square leaves two factors of 135 and a short divisor enumeration.')
put('e889b7',5.5,'Number Theory','arithmetic progressions,gcd,products','Reducing each successive product ratio forces a divisibility lower bound on all alpha entries; multiplying those bounds exposes n factorial.',solution=r'''Write $n=\nu$, the first product as $u$, and the common difference as $d>0$. Let $g=\gcd(u,d)$, and put $u=gv$, $d=gt$, where $v,t$ are coprime positive integers. For each $i=1,\ldots,n$,
$$\frac{\beta_i}{\alpha_i}=\frac{v+it}{v+(i-1)t}.$$
The numerator and denominator are coprime, so $v+(i-1)t$ divides $\alpha_i$. Multiplying gives
$$gv=u=\prod_i\alpha_i\ge\prod_{i=1}^n(v+(i-1)t),$$
so $g\ge\prod_{i=1}^{n-1}(v+it)\ge2\cdot3\cdots n=n!$. Hence $d=gt\ge n!$.

Equality is possible: choose $\alpha_i=i$ and $\beta_i=i+1$. The successive products are $n!,2n!,\ldots,(n+1)n!$, an arithmetic progression with difference $\boxed{n!}$.''')
for s,r in R.items():
 if s.startswith('grc_2024_'):
  raw=json.loads((p/(s+'.json')).read_text());r['competition']='Greek IMO Selection Test' if raw['competition']=='IMO TST' else raw['competition']
(p/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
