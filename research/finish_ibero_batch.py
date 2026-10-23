from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');raw=p/'international-raw';r=json.loads((p/'international-reviews.json').read_text());o=json.loads((p/'international-extra-solutions.json').read_text())
slug='ibero_2000_official_p2'
statement=r'''Two circles with centres $O_1,O_2$ meet at $M,N$. Their common external tangent nearer $M$ touches them at $A,B$, respectively. Let $C$ be the point on the second circle diametrically opposite $B$. Let $D$ be the intersection of $O_1O_2$ with the line through $B$ perpendicular to $AM$. Prove that $M,D,C$ are collinear.'''
solution=r'''Choose coordinates with the common tangent as the horizontal axis and both centres above it:
$$A=(0,0),\quad B=(b,0),\quad O_1=(0,r),\quad O_2=(b,s),\quad C=(b,2s),$$
where $b,r,s>0$. Write $M=(x,y)$. Its two circle equations give
$$x^2+y^2=2ry,\qquad(x-b)^2+y^2=2sy,$$
and hence $2bx=b^2+2(r-s)y$.

Consider the point
$$D'=\left(b-\frac{2sy}{b},\frac{2sx}{b}\right).$$
Its displacement from $B$ has zero dot product with $(x,y)$, so $BD'\perp AM$. Substituting $2bx=b^2+2(r-s)y$ shows
$$b(D'_y-r)=(s-r)D'_x,$$
which is the equation of $O_1O_2$. Thus $D'=D$.

Moreover $\overrightarrow{CD}=(2s/b)(-y,x-b)$ is perpendicular to $\overrightarrow{BM}=(x-b,y)$. Since $BC$ is a diameter, $CM\perp BM$ too. Therefore $C,D,M$ lie on the same line.'''
d={'id':slug,'competition_code':'Ibero-American Mathematical Olympiad','competition':'Ibero-American Mathematical Olympiad','year':2000,'problem_number':'2','primary_domain':'Geometry','topics':[['Geometry','Circles'],['Geometry','Coordinates']],'problem_markdown':statement,'solutions_markdown':[solution],'officialSourceUrl':'https://www.obm.org.br/content/uploads/2018/01/ibero2000.pdf','officialSolutionUrl':'https://www.obm.org.br/content/uploads/2018/01/ibero2000.pdf','reviewNote':'Statement translated from the official OBM archive. Embedded solution is an independently derived coordinate proof; the source PDF contains the questions.'}
(raw/(slug+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2));r[slug]=[5,'Putting the common tangent on an axis makes the circle equations linear after subtraction; a rotated vector identifies the required intersection and the diameter supplies the final perpendicularity.']
r['ibe_2001_461dd2']=[5,'Copy the opponent’s previous acceleration while maintaining a unit velocity offset; the relative position then advances diagonally through every square by coprimality of the board dimensions.']
o['ibe_2001_461dd2']=r'''The first player can always win. Treat positions as elements of $\mathbb Z/2000\mathbb Z\times\mathbb Z/2001\mathbb Z$, and write velocities as integer pairs. Let the second player's velocity on turn $j$ be $v_j$, with $v_0=(0,0)$.

On their turn $j$, the first player chooses velocity
$$u_j=v_{j-1}+(1,1).$$
The initial velocity is $(1,1)$, which is legal. Thereafter
$$u_j-u_{j-1}=v_{j-1}-v_{j-2},$$
so each change in the first player's velocity is exactly the opponent's previous legal change, hence is legal too.

Let $A_j$ be the first player's position after turn $j$ and $B_j$ the second player's position after turn $j$. The relative position at the moment capture is checked satisfies
$$A_j-B_{j-1}=A_0-B_0+j(1,1).$$
Since $2000$ and $2001$ are coprime, the Chinese remainder theorem gives a positive $j$ satisfying both coordinate congruences $A_0-B_0+j(1,1)=(0,0)$. At that turn, or earlier, the first player captures the second.'''
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));(p/'international-extra-solutions.json').write_text(json.dumps(o,ensure_ascii=False,indent=2))
# Keep the unreviewed source record's original text for audit, but record the corrected official question separately.
corrections={'ibe_2000_73ec10':{'officialStatement':r'A convex hexagon is called beautiful if four of its diagonals have length one and together have all six vertices as endpoints. (a) For each real $0<k\leq1$, construct a beautiful hexagon of area $k$. (b) Prove that every beautiful hexagon has area less than $3/2$.','sourceUrl':'https://www.obm.org.br/content/uploads/2018/01/ibero2000.pdf','status':'statement-verified-solution-pending'},'ibe_2001_94c52e':{'officialStatement':r'Prove that five congruent squares, each with side length strictly less than $1/2$, cannot cover a unit square.','sourceUrl':'https://www.obm.org.br/content/uploads/2018/01/ibero2001.pdf','status':'statement-verified-solution-pending'}}
(p/'international-pending-corrections.json').write_text(json.dumps(corrections,ensure_ascii=False,indent=2))
