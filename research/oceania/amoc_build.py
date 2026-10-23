import json
P='/workspace/sites/olympiad-atlas/research/oceania/'
items=[];ledger=[]
def url(y):return f'https://enrichedmaths.maths.uwa.edu.au/Olympiad/SMC/SMC{y}wsoln'+('a' if y==2023 else '')+'.pdf'
def add(y,n,d,topic,tags,s,sol,r):
 id=f'aus_amoc_{y}_{n}'
 items.append(dict(id=id,country='Australia',competition='AMOC Senior Contest',year=y,number=str(n),statement=s,solution=sol,sourceUrl=url(y),solutionUrl=url(y),topic=topic,tags=tags,difficulty=d,ratingReason=r,reviewStatus='individually-assessed',solutionKind='original-exposition',notes='Australian Mathematics Trust paper hosted by the University of Western Australia. Mathematical statement paraphrased and displayed exposition independently written.'))
 ledger.append(dict(id=id,country='Australia',competition='AMOC Senior Contest',year=y,number=str(n),difficulty=d,status='reviewed',included=True,reason=r,sourceUrl=url(y)))
def skip(y,n,d,r):ledger.append(dict(id=f'aus_amoc_{y}_{n}',country='Australia',competition='AMOC Senior Contest',year=y,number=str(n),difficulty=d,status='reviewed' if d else 'pending-solution-review',included=False,reason=r,sourceUrl=url(y)))
skip(2018,1,1.5,'Factoring the difference of square roots gives sqrt(a)+sqrt(b)=1 and the immediate upper bound one.')
add(2018,2,4,'Number Theory',['coprimality','short intervals','construction'],r'Prove that every ten consecutive positive integers contain five that are pairwise coprime.',r'''Among the five odd numbers, at most two are divisible by three. Discard one multiple of three, leaving four odd numbers with at most one multiple of three. No two of these four can share a prime factor greater than three: two odd multiples of five differ by at least ten, and two odd multiples of seven differ by at least fourteen.

Among the five even numbers, at most two are divisible by three, at most one by five, and at most one by seven. Choose an even number divisible by none of these primes. Together with the four chosen odd numbers, it gives a pairwise coprime set: any common prime divisor would divide a nonzero difference at most nine, so would be one of $2,3,5,7$, all of which have been excluded.''','The construction must coordinate an odd-number selection with an even number avoiding every possible small shared prime.')
skip(2018,3,2.5,'Among the seven first-match losers, the last two results have only three allowed patterns; pigeonhole immediately gives three identical records.')
add(2018,4,6.5,'Geometry',['tangents','cyclic quadrilaterals','circle centres','equivalence'],r'Circles $K_1,K_2$ meet at $A,B$. The tangents to $K_1$ at these points meet at $P$ inside $K_2$, and $BP$ meets $K_2$ again at $C$. The tangents to $K_2$ at $A,C$ meet at $Q$, and $QA$ meets $K_1$ again at $D$. Prove $QP\perp PD$ if and only if the centre of $K_2$ lies on $K_1$.',r'''Let $O$ be the centre of $K_2$ and $X$ that of $K_1$. First assume $O\in K_1$. Since $AD$ is tangent to $K_2$, $OA\perp AD$, so $OD$ is a diameter of $K_1$. The common chord $AB$ is perpendicular to the centres' line $OX$, and the two tangents to $K_1$ are symmetric about this line. Thus $D,O,X,P$ are collinear.

Reflection in this line interchanges $A,B$, so $\angle PAO=\angle PBO=\angle BCO$. Consequently $A,O,P,C$ are cyclic. The right angles at $A,C$ also put $A,O,Q,C$ on one circle. Thus $P$ lies on the circle with diameter $OQ$, giving $QP\perp PO$, hence $QP\perp PD$.

Conversely, tangent-chord angle equalities give, with directed angles,
$$\angle QAC=\angle QCA=\angle PAB=\angle PBA=\alpha.$$
It follows that $\angle APB=\angle AQC$, so $A,Q,C,P$ are cyclic, and $PQ$ bisects $\angle APC$. If $PD\perp PQ$, then $PD$ is the other bisector of the angle formed by the equal tangents $PA,PB$. Therefore $P,D,O,X$ are collinear. Since $OA\perp AD$ and $XA=XD$, the right-triangle angle relations give $\angle XOA=\angle XAO$. Hence $XO=XA$, which says $O\in K_1$.''','Both directions require identifying a common cyclic pentagon and relating two different angle bisectors to the line of circle centres.')
add(2018,5,4.5,'Algebra',['functional equations','surjectivity','positive functions'],r'Find all $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfying $xf(xf(2y))=y+xyf(x)$ for all $x,y>0$.',r'''The only solution is $f(x)=1/x$. At $x=1$, the equation gives $f(f(2y))=y(1+f(1))$. The right side takes every positive value, so $f$ is surjective. Choose $a>0$ with $f(2a)=1$. Substitution of $y=a$ yields
$$xf(x)=a(1+xf(x)).$$
Positivity forces $a<1$ and then $f(x)=c/x$, where $c=a/(1-a)>0$. Substitution into the original equation gives $2y=y(1+c)$, hence $c=1$. Direct substitution verifies this function.''','Surjectivity has to be extracted from a nested composition before a specially chosen input collapses the functional equation.')
skip(2019,1,3,'For odd n the peak-minus-valley angle sum telescopes to two positive endpoint angles.')
skip(2019,2,3,'Clearing pairwise-coprime denominators shows each is ±1, leaving the even integers from −10 to10.')
add(2019,3,4,'Combinatorics',['grid colouring','cyclic construction','sharp bounds'],r'A $2017\times2019$ grid is coloured black and white so that, in every row and every column, the counts of the two colours differ by one. What is the largest possible difference between the total numbers of black and white cells?',r'''The answer is $2017$. Summing the signed colour differences over the $2017$ rows gives an absolute difference at most $2017$.

To attain it, first make a $2017\times2017$ square whose first column has $1009$ black and $1008$ white cells. Form each following column by cyclically shifting the preceding one down by one place. Every row and column of this square has one more black cell than white cell.

Append two complementary columns, one with $1009$ black cells and the other with the opposite colours. Each new column has colour-count difference one, and the pair contributes one cell of each colour to every row. Thus each row still has one extra black cell, giving total difference $2017$.''','The elementary upper bound must be realized while satisfying both row and column constraints; a cyclic square and complementary extension do this.')
skip(2019,4,None,'Both implications of the reflected-point circumcircle condition still need a complete proof assessment.')
add(2019,5,4.5,'Algebra',['functional equations','odd functions','substitution'],r'Find all $f:\mathbb R\to\mathbb R$ satisfying $(x-y)f(x+y)=xf(x)-yf(y)$ for all real $x,y$.',r'''Exactly the affine functions $f(x)=ax+b$ work. Subtract the constant $f(0)$ and call the resulting function $g$. It satisfies the same equation and $g(0)=0$. Taking $y=-x$ shows $g(-x)=-g(x)$ for nonzero $x$, and this holds at zero as well.

The equations for $(x,y)$ and $(x,-y)$ now have equal right sides, giving
$$(x-y)g(x+y)=(x+y)g(x-y).$$
Every real pair $u,v$ can be written $u=x+y,v=x-y$, so $vg(u)=ug(v)$. Taking $v=1$ proves $g(u)=ug(1)$. Restoring the subtracted constant gives the stated family, and substitution verifies it.''','Removing the constant and proving oddness makes a reflection of one input reveal homogeneity for arbitrary real pairs.')
skip(2020,1,3,'Assuming all three quadratics lack real roots gives three incompatible discriminant inequalities; the zero leading-coefficient case is immediate.')
add(2020,2,5,'Combinatorics',['Euler trails','bipartite graphs','rook tours'],r'For integers $m,n>1$, determine when the cells of an $m\times n$ board can be labelled $1,\ldots,mn$ so that consecutive labels share a row or column, but no three consecutive labels share a row or column.',r'''It is possible exactly when $m=2$, or $n=2$, or both dimensions are even.

Construct a bipartite graph with one vertex for each row and one for each column; cell $(i,j)$ is represented by the edge joining its row and column. A valid numbering is exactly an Euler trail: successive edges meet, and the prohibition on three labels in a common row or column makes the shared endpoint alternate between row and column vertices.

A connected finite graph has an Euler trail exactly when it has zero or two vertices of odd degree. Necessity follows because every intermediate visit pairs an entering and leaving edge. Sufficiency follows by tracing a trail and splicing in unused closed trails, with an extra edge between the odd vertices if necessary.

Here the row vertices have degree $n$ and the column vertices degree $m$. There are zero odd degrees if both are even; if just one is odd, there are two odd degrees precisely when the other dimension is two. If both are odd, there are $m+n>2$ odd vertices. This proves the classification.''','A constrained grid ordering must be converted into an Euler trail in a different graph, after which degree parity yields both necessity and existence.')
add(2020,3,4,'Number Theory',['greedy sequences','divisibility','factor bounds'],r'Start with an integer $a_1>1$. Thereafter let $a_k$ be the least integer greater than $a_{k-1}$ divisible by none of $a_1,\ldots,a_{k-1}$. Prove that only finitely many terms are composite.',r'''Every integer greater than $a_1$ that fails to enter the sequence is divisible by an earlier selected term: this is exactly why the greedy rule skips it.

Suppose a selected composite $a_i$ exceeds $a_1^2$. Write $a_i=cd$ with $c,d>1$ and choose the larger factor $c$, so $a_1<c<a_i$. If $c$ was itself selected earlier, its divisibility into $a_i$ violates the defining rule. If it was skipped, some earlier selected term divides $c$ and hence also $a_i$, giving the same contradiction.

Thus every composite selected term is at most $a_1^2$, leaving only finitely many possibilities.''','The greedy minimality has to be applied to a proper factor that may itself have been skipped, producing an explicit uniform bound.')
add(2020,4,6,'Geometry',['circumcentres','angle bisectors','midpoints','cyclic quadrilaterals'],r'In acute triangle $ABC$ with $AB>AC$, let $O$ be the circumcentre and $P$ the altitude foot from $A$ onto $BC$. Let $D,E,F$ be the midpoints of $BC,CA,AB$. Set $Q=AO\cap DE$ and $R=AO\cap DF$. Prove $D$ is the incentre of triangle $PQR$.',r'''Let line $AO$ meet the circumcircle again at $X$; then $AX$ is a diameter. Since $DE\parallel AB$,
$$\angle AQE=\angle XAB=90^\circ-\angle BXA=90^\circ-\angle BCA=\angle CAP.$$
In right triangle $APC$, its hypotenuse midpoint $E$ satisfies $EA=EP=EC$, so $\angle CAP=\angle APE$. These equalities show that $A,Q,P,E$ are cyclic.

The equal chords $EA,EP$ in this circle give $\angle RQD=\angle DQP$, with the internal-angle choice supplied by the acute configuration and $AB>AC$. Hence $QD$ bisects the angle at $Q$ of $PQR$.

Interchanging $B,C$ and using $F$ in place of $E$ gives $\angle DRQ=\angle PRD$, so $RD$ is the internal bisector at $R$. Their intersection $D$ is therefore the incentre.''','A diameter extension and hypotenuse-midpoint circles create two cyclic quadrilaterals, from which the correct internal bisectors must be identified.')
add(2020,5,6,'Algebra',['functional equations','injectivity','multiplicativity','additivity'],r'Find all $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfying $f(x^{f(y)})=f(x)^y$ for all positive $x,y$.',r'''The solutions are $f\equiv1$ and $f(x)=x$. Suppose $f(a)\ne1$ for some $a$. If $f(y)=f(z)$, using $x=a$ in the equation gives $f(a)^y=f(a)^z$, so $y=z$: the function is injective.

Evaluate $f(x^{f(y)f(z)})$ first by two successive applications and then by one with input $yz$. The resulting values are both $f(x)^{yz}$. Injectivity, with any $x\ne1$, gives $f(yz)=f(y)f(z)$.

Now use this multiplicativity to evaluate
$$f(x^{f(y)+f(z)})=f(x^{f(y)})f(x^{f(z)})=f(x)^{y+z}=f(x^{f(y+z)}).$$
Injectivity again gives $f(y+z)=f(y)+f(z)$. A positive additive function is strictly increasing, since $v>u$ implies $f(v)=f(u)+f(v-u)>f(u)$. Multiplicativity gives $f(1)=1$, and additivity then fixes every positive rational. Trapping an arbitrary positive real between rational numbers proves $f(x)=x$. Both proposed functions satisfy the equation.''','Nested exponent substitutions first force multiplicativity and then additivity; positivity is needed to exclude nonstandard additive behavior.')
skip(2021,1,3.5,'Two pairs of similar triangles give equal division ratios, forcing KM parallel to the bases and hence the angle bisector.')
add(2021,2,4.5,'Combinatorics',['triangular grids','tilings','parity','construction'],r'An equilateral triangle of integer side $n$ is divided into unit equilateral triangles. A tile consists of two unit triangles with the same orientation that share exactly one vertex. For which positive $n$ can the entire triangle be tiled?',r'''Exactly the multiples of four work. There are $n(n+1)/2$ upward unit triangles and $n(n-1)/2$ downward ones. Every tile uses two of one orientation, so both counts must be even. Their simultaneous divisibility by two is equivalent to $4\mid n$.

It remains to tile a side-four triangle, since a triangle of side $4k$ splits into side-four triangles, possibly rotated. For an explicit tiling, use lattice basis vectors at $60^\circ$. Write $U(i,j)$ for the upward triangle with vertices $(i,j),(i+1,j),(i,j+1)$ and $D(i,j)$ for the downward triangle with vertices $(i+1,j),(i,j+1),(i+1,j+1)$.

Pair the ten upward triangles as
$$U(0,0)\!:\!U(1,0),\ U(0,1)\!:\!U(0,2),\ U(0,3)\!:\!U(1,2),\ U(1,1)\!:\!U(2,0),\ U(2,1)\!:\!U(3,0).$$
Pair the six downward triangles as
$$D(0,0)\!:\!D(0,1),\ D(0,2)\!:\!D(1,1),\ D(1,0)\!:\!D(2,0).$$
Each pair shares exactly one vertex, and every unit triangle occurs once. This supplies the required construction.''','Separate parity counts for the two triangle orientations give the obstruction, and a complete small tiling must be constructed for sufficiency.')
add(2021,3,4.5,'Combinatorics',['equal sums','equal square sums','symmetric construction'],r'Can two lists of $2021$ positive integers have equal sums and equal sums of squares while all $4042$ entries are distinct?',r'''Yes. More generally take $n\ge3$, put $N=1+2+\cdots+(n-1)$, and choose an integer $x>N$. Use the two lists
$$x+1,x+2,\ldots,x+n-1,x-N$$
and
$$x-1,x-2,\ldots,x-(n-1),x+N.$$
Every entry is positive and the lists are disjoint because $N>n-1$. Each list has sum $nx$. For the square sums, expanding around $x$ gives the same constant part $nx^2$, while the linear terms cancel since $N=\sum_{j=1}^{n-1}j$. The remaining square terms in both lists are $N^2+\sum_{j=1}^{n-1}j^2$. Taking $n=2021$ proves existence.''','A symmetric signed-deviation construction has to satisfy two moment conditions simultaneously while preserving positivity and complete distinctness.')
add(2021,4,6,'Geometry',['tangent circles','parallelograms','angle chasing'],r'In triangle $ABC$, let $M$ be the midpoint of $BC$. The tangent at $B$ to circle $ABM$ meets line $AC$ at $P$. Circle $PAM$ meets line $PB$ again at $Q$. Prove circle $QMC$ is tangent to line $AC$.',r'''Use directed angles, and set $R=QM\cap AB$. The circle $PAMQ$ and the tangent at $B$ give
$$\angle ACM=\angle AMB-\angle MAC=\angle RBP-\angle RQB=\angle BRM.$$
Therefore $A,R,C,M$ are cyclic. These two cyclic quadrilaterals then give
$$\angle RQP=\angle MAC=\angle MRC,$$
so $BQ\parallel RC$.

Since $R,Q,M$ are collinear and $BM=MC$, the parallelism implies $RM=MQ$: the two triangles at $M$ are similar with equal corresponding base lengths. Hence $B,R,C,Q$ is a parallelogram.

Finally,
$$\angle ACM=\angle ARM=\angle CQM.$$
This is the tangent-chord equality at $C$ for circle $QMC$, proving that its tangent there is $AC$.''','An auxiliary line intersection must reveal a cyclic quadrilateral and then a parallelogram before the final tangent-chord criterion becomes available.')
skip(2021,5,None,'The positive-real nested functional equation is statement-screened but its full solution is not yet assessed.')
add(2023,1,4,'Combinatorics',['rewriting systems','invariants','obstruction'],r'A move on a finite word in $A,B$ replaces an occurrence of $AB$ by $BBAA$. Can every starting word eventually be transformed so that all $B$s precede all $A$s?',r'''No; for example start with $AAB$. The property of containing either $AAB$ or $ABB$ is preserved by every move. A move away from a displayed block leaves that block unchanged. If it acts inside $AAB$, the result $ABBAA$ contains $ABB$. If it acts inside $ABB$, the result $BBAAB$ contains $AAB$.

Thus every word obtainable from $AAB$ still contains one of these two forbidden blocks. A word in which all $B$s precede all $A$s contains neither, so it cannot be reached.''','A single forbidden pattern is not preserved, so the obstruction must track a mutually regenerating pair of patterns.')
add(2023,2,5.5,'Number Theory',['games','decimal digits','modular invariants'],r'Alice starts by writing one nonzero decimal digit. Bob and Alice then alternately append or prepend one digit, with no leading zeros. Bob wins as soon as the displayed integer is divisible by a fixed positive integer $m$. Find the smallest $m$ for which Alice can prevent this forever: (a) with the stated one-digit start; (b) if Alice may start with any positive integer.',r'''The answers are (a) $12$ and (b) $11$. For $m\le10$, Bob can append a digit to obtain a multiple of $m$, because the ten possible results are consecutive integers. In (a), $m=11$ also lets Bob win immediately by repeating Alice's first digit.

For (a), Alice starts at $5$ and leaves a number congruent to $5$ modulo $6$ after each turn. Bob cannot win by prepending, since the number remains odd. Appending a digit $e$ produces a number congruent to $2+e$ modulo $12$, never zero for $0\le e\le9$. Alice restores her invariant by appending one of $1,3,5$, whose resulting residues include all odd classes modulo six.

For (b), Alice starts at $120$. Her invariant is an odd digit count and residue $-1$ modulo $11$. Appending digit $e$ produces residue $e+1$, and prepending it produces $-e-1$; neither is zero for a legal digit. Alice copies Bob's digit at the same end. This adds a multiple of eleven, with an extra factor $100$ if appended, restoring both the residue and the odd digit count. Thus Bob never wins.''','The two starting rules require different invariants, and each strategy must survive either prepending or appending digits.')
add(2023,3,6,'Geometry',['cyclic quadrilaterals','rectangles','parallel lines'],r'Points $A,B,C,D$ lie respectively on sides $EF,FG,GH,HE$ of parallelogram $EFGH$. Suppose $AC\perp EF$, $BD\perp FG$, and $ABCD$ is cyclic. Let $Q\in AC$ satisfy $FQ\parallel BC$. Prove $EQ\parallel DC$.',r'''Let the circle $ABCD$ meet line $FG$ again at $X$ and line $EH$ again at $Y$. Because $BD$ is perpendicular to both these parallel lines, the cyclic quadrilateral $B,X,Y,D$ is a rectangle; in particular $XY\perp FG$.

Set $Q'=XY\cap AC$. Since $AC\perp EF$ and $XY\perp FG$, the angles at $A$ and $X$ in $A,F,X,Q'$ are right angles, so these four points are cyclic. Therefore
$$\angle FQ'A=\angle FXA=\angle BCA,$$
where the final equality uses circle $ABCD$. It follows that $FQ'\parallel BC$, so the defining uniqueness gives $Q'=Q$.

The same argument with $E,Y,D$ replacing $F,X,B$ shows that $A,E,Y,Q$ is cyclic and
$$\angle EQA=\angle EYA=\angle DCA$$
with directed angles interpreted consistently. Hence $EQ\parallel DC$.''','Two additional intersections with the original circle create a rectangle, then two separate right-angle circles transfer the desired parallelism.')
skip(2023,4,None,'The row-column parity invariant is checked, but the full extremal constructions depend on diagrams not yet independently verified.')
add(2023,5,5.5,'Algebra',['inequalities','sorting','summation by parts','sum of squares'],r'For real numbers $a_1,\ldots,a_n,b_1,\ldots,b_n$ with $n\ge2$, put $K=\max b_i$ and $L=\min b_i$. Prove $\displaystyle\sum_{i<j}a_i a_j|b_i-b_j|\le\frac{K-L}{2}(a_1+\cdots+a_n)^2$.',r'''Reorder the paired entries so that $b_1\le\cdots\le b_n$, and put $d_k=b_{k+1}-b_k\ge0$. If $U_k=\sum_{i\le k}a_i$ and $V_k=\sum_{i>k}a_i$, expanding each difference as a sum of consecutive gaps gives
$$\sum_{i<j}a_i a_j|b_i-b_j|=\sum_{k=1}^{n-1}d_kU_kV_k.$$
For arbitrary real $U,V$, the inequality $UV\le(U+V)^2/2$ follows from $U^2+V^2\ge0$. Since $U_k+V_k=\sum_i a_i$, the preceding sum is at most
$$\frac12\left(\sum_{k=1}^{n-1}d_k\right)\left(\sum_i a_i\right)^2
=\frac{K-L}{2}\left(\sum_i a_i\right)^2.$$
The nonnegativity of the gaps permits termwise comparison despite the unrestricted signs of the $a_i$.''','Sorting and expanding distance gaps turns a signed pairwise sum into products of partial sums; ordinary termwise positivity arguments would fail.')
skip(2024,1,2.5,'Period100 and reversal identify residue classes in 49 pairs and two fixed classes, giving51 colours.')
add(2024,2,4.5,'Algebra',['nested recurrences','strong induction','monotonicity'],r'A function $f$ from positive integers to positive integers satisfies $f(1)=1$ and $f(n+1)=n+2-f(f(n))$. Prove that $f$ is nondecreasing.',r'''Prove the stronger statement that every successive difference is zero or one. Initially $f(2)=2$, so the claim holds. Suppose it holds for differences through $f(k+1)-f(k)$. Then $f(k)\le k$, and subtracting two recurrence equations gives
$$f(k+2)-f(k+1)=1-\bigl(f(f(k+1))-f(f(k))\bigr).$$
If $f(k+1)=f(k)$, the expression in brackets is zero. Otherwise $f(k+1)=f(k)+1$, and the induction hypothesis applies to the adjacent inputs $f(k),f(k)+1$, because $f(k)\le k$. The bracket is therefore zero or one in this case too.

Thus the next difference is zero or one, completing strong induction and proving monotonicity.''','A stronger bounded-increment induction is necessary to control the nested function arguments and justify applying the induction hypothesis.')
add(2024,3,5.5,'Number Theory',['gcd graphs','cyclic arrangements','prime factors','construction'],r'For $n>5$, start with $2,3,\ldots,n$ and delete every prime greater than $n/3$. Determine when the remaining integers can be arranged around a circle so that every neighbouring pair has gcd greater than one.',r'''Exactly $n=6,7,8$ and all $n\ge12$ work. For $6\le n\le8$, the remaining integers are all even. For $9\le n\le11$, both $3$ and $9$ can be adjacent only to each other and $6$. They would force the isolated three-cycle $3,6,9$, preventing inclusion of the other numbers.

Now let $n\ge12$. For each prime $p>3$ with $p\le n/3$, form a block containing every remaining odd number whose largest prime factor is $p$, together with the even number $2p$. Arrange this block with first term $2p$ and last term $3p$; all entries are divisible by $p$.

The remaining odd numbers are powers of three. Put these in a base block beginning with $12$, followed by all these odd powers, then $6$, then all unused even numbers. Every adjacency inside this block has a shared factor, its first entry is divisible by six, and its last entry is even.

Join the prime blocks after the base block, alternately in forward and reverse order. At each join the endpoints share factor two or three. The last endpoint shares either factor with the initial $12$, closing the circle. Every surviving number is used once. In particular, even composites whose largest prime factor exceeds $n/3$ simply belong to the base block.''','A sharp small-case obstruction is followed by a prime-factor block construction; the even composites omitted by a naive largest-prime partition need explicit placement.')
add(2024,4,5.5,'Combinatorics',['union-closed families','inclusion-exclusion','parity'],r'A finite school has a nonempty family of nonempty clubs. The union of any two clubs is also a club, but no student belongs to every club. Must some club have an even number of students?',r'''Yes. Suppose instead that every club has odd size. Let $S$ be the union of all clubs. Closure under pairwise unions makes $S$ itself a club, so $|S|$ is odd.

For each club $A$, take its complement $T=S\setminus A$ within $S$. Each $T$ has even size. These complements are closed under intersections, because
$$(S\setminus A)\cap(S\setminus B)=S\setminus(A\cup B).$$
Hence every nonempty finite intersection of the complements has even size. Their union is all of $S$: otherwise a student outside that union would belong to every club.

Apply inclusion-exclusion to this union. Every term on its right-hand side is even, so $|S|$ is even, contradicting its odd size. Some club must therefore have even size.''','Passing to complements changes union closure into intersection closure, allowing inclusion-exclusion to turn a local parity assumption into a global contradiction.')
add(2024,5,6.5,'Geometry',['radical axes','midpoints','cyclic quadrilaterals','concurrence'],r'In triangle $ABC$ with $AB<AC$, the altitude line from $A$ meets its circumcircle again at $D$. Let $M$ be the midpoint of $BC$, and let $DM$ meet the circumcircle again at $E$. Choose $P\in BC$ with $PA=PC$. Line $CE$ meets circle $BPE$ again at $F$. Prove that line $AB$, the perpendicular bisector of $BC$, and the line through $F$ parallel to $BC$ are concurrent.',r'''Let $Q$ be the intersection of $AC$ with the perpendicular bisector of $BC$, and let the parallel through $F$ meet $AB$ at $G$. Use directed angles throughout.

Since $QB=QC$ and $PA=PC$, angle chasing gives $\angle AQB=\angle APB$, so $A,B,Q,P$ are cyclic. Powers of $C$ with respect to this circle and circle $BPEF$ give
$$CA\cdot CQ=CB\cdot CP=CE\cdot CF.$$
Therefore $A,Q,E,F$ are cyclic. Also $GF\parallel BC$ implies $\angle AGF=\angle ABC=\angle AEF$, so $A,G,E,F$ are cyclic. Thus $A,Q,E,F,G$ lie on one circle.

Now $AD\parallel QM$ and $D,E,M$ are collinear. The original circumcircle gives the angle equality $\angle CEM=\angle CAD=\angle CQM$ gives $C,E,Q,M$ cyclic. Consequently
$$\angle GQE=\angle GFE=\angle MCE=\angle MQE.$$
This forces $G,Q,M$ to be collinear. Since $QM$ is the perpendicular bisector of $BC$, the three required lines meet at $G$.''','Several auxiliary circles must be established in sequence, including one through a power-of-a-point calculation, before the concurrence follows from a final angle comparison.')
json.dump(items,open(P+'amoc.json','w'),indent=2)
json.dump(ledger,open(P+'amoc-ledger.json','w'),indent=2)
print(len(items),len(ledger))
