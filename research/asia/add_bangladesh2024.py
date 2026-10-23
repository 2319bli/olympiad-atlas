import json,pathlib
P=pathlib.Path('/workspace/sites/olympiad-atlas/research/asia');RAW=P.parent/'raw'/'asia'
rev=json.loads((P/'reviews.json').read_text());man=json.loads((P/'manifest.json').read_text());rows=[]
url='https://drive.google.com/file/d/109NZke8qlIzj9huGQR7gfPQcNreTitvx/view'
def add(cat,n,d,topic,reason,statement='',solution='',omit=''):
 rows.append((cat,n,d,topic,reason,statement,solution,omit))
add('Primary',1,1,'Number Theory','The first digit must be at least seven; seven followed by zero is the minimum.')
add('Primary',3,3,'Number Theory','The two missing digits give a two-variable linear congruence modulo 41, with each variable restricted to ten possible digits.')
add('Primary',5,2.5,'Number Theory','After dividing by the gcd, the friendship condition factors as (u-1)(v-1)=0, so the smaller friend is a proper divisor of 961.')
add('Primary',6,3,'Number Theory','Prime factorization gives 2^28 times 3^13 times 5^6; divisor counts and even exponent choices answer the two questions.')
add('Primary',7,4.5,'Number Theory','A sum-of-two-squares multiplication must choose its sign at each step so that neither new coordinate becomes divisible by five.',r'''Prove that for every positive integer $n$, there exist positive integers $a,b$, neither divisible by $5$, such that $5^n=a^2+b^2$.''',r'''Use induction, starting from $5=1^2+2^2$. Suppose $a^2+b^2=5^n$ and neither $a$ nor $b$ is divisible by $5$. Then $a\equiv2b$ or $a\equiv-2b\pmod5$.

Both identities
$$5(a^2+b^2)=(2a+b)^2+(a-2b)^2=(2a-b)^2+(a+2b)^2$$
hold. If $a\equiv2b$, choose the second pair; its entries are congruent to $3b,4b$, both nonzero modulo $5$. If $a\equiv-2b$, choose the first pair; again both entries are nonzero modulo $5$. Taking absolute values gives positive integers and completes the induction.''')
add('Primary',8,4,'Geometry','The two midpoint conditions determine a fixed ratio on AB; a short coordinate identity turns the given equal lengths into the desired pair.',r'''In triangle $ABC$, let $P$ be the midpoint of $BC$ and $M$ the midpoint of $AP$. Line $CM$ meets $AB$ at $X$. If $BM=BP$, prove that $AX=MX$.''',r'''Scale and place the triangle so that $P=(0,0)$, $B=(-1,0)$, $C=(1,0)$. Write $M=(u,v)$, so $A=(2u,2v)$. The condition $BM=1$ gives
$$u^2+v^2+2u=0.$$
Solving the two line equations for $AB$ and $CM$ gives
$$X=\left(\frac{4u-1}{3},\frac{4v}{3}\right).$$
Consequently
$$9(AX^2-MX^2)=(2u+1)^2+4v^2-(u-1)^2-v^2
=3(u^2+v^2+2u)=0,$$
as required.''')
add('Junior',1,3.5,'Combinatorics','Moving all population increases before all divisions can only help; checking the maximum product for five operations and giving a six-operation construction settles the optimum.')
add('Junior',2,1.5,'Algebra','The expression is exactly the square of 2(x^2-x+1).')
add('Junior',3,3.5,'Geometry','Two applications of the angle-bisector theorem immediately give equal side ratios, hence the required parallelism.')
add('Junior',4,2.5,'Algebra','A transfer raises both means precisely when the transferred value lies between the original means; the resulting integer interval has 54 members.')
add('Junior',5,4,'Algebra','The positive and negative cases behave differently under multiplication by the integer part; careful endpoint tracking produces a half-open interval.',r'''Find all real $x$ such that $\lfloor x\lfloor x\rfloor\rfloor=2024$.''',r'''Put $m=\lfloor x\rfloor$. If $m\ge0$, then $m\le x<m+1$, so $m^2\le mx<m(m+1)$. The square bounds force $m\le44$, but then $mx<44\cdot45=1980$, impossible.

If $m<0$, write $m=-k$ with $k>0$. Then $-k\le x<-k+1$, so $k(k-1)<-kx\le k^2$. To have $2024\le-kx<2025$, we need $k=45$: $k\le44$ makes the upper bound too small, while $k\ge46$ makes the lower bound too large. For $k=45$, solving gives
$$-45<x\le-\frac{2024}{45}.$$
Every number in this interval has integer part $-45$ and satisfies the original equation.''')
add('Junior',7,5,'Combinatorics','A parity count of differently colored pairs, grouped by their unique midpoint, proves that the number of rainbow isosceles triangles is odd.',r'''The vertices of a regular $17$-gon are colored red, blue and yellow, with an odd number of vertices of each color. Prove that three differently colored vertices form an isosceles triangle.''',r'''Label the vertices modulo $17$. Every unordered pair $\{u,v\}$ has a unique midpoint vertex $w$ satisfying $2w=u+v$. Thus every pair determines an isosceles triangle with apex $w$.

The number of pairs with different colors is $RB+BY+YR$, where $R,B,Y$ are the three odd color counts. This number is odd. Such a pair either has a midpoint of the third color, giving the desired triangle, or has a midpoint matching one endpoint.

For each fixed apex $w$, reflection about its radius pairs up the other $16$ vertices. The number of vertices whose color differs from that of $w$ is $17$ minus an odd number, hence even. Therefore an even number of reflection pairs have exactly one endpoint of the apex's color: pairs with two differently colored-from-apex endpoints contribute two to that count, and pairs with one contribute one. Summing over apices, the number of pairs of the second type is even. An odd number remain of the first type, so at least one rainbow isosceles triangle exists.''')
add('Junior',8,4,'Number Theory','Normalize the conjugate powers by 2^n; their sum has an integer recurrence that preserves odd parity.',r'''For every integer $n>1$, prove that
$$10^n-(5+\sqrt{17})^n-(5-\sqrt{17})^n$$
is an integer divisible by $2^{n+1}$.''',r'''Put $\alpha=(5+\sqrt{17})/2$, $\beta=(5-\sqrt{17})/2$ and $s_n=\alpha^n+\beta^n$. Since $\alpha+\beta=5$ and $\alpha\beta=2$,
$$s_0=2,\quad s_1=5,\quad s_n=5s_{n-1}-2s_{n-2}.$$
Thus all $s_n$ are integers, and every $s_n$ with $n\ge1$ is odd. The expression in the question equals $2^n(5^n-s_n)$. Its parenthesis is an even integer, proving the claim.''')
add('Secondary',1,3.5,'Number Theory','Reducing modulo x and y forces the positive variables to divide one another, and the remaining one-variable equation factors completely.')
add('Secondary',2,4,'Geometry','Signed secant products at the intersection of the diagonals give the same power for the four proposed concyclic points.',r'''Diagonals $AC,BD$ of cyclic quadrilateral $ABCD$ meet at $E$. Points $F\in AC$ and $G\in BD$ satisfy $AF=BE$ and $DG=CE$. Prove that $B,G,F,C$ are concyclic.''',r'''Let $EA=a$, $EB=b$, $EC=c$, $ED=d$. Power of $E$ gives $ac=bd$. Orient $AC$ from $E$ toward $C$ and $BD$ from $E$ toward $D$. The signed coordinates of $F,G$ on their lines are $b-a$ and $d-c$, respectively. Therefore
$$\overline{EF}\,\overline{EC}=c(b-a)=bc-ac=bc-bd=(-b)(d-c)=\overline{EB}\,\overline{EG}.$$
By the converse of the intersecting-secants theorem, $B,G,F,C$ lie on one circle. As usual, the construction is understood to have distinct points so that this circle is defined.''')
add('Secondary',3,3,'Algebra','Cross multiplication factors using a+b nonzero to give ab=5; the common ratio is then one quarter and leaves two ordered pairs.')
add('Secondary',4,3,'Combinatorics','Among the eight subset sums, two agree modulo seven; subtracting them gives the permitted nonzero coefficient vector.')
add('Secondary',5,5.5,'Geometry','Equal circumradii do not determine the apex angle rather than its supplement; even symmetric isosceles examples violate the claimed conclusion.','','','Withheld: the official statement is false as written. Take P=(-1,0), Q=(1,0), X=(0,2), Y=(0,-1/2). Both circumradii are 5/4 and both incenters lie on the perpendicular bisector through M, but XPYQ is not a parallelogram.')
add('Secondary',6,4.5,'Algebra','The integer difference of neighboring entries bounds each summand by a reciprocal variation; total variation across the extreme reciprocals is sharp in sorted order.',r'''Let $a_1,\ldots,a_{2024}$ be a permutation of $1,\ldots,2024$. Find the minimum of
$$\sum_{i=1}^{2023}\left[(a_i+a_{i+1})\left(\frac1{a_i}+\frac1{a_{i+1}}\right)+\frac1{a_i a_{i+1}}\right].$$''',r'''For distinct positive integers $a,b$, put $d=|a-b|\ge1$. Since $d^2+1\ge2d$,
$$(a+b)(1/a+1/b)+1/(ab)=4+\frac{d^2+1}{ab}
\ge4+2\left|\frac1a-\frac1b\right|.$$
The sum of the absolute successive differences of a sequence is at least the difference between its largest and smallest entries. Applied to the reciprocals, this gives a lower bound
$$4\cdot2023+2\left(1-\frac1{2024}\right)=8094-\frac1{1012}.$$
The increasing permutation attains equality: every adjacent difference is one and the reciprocals are monotone. This is the minimum.''')
add('Secondary',7,5,'Geometry','A coordinate system at the square vertex makes one constructed line vertical; the two remaining intersection formulas cancel in a dot product.',r'''In square $ABCD$, choose $E\in AB$, $F\in BC$ with $BE=BF$. The line through $B$ perpendicular to $CE$ meets $CE$ at $G$ and line $AD$ at $H$. Let $P=FH\cap CE$ and $Q=GF\cap CD$. Prove that $DP\perp BQ$.''',r'''Take $B=(0,0)$, $C=(1,0)$, $D=(1,1)$, $A=(0,1)$ and write $E=(0,t)$, $F=(t,0)$, where $0<t<1$. Line $CE$ has equation $tx+y=t$, and its perpendicular through $B$ has equation $y=x/t$. Hence
$$G=\left(\frac{t^2}{1+t^2},\frac{t}{1+t^2}\right),\qquad H=(t,1).$$
Thus $FH$ is vertical, giving $P=(t,t-t^2)$. Intersecting line $GF$ with $x=1$ gives
$$Q=\left(1,\frac{t-1}{t^2-t+1}\right).$$
Now
$$\overrightarrow{DP}\cdot\overrightarrow{BQ}
=(t-1)-(t^2-t+1)\frac{t-1}{t^2-t+1}=0,$$
which proves the perpendicularity.''')
add('Secondary',9,4.5,'Number Theory','Necessity is exposed by n=1 and a prime shared with the step; sufficiency counts multiples of every prime power in an arithmetic progression.',r'''Find all positive integer pairs $(k,m)$ such that $k!$ divides
$$(n+m)(n+2m)\cdots(n+km)$$
for every positive integer $n$.''',r'''Exactly the pairs with $\gcd(m,k!)=1$ work. If a prime $p\le k$ divides $m$, set $n=1$. None of the factors is divisible by $p$, although $k!$ is, so the property fails.

Conversely assume $m$ has no prime divisor at most $k$. Fix a prime $p\le k$. For every $e\ge1$, multiplication by $m$ is invertible modulo $p^e$. Thus among any $p^e$ consecutive indices $i$, exactly one makes $n+im$ divisible by $p^e$. Among $1\le i\le k$ there are at least $\lfloor k/p^e\rfloor$ such indices. Summing over $e$ shows that the product's $p$-adic valuation is at least
$$\sum_{e\ge1}\left\lfloor\frac{k}{p^e}\right\rfloor=v_p(k!).$$
This holds for every prime factor of $k!$, proving divisibility.''')
add('Higher Secondary',1,4.5,'Number Theory','Cubic residues modulo 13 combine with the order of 3 to force p=13; the small prime-exponent exception is checked separately.',r'''Find all primes $p,q$ satisfying $p^3-3^q=10$.''',r'''For $q=3$, the equation gives $p^3=37$, impossible. For any other prime $q$, its residue modulo $3$ is $1$ or $2$. Since $3^3\equiv1\pmod{13}$, we have $3^q\equiv3$ or $9\pmod{13}$, respectively. Thus $p^3\equiv0$ or $6\pmod{13}$.

The cubic residues modulo $13$ are $0,1,5,8,12$, so $6$ is impossible. Hence $13\mid p$, and primality gives $p=13$. Substitution yields $3^q=13^3-10=2187=3^7$. Therefore the sole pair is $(p,q)=(13,7)$.''')
add('Higher Secondary',4,3.5,'Combinatorics','The 2048 subset sums occupy only 2024 residue classes, so subtracting equal-residue sums gives the desired coefficients.')
add('Higher Secondary',5,5.5,'Geometry','The incenter projection and a parallel tangent have explicit coordinates; a side-length identity makes both the scalar and cross products of the angle pairs agree.',r'''Let $I$ be the incenter of triangle $ABC$. Define $P$ by $PI\perp BC$ and $PA\parallel BC$. The tangent to the incircle parallel to $BC$ and different from $BC$ meets $AB,AC$ at $Q,R$. Prove that $\angle BPQ=\angle CPR$.''',r'''Choose $B=(0,0)$, $C=(a,0)$, $A=(v,h)$, with $h>0$. Let $b=CA$, $c=AB$, $s=(a+b+c)/2$, and let $r$ be the inradius. The incircle's contact point on $BC$ has coordinate $u=s-b$, so $I=(u,r)$, $P=(u,h)$ and $2r=ah/s$. The upper tangent is $y=2r$, giving
$$Q=(2rv/h,2r),\qquad R=(a+2r(v-a)/h,2r).$$
The cosine rule gives $2av=a^2+c^2-b^2$. Using this and $2u=a+c-b$, direct simplification gives
$$h(a-2u)+2r(v-a+u)=0.\tag{1}$$
Now the cross products of the ordered vector pairs $(PB,PQ)$ and $(PC,PR)$ both equal $2r(v-u)$. Their dot products differ by
$$a(a-2u)+\frac{2ra}{h}(v-a+u),$$
which is zero by (1). Equal cross and dot products imply equal directed angles, and hence the stated ordinary angles. This also covers the zero-cross-product case by continuity whenever the indicated angles are defined.''')
add('Higher Secondary',6,3.5,'Algebra','Eliminating the sequence gives P(2n)-P(n) constant on positive integers; comparing polynomial leading terms forces P to be constant.')
add('Higher Secondary',7,4.5,'Algebra','A large denominator fixes f(1), then the equation makes f an involution; a diagonal substitution bounds f(n) by n and forces equality.',r'''Find every function $f:\mathbb N\to\mathbb N$, where $\mathbb N$ denotes the positive integers, satisfying
$$f\!\left(\left\lceil\frac{f(m)}n\right\rceil\right)=\left\lceil\frac m{f(n)}\right\rceil$$
for all positive integers $m,n$.''',r'''Set $m=1$ and choose $n\ge f(1)$. Both ceilings then equal $1$, so $f(1)=1$. Taking $n=1$ gives $f(f(m))=m$, in particular $f$ is injective.

Suppose $f(n)>n$ for some $n$. Setting $m=n$ makes the right side $1$, while the argument on the left is $\lceil f(n)/n\rceil\ge2$. This contradicts injectivity because $f(1)=1$. Hence $f(n)\le n$ for every $n$. Apply this inequality to $f(n)$ to obtain $n=f(f(n))\le f(n)$. Therefore $f(n)=n$ for all $n$, which satisfies the equation.''')
# These statements have been read, but a reliable full mathematical assessment
# is still pending. They are discovered records, never published as rated tasks.
pending=[('Primary',2,'Diagram-dependent area problem; full diagram review pending.'),('Primary',4,'Road/crossing statement needs a clear interpretation of whether roads must be straight.'),('Junior',6,'Full geometry solution still to be checked.'),('Secondary',8,'Classification of planar sets with every triple isosceles still to be checked.'),('Higher Secondary',8,'Official numerator is typeset ambiguously as n raised to n-1; need a corrected intended statement before a divisibility proof.'),('Higher Secondary',9,'Full circle geometry solution still to be checked.'),('Higher Secondary',10,'Winning-strategy proof still to be checked.')]
for cat,n,d,topic,reason,statement,solution,omit in rows:
 slug=f'bgd_2024_national_{cat.lower().replace(" ","_")}_q{n}'
 comp='Bangladesh Mathematical Olympiad — National'
 raw={'country':'Bangladesh','competition':comp,'year':2024,'section':cat,'problem_number':str(n),'problem_markdown':statement or f'{cat} Problem {n}; see official paper','solutions_markdown':[solution],'primary_domain':topic,'topics':[],'booklet_title':'Bangladesh Mathematical Olympiad 2024 National — official bilingual paper','sourceDataset':'Bangladesh Mathematical Olympiad Committee public archive','sourceLicense':'Official mathematical statement translated/paraphrased; original independent worked solution.'}
 (RAW/(slug+'.json')).write_text(json.dumps(raw,ensure_ascii=False,indent=2))
 note='Official national paper obtained from the public Drive archive linked by https://matholympiad.org.bd/resources/bdmo-questions. Independent mathematical review; gaps remain explicitly pending.'
 if cat=='Secondary' and n==6:note+=' Also Higher Secondary Problem 3; identical appearance merged.'
 if cat=='Secondary' and n==7:note+=' Also Higher Secondary Problem 2; identical appearance merged.'
 v={'difficulty':d,'reason':reason,'sourceUrl':url,'solutionUrl':url,'note':note}
 if solution:v['solutionOverride']=solution
 else:v['solutionKind']='source-link'
 if omit:v['omitReason']=omit
 rev[slug]=v
 if slug not in {x[0] for x in man}:man.append([slug,'bangladesh-official',2024,comp,0,0,str(n)])
for cat,n,reason in pending:
 slug=f'bgd_2024_national_{cat.lower().replace(" ","_")}_q{n}'
 if slug not in {x[0] for x in man}:man.append([slug,'bangladesh-official',2024,'Bangladesh Mathematical Olympiad — National',0,0,str(n)])
(P/'bangladesh-pending.json').write_text(json.dumps(pending,ensure_ascii=False,indent=2))
(P/'reviews.json').write_text(json.dumps(rev,ensure_ascii=False,indent=2));(P/'manifest.json').write_text(json.dumps(man,ensure_ascii=False,indent=2))
print('Bangladesh assessed',len(rows),'included',sum(4<=r[2]<=7 and not r[-1] for r in rows),'pending',len(pending))
