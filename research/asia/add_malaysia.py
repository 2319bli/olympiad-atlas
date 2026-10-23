import json,pathlib
P=pathlib.Path('/workspace/sites/olympiad-atlas/research/asia'); RAW=P.parent/'raw'/'asia'
REV=json.loads((P/'reviews.json').read_text()); MAN=json.loads((P/'manifest.json').read_text())
URL='https://imo-malaysia.org/wp-content/uploads/2026/10/main-2.pdf'
# All 84 distinct tasks in the official compilation were read individually, including solutions.
# Tuple: category/question, score, assessment, topic, starting PDF page.
R={
2020:[('Primary 1',2,'A cyclic quadrilateral follows from two angle sums; the requested sum is then immediate.','Geometry',4),('Primary 2',1,'The sum of odd numbers is a standard induction or arithmetic-series formula.','Algebra',4),('Primary 3',2.5,'A four-digit expansion and short bounds leave a small digit check.','Number Theory',5),('Primary 4 / Junior 1',2,'The standard area formula and Pythagoras give the inradius.','Geometry',5),('Primary 5 / Junior 2',3.5,'Construct the three initial triangular tilings, then subdivide a tile to increase the count by three.','Combinatorics',6),('Primary 6 / Junior 3',2.5,'Listing square residues modulo 11 gives the result.','Number Theory',7),('Junior 4 / Senior 1',3.5,'Extending the trapezium to a triangle reveals a triangular lattice tiling.','Geometry',7),('Junior 5 / Senior 2',2.5,'Subtract twice the even-indexed terms from the harmonic sum.','Algebra',8),('Junior 6 / Senior 3',2.5,'Congruences modulo 4 and 3 determine the repeated digit, followed by a quadratic.','Number Theory',8),('Senior 4',4.5,'A useful inversion turns four tangent circles into a collinearity argument with two similar isosceles triangles.','Geometry',8),('Senior 5',2,'The discriminant and two linear choices reduce to four explicit quadratics.','Algebra',9),('Senior 6',4,'Recognizing a quadratic potential shows the apparently optimizable splitting score is invariant.','Combinatorics',10)],
2021:[('Primary 1',2,'Similar-triangle areas form consecutive odd multiples and the alternating sum is elementary.','Geometry',11),('Primary 2',2,'Cancel common summands in the given inequalities to identify the extrema.','Algebra',11),('Primary 3',4,'Counts positive edge labels against negative face products, then constructs a matching of the six faces.','Combinatorics',12),('Primary 4 / Junior 1',2.5,'Inscribed angles and one triangle angle sum give the answer.','Geometry',13),('Primary 5 / Junior 2',2,'Bounding each square by the next square gives two incompatible inequalities.','Number Theory',14),('Primary 6 / Junior 3',2.5,'Successive differences double, giving a direct geometric progression.','Algebra',14),('Junior 4 / Senior 1',2.5,'Completing a product converts the rectangle condition to factor pairs of 16.','Number Theory',15),('Junior 5 / Senior 2',5.5,'The total score limits the bottom team to three cases; draw counts and incompatible low-score records finish the argument.','Combinatorics',16),('Junior 6 / Senior 3',3.5,'The difference-of-squares identity turns the required radical into an explicit rational quotient.','Algebra',17),('Senior 4',4.5,'Vector closure separates rational and irrational components to force equality of opposite sides.','Geometry',18),('Senior 5',5,'Recognize nonfriendship as an equivalence relation, then use equal degrees to classify complete multipartite graphs.','Combinatorics',19),('Senior 6',5,'Build the decimal expansion inductively, choosing an odd leading digit to lift divisibility by a power of five.','Number Theory',20)],
2022:[('Primary 1',1,'Subtract the ten sides from the number of vertex pairs.','Combinatorics',22),('Primary 2',2.5,'A short count by digit length and the location of the exceptional digit gives the index.','Combinatorics',22),('Primary 3',1.5,'The sum follows directly from standard sums or induction.','Algebra',22),('Primary 4 / Junior 1',3,'The arc-midpoint condition supplies equal inscribed angles for one cyclicity check.','Geometry',24),('Primary 5 / Junior 2',2.5,'Bound the bases by nearby powers of two and compare exponents.','Algebra',24),('Primary 6 / Junior 3',3,'The absence of carries forces an odd digit-sum total, contradicting the two equal digit sums.','Number Theory',25),('Junior 4 / Senior 1',4,'Express area using distances to two sides, then use the perimeter condition to identify the incenter.','Geometry',25),('Junior 5 / Senior 2',6.5,'Parity gives a necessary multiple-of-four condition; sufficiency requires a carefully signed factor construction in three cases.','Number Theory',26),('Junior 6 / Senior 3',4.5,'A digit-by-digit induction lifts divisibility by 2 while preserving the restricted decimal alphabet.','Number Theory',26),('Senior 4',4,'Intersecting two diagonals reveals two cyclic quadrilaterals and a short angle chain.','Geometry',27),('Senior 5',4.5,'Divide the exponents with remainder, cancel an invertible power modulo the denominator, then exploit a strict size bound.','Number Theory',27),('Senior 6',7,'Translate the hypothesis to an invertible symmetric matrix over parity; a nontrivial alternating-matrix or subset-bijection argument forces even order.','Combinatorics',28)],
2023:[('Primary 1',1.5,'This is the standard sum-of-cubes identity proved by induction.','Algebra',29),('Primary 2',2,'Equality in AM-GM forces all five counts to equal ten.','Algebra',29),('Primary 3',2,'Factor the sum of cubes and bound its second factor.','Number Theory',30),('Primary 4',1.5,'Pythagoras and the two-variable square inequality give the maximum.','Geometry',30),('Primary 5',2,'The total sum decreases by exactly one at each of nine moves.','Combinatorics',30),('Primary 6',2.5,'Projection onto the chord respects the midpoint of the diameter.','Geometry',30),('Senior 1',4.5,'Combine the sum-of-cubes identity with freely chosen sixth powers to balance two different prescribed term counts.','Number Theory',31),('Senior 2',3.5,'Remove common powers of two and use the odd-square residue modulo four.','Number Theory',31),('Senior 3',7.5,'The general n-queens construction requires several non-obvious residue-dependent placement patterns and verification.','Combinatorics',32),('Senior 4',4,'A ratio from parallel sides combines with altitude similarity to produce the required cyclic quadrilateral.','Geometry',32),('Senior 5',4,'A triangle-inequality bound must be paired with a near-degenerate construction to prove the constant is sharp.','Geometry',33),('Senior 6',2.5,'The cosine rule reduces the problem to an impossible quadratic-form residue modulo three.','Number Theory',33)],
2024:[('Primary 1',2.5,'Count seven possible starts of the fixed substring and correct the unique double count.','Combinatorics',34),('Primary 2',2.5,'Two right triangles are congruent, giving supplementary angles.','Geometry',34),('Primary 3',3,'Construct backwards using powers of two with a prescribed divisor count.','Number Theory',35),('Primary 4 / Junior 1',2.5,'A common multiple gives part (a); the lcm lower bounds give an immediate contradictory sum in part (b).','Number Theory',35),('Primary 5 / Junior 2',4,'Two successive cyclic quadrilaterals convert the unusual 135-degree condition into the target angle.','Geometry',35),('Primary 6 / Junior 3',4.5,'Continuous interpolation of the opposite motions exposes two meeting points whose chord separates all simultaneous positions.','Combinatorics',36),('Junior 4 / Senior 1',3.5,'Weighted AM-GM and one elementary rearrangement inequality yield the result.','Algebra',37),('Junior 5 / Senior 2',4,'Compare with triangular numbers, then construct all possible remainders using one or two gaps of size two.','Number Theory',37),('Junior 6 / Senior 3',4.5,'Interpret each floor sum as counting lattice pairs below the same power-product boundary.','Combinatorics',38),('Senior 4',3.5,'The residue of 2 to the nth power modulo three gives an explicit formula and a direct recurrence check.','Algebra',39),('Senior 5',4.5,'A modular permutation gives the bijection, while three independent congruence classes explain the cube.','Combinatorics',40),('Senior 6',5,'Either a chain of circle and power relations or two circle equations and a radical axis establish the exact collinearity.','Geometry',41)],
2025:[('Beginner 1',1.5,'Count the odd entries used by same-parity and mixed pairs.','Combinatorics',44),('Beginner 2',3.5,'The construction starts with 1,2,3 and doubles successive terms so their sum remains a common multiple.','Number Theory',44),('Beginner 3',3,'The longest tile has only two placements, each leaving a smaller staircase.','Combinatorics',44),('Beginner 4',1.5,'The two right triangles are immediately similar with ratio one to two.','Geometry',45),('Beginner 5',3.5,'Applying the linear operation twice scales both inputs by one half; parity of the number of steps finishes.','Algebra',45),('Beginner 6',3,'An elementary inductive bound shows twice the sum of smaller factorials is too small once n reaches four.','Number Theory',46),('Pioneer 1',2.5,'Summing the permutation identity gives a sum of squares equal to zero.','Algebra',46),('Pioneer 2',3,'An exterior-angle comparison uses the cyclic quadrilateral and the bisector.','Geometry',46),('Pioneer 3',4,'A useful modulus kills every factorial from the seventh onward, while triangular residues give the obstruction.','Number Theory',47),('Pioneer 4',6.5,'Simulate multiplication and addition using difference and division, with substantial exceptional-case work because equal operands are forbidden.','Algebra',48),('Pioneer 5',4,'Double-count mixed pairs in columns for the divisibility obstruction, then realize it with four column types.','Combinatorics',49),('Pioneer 6',2,'Translate all three variables by three to obtain a nonnegative expression vanishing only at zero.','Algebra',50),('Junior 1',3,'The gcd identity makes a fixed integer divisible by every positive integer.','Number Theory',50),('Junior 2',4.5,'The equal chords from the perpendicular-bisector point lead to an angle chain across two secants and a parallel.','Geometry',51),('Junior 3',2,'Conditioning on all but the first box leaves an unbiased parity switch.','Combinatorics',51),('Junior 4',5,'Count at least two forbidden squares on each interior antidiagonal, then match the bound with a boundary path.','Combinatorics',52),('Junior 5',5,'Two pairs of similar triangles incorporate the external equilateral triangles and sum to a straight angle.','Geometry',53),('Junior 6',6,'Construct a very large half-integer so every relevant binomial expansion has an integer part with enough powers of two.','Number Theory',54),('Senior 1',4.5,'Optimize a worst-case reachability formula using a strategically chosen residue and AM-GM.','Number Theory',54),('Senior 2',4.5,'The reflected circumcenter of BHC and the orthocenter vector identity reduce chord-midpoint location to a projection.','Geometry',54),('Senior 3',4.5,'Successive differences convert the expression into a symmetric pair-product sum bounded by Cauchy.','Algebra',55),('Senior 4',8,'Designing five forced interlocking equal-area polyominoes is substantially beyond the target, and the source construction requires a detailed diagram.','Combinatorics',56),('Senior 5',5,'Reflect the midpoint to create a circle centered at D, then apply a tangent power relation to determine the angle.','Geometry',57),('Senior 6',7,'A maximal-set count handles the first bound; the stronger bound requires recursive residue splitting and a concavity estimate.','Combinatorics',57)]}
S={}
def sol(year,label,statement,solution,tags=()):S[(year,label)]={'statement':statement,'solution':solution,'tags':tags}
sol(2020,'Senior 4',r'''Four circles $\Gamma_1,\Gamma_2,\Gamma_3,\Gamma_4$ are externally tangent in succession: their consecutive contact points are $A,B,C,D$, respectively (including $\Gamma_4$ with $\Gamma_1$). Prove that $A,B,C,D$ lie on one circle.''',r'''Invert about $A$. The first two circles become parallel lines. The other two become tangent circles, with centers $U,V$ and contact point $C'$, touching the parallel lines at $B',D'$.

Since $UB'\parallel VD'$ and $UB'=UC'$, $VD'=VC'$, the two isosceles triangles $UB'C'$ and $VC'D'$ have equal corresponding angles. As $U,C',V$ are collinear, this gives $B',C',D'$ collinear. Inverting their line back yields a circle through $A,B,C,D$.''',('Inversion','Tangency'))
sol(2020,'Senior 6',r'''Start with the integer $20$ on a board and score $0$. A move replaces an integer $a$ by positive integers $b,c$ satisfying $b+c=a$, adding $bc$ to the score. Continue until every entry is $1$. Find the difference between the largest and smallest possible final scores.''',r'''Let $Q$ be the sum of the squares of the board entries and $T$ the score. A move changes $Q$ by
$$b^2+c^2-(b+c)^2=-2bc,$$
so $Q+2T$ is invariant. Initially it is $400$. The sum of the entries stays $20$, so the final board contains twenty ones and $Q=20$. Thus every play has $T=(400-20)/2=190$, and the requested difference is $\boxed0$.''',('Invariants','Games'))
sol(2021,'Primary 3',r'''Label each of the twelve edges of a cube by $1$ or $-1$. Label each face by the product of its four edge labels. What is the minimum sum of all eighteen labels?''',r'''Suppose $e$ edge labels are positive. A face with negative product contains an odd number of positive edges, so the number $f$ of negative faces is at most $2e$, since each edge belongs to two faces. The total number of positive labels is $e+6-f$. If $e\le2$, this is at least $6-e\ge4$; if $e\ge3$, it is at least $3$. Consequently the total sum is at least $3-15=-12$.

To attain this, give positive labels to the top-front edge, bottom-right edge and back-left vertical edge, with all other edges negative. These three edges meet each face exactly once. All six face labels are negative, giving $\boxed{-12}$.''',('Double counting','Extremal combinatorics'))
sol(2021,'Junior 5 / Senior 2',r'''Six teams play a round robin. A win earns $3$ points, a draw $1$, and a loss $0$. The six final scores, in descending order, are distinct consecutive terms of an arithmetic progression with common difference $-2$. Prove that the fourth team won twice and lost three times.''',r'''Let the scores in ascending order be $p,p+2,\ldots,p+10$. Their sum is $6p+30\le45$, so $p=0,1$ or $2$.

If $p=0$, the bottom team loses to everyone, including the team with only $2$ points, which is impossible.

If $p=1$, there are six decisive games and nine draws. The bottom team has four losses. The next team, scoring $3$, has either one win and four losses or three draws and two losses. In the first case its four losses are additional to the bottom team's four, a contradiction. In the second case it must draw with the bottom team. The team scoring $5$ therefore beats the bottom team and has one win, two draws and two losses. It must also draw with the $3$-point team. Thus the four bottom-team losses, the two $3$-point-team losses and the two $5$-point-team losses are eight different decisive games, again impossible.

Hence $p=2$. There are three draws, giving six draw appearances. Teams with scores $2,4,8,10$ require at least $2,1,2,1$ draws, respectively (reduce their scores modulo $3$). They account for all six appearances. The fourth team has $6$ points and no draws, so has exactly two wins and three losses.''',('Tournament scores','Case analysis'))
sol(2021,'Senior 4',r'''An octagon has all eight interior angles equal, and every side has integer length. Prove that its opposite sides have equal lengths.''',r'''Its exterior angles are $45^\circ$. Orient the first side horizontally and denote consecutive lengths by $a_0,\ldots,a_7$. The sum of its side vectors is zero. Multiplying the horizontal and vertical equations by $\sqrt2$ gives
$$\sqrt2(a_0-a_4)+(a_1-a_3-a_5+a_7)=0,$$
$$\sqrt2(a_2-a_6)+(a_1+a_3-a_5-a_7)=0.$$
All bracketed quantities are integers. Irrationality of $\sqrt2$ implies $a_0=a_4$, $a_2=a_6$, and both remaining integer expressions vanish. Adding and subtracting those expressions gives $a_1=a_5$ and $a_3=a_7$.''',('Vectors','Irrationality'))
sol(2021,'Senior 5',r'''At a gathering, each guest has exactly four friends among the other guests. Whenever a guest is not friends with two others, those two are not friends with each other. Determine all possible numbers of guests.''',r'''Define two guests to be equivalent if they coincide or are not friends. The stated condition makes this relation transitive; it is also symmetric and reflexive. Thus the guests split into classes, with no friendships inside a class and all possible friendships between different classes.

If there are $n$ guests, every class must have size $n-4$, since each member has exactly four friends outside it. If there are $k$ classes, then $k(n-4)=n$, or
$$(k-1)(n-4)=4.$$
The positive divisor possibilities give $n-4=1,2,4$, hence $\boxed{n=5,6,8}$. They are attained by five singleton classes, three classes of size two, and two classes of size four.''',('Graph structure','Equivalence relations'))
sol(2021,'Senior 6',r'''Prove that some positive multiple of $5^{2021}$ has only odd decimal digits.''',r'''We prove more generally that for every $n\ge1$ there is an $n$-digit multiple of $5^n$ with only odd digits. Start with $5$. Suppose $N=5^nq$ is such a number. Seek the next number as $d10^n+N$, where $d\in\{1,3,5,7,9\}$. Dividing by $5^n$, the divisibility requirement is
$$2^nd+q\equiv0\pmod5.$$
The five permitted digits represent all residues modulo $5$, and $2^n$ is invertible, so exactly one works. Appending it on the left completes the induction.''',('Digit construction','Induction','Congruences'))
sol(2022,'Junior 4 / Senior 1',r'''A line divides both the area and the perimeter of a triangle into equal halves. Prove that it passes through the incenter.''',r'''Relabel so the line meets $AB,AC$ at $D,E$. Let the inradius be $r$ and the semiperimeter be $s$. The perimeter condition gives $AD+AE=s$, while the area condition gives $[ADE]=rs/2$.

Let $P=DE\cap AI$, where $AI$ is the internal angle bisector. Its perpendicular distances to $AB,AC$ are equal; call the common distance $x$. Splitting $ADE$ into $ADP$ and $AEP$ gives
$$[ADE]=\frac{x(AD+AE)}2=\frac{xs}2.$$
Hence $x=r$. There is exactly one point on the internal angle-bisector ray at distance $r$ from the sides, namely the incenter. Thus $P=I$.''',('Area','Incenter'))
sol(2022,'Junior 5 / Senior 2',r'''For which positive integers $n$ do there exist integers $a_1,\ldots,a_n$ with
$$a_1+\cdots+a_n=0,\qquad a_1\cdots a_n=n?$$''',r'''The answer is all multiples of $4$.

If $n$ is odd, all factors are odd, so their sum is odd. If $n\equiv2\pmod4$, exactly one factor is even and the other $n-1$ factors are odd, again giving an odd sum. Thus $4\mid n$ is necessary.

Write $n=4k$. The following constructions each have sum zero, length $4k$ and product $4k$; every stated number of copies is nonnegative.

* If $k$ is odd, use $2k,-2$, then $2k-2$ copies of $-1$, then $k$ pairs $(1,-1)$.
* If $k\equiv2\pmod4$, use $k,4$, then $k+4$ copies of $-1$, then $(3k-6)/2$ pairs $(1,-1)$.
* If $4\mid k$, use $k,-4$, then $k-4$ copies of $-1$, then $(3k+2)/2$ pairs $(1,-1)$.

For example, the first construction has product $-4k(-1)^{2k-2+k}=4k$; the other two sign counts are even as well. This proves sufficiency.''',('Parity','Integer construction'))
sol(2022,'Junior 6 / Senior 3',r'''Show that a $2022$-digit multiple of $2^{2022}$ exists whose decimal digits all belong to $\{1,2\}$.''',r'''Inductively construct an $n$-digit multiple $N=2^nq$ using only $1,2$. The starting case is $N=2$. Prepend a digit $d\in\{1,2\}$. Then
$$d10^n+N=2^n(d5^n+q).$$
Because $5^n$ is odd, choose $d=1$ if $q$ is odd and $d=2$ if $q$ is even. The parenthesis is even, so the new number is divisible by $2^{n+1}$. Induction reaches $n=2022$.''',('Induction','Restricted digits'))
sol(2022,'Senior 4',r'''A convex pentagon $ABCDE$ satisfies $\angle ABC=\angle ADE$ and $\angle ADB=\angle AEC$. Prove that $\angle BAC=\angle DAE$.''',r'''Put $F=BD\cap CE$. The equality $\angle ADF=\angle AEF$ shows that $A,F,D,E$ are concyclic. Consequently
$$\angle AFE=\angle ADE=\angle ABC,$$
so $A,B,C,F$ are also concyclic (using directed angles if necessary). The two circles now give
$$\angle BAC=\angle BFC=\angle DFE=\angle DAE.$$''',('Cyclic quadrilaterals','Auxiliary intersection'))
sol(2022,'Senior 5',r'''Let $a,b,r,s$ be positive integers with $a\ge2$ and $\gcd(a,b)=1$. Prove that
$$a^s+b^s\mid a^r+b^r\quad\Longrightarrow\quad s\mid r.$$''',r'''Write $r=qs+t$ with $0\le t<s$, and put $M=a^s+b^s$. Since $a$ and $b$ are coprime, $b$ is invertible modulo $M$. Using $a^s\equiv-b^s\pmod M$ in the given divisibility and cancelling $b^{qs}$ gives
$$(-1)^qa^t+b^t\equiv0\pmod M.$$
If $t>0$, both $a^t+b^t$ and $|a^t-b^t|$ are strictly less than $M$. They are nonzero: $a=b$ would contradict $a\ge2$ and coprimality. Thus neither can be a multiple of $M$. Therefore $t=0$, as required.''',('Exponent reduction','Divisibility'))
sol(2022,'Senior 6',r'''In a round robin with $n$ teams, wins, draws and losses earn $2,1,0$ points. Suppose that for every nonempty set $S$ of teams, some team earns an odd total of points against the members of $S$. Prove that $n$ is even.''',r'''Work modulo $2$. Form the $n\times n$ matrix $A$ whose entry $A_{ij}$ is $1$ exactly when teams $i,j$ draw. It is symmetric with zero diagonal. For a set $S$, its indicator vector $v$ satisfies $Av\ne0$ by the hypothesis. Thus $A$ has no nonzero kernel and is invertible.

We show that a symmetric zero-diagonal matrix of odd order cannot be invertible over the two-element field. Expand its determinant as a sum over permutations. Terms with a fixed point vanish. If $n$ is odd, any permutation without fixed points has an odd cycle of length at least three. Select the odd cycle containing the smallest element among all odd cycles, and reverse that cycle. This pairs permutations in a fixed-point-free involution. Symmetry makes the paired products equal, so they cancel modulo $2$. The determinant is zero, a contradiction. Hence $n$ is even.''',('Parity','Graphs','Linear algebra'))
sol(2023,'Senior 1',r'''Prove that infinitely many positive integers can each be expressed both as a sum of $2001$ distinct perfect squares and as a sum of $2023$ distinct positive perfect cubes.''',r'''Use
$$1^3+2^3+\cdots+23^3=(1+2+\cdots+23)^2=276^2.$$
Choose any $2000$ distinct integers $t_1,\ldots,t_{2000}$ greater than $276$, and add $t_1^6+\cdots+t_{2000}^6$ to both sides. Each sixth power is simultaneously the square $(t_i^3)^2$ and the cube $(t_i^2)^3$. The resulting integer has the required $2001$ distinct square terms and $2023$ distinct positive cube terms. Varying the largest $t_i$ gives infinitely many integers.''',('Constructive number theory','Powers'))
sol(2023,'Senior 4',r'''In right triangle $ABC$, $\angle BAC=90^\circ$ and $AD\perp BC$ with $D\in BC$. Choose $E\in CA$ and $F\in AB$ with $EF\parallel BC$. Choose $G\in AC$ so that $AG=CE$. Prove that $DG\perp DF$.''',r'''Parallelism and the altitude similarities give
$$\frac{AG}{BF}=\frac{CE}{BF}=\frac{AC}{AB}=\frac{AD}{BD}.$$
Also $\angle GAD=\angle FBD$, both equal to $90^\circ-\angle ACB$. Hence triangles $AGD$ and $BFD$ are similar by two proportional sides and their included angle. It follows that
$$\angle AGD=\angle BFD=180^\circ-\angle AFD,$$
so $A,F,D,G$ are cyclic. Since $\angle GAF=90^\circ$, the opposite angle $\angle GDF$ is also $90^\circ$.''',('Similarity','Right triangles','Cyclicity'))
sol(2023,'Senior 5',r'''Find the least positive real $m$ with this property: whenever $a,b,c$ are the side lengths of a triangle and $a^2+b^2>mc^2$, the side $c$ is the shortest.''',r'''The answer is $5$. If $c$ is not the shortest, suppose $b\le c$. The triangle inequality gives $a<b+c\le2c$, so
$$a^2+b^2<4c^2+c^2=5c^2.$$
Thus the implication holds for $m=5$.

For every $m<5$, choose a sufficiently small $\varepsilon>0$ and take
$$a=2-2\varepsilon,\quad b=1-\varepsilon,\quad c=1.$$
These form a triangle, $b<c$, and $a^2+b^2=5(1-\varepsilon)^2>m=mc^2$. Hence no smaller $m$ works.''',('Sharp constants','Triangle inequality'))
sol(2024,'Primary 5 / Junior 2',r'''Let $ABCD$ be a square with center $F$. Reflect $C$ in $B$ to obtain $E$. A point $G$ lies on ray $EF$ beyond $F$ and satisfies $\angle AGC=135^\circ$. Prove that $\angle CGD=135^\circ$.''',r'''Since $\angle AEC=45^\circ$, the condition $\angle AGC=135^\circ$ makes $A,E,C,G$ cyclic. Thus
$$\angle AGF=\angle AGE=\angle ACE=45^\circ=\angle ADF.$$
Therefore $A,D,G,F$ are cyclic. As the square's diagonals are perpendicular, $\angle AFD=90^\circ$, whence $\angle AGD=90^\circ$. The angles around $G$ now give
$$\angle CGD=360^\circ-135^\circ-90^\circ=135^\circ.$$''',('Cyclic quadrilaterals','Squares'))
sol(2024,'Primary 6 / Junior 3',r'''A circle contains $n$ red points and $n$ blue points, all distinct. A red frog starts on a red point and a blue frog on a blue point. Each minute the red frog moves to the next red point clockwise, and the blue frog to the next blue point anticlockwise. Prove that one fixed straight line separates the frogs at every integer time.''',r'''Interpolate each jump by continuous motion along its arc at constant speed during that minute. Each frog makes exactly one complete revolution in $n$ minutes, in opposite directions. Their relative angular displacement increases strictly by $4\pi$, so they meet exactly twice in a full period. Neither meeting occurs at an integer time, because red and blue points are distinct.

Call the two meeting points $U,V$. Between these meetings the red frog traverses one of the two arcs from $U$ to $V$, while the blue frog traverses the other. Between the second meeting and the next first meeting the same holds with the complementary arcs. Thus the chord line $UV$ separates their positions except at the two meeting instants. It therefore separates them at every integer time, and the motion repeats after $n$ minutes.''',('Continuous interpolation','Circular order'))
sol(2024,'Junior 5 / Senior 2',r'''Determine the positive integers that cannot be a sum $a_1+\cdots+a_k$, where $a_1=1$ and each difference $a_{i+1}-a_i$ is $1$ or $2$.''',r'''Only $\boxed{2,5}$ fail: one term gives $1$, two terms give $3$ or $4$, and three or more terms give at least $6$.

For $n\ge6$, choose the largest $k$ for which $T_k=k(k+1)/2\le n$, and write $n=T_k+r$ with $0\le r\le k$. If $r=0$, use $1,2,\ldots,k$. If $0<r<k$, raise the final $r$ entries of that list by $1$; exactly one gap becomes $2$. If $r=k$, use
$$1,3,4,\ldots,k,k+2.$$
It has $k$ terms, allowable gaps and sum $T_k+k$. The remaining representable small values are $1,3,4$.''',('Constructive sums','Triangular numbers'))
sol(2024,'Junior 6 / Senior 3',r'''Prove that for every positive integer $n$,
$$\sum_{i\ge1}\left\lfloor\sqrt{\frac{n}{i^3}}\right\rfloor
=\sum_{i\ge1}\left\lfloor\sqrt[3]{\frac{n}{i^2}}\right\rfloor.$$
(Each sum has only finitely many nonzero terms.)''',r'''Count ordered pairs of positive integers $(u,v)$ satisfying $u^2v^3\le n$. Fixing $v=i$ leaves exactly $\lfloor\sqrt{n/i^3}\rfloor$ choices for $u$, giving the left side. Fixing $u=i$ instead leaves exactly $\lfloor\sqrt[3]{n/i^2}\rfloor$ choices for $v$, giving the right side.''',('Double counting','Floor functions'))
sol(2024,'Senior 5',r'''There are $2025$ equally indexed positions around a circle. Let $S_1$ count subsets containing no pair whose circular indices differ by $3$, and let $S_2$ count subsets containing no pair whose circular indices differ by $6$ (differences are modulo $2025$). Prove that $S_1=S_2$ and that this common number is a perfect cube.''',r'''Multiplication of indices by $2$ modulo $2025$ is a permutation, since $2$ is coprime to $2025$. It maps pairs with index difference $\pm3$ exactly to pairs with difference $\pm6$. Applying it to every chosen index is therefore a bijection between the two families, so $S_1=S_2$.

For the first family, forbidden pairs lie entirely inside a single residue class modulo $3$. The three residue classes are independent and have identical cyclic restriction patterns, each with $675$ positions. If one class has $T$ permissible subsets, then $S_1=T^3$.''',('Bijections','Modular permutations','Graph components'))
sol(2024,'Senior 6',r'''A square $ABCJ$ is inscribed in a circle $\omega$ with center $O$. Let $M$ be the midpoint of $AB$ and let $\Gamma$ be the circle through $J,O,M$. Its second intersections with line $AJ$ and circle $\omega$ are $P$ and $Q$, respectively. If $R\in BC$ satisfies $RC=3RB$, prove that $P,Q,R$ are collinear.''',r'''Scale and rotate so that
$$J=(0,0),\ A=(0,1),\ B=(1,1),\ C=(1,0).$$
Then $O=(1/2,1/2)$ and $M=(1/2,1)$. The two circle equations are
$$\omega:\ x^2+y^2-x-y=0,$$
$$\Gamma:\ x^2+y^2+\tfrac12x-\tfrac32y=0.$$
Setting $x=0$ in the second gives $P=(0,3/2)$. Subtracting the equations gives the common chord line $y=3x$, and substituting into $\omega$ yields $Q=(2/5,6/5)$. Also $R=(1,3/4)$. These three points all satisfy $y=3/2-3x/4$, proving the claim.''',('Coordinate geometry','Radical axis'))
sol(2025,'Pioneer 3',r'''Find all positive integers $x,y$ satisfying
$$1!+2!+\cdots+x!=1+2+\cdots+y.$$''',r'''For $x\ge7$, the factorial sum is congruent modulo $7$ to
$$1!+2!+\cdots+6!=873\equiv5\pmod7.$$
But the triangular numbers $y(y+1)/2$ have only residues $0,1,3,6$ modulo $7$. Thus $x\le6$.

For $x=1,2,3,4,5,6$ the factorial sums are $1,3,9,33,153,873$. A number $N$ is triangular exactly when $8N+1$ is an odd square. Testing these six values gives only $1,3,153$, with $y=1,2,17$. The answers are $\boxed{(1,1),(2,2),(5,17)}$.''',('Congruences','Factorials'))
sol(2025,'Pioneer 4',r'''Two distinct positive real numbers $A,B$ are initially written on a board. A move chooses distinct numbers $x,y$ already present and writes either $|x-y|$ or $x/y$, retaining the existing numbers. Is it always possible eventually to write (i) $AB$ and (ii) $A+B$?''','',('Algebraic construction','Closure'))
sol(2025,'Pioneer 5',r'''Let $n$ be a positive even integer. Arrange coins in three rows and $n$ columns, choosing each coin's face freely. Require that deleting any row leaves exactly $n/2$ columns with one head and one tail. For which $n$ is this possible?''',r'''Count pairs of differently facing coins in the same column. The condition contributes $n/2$ pairs for each of the three choices of rows, so there are $3n/2$ pairs. A column contributes either $0$ pairs if all three coins agree, or $2$ otherwise. Hence $3n/2$ is even, which forces $4\mid n$.

Conversely, if $n=4k$, repeat each of the four column patterns
$$HHH,\quad HHT,\quad HTH,\quad HTT$$
exactly $k$ times. Every pair of rows disagrees in exactly two of these four patterns, so the requirement holds. Thus the answer is precisely the multiples of $4$.''',('Double counting','Parity','Construction'))
sol(2025,'Junior 2',r'''Let $ABC$ be acute with $AB<AC$. Choose a point $D$ on the perpendicular bisector of $BC$, and let the circle through $B,C,D$ meet lines $AB,AC$ again at $E,F$. Lines $DE,DF$ meet the line through $A$ parallel to $BC$ at $G,H$. Prove that $E,F,G,H$ are concyclic, whenever these intersections are distinct and defined.''',r'''Use directed angles modulo $180^\circ$, and put $P=DE\cap BC$. Since $DB=DC$, the base angles of $DBC$ agree. The circle through $B,C,D,E,F$ gives
$$\begin{aligned}
\angle EFD&=\angle ECD\\
&=\angle BCD-\angle BCE\\
&=\angle CBD-\angle BCE\\
&=\angle DEC-\angle BCE\\
&=\angle EPB.
\end{aligned}$$
Because $GH\parallel PB$ and $E,P,G,D$ are collinear, this last angle is $\angle EGH$. Thus $\angle EFH=\angle EGH$ modulo $180^\circ$, which is exactly the cyclicity condition.''',('Directed angles','Cyclic quadrilaterals'))
sol(2025,'Junior 4',r'''Some squares of an $n\times n$ grid contain obstacles. A path from the bottom-left square to the top-right square uses orthogonally adjacent steps and never occupies either an obstacle square or a square orthogonally adjacent to one. What is the maximum possible number of obstacles if such a path exists?''',r'''For $n=1$ the answer is $0$. Suppose $n\ge2$. Index squares by $(x,y)$ with $1\le x,y\le n$. The path visits every antidiagonal $x+y=d$, since a step changes $x+y$ by $1$.

Each interior antidiagonal $3\le d\le2n-1$ contains at least two squares without obstacles. For $d\le n+1$, take a visited square on antidiagonal $d-1$; its upper and right neighbors lie in the grid on antidiagonal $d$, and both must be clear. For $d\ge n+1$, take a visited square on antidiagonal $d+1$ and use its lower and left neighbors. The two corner antidiagonals each have one clear square. Hence at least
$$2+2(2n-3)=4n-4$$
squares are clear, leaving at most $(n-2)^2$ obstacles.

For equality, take the path along the bottom row and then the rightmost column. Put obstacles in every square outside the bottom two rows and the rightmost two columns. This gives exactly $\boxed{(n-2)^2}$.''',('Grid paths','Extremal counting'))
sol(2025,'Junior 5',r'''Let $ABCD$ be a cyclic quadrilateral with diagonals meeting at $P$. Construct outward equilateral triangles $WAB,XBC,YCD,ZDA$. Prove that
$$\angle WPZ+\angle YPX=180^\circ.$$''',r'''Cyclicity gives similarities $ABP\sim DCP$ and $ADP\sim BCP$. Adding the equal $60^\circ$ angles supplied by the outward equilateral triangles then yields
$$WAP\sim YDP,\qquad ZAP\sim XBP.$$
For example, $WA/AP=AB/AP=DC/DP=YD/DP$ and $\angle WAP=60^\circ+\angle BAP=60^\circ+\angle CDP=\angle YDP$.

Thus $\angle WPA=\angle DPY$ and $\angle APZ=\angle BPX$. Adding these and using the straight line $BPD$ gives
$$\angle WPZ+\angle YPX
=\angle DPY+\angle YPX+\angle XPB=180^\circ.$$''',('Equilateral triangles','Similarity'))
sol(2025,'Junior 6',r'''Suppose $x>1$ is real and $x^k\lfloor x^k\rfloor$ is an integer for every $k=1,\ldots,2025$. Must $x$ be an integer?''',r'''No. Take $x=2^{4049}+1/2$. For $1\le k\le2025$, every term except the last in the binomial expansion of $x^k$ is an integer multiple of $2^{2025}$: a term containing $(2^{4049})^i$ with $i\ge1$ has a power of two at least
$$4049i-(k-i)=4050i-k\ge2025.$$
Thus for some integer $N$,
$$x^k=2^{2025}N+2^{-k},\qquad \lfloor x^k\rfloor=2^{2025}N.$$
Their product is $2^{4050}N^2+2^{2025-k}N$, an integer. Yet $x$ is a nonintegral half-integer.''',('Floor functions','Binomial theorem','Counterexamples'))
sol(2025,'Senior 1',r'''Starting at $0$, a token may move either $k$ units forward or $1$ unit backward, where the positive integer $k$ is fixed. Choose $k$ to minimize the number $m$ such that every integer $a$ with $1\le a\le2025$ can be reached within $m$ moves. Find this least $m$.''',r'''Choose $k=45$. To reach $a$, move forward to the least multiple of $45$ not smaller than $a$, then backward to $a$. This uses at most $45+44=89$ moves.

For any fixed $k$, put $q=\lfloor2024/k\rfloor$ and consider $a=qk+1\le2025$. Any route to $a$ needs at least $q+1$ forward moves and at least $k-1$ backward moves, hence at least $q+k$ moves. Since $2024=qk+r$ with $r\le k-1$,
$$q+k\ge\frac{2025}{k}+k-1\ge2\sqrt{2025}-1=89.$$
Thus the optimum is $\boxed{89}$.''',('Optimization','Residue classes','AM-GM'))
sol(2025,'Senior 2',r'''A triangle $ABC$ has circumcenter $O$ and orthocenter $H$, with $\angle AOH=90^\circ$. Line $AO$ meets the circle through $B,H,C$ at $X,Y$. Prove that the midpoint of $XY$ belongs to the circumcircle of $ABC$.''',r'''Use vector coordinates with $O$ as origin and circumradius $R$. Write the vertex vectors as $a,b,c$. The orthocenter vector is $h=a+b+c$.

The circle through $B,H,C$ has center $o'=b+c=h-a$: its distances to $b,c,h$ are respectively $|c|,|b|,|a|$, all equal to $R$. The midpoint of chord $XY$ is the perpendicular projection of $o'$ onto line $AO$. Because $a\cdot h=0$, this projection is
$$\frac{(h-a)\cdot a}{R^2}a=-a.$$
This is the antipode of $A$ on the original circumcircle, proving the claim.''',('Vectors','Orthocenter','Chord midpoint'))
sol(2025,'Senior 3',r'''For an integer $n\ge2$, find the maximum of
$$\sum_{i=1}^{n-1}x_i(x_{i+1}-x_i)$$
over positive real numbers $x_1\le x_2\le\cdots\le x_n\le n$.''',r'''Put $d_1=x_1$ and $d_i=x_i-x_{i-1}$ for $i\ge2$. These are nonnegative and have sum $s=x_n\le n$. The expression becomes
$$\sum_{i<j}d_id_j=\frac12\left(s^2-\sum_{i=1}^nd_i^2\right).$$
By Cauchy's inequality, $\sum d_i^2\ge s^2/n$. Therefore the expression is at most
$$\frac{n-1}{2n}s^2\le\frac{n(n-1)}2.$$
Equality is attained by $d_1=\cdots=d_n=1$, equivalently $x_i=i$. Hence the maximum is $\boxed{n(n-1)/2}$.''',('Substitution','Cauchy-Schwarz','Sharp inequalities'))
sol(2025,'Senior 5',r'''Let $ABC$ be acute with circumcenter $O$. Let $M,N$ be the midpoints of $BC,AO$. The tangent at $A$ to the circumcircle meets line $BC$ at $D$. If $DM=DN$, determine $\angle A$.''',r'''Scale the circumradius to $1$ and choose coordinates $O=(0,0)$, $A=(0,1)$. Then $N=(0,1/2)$ and $D=(d,1)$ because $AD$ is tangent. Since $OM\perp BC$, the right triangle $OMD$ gives
$$DM^2=OD^2-OM^2=d^2+1-OM^2.$$
On the other hand, $DN^2=d^2+1/4$. Their equality forces $OM^2=3/4$.

Thus the distance of chord $BC$ from its circle center is $\sqrt3/2$, so the minor central angle $BOC$ is $60^\circ$. Its inscribed angle at $A$ is either $30^\circ$ or $150^\circ$. The triangle is acute, giving $\boxed{\angle A=30^\circ}$.''',('Coordinate geometry','Tangent','Chord lengths'))
sol(2025,'Senior 6',r'''Let $S$ be a set of $2025$ distinct integers. Call a subset progression-free if it contains no three distinct terms in arithmetic progression. Prove that $S$ has a progression-free subset of size at least (i) $37$; (ii) $119$.''',r'''For (i), choose a progression-free subset $T$ maximal under inclusion, of size $t$. Every excluded element completes a progression with some pair $a,b\in T$, so it is one of $2a-b,2b-a,(a+b)/2$. Consequently
$$2025\le t+3\binom t2.$$
At $t=36$ the right side is $1926$, and it increases with $t$, so $t\ge37$.

For (ii), set $\alpha=\log_3 2$. We prove by strong induction that every $n$-element integer set has a progression-free subset of size at least $n^\alpha$. The cases $n=0,1$ are immediate. Translate and divide by $3$ repeatedly if all elements have the same residue; these operations preserve progressions, and eventually at least two residue classes are nonempty. Let their sizes, in decreasing order, be $a\ge b\ge c$, with $b>0$.

A three-term progression modulo $3$ has either one residue throughout or all three residues. Therefore progression-free subsets chosen within the two largest classes can be united safely. Induction gives a subset of size at least $a^\alpha+b^\alpha$. Put $t=a/b\ge1$. Concavity of $u^\alpha$ means its increments over intervals of length two decrease, so
$$(t+2)^\alpha-t^\alpha\le3^\alpha-1=1.$$
Hence
$$a^\alpha+b^\alpha\ge(a+2b)^\alpha\ge(a+b+c)^\alpha=n^\alpha.$$
The induction follows. Finally, because $2025<3^7$ and $\alpha-1<0$,
$$2025^\alpha>2025(3^7)^{\alpha-1}=\frac{2025\cdot128}{2187}>118.$$
The integral subset size is therefore at least $119$.''',('Arithmetic progressions','Induction','Residue splitting'))
# Store primary-source records separately from the corpus while preserving one export schema.
for year,rows in R.items():
 for index,(label,rating,reason,topic,page) in enumerate(rows,1):
  slug=f'mys_{year}_imonst2_{index:02d}'
  catnum=label.split(' / ')[-1]; category,num=catnum.split()
  supplied=S.get((year,label),{})
  if 4<=rating<=7 and not supplied:raise RuntimeError((year,label,'missing manually written content'))
  raw={'country':'Malaysia','competition':'IMONST 2 — '+category,'year':year,'section':category,'problem_number':num,'problem_markdown':supplied.get('statement',label+' (see official source)'), 'solutions_markdown':[supplied.get('solution','')], 'primary_domain':topic,'topics':[[topic,t] for t in supplied.get('tags',[])], 'booklet_title':'IMO Committee Malaysia: IMONST 2 2020–2025 Solutions','sourceDataset':'IMO Committee Malaysia official archive','sourceLicense':'Original mathematical formulation and solution exposition; official source linked.'}
  (RAW/(slug+'.json')).write_text(json.dumps(raw,ensure_ascii=False,indent=2))
  review={'difficulty':rating,'reason':reason,'sourceUrl':URL+f'#page={page}','solutionUrl':URL+f'#page={page}','note':'Reviewed against the official complete solution compilation. Original appearance: '+str(year)+' IMONST 2, '+label+'.'}
  if supplied.get('solution'):review['solutionOverride']=supplied['solution']
  else:review['solutionKind']='source-link'
  REV[slug]=review
  if slug not in {x[0] for x in MAN}:MAN.append([slug,'malaysia-official',year,'IMONST 2 — '+category,0,0,num])
(P/'reviews.json').write_text(json.dumps(REV,ensure_ascii=False,indent=2));(P/'manifest.json').write_text(json.dumps(MAN,ensure_ascii=False,indent=2))
print('Added Malaysia complete compilation:',sum(map(len,R.values())),'distinct tasks;',len(S),'in target band.')
