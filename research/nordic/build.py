"""Manual mathematical assessments from official Nordic national papers."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
rows=[]; decisions=[]; papers=[]
def paper(country,competition,year,source,solution,date,section='Final',complete=True):
    global ctx
    ctx=dict(country=country,competition=competition,year=year,sourceUrl=source,solutionUrl=solution,section=section)
    if len(date)==10:ctx['sittingDate']=date
    papers.append(ctx|{'complete':complete})
def add(num,rating,topic,statement,reason,tags,solution=None,notes=''):
    p=ctx|dict(id=f"nordic-{ctx['country'].lower()}-{ctx['year']}-{num}",number=num,difficulty=rating,topic=topic,statement=statement,ratingReason=reason,tags=tags,reviewStatus='individually-assessed',solutionKind='original-exposition' if solution else 'source-link',solutionCredit='Independent mathematical exposition for Olympiad Atlas' if solution else 'Official competition solutions',solution=solution or 'The organiser’s complete worked solution is linked below. '+('The PDF is in Norwegian.' if ctx['country']=='Norway' else 'The PDF is in Swedish.' if ctx['country']=='Sweden' else 'The PDF is in Danish.' if ctx['country']=='Denmark' else 'The PDF is in Icelandic.' if ctx['country']=='Iceland' else 'The PDF is in Finnish.'),notes='English mathematical paraphrase of the official paper. Year denotes the actual sitting year. '+notes)
    rows.append(p);decisions.append({k:p[k] for k in ['id','country','competition','year','section','number','difficulty','ratingReason']}|{'included':True})
def ex(num,rating,reason):
    decisions.append({k:ctx[k] for k in ['country','competition','year','section']}|dict(number=num,difficulty=rating,included=False,reason=reason))
nor26='https://www.matematikksenteret.no/sites/default/files/images/Abelkonkurransen/Abelkonkurransen2526/'
nor25='https://www.matematikksenteret.no/sites/default/files/attachments/Abelkonkurransen/abel-oppgaver/'
links=json.loads((R/'research/nordic/archive-links.json').read_text())['norway']
def norfile(name):return next(x['url'] for x in links if x['url'].endswith('/'+name))
paper('Norway','Abel Mathematical Competition',2026,norfile('Abel2025_f_en.pdf'),norfile('Abel2025_fl_nb.pdf'),'2026-03-10')
ex('1(a)',2,'Ordering a and b puts the smaller expression strictly between consecutive squares unless a=b.')
add('1(b)',5,'Number Theory',r'Write $S(n)=\sum_{j=1}^{n}j^j$. Prove that infinitely many positive integers $n$ share both their first decimal digit and their last decimal digit with $S(n)$.','Two separate mechanisms are needed: a sharp leading-term bound and periodicity of powers modulo ten, combined in a suitable infinite family.',['decimal digits','bounding','periodicity'])
add('2(a)',4.5,'Combinatorics',r'A stack initially reads $1,2,\ldots,n$ from top to bottom. Replace adjacent entries $b,a$ by $b-a$, inserting that new entry anywhere. Determine when repeated moves can leave only $0$.','Parity gives the obstruction, but sufficiency needs block constructions and the exceptional case n=3 must be excluded.',['invariant','construction','exceptional cases'])
ex('2(b)',7.5,'Finding the checkerboard edge invariant is only the first step; proving that it completely classifies move components requires a nontrivial local permutation construction and induction.')
add('3(a)',4.5,'Algebra',r'Find all positive-integer sequences $(a_n)_{n\ge1}$ such that, for each $n$, some positive integer $k$ satisfies $\sum_{i=1}^{k}a_n/a_{n+i}=k$.','The least term anchors an equality case; the resulting constant tail must then be propagated backwards.',['well-ordering','equality case','sequences'],r'''The constant positive-integer sequences work. Conversely, let $m$ be the least value occurring and choose $a_N=m$. Every summand $m/a_{N+i}$ is at most $1$. Their sum equals their number, so each is $1$, in particular $a_{N+1}=m$. Repeating at $N+1,N+2,\ldots$ shows that the whole tail equals $m$.

Now apply the equation at $N-1$. All its denominators equal $m$, giving $k a_{N-1}/m=k$, hence $a_{N-1}=m$. Continue backwards to obtain $a_n=m$ for every $n$.''')
add('3(b)',6.5,'Combinatorics',r'Choose $4052$ distinct nonzero integers $a_1,\ldots,a_{2026},b_1,\ldots,b_{2026}$. Maximise the number of pairs $i<j$ satisfying $2(a_ib_j+a_jb_i)^2=(a_i^2+b_i^2)(a_j^2+b_j^2)$.','An algebraic identity turns the relation into two rational involutions. Their four-element orbits expose a bipartite extremal problem; a distinct-integer construction completes it.',['identity','bipartite graph','extremal counting'])
add('4(a)',4.5,'Geometry',r'Inside triangle $ABC$, choose $D$. Points $E\in AC$ and $F\in AB$ satisfy $\angle ADE=\angle ABC$ and $\angle ADF=\angle ACB$. Prove that the circles $(ABC)$ and $(DEF)$ are tangent.','Angle addition reveals an extra concyclic point; the resulting similarity must then be interpreted as a homothety of the circles.',['cyclic quadrilaterals','homothety'])
add('4(b)',5.5,'Geometry',r'For triangle $ABC$, let $E,F$ satisfy $CE\perp BC$, $AE\perp AC$, $BF\perp BC$, $AF\perp AB$. Suppose $D=BC\cap EF$ exists. Prove that $AD$ is tangent to $(ABC)$.','The useful auxiliary circles are not stated. Combining their homothety with two power-of-a-point relations yields the required tangent criterion.',['auxiliary circles','power of a point','homothety'])
paper('Norway','Abel Mathematical Competition',2025,norfile('Abel2024_f_en.pdf'),norfile('Abel2024_fl_nb.pdf'),'2025-03-18')
add('1(a)',4.5,'Combinatorics',r'A row of $n\ge2$ coins starts heads-up. Players alternate: A flips any nonempty set of nonadjacent coins; B flips two adjacent coins. A starts and wins whenever all coins are tails. For which $n$ can B prevent this?','The winning threshold requires both small-case strategies and a local-pattern invariant which B can restore after every move.',['games','local patterns','invariant'])
add('1(b)',6,'Combinatorics',r'In a finite directed graph without loops, every vertex has an outgoing edge. Every $2025$-step walk from $G$ ends at $G$, and $H$ is reachable from $G$. For which positive integers $n$ is an $n$-step closed walk from $H$ necessarily impossible?','One must prove that reachable cycles all pass through G and have the same length; divisibility alone does not establish the necessary return-time restriction.',['directed graphs','cycles','periodicity'],notes='Equivalent graph formulation of the trophy-passing problem; a walk may repeat vertices.')
add('2(a)',4.5,'Number Theory',r'Eleven distinct positive integers are all below $10000$. Prove that some subset of at least two of them has nonintegral arithmetic mean.','Comparing subsets that differ in one entry forces simultaneous congruences. Their least common multiple then contradicts the available interval.',['subset sums','least common multiple','contradiction'])
add('2(b)',5.5,'Number Theory',r'Find every positive integer $a$ for which $n!-a$ is a square for infinitely many positive integers $n$.','Unbounded factorial divisibility must be converted into a condition modulo every integer. Prime-square descent then produces a final modular contradiction.',['factorials','valuations','descent'])
ex('3(a)',3,'The circle with diameter BC immediately gives a common midpoint for the two projected pairs, so EP=FQ.')
add('3(b)',6.5,'Geometry',r'An acute triangle $ABC$ has circumcentre $O$. Set $D=AO\cap BC$, $E=BO\cap CA$, $F=CO\cap AB$. If $ABC$ and $DEF$ are similar in the stated order, prove that $ABC$ is equilateral.','The substantial step is proving that the two circumcentres coincide. Angle comparisons and the specified similarity correspondence then force equal angles.',['circumcentre','similar triangles','angle comparison'])
add('4(a)',5,'Algebra',r'Find all real polynomials $P$ satisfying $P(1/(1+x))=1/(1+P(x))$ for every real $x\ne-1$.','A reciprocal-polynomial transformation controls the degree without calculus; constant solutions must be treated separately from P(x)=x.',['polynomial identity','degree','reciprocal substitution'])
add('4(b)',4.5,'Algebra',r'Find the greatest $C$ such that $1/x+1/(2y)+1/(3z)\ge C$ whenever nonzero real $x,y,z$ satisfy $x/(yz)+4y/(zx)+9z/(xy)=24$.','The variables need rescaling, and positivity cannot be assumed. A sum-of-squares identity supplies both the lower bound and an attainable equality case.',['inequalities','rescaling','equality case'])
paper('Norway','Abel Mathematical Competition',2024,norfile('Abel2023_f_en.pdf'),norfile('Abel2023_fl_nb.pdf'),'2024-03-05')
ex('1(a)',3,'Pairing coprime residues k and n−k reduces the condition to the parity of n; n=2 is checked directly.')
add('1(b)',5,'Algebra',r'Find all $f:\mathbb Z\to\mathbb Z$ for which $n,f(n),\ldots,f^{m-1}(n)$ have distinct residues modulo $m$, for every integer $n$ and every $m>1$. Here $f^j$ denotes iteration.','Choosing a modulus from f(n)−n forces unit steps, but the global classification allows a threshold separating leftward and rightward orbits.',['functional equation','iteration','modular arithmetic'])
add('2(a)',6.5,'Number Theory',r'For each $n\ge1$, minimise $a_n$ over positive integers $a_0<\cdots<a_n$ such that none of the differences $a_j-a_i$ ($i<j$) is prime.','A natural arithmetic progression is not optimal in every small case. A lower bound requires carefully grouping exceptional unit gaps and controlling neighbouring gaps.',['extremal construction','prime differences','gap analysis'])
add('2(b)',5.5,'Algebra',r'Find every $f:\mathbb R\to\mathbb R$ satisfying $x f(f(x)+y)=f(xy)+x^2$ for all real $x,y$.','Substitutions establish involutivity and f(x)=±x, but an additional argument is needed to rule out mixing the two signs at different inputs.',['functional equation','involution','sign consistency'])
add('3(a)',5,'Combinatorics',r'In an unknown finite connected graph, two vertices $A,B$ are distinguished. You know only the multiset of values $\max(d(v,A),d(v,B))$ over all vertices $v$, where distance counts edges. Find the smallest universal $N$ allowing $d(A,B)$ to be narrowed to at most $N$ possibilities.','A shortest-path midpoint gives a sharp two-value bound. Showing two are sometimes necessary requires two graphs with exactly the same observed multiset.',['graph distance','triangle inequality','sharp example'],r'''Let $\mu$ be the smallest listed value and put $d=d(A,B)$. The triangle inequality gives $d\le d(v,A)+d(v,B)\le2\max(d(v,A),d(v,B))$, so $d\le2\mu$.

A middle vertex of a shortest $A$–$B$ path has maximum distance $\lceil d/2\rceil$. Thus $\mu=\lceil d/2\rceil$ and $d\in\{2\mu-1,2\mu\}$. Two possibilities always suffice.

On a cycle of length four, choose adjacent vertices as $A,B$, or choose opposite vertices. In both cases the observed multiset is $\{1,1,2,2\}$, while the distances are respectively $1$ and $2$. Therefore $\boxed{N=2}$ is best possible.''',notes='The original wording has an ambiguous distance convention. This equivalent formulation uses edge distance explicitly; the answer N is unchanged. The original solution PDF has a sign typo in its two candidate distances; the exposition here corrects it.')
add('3(b)',6.5,'Combinatorics',r'Fill a $2\times2024$ array with $1,\ldots,4048$. A valid colouring selects one cell per column and $1012$ per row. Find the greatest $N$ such that every array admits a selected sum at least $N$. Count the arrays whose every selected sum is at most $N$.','Complementation gives the threshold, but the equality case forces constant column differences. Counting all compatible pairings then requires a divisibility classification.',['complementation','equality case','counting'])
add('4(a)',4.5,'Geometry',r'Triangle $ABC$ has $AB<AC$, altitude $AD$, and circumcentre $O$. A point $E$ on $(ABC)$ lies opposite $A$ across $BC$, with $AD=DE$ and $\angle ADO=\angle CDE$. Determine $\angle BAC$.','An equal-distance locus turns the angle condition into a restriction on the circumcentre; recognising the relevant perpendicular bisector is the main discovery.',['perpendicular bisector','circumcentre','angle chase'])
ex('4(b)',7.5,'The cyclic pentagon incenter configuration needs several auxiliary cyclic quadrilaterals, a long directed-angle argument, then a radical-axis concurrency chain.')
sw='https://www.mattetavling.se/s/'
paper('Sweden','Skolornas matematiktävling',2025,sw+'Final_2526.pdf',sw+'Finalloesningar_2526_fig.pdf','2025-11-22')
add('1',4,'Geometry',r'A convex pentagon $ABCDE$ has right angles at $A,B$ and $BC=CD=DE=EA=1$. Its diagonals $AC$ and $BD$ are perpendicular. Determine their lengths.','Orthogonality and repeated unit lengths conceal a rigid symmetric configuration; one must establish that rigidity before using standard special triangles.',['congruence','coordinates','special triangles'],r'''Take $A=(0,0)$, $B=(s,0)$, $C=(s,1)$ and $E=(0,1)$. Convexity and $CD=DE=1$ give $D=(s/2,1+h)$, where $h>0$ and $s^2/4+h^2=1$.

Since $AC\perp BD$, their direction vectors satisfy $(s,1)\cdot(-s/2,1+h)=0$, hence $s^2=2(1+h)$. Substitution gives $2h^2+h-1=0$, so $h=1/2$ and $s=\sqrt3$.

Consequently $\boxed{AC=2,\ BD=\sqrt3}$. (The official solution’s line saying $BC=2$ is a typo; the given $BC$ remains $1$.)''')
add('2',5,'Combinatorics',r'Six coins each weigh either $3$ or $4$ grams. Using a scale that reports exact total weight, prove that five weighings suffice to identify every coin’s weight.','Straight individual weighing is insufficient. A chain of pair measurements leaves a special alternating ambiguity which the final weighing must resolve together with the last coin.',['information','adaptive construction','weighing'])
add('3',4,'Algebra',r'Find all $f:\mathbb R\to\mathbb R$ such that $f^5(x+y)=f^2(x)+y+1$ for all real $x,y$, where superscripts denote iteration.','Making x+y constant exposes the second iterate. Substituting that affine iterate back into the fifth iterate determines f itself.',['functional equation','iteration','substitution'],r'''Set $y=-x$. There is a constant $c$ such that $f^2(x)=x+c$ for every $x$. Therefore $f^4(x)=x+2c$ and $f^5(x)=f(x+2c)$.

The equation with $y=0$ gives $f(x+2c)=x+c+1$. Replacing $x+2c$ by $t$ yields $f(t)=t+1-c$. Its second iterate is then $t+2-2c$, which must equal $t+c$. Hence $c=2/3$ and $\boxed{f(t)=t+1/3}$.

Direct substitution verifies the answer.''')
add('4',6,'Number Theory',r'Prove that $a^6+b^6+c^6=d^6+e^6$ has no solution in primes $a,b,c,d,e$.','Several carefully chosen moduli force a growing list of specific primes. The final obstruction combines another residue calculation with a size comparison.',['modular arithmetic','prime powers','bounding'])
add('5',6,'Geometry',r'In $ABC$, $\angle C=60^\circ$ and its internal bisector meets $AB$ at $D$. Construct equilateral triangles $AED,BDF$ on the opposite side of $AB$ from $C$. With circumcentre $O$, set $G=CO\cap AB$, $H=CD\cap EF$. Prove $DH=GH$.','An arc midpoint links two circumcentres and the equilateral constructions. The proof then needs a carefully matched similarity and auxiliary parallel line.',['arc midpoint','similarity','equilateral triangles'])
ex('6',7.5,'Classifying regular-polygon dissections requires local angle restrictions, ruling out a subtle 30-gon possibility, and exact 2025-piece constructions for four surviving polygon sizes.')
paper('Sweden','Skolornas matematiktävling',2024,sw+'Final_2425.pdf',sw+'Finalloesningar_2425.pdf','2024-11-23')
ex('1',2.5,'Eliminating the white bead weight leaves a simple positive-integer bound forcing the remaining weights.')
add('2',4,'Number Theory',r'Prove that each positive integer $n$ not divisible by $3$ has a unique expression $n=3m+2^k$, with integers $k,m$ and $0\le m<2^k$.','Locating n between adjacent powers of two gives two candidate exponents; their opposite residues modulo three settle existence and uniqueness.',['powers of two','intervals','modular arithmetic'])
add('3',4.5,'Algebra',r'Find all real polynomials $p$ satisfying $p(0)=0$ and $p(3x^2+2x+1)=3p(x)^2+2p(x)+1$ for every real $x$.','The efficient route is to generate infinitely many fixed points, rather than expand an unknown-degree polynomial.',['polynomial roots','iteration','induction'],r'''Let $x_0=0$ and $x_{n+1}=3x_n^2+2x_n+1$. The given equation and $p(x_0)=x_0$ imply inductively that $p(x_n)=x_n$ for every $n$.

All $x_n$ are nonnegative and $x_{n+1}-x_n=3x_n^2+x_n+1>0$, so they are distinct. Hence the polynomial $p(x)-x$ has infinitely many roots and is identically zero. The answer $\boxed{p(x)=x}$ satisfies both conditions.''')
add('4',5.5,'Geometry',r'In parallelogram $ABCD$, diagonals meet at $M$. Line $AB$ is tangent to $(CDM)$ and line $AD$ to $(BCM)$. Determine the parallelogram’s angles.','Both tangency conditions must be used together. A midpoint construction converts them into restrictions on adjacent central angles, forcing a special rhombus.',['tangency','midpoints','parallelogram'])
add('5',5,'Combinatorics',r'Starting with an integer $n\ge2$, players alternately subtract a prime divisor of the current number. Whoever produces $0$ loses. Determine all winning initial positions.','Parity identifies most positions, but powers of two and the small exceptional position 4 demand a separate inductive classification.',['games','parity','induction'])
add('6',6.5,'Number Theory',r'Prove that every positive integer $k$ has a positive multiple with exactly $k$ positive divisors. Determine when this multiple is unique.','A prime-exponent construction gives existence, while uniqueness requires altering exponents or introducing a new prime and handling exceptional small prime powers.',['divisor function','construction','prime factorisation'])
paper('Sweden','Skolornas matematiktävling',2023,sw+'Final_2324.pdf',sw+'Finalloesningar_2324.pdf','2023-11-18')
ex('1',3.5,'One sharing cycle has a fixed average speed; summing cycles gives 21/5 hours without knowing their number.')
add('2',4.5,'Geometry',r'In triangle $ABC$, let $D\in BC$, $E\in AC$, and $F=AD\cap BE$. Given $AF=5$, $FD=2$, $BF=4$, $FE=2$, which of the four regions $ABF,AFE,BFD,CDFE$ has greatest area?','Shared-altitude ratios give three small regions quickly; the quadrilateral requires one further decomposition and a coupled area relation.',['area ratios','cevians','decomposition'])
ex('3',3.5,'Each internal position is a strict local minimum with probability1/3. Linearity gives (n−2)/3 for n≥2 and zero for n=1.')
add('4',5.5,'Combinatorics',r'A function $f:\mathbb Z_{>0}^2\to\mathbb Z_{>0}$ satisfies $f(x,y)\le xy$. Prove that some value is attained on at least $2023$ distinct ordered pairs.','The useful finite domain is bounded by a hyperbola, not a square. Its lattice-point count and growth of harmonic sums enable pigeonhole.',['pigeonhole principle','harmonic sum','lattice-point counting'])
add('5',6.5,'Number Theory',r'For integers $x,y$: (a) prove that $x^n\equiv y^n\pmod n$ for every positive $n$ forces $x=y$; (b) classify pairs for which the congruence holds for infinitely many positive $n$.','The first part is a short Fermat argument; the second needs both a prime-power construction and a least-prime-divisor obstruction for consecutive integers.',['Fermat theorem','prime powers','least prime divisor'])
add('6',6.5,'Number Theory',r'Prove that every rational number in $(0,1)$ is a finite sum of distinct terms from the sequence $1/[k(k+1)]$, $k=1,2,\ldots$.','Ordinary greedy Egyptian fractions do not immediately ensure this denominator pattern or distinctness. A terminating alternating expansion and telescoping are the key extra ideas.',['Egyptian fractions','induction','telescoping'])
gm='https://www.georgmohr.dk/gmopg/'
paper('Denmark','Georg Mohr Contest',2025,gm+'gm25pb.pdf',gm+'gm25loes.pdf','2025-01-14','Second round')
ex('1',1.5,'Keeping track of cumulative contributions gives 4x+240=16x, hence x20.')
ex('2',2.5,'Expanding the five addition layers yields5a+10b+10c+33 modulo10, so the bottom digit is3 or8.')
add('3',4,'Combinatorics',r'Players alternately choose unused numbers from $1,\ldots,2025$. The first player to make the product of all chosen numbers divisible by $2025$ loses. Who has a winning strategy?','A suitable first move reduces a two-prime divisibility condition to avoiding one class of numbers; the parity of the safe moves then settles play.',['games','prime factorisation','parity'])
ex('4',3.5,'The semicircle diagram needs two applications of Pythagoras, first obtaining a4-unit horizontal offset and then radius5.')
add('5',5,'Number Theory',r'Iterate the rule $m\mapsto m/2$ for even $m$, and $m\mapsto m^2+3$ for odd $m$. Which positive starting integers return to themselves after a positive number of moves?','Compressing three moves to the next odd term reveals strict growth outside two small cycles. Merely finding those cycles does not prove exhaustiveness.',['iteration','monovariant','parity'])
paper('Denmark','Georg Mohr Contest',2024,gm+'gm24pb.pdf',gm+'gm24loes.pdf','2024-01-09','Second round')
ex('1',2,'The two construction rules are24n+102 and15m+26; reduction modulo3 separates them.')
ex('2',3,'Similarity gives each shaded triangle one-fifth of a100-unit corner triangle, leaving star area240.')
add('3',4,'Combinatorics',r'A palindrome of length $100$ contains $60$ letters A, $12$ letters B and $28$ letters C. Its first $66$ letters also form a palindrome. Determine its $34$th letter.','Overlapping palindromes impose a repeated-block decomposition. Counting letters modulo three identifies the exceptional central position.',['palindromes','word structure','modular counting'])
add('4',5.5,'Number Theory',r'A board initially holds three distinct nonnegative integers. A move replaces two entries $a>b$ by $a^2-b^2$ and $3a-b$. Classify the initial triples from which three equal entries can be reached.','Working backwards exposes a restrictive Diophantine equation. The full answer then requires enumerating predecessors and proving the reverse tree stops.',['reverse process','Diophantine equation','bounding'])
add('5',5.5,'Algebra',r'Let $0<x_1<\cdots<x_{2024}=1$. Colour half the numbers red and half blue, listing each colour increasingly as $r_i,b_i$; put $b_0=0$ and $S=\sum_{i=1}^{1012}r_i(b_i-b_{i-1})$. (a) Show some choice of the $x_i$ makes every colouring satisfy $S<1/2$. (b) Show every choice admits a colouring with $S>x_{2023}/2$.','Telescoping supplies a uniform upper bound, while the lower bound needs a specially arranged colouring and two complementary estimates.',['inequalities','telescoping','construction'])
paper('Denmark','Georg Mohr Contest',2026,gm+'gm26pb.pdf',gm+'gm26loes.pdf','2026-01-13','Second round',True)
ex('1',2.5,'The subtraction forces99(A−C)=198, leaving five choices of C and five of B.')
ex('2',3,'Successive equal neighbouring sums propagate the labels around the illustrated graph and force the unknown label202.')
ex('3',3.5,'A reduced numerator is even precisely when its original numerator contains more factors of2 than the denominator; counting those500 numerators determines odd parity.')
add('5',5.5,'Combinatorics',r'A simple closed lattice walk uses unit horizontal or vertical steps and has length greater than $2$. A lattice point $P$ outside the walk’s vertex set sees every visited vertex $Q$: segment $PQ$ contains no other lattice point. Prove that the walk’s length is divisible by $4$.','Translation reveals a forbidden parity class. Simplicity then forces horizontal and vertical steps into same-direction pairs, a stronger constraint than ordinary even cycle length.',['lattice parity','invariant','closed walk'])
add('4',4.5,'Geometry',r'''A square $ABCD$ has its bottom vertex $A$ on a horizontal line, with $B$ to the left and $D$ to the right above that line. Place two upright squares on the line: $B$ is the upper-right corner of the left square, and $D$ the upper-left corner of the right one. Let $E,F$ be their other upper corners.

Construct squares on $EC$ and $CF$, on the sides of those lines opposite $A$. Let $U,V$ be their respective new vertices adjacent to $C$. Prove that triangle $UCV$ and square $ABCD$ have equal areas.

![Five squares surrounding the target triangle](assets/diagrams/denmark-2026-q4.svg)''','The five-square picture must be converted into compatible lengths or rotated vectors. A determinant or an auxiliary-rectangle decomposition then reveals the area identity.',['squares','rotation','area identity'],r'''Choose coordinates $A=(0,0)$, $B=(-b,a)$ and $D=(a,b)$, with $a,b>0$. Then $C=(a-b,a+b)$ and the central square has area $a^2+b^2$.

The two upright squares give $E=(-a-b,a)$ and $F=(a+b,b)$, so $\overrightarrow{EC}=(2a,b)$ and $\overrightarrow{CF}=(2b,-a)$. Rotating the relevant side vectors through a right angle in the outward direction gives
$$\overrightarrow{CU}=(-b,2a),\qquad \overrightarrow{CV}=(a,2b).$$
Consequently the area of $UCV$ is
$$\frac12\left|(-b)(2b)-(2a)a\right|=a^2+b^2,$$
exactly the area of the central square.''',notes='The original question consists of a five-square diagram. This labelled formulation and reconstructed diagram state the same configuration explicitly.')
paper('Finland','MAOL High School Mathematics Competition',2025,'https://drive.google.com/file/d/1Fjetz__TROeuHtGdWGe1oModBqzLC80A/view','https://drive.google.com/file/d/1Fjetz__TROeuHtGdWGe1oModBqzLC80A/view','2025','Final',False)
ex('1',3.5,'Thin isosceles triangles make the product of altitudes arbitrarily small; multiplying pairwise side-product bounds proves the strict upper bound1.')
add('4',4.5,'Number Theory',r'Find all positive integer solutions of $(x+y)^2=100x+y$.','Introducing the sum bounds the search and forces a consecutive-product congruence modulo99; coprimality reduces this to four residue classes.',['Diophantine equation','consecutive integers','Chinese remainder theorem'],r'''Set $s=x+y$. Then $s(s-1)=99x$. Since $0<x<s$, we have $1<s\le99$. Also $99\mid s(s-1)$.

Consecutive integers are coprime. Hence each of $9$ and $11$ divides either $s$ or $s-1$, so modulo $99$ we have $s\equiv0,1,45,55$. In the interval $1<s\le99$, this leaves $s=45,55,99$.

Recovering $x=s(s-1)/99$ and $y=s-x$ gives exactly $\boxed{(20,25),(30,25),(98,1)}$. Direct substitution verifies all three.''',notes='The organiser’s solution PDF includes both the problem and its solution. The archive’s separate problem link is malformed; provenance is taken from the working solution file.')
ice='https://stae.is/sites/default/files/'
paper('Iceland','Icelandic Mathematical Olympiad',2026,ice+'EN_contest.pdf',ice+'solutions_1.pdf','2026-02-28')
ex('1',3,'List length decreases whenever an entry is repeated; a list of distinct entries becomes all ones, then a singleton, then [1].')
ex('2',3,'Adding the three pairwise flow and heat equations directly determines the combined temperature as38 degrees.')
ex('3',3.5,'Substituting the perimeter into Pythagoras gives (1000−a)(1000−b)=500000. The bounded divisor pairs leave legs200,375 and hypotenuse425.')
add('4',5.5,'Combinatorics',r'Three perfect logicians A, B and C each have a positive integer on their forehead. Each sees the other two numbers, knows that one number is the sum of the other two, and knows that everyone reasons perfectly. Asked in order, A, B and C each say they cannot determine their own number. Asked again, A correctly announces $65$. Find all three numbers.','Each announcement eliminates entire proportional families. A complete fourth-round classification is needed; noticing one plausible triple does not establish uniqueness.',['logic','successive elimination','case classification'],r'''Write a triple in the order $(A,B,C)$. A person seeing $u,v$ considers $u+v$ and $|u-v|$, with zero forbidden. In the following lists, every triple may be multiplied by any positive integer.

A would know immediately exactly for $(2,1,1)$, so the first answer excludes that family.

At B's turn, the newly excluded families are $(1,2,1)$ (equal visible numbers) and $(2,3,1)$ (B's other candidate gives the already excluded $(2,1,1)$).

At C's turn, the newly excluded families are
$$ (1,1,2),\quad(2,1,3),\quad(1,2,3),\quad(2,3,5). $$
The first has equal visible numbers. In each other case, changing C's number to the other candidate gives one of the earlier excluded families. These lists are exhaustive: the only reasons to know are equal visible numbers or an alternative already ruled out.

For A to know on the fourth turn, changing A's value must produce one of those six previously excluded families, while the actual triple must have survived all three answers. The possibilities are exactly
$$ (3,2,1),\ (4,3,1),\ (3,1,2),\ (4,1,3),\ (5,2,3),\ (8,3,5). $$
All are primitive integer triples, so their scale factors must be integers. Only $5$ among their first coordinates divides $65$. Thus $\boxed{(A,B,C)=(65,26,39)}$.

This triple does survive the first three answers; A's alternative $13$ would give $(13,26,39)$, a multiple of $(1,2,3)$, in which C would have known. Hence A's final announcement is justified.''',notes='The English statement renames the three participants. The original solution omits some elimination cases; the complete classification is supplied here.')
ex('5',3.5,'The midpoint of the minor contact arc lies on the symmetry axis and bisects a base angle by the tangent–chord theorem; it is therefore the incenter.')
ex('6',8,'The hypercube pursuit game needs a coordinate-avoidance lower bound and a multi-cop projection induction with synchronized capture. It is beyond the target range.')
paper('Iceland','Icelandic Mathematical Olympiad',2025,ice+'rslitakeppni_2025.pdf',ice+'rslitakeppni_2025%20lausnir.pdf','2025-03-01')
add('1',4.5,'Combinatorics',r'Ten boxes in a row contain $8,7,3,9,1,5,2,6,4$ followed by an empty box. A move transfers any number into the empty box, leaving its previous box empty. Find the minimum number of moves needed to obtain $1,2,\ldots,9$ followed by an empty box, and prove minimality.','Cycle decomposition gives a construction, but a rigorous lower bound must account for the extra move needed to enter every nontrivial cycle.',['permutation cycles','lower bound','construction'],r'''Ignore the fixed entry $3$. The other entries form three cycles, with lengths $4,2,2$: $(1,8,6,5)$, $(2,7)$ and $(4,9)$.

A cycle of length $r$ can be repaired in $r+1$ moves: move one of its entries into the spare box, fill the newly empty position with its correct entry, continue around the cycle, then return the parked entry to its correct position. This gives $5+3+3=11$ moves.

For the lower bound, each of the eight initially misplaced entries must eventually be moved into its final position. For each original cycle, consider the first move involving one of its entries. No box of that cycle is empty before this move, so the entry moves outside the cycle and is not placed correctly. This is an additional move, distinct for each of the three cycles. Thus at least $8+3=\boxed{11}$ moves are necessary.''')
ex('2',2,'Multiplying the radical sum by its conjugate gives a difference of1, hence square roots45 and46.')
ex('3',2.5,'The four triangle areas are half the products of adjacent diagonal segments and a common sine; the products on both sides coincide.')
add('4',4,'Combinatorics',r'Assign a colour to each nonempty subset of an $n$-element set, where $n\ge1$. Two subsets with a common element must receive different colours. What is the minimum number of colours?','A common-element family gives the sharp lower bound, while pairing complementary subsets supplies a matching global construction.',['extremal colouring','complementary sets','lower bound'],r'''Fix an element $a$. There are $2^{n-1}$ subsets containing $a$, and all must have different colours. Thus at least $2^{n-1}$ colours are needed.

Pair each subset $S$ with its complement. The $2^n$ subsets form $2^{n-1}$ pairs, and the members of a pair are disjoint. Assign a different colour to each pair, omitting the empty subset. This is valid and uses exactly $\boxed{2^{n-1}}$ colours.''',notes='Equivalent subset-colouring formulation of the family television-series assignment.')
add('5',4.5,'Number Theory',r'Let $m\ge3$ be an integer. Count the integers $x$ with $0<x<m(m-1)$ for which $m\mid x-1$ and $m(m-1)\mid x(x-1)$. Give the answer for $m=2025$ and in general.','A substitution reduces the condition to consecutive factors modulo m−1; independence of prime-power choices and the endpoint range must both be justified.',['Chinese remainder theorem','prime powers','consecutive integers'],r'''Write $x=km+1$. The given range is equivalent to $0\le k\le m-2$, so $k$ traverses every residue class modulo $m-1$ exactly once. Cancelling $m$ in the second divisibility condition gives
$$m-1\mid k(km+1),\qquad\text{equivalently}\qquad m-1\mid k(k+1).$$
Factor $m-1=\prod_{i=1}^r p_i^{e_i}$. Since consecutive integers are coprime, each prime power must divide exactly one of $k,k+1$. Thus $k\equiv0$ or $-1\pmod{p_i^{e_i}}$, independently for every $i$.

The Chinese remainder theorem gives exactly $\boxed{2^r}$ allowed values. For $2025$, we have $2024=2^3\cdot11\cdot23$, giving $\boxed8$.''')
add('6',6.5,'Algebra',r'For a fixed positive integer $k$, classify all functions $f:\mathbb Z_{>0}\to\mathbb Z_{>0}$ satisfying $f(f(n))=n+k$ for every positive integer $n$.','Commuting the function with its second iterate reveals periodic translation. Complete classification then requires pairing residue classes and controlling which class receives the extra shift.',['functional equation','iteration','residue classes','classification'],r'''There are no solutions for odd $k$. For even $k$, all solutions are obtained as follows. Partition $\{1,\ldots,k\}$ into unordered pairs, choose an ordering $(a,b)$ for each pair, and define, for $q\ge0$,
$$f(a+qk)=b+qk,\qquad f(b+qk)=a+(q+1)k.$$
These formulas clearly give $f^2(n)=n+k$.

For completeness, evaluating $f^3(n)$ in two ways yields $f(n+k)=f(n)+k$. Thus the first $k$ values determine $f$. Their residues modulo $k$ cover all classes, because $f^2$ does; hence they define a permutation $\pi$ of $\{1,\ldots,k\}$.

Write $f(i)=\pi(i)+q_i k$, with $q_i\ge0$. Then
$$f^2(i)=\pi^2(i)+(q_i+q_{\pi(i)})k=i+k.$$
Comparison of residues and quotients gives $\pi^2(i)=i$ and $q_i+q_{\pi(i)}=1$. A fixed point is impossible, since it would require $2q_i=1$. Consequently $\pi$ pairs the residue classes, and on each pair the two shifts are $0$ and $1$. This proves the claimed classification and forces $k$ to be even.''')

paper('Sweden','Skolornas matematiktävling',2022,sw+'Final_2223.pdf',sw+'Finalloesningar_2223.pdf','2022-11-19')
add('1',5,'Combinatorics',r'For which positive integers $n$ can an $n\times n$ square board be tiled without overlap by L-shaped triominoes, each formed from three unit squares in a $2\times2$ block? Rotations and reflections are allowed.','Area divisibility does not settle the problem: a corner obstruction eliminates side3, and the odd-multiple construction needs a genuinely tileable9×9 base case.',['tiling','corner obstruction','construction'])
ex('2',3,'Either f is identically zero, or one nonzero output lets zf(y) range over all reals, forcingf(t)=t+C.')
ex('3',3,'Divisibility by3 forces digit sum at least3, attained by10101=39·259; the short power cycle modulo13 discovers the example.')
add('4',4.5,'Geometry',r'Let $ABC$ be acute, let $I$ lie strictly inside it, and choose $D$ on $AB$. The line through $D$ parallel to $AI$ meets line $AC$ at $E$; the line through $D$ parallel to $BI$ meets line $BC$ at $F$. Prove $EF\cdot CI\ge2[ABC]$, where brackets denote area.','Parallel-line area transfers convert the whole triangle into two triangles on the same base CI; a final height bound yields the product inequality.',['area transfer','parallel lines','inequalities'])
add('5',5,'Number Theory',r'Prove that for every pair of positive integers $k,n$, there exist integers $x_1,\ldots,x_k$ such that $n=x_1+x_2^2+\cdots+x_k^k$ and $0\le x_j\le2^{k-1}n^{1/k}$ for every $j$.','Greedily removing a kth power is natural, but the remainder estimate must be strong enough for the induction to preserve a uniform kth-root bound.',['strong induction','greedy construction','power differences'],r'''We also allow $n=0$, when all entries can be zero. Induct on $k$; $k=1$ is immediate.

For $k\ge2$, put $t=n^{1/k}$, $x_k=\lfloor t\rfloor$, and $r=n-x_k^k$. Factoring the power difference gives
$$0\le r=(t-x_k)\sum_{i=0}^{k-1}t^{k-1-i}x_k^i\le k t^{k-1}\le2^{k-1}t^{k-1}.$$
The induction hypothesis represents $r$ as $x_1+\cdots+x_{k-1}^{k-1}$ with
$$x_j\le2^{k-2}r^{1/(k-1)}\le2^{k-1}t.$$
Also $x_k\le t$. Together these give the requested representation and bounds.''')
add('6',4.5,'Combinatorics',r'On an $n\times n$ board, a player wants to place exactly one cross and one circle in every row and column, with at most one symbol per cell. Beforehand, an opponent may forbid a cross or forbid a circle in selected cells, with at most one prohibition per cell. Minimise the larger of the two prohibition counts needed to make the placement impossible.','A collision construction gives an upper bound, while cyclic diagonals simultaneously provide many disjoint permutation placements for the lower bound.',['cyclic diagonals','permutations','extremal construction'],r'''The answer is $\boxed{n-1}$; for $n=1$ the requested placement is already impossible with no prohibitions.

For $n\ge2$, forbid crosses in $(1,2),\ldots,(1,n)$ and circles in $(2,1),\ldots,(n,1)$. A cross in the first row and a circle in the first column would both be forced into $(1,1)$. Thus $n-1$ prohibitions of each type suffice.

Conversely, partition the board into the $n$ cyclic diagonals $j-i\equiv r\pmod n$. Each diagonal contains one cell in every row and column. If there are at most $n-2$ cross prohibitions, at least two diagonals are entirely available for crosses. Likewise at least two are available for circles. Choose one of the former and a different one of the latter. The two diagonals are disjoint and give a valid placement. Hence fewer than $n-1$ of each type cannot block the player.''')
paper('Sweden','Skolornas matematiktävling',2021,sw+'Final_2122.pdf',sw+'Finalloesningar_2122.pdf','2021-11-20')
ex('1',3.5,'The middle angle is60degrees and its opposite side is the mean of the other two. Substitution in the cosine rule forces the two extreme sides equal.')
add('2',4,'Number Theory',r'An orange, banana and lemon each have a positive integer price. Four oranges, three bananas and a lemon cost the same as three oranges and two lemons. A friend knows the total price $M$ of three oranges and two lemons, but cannot determine the three prices. For every smaller attainable total, the prices would be uniquely determined. Find $M$.','The logical statement must be converted into the first repeated value of a two-variable positive-integer linear form, then an extremal pair of representations identified.',['Diophantine equations','uniqueness','minimality'],r'''Let the prices be $a,b,c$. The equality gives $c=a+3b$, hence $M=3a+2c=5a+6b$.

Two distinct positive representations satisfy $5(a-a')=6(b'-b)$. Their $a$-values differ by at least $6$ and their $b$-values by at least $5$. In the representation with the smaller $a$, we therefore have $a\ge1,b\ge6$, giving $M\ge5+36=41$.

At $M=41$, the representations $(a,b)=(1,6)$ and $(7,1)$ both work, with $c=19$ and $10$. Thus the first ambiguous attainable total is $\boxed{41}$.''',notes='Equivalent formulation of the original fruit-price conversation, whose total equals the friend’s mother’s age.')
add('3',5,'Geometry',r'Four labelled coins initially occupy the vertices of a square. A move reflects one coin in the position of another coin, which stays fixed. Can a finite sequence of moves leave the coins at the vertices of a square with a different side length?','A lattice invariant rules out shrinking; reversibility and similarity must then be combined to rule out enlargement as well.',['lattice invariant','reversibility','similarity'],r'''Scale and rotate so the original square has vertices $(0,0),(1,0),(1,1),(0,1)$. A move replaces a point $X$ by $2Y-X$, so every coin retains integer coordinates. Distinct lattice points are at least distance $1$ apart; therefore a smaller square is impossible.

Every move is its own inverse. If a sequence reached a square of side $s>1$, its reverse would take that labelled square back to a unit square. Apply a similarity of ratio $1/s$ carrying the larger square to a unit square. Reflections in coin positions commute with similarities, so the same reverse instructions would take a unit square to one of side $1/s<1$, contradicting the lattice argument. Hence the side length cannot change.''')
add('4',5.5,'Algebra',r'(a) Give a function $f:\mathbb R\to\mathbb R$ such that $0<f(x)<f(x+f(x))<\sqrt2x$ for all $x>0$. (b) Prove that no function $f:\mathbb R\to\mathbb R$ satisfies $x<f(x+f(x))<\sqrt2f(x)$ for all $x>0$.','The existence example is easy, but impossibility requires repeatedly improving a global lower bound and feeding it back into the shifted argument.',['functional inequalities','iterated bounds','contradiction'],r'''(a) The function $f(x)=x/2$ works, since $f(x+f(x))=3x/4$.

(b) Suppose such a function exists. The given chain first implies $f(x)>x/\sqrt2>0$. Applying this bound at $x+f(x)>0$ gives
$$\sqrt2f(x)>f(x+f(x))>\frac{x+f(x)}{\sqrt2},$$
so $f(x)>x$. Applying the improved bound at the same argument now yields $\sqrt2f(x)>x+f(x)$, hence $f(x)>(1+\sqrt2)x$.

One last substitution gives
$$\sqrt2f(x)>f(x+f(x))>(1+\sqrt2)(x+f(x))>\sqrt2f(x),$$
a contradiction.''')
add('5',6.5,'Combinatorics',r'Let $n\equiv1\pmod4$ be positive. A bag holds balls labelled $0,1,\ldots,n$. Draw one uniformly at random and call its label $k$. Keep it, then draw $k$ more balls uniformly without replacement. What is the probability that the sum of all drawn labels is odd?','The sample size depends on the first draw, so an ordinary parity symmetry is insufficient. A complement-and-reflection bijection pairs outcomes of different sizes while preserving their probabilities.',['probability','bijection','complementation','parity'])
add('6',6.5,'Number Theory',r'Find the largest positive integer which cannot be written $a+bc$ with positive integers $a<b<c$.','One must prove eventual representability, not just search small values. A division-with-remainder interpretation leads to a least-common-multiple bound or a careful construction near consecutive squares.',['Euclidean division','least common multiple','extremal construction'],r'''The answer is $\boxed{24}$. Indeed, if $24=a+bc$ with $0<a<b<c$, then $b\in\{2,3,4\}$. Each such $b$ divides $24$, whereas division by $b$ would have nonzero remainder $a$, impossible.

For $25\le n\le29$, use respectively
$$25=1+4\cdot6,\quad26=2+3\cdot8,\quad27=1+2\cdot13,\quad28=1+3\cdot9,\quad29=1+2\cdot14.$$
Now let $n\ge30$, and choose $k\ge5$ with $k(k+1)\le n<(k+1)(k+2)$. If any $2\le b\le k$ fails to divide $n$, division gives $n=bc+a$ with $0<a<b$ and $c\ge b+1$, a valid representation.

Otherwise $n$ is divisible by every integer up to $k$. For $k=5$, this forces $n\ge60$, contradicting $n<42$. For $k\ge6$,
$$n\ge\operatorname{lcm}(k-2,k-1,k)\ge\frac{k(k-1)(k-2)}2>(k+1)(k+2).$$
For the last inequality, writing $k=6+t$ reduces twice the difference to $t^3+13t^2+44t+8>0$. This again contradicts the choice of $k$. Therefore every $n>24$ is representable.''')
paper('Sweden','Skolornas matematiktävling',2020,sw+'Final_2021-lkcd.pdf',sw+'Finalloesningar_2021_fig.pdf','2020-11-21')
add('1',4,'Number Theory',r'How many integers $1\le n\le2020$ satisfy $2020\mid n(n+1)(n+2)$?','The factors4,5 and101 impose independent residue restrictions; the square factor4 needs separate attention before the Chinese remainder theorem can be applied.',['Chinese remainder theorem','consecutive integers','counting'],r'''Since $2020=4\cdot5\cdot101$, all three factors must divide the product. Modulo each of $4,5,101$, the admissible residues of $n$ are exactly $0,-1,-2$. For modulus $4$, the only other residue $1$ gives product $1\cdot2\cdot3\equiv2$, so it fails.

The moduli are pairwise coprime. Each of the $3^3$ combinations gives exactly one residue modulo $2020$, and the interval $1,\ldots,2020$ contains each residue once. The answer is $\boxed{27}$.''')
ex('2',3.5,'The centroid divides the two perpendicular medians in ratio2:1. Pythagoras gives a ratio of positive quadratic forms lying strictly between1/4 and4.')
add('3',4,'Algebra',r'Classify all bounded functions $f:\mathbb R\to\mathbb R$ satisfying $f(f(x)+y)=f(x)+f(y)$ for every real $x,y$.','The equation makes the range closed under addition. Iterating one nonzero output contradicts boundedness; no regularity assumption such as continuity is needed.',['functional equation','boundedness','iteration'],r'''If $u=f(a)$ is any value in the range, define $x_1=a$ and $x_{j+1}=f(x_j)+a$. The equation gives $f(x_{j+1})=f(x_j)+u$, so by induction $f(x_j)=ju$.

If $u\ne0$, this contradicts boundedness. Thus every output is zero. Conversely $\boxed{f\equiv0}$ satisfies the equation.''')
add('4',5.5,'Geometry',r'Find the least $n$ for which a simple, nondegenerate polygon with integer-coordinate vertices can have side lengths $1,2,\ldots,n$, in some order.','Parity eliminates two sizes, while the remaining small cases require geometric restrictions. A valid non-self-intersecting lattice construction is also essential.',['lattice geometry','parity','construction'],r'''The answer is $\boxed7$. Three sides of lengths $1,2,3$ give a degenerate triangle. A lattice segment of integer length at most $4$ must be horizontal or vertical; hence a nondegenerate four-sided polygon with those lengths would have to be a rectangle, impossible with four distinct lengths.

For any lattice segment with integer length $d$ and coordinate differences $u,v$, we have $u+v\equiv u^2+v^2=d^2\equiv d\pmod2$. Summing around a closed polygon shows its integer perimeter is even. For $n=5,6$, the perimeter is respectively $15,21$, excluding both.

For $n=7$, take the successive vertices
$$(0,0),(1,0),(1,-2),(4,-2),(4,2),(-3,2),(-3,-4).$$
Their side lengths are $1,2,3,4,7,6,5$. The six axis-parallel segments and final diagonal meet only at neighbouring endpoints, giving the required simple polygon.''')
add('5',6,'Number Theory',r'Find all integers $a$ for which some prime $p\ge5$ divides $\displaystyle\sum_{j=2}^{p-3}\binom{p-1}{j}a^{j-2}$.','Binomial coefficients modulo a prime reveal a truncated geometric sum. The remaining existence question requires classifying when a quadratic has only the prime factor3.',['binomial coefficients','Fermat theorem','prime divisors'],r'''Write the sum as $X_p(a)$. Modulo $p$, $\binom{p-1}{j}\equiv(-1)^j$. Thus
$$X_p(a)\equiv\sum_{r=0}^{p-5}(-a)^r.$$
If $a\equiv0$, the sum is $1$; if $a\equiv-1$, it is $p-4\not\equiv0$. Otherwise geometric summation and Fermat's theorem give
$$a^3X_p(a)\equiv a^2-a+1.$$
Therefore the desired prime exists exactly when $a^2-a+1$ has a prime divisor at least $5$; such a divisor automatically avoids $a=0,-1$ modulo $p$.

The quadratic is positive and odd. If it has no such prime divisor, it is a power of $3$. When $3$ divides it, $a=3t-1$, and
$$a^2-a+1=3(3t^2-3t+1),$$
so its exponent of $3$ is exactly one. Hence the only excluded cases satisfy $a^2-a+1=1$ or $3$, giving $a=0,1,-1,2$.

The answer is all integers except $\boxed{-1,0,1,2}$.''')
add('6',5.5,'Combinatorics',r'A finite collection of closed cubes in three-dimensional space has all edges parallel to the coordinate axes. No point belongs to more than $M$ cubes. Prove that the cubes can be partitioned into at most $8(M-1)+1$ groups, each consisting of pairwise disjoint cubes.','Choosing a smallest cube bounds all its neighbours by its eight vertices, converting a geometric overlap condition into a greedy colouring induction.',['extremal choice','graph colouring','induction'],r'''Choose a cube $Q$ of least side length. Any other cube meeting it has at least that side length. In each coordinate, an interval of at least the length of $Q$'s interval that intersects it must contain an endpoint of it. Consequently every cube meeting $Q$ contains at least one of $Q$'s eight vertices.

At each vertex, at most $M-1$ other cubes can occur. Hence $Q$ meets at most $8(M-1)$ other cubes.

Induct on the collection size. Colour all cubes other than $Q$ with $8(M-1)+1$ colours so that intersecting cubes have different colours. At most $8(M-1)$ colours are used on neighbours of $Q$, leaving an available colour for it. Colour classes are the required groups.''')

paper('Sweden','Skolornas matematiktävling',2019,sw+'Final_1920.pdf',sw+'Finalloesningar_1920.pdf','2019-11-23')
ex('1',3.5,'Equal shares are at least25. The possible labelled pair sums above that bound are distinct, forcing the unlabelled bag to a sister; the smallest permitted triple matches the largest pair33.')
ex('2',3.5,'Both secant productsAC·AP andAD·AQ equalAB² by right-triangle similarity, giving concyclicity by the converse power criterion.')
add('3',6,'Combinatorics',r'Two bowls, white and black, initially hold $2019$ and $0$ marbles. Players alternate, starting with A. A move transfers any positive number of marbles from one bowl to the other, or removes one marble from the white bowl. A resulting ordered pair of bowl counts must never have occurred before. A player unable to move loses. Determine who can force a win.','The no-repeat rule makes naive position recursion unsafe. One must analyse whole fixed-total layers and use parity together with the fresh lower-total layers.',['games','history-dependent moves','layer induction','parity'])
add('4',7,'Geometry',r'Let $\Omega$ be the closed unit disk. Find the least real $r$ for which three points can be chosen in $\Omega$ so that every closed disk contained in $\Omega$ with radius greater than $r$ contains at least one chosen point.','A sharp result needs both an empty-sector obstruction for every placement and a carefully scaled equilateral placement whose interception property must be proved.',['geometric covering','extremal configuration','circle intersections'],r'''Put $\rho=\sqrt3/(2+\sqrt3)$ and $\gamma=(1-\rho)/2$, so $\rho=\sqrt3\gamma$.

For a lower bound, divide the unit disk into three $120^\circ$ sectors, choosing a sector boundary through one of the three proposed points. At least one sector has no proposed point in its interior. The largest disk inscribed in that sector has radius $\rho$: if its centre is distance $d$ from the unit-disk centre, then its radius is $d\sin60^\circ$ and also $1-d$. For any $r<\rho$, shrink that disk slightly to a radius still greater than $r$. It lies strictly inside the sector and misses all three points. Thus $r\ge\rho$.

For the matching construction, choose three equally spaced points on the concentric circle of radius $\gamma$. Consider any disk of radius $R>\rho$ contained in $\Omega$, with centre distance $d\le1-R$ from the origin. If it contains the entire small circle, we are done. Otherwise its intersection with that circle is an arc. The half-angle $\theta$ of that arc satisfies
$$\cos\theta=\frac{d^2+\gamma^2-R^2}{2\gamma d}.$$
Here $d>0$ and $R>\gamma$. For fixed $R$, the expression increases with $d$, so it is at most its value at $d=1-R$. Writing $t=1-R<2\gamma$, that value is
$$\frac{2t+\gamma^2-1}{2\gamma t},$$
which increases with $t$. At $t=2\gamma$ it equals $1/2$, using $\rho^2=3\gamma^2$. Hence $\theta>60^\circ$. The arc has length greater than $120^\circ$ in angle and contains one of the three equally spaced points.

Therefore the least value is $\boxed{r=\sqrt3/(2+\sqrt3)}$.''')
add('5',5.5,'Algebra',r'A strictly increasing function $f:\mathbb Z_{>0}\to\mathbb Z_{>0}$ satisfies $f(f(n))=3n$ for every $n$. Determine $f(2019)$.','Iterating at powers of3 gives anchor values. Strict increase then fills entire integer intervals exactly, after which the second iterate controls the alternating intervals.',['functional equation','monotonicity','integer intervals'],r'''First $f(1)=2$: the value $1$ contradicts $f^2(1)=3$, while $f(1)\ge3$ would force $f(f(1))\ge f(3)\ge5$. Hence $f(2)=3$.

Evaluating $f^3(n)$ in two ways gives $f(3n)=3f(n)$. Thus for $a=3^k$,
$$f(a)=2a,\qquad f(2a)=3a.$$
There are exactly $a-1$ integers between each pair of endpoints. Strict increase therefore forces $f(a+j)=2a+j$ for $0\le j\le a$.

Applying $f$ again yields
$$f(2a+j)=3(a+j)\qquad(0\le j\le a).$$
Since $2019=2\cdot729+561$, take $a=729=3^6$ to obtain $\boxed{f(2019)=3(729+561)=3870}$.''')
add('6',6.5,'Number Theory',r'Does there exist a sequence containing each positive integer exactly once such that every sum of consecutive terms is a perfect square?','A greedy square-sum choice need not visit every integer. A controlled three-term bridge must reach the least omitted integer while keeping all added terms fresh.',['infinite construction','difference of squares','parity'],r'''Yes. Build finite initial segments, always preserving distinctness and the square-sum condition. Start with $1$. Suppose the current last term is $L$, and let $c$ be the least positive integer not yet used.

Choose an arbitrarily large integer $N$ of such parity that $a=N^2-L$ has parity opposite to $c$. Put
$$x=\frac{a-c-1}{2},\qquad b=x^2-c.$$
By choosing $N$ sufficiently large, we ensure that $a$ exceeds every previously used term and $b>a$. This is possible because $b$ grows quadratically in $a$.

Append $a,b,c$. They are positive, distinct and unused, and
$$L+a=N^2,\qquad a+b=(x+1)^2,\qquad b+c=x^2.$$
Thus the construction can continue. Each stage includes the least omitted positive integer, so every positive integer eventually appears, exactly once.''')
paper('Sweden','Skolornas matematiktävling',2018,sw+'Final_1819.pdf',sw+'Finalloesningar_1819.pdf','2018-11-24')
add('1',5,'Geometry',r'A convex cyclic quadrilateral has no parallel opposite sides. Let $P,Q$ be the intersections of its two pairs of opposite side-lines, and let $O$ be the intersection of its diagonals. Prove that the pair of angle-bisector lines at each of $P$ and $Q$ is parallel to the pair of angle-bisector lines at $O$.','The three different line pairs share a hidden relation imposed by cyclicity. Directed-angle bookkeeping or reflection converts it into matching bisector directions.',['cyclic quadrilateral','angle bisectors','directed angles'])
ex('2',3,'The mapx↦cube-root(1−x³) is an involution. Applying it once gives a two-by-two linear system andf(x)=2/3−x³.')
add('3',5.5,'Combinatorics',r'Fix $m\ge1$. A pattern is a string of $m$ signs, each either $<$ or $>$. Find the least $n$ for which some real sequence $x_1,\ldots,x_n$ has, as a subsequence, a realisation of every pattern: $x_{i_1},\ldots,x_{i_{m+1}}$ with $i_1<\cdots<i_{m+1}$ and the prescribed comparisons between consecutive terms.','The increasing and decreasing patterns give a sharp intersection obstruction. Attainment needs a universal sequence and a greedy argument bounding how many entries each comparison consumes.',['subsequences','extremal construction','greedy algorithm'],r'''The answer is $\boxed{2m+1}$.

An increasing subsequence of length $m+1$ and a decreasing one of that length cannot share two indices: the associated pair of terms would have to be both increasing and decreasing. Their union therefore has at least $2m+1$ indices.

For attainment use
$$0,1,-1,2,-2,\ldots,m,-m.$$
Start at $0$ and follow the desired comparisons greedily. After any selected term, among the next two entries there is one larger and one smaller than it. Thus each comparison requires advancing at most two positions. After $m$ comparisons the chosen subsequence ends by position $2m+1$, proving that every pattern occurs.''')
add('4',5.5,'Number Theory',r'Find the least positive integer $n$ such that every block of $n$ consecutive positive integers, all less than $2018$, contains a number divisible by its decimal digit sum.','Multiples of18 provide the uniform upper bound, but an exceptional digit-sum case and a fully checked17-number counterexample are needed for sharpness.',['digit sums','intervals','sharp example'])
add('5',5.5,'Geometry',r'Two internal rays trisect angle $A$ of triangle $ABC$, meeting $BC$ at $P,Q$ in that order. Find the least constant $K$ such that $PQ\le K(BP+QC)$ for every triangle. Determine whether equality is possible.','Two angle-bisector length identities yield a strict product bound; AM–GM gives the inequality, and a degenerating family is needed to prove the constant optimal.',['angle bisector theorem','AM–GM','sharp inequality'],r'''Write $AB=c$, $AC=b$, $AP=s$, $AQ=t$, and $BP=x$, $PQ=y$, $QC=z$. In triangle $ABQ$, the ray $AP$ is an angle bisector, giving $s^2=ct-xy<ct$. Similarly $t^2=bs-yz<bs$. Multiplying yields $st<bc$.

The angle-bisector theorem also gives $x/y=c/t$ and $z/y=b/s$. Hence
$$x+z=y\left(\frac ct+\frac bs\right)\ge2y\sqrt{\frac{bc}{st}}>2y.$$
Thus $K=1/2$ works and equality is never attained.

To see optimality, take isosceles triangles with fixed altitude from $A$ and let the base tend to zero. Then $b=c$, $s=t$, and all four lengths tend to that altitude. Therefore $(x+z)/y=c/t+b/s$ tends to $2$. No smaller $K$ works, so $\boxed{K=1/2}$.''')
add('6',6.5,'Algebra',r'For which positive integers $n$ is $1+x^n+x^{2n}$ a product of two nonconstant polynomials with integer coefficients?','The reducible direction uses third roots of unity or polynomial remainders. The irreducible direction hinges on reduction modulo3 and a contradiction from evaluating both factors at1.',['integer polynomials','modular factorisation','irreducibility'],r'''It is reducible exactly when $n$ is not a power of $3$.

If $n=3^k m$ with $m>1$ and $3\nmid m$, then $1+t^m+t^{2m}$ is divisible in $\mathbb Z[t]$ by $1+t+t^2$: modulo the latter polynomial, $t^3=1$, and the exponents $0,m,2m$ represent all three residue classes modulo $3$. Substitute $t=x^{3^k}$ to obtain a nontrivial factorisation.

Conversely let $n=3^k$. Over $\mathbb F_3$ the polynomial becomes
$$1+x^n+x^{2n}=(x^2+x+1)^{3^k}=(x-1)^{2n}.$$
If it factored as nonconstant integer polynomials, we could take both factors monic. Their reductions modulo $3$ retain their positive degrees, so each is a positive power of $x-1$. Both factors therefore have values at $x=1$ divisible by $3$. Their product at $1$ would be divisible by $9$, whereas the given polynomial has value $3$. Contradiction.''')
paper('Sweden','Skolornas matematiktävling',2017,sw+'Final_1718.pdf',sw+'Finalloesningar_1718.pdf','2017-11-18')
ex('1',3,'Backward analysis from the target square resolves all nine game states, despite backward moves; the first player moves from1 to the losing square2.')
add('2',4.5,'Number Theory',r'For a prime $p$, determine all coprime positive integers $m,n$ satisfying $\dfrac{p+m}{p+n}=\dfrac mn+\dfrac1{p^2}$.','Clearing denominators first forces a prime divisor of n; coprimality then makes the remaining multiplier divide p, reducing the equation to two carefully separated cases.',['coprimality','prime divisibility','Diophantine equation'],r'''Clearing denominators gives $(n-m)p^3=n(p+n)$, so $p\mid n$. Write $n=kp$; division by $p^2$ yields
$$pm=k(p^2-k-1).$$
Because $\gcd(m,n)=1$, also $\gcd(m,k)=1$, so $k\mid p$. Thus $k=1$ or $k=p$.

If $k=1$, then $pm=p^2-2$, forcing $p=2$ and $(m,n)=(1,2)$. If $k=p$, then $m=p^2-p-1$ and $n=p^2$; these are positive and coprime for every prime $p$.

Direct substitution verifies the answers: $\boxed{(p^2-p-1,p^2)}$ always, with the extra pair $\boxed{(1,2)}$ only when $p=2$.''')
ex('3',3,'Introduce the midpoint ofAC. Two midsegment equalities and the triangle inequality prove the bound; equality is the corresponding aligned trapezoid case.')
add('4',4.5,'Geometry',r'In triangle $ABC$, let $D$ be the foot of the altitude from $A$ to $BC$, and let the internal bisector of angle $C$ meet $AB$ at $E$. Given $\angle AEC=45^\circ$, determine $\angle EDB$.','Reflecting A in the angle bisector creates an isosceles right triangle and an auxiliary cyclic quadrilateral, exposing the fixed angle.',['reflection','angle bisector','cyclic quadrilateral'])
add('5',5,'Geometry',r'Find the smallest constant $C$ such that $S\le C(ab+bc+ca)$ for every triangle with side lengths $a,b,c$ and area $S$.','The sharp equilateral value needs a proof for all triangles; a semiperimeter substitution turns Heron’s formula into two linked symmetric inequalities.',['Heron formula','symmetric inequalities','equality case'],r'''Set $a=x+y$, $b=y+z$, $c=z+x$ with $x,y,z>0$. Write $p=x+y+z$, $q=xy+yz+zx$, $r=xyz$. Then
$$ab+bc+ca=p^2+q,\qquad S^2=pr.$$
The elementary inequalities $p^2\ge3q$ and $q^2\ge3pr$ give
$$ (ab+bc+ca)^2=(p^2+q)^2\ge16q^2\ge48pr=48S^2.$$
Both equalities hold when $x=y=z$, i.e. for an equilateral triangle. Thus the optimal constant is $\boxed{C=1/(4\sqrt3)=\sqrt3/12}$.''')
add('6',5,'Algebra',r'Real numbers $a,b,c,x,y,z$ satisfy $x+y+z=0$, $a+b+c\ge0$ and $ab+bc+ca\ge0$. Prove $ax^2+by^2+cz^2\ge0$.','The coefficients need not be positive. A hidden square identity uses the constraint on x,y,z and the two symmetric conditions to control the quadratic form.',['sum of squares','quadratic forms','symmetric conditions'],r'''If $a+b+c=0$, then $a^2+b^2+c^2=(a+b+c)^2-2(ab+bc+ca)\le0$, so $a=b=c=0$ and the claim is immediate.

Otherwise $a+b+c>0$, so at least one pair sum is positive. Relabel the corresponding coefficients and variables so that $a+b>0$. Since $z=-x-y$, direct expansion gives
$$ (a+b)(ax^2+by^2+cz^2)=(ax-by)^2+(ab+bc+ca)(x+y)^2\ge0.$$
Division by $a+b$ proves the result.''')
paper('Sweden','Skolornas matematiktävling',2016,sw+'Final_1617.pdf',sw+'Finallosningar_1617.pdf','2016-11-19')
add('1',4.5,'Geometry',r'Two existing fence segments of length $20$ meet at a right angle. Let $A$ be the free end of one segment. Can two further straight fence segments, of lengths $13$ and $14$, be joined to form a path from $A$ to a point on the other existing segment, enclosing an area of at least $200$?','One must choose a non-obvious closing point so that the added triangle is feasible and sufficiently large; Heron’s formula verifies an exact construction.',['geometric construction','Heron formula','area bound'],r'''Yes. Let the corner be $O$, with $OA=20$, and choose $B$ on the other segment with $OB=15$. Then $AB=25$.

Construct triangle $APB$ on the side of $AB$ opposite $O$, with $AP=13$ and $PB=14$. It exists because $13+14>25$. Its semiperimeter is $26$, so its area is
$$\sqrt{26(26-13)(26-14)(26-25)}=26\sqrt6.$$
The enclosed quadrilateral $OAPB$ has area $150+26\sqrt6>200$, since $(26\sqrt6)^2=4056>2500$. This is a valid placement within the angle between the existing fence rays.''',notes='The original statement supplies the right-angle fence configuration as a diagram; it is described explicitly here.')
ex('2',3.5,'The radicals are distances from(x,2) to(−1,0) and(2,0); the strict reverse triangle inequality gives a difference below3.')
add('3',4,'Geometry',r'A convex cyclic trapezoid $ABCD$ has $AB\parallel CD$. Its circumcircle has radius $R$ and centre on $AB$. A point $E$ on the circle satisfies $\angle DAE=90^\circ$ and $AE/AB=3/4$. Determine all four side lengths of the trapezoid.','Recognising both diameters and the isosceles trapezoid reduces the problem to two right-triangle relations; the shorter base then requires recovering a chord’s projection.',['cyclic trapezoid','diameter','Pythagoras'],r'''Since the circle centre lies on $AB$, we have $AB=2R$ and $AE=3R/2$. The right angle $DAE$ makes $DE$ another diameter, so
$$AD^2=(2R)^2-(3R/2)^2=7R^2/4.$$
A cyclic trapezoid is isosceles, hence $BC=AD=R\sqrt7/2$.

Place $A=(-R,0)$, $B=(R,0)$ and $D=(u,v)$ on the circle. Then
$$AD^2=(u+R)^2+v^2=2R^2+2Ru=7R^2/4,$$
giving $u=-R/8$. Symmetry puts $C=(R/8,v)$, so $CD=R/4$.

Thus $\boxed{AB=2R,\ CD=R/4,\ AD=BC=R\sqrt7/2}$.''')
add('4',5,'Number Theory',r'Find all primes $p$ such that $p+1$ equals the product of all primes smaller than $p$.','Prime factors of nearby smaller odd numbers are forced to divide tiny differences. Two such restrictions then contradict a simple modulus.',['prime factors','Euclid argument','modular contradiction'],r'''Checking $p=2,3,5,7$ leaves only $p=5$, which works.

Suppose $p\ge11$ works. Every prime divisor of $p-2$ is smaller than $p$, so it divides the product $p+1$. Hence it divides $3$, and $p-2=3^u$ for some $u\ge1$.

Similarly every prime divisor of $p-6$ divides both $p-6$ and $p+1$, hence is $7$. Therefore $p-6=7^v$ for some $v\ge1$.

Subtracting gives $3^u=7^v+4$, impossible modulo $3$ since its right side is $2$ modulo $3$. Thus $\boxed{p=5}$ is the only solution.''')
add('5',5,'Algebra',r'A binary operation $\ast$ on $\{1,2,3,4\}$ is associative and satisfies left and right cancellation: $a\ast b=a\ast c$ or $b\ast a=c\ast a$ implies $b=c$. Given $1\ast3=2$ and $2\ast2=4$, determine $3\ast1$.','Associativity and cancellation must be combined to force the small operation table; assuming ordinary multiplication or commutativity would beg the question.',['associativity','cancellation','finite operations'])
add('6',4.5,'Combinatorics',r'Each cell of a $13\times13$ board is black or white. A move reverses all colours in a contiguous $2\times2$ or $9\times9$ subsquare. Is it always possible to make the whole board black?','The useful invariant is restricted to two central rows, chosen so every large move covers both and every small move changes an even number of their cells.',['colouring','parity invariant','counterexample'],r'''No. Number rows $1,\ldots,13$, and consider the parity of the number of white cells in rows $6$ and $7$ together.

A $2\times2$ move meets these rows in $0,2$ or $4$ cells. Every $9\times9$ subsquare contains both central rows, so it meets them in $18$ cells. Thus every move changes an even number of cells in the chosen set and preserves the parity of its white count.

Start with exactly one white cell in row $7$, all other cells black. The invariant is odd, while an all-black board has even count zero. Therefore this colouring cannot reach all black.''')

cov={'reviewedCount':len(decisions),'includedCount':len(rows),'decisions':decisions,'papers':papers,'gaps':['Norway: official final archive discovered for2004–2026; only2024–2026 assessed here. Earlier rounds and older finals remain pending.','Sweden: official finals and solutions discovered2006–2025; sitting years2016–2025 fully assessed here;2006–2015 pending.','Denmark: second-round archive1991–2026 discovered. Papers2024–2026 complete. Older papers remain pending.','Finland:2025 Q2 has an unspecified function domain in the retrieved statement;Q3 needs diagram and correction of an and/or typo in its solution;Q5 needs further geometry verification. Earlier archive1997–2019 discovered but pending.'],'icelandNote':'Finals2025 and2026 fully assessed. Historical archive1984–2024 is discovered but pending. Original2026Q4 solution corrected with complete elimination families.','method':'Numerical ratings are individual mathematical judgments after reading statements and analysing proofs. Source links are hidden worked solutions in the original language; selected independent English expositions are included. Norway subparts are independent tasks and are counted separately.'}
for name,value in [('data/nordic.json',rows),('research/nordic-coverage.json',cov)]:
    (R/name).write_text(json.dumps(value,ensure_ascii=False,indent=2))
print({'reviewed':len(decisions),'included':len(rows)})


# Restore reviewed questions outside the preferred browsing band.
if __name__ == "__main__":
    import runpy
    runpy.run_path(str(Path(__file__).resolve().parents[1] / "restore-smaller-range.py"))["main"](["nordic"])
