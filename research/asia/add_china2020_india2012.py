import json,pathlib
P=pathlib.Path('/workspace/sites/olympiad-atlas/research/asia');RAW=P.parent/'raw'/'asia';r=json.loads((P/'reviews.json').read_text());m=json.loads((P/'manifest.json').read_text())
def review(slug,d,reason,solution='',statement='',**kw):
 v={'difficulty':d,'reason':reason,**kw}
 if solution:v['solutionOverride']=solution
 if statement:v['statementOverride']=statement
 r[slug]=v
low={
'030836':(1.5,'Geometric-sequence ratios determine the first term as 13 cubed, giving the logarithm immediately.'),
'c412ea':(1.5,'Change every logarithm to base two and solve the resulting linear equation.'),
'e8f4b1':(2,'Standard ellipse coordinates turn the two dot products into a direct relation among squared lengths.'),
'370a0d':(1.5,'Perpendicular slopes identify a diameter, so the greatest distance from the origin is that diameter length.'),
'ce83b8':(2.5,'The function decreases to ten and increases afterwards; one interval minimum is twenty and the other is its endpoint value.'),
'439128':(1.5,'A consecutive subset with at least two elements is uniquely specified by its two distinct endpoints.'),
'c9216b':(3,'The real quotient places the complex number on a line; the minimum is an ordinary point-to-line distance.'),
'141bc5':(2.5,'The cosine rule and the identity sin^6(t)+cos^6(t)=1-3sin^2(t)cos^2(t) give the value.'),
'3015e8':(3,'The median formula first determines the third side, after which the cosine rule and one power identity finish.'),
'02f937':(2,'Only the three equal-modulus pairs may be swapped, yielding eight permutations.'),
'19b8fd':(3.5,'The sphere center lies one quarter of the tetrahedron height above the base, so the middle parallel section has the same radius as the base circumcircle.'),
'875b51':(2.5,'Symmetry identifies the sphere center midway between the base centroids, and Pythagoras supplies its radius.'),
'219100':(3,'Subtracting 8x gives the monic polynomial with roots one through five; its linear coefficient follows by elementary symmetric sums.'),
'6f1224':(3.5,'Separate the two possible values of A and rewrite each expression as a shifted sine, tracking the open angle endpoints.'),
'5db7f7':(3.5,'Ellipse coordinates fix two length ratios and the tangent addition formulas give their angle product.')}
for suffix,(d,reason) in low.items():review('chn_2020_'+suffix,d,reason)
review('chn_2020_2e1b0e',4,'The vector relation in the transcription does not match the relation used by the source solution.',omitReason='Withheld: the printed vector equation forces P=D and is incompatible with the stated convex trapezoid; the solution uses a different midpoint-weight relation. Correct original equation required.')
review('chn_2020_050ad3',4.5,'Reflection symmetry forces the middle root to be the center of the two radicals; locating the two outer roots and using the supplied largest-root condition then fixes both parameters.',r'''The expression $\sqrt{|x|}+\sqrt{|x+a|}$ is symmetric under $x\mapsto-a-x$. With exactly three distinct solutions, the middle one must be $x=-a/2$. Substitution gives $b=\sqrt{2a}$.

On $[-a,0]$, Cauchy gives $\sqrt{-x}+\sqrt{x+a}\le\sqrt{2a}$, with equality only at $-a/2$. On $[0,\infty)$, the expression is strictly increasing. Its value at $x=a/8$ is
$$\sqrt{a/8}+\sqrt{9a/8}=\sqrt{2a}.$$
Thus the largest root is $a/8$; reflection gives the other outer root $-9a/8$. The condition $x_3=b$ now gives $a/8=\sqrt{2a}$, so $a=128$, $b=16$, and $a+b=144$.''')
review('chn_2020_294f9a',4.5,'The distinguished box must contain three or four cards; the three-card case requires a small tournament-orientation classification with an extra capacity restriction.',r'''Box $1$ must receive at least three cards, since otherwise ten cards could not fit while all four other boxes have fewer. At most four cards can go into box $1$.

If all four cards $\{1,j\}$ go there, each other box can contain at most three, so all $2^6=64$ placements of the remaining cards work.

Now suppose exactly three cards go into box $1$. There are four choices for the exceptional card; fix it as $\{1,5\}$ in box $5$. The three cards joining boxes $2,3,4$ have eight placements. Six produce loads $(2,1,0)$ in some order, and two produce $(1,1,1)$. In the first case, the box already holding two cards forces its card with $5$ into box $5$; then the two remaining cards with $5$ must go to their other endpoints. This gives one extension for each of the six placements. In the second case, zero or one of the three remaining cards may go into box $5$, giving $1+3=4$ extensions each.

Hence this case contributes $4(6+2\cdot4)=56$, and the total is $64+56=120$.''',r'''For every pair $1\le i<j\le5$, there is one card marked $i,j$. Place each of these ten cards into either box $i$ or box $j$. How many placements give box $1$ strictly more cards than every other box?''')
review('chn_2020_aed280',4,'Completing squares gives a sphere constraint whose supporting linear bound matches a second weighted Cauchy inequality exactly.',r'''Complete squares in the constraint:
$$a^2+(2b-1)^2+(3c-2)^2=3.$$
Cauchy gives $(a+2b+3c-3)^2\le9$, so $a+2b+3c\le6$. A second application gives
$$\left(\frac1a+\frac2b+\frac3c\right)(a+2b+3c)\ge(1+2+3)^2=36.$$
Therefore the requested expression is at least $6$. The choice $a=b=c=1$ satisfies the constraint and attains equality.''')
review('chn_2020_b4a270',4.5,'Recognize the radical formula as an integer recurrence, then find an alternating determinant invariant that produces a square at every odd index.',r'''The two bases in the formula satisfy $q^2=q+1$, so $a_1=a_2=1$ and $a_{n+2}=a_{n+1}+a_n$. Hence the sequence consists of positive integers.

Set $D_n=a_na_{n+4}-a_{n+2}^2$. If $x=a_n$ and $y=a_{n+1}$, then $a_{n+2}=x+y$, $a_{n+4}=2x+3y$, so
$$D_n=x^2+xy-y^2.$$
Replacing $(x,y)$ by $(y,x+y)$ negates this expression. Since $D_1=1$, we obtain $D_n=(-1)^{n+1}$. Thus for every positive odd $n$,
$$a_na_{n+4}-1=a_{n+2}^2,$$
which provides infinitely many required indices.''')
u='https://library.hbcse.tifr.res.in/olympiads/uploads/inmo-2012.pdf/at_download/file'
def ind(slug,d,reason,sol='',statement='',**extra):review(slug,d,reason,sol,statement,sourceUrl=u,solutionUrl=u,competitionOverride='Indian National Mathematical Olympiad (INMO)',note='Checked against the complete official six-problem INMO 2012 solution booklet. '+extra.pop('note',''),**extra)
ind('ind_2012_f4574f',4.5,'An extremal-position argument makes the three free chords equal; the two possible arcs containing the remaining vertices must be compared.',r'''The chord formula $AB=2R\sin67.5^\circ$ gives $R=1$. At a nondegenerate maximum, with $A,B,C$ fixed, moving $D$ to the midpoint of the arc $AC$ not containing $B$ maximizes its distance from $AC$, and hence the area. Thus $AD=DC$. Applying the same argument to $C$ gives $BC=CD$. Therefore the three free chords are equal.

If $C,D$ lie on the major arc $BA$, their three successive arcs each measure $225^\circ/3=75^\circ$. The area is
$$\frac12\sin135^\circ+\frac32\sin75^\circ
=\frac{5+3\sqrt3}{4\sqrt2}.$$
If they lie on the minor arc, the three arcs each measure $45^\circ$, giving area $\frac32\sin45^\circ-\frac12\sin135^\circ=\sqrt2/2$, which is smaller. Boundary cases are triangles inscribed in a unit circle, whose area is at most $3\sqrt3/4$, also smaller than the first value. Thus the first displayed value is the maximum.''',r'''A cyclic quadrilateral $ABCD$ has $AB=\sqrt{2+\sqrt2}$, and chord $AB$ subtends a $135^\circ$ angle at the circle's center. Find the greatest possible area of $ABCD$.''')
ind('ind_2012_7115a8',4,'Parity limits the possible prime offsets, then residues modulo three and five force the same starting class modulo thirty.',r'''For any four primes $p_1<\cdots<p_4$ satisfying the hypotheses, all are odd and lie among
$$p_1,p_1+2,p_1+4,p_1+6,p_1+8.$$
If $p_1\equiv1\pmod3$, both $p_1+2$ and $p_1+8$ would be divisible by $3$, leaving too few primes. Hence $p_1\equiv2\pmod3$, and the four primes must be $p_1,p_1+2,p_1+6,p_1+8$.

Modulo $5$, the starting residue cannot be $0,2,3,4$, since respectively one of these four primes would be divisible by $5$. Thus $p_1\equiv1\pmod5$. Together with oddness this gives $p_1\equiv11\pmod{30}$. The same argument applies to $q_1$, proving $30\mid p_1-q_1$.''')
ind('ind_2012_5fd3c8',5.5,'Subtract neighboring nonlinear recurrences to uncover a constant quotient, converting rational division into an integer-coefficient linear recurrence.',r'''First $f_2=x^2-1$. Subtract the identities at adjacent indices to obtain
$$f_n(f_n+f_{n-2})=f_{n-1}(f_{n+1}+f_{n-1}).$$
Consequently, as identities of rational functions,
$$\frac{f_{n+1}+f_{n-1}}{f_n}=\frac{f_n+f_{n-2}}{f_{n-1}}=\cdots=\frac{f_2+f_0}{f_1}=x.$$
It follows that $f_{n+1}=xf_n-f_{n-1}$. Starting from $1,x$, this recurrence produces polynomials with integer coefficients by induction, so every apparent denominator in the original recurrence cancels. It also shows each polynomial is monic of degree $n$, ensuring that the rational-function divisions above use nonzero functions.''',r'''Starting with $f_0(x)=1$ and $f_1(x)=x$, recursively form rational functions by
$$f_{n+1}(x)=\frac{f_n(x)^2-1}{f_{n-1}(x)}\qquad(n\ge1).$$
Prove that every $f_n$ simplifies to a polynomial with integer coefficients.''',note='The recurrence is explicitly interpreted as a rational-function identity, matching the official division argument; arbitrary independently assigned values at removable singularities are not intended.')
ind('ind_2012_0f1968',4.5,'Equal-area radial pieces encode the point by three positive integer barycentric weights; proving the converse turns the geometry into stars and bars.',r'''Every vertex of $ABC$ must lie on one of the rays, or one resulting region would be a quadrilateral. Suppose $l,m,n$ small triangles have bases on $BC,CA,AB$, respectively. They are positive integers with $l+m+n=27$. Since all small triangles have equal area,
$$[PBC]:[PCA]:[PAB]=l:m:n.$$
These three area ratios determine the interior point uniquely: explicitly $P=(lA+mB+nC)/27$ in vector notation.

Conversely each positive triple $l+m+n=27$ determines this interior point. Divide $BC,CA,AB$ into $l,m,n$ equal segments and join their endpoints to $P$. The resulting $27$ triangles all have area $[ABC]/27$, so $P$ is good. Thus the number of good points is the number of positive compositions of $27$ into three parts,
$$\binom{26}{2}=325.$$''',topic='Combinatorics')
ind('ind_2012_9dc9fe',5.5,'The functional identities first restrict values to zero and one; the nonzero set is closed under differences and integer multiples, and a prime-factor condition pins it to the multiples of five.',r'''Set $x=y=0$ in (i). Since $f(0)\ne0$, it gives $f(0)=1$. Then (ii) with $y=0$ implies $(f(x)-1)f(x)=0$, so every value is $0$ or $1$. Both occur, since $f(0)=1$ and $f(1)=0$.

For part (b), let $S=\{n:f(n)=1\}$. Identity (i) says that if either factor lies in $S$, its product does; conversely, if a product lies in $S$, at least one factor does. Identity (ii) says that $S$ is closed under differences.

Since $10\in S$ but $2\notin S$, we get $5\in S$, and therefore every multiple of $5$ belongs to $S$. If some integer $t$ not divisible by $5$ belonged to $S$, choose an integer $u$ with $ut\equiv1\pmod5$. Both $ut$ and $ut-1$ would belong to $S$, so their difference $1$ would too, a contradiction. Hence $S=5\mathbb Z$. The function equal to one on multiples of five and zero elsewhere satisfies both identities, verifying existence.''')
# Problem 5 is absent from MathNet and restored from the official booklet.
slug='ind_2012_official_q5'
raw={'country':'India','competition':'Indian National Mathematical Olympiad (INMO)','year':2012,'section':'','problem_number':'5','problem_markdown':r'''In acute triangle $ABC$, points $D,E,F$ lie on $BC,CA,AB$, respectively. Suppose $AD$ is a median, $BE$ is an internal angle bisector, and $CF$ is an altitude. If $\angle FDE=\angle C$, $\angle DEF=\angle A$, and $\angle EFD=\angle B$, prove that $ABC$ is equilateral.''','solutions_markdown':[],'primary_domain':'Geometry','topics':[],'booklet_title':'Problems and Solutions: INMO-2012','sourceDataset':'HBCSE official archive','sourceLicense':'Mathematical statement paraphrased; official worked solution linked.'}
(RAW/(slug+'.json')).write_text(json.dumps(raw,ensure_ascii=False,indent=2))
ind(slug,6.5,'The midpoint of the hypotenuse fixes one side of DEF; its similarity with ABC and two sine-rule computations produce a cubic that factors as a squared side difference.',solutionKind='source-link')
if slug not in {x[0] for x in m}:m.append([slug,'india-official',2012,'INMO',2,0,'5'])
(P/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));(P/'manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2))
print('China2020 CMC20 assessed/4 included; INMO2012 all6 assessed/included')
