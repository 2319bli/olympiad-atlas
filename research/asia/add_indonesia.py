import json,pathlib
P=pathlib.Path('/workspace/sites/olympiad-atlas/research/asia');RAW=P.parent/'raw'/'asia'
reviews=json.loads((P/'reviews.json').read_text());manifest=json.loads((P/'manifest.json').read_text()); rows=[]
urls={
 '2021day1':'https://wildan-wicaksono.github.io/files/KSN%202021%20Hari%20Pertama.pdf',
 '2021day2':'https://wildan-wicaksono.github.io/files/KSN%202021%20Hari%20Kedua.pdf',
 '2022day1':'https://wildan-wicaksono.github.io/files/Soal%20dan%20Solusi%20OSN%20SMA%202022%20Hari%20Pertama.pdf',
 '2022day2':'https://wildan-wicaksono.github.io/files/Soal%20dan%20Solusi%20OSN%20SMA%202022%20Hari%20Kedua.pdf',
 '2024province':'https://wildan-wicaksono.github.io/files/OSP%20SMA%202024.pdf'}
def add(year,section,num,rating,topic,reason,statement='',solution='',omit=''):
 rows.append((year,section,num,rating,topic,reason,statement,solution,omit))
add(2021,'National',1,3.5,'Combinatorics','Writing the result as 45 minus twice a subset sum reduces this to a short finite construction covering all required sums.')
add(2021,'National',2,4.5,'Geometry','Two circle-power identities combine with the median formula; the possible relative positions of the second intersections also need checking.',r'''In acute triangle $ABC$, let $D,E$ be the midpoints of $AB,AC$. Line $CD$ meets the circumcircles of $ABC$ and $ADE$ again at $M\ne C$ and $N\ne D$, respectively. If $DM=DN$, prove that $ABC$ is isosceles.''',r'''Write $AD=DB=c$, $AE=EC=b$, $BC=2a$, $CD=t$ and $DM=DN=s$. Since $D$ lies inside the circumcircle of $ABC$, $M$ lies on the ray from $D$ opposite $C$. Power at $D$ gives $st=c^2$.

Power of $C$ with respect to the circle $ADE$ gives $CD\cdot CN=CA\cdot CE=2b^2$. If $N$ were on the same side of $D$ as $M$, then $CN=t+s$, so $t^2+c^2=2b^2$. But the median formula gives $t^2=2a^2+2b^2-c^2$, forcing $a=0$, impossible. Thus $N$ is on the other side. It cannot lie beyond $C$, since $C$ has positive power, so $CN=t-s$. Hence $t^2-c^2=2b^2$. Comparing with the median formula now gives $a=c$, or $BC=AB$.''')
add(2021,'National',3,5,'Number Theory','The even terms recur every three positions; their 2-adic valuations restrict where the only possible small even term can occur.',r'''Call a positive integer a prime power if it equals $p^k$ for a prime $p$ and a positive integer $k$. Find the greatest $n$ for which prime powers $a_1,\ldots,a_n$ can satisfy $a_i=a_{i-1}+a_{i-2}$ for every $3\le i\le n$.''',r'''The answer is $7$, attained by $5,2,7,9,16,25,41$.

Suppose there are eight terms. If $a_1,a_2$ are both even, they are powers of $2$. Their sum is a power of $2$ only when they are equal, but then $a_4=3a_1$ is not a prime power. Otherwise the parity pattern has one even term every three positions. If an even term $a_i=2^u$ has the following three terms available, then
$$a_{i+3}=a_i+2a_{i+1}.$$
Here $a_{i+1}$ is odd. If $u\ge2$, the right side is divisible by $2$ but not by $4$ and exceeds $2$, so it cannot be a prime power. Therefore such an $a_i$ must equal $2$.

The first even term has index $1$, $2$ or $3$. At index $3$ it is the sum of two odd prime powers, hence at least $6$, already impossible since $a_6$ exists. At index $1$ or $2$ it must be $2$, but the next even term, at index $4$ or $5$, is greater than $2$ and still has three following terms. This is again impossible.''')
add(2021,'National',4,5,'Algebra','An inner square-root estimate uses the fixed sum, followed by a cyclic pairing of outer square roots; the orientation of the cycle is the main insight.',r'''For positive reals $x+y+z=3$, prove
$$2\sqrt{x+\sqrt y}+2\sqrt{y+\sqrt z}+2\sqrt{z+\sqrt x}
\le\sqrt{8+x-y}+\sqrt{8+y-z}+\sqrt{8+z-x}.$$''',r'''Since $2\sqrt y\le y+1$,
$$2\sqrt{x+\sqrt y}\le\sqrt{4x+2y+2}=\sqrt{8+2x-2z}.$$
Thus it is enough to compare the cyclic sums of the latter square roots. The inequality $\sqrt u+\sqrt v\le2\sqrt{(u+v)/2}$ gives
$$\sqrt{8+2x-2z}+\sqrt{8+2z-2y}\le2\sqrt{8+x-y}.$$
Add this inequality and its two cyclic counterparts, then divide by $2$. All radicands are positive because $x,y,z$ lie between $0$ and $3$.''')
add(2021,'National',5,3.5,'Algebra','The minimum of the monic quadratic is minus one quarter of its root gap squared; it therefore lies above both roots, immediately settling the composition.')
add(2021,'National',6,4.5,'Number Theory','First manufacture the gcd of the whole collection, then use it as a permanent tool to decrease every other entry to that value.',r'''A board contains $n$ positive integers. A move selects distinct entries with values $a,b$ and replaces them by $\gcd(a,b)$ and $\operatorname{lcm}(a,b)-\gcd(a,b)$. Prove that some finite sequence of moves makes all entries equal.''',r'''If all entries are already equal, stop. Otherwise retain one entry as an accumulator. Pair it successively with each other original entry whose value differs from the accumulator, keeping the gcd as the new accumulator. An equal entry can be skipped. No performed move creates zero, since its two values differ. After this process the accumulator is the gcd $g$ of all the initial entries.

Every current entry is a positive multiple of $g$. Whenever an entry is $kg$ with $k>1$, pair it with the accumulator $g$. The new values are $g$ and $(k-1)g$. Thus the accumulator survives and the other entry decreases by $g$. Repeating finitely many times makes every entry equal to $g$.''')
add(2021,'National',7,6.5,'Geometry','The advertised geometric converse has an undefined point and the solution author supplies counterexamples rather than a valid proof.','','','Withheld: point P is not defined in the printed task, and the author documents a counterexample even to the intended converse. Needs a corrected original statement.')
add(2021,'National',8,5.5,'Combinatorics','Two residue colorings force lower bounds and divisibility for the orientations; a boundary construction and independent 3-by-3 blocks realize every permitted pair.',r'''A $100\times100$ board is covered by nonoverlapping $1\times3$ and $3\times1$ tiles, leaving exactly one square uncovered. Determine all possible ordered pairs $(H,V)$, where $H$ and $V$ count horizontal and vertical tiles.''',r'''Exactly $9999/3=3333$ tiles are used, so $H+V=3333$.

Color columns by their indices modulo $3$. The three color classes have sizes $3400,3300,3300$. A horizontal tile covers one square of each color, and a vertical tile covers three of one color. Modulo $3$, the uncovered square must belong to the class of size $3400$ and $H\equiv0\pmod3$. Comparing that class with either smaller class gives $3(V_1-V_2)=99$, so $V\ge33$. Coloring rows the same way gives $V\equiv0\pmod3$ and $H\ge33$.

Conversely leave the upper-left square empty. Tile the remaining $99$ squares of its row horizontally, using $33$ tiles, and the remaining $99$ squares of its column vertically, using $33$ tiles. The remaining $99\times99$ square splits into $1089$ blocks of size $3\times3$. Each block may use three horizontal or three vertical tiles independently. Thus precisely
$$H=33+3r,\qquad V=33+3(1089-r),\qquad 0\le r\le1089,$$
are possible.''')
add(2022,'National',1,5,'Algebra','Obtaining a zero in the image first removes the unknown f(0); two short compositions then force the function to vanish.',r'''Find every function $f:\mathbb R\to\mathbb R$ satisfying
$$f\bigl(f(f(x))+f(y)\bigr)=f(y)-f(x)$$
for all real $x,y$.''',r'''Setting $x=y$ shows that $0$ belongs to the image. Choose $t$ with $f(t)=0$, and put $a=f(0)$. The equation at $(t,t)$ gives $f(a)=0$. At $(0,a)$, its left side is $f(f(a)+f(a))=a$, while its right side is $-a$. Hence $a=0$.

Taking $x=0$ now gives $f(f(y))=f(y)$. Taking $y=0$ gives $f(f(f(x)))=-f(x)$. But the first identity makes this same left side equal to $f(x)$. Therefore $f(x)=0$ everywhere, and this function indeed works.''')
add(2022,'National',2,3.5,'Number Theory','Divisibility of differences of integer-polynomial values bounds any integer root to a tiny list, while the construction is a quadratic interpolation.')
add(2022,'National',3,5,'Geometry','Two pairs of power-of-a-point products give simple intercept coordinates; both required lines then have the same diagonal intersection.',r'''In rectangle $ABCD$, points $F,E$ lie on diagonal $AC$ in the order $A,F,E,C$. The circle through $B,E,F$ meets $AB,BC$ again at $G,H$, respectively. The circle through $D,E,F$ meets $AD,CD$ again at $I,J$, respectively. Prove that lines $GJ$, $IH$, $AC$ are concurrent.''',r'''Take $A=(0,0)$, $B=(b,0)$, $C=(b,c)$, $D=(0,c)$, and write $E=e(b,c)$, $F=f(b,c)$, where $0<f<e<1$. Put
$$k=ef(b^2+c^2),\qquad l=(1-e)(1-f)(b^2+c^2).$$
The powers of $A$ with respect to the two circles give $AG\cdot AB=AI\cdot AD=k$, with directed lengths if necessary. The powers of $C$ similarly give $CH\cdot CB=CJ\cdot CD=l$. Hence
$$G=(k/b,0),\ I=(0,k/c),\ H=(b,c-l/c),\ J=(b-l/b,c).$$
Let $T=\frac{k}{k+l}(b,c)$. Direct subtraction gives
$$T-G=\frac{k}{k+l}(J-G),\qquad T-I=\frac{k}{k+l}(H-I).$$
Thus $T$ lies on $GJ$, $IH$ and $AC$.''')
add(2022,'National',4,6,'Combinatorics','A parity reduction leaves five points modulo 13; counting pair midpoints forces two additive collisions whose overlap creates an isosceles triangle.',r'''Prove that every set of nine vertices of a regular $26$-gon contains the vertices of an isosceles triangle.''',r'''At least five selected vertices have indices of the same parity. They lie on a regular $13$-gon, whose vertices we label by $\mathbb Z/13\mathbb Z$. It suffices to show that any five-element set $S$ contains distinct $u,v,w$ with $u+w=2v$: those three vertices form an isosceles triangle with apex $v$.

Suppose no such triple exists. Each of the ten unordered pairs in $S$ has its midpoint outside $S$, leaving eight possible midpoint residues. A midpoint can occur for at most two pairs, since pairs with the same midpoint are disjoint and $S$ has only five elements. Therefore at least two distinct midpoints each occur twice.

Each such collision uses four elements. The two four-element sets cannot be identical: two different pairings of the same four elements with equal sums force two elements to coincide, since $2$ is invertible modulo $13$. Relabel so the first collision is $a+b=c+d$ and the second uses $a,b,c,e$. It cannot be $a+b=c+e$, as then $d=e$. If it is $a+c=b+e$, the two equations give $2a=d+e$; if it is $b+c=a+e$, they give $2c=d+e$. Either is the forbidden triple. This proves the claim.''')
add(2022,'National',5,3.5,'Number Theory','If all entries were units, equal residues among the prefix products would produce a contiguous product equal to one; this is a direct pigeonhole argument.')
add(2022,'National',6,4.5,'Geometry','A second point defined by two parallels simultaneously supplies a diameter circle and a homothety centered at A.',r'''In triangle $ABC$, take $D\in AB$ and $E\in AC$ with $DE\parallel BC$. A point $P$ inside quadrilateral $BDEC$ satisfies $\angle BPD=\angle CPE=90^\circ$. Prove that line $AP$ passes through the circumcenters of triangles $DPE$ and $BPC$.''',r'''Define $P'$ by $BP'\parallel DP$ and $CP'\parallel EP$. The triangles $PDE$ and $P'BC$ have corresponding sides parallel. The homothety carrying $D,E$ to $B,C$ is centered at $A$, so it also carries $P$ to $P'$. In particular $A,P,P'$ are collinear.

The given right angles imply $BP\perp BP'$ and $CP\perp CP'$. Thus $B,C$ lie on the circle with diameter $PP'$. This is the circumcircle of $BPC$, whose center lies on $AP$. The homothety just described carries the circumcircle of $DPE$ to that same circle through $B,C,P'$. Its center must therefore also lie on $AP$.''')
add(2022,'National',7,6.5,'Combinatorics','Classifying the connected components requires a lexicographic extremal argument, two local reversal improvements, and recognition of the isolated alternating words.',r'''A binary word has length $2022$. A legal move reverses a consecutive block containing unequal numbers of zeros and ones. What is the largest size of a collection of words such that no member can be transformed into another by legal moves?''',r'''The answer is $2025$. The number of ones is invariant. In addition, the two fully alternating words are isolated: an even-length block has equal counts and cannot be reversed, while an odd-length alternating block reads the same backwards.

We show that every other word can reach the decreasing word with the same number of ones. Choose the lexicographically largest word reachable from it, with $1>0$. It contains neither $001$ nor $011$, since reversing either block is legal and increases the word. Consequently it has the form
$$1^a(01)^b0^c.$$
If it is neither decreasing nor fully alternating, it contains $1101$ or $0100$: this follows by looking at the junction between a repeated initial or final symbol and the alternating portion. But the legal two-move transformations
$$1101\longrightarrow0111\longrightarrow1110,
\qquad0100\longrightarrow0001\longrightarrow1000$$
increase lexicographic order, a contradiction. Thus the maximum reachable word is decreasing, unless the starting word was one of the isolated alternating words.

There are $2023$ possible numbers of ones, giving $2023$ ordinary components, and the two additional isolated words. Taking one representative from each component gives the result.''')
add(2022,'National',8,5.5,'Algebra','Convexity of the Euclidean norm reduces a three-variable sharp inequality to cube vertices; two nontrivial vertex types determine the constant.',r'''Find the least positive real $K$ such that for all $a,b,c\in[0,1]$,
$$K+\frac{a+b+c}{3}\ge (K+1)\sqrt{\frac{a^2+b^2+c^2}{3}}.$$''',r'''The answer is $K=\sqrt{2/3}$. For fixed $K$, the left side minus the right side is a concave function on the unit cube: its affine part is both convex and concave, and the negative of the Euclidean norm is concave by the triangle inequality. Every point of the cube is a convex combination of its vertices. Therefore it suffices to verify the inequality at vertices.

At a vertex with $j$ coordinates equal to one, it becomes
$$K+j/3\ge(K+1)\sqrt{j/3}.$$
The cases $j=0,3$ are automatic. For $j=1$, rearranging gives $K\ge1/\sqrt3$; for $j=2$, it gives $K\ge\sqrt{2/3}$. Thus the stated value is both sufficient and necessary, with necessity witnessed by $(1,1,0)$.''')
add(2024,'Provincial short answer',1,1.5,'Number Theory','Factoring 777 identifies its sole pair of two-digit factors, after which the digit sum is immediate.')
add(2024,'Provincial short answer',2,2,'Algebra','Compare coefficients of the given affine identity and use the supplied value of g; no functional-equation rigidity remains.')
add(2024,'Provincial short answer',3,4,'Geometry','The parallel side fixes one similarity ratio; a sine-rule computation in the small remaining triangle determines the radical expression.',r'''Triangle $ABC$ has $AB=15$, $AC=13$, $BC=4$. An equilateral triangle $PQR$ has $P\in BC$, $Q\in CA$, $R\in AB$ and $PQ\parallel AB$. Write
$$\frac{PQ}{AB}=\frac{a}{b+c\sqrt d},$$
where $a,b,c$ are integers, $a>0$, $d$ is squarefree and $\gcd(a,b,c)=1$. Find $a+b+c+d$.''',r'''Put $CP=x$. Similar triangles $CPQ$ and $CBA$ give $PQ=15x/4$. By the cosine rule at $B$,
$$\cos B=\frac{15^2+4^2-13^2}{2\cdot15\cdot4}=\frac35,\qquad\sin B=\frac45.$$
Because $PQ\parallel AB$ and $PQR$ is equilateral, $\angle PRB=60^\circ$. The sine rule in $PBR$ yields
$$PB=\frac{PR\sin60^\circ}{\sin B}=\frac{75\sqrt3}{32}x.$$
Since $PB+PC=4$,
$$\frac{PQ}{AB}=\frac{x}{4}=\frac{32}{32+75\sqrt3}.$$
Thus the requested sum is $32+32+75+3=142$.''')
add(2024,'Provincial short answer',4,4,'Combinatorics','An odd-parity condition determines every interior cell from a boundary; the remaining task is a modular power computation.',r'''Color every square of a $3\times2023$ board black or white so that every $2\times2$ subboard contains an odd number of squares of each color. If $A$ is the number of such colorings, find the remainder of $A$ on division by $1000$.''',r'''Choose the first row and first column arbitrarily. Every other square is uniquely determined, scanning row by row: in its $2\times2$ block with the three already chosen neighbors, exactly one of its two colors makes the black count odd. Conversely this process satisfies every constraint. There are $3+2023-1=2025$ freely chosen squares, so $A=2^{2025}$.

Modulo $8$ this is $0$. Modulo $125$, Euler's theorem reduces the exponent modulo $100$, giving $2^{2025}\equiv2^{25}\equiv57$. The unique residue modulo $1000$ with these two properties is $432$.''')
add(2024,'Provincial short answer',5,3,'Number Theory','Euler totient counts the units, and the four CRT choices of signs count the roots of one; their difference is immediate.')
add(2024,'Provincial short answer',6,5.5,'Geometry','An angle-bisector chase fixes a 15-degree angle, then a cyclic quadrilateral and a second bisector ratio determine the final length.',r'''Square $ABCD$ has side length $\sqrt2+\sqrt6$. A point $X$ on diagonal $AC$ satisfies $AX>XC$. The internal bisectors of $\angle AXB$ and $\angle CXD$ meet $AB$ and $CD$ at $U$ and $V$, respectively. If $\angle UXV=150^\circ$, find $\lfloor3UV^2\rfloor$.''',r'''Write the side length as $a\sqrt3$, and set $\beta=\angle XBC$. Symmetry across $AC$ gives $\angle XDC=\beta$. The relevant angles are
$$\angle AXB=45^\circ+\beta,\quad\angle DXC=135^\circ-\beta,\quad\angle AXD=45^\circ+\beta.$$
Adding the two half angles and $\angle AXD$ shows $\angle UXV=135^\circ+\beta$. Thus $\beta=15^\circ$, $\angle AXU=30^\circ$, and $\angle DXU=90^\circ$.

Consequently $A,U,X,D$ are cyclic. Their angles give $AU=a$, $DU=2a$, and $DX=XU=a\sqrt2$. Ptolemy's theorem gives
$$AX=\frac{a(\sqrt6+\sqrt2)}2,\qquad XC=\frac{a(\sqrt6-\sqrt2)}2.$$
The bisector theorem in $DXC$ yields $DV/VC=DX/XC=\sqrt3+1$, hence $DV=(3-\sqrt3)a$. The horizontal separation of $U,V$ is therefore $(2-\sqrt3)a$, and their vertical separation is $a\sqrt3$. Thus
$$UV^2=(10-4\sqrt3)a^2=\frac{32+8\sqrt3}{3}.$$
Since $13<8\sqrt3<14$, the required integer is $45$.''')
add(2024,'Provincial short answer',7,2.5,'Combinatorics','Choose the intersection of size zero, one or two, then give each remaining element one of three independent memberships.')
add(2024,'Provincial short answer',8,3.5,'Algebra','The printed one-sided inequality cannot have the claimed finite minimum: the constant coefficient may tend to minus infinity.','','','Withheld: the printed statement lacks the absolute value used in the worked solution. Taking a=b=0 and c tending to negative infinity makes the requested expression unbounded below.')
add(2024,'Provincial proof',1,3,'Algebra','Quadratic mean is at least arithmetic mean; with t=x+y at least two, the residual expression factors as (t-2)(t-C)/(2t).')
add(2024,'Provincial proof',2,4.5,'Combinatorics','Count all adjacency edges for the lower bound, then alter a checkerboard at isolated interior squares to meet the exact target.',r'''Color some squares of an $n\times n$ board black and the rest white. Exactly $2024$ placements of a domino cover one black and one white square; both horizontal and vertical placements count. Find the least possible $n$.''',r'''There are $2n(n-1)$ pairs of side-adjacent squares in total. Since $2\cdot32\cdot31=1984<2024$, we need $n\ge33$.

Start with a $33\times33$ checkerboard. All $2\cdot33\cdot32=2112$ adjacent pairs have opposite colors. Flip the colors of $22$ pairwise nonadjacent interior squares. Each flip removes exactly four opposite-color pairs, with no overlaps, leaving $2112-88=2024$.

Such squares exist: take $(2,j)$ for even $j=2,4,\ldots,32$, and $(4,j)$ for even $j=2,4,\ldots,12$. These are $16+6=22$ interior squares with no shared side. Hence the least $n$ is $33$.''')
add(2024,'Provincial proof',3,6,'Geometry','The provided proof uses two cyclic quadrilaterals and a homothety of altitude triangles, but the unqualified statement admits a degenerate counterexample.','','','Withheld pending a nondegeneracy condition: for A=(0,0), B=(1,0), C=(1,1), one gets Z1=Z2=(1/2,1/2), Y1=(3/4,1/4), Y2=(1,0). Then K=(0,-1/2) satisfies both given equal-distance conditions but KB is not KC. The source does not exclude right triangles or coincident constructed points.')
add(2024,'Provincial proof',4,5,'Number Theory','Use the bijectivity of cubing modulo a prime congruent to five modulo six, then parametrize by a quotient; minus one being a nonsquare removes every exceptional denominator.',r'''How many ordered pairs of integers $1\le a,b\le2027$ satisfy
$$2027\mid a^6+b^5+b^2?$$''',r'''Work modulo the prime $p=2027$; the given interval supplies each residue once. Cubing permutes the residues because $\gcd(3,p-1)=1$. For $b=0$, only $a=0$ works, giving one pair.

For $b\ne0$, put $t=a^3/b$. The equation becomes
$$t^2+b^3+1=0.$$
For every residue $t$, the number $-t^2-1$ is nonzero: otherwise $t^2=-1$, impossible since $p\equiv3\pmod4$ (raise to the power $(p-1)/2$ and use Fermat's theorem). As cubing is bijective, there is a unique nonzero $b$ with $b^3=-t^2-1$, and then a unique $a$ with $a^3=bt$. Thus the nonzero-$b$ case gives exactly $2027$ pairs, for a total of $2028$.''')
for year,section,num,rating,topic,reason,statement,solution,omit in rows:
 suffix='national' if section=='National' else ('province_short' if 'short' in section else 'province_proof')
 slug=f'idn_{year}_{suffix}_q{num}'
 key=f'{year}day{1 if num<=4 else 2}' if section=='National' else '2024province'
 comp=f'Indonesia {"KSN" if year==2021 else "OSN"} — {"National" if section=="National" else "Provincial (OSP)"}'
 raw={'country':'Indonesia','competition':comp,'year':year,'section':section,'problem_number':str(num),'problem_markdown':statement or f'{section} Problem {num}; see source','solutions_markdown':[solution],'primary_domain':topic,'topics':[],'booklet_title':f'{comp} {year}: Wicaksono solution booklet','sourceDataset':'Wildan Bagus Wicaksono contest solution archive','sourceLicense':'Mathematical statement translated and solution independently rewritten; original author source linked.'}
 (RAW/(slug+'.json')).write_text(json.dumps(raw,ensure_ascii=False,indent=2))
 review={'difficulty':rating,'reason':reason,'sourceUrl':urls[key],'solutionUrl':urls[key],'note':f'{section}. Reviewed all 8 national tasks in each of 2021 and 2022 and all 12 provincial tasks (8 short answer, 4 proof) in the 2024 booklet. Primary author solution archive; not represented as an official organizing-body publication.'}
 if solution:review['solutionOverride']=solution
 else:review['solutionKind']='source-link'
 if omit:review['omitReason']=omit
 reviews[slug]=review
 if slug not in {x[0] for x in manifest}:manifest.append([slug,'indonesia-wicaksono',year,comp,0,0,str(num)])
(P/'reviews.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2));(P/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('Indonesia individually assessed',len(rows),'included',sum(4<=r[3]<=7 and not r[-1] for r in rows))
