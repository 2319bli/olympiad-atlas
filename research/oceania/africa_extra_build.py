import json
P='/workspace/sites/olympiad-atlas/research/oceania/'
items=[];ledger=[]
TN21='https://ef9a8b7a-aca5-4792-bda3-7f88edc1de0a.filesusr.com/ugd/bed7ad_82406275d1f34533a3d79819cb786592.pdf'
TN22='https://ef9a8b7a-aca5-4792-bda3-7f88edc1de0a.filesusr.com/ugd/bed7ad_101e10e7b1484968b4623cf5bac91276.pdf'
TN22SOL='https://ef9a8b7a-aca5-4792-bda3-7f88edc1de0a.filesusr.com/ugd/bed7ad_474924e16e3740f29decbe0ab47ba37c.pdf'
def meta(c,y,sec,n):
 comp=('Tunisian Mathematical Olympiad — National Preselection' if y==2021 else 'Tunisian Mathematical Olympiad — Sfax/Hammamet Test') if c=='Tunisia' else 'Algerian Mathematical Olympiad'
 u=(TN21 if y==2021 else TN22) if c=='Tunisia' else f'https://almo2025.com/{sec.lower()}-day{1 if n<=3 else 2}.pdf'
 return dict(id=f'{"tun" if c=="Tunisia" else "dza"}_{y}_{sec.lower()}_{n}',country=c,competition=comp,year=y,section=sec,number=str(n),sourceUrl=u)
def add(c,y,sec,n,d,t,tags,s,sol,r):
 m=meta(c,y,sec,n); items.append(dict(**m,statement=s,solution=sol,solutionUrl=TN22SOL if c=='Tunisia' and y==2022 else None,topic=t,tags=tags,difficulty=d,ratingReason=r,reviewStatus='individually-assessed',solutionKind='original-exposition',notes=('Official ATSM paper; English paraphrase and independently written proof. ' if c=='Tunisia' else 'Official ALMO2025 English paper; independently written statement and proof. Live organiser site intermittently returns502, but indexed PDF text was recovered. ')))
 ledger.append(dict(**m,difficulty=d,status='reviewed',included=True,reason=r))
def skip(c,y,sec,n,d,r,status=None):ledger.append(dict(**meta(c,y,sec,n),difficulty=d,status=status or ('reviewed' if d is not None else 'pending-solution-review'),included=False,reason=r))
skip('Tunisia',2021,'',1,None,'The printed nonzero-real domain makes the claim false:3,3,−4/3 have pair-product sum1, but every remaining two-term sum exceeds sqrt2. A positivity assumption would repair it; withheld rather than silently changing the domain.','withheld-malformed')
add('Tunisia',2021,'',2,4.5,'Number Theory',['permutations','constructive proof','modular obstruction'],r'Call a permutation $a_1,\ldots,a_n$ of $1,\ldots,n$ square if every $a_i a_{i+1}+1$ is a perfect square. Construct square permutations for infinitely many $n$. Show that no permutation of $1,\ldots,n$, for any $n\ge2$, can instead make all these expressions perfect cubes.',r'''For every odd integer $k\ge3$, take $n=k^2-1$ and use
$$2,4,6,\ldots,n,1,3,5,\ldots,n-1.$$
Within each parity block, successive terms differ by two, and $a(a+2)+1=(a+1)^2$. At the join, $n\cdot1+1=k^2$. This gives infinitely many square permutations.

For the cubic condition, let $a=2^k$ be the largest power of2 not exceeding $n$, so $a\le n<2a$ and $a\ge2$. It must have some neighbour $b$ in the permutation. If $ab+1=t^3$, then $t$ is odd and
$$ab=(t-1)(t^2+t+1).$$
The second factor is odd, so $a\mid t-1$, giving $t\ge a+1$. Therefore
$$b\ge\frac{(a+1)^3-1}{a}=a^2+3a+3>n,$$
a contradiction.''','A parity-block construction gives infinitely many square cases; choosing the largest power of2 creates the cubic obstruction via a sharp size bound.')
skip('Tunisia',2021,'',3,2,'Each element independently belongs to the first subset, the second, or neither, giving3^n for the ordered interpretation used by the supplied scaffold.')
add('Tunisia',2021,'',4,4.5,'Geometry',['coordinates','angle doubling','squares'],r'Let $ABCD$ be a square. Choose $N\in AB$ and $P\in AD$ so that $PN=NC$, then choose $Q\in AN$ satisfying $\angle NCB=\angle QPN$. In a nondegenerate configuration, prove that $\angle BCQ=\tfrac12\angle PQA$.',r'''Scale the square to $A=(0,0),B=(1,0),C=(1,1),D=(0,1)$, and write $P=(0,p),N=(n,0),Q=(q,0)$. The distance condition gives
$$n^2+p^2=(1-n)^2+1,\qquad n=1-\frac{p^2}{2}.$$
The equal-angle condition, using their tangents, becomes
$$1-n=\frac{p(n-q)}{p^2+nq}.$$
Substituting for $n$ and solving yields
$$q=\frac{2n-p^3}{2+pn}=\frac{2(1-p)}{2-p}.$$
The endpoint cases make one of the stated angles degenerate; thus $0<p<1$ and $0<q<1$.

Put $\theta=\angle BCQ$. Then $\tan\theta=1-q=p/(2-p)$, so $0<\theta<45^\circ$ and
$$\tan(2\theta)=\frac{2(1-q)}{1-(1-q)^2}=\frac pq=\tan\angle PQA.$$
Both doubled and target angles lie between $0$ and $90^\circ$, proving the equality.''','The equal-distance condition controls the free parameter, and the second angle condition must be converted and simplified before a double-angle identity closes the proof.')
add('Tunisia',2022,'',1,4,'Geometry',['radical axis','homothety','reflection'],r'Two circles meet at $M,N$. Their common external tangent nearer to $M$ touches them at $A,B$. The line through $M$ parallel to $AB$ meets the circles again at $C,D$, respectively. Let $E=CA\cap DB$, $P=AN\cap CD$ and $Q=BN\cap CD$. Prove that $MN$ passes through the midpoint of $AB$ and that $EP=EQ$.',r'''Let $I=MN\cap AB$. As $MN$ is the radical axis, $IA^2=IB^2$ by the tangent form of power of a point, so $I$ is the midpoint of $AB$. The homothety centred at $N$ taking line $AB$ to its parallel $CD$ sends $A,B,I$ to $P,Q,M$. Hence $M$ is the midpoint of $PQ$.

It remains to show $EM\perp CD$. Use coordinates with $AB$ horizontal: $A=(a,0),B=(b,0),M=(m,h)$. Each circle's centre lies vertically above or below its tangency point. Therefore its horizontal chord through $M$ has that vertical line as perpendicular bisector, giving
$$C=(2a-m,h),\qquad D=(2b-m,h).$$
The point $(m,-h)$ lies on both $AC$ and $BD$, so it is $E$. Thus $EM$ is vertical, while $PQ$ is horizontal. Since $M$ is its midpoint, $E$ lies on the perpendicular bisector of $PQ$, proving $EP=EQ$.''','The radical-axis midpoint must be transported to a second line; recognizing the reflected intersection then supplies the perpendicular bisector.')
skip('Tunisia',2022,'',2,3,'Substitute1/x and−x into f(−x)/x+f(1/x)=x; elimination gives f(x)=x²/2+1/(2x), verified directly.')
skip('Tunisia',2022,'',3,1.5,'Squares modulo8 are0,1,4; no sum of two such residues equals2022≡6.')
# Algeria: all recovered Senior/Junior papers, and Benjamin Day1.
add('Algeria',2025,'Senior',1,4,'Geometry',['power of a point','similar triangles','parallel lines'],r'In acute triangle $ABC$, let $D$ be the second intersection of the internal bisector of $\angle BAC$ with its circumcircle. Choose $E$ on ray $DC$ so that circle $ACE$ meets segment $BC$ again at $F$. Line $DF$ meets circle $ABC$ again at $G$, and circle $ACF$ again at $H$. Prove that $GC\parallel HE$.',r'''Since $D$ is the midpoint of arc $BC$ not containing $A$, $DB=DC$. The cyclic angles give
$$\angle DGC=\angle DBC=\angle DCB=\angle DCF,$$
while $\angle GDC=\angle CDF$. Thus triangles $DGC$ and $DCF$ are similar, yielding
$$DF\cdot DG=DC^2.$$
The circle through $A,C,E,F$ gives, by power of $D$,
$$DF\cdot DH=DC\cdot DE.$$
Dividing the two identities gives $DH/DG=DE/DC$. As $D,H,G$ and $D,E,C$ are collinear, the converse of the intercept theorem gives $HE\parallel GC$. Directed lengths cover the possible orders on the rays.''','The decisive step is an isosceles arc-midpoint similarity; comparing its product identity with a second circle power produces the required homothety.')
add('Algeria',2025,'Senior',2,4.5,'Number Theory',['coprime factorization','prime powers','perfect squares'],r'Find all positive integers $a,b$ for which $ab$ is a perfect square and $a^2+ab+b^2=p^k$ for some prime $p$ and positive integer $k$.',r'''Exactly $a=b=3^t$ for integers $t\ge0$ work, with $p=3,k=2t+1$.

Put $d=\gcd(a,b)$. Since $ab$ is square and the quotients are coprime, write $a=du^2,b=dv^2$ with coprime positive integers $u,v$. Then
$$p^k=d^2(u^2+uv+v^2)(u^2-uv+v^2).$$
The two last factors are odd, and any common divisor divides $2uv$. Each is coprime to $uv$, so their gcd is1. Because their product is a prime power, the smaller factor must equal1. But
$$u^2-uv+v^2=(u-v)^2+uv\ge1,$$
with equality only at $u=v=1$. Hence $a=b=d$ and $3d^2=p^k$, forcing $p=3,d=3^t$. Direct substitution verifies all these pairs.''','One must exploit the square product before factoring a quartic; coprimality of the two quadratic factors forces equality of the original variables.')
add('Algeria',2025,'Senior',3,5.5,'Algebra',['functional equations','surjectivity','rational domain'],r'''Find every surjective function $f:\mathbb Q\setminus\{0\}\to\mathbb Q\setminus\{0\}$ satisfying
$$(f(x)+f(y))f(x+y)=f(xy)$$
whenever $x,y$ and $x+y$ are nonzero rationals.''',r'''The unique solution is $f(x)=1/x$.

For any $x$, surjectivity provides $y$ with $f(y)=-f(x)$. If $x+y\ne0$, the displayed equation has zero left side and nonzero right side. Thus $y=-x$, proving oddness. The same argument shows injectivity: if $f(u)=f(v)$, then $f(u)+f(-v)=0$ forces $u=v$.

Taking $x=y=1$ gives $f(2)=1/2$, so $f(-2)=-1/2$. Write $c=f(1)$. The pair $(1,-2)$ gives
$$(c-1/2)(-c)=-1/2,$$
so $c=1$ or $-1/2$. The latter would make $f(1)+f(2)=0$ despite $1+2\ne0$, impossible. Thus $f(1)=1$.

Set $h(x)=1/f(x)$. It is odd and injective, and using the pair $(1,x)$ gives
$$h(x+1)=h(x)+1\qquad(x\ne0,-1).$$
Hence $h(n)=n$ for every nonzero integer, and repeated translation gives $h(x+n)=h(x)+n$ for nonintegral rational $x$ and positive integer $n$.

Rewriting the original equation with $y=n$ now gives
$$h(x)+n=\frac{(h(x)+n)h(nx)}{n h(x)}.$$
The factor $h(x)+n$ is nonzero: otherwise injectivity and $h(-n)=-n$ would imply $x=-n$. Therefore $h(nx)=nh(x)$. For $x=a/b$ with positive integer $b$ and nonzero integer $a$, take $n=b$ to obtain $h(x)=a/b=x$. The integral cases were already settled. Thus $f(x)=1/x$, which satisfies the equation and is surjective.''','Surjectivity first forces both oddness and injectivity; reciprocal substitution then turns the equation into integer translations and rational homogeneity.')
skip('Algeria',2025,'Senior',4,3.5,'Put p=xyz. The pair-product constraint gives sqrt(p)(sqrt(x)+sqrt(y)+sqrt(z))=sum sqrt((xy)(xz))≤3. Then2sqrt(p)≤1+p proves the claimed inequality.')
skip('Algeria',2025,'Senior',5,3,'Only initially occurring values are ever selected. All their counts eventually reach the initial maximum, after which selection cycles through the distinct values in increasing order.')
skip('Algeria',2025,'Senior',6,None,'Multi-circle tangent-concurrence statement recovered; full proof not yet established.')
skip('Algeria',2025,'Junior',1,2.5,'Setting x=0 gives idempotence. The original equation reduces to f(t+x)+f(x)=2x+f(t); setting t=0 and then x=0 forces f(0)=0 and f(x)=x.')
skip('Algeria',2025,'Junior',2,None,'Cyclic parallel-chord construction with angleB=3angleC; proof still pending.')
skip('Algeria',2025,'Junior',3,2.5,'Strict divisibility increases total prime-factor multiplicity by at least one;2024=2³·11·23 gives the maximum chain length10125. The Day1 PDF mistakenly labels this third question Problem6.')
skip('Algeria',2025,'Junior',4,1.5,'For each k from1 through8, nine integers contain two congruent modulo k by pigeonhole, so k divides their difference.')
add('Algeria',2025,'Junior',5,4.5,'Number Theory',['coprime factors','Diophantine equations','parity'],r'Find all nonnegative integers $x,y$ and primes $p$ such that $x^2=p-2$ and $y^2=2p^2-2$.',r'''The only triple is $(x,y,p)=(1,4,3)$.

If $p=2$, then $x=0$ but $y^2=6$, impossible. Thus $p$ is odd and $x$ is odd. Substituting $p=x^2+2$ gives
$$y^2=2(x^2+1)(x^2+3).$$
Write $a=(x^2+1)/2$ and $b=(x^2+3)/4$. Both are positive odd integers, since $x^2\equiv1\pmod8$, and $2b-a=1$, so $\gcd(a,b)=1$. The equation is $y^2=16ab$, hence $ab$ is square. Coprimality makes each factor square, say $b=v^2$.

Consequently $x^2+3=4v^2$, or
$$(2v-x)(2v+x)=3.$$
Both factors are positive integers, so they are1 and3. This yields $x=1,v=1$, then $p=3,y=4$, which indeed satisfy the equations.''','Substitution exposes two near-consecutive factors, but parity and their exact gcd are needed before a square factor collapses the equation.')
add('Algeria',2025,'Junior',6,4.5,'Geometry',['orthocentres','coordinates','midpoints'],r'In triangle $ABC$, the altitude feet from $A,B,C$ are $D,E,F$, and the orthocentre $H$ is the midpoint of $CF$. Let $M,N$ be the midpoints of $BC,BE$, respectively, and let $X=AN\cap MF$. Prove that $HX\perp XM$.',r'''Take $A=(0,0),B=(b,0),C=(c,h)$ with $b,h>0$. Then $F=(c,0)$ and $H=(c,h/2)$. Since $BH\perp AC$,
$$h^2=2c(b-c).$$
Projecting $B$ onto $AC$ gives
$$E=\left(\frac{bc^2}{c^2+h^2},\frac{bch}{c^2+h^2}\right).$$
Using $c^2+h^2=c(2b-c)$, the midpoint $N$ has coordinates
$$N=\left(\frac{b^2}{2b-c},\frac{bh}{2(2b-c)}\right).$$
Thus $AN$ has slope $h/(2b)$, while $MF$ has slope $h/(b-c)$. Their intersection is
$$X=\left(\frac{2bc}{b+c},\frac{ch}{b+c}\right).$$
Now $X-H$ is a scalar multiple of $(c,-h/2)$, and a direction vector of $MF$ is $(b-c,h)$. Their dot product is $c(b-c)-h^2/2=0$. Therefore $HX\perp MF$, as required.''','The midpoint condition on the orthocentre supplies a non-obvious metric relation; projecting an altitude foot then makes the two midpoint lines computable.')
skip('Algeria',2025,'Benjamin',1,2.5,'Modulo n²+n+1, n³≡1 so the numerator leaves n+62. A size bound leaves0≤n≤7, and direct checking yields n=0,1,3 (or1,3 if natural excludes0).')
skip('Algeria',2025,'Benjamin',2,2,'Termwise AM-GM gives2k/45 and total46; equality in every term forces a_k=1/(45k).')
skip('Algeria',2025,'Benjamin',3,None,'Circle/altitude/circumcentre construction recovered; two intersections in the printed F definition require visual clarification, and proof remains pending.')
json.dump(items,open(P+'africa-extra.json','w'),indent=2)
json.dump(ledger,open(P+'africa-extra-ledger.json','w'),indent=2)
print(len(items),len(ledger))
