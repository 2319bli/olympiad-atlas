from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');raw=p/'international-raw';r=json.loads((p/'international-reviews.json').read_text())
def add(year,num,topic,rating,reason,statement,solution='',tags=None):
 slug=f'imo_{year}_official_p{num}'
 d={'id':slug,'competition_code':'IMO','competition':'IMO','year':year,'problem_number':str(num),'primary_domain':topic,'topics':[[topic,t] for t in (tags or [])],'problem_markdown':statement,'solutions_markdown':[solution],'officialSourceUrl':f'https://www.imo-official.org/assets/documents/problems/{year}/{year}_eng.pdf','officialSolutionUrl':f'https://www.imo-official.org/assets/documents/problems/{year}/IMO{year}SL.pdf' if year==2025 else 'https://web.evanchen.cc/exams/IMO-2026-notes.pdf'}
 (raw/(slug+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2));r[slug]=[rating,reason]
add(2025,1,'Combinatorics',5.5,'Count the boundary points to force deletion of a triangle side, then resolve the exceptional three-row configuration and construct all three possible counts.',r'''Call a line sunny if it is parallel to none of the lines $x=0$, $y=0$, $x+y=0$. Fix an integer $n\geq3$. Which nonnegative integers $k$ are possible if $n$ distinct lines cover all points $(a,b)$ with positive integer coordinates satisfying $a+b\leq n+1$, and exactly $k$ of the lines are sunny?''',r'''The possibilities are $k=0,1,3$.

For $n>3$, the boundary of the triangular array contains $3n-3>2n$ points. A line which is not one of the three boundary lines meets this boundary in at most two points. Thus any cover by $n$ lines contains a boundary line. Remove it and its $n$ boundary points. The remaining array is a translated triangular array of side length $n-1$, covered by the other $n-1$ lines. The number of sunny lines is unchanged. Repeating reduces to $n=3$.

For this six-point array a sunny line contains at most two points. Suppose there are exactly two sunny lines, with the third line ordinary. If that ordinary line covers at most one point, the total is at most five. If it covers two points, the four remaining points include three on a boundary line; two sunny lines cannot cover those three. If it covers three points, it is a boundary line, leaving a three-point triangle whose every joining line is ordinary, so two sunny lines again cannot cover it. This excludes $k=2$.

All other values for $n=3$ are attained: use the three vertical lines for $k=0$; use $x=1$, $y=1$ and a sunny line through $(2,2)$ for $k=1$; or use the three lines through the pairs
$$\{(1,1),(2,2)\},\quad\{(1,2),(3,1)\},\quad\{(1,3),(2,1)\}$$
for $k=3$. For larger $n$, cover the first $n-3$ vertical columns and apply one of these constructions to the remaining translated six-point triangle.''',['Covering','Invariants','Induction'])
add(2025,2,'Geometry',7,'The tangent is found at an unexpected fourth concyclic point. Two parallelograms, auxiliary cyclicities and a power-of-a-point ratio then identify the required parallel through the orthocentre.',r'''Circles $\Omega,\Gamma$ have centres $M,N$, with the radius of $\Omega$ smaller. They meet at distinct points $A,B$. Line $MN$ meets $\Omega$ at $C$ and $\Gamma$ at $D$, with $C,M,N,D$ in that order. Let $P$ be the circumcentre of $ACD$. Line $AP$ meets $\Omega$ again at $E\ne A$ and $\Gamma$ again at $F\ne A$. Let $H$ be the orthocentre of $PMN$. Prove that the line through $H$ parallel to $AP$ is tangent to the circumcircle of $BEF$.''',r'''Use directed angles throughout. The common chords $AC,AD$ of the circle $(ACD)$ with $\Omega,\Gamma$ show that $PM\perp AC$ and $PN\perp AD$. Since $PC=PD$,
$$\angle PAM=\angle MCP=\angle PDN=\angle NAP.$$
It follows that $EM\parallel NA$ and $FN\parallel MA$. Let $T=EM\cap FN$; then $AMTN$ is a parallelogram.

Points $A,B$ are reflections in $MN$, so $MBTN$ is an isosceles trapezium. Therefore $\angle TMB=\angle TNB$. Together with $EM=MB$ and $FN=NB$, this gives $\triangle EMB\sim\triangle FNB$. An angle chase now gives
$$\angle EBF=\angle MBN=\angle MTN=180^\circ-\angle FTE,$$
so $B,E,F,T$ are concyclic. Also $\angle EFT=\angle NAF=\angle TEF$, so $TE=TF$. The tangent to this circle at $T$ is consequently parallel to $EF$.

We must show that this tangent passes through $H$. Put $Q=AP\cap MN$. The earlier angle equality shows that $D,A,M,P$ are cyclic; likewise $C,P,N,A$ are cyclic. Powers of $Q$ give
$$QC\cdot QN=QA\cdot QP=QM\cdot QD,$$
using directed lengths. Thus $QM/QC=QN/QD=:k$. Choose $L$ on line $AQ$ with $QL/QA=k$. Similar triangles give $ML\parallel CA$ and $NL\parallel DA$.

Since $HN\perp PM$ and $HM\perp PN$, we have $HN\parallel AC$ and $HM\parallel AD$. Thus $LMHN$ is a parallelogram. Comparing it with $AMTN$ gives $\overrightarrow{TH}=\overrightarrow{AL}$, which is parallel to $AP$. Hence the line through $H$ parallel to $AP$ is exactly the tangent at $T$.''',['Circles','Power of a point','Parallelograms'])
add(2025,3,'Number theory',8.5,'The argument first separates the identity function from all other functions through prime inputs, eliminates every odd prime factor, then needs a sharp 2-adic bound and an exceptional construction.',r'''A function $f:\mathbb Z_{>0}\to\mathbb Z_{>0}$ is called bonza when
$$f(a)\mid b^a-f(b)^{f(a)}$$
for every positive integers $a,b$. Determine the least real number $c$ such that $f(n)\leq cn$ for every bonza function and every positive integer $n$.''')
add(2025,4,'Number theory',6,'Two descending-sequence obstructions force divisibility by six. A case split on the third-smallest divisor then tracks powers of two and three to classify all possible starting values.',r'''An infinite sequence $a_1,a_2,\ldots$ consists of positive integers, each having at least three proper positive divisors. For every $n\geq1$, the next term $a_{n+1}$ is the sum of the three largest proper divisors of $a_n$. Determine all possible initial values $a_1$.''',r'''Exactly the numbers
$$a_1=6\cdot12^m u,\qquad m\geq0,\quad u\geq1,\quad\gcd(u,10)=1$$
work.

An odd term would be followed by an odd term at most $(1/3+1/5+1/7)$ times as large. This would give an infinite strictly decreasing sequence of positive integers. Hence every term is even.

Suppose a term $a$ is not divisible by three. If $4\mid a$, its next term is $3a/4+d$, where $d$ is another divisor of $a$, so it is still not divisible by three. If $4\nmid a$, let $p$ be its least odd prime factor. The two largest proper divisors are $a/2$ and $a/p$. Since the next term must be even, the third divisor must be odd, and therefore equals $a/(2p)$. The next term is $a/2+3a/(2p)$, again not divisible by three. In either case the next term is at most $(1/2+1/4+1/5)a<a$. This produces the same impossible descent. Therefore every term is divisible by six.

There are now only three transitions:
$$a\longmapsto
\begin{cases}
13a/12,&4\mid a,\\
31a/30,&4\nmid a,\ 5\mid a,\\
a,&4\nmid a,\ 5\nmid a.
\end{cases}$$
The middle case gives an odd next term and is impossible. Each use of the first case reduces the exponent of two by two, so only finitely many can occur. The sequence must eventually be fixed at $6u'$ with $\gcd(u',10)=1$. If there were $m$ nonconstant steps, reversing them yields $a_1=6\cdot12^m u$, where $u=u'/13^m$ is a positive integer coprime to ten. Integrality follows because $13^m$ is coprime to $6\cdot12^m$.

Conversely, such a starting value follows
$$a_j=6\cdot12^{m+1-j}13^{j-1}u\quad(1\leq j\leq m+1),$$
then remains equal to $6\cdot13^m u$. All these terms have the required divisors.''',['Divisors','Descent','Valuations'])
add(2025,5,'Combinatorics',6.5,'The three parameter regimes require two different strategies: saturating a quadratic budget and saving a linear budget for one large move, with a separate boundary draw proof.',r'''Fix $\lambda>0$. Alice and Bazza choose nonnegative real numbers $x_1,x_2,\ldots$ in alternating turns. On odd turn $n$, Alice must ensure $x_1+\cdots+x_n\leq\lambda n$. On even turn $n$, Bazza must ensure $x_1^2+\cdots+x_n^2\leq n$. A player with no legal move loses; an infinite game has no winner. Both players know all previous choices. Determine the values of $\lambda$ for which each player has a winning strategy.''',r'''Alice wins for $\lambda>1/\sqrt2$, Bazza wins for $\lambda<1/\sqrt2$, and neither can force a win at equality.

For $\lambda\leq1/\sqrt2$, Bazza can choose
$$x_{2j}=\sqrt{2-x_{2j-1}^2}.$$
Inductively the sum of squares after his move equals $2j$, and Alice's next available choice is at most $\lambda$. Indeed each completed pair has sum at least $\sqrt2$, so before Alice's turn $2j+1$ the sum is at least $j\sqrt2$ and she has room at most $\lambda(2j+1)-j\sqrt2\leq\lambda$. Thus Bazza's response is always real and legal. If $\lambda<1/\sqrt2$, eventually $j\sqrt2>\lambda(2j+1)$, so Alice has no legal move.

For $\lambda\geq1/\sqrt2$, Alice can choose zero on each of her turns indefinitely. After $2j$ turns, Cauchy–Schwarz bounds the sum of Bazza's $j$ choices by $\sqrt{j\cdot2j}=j\sqrt2\leq\lambda(2j+1)$, so another zero is legal. This already gives her a nonlosing strategy at equality.

If $\lambda>1/\sqrt2$, choose a sufficiently large $j$ that
$$u_j:=\lambda(2j+1)-j\sqrt2>\sqrt{2j+2}.$$
After playing zero for her first $j$ turns, Alice plays $u_j$. The same Cauchy–Schwarz bound makes this legal. Its square alone exceeds Bazza's entire budget on turn $2j+2$, so he loses. At equality Bazza's first strategy and Alice's zero strategy each prevent their owner from losing, so neither has a winning strategy.''',['Games','Cauchy–Schwarz','Strategies'])
add(2025,6,'Combinatorics',9,'The sharp lower bound needs a global barrier and disjoint alternating chains through the exposed squares, followed by an extremal chain count; the matching rectangular construction is also highly structured.',r'''Place nonoverlapping rectangular tiles on a $2025\times2025$ grid of unit squares, with every tile side on a grid line. Exactly one unit square in each row and exactly one in each column must remain uncovered. What is the minimum possible number of tiles?''')
add(2026,1,'Number theory',5.5,'Termination needs a two-part decreasing quantity; uniqueness is a separate invariant, the gcd of the exponents of each prime, revealed by the Euclidean algorithm.',r'''Initially a blackboard contains 2026 integers greater than one, repetitions allowed. A move chooses two entries $m,n>1$ and replaces them by
$$\gcd(m,n),\qquad\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}.$$
Moves continue whenever possible. Prove that the process always stops after finitely many moves with exactly one entry $M>1$, and that $M$ is independent of all choices.''',r'''Let $P$ be the product of all entries and let $r$ be the number of entries greater than one. If $g=\gcd(m,n)>1$, the product changes from $P$ to $P/g<P$. If $g=1$, the product is unchanged but the pair becomes $(1,mn)$, so $r$ decreases. Thus the pair $(P,r)$ decreases lexicographically in positive integers, and the process terminates. A move never removes the last entry greater than one, while two such entries would permit another move. The terminal board therefore has exactly one such entry.

Fix a prime $p$. If its exponents in the chosen entries are $a,b$, its new exponents are $\min(a,b)$ and $|a-b|$. Their gcd equals $\gcd(a,b)$, so the gcd of the $p$-exponents across the entire board is invariant. At termination this gcd is $v_p(M)$, since all the other exponents are zero. Therefore, if the original entries were $t_1,\ldots,t_{2026}$,
$$v_p(M)=\gcd(v_p(t_1),\ldots,v_p(t_{2026})).$$
This determines every prime exponent of $M$ uniquely.''',['Invariants','Euclidean algorithm','Valuations'])
add(2026,2,'Geometry',6.5,'The angle hypotheses become three cyclic quadrilaterals. The main discovery is a circle through two auxiliary midpoints and both interior points, allowing equality of powers to settle the centre distances.',r'''Let $M,N$ be the midpoints of sides $AB,AC$ of triangle $ABC$. Choose $K,L$ strictly inside triangles $BMC,BNC$, respectively, with $K$ strictly inside $ABL$ and $L$ strictly inside $AKC$. Suppose
$$\angle KBA=\angle ACL,\qquad\angle LBK=\angle LNC,\qquad\angle LCK=\angle BMK.$$
If $O$ is the circumcentre of $AKL$, prove $OM=ON$.''',r'''All products below use directed lengths. Set $X=BK\cap AC$ and $Y=CL\cap AB$. The three angle conditions imply that $B,Y,X,C$ are cyclic, that $X,N,L,B$ are cyclic, and that $Y,M,K,C$ are cyclic. Since $M,N$ are midpoints, the first cyclicity also yields
$$AY\cdot AM=AX\cdot AN.$$

Let $E,F$ be the midpoints of $BY,CX$. We show that $A,E,F,K,L$ lie on one circle. Let line $XK$ meet $(YMKC)$ again at $K'$, and line $AC$ meet it again at $C'$. Powers of $A$ give
$$AC'\cdot AC=AY\cdot AM=AX\cdot AN=\tfrac12 AX\cdot AC,$$
so $C'$ is the midpoint of $AX$. Consequently
$$XK\cdot XK'=XC'\cdot XC=XA\cdot XF,$$
and
$$BK\cdot BK'=BM\cdot BY=BA\cdot BE.$$
The converse power-of-a-point theorem makes $A,F,K,K'$ cyclic and $A,E,K,K'$ cyclic, so $K$ lies on $(AEF)$. The symmetric argument using $(XNLB)$ shows that $L$ does too. Intersections are counted with multiplicity if a line is tangent; the same power argument applies.

Finally, $ME=AY/2$ and $NF=AX/2$. Hence the powers of $M,N$ with respect to $(AEF)=(AKL)$ agree, because
$$AM\cdot ME=\tfrac12 AM\cdot AY=\tfrac12 AN\cdot AX=AN\cdot NF.$$
Writing these powers as $OM^2-R^2$ and $ON^2-R^2$, where $R$ is the common circumradius, gives $OM=ON$.''',['Power of a point','Circles','Midpoints'])
add(2026,3,'Combinatorics',8.5,'The minimax value requires matching cuts for nearly equal subset sums and a separate lower bound for a powers-of-two division, using a graph component or a strengthened induction.',r'''Two players divide a unit stick. First Liu marks at most $n$ points; then Xiang marks at most $n$ further points, all marks distinct. Cutting at every mark produces pieces, which the players then choose alternately, Liu first. Each maximises their own total length. For every positive integer $n$, determine the largest total length Liu can guarantee regardless of Xiang's choices.''')
add(2026,4,'Combinatorics',6,'The winning angles arise from an integer-multiple reduction and a right-triangle cut. The converse needs a stronger invariant excluding every integer multiple, rather than just the target angle.',r'''Fix an angle $0^\circ<\theta<180^\circ$. Shan-Yu chooses an initial paper triangle. If the current triangle has an angle $\theta$, Mulan wins. Otherwise Mulan cuts from a vertex to a nonvertex point of the opposite side, obtaining two triangles, and Shan-Yu chooses which one is retained. For which $\theta$ can Mulan force a win in finitely many cuts, whatever the initial triangle and Shan-Yu's choices?''',r'''Exactly $\theta=180^\circ/n$ for integers $n\geq2$ work.

First, any triangle with an angle $k\theta$ is winning: split that angle into $\theta$ and $(k-1)\theta$, and use induction on $k$. Suppose now $\theta=180^\circ/n$. Cut along an altitude from a largest-angle vertex to obtain a right triangle. For $n=2$ this already wins. Otherwise choose an integer $k$ with $45^\circ<k\theta\leq90^\circ$. In the right triangle $ABC$, let $\angle A=90^\circ$ and $\angle B\leq45^\circ$. There is an interior point $D$ of $BC$ for which $\angle BAD=k\theta-\angle B$, so $\angle ADC=k\theta$. The other triangle has angle $\angle ADB=(n-k)\theta$. Whichever is retained has an integer multiple of $\theta$, so the preceding induction finishes.

Conversely suppose $180^\circ$ is not an integer multiple of $\theta$. Call a triangle safe if none of its angles is an integer multiple of $\theta$, and choose a safe initial triangle. Such a choice is possible because only finitely many angles in $(0,180^\circ)$ are forbidden.

If a cut splits the old angle $\alpha$ into $u,v$, the new angles at the cut point are $\delta,180^\circ-\delta$. The other two old angles $\beta,\gamma$ remain safe. If both resulting triangles were unsafe, the offending pair would be one of
$$ (u,v),\quad(\delta,180^\circ-\delta),\quad(u,180^\circ-\delta),\quad(\delta,v).$$
The first would make $\alpha$ a multiple of $\theta$; the second would make $180^\circ$ one; the third would make $\beta=180^\circ-\delta-u$ one; the fourth would make $\gamma=\delta-v$ one. Each is impossible. Thus Shan-Yu can always retain a safe triangle and avoid the target forever.''',['Games','Geometry','Invariants'])
add(2026,5,'Algebra',6.5,'Equality at a composed input yields arithmetic function iterates. One must then prove monotonicity of both the function and its displacement and rule out a mixture of fixed and translated points.',r'''Find all functions $f:(0,\infty)\to(0,\infty)$ such that for all $x,y>0$,
$$\sqrt{\frac{x^2+f(y)^2}{2}}\ \geq\ \frac{f(x)+y}{2}\ \geq\ \sqrt{x f(y)}.$$''',r'''The solutions are $f(x)=x+c$ with $c\geq0$; substitution gives the usual quadratic-mean, arithmetic-mean and geometric-mean inequalities for $x$ and $y+c$.

Set $x=f(t)$ in both bounds. Their outside expressions are both $f(t)$, so
$$f(f(t))=2f(t)-t.$$
Thus $f^j(t)=t+jg(t)$, where $g(t)=f(t)-t$. Positivity for every $j$ implies $g(t)\geq0$.

The lower bound, applied to $(f(x),y)$, gives
$$x-y\leq2f(x)-2\sqrt{f(x)f(y)}.$$
Therefore $x>y$ forces $f(x)>f(y)$: $f$ is strictly increasing. Comparing its iterates at $x<y$ now gives $x+jg(x)<y+jg(y)$ for every $j$, hence $g(x)\leq g(y)$. So $g$ is nondecreasing.

If $g(t)=c>0$, then $g(f^j(t))=c$ for every $j$. Monotonicity and $f^j(t)=t+jc\to\infty$ imply $g(x)=c$ for all $x\geq t$. Any other positive value of $g$ must therefore equal $c$. Thus either $g$ is identically zero, or $g(x)\in\{0,c\}$ everywhere for one fixed $c>0$.

The two values cannot coexist. If $g(x)=c$ and $g(y)=0$ with $x>y$, the upper bound gives
$$\frac{x+y+c}{2}\leq\sqrt{\frac{x^2+y^2}{2}}<x,$$
so $x-y>c$. If $x<y$, the lower bound at $(y,x)$ gives $\sqrt{y(x+c)}\leq(x+y)/2<y$, so $y-x>c$. Consequently a point where $g=c$ cannot be within distance $c$ of a zero. Starting from one such point and moving to any other positive point in finitely many steps shorter than $c$ shows that there are no zeros. Therefore $g$ is constant and the stated family is complete.''',['Functional equations','Inequalities','Iteration'])
add(2026,6,'Number theory',8,'A finite-state description is hidden behind unbounded prime factors. The key induction shows every sufficiently large prime occurs only in a redundant term, after which a periodic residue-class argument applies.',r'''Let $a_1,a_2,\ldots$ be integers greater than one. For every $n$, let $a_{n+1}$ be the smallest integer greater than $a_n$ that shares a prime factor with each of $a_1,\ldots,a_n$. Prove that positive integers $T,L$ exist such that $a_{n+T}=a_n+L$ for every $n\geq1$.''')
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
