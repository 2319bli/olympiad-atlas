import json,pathlib
P=pathlib.Path('/workspace/sites/olympiad-atlas/research/asia'); RAW=P.parent/'raw'/'asia'
reviews=json.loads((P/'reviews.json').read_text());manifest=json.loads((P/'manifest.json').read_text())
rows=[]
def add(grade,num,rating,topic,reason,statement,solution,comment,note=''):
 rows.append((grade,num,rating,topic,reason,statement,solution,comment,note))
add(9,1,4,'Number Theory','The ratio a/b turns both equations into the same cubic; a monotonicity or factorization argument then identifies it with c.',r'''Positive integers $a,b,c$ satisfy $a^2=b^3+ab$ and $c^3=a+b+c$. Prove that $a=bc$.''',r'''Put $t=a/b$. Dividing the first equation by $b^2$ gives $b=t^2-t$, so $t>1$. The second equation now yields
$$c^3-c=a+b=b(t+1)=(t^2-t)(t+1)=t^3-t.$$
Therefore
$$(c-t)(c^2+ct+t^2-1)=0.$$
The second factor is positive because $t>1$ and $c>0$. Hence $c=t=a/b$, proving $a=bc$.''',5472)
add(9,2,5.5,'Combinatorics','Parity of the board determines whether rotations swap colors; the odd case needs a connected-shape bounding-box argument and sharp obstructing examples.',r'''An $n\times n$ board, $n>1$, is colored as a chessboard. A shape is a nonempty set of squares; it is connected when any two squares can be joined within it by side-adjacent steps. Copies may be obtained by translations and rotations through multiples of $90^\circ$, staying inside the board. Find the greatest $k$ such that every connected $k$-square shape has both a copy with more white than black squares and a copy with more black than white squares.''',r'''If $n$ is even, a quarter-turn swaps the two colors. Every shape of odd size has an unequal color count, so $k=n^2-1$ works. The only larger possibility is the whole board, which has equal counts. Thus the answer is $n^2-1$.

Suppose $n$ is odd. We claim the answer is $2n-3$. A connected shape whose bounding box has width $w$ and height $h$ uses at least $w+h-1$ squares: a spanning tree must contain at least $w-1$ horizontal and $h-1$ vertical edges. A shape with $2n-3$ squares therefore cannot span all rows and all columns. It can be translated one square in some direction, reversing every color. Its size is odd, so this supplies both required imbalances.

For $k=2n-2$, use the first row and first column, omitting their shared corner and retaining the other $2n-2$ squares as an L with the corner instead included and one endpoint removed. More explicitly, take the entire first row and the first $n-2$ additional squares of the first column. The two arms together have equal color counts, so every copy is balanced.

For $k\ge2n-1$, start with the entire first row and first column and add squares while maintaining connectedness until size $k$. Its bounding box is the whole board, so no nonzero translation fits. Quarter-turns preserve chessboard colors when $n$ is odd; hence copies cannot have opposite imbalances. This excludes all larger $k$.''',5473)
add(9,3,6.5,'Geometry','A circle centered at the base midpoint encodes an isogonal relation; a disciplined coordinate calculation converts the two parallel lines to a circumcenter-tangent collinearity.',r'''Let acute triangle $ABC$ satisfy $AB\ne AC$, with circumcenter $O$ and $M$ the midpoint of $BC$. The tangent at $A$ to its circumcircle meets line $BC$ at $D$. The circle centered at $M$ through $A$ meets lines $AB,AC$ again at $K,L$. Define $X$ by $BX\parallel MK$ and $CX\parallel ML$. Prove that $X,D,O$ are collinear.''',r'''Choose $M=(0,0)$, $B=(-1,0)$, $C=(1,0)$, $A=(u,v)$ and put $s=u^2+v^2$. The assumptions give $u\ne0$, $v>0$, and $s>1$. The circle centered at $M$ is $x^2+y^2=s$.

Intersecting it with the two side lines gives
$$K=\frac{(-u(s+1)-2s,\ (1-s)v)}{s+2u+1},\qquad
L=\frac{(-u(s+1)+2s,\ (1-s)v)}{s-2u+1}.$$
Solve the two parallel-line equations $X=B+\lambda K=C+\mu L$. Equality of the second coordinates gives $\lambda/(s+2u+1)=\mu/(s-2u+1)$; equality of the first makes their common value $-1/(2s)$. Thus
$$X=\left(\frac{u(s+1)}{2s},\frac{v(s-1)}{2s}\right).$$
The circumcenter and tangent intercept are
$$O=\left(0,\frac{s-1}{2v}\right),\qquad D=\left(\frac{s+1}{2u},0\right).$$
Substitution into the intercept equation of $OD$ gives
$$\frac{X_x}{D_x}+\frac{X_y}{O_y}=\frac{u^2}{s}+\frac{v^2}{s}=1.$$
Therefore $X$ lies on $OD$.''',5474)
add(9,4,4,'Number Theory','A cyclic weighted sum collapses the three divisibility conditions to a linear sum, which a size bound then rules out.',r'''Show that for positive integers $a,b,c$, the number $a^2+b^2+c^2$ cannot divide all three numbers $a^3b+1$, $b^3c+1$, $c^3a+1$.''',r'''Suppose it divides all three, and write $N=a^2+b^2+c^2$. Multiplying the three expressions by $c,a,b$, respectively, and adding gives
$$N\mid abcN+a+b+c,$$
so $N\mid a+b+c$. But $0<a+b+c\le N$, with equality only when $a=b=c=1$. Divisibility forces this equality case. There $N=3$ while each original expression equals $2$, a contradiction.''',5475)
add(9,5,6,'Geometry','The two right-angle bisectors fix useful coordinates; identifying the base midpoint as the center requires relating a second circle intersection to those coordinates.',r'''All angles of triangle $ABC$ exceed $45^\circ$, and $AB\ne AC$. Let $AD$ be its altitude. The internal bisector of $\angle ADB$ meets the circle with diameter $AC$ again at $P$; the internal bisector of $\angle ADC$ meets the circle with diameter $AB$ again at $Q$. Line $AP$ meets the latter circle again at $R$. Prove that the circumcenter of $PQR$ lies on $BC$.''',r'''Take $D=(0,0)$, $A=(0,h)$, $B=(-b,0)$ and $C=(c,0)$. The angle conditions give $h>b,c>0$. Set $u=(h-c)/2$ and $v=(h-b)/2$. Substituting the bisector lines $y=-x$ and $y=x$ into the diameter circles gives
$$P=(-u,u),\qquad Q=(v,v).$$
The base midpoint is $M=(v-u,0)$. Both $MP^2$ and $MQ^2$ equal $u^2+v^2$.

It remains to put $R$ on the circle
$$\Sigma:\ x^2+y^2-2(v-u)x-2uv=0.$$
The circle with diameter $AB$ is $x^2+y^2+bx-hy=0$. On line $AP$, write $(x,y)=(-ut,h-t(h-u))$. Besides $t=0$ at $A$, its intersection with this diameter circle has
$$t=\frac{h(h-u)+bu}{u^2+(h-u)^2}.$$
The difference between the equation of $\Sigma$ and that diameter circle, evaluated at this point, is
$$h^2-2uv-t\bigl(h^2-u(h+c)\bigr)=0,$$
because $h^2-u(h+c)=u^2+(h-u)^2$ and $h^2-2uv=h(h-u)+bu$. Hence $R\in\Sigma$, whose center is $M\in BC$.''',5476)
add(9,6,5.5,'Algebra','Consecutive recurrence equations force all two-step differences to have one sign; positivity rules out descent and a power inequality gives a uniform bound.',r'''Let $m\ge3$ be an integer and let $(a_n)_{n\ge1}$ be an infinite sequence of positive integers satisfying
$$a_{n+2}=2\sqrt[m]{a_{n+1}^{m-1}+a_n^{m-1}}-a_{n+1}.$$
Prove that $a_1<2^m$.''',r'''Raise the recurrence to the $m$th power and compare adjacent instances:
$$(a_{n+3}+a_{n+2})^m-(a_{n+2}+a_{n+1})^m
=2^m(a_{n+2}^{m-1}-a_n^{m-1}).$$
Since positive powers are strictly increasing, $a_{n+3}-a_{n+1}$ has the same sign as $a_{n+2}-a_n$. Hence all two-step differences have the same sign. They cannot be negative, as that would give an infinite strictly decreasing sequence of positive integers along each parity. Thus $a_{n+2}\ge a_n$.

Put $s_n=a_n+a_{n+1}$. Then $s_{n+1}\ge s_n$, while
$$s_{n+1}^m=2^m(a_n^{m-1}+a_{n+1}^{m-1})<2^m s_n^{m-1}.$$
The strict inequality uses $m-1\ge2$ and positivity. Therefore $s_n^m<2^m s_n^{m-1}$, so $s_n<2^m$. In particular $a_1<s_1<2^m$.''',5477,'Also Grade 10 Problem 5 and Grade 11 Problem 5; merged identical appearances.')
add(10,1,5.5,'Geometry','The tangent-chord relation identifies equal angles, and two right triangles supply the proportional sides for a final similarity.',r'''In acute triangle $ABC$, let $AD$ be the altitude and $H$ the orthocenter. A circle through $A,B$ is tangent to $AC$ at $A$, and $BE$ is its diameter. Lines $BH,AH$ meet this circle again at $K,L$. Let $T=EK\cap AB$. Prove that $\angle BDK=\angle BLT$.''','',5478,'Also Grade 11 Problem 1; merged identical appearance. The linked discussion supplies worked geometric solutions.')
add(10,2,6,'Number Theory','Choose an exponent avoiding zero factors, then freeze every p-adic valuation along a congruence progression while the exponent grows.',r'''Let $p\ge3$ be prime and $d$ a positive integer. Prove that there is a positive integer $n$ coprime to $d$ such that
$$p^n\nmid\prod_{1\le i<j<p}\left(i^{n+j}-j^{n+i}\right).$$''',r'''For fixed $i<j$, the equation $i^{n+j}=j^{n+i}$ is equivalent to $(i/j)^n=j^i/i^j$, and has at most one real solution $n$. There are only finitely many pairs. Hence choose a positive $n_0$ coprime to $d$ for which no factor vanishes.

Let $e$ be the sum of the $p$-adic valuations of the factors at $n_0$, and choose $M$ larger than every individual valuation. For any positive integer $t$, set
$$n=n_0+t\,d(p-1)p^M.$$
Then $\gcd(n,d)=1$. Euler's theorem modulo $p^M$ shows that each factor at $n$ is congruent to its factor at $n_0$ modulo $p^M$, since all bases lie between $1$ and $p-1$. As the original factor's valuation is less than $M$, its valuation is unchanged. Thus the product always has valuation $e$. Choose $t$ large enough that $n>e$. The product is then not divisible by $p^n$.''',5479,'Also Grade 11 Problem 2; merged identical appearance.')
add(10,3,8,'Algebra','A lower-bound dichotomy and an iterated multiplicative orbit are needed to force either a constant function or the square function.','','',5480,'Also Grade 11 Problem 3; above target difficulty.')
add(10,4,3.5,'Combinatorics','Enumerate unit squares until a positive circle query confines the point to four vertices, then use two shifted square queries to distinguish them.','','',5481,'Also Grade 11 Problem 4; below target difficulty.')
add(10,6,8.5,'Geometry','The solution needs multiple polar incidences and a harmonic-pencil argument, or a long inversion and symmedian construction.','','',5483,'Also Grade 11 Problem 6; above target difficulty.')
for grade,num,rating,topic,reason,statement,solution,comment,note in rows:
 slug=f'kaz_2024_national_g{grade}_q{num}'
 raw={'country':'Kazakhstan','competition':f'Kazakhstan National Mathematical Olympiad — Grade {grade}','year':2024,'section':f'Grade {grade}','problem_number':str(num),'problem_markdown':statement or f'Grade {grade} Problem {num}; see source','solutions_markdown':[solution],'primary_domain':topic,'topics':[],'booklet_title':'Matol.kz: Kazakhstan National Mathematical Olympiad 2024','sourceDataset':'Matol.kz national olympiad archive','sourceLicense':'Mathematical statement translated and solution independently rewritten; original source linked.'}
 (RAW/(slug+'.json')).write_text(json.dumps(raw,ensure_ascii=False,indent=2))
 review={'difficulty':rating,'reason':reason,'sourceUrl':f'https://matol.kz/comments/{comment}/show','solutionUrl':f'https://matol.kz/comments/{comment}/show','note':note+' Reviewed all six tasks in each of the 2024 Grade 9, 10 and 11 archive pages; identical tasks merged.'}
 if solution:review['solutionOverride']=solution
 else:review['solutionKind']='source-link'
 reviews[slug]=review
 if slug not in {x[0] for x in manifest}:manifest.append([slug,'kazakhstan-matol',2024,raw['competition'],0,0,str(num)])
(P/'reviews.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2));(P/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Kazakhstan reviewed',len(rows),'distinct tasks / 18 appearances;',sum(4<=r[2]<=7 for r in rows),'included')
