import json,re
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text())
def add(s,d,t,tags,reason,solution=None,statement=None,q=False):
 id='ukr_2023_'+s;r[id]={'difficulty':d,'topic':t,'tags':tags,'reason':reason}
 if solution:r[id]['solution']=solution
 if statement:r[id]['statement']=statement
 if q:r[id]['quarantine']=True
add('881db3',1.5,'Number theory',['parity'],'An odd product of edge sums forces every edge product even, so their total cannot be odd.')
add('1f197d',4,'Combinatorics',['adaptive strategy','averaging'],'Repeatedly predict losses for a minimum-score player; odd residual degrees give strict improvement.')
add('e537fc',4.5,'Algebra',['fractional parts','radicals'],'Pin down the integer parts and obtain incompatible bounds on the ratio x/y.',r'''Suppose $x<y$. Then $y<\sqrt{y^2+2x}<y+1$, so the second condition gives $x>2y/3$. Since $y\ge x+1$, the first radical is larger than $x+1$. Since $2y<3x<4x+4$, it is smaller than $x+2$. Thus the first condition gives
$$x^2+2y>(x+5/3)^2,$$
so $y>5x/3$. Combining yields $x>10x/9$, impossible. Interchanging $x,y$ handles the other unequal ordering.''')
add('12836f',4.5,'Geometry',['circle tangency','angle bisector theorem'],'The central-angle relation gives a radius ratio; tangency turns it into an angle-bisector condition.',statement=r'In rhombus $ABCD$, a point $T$ satisfies $\angle ATC+\angle BTD=180^\circ$, and circles $ATC$ and $BTD$ are tangent. Prove that $T$ has equal distances from the two diagonal lines.')
add('395090',2.5,'Algebra',['monotonicity'],'All entries are nonnegative; a+sqrt(a)=S is strictly increasing, so every entry must coincide.')
add('ef78ef',2.5,'Geometry',['parallelograms','auxiliary intersection'],'Extending two sides produces a parallelogram and an isosceles triangle, immediately giving the length identity.')
add('0d264a',5,'Combinatorics',['graph complements','extremal construction'],'A four-vertex obstruction gives the upper bound, and a path ending in a triangle attains it.',r'''Pass to the complementary graph: at each step delete its unique vertex of minimum degree. With two vertices this is impossible. If four vertices $A,B,C,D$ remain and $D$ can be deleted, then it is impossible to delete $C$ next. Indeed, in a three-vertex graph a unique minimum-degree vertex must be isolated while the other two are adjacent. Thus $C$ has degree at most one before $D$ is deleted. For $D$ to have strictly smaller degree it must have degree zero, leaving $C$ also with degree zero, a contradiction.
For $n\ge4$, at least three vertices therefore remain. Equality is achieved by the complement consisting of the path $A_1A_2\cdots A_n$ with the additional edge $A_{n-2}A_n$: successive unique leaves $A_1,\ldots,A_{n-3}$ can be deleted, leaving a triangle. Hence the maximum is $n-3$.
For $n=3$, take a complementary graph with one edge and one isolated vertex. Exactly one deletion is possible, so the maximum is $1$.''',r'An undirected flight network has $n\ge3$ airports. Each day, close the airport whose number of flights is strictly greater than that of every other remaining airport, and remove its flights. If there is no such airport, stop. Over all starting networks, what is the maximum number of days?')
r['ukr_2023_0d264a']['notes']='The strict uniqueness condition, omitted from the MathNet English transcription, is verified against the original Ukrainian Grade 8 paper: https://mathedu.kh.ua/wp-content/uploads/2023/04/%D0%92%D1%81%D0%B5%D1%83%D0%BA%D1%80-2023_8-%D0%BA%D0%BB%D0%B0%D1%81.pdf'
add('c1d545',4,'Number theory',['modular arithmetic','merging induction'],'Merging a zero residue, or the smallest and largest nonzero residues, preserves distinctness.')
add('89fe63',3.5,'Algebra',['cyclic sequences','maximum principle'],'A maximum propagates two positions at a time; alternating values handle even n.')
add('3b672d',4,'Number theory',['cyclic divisibility','telescoping'],'Sum the successor bounds around the cycle and exploit the final strict multiple; consecutive values attain the bound.')
add('e3eb6e',None,'Geometry',['radical axes'],'The concurrency claim needs a parallel-line exception: an isosceles acute triangle gives three parallel lines. This omission persists in the original paper; quarantined rather than silently changing the problem.',q=True)
add('39b9e7',6.5,'Algebra',['fractional parts','sharp bounds'],'The golden-ratio bound needs both an integer-part argument and an asymptotic extremal construction.',r'''Put $c=(\sqrt5-1)/2$, so $c(c+1)=1$. Suppose $x<y$ and both fractional parts are at least $c$. Since $y<\sqrt{y^2+2x}<y+1$, we obtain $2x\ge2cy+c^2$, hence $x>cy$. Also $y\ge x+1$, while $2y<2x/c<4x$, so
$$x+1<\sqrt{x^2+2y}<x+2.$$
The first fractional-part condition now yields $2y\ge2(c+1)x+(c+1)^2$, hence $y>(c+1)x$. Multiplication contradicts $c(c+1)=1$. Thus the minimum is always strictly below $c$.
To prove sharpness, let $x$ tend through positive integers and put $y=\lfloor(c+1)x\rfloor$. For sufficiently large $x$, the two radicals lie between $x+1,x+2$ and $y,y+1$, respectively. Rationalizing shows
$$\sqrt{x^2+2y}-x\longrightarrow c+1,\qquad\sqrt{y^2+2x}-y\longrightarrow\frac1{c+1}=c.$$
Their fractional parts both tend to $c$. No smaller constant works, so the answer is $c$.''',r'Find the least real $C$ such that, for all distinct positive integers $x,y$, $$\min\bigl(\{\sqrt{x^2+2y}\},\{\sqrt{y^2+2x}\}\bigr)<C,$$ where $\{t\}=t-\lfloor t\rfloor$.')
add('990e8c',5,'Geometry',['midpoints','cyclic quadrilaterals'],'Introduce two segment midpoints and prove that all five relevant points lie on one diameter circle.',statement=r'Inside triangle $ABC$, let $O$ satisfy $\angle BOC=90^\circ-\angle BAC$. Rays $BO,CO$ meet $AC,AB$ at $K,L$. Choose $K_1\in LC$, $L_1\in BK$ with $BK_1=K_1K$ and $CL_1=L_1L$. If $M$ is the midpoint of $BC$, prove $\angle K_1ML_1=90^\circ$.')
add('f5d663',3.5,'Combinatorics',['extremal element','induction'],'The largest number belongs to at most one power-of-two pair; induction and a star construction give n−1.')
add('12054b',5,'Combinatorics',['perfect matchings','extremal graphs'],'Each pair of matching edges allows at most two cross-edges; a triangular construction has a forced matching.')
# Restore duplicate appearances suppressed by the source corpus.
for id,orig,num in [('ukr_2023_grade8_5','ukr_2023_395090','8-5'),('ukr_2023_grade8_6','ukr_2023_ef78ef','8-6')]:
 d=json.loads((p/(orig+'.json')).read_text());d['section']='Fourth Round, April 2023 - Second Day - 8th Grade';d['problem_number']=num;(p/(id+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2));r[id]=dict(r[orig]);r[id]['duplicateOf']=orig;r[id]['reason']='Same problem as another grade on the 2023 national paper; '+r[orig]['reason']
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
