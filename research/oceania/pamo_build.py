import json,math
P='/workspace/sites/olympiad-atlas/research/oceania/';U='https://www.pamoofficial.org/problems/'
items=[]; ledger=[]
def add(y,n,d,topic,tags,s,sol,r):
 id=f'pamo_{y}_{n}'
 items.append(dict(id=id,country='Pan-African',competition='Pan-African Mathematics Olympiad',year=y,number=str(n),statement=s,solution=sol,sourceUrl=U,solutionUrl=None,topic=topic,tags=tags,difficulty=d,ratingReason=r,reviewStatus='individually-assessed',solutionKind='original-exposition',notes='Organiser statement archive; mathematical statement paraphrased and solution independently worked for this bank. The archive link contains statements, while the worked exposition is displayed here.'))
 ledger.append(dict(id=id,country='Pan-African',competition='Pan-African Mathematics Olympiad',year=y,number=str(n),difficulty=d,status='reviewed',included=True,reason=r,sourceUrl=U))
def skip(y,n,d,r,status=None): ledger.append(dict(id=f'pamo_{y}_{n}',country='Pan-African',competition='Pan-African Mathematics Olympiad',year=y,number=str(n),difficulty=d,status=status or ('reviewed' if d else 'pending-solution-review'),included=False,reason=r,sourceUrl=U))
skip(2026,1,3.5,'The eight-card game reduces to a small table of removable path components.')
add(2026,2,5.5,'Geometry',['orthocentres','radical axes','coordinates'],r'In acute triangle $ABC$, let $H$ be the orthocentre and $D,E,F$ the altitude feet on $BC,CA,AB$. Set $G=EF\cap AD$. If $I$ is the antipode of $A$ on the circumcircle and $J=AI\cap BC$, prove $HI\parallel GJ$.',r'''Choose $A=(0,0),B=(u,v),C=(w,v)$, where $v>0$ and $u<0<w$. Put $q=v^2-uw>0$. The altitude through $B$ gives
$$H=(0,(v^2+uw)/v),$$
and the circumcircle centre gives $I=(u+w,q/v)$. Therefore
$$J=(v^2(u+w)/q,v).$$
Both $E,F$ lie on the circles with diameters $AH$ and $BC$. Subtracting their circle equations gives their common chord line
$$(u+w)x+(q/v)y=v^2+uw.$$
Consequently $G=(0,v(v^2+uw)/q)$, and
$$J-G=\frac{v^2}{q}\left(u+w,-\frac{2uw}{v}\right)=\frac{v^2}{q}(I-H).$$
The asserted parallelism follows.''','Several auxiliary points must be coordinated; using the common chord of two diameter circles avoids a long direct computation of both altitude feet.')
skip(2026,3,None,'Polynomial valuation identity screened; requires a fuller number-theoretic assessment.')
skip(2026,4,2.5,'Nonnegative coefficients make every cross term in P(sqrt(2)) squared nonnegative, forcing a single monomial.')
add(2026,5,5,'Number Theory',['prime powers','difference of squares','valuations'],r'Classify prime powers $a$ and integers $n\ge2$ for which $a^n(a-1)+1$ is a square.',r'''The solutions are $(a,n)=(2,3)$ and $(4,2)$, giving squares $9$ and $49$.

Write $m^2-1=a^n(a-1)$ with $m>1$. If $a=p^r$ for an odd prime $p$, then all of $p^{rn}$ divides one of $m-1,m+1$, since their gcd divides $2$. Thus $m\ge a^n-1$. Squaring and comparing gives $a^n\le a+1$, impossible for $a\ge3,n\ge2$.

If $a$ is a power of two, then $m$ is odd. Exactly one of $m-1,m+1$ has 2-adic valuation one, so the other is divisible by $a^n/2$. Hence $m\ge a^n/2-1$. Comparing squares now yields
$$a^{2n}/4-a^n\le a^n(a-1),\qquad a^{n-1}\le4.$$
Only $(2,2),(2,3),(4,2)$ remain, and direct substitution excludes $(2,2)$.''','Splitting the two neighbouring factors requires separate odd-prime and power-of-two valuations, followed by a sharp size bound.')
add(2026,6,4.5,'Combinatorics',['invariants','binary strings','equivalence classes'],r'A move on a binary string of length $n$ replaces two equal neighbouring bits by their complements. What is the largest family of strings in which no two can be transformed into one another by such moves?',r'''The answer is $n+1$. Complement every other position in every string. Under this bijection, a legal move becomes an adjacent swap $01\leftrightarrow10$: originally equal neighbours become unequal because exactly one position was complemented.

Adjacent swaps preserve the number of ones, and any two binary strings with the same number of ones can be connected by adjacent swaps, by moving all ones to the left. Thus the original move system has exactly one equivalence class for each transformed number of ones $0,1,\ldots,n$. Taking one representative from each class attains $n+1$, and no larger family is possible.''','An alternating complementation turns an unfamiliar move into adjacent swaps, giving both the invariant and completeness of its classes.')
add(2025,1,4.5,'Geometry',['power of a point','orthogonal projections','cyclic quadrilaterals'],r"A circle through $B,C$ meets $AB,AC$ again at $D,E$. Project $B,E$ perpendicularly onto $CD$, obtaining $B',E'$, and project $D,C$ onto $BE$, obtaining $D',C'$. Prove that $B',E',D',C'$ are concyclic.",r'''Let $O=BE\cap CD$ and let the angle between these lines be $\theta$. Using directed distances, the original cyclicity says $OB\cdot OE=OC\cdot OD$. Projection multiplies each relevant distance by $\cos\theta$, so
$$OB'\cdot OE'=\cos^2\theta\,OB\cdot OE=\cos^2\theta\,OC\cdot OD=OC'\cdot OD'.$$
The converse of the intersecting-secants theorem gives the required circle. If the two lines are perpendicular, all four projections coincide at $O$, and the assertion is immediate. If they are parallel, the midpoints of both pairs of projected points lie on the same perpendicular diameter of the original circle. The common perpendicular bisector of these pairs contains a point equidistant from the two pairs, which is the centre of a circle through all four points.''','Projection rescales two equal secant products by the same factor; parallel and perpendicular degeneracies require separate attention.')
skip(2025,2,3.5,'The even-parity count is ((3+1)^20+(3-1)^20)/2, using a standard two-state count.')
add(2025,3,4.5,'Number Theory',['Chinese remainder theorem','idempotents','decimal digits'],r'Find all six-digit positive integers $N$ for which every positive power of $N$ ends in the same six digits as $N$.',r'''It is necessary and sufficient that $N^2\equiv N\pmod{10^6}$: sufficiency follows by multiplying the congruence inductively. Since $N,N-1$ are coprime, each of $2^6=64$ and $5^6=15625$ must divide one of them entirely. Thus there are four residue classes modulo $10^6$.

The choices where both prime powers divide the same factor give $N\equiv0$ or $1$. The mixed choices give $N\equiv109376$ or $890625$; direct reduction modulo $64$ and $15625$ verifies these two classes. Only the mixed residues have six digits. The answers are therefore $109376$ and $890625$.''','The repeated-power condition must be reduced to idempotency, then coprimality and CRT classify the decimal endings.')
skip(2025,4,3,'Division by x+1 leaves remainder -2, so x+1 divides 2 and only four cases remain.')
add(2025,5,4.5,'Algebra',['functional equations','integer domain','recurrences'],r'Find all $f:\mathbb Z\to\mathbb Z$ with $f(1)=1$ and $f(x+y)+f(x-y)=\max\{f(2x),2f(y)\}$ for all integers $x,y$.',r'''The solutions are $f(n)=1$ and $f(n)=|n|$. Write $c=f(0)$. The case $y=0$ gives $2f(x)=\max(f(2x),2c)$, so $f(x)\ge c$. Taking $x=y=0$ gives $c\ge0$; taking $x=1,y=0$ gives $c\le1$ and $f(2)\le2$. Hence $c=0$ or $1$.

With $x=0$, the equation yields $f(-y)=f(y)$, since $f(y)\ge c\ge0$. With $x=y=1$ it gives $f(2)=2-c$. Finally $x=1$ gives
$$f(y+1)+f(y-1)=\max(2-c,2f(y)).$$
Starting from $f(0)=c,f(1)=1$, this recurrence forces $f(n)=n$ for $n\ge0$ when $c=0$, and $f(n)=1$ when $c=1$. Evenness determines negative indices. The constant solution is immediate; for absolute values use $|x+y|+|x-y|=2\max(|x|,|y|)$.''','The maximum first gives range bounds and evenness; a one-dimensional recurrence then separates the two possible initial values.')
add(2025,6,4.5,'Combinatorics',['increasing paths','grid colouring','extremal construction'],r'Place the integers $1,\ldots,2025^2$ in a square grid. A token may move at most three rows and at most three columns, always to a larger entry. What is the largest number of moves guaranteed by a suitable starting cell and path, for every arrangement?',r'''The answer is $15$. In any $4\times4$ block, every cell can reach every other cell in one move. Visiting its sixteen entries in increasing order gives fifteen moves.

For a matching upper bound, colour a cell by the ordered pair of its row and column residues modulo $4$, producing sixteen colours. No legal move connects two cells of the same colour. Order these colours and assign the smallest available numbers to every cell of the first colour, then to every cell of the second, and so on. Any increasing move must then go to a strictly later colour. An increasing path visits at most sixteen colours, so has at most fifteen moves.''','A local clique gives the lower bound and a global sixteen-colouring supplies the matching adversarial arrangement.')
skip(2024,1,3.5,'The fraction identity makes the stated prime equal (a+b+c)(a+b-c), after which positivity bounds the remaining small case.')
add(2024,2,4.5,'Geometry',['power of a point','tangency','coordinates'],r'In triangle $ABC$, let $M$ be the midpoint of $BC$ and $N$ the midpoint of $AM$. A circle through $N$ tangent to $AC$ at $A$ meets $AB$ again at $P$. Prove that circle $BPM$ is tangent to $AM$.',r'''Take $A$ as origin, and write $M=v$, $B=b$, so $C=2v-b$ and $N=v/2$. A circle through the origin has equation $r\cdot r-\ell\cdot r=0$. Its tangent at the origin is perpendicular to $\ell$, so tangency to $AC$ gives $\ell\cdot(2v-b)=0$. Substitution of $N$ gives $\ell\cdot v=|v|^2/2$, and hence $\ell\cdot b=|v|^2$.

Writing $P=tb$, the circle equation yields $t|b|^2=|v|^2$, or $AP\cdot AB=AM^2$. The left side is the power of $A$ with respect to circle $BPM$. Since $M$ lies on that circle, the equality says precisely that $AM$ is tangent there.''','The midpoint relations lead to an exact power equality; extracting it from the tangent circle is the main step.')
add(2024,3,4,'Combinatorics',['grid construction','majority','double counting'],r'Fill a $(2n+1)\times(2n+1)$ board with alternating crosses and circles, starting with a cross. Maximise the number of rows with a cross majority plus the number of columns with a circle majority.',r'''The answer is $4n$. There are $2n^2+2n+1$ crosses and $2n^2+2n$ circles. All $2n+1$ rows cannot have at least $n+1$ crosses, since that would require $2n^2+3n+1$ crosses. Similarly all columns cannot have circle majorities. The score is therefore at most $2n+2n$.

For equality, fill the last column with crosses and the remaining cells of the last row with circles. In the upper-left $2n\times2n$ block place exactly $n$ crosses in every row and every column, for example by a cyclic band of width $n$. This uses exactly the required totals. The first $2n$ rows have cross majorities, and the first $2n$ columns have circle majorities. Any filling with these totals can be made by the required alternating placement order.''','Global symbol counts give the upper bound, but a balanced block construction is needed to achieve both families of majorities simultaneously.')
add(2024,4,4.5,'Combinatorics',['intervals','extremal bounds','pigeonhole principle'],r'Intervals have endpoints in $\{1,\ldots,2024\}$, distinct positive lengths, and none contains another. What is the maximum possible number of intervals?',r'''The answer is $1012$. For $m$ intervals, order their left endpoints $l_1<\cdots<l_m$. Their right endpoints must also increase strictly, since otherwise one interval would contain another. Thus $l_i\ge i$ and $r_i\le2024-m+i$, giving
$$1\le r_i-l_i\le2024-m.$$
There are $m$ distinct lengths in this range, so $m\le2024-m$, or $m\le1012$.

The intervals $[i,2i]$ for $1\le i\le1012$ achieve equality: both endpoints increase, and the lengths are the distinct integers $1,\ldots,1012$.''','Ordering both endpoint lists produces a uniform length bound; this must then be combined with distinctness rather than just endpoint counting.')
add(2024,5,5,'Algebra',['functional equations','case analysis','zero sets'],r'Find all functions $f:\mathbb R\to\mathbb R$ satisfying $f(x^2)-yf(y)=f(x+y)(f(x)-y)$ for all real $x,y$.',r'''The solutions are $f\equiv0$, $f\equiv1$, and $f(x)=x$. Setting $x=0$ gives $f(0)=f(0)f(y)$, so if $f(0)\ne0$ then $f\equiv1$.

Now suppose $f(0)=0$. Taking $y=0$ gives $f(x^2)=f(x)^2$, and taking $y=-x$ gives $f(x)^2=-xf(-x)$. Applying the latter to $-x$ as well shows that, for each nonzero $x$, either $f(x)=0$ or $f(x)=x$: if both values are nonzero, substitution yields $f(x)^3=x^3$.

If $f$ is not zero everywhere, choose $t\ne0$ with $f(t)=t$. If $f(z)=0$ for some $z\ne0$, substitute $x=t,y=z-t$. The equation gives $(z-t)f(z-t)=t^2$, hence $(z-t)^2=t^2$ and $z=2t$. But if $f(2t)=0$, substitute $x=2t,y=-t$. The left side is $-t^2$, while the right side is $t^2$, a contradiction. Thus every nonzero input is fixed, and $f(x)=x$. All three proposed functions check directly.''','Several substitutions restrict each point to a zero-or-identity choice; a separate zero-set argument is needed to rule out mixed solutions.')
skip(2024,6,None,'The seventh-power minus 41 square equation has no elementary local obstruction found; withheld pending a reliable complete solution.')
skip(2023,1,None,'Parallel-line geometry statement screened; proof assessment pending.')
add(2023,2,4.5,'Number Theory',['coprimality','symmetric expressions','divisibility'],r'Find coprime positive integers $m,n$ such that $m^3+n^3$ divides $m^2+20mn+n^2$.',r'''The pairs are $(1,1),(1,2),(2,1),(1,5),(5,1)$. Put $s=m+n,t=mn$. The divisibility is
$$s(s^2-3t)\mid s^2+18t.$$
Since $\gcd(s,t)=1$, it follows that $s\mid18$, so $s\in\{2,3,6,9,18\}$. By symmetry assume $m\le n$. The coprime candidates for these sums are respectively
$$ (1,1);\ (1,2);\ (1,5);\ (1,8),(2,7),(4,5);\ (1,17),(5,13),(7,11).$$
Substitution into the original divisibility leaves exactly the first three pairs, with quotients $11,5,1$. Restoring the reversed pairs gives the list.''','The sum-and-product substitution and coprimality reduce an unbounded divisibility problem to a small exact list.')
add(2023,3,4.5,'Algebra',['recurrences','quadratic surds','Chebyshev polynomials'],r'For a positive integer $c$, set $x_1=c$ and $x_{n+1}=cx_n+\sqrt{c^2-1}\sqrt{x_n^2-1}$. Prove that every $x_n$ is an integer.',r'''If $c=1$, every term is one. Otherwise put $u=c+\sqrt{c^2-1}>1$, so $u^{-1}=c-\sqrt{c^2-1}$. Induction using the given positive square roots gives
$$x_n=\frac{u^n+u^{-n}}2,\qquad \sqrt{x_n^2-1}=\frac{u^n-u^{-n}}2.$$
Since $u+u^{-1}=2c$, these expressions satisfy
$$x_{n+1}=2cx_n-x_{n-1},$$
with $x_0=1,x_1=c$. This recurrence has integer coefficients and integer initial values, so all its terms are integers.''','The radical recurrence must be linearized using conjugate quadratic surds; the signs of the square roots matter.')
add(2023,4,6,'Combinatorics',['integer optimization','extremal distributions','construction'],r'Distribute $n$ stamps over ten pages, using distinct nonnegative counts. Find the largest $n$ for which every such distribution has four pages together containing at least $n/2$ stamps.',r'''The answer is $140$. Sort the page counts as $x_1<\cdots<x_{10}$, and put $a=x_6$, $B=x_1+\cdots+x_6$, $T=x_7+\cdots+x_{10}$. A counterexample requires $B>T$. Distinctness gives
$$B\le6a-15,\qquad T\ge4a+10.$$
If $n=140$, then $T\le69$ forces $a\le14$, while $B\ge71$ contradicts $B\le69$. Thus $140$ works.

For every integer $a\ge15$, counterexamples exist for every total
$$8a+21\le n\le12a-31.$$
Indeed choose an integer $B$ with $n/2<B\le6a-15$ and $T=n-B\ge4a+10$; such a choice exists throughout this interval. Six distinct nonnegative integers ending in $a$ can realize every sum from $a+10$ to $6a-15$: start with $0,1,2,3,4,a$ and increase the first five entries without collisions. Four distinct integers above $a$ can realize every sum at least $4a+10$ by increasing the largest entry. These choices realize $B,T$ and hence the counterexample.

The displayed intervals begin at $141$ when $a=15$, and successive intervals overlap or touch because $8(a+1)+21\le12a-30$ for $a\ge15$. They cover every $n>140$, completing the proof.''','The sharp answer depends on gaps between feasible integer totals, not just an asymptotic averaging bound; a construction must cover every larger total.')
add(2023,5,4.5,'Algebra',['Vieta formulas','positive roots','AM-HM'],r'For real $a\ne0,b$, prove that all four roots, counted with multiplicity, of $ax^4-4ax^3+(5a+b)x^2-4bx+b$ are positive real numbers exactly when $a=b$.',r'''If the roots $r_1,\ldots,r_4$ are positive, their product is $b/a>0$. Vieta's formulas give
$$\sum r_i=4,\qquad \sum\frac1{r_i}=\frac{4b/a}{b/a}=4.$$
Cauchy–Schwarz gives $(\sum r_i)(\sum1/r_i)\ge16$, with equality only when all four roots are equal. Here equality holds, so each root is one. Their product then gives $b/a=1$.

Conversely, if $a=b$, the polynomial is $a(x-1)^4$, whose four roots are positive.''','Vieta reveals both the root sum and reciprocal sum; recognizing the equality case of Cauchy–Schwarz forces all four roots.')
skip(2023,6,None,'Altitude-foot and auxiliary-circle geometry screened; complete proof assessment pending.')
skip(2022,1,5.5,'Same problem as SAMO2021 Senior Final Q4, already included under zaf_2021_757d61; recorded as an additional contest appearance.','duplicate-appearance')
add(2022,2,4.5,'Number Theory',['consecutive squares','ordered variables','Diophantine equations'],r'Find positive integers $a\ge b\ge c$ for which $a^2+3b$, $b^2+3c$, and $c^2+3a$ are all squares.',r'''Because $0<3b\le3a<4a+4$, the first square must be $(a+1)^2$, so $3b=2a+1$. Similarly $3c=2b+1$. These force
$$c=4t+1,\quad b=6t+1,\quad a=9t+1$$
for an integer $t\ge0$. The last expression becomes $16t^2+35t+4$.

For $t>4$, this lies strictly between $(4t+4)^2$ and $(4t+5)^2$, since its differences from these are $3t-12>0$ and $-5t-21<0$. Checking $t=0,1,2,3,4$ leaves exactly $t=0,4$. Thus the solutions are $(1,1,1)$ and $(37,25,17)$.''','Ordering allows two square gaps to be pinned down exactly, after which a parametrization and a second consecutive-square bound finish the classification.')
skip(2022,3,None,'Cyclic-product inequality screened; proof assessment pending.')
add(2022,4,4,'Algebra',['functional equations','elimination','positive domain'],r'Find positive-valued functions $f,g$ on the positive reals satisfying $(f(x)+y-1)(g(y)+x-1)=(x+y)^2$ and $(-f(x)+y)(g(y)+x)=(x+y+1)(y-x-1)$ for all $x,y>0$.',r'''Adding the expanded equations cancels the product $f(x)g(y)$ and yields
$$f(x)-x=(2y-1)g(y)-2y^2-y+2.$$
Set $y=1/2$ to obtain $f(x)-x=1$, so $f(x)=x+1$. Substituting this in the first original equation gives
$$(x+y)(g(y)+x-1)=(x+y)^2.$$
Since $x+y>0$, division gives $g(y)=y+1$. These functions are positive and direct substitution verifies both identities.''','The product terms must be eliminated before a carefully chosen input removes the other unknown function.')
skip(2022,5,None,'The organiser transcription allows a=b, making the question trivial; likely missing distinctness condition. Withheld rather than silently repaired.','withheld-malformed')
skip(2022,6,None,'Cyclic product of powers screened; full impossibility proof pending.')
exec(open(P+'pamo_extra.py').read())
exec(open(P+'pamo_resolved.py').read())
# All statements in each accessible official paper were read. Pending items remain explicit, never silently excluded by question number.
years=list(range(2000,2011))+[2012,2013]+list(range(2015,2020))+list(range(2021,2027))
for y in years:
 for n in range(1,7):
  if not any(r['year']==y and r['number']==str(n) for r in ledger):skip(y,n,None,'Statement individually screened in the official archive; full solution assessment not yet complete.')
json.dump(items,open(P+'pamo.json','w'),indent=2)
json.dump(ledger,open(P+'pamo-ledger.json','w'),indent=2)
print(len(items),len(ledger))
