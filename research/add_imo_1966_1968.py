from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');raw=p/'international-raw';r=json.loads((p/'international-reviews.json').read_text())
def add(year,num,topic,rating,reason,statement,solution='',tags=None,note=None,solution_url=None):
 slug=f'imo_{year}_official_p{num}'
 d={'id':slug,'competition_code':'IMO','competition':'IMO','year':year,'problem_number':str(num),'primary_domain':topic,'topics':[[topic,t] for t in (tags or [])],'problem_markdown':statement,'solutions_markdown':[solution],'officialSourceUrl':f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf','officialSolutionUrl':solution_url or f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf','reviewNote':note or 'Official released statement checked; worked exposition independently written and mathematically assessed.'}
 (raw/(slug+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2));r[slug]=[rating,reason]
add(1966,1,'Combinatorics',3.5,'Venn-region variables reduce the conditions to $9z+4w=26$ in nonnegative integers, determining that six students solved only B.',r'''Among the contestants in a three-problem competition, 25 solved at least one problem. Among those who did not solve $A$, twice as many solved $B$ as solved $C$. The number solving only $A$ exceeds the number solving $A$ and another problem by one. Among those solving exactly one problem, half did not solve $A$. How many solved only $B$?''')
add(1966,2,'Geometry',3.5,r'The sine rule and sum-to-product formulas reduce the hypothesis to $\cos\alpha\cos\beta=\cos^2((\alpha+\beta)/2)$, which forces the two angles equal.',r'A triangle has sides $a,b,c$ opposite angles $\alpha,\beta,\gamma$. If the tangents are defined and $a+b=\tan(\gamma/2)(a\tan\alpha+b\tan\beta)$, prove the triangle is isosceles.')
add(1966,3,'Geometry',4,'Project each distance onto the corresponding radial direction. The four linear terms cancel because the tetrahedron’s vertex vectors sum to zero, and the equality case requires care.',r'For a regular tetrahedron, prove that the sum of distances from a point in space to the four vertices is uniquely minimised at the circumcentre.',r'''Place the circumcentre $O$ at the origin, and let the vertex vectors be $v_1,\ldots,v_4$, each of length $R$. Symmetry gives $v_1+\cdots+v_4=0$.

For any point with position vector $p$, projection onto the unit vector $-v_i/R$ gives
$$|p-v_i|\geq(p-v_i)\cdot\frac{-v_i}{R}=R-\frac{p\cdot v_i}{R}.$$
Adding over the four vertices cancels the scalar products and yields
$$\sum_{i=1}^4|p-v_i|\geq4R.$$
The circumcentre attains $4R$. If equality holds, each vector $p-v_i$ is a nonnegative multiple of $-v_i$, so $p$ lies on every line $Ov_i$. Two such distinct lines already intersect only at $O$, hence $p=0$. The minimum is therefore unique.''',['Solid geometry','Vectors','Inequalities'])
add(1966,4,'Algebra',2,'The double-angle identity $1/\sin2u=\cot u-\cot2u$ makes the entire sum telescope.',r'For positive integer $n$ and real $x$ for which all terms are defined, prove $\sum_{j=1}^{n}1/\sin(2^jx)=\cot x-\cot(2^nx)$.')
add(1966,5,'Algebra',4.5,'Order the parameters and regard the equations as equal values of a piecewise linear function. Its interior slope jumps must vanish, leaving only the two extreme variables.',r'Let $a_1,a_2,a_3,a_4$ be distinct real numbers. Solve the four equations $\sum_{j=1}^4|a_i-a_j|x_j=1$ for $i=1,2,3,4$.',r'''Relabel so that $a_1<a_2<a_3<a_4$. The answer is
$$x_1=x_4=\frac1{a_4-a_1},\qquad x_2=x_3=0.$$

Define $F(t)=\sum_{j=1}^4|t-a_j|x_j$. The equations assert $F(a_i)=1$ for all four parameters. The function is affine on each of $[a_1,a_2]$, $[a_2,a_3]$, $[a_3,a_4]$; since the endpoint values agree, it is constant on each interval. Its slope jump at $a_2$ is $2x_2$, and at $a_3$ is $2x_3$. Both must be zero.

The equations at the extremes now give $(a_4-a_1)x_4=1$ and $(a_4-a_1)x_1=1$, establishing the unique solution. Substitution gives $F(t)=1$ throughout $[a_1,a_4]$, verifying all four equations.

With the original labels, the variables corresponding to the smallest and largest $a_i$ are both the reciprocal of their difference, and the other two are zero.''',['Absolute values','Piecewise linear functions','Linear systems'],note='The current official English PDF has duplicated/missing terms in its expanded system. The intended symmetric system was verified against John Scholes’s authored statement and solution, linked here.',solution_url='https://prase.cz/kalva/imo/isoln/isoln665.html')
add(1966,6,'Geometry',3,'The three corner-area ratios have product $x(1-x)y(1-y)z(1-z)\leq1/64$, so one is at most one quarter.',r'Points $K,L,M$ are interior to sides $BC,CA,AB$ of a triangle. Prove at least one of $[AML],[BKM],[CLK]$ is at most $[ABC]/4$.')
add(1967,1,'Geometry',5,'Recognise the covering radius of an acute triangle as its circumradius and prove that the opposite parallelogram vertex cannot cover its circumcentre. The final inequality is a cosine-rule calculation.',r'''A parallelogram $ABCD$ has $AB=a$, $AD=1$ and $\angle BAD=\alpha$, with triangle $ABD$ acute. Prove that the four closed disks of radius $1$ centred at its vertices cover the parallelogram exactly when $a\leq\cos\alpha+\sqrt3\sin\alpha$.''',r'''Let $O,R$ be the circumcentre and circumradius of acute triangle $ABD$. This triangle is covered by the three vertex disks of radius $R$. Indeed, if $X=\lambda A+\mu B+\nu D$ with nonnegative weights summing to one, then
$$\lambda|X-A|^2+\mu|X-B|^2+\nu|X-D|^2=R^2-|X-O|^2\leq R^2.$$
At least one distance is therefore at most $R$. The congruent triangle $BCD$ has the same property. Thus $R\leq1$ is sufficient to cover the parallelogram.

Conversely $O$ is inside $ABD$. Put $A=0$, $B=b$, $D=d$, so $C=b+d$. The circumcentre equations give $2O\cdot b=a^2$ and $2O\cdot d=1$, whence
$$|O-C|^2=R^2+2b\cdot d=R^2+2a\cos\alpha>R^2.$$
If $R>1$, none of the four unit disks covers $O$. Hence coverage is equivalent to $R\leq1$.

The sine and cosine rules give
$$R=\frac{BD}{2\sin\alpha},\qquad BD^2=a^2+1-2a\cos\alpha.$$
Consequently $R\leq1$ is equivalent to $(a-\cos\alpha)^2\leq3\sin^2\alpha$. Since the acute angle at $B$ gives $a>\cos\alpha$, this is precisely the inequality in the question.''',['Covering','Circumradius','Vectors'])
add(1967,2,'Geometry',5.5,'Combine the four short-edge square lengths using the two opposite-edge midpoints. This bounds the perpendicular separation, and a constrained three-factor product gives the sharp volume limit.',r'Exactly one edge of a tetrahedron is longer than $1$. Prove that its volume is at most $1/8$.',r'''Let the exceptional edge be $AB$ of length $a$, let $CD$ have length $b\leq1$, and let their midpoints be $M,N$. If $h$ is the distance between the two supporting lines and $\omega$ their angle, then
$$V=\frac{ab h|\sin\omega|}{6}\leq\frac{ab|MN|}{6}.$$
The parallelogram identity, applied to the four cross edges, gives
$$AC^2+AD^2+BC^2+BD^2=a^2+b^2+4MN^2\leq4.$$
Hence, writing $u=a^2$ and $v=b^2\in(0,1]$,
$$V^2\leq\frac{uv(4-u-v)}{144}\leq\frac{v(4-v)^2}{576}.$$
The second inequality is $u(4-v-u)\leq(4-v)^2/4$. Finally
$$9-v(4-v)^2=(1-v)(v^2-7v+9)\geq0$$
for $0<v\leq1$. Therefore $V^2\leq9/576=1/64$.

The bound is sharp: take $AB=\sqrt{3/2}$ and all five other edges equal to $1$. One coordinate realisation is
$$A=(-\sqrt{3/8},0,0),\quad B=(\sqrt{3/8},0,0),$$
$$C=(0,-1/2,\sqrt{3/8}),\quad D=(0,1/2,\sqrt{3/8}).$$
Its volume is $1/8$ and exactly $AB$ exceeds one.''',['Solid geometry','Volumes','Inequalities'])
add(1967,3,'Number theory',4,'Factor the quadratic differences into two consecutive-integer products. The prime hypothesis lets one insert and then cancel one extra factor to gain the required additional factorial.',r'''Let positive integers $k,m,n$ satisfy that $p=m+k+1$ is prime and $p>n+1$. Put $c_s=s(s+1)$. Prove that $\prod_{i=1}^n(c_{m+i}-c_k)$ is divisible by $c_1c_2\cdots c_n$.''',r'''Factor each difference:
$$c_{m+i}-c_k=(m+i-k)(m+i+k+1)=(m+i-k)(p+i).$$
The product $\prod_{i=1}^n(m+i-k)$ of $n$ consecutive integers is divisible by $n!$. This remains true if some are zero or negative, by the integer-valued binomial product formula, or by reversing the signs and order in the entirely negative case.

The product $p(p+1)\cdots(p+n)$ of $n+1$ consecutive integers is divisible by $(n+1)!$. Since $p$ is prime and greater than $n+1$, it is coprime to that factorial. Cancelling this coprime factor shows that $\prod_{i=1}^n(p+i)$ itself is divisible by $(n+1)!$.

Multiplying the two divisibilities gives the required divisor
$$n!(n+1)!=\prod_{i=1}^n i(i+1)=c_1c_2\cdots c_n.$$''',['Divisibility','Consecutive integers','Factorisation'])
add(1967,5,'Algebra',4.5,'Infinitely many zero moments must be odd. Comparing the multiplicities of the largest positive and negative magnitudes, then repeating after cancellation, forces a symmetric multiset.',r'''Real numbers $a_1,\ldots,a_8$ are not all zero, and $c_n=\sum_{i=1}^8a_i^n$ for positive integers $n$. If infinitely many $c_n$ vanish, determine exactly which positive integers $n$ satisfy $c_n=0$.''',r'''Exactly the odd positive integers satisfy $c_n=0$.

Every even term is positive, since it is a sum of nonnegative even powers and at least one summand is nonzero. Thus the infinitely many zero terms have odd indices tending to infinity.

Let $M$ be the largest nonzero magnitude among the $a_i$, and let $r,s$ be the numbers of occurrences of $M,-M$. Along those odd zero indices,
$$0=\frac{c_n}{M^n}=r-s+\sum_{|a_i|<M}(a_i/M)^n.$$
The remaining sum tends to zero, so $r=s$. Remove all occurrences of $M,-M$. They cancel in every odd power sum, leaving the same zero odd indices for the remaining numbers.

Repeat with the next largest magnitude. There are only finitely many, so each positive magnitude has equal positive and negative multiplicities. Their contributions cancel for every odd exponent; zeros contribute nothing. Hence every odd term vanishes and no even term does.''',['Power sums','Dominant terms','Limits'])
add(1967,6,'Number theory',4.5,'An affine shift solves the remaining-medal recurrence. The terminal condition creates a strong divisibility constraint, leaving just one possible number of days.',r'''A contest awards $m$ medals over $n>1$ days. On day $i$, it awards $i$ medals and then one seventh of the medals still remaining. On the last day the remaining $n$ medals are awarded. Determine $m,n$.''',r'''Let $R_i$ be the medals remaining after day $i$, with $R_0=m$. Then
$$R_i=\frac67(R_{i-1}-i),\qquad R_n=0.$$
The same recurrence is valid for the last day because $R_{n-1}=n$. Solving it by subtracting the particular solution $36-6i$ gives
$$R_i=36-6i+\left(\frac67\right)^i(m-36).$$
At $i=n$ this implies
$$6^{n-1}(m-36)=(n-6)7^n.$$
Since $6$ and $7$ are coprime, $6^{n-1}$ divides $n-6$. For $n\geq2$ we have $|n-6|<6^{n-1}$, so $n=6$. The displayed identity then gives $m=36$.

These values work: $R_i=36-6i$, and on each day before the last, $i+(36-6(i-1)-i)/7=6$ medals are awarded. On day six the final six medals are awarded.''',['Recurrences','Divisibility','Integer constraints'])
add(1968,1,'Geometry',4.5,'Translate a doubled-angle relation into a side-length identity, then treat all three possible ordered angle pairs. Only one yields a nondegenerate integer triangle.',r'Prove that exactly one triangle has consecutive positive integer side lengths and an angle twice another angle. Determine its side lengths.',r'''If sides $u,v,w$ are opposite angles $U,V,W$ and $V=2U$, the sine and cosine rules give
$$v=2u\cos U,\qquad 2vw\cos U=v^2+w^2-u^2.$$
Eliminating $\cos U$ and using $w\ne u$ yields
$$v^2=u(u+w).$$
Conversely this identity for a triangle with distinct sides implies $v=2u\cos U$ and then $\sin V=\sin2U$. Since $v>u$, the supplementary alternative $V=180^\circ-2U$ would give $W=U$, hence $w=u$, excluded. Thus it characterises the required doubled angle.

Write the consecutive sides as $x,x+1,x+2$, with $x\geq2$ for a nondegenerate triangle. The doubled angle must be the larger of a pair, leaving three possibilities:

- $u=x,v=x+1,w=x+2$ gives $(x+1)^2=x(2x+2)$, hence $x=1$, inadmissible.
- $u=x,v=x+2,w=x+1$ gives $(x+2)^2=x(2x+1)$, hence $(x-4)(x+1)=0$, so $x=4$.
- $u=x+1,v=x+2,w=x$ gives $x^2-x-3=0$, which has no integer root.

Therefore the unique side lengths are $4,5,6$. Since $6^2=4(4+5)$, the angle opposite $6$ is twice that opposite $4$.''',['Sine rule','Cosine rule','Diophantine equations'])
add(1968,2,'Number theory',3.5,'The digit product is at most the number itself. These lower and upper bounds on the quadratic leave only $x=12$, which verifies directly.',r'Find every positive integer $x$ whose decimal digit product equals $x^2-10x-22$.')
add(1968,3,'Algebra',3,'Compare the quadratic map to the identity: a constant strict sign forbids a cycle, a double root forces the only constant cycle, and two fixed points give two solutions.',r'''Let $a,b,c$ be real with $a\ne0$ and consider $x_{i+1}=ax_i^2+bx_i+c$ cyclically for $i=1,\ldots,n$, with $x_{n+1}=x_1$. Put $\Delta=(b-1)^2-4ac$. Prove there are no real solutions if $\Delta<0$, exactly one if $\Delta=0$, and more than one if $\Delta>0$.''')
add(1968,4,'Geometry',2.5,'Choose a longest edge. If the three incident lengths failed the triangle inequality at both endpoints, adding those failures would contradict the two face triangle inequalities.',r'Prove that every tetrahedron has a vertex whose three incident edge lengths are the side lengths of a triangle.')
add(1968,5,'Algebra',3.5,'The range is forced into $[1/2,1]$, on which the given transformation is an involution. Alternating its endpoint values on unit intervals supplies an example.',r'''A real function on all of $\mathbb R$ satisfies $f(x+a)=\tfrac12+\sqrt{f(x)-f(x)^2}$ for a fixed $a>0$. Prove it is periodic, and for $a=1$ construct a nonconstant example.''')
add(1968,6,'Number theory',4,'Each floor counts the positive integers up to $n$ with one specified exponent of two. These disjoint classes exhaust all integers from one to $n$.',r'For every positive integer $n$, evaluate $\displaystyle\sum_{k=0}^{\infty}\left\lfloor\frac{n+2^k}{2^{k+1}}\right\rfloor$.',r'''The sum equals $n$.

For a fixed $k\geq0$, the positive integers at most $n$ divisible by $2^k$ but not by $2^{k+1}$ are
$$2^k,\ 3\cdot2^k,\ 5\cdot2^k,\ldots.$$
Their number is exactly
$$\left\lfloor\frac{n+2^k}{2^{k+1}}\right\rfloor.$$
Every positive integer has a unique exponent of two in its prime factorisation. Thus these classes, as $k$ varies, partition $\{1,\ldots,n\}$. Adding their sizes gives $n$. Only finitely many terms are nonzero, since the class is empty when $2^k>n$.''',['Floor functions','Valuations','Double counting'])
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
