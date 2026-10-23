"""Independently paraphrased statements recovered from the cited UWA papers.
Ratings are joined unchanged from the existing individual review ledger.
"""
import json
from pathlib import Path
P=Path(__file__).parent
rows=[]
def q(y,n,t,sub,s,solution=None,senior=False):
 rows.append(dict(id=f'aus_{"amoc" if senior else "amo"}_{y}_{n}',topic=t,subtopics=sub.split('|'),statement=s,solution=solution))
q(1995,1,'Number Theory','Primes|Digits & bases|Divisibility & GCD',r'Prove that at most nine primes between $10$ and $10^{29}$ have only the digit $1$ in decimal notation.')
q(1995,3,'Geometry','Circles & tangency|Coordinates & vectors',r'A line meets two concentric circles at $A,B,C,D$ in that order. Chords $AE$ of the outer circle and $BF$ of the inner circle are parallel. Let $G,H$ be the perpendicular projections of $C,D$ onto $BF,AE$, respectively. Prove $GF=HE$.')
q(1995,5,'Algebra','Equations & systems|Inequalities',r'For which real $r$ does the system $y-x=r$, $x^2+y^2+2x\le1$ have exactly one real solution $(x,y)$?')
q(1995,6,'Number Theory','Integer polynomials|Parity|Induction',r'Prove that infinitely many positive integers $n$ make exactly three coefficients of $(x^2+x+1)^n$ odd.')
q(1996,2,'Algebra','Polynomials|Algebraic identities',r'A cubic $p$ with roots $r_1,r_2,r_3$ satisfies $[p(1/2)+p(-1/2)]/p(0)=1000$. Evaluate $1/(r_1r_2)+1/(r_2r_3)+1/(r_3r_1)$.')
q(1996,3,'Number Theory','Digits & bases|Modular arithmetic|Sequences & recurrences',r'The centred hexagonal numbers count one central point surrounded by complete hexagonal layers: $1,7,19,37,61,91,\ldots$. Find the 69th term in this sequence whose last two digits are 69.')
q(1996,4,'Combinatorics','Permutations & arrangements|Parity|Graph theory',r'For which positive $n$ is there a permutation $(a_1,\ldots,a_n)$ of $1,\ldots,n$ such that all $|a_i-i|$ are equal and nonzero?')
q(1996,5,'Algebra','Inequalities|Extremal arguments',r'If $a_1\le\cdots\le a_n$, $\sum a_i=0$ and $\sum|a_i|=s$, prove $a_n-a_1\ge2s/n$.')
q(1996,6,'Geometry','Angles & cyclic quadrilaterals|Area & dissection|Trigonometry',r'In cyclic quadrilateral $ABCD$, points $P\in AB,Q\in AD$ satisfy $AP=CD$ and $AQ=BC$. Prove that $AC$ bisects $PQ$.')
q(1996,8,'Combinatorics','Pigeonhole principle|Sets & partitions',r'A function $f:\mathbb Z\to\{0,1\}$ has period 1996 and $\sum_{i=1}^{1996}f(i)=45$. Prove that some integer $t$ satisfies $f(n+t)=0$ whenever $f(n)=1$.')
q(1997,1,'Geometry','Geometric inequalities|Trigonometry|Triangle geometry',r'In isosceles $ABC$, $AB=AC$ and $\angle A<120^\circ$. Let $D$ be the midpoint of $BC$ and choose $E\in AD$ with $\angle AEB=120^\circ$. Prove that $EA+EB+EC$ is strictly smaller than $E\prime A+E\prime B+E\prime C$ for any other $E\prime\in AD$.')
q(1997,2,'Algebra','Inequalities',r'If $0\le a_1\le\cdots\le a_k$ and $\sum_{i=1}^k a_i=1$, prove $\frac1n\sum_{i=1}^n a_i\le1/k$ for $1\le n\le k$.')
q(1997,3,'Algebra','Functional equations|Functions & graphs|Inequalities',r'Find all $f:\mathbb R\to\mathbb R$ satisfying $|f(x+h)-f(x)|\le h^2$ for every real $x,h$.')
q(1997,6,'Algebra','Floors & fractional parts|Inequalities',r'For every positive integer $n$, prove $\lfloor\sqrt n+\sqrt{n+1}\rfloor=\lfloor\sqrt{4n+1}\rfloor$.')
q(1997,7,'Algebra','Inequalities',r'For integers $m,n>1$, prove $(n+1)^{-1/m}+(m+1)^{-1/n}>1$.')
q(1998,1,'Algebra','Equations & systems|Algebraic identities',r'Solve $(x+1998)(x+1999)(x+2000)(x+2001)+1=0$ over $\mathbb R$.')
q(1998,2,'Algebra','Equations & systems|Inequalities',r'Find $r,s\ge0$ satisfying $r+s=2$ and $2^{r^4+s^2}+2^{r^2+s^4}=8$.')
q(1998,3,'Geometry','Geometric inequalities|Similarity & congruence|Circles & tangency',r'A segment $DE$ joins sides $AB,AC$ of triangle $ABC$, is parallel to $BC$, and touches the incircle. Prove $8DE\le AB+BC+CA$.')
q(1998,4,'Algebra','Functional equations|Symmetry',r'Find all even functions $f:\mathbb R\setminus\{0\}\to\mathbb R$ with $f(1/(x+y))=f(1/x)+f(1/y)+2(xy-1000)$ whenever $x,y,x+y\ne0$.')
q(1998,5,'Combinatorics','Permutations & arrangements|Algorithms & constructions',r'Two $2\times2$ binary arrays are compatible if both occur as contiguous $2\times2$ subarrays of one $3\times3$ binary array, without rotation. Classify the incompatible pairs.')
q(1998,6,'Algebra','Inequalities',r'Prove $(1998n)!\le\left(\prod_{j=1}^{1998}\frac{(2j-1)n+1}{2}\right)^n$ for every positive integer $n$.')
q(1998,7,'Geometry','Area & dissection|Coordinates & vectors|Geometric inequalities',r'A line through the centroid splits a triangle of area $1998$ into regions of areas $A_1,A_2$. Maximise $A_1-A_2$.')
q(1999,1,'Geometry','Angles & cyclic quadrilaterals|Circles & tangency',r'Points $P,Q,R,S$ occur in that order on a circle, with $PQ\parallel SR$ and $QR=SR$. Ray $QT$ is tangent and $\angle RQT$ is acute. Prove $PS=QR$ and that $QR,QS$ trisect $\angle PQT$.')
q(1999,4,'Geometry','Geometric inequalities|Area & dissection',r'Prove that the sum of a triangle’s three altitudes is at least nine times its inradius.')
q(1999,5,'Algebra','Inequalities',r'For real $x>1$ and integer $n>1$, prove $1+\frac{x-1}{nx}<\sqrt[n]x<1+\frac{x-1}{n}$.')
q(2000,1,'Algebra','Polynomials',r'Find all real polynomials $f$ satisfying $(x-27)f(3x)=27(x-1)f(x)$.')
q(2000,2,'Number Theory','Valuations|Modular arithmetic',r'For a date with day $d$ and month $m$ in the year 2000, consider the largest power of 5 dividing $d^m-2000$. Which dates maximise that power?')
q(2000,5,'Number Theory','Squares & powers|Divisibility & GCD',r'Prove that $m^{n+2}+m^{n+1}+m^n$ is never a square when $m,n$ are positive integers.')
q(2000,6,'Algebra','Functional equations|Equations & systems',r'For fixed real $a,b,c$, not all zero, classify every $f:\mathbb R\to\mathbb R$ satisfying $af(xy+z^2)+bf(yz+x^2)+cf(zx+y^2)=0$ for all real $x,y,z$. Describe the cases according to $a,b,c$.')
q(2000,7,'Algebra','Floors & fractional parts|Equations & systems',r'Writing $\{t\}=t-\lfloor t\rfloor$, solve $x+\lfloor y\rfloor+\{z\}=200$, $\{x\}+y+\lfloor z\rfloor=190.1$, $\lfloor x\rfloor+\{y\}+z=178.8$.')
q(2001,1,'Number Theory','Divisibility & GCD|Primes|Modular arithmetic',r'Let $L(n)=\operatorname{lcm}(1,2,\ldots,n)$. Find prime pairs $p,q$ with $q=p+2$ and $L(q)>qL(p)$.')
q(2001,2,'Geometry','Coordinates & vectors|Angles & cyclic quadrilaterals',r'In isosceles $ABC$ with $CA=CB$, let $O$ be the circumcentre. Choose $P\in AB$, $Q\in BC$, $R\in CA$ so $PQ\parallel AC$, $PR\parallel BC$. Prove $C,R,O,Q$ are cyclic.')
q(2001,3,'Combinatorics','Double counting|Parity|Counting',r'Each of $c$ celebrities appears in an odd number of $m$ magazines, and each magazine mentions an odd number of celebrities. Prove $c,m$ have the same parity, and count the possible incidence patterns.')
q(2001,5,'Algebra','Functional equations',r'Find all $f:\mathbb R\to\mathbb R$ such that $f((x-y)^2)=x^2-2yf(x)+f(y)^2$ for real $x,y$.')
q(2001,6,'Geometry','Circles & tangency|Triangle geometry|Coordinates & vectors',r'In triangle $ABC$ with $AC>BC$, $D$ is the midpoint of the circumcircle’s arc $AB$ containing $C$. Its perpendicular projection onto $AC$ is $E$. Prove $AE=EC+CB$.')
q(2001,7,'Number Theory','Modular arithmetic|Squares & powers',r'Prove there are no positive integers $w,x,y,z$ satisfying $x^2=10w-1$, $y^2=13w-1$, $z^2=85w-1$.')
q(2003,1,'Number Theory','Primes|Diophantine equations|Divisibility & GCD',r'Find primes $p,q,r$ satisfying $p(q-r)=q+r$.')
q(2003,2,'Algebra','Functional equations|Equations & systems',r'Find $f:\mathbb R\setminus\{0,1\}\to\mathbb R$ satisfying $f(x)+\frac1{2x}f(1/(1-x))=1$.')
q(2003,5,'Combinatorics','Parity|Permutations & arrangements',r'Three cyclists initially lead in the order Andrew, Brenda, Chris. Only these three contest the first three places, and no three are ever level. The leader changes 19 times and the third-place rider changes 17 times. Brenda finishes third. Who wins? Justify your answer.')
q(2004,1,'Algebra','Polynomials|Sequences & recurrences',r'For which real $a,b$ does $x^3+3x^2+ax+b=0$ have three distinct roots in arithmetic progression?')
q(2004,2,'Algebra','Inequalities|Extremal arguments',r'Given $0\le x\le a\le y\le b\le z$ and $a+b+x+y+z=2004$, find the minimum and maximum of $x+y+z$.')
q(2004,4,'Geometry','Coordinates & vectors|Triangle centres|Triangle geometry',r'In equilateral $ABC$, take $D$ strictly between $A,B$ and $E\in AC$ with $DE\parallel BC$. If $F$ is the midpoint of $CD$ and $G$ the circumcentre of $ADE$, find all angles of $BFG$.')
q(2004,5,'Number Theory','Diophantine equations|Modular arithmetic|Valuations',r'For which nonnegative integers $m,n$ is $6^m+2^n+2$ a perfect square?')
q(2004,6,'Algebra','Functional equations|Sequences & recurrences',r'Does a function $f:\mathbb Z_{>0}\to\mathbb Z_{>0}$ exist with $f(f(1))=5$, $f(f(2))=6$, $f(f(3))=4$, $f(f(4))=3$, and $f(f(n))=n+2$ for all $n\ge5$?')


q(2003,7,'Algebra','Sequences & recurrences|Inequalities|Telescoping sums',r'Let $a_1=0$, with each later term chosen by $a_{i+1}=a_i+1$ or $a_{i+1}=-a_i-1$. Prove $\frac{a_1+\cdots+a_n}{n}\ge-\frac12$ for every positive integer $n$.')
q(2006,1,'Number Theory','Diophantine equations|Squares & powers|Modular arithmetic',r'Find positive integers $m,n$ such that $1+5\cdot2^m=n^2$.')
q(2006,5,'Geometry','Triangle centres|Circles & tangency|Coordinates & vectors',r'In square $ABCD$, choose $E$ strictly between $B,D$. The circumcentres of $ABE$ and $ADE$ are $O_1,O_2$. Prove $AO_1EO_2$ is a square.')
q(2006,6,'Number Theory','Digits & bases|Diophantine equations',r'Let $a(n)$ be the product of the decimal digits of a positive integer $n$. Prove $a(n)\le n$, and find all $n$ satisfying $n^2-17n+56=a(n)$.')
q(2007,1,'Geometry','Circles & tangency|Triangle geometry|Coordinates & vectors',r'In triangle $ABC$, $AB$ is the shortest side, and $X,Y$ are the midpoints of $BC,AC$. Let $P\in AC$ satisfy $PX\perp BC$. The circle through $A,B,P$ meets $BC$ again at $Q$. Prove $QY\perp AC$.')
q(2007,2,'Number Theory','Diophantine equations|Primes|Factorisation',r'For an odd prime $p$, find all positive integers $m,n$ satisfying $(p-1)(p^n+1)=4m(m+1)$.')
q(2007,4,'Algebra','Inequalities|Extremal arguments',r'For each positive integer $n$, find the least constant $C_n$ for which $r+r^2+\cdots+r^{2n}\le C_n(1+r^{2n+1})$ holds for every positive real $r$. Prove this constant is finite.')
q(2007,6,'Algebra','Inequalities|Absolute values',r'Nonzero real numbers $a,b$ satisfy $a^2+b^2=1$. Prove $|a+a/b+b+b/a|\ge2-\sqrt2$.')
q(2008,1,'Geometry','Circles & tangency|Angle chasing',r'A circle has diameter $PQ$. A second circle has its centre on the first and is tangent to $PQ$. Prove that its other tangents from $P$ and $Q$ are parallel.')
q(2008,2,'Algebra','Equations & systems|Monotonicity',r'Let $f(x)=5^x$. Solve $f(x+f(2008))=2008-x$ over the reals.')
q(2008,5,'Number Theory','Valuations|Factorials & binomial coefficients',r'For a positive integer $m$, let $F(m)$ be the largest integer $e$ such that $10^e\mid m!$. Prove that some positive integer $n$ satisfies, for every positive $m$, either $F(m)\le n$ or $F(m)\ge n+2008$.')
q(2008,6,'Geometry','Circles & tangency|Coordinates & vectors',r'In convex quadrilateral $ABCD$, $P\in AB$ satisfies $\angle APD=\angle BPC=45^\circ$. Let $Q$ be the intersection of line $AB$ and the perpendicular bisector of $CD$. Prove $\angle CQD=90^\circ$.')
q(2008,7,'Geometry','Triangle inequality|Inequalities',r'Two triangles have vertices $A_1,A_2,A_3$ and $B_1,B_2,B_3$. If $p$ is the sum of their perimeters and $q=\sum_{i=1}^3\sum_{j=1}^3 A_iB_j$, prove $3p\le4q$.')
q(2009,1,'Geometry','Circles & tangency|Perpendicularity|Coordinates & vectors',r'In acute triangle $ABC$, choose $P\in AC$ and $Q\in BC$ such that $A,P,Q,B$ are concyclic. The perpendiculars to $AC$ at $P$ and to $BC$ at $Q$ meet at $R$. Prove $CR\perp AB$.')
q(2009,2,'Number Theory','Diophantine equations|Extremal arguments|Factorisation',r'Two rectangles have integer side lengths greater than one and are tiled by unit squares. In each rectangle, the number of boundary tiles equals the number of interior tiles in the other. Maximise the shortest of the four side lengths.')
q(2009,3,'Algebra','Polynomials|Modular arithmetic|Invariants',r'Initially a board contains $x^2+x$ and $x^2+2$. A move writes the sum, difference, or product of any two polynomials already present. Can the polynomial $x$ ever appear?')
q(2009,5,'Combinatorics','Graphs|Extremal arguments|Combinatorial geometry',r'A finite set of towns lies in the plane, with all pairwise distances distinct. Join each town by a straight road to its nearest neighbour. Prove that roads do not cross and the resulting graph has no cycle.')
q(2010,1,'Algebra','Sequences & recurrences|Equations & systems',r'A real sequence satisfies $a_1+a_2=2010$ and $a_{n-1}a_{n+1}=a_n$ for every $n\ge2$. Find all possible values of $a_{2011}+a_{2012}$.')
q(2010,5,'Geometry','Circles & tangency|Power of a point|Coordinates & vectors',r'Two concentric circles have radii $r<s$. Let $PA$ be a chord of the inner circle, and let the chord $BC$ of the outer circle pass through $P$ perpendicular to $PA$. Express $PA^2+PB^2+PC^2$ in terms of $r,s$.')
q(2010,6,'Algebra','Algebraic identities|Radicals',r'Prove the identity $$\sqrt[3]{6+\sqrt[3]{845}+\sqrt[3]{325}}+\sqrt[3]{6+\sqrt[3]{847}+\sqrt[3]{539}}=\sqrt[3]{4+\sqrt[3]{245}+\sqrt[3]{175}}+\sqrt[3]{8+\sqrt[3]{1859}+\sqrt[3]{1573}}.$$')
q(2011,1,'Number Theory','Digits & bases|Divisibility & GCD',r'Fix an integer $b\ge2$, and let $S_b(n)$ be the sum of the base-$b$ digits of $n$. Find all positive integers $m$ such that $m\mid S_b(n)$ implies $m\mid S_b(n+1)-1$ for every positive integer $n$.')
q(2011,2,'Geometry','Trigonometry|Regular polygons|Products',r'A regular $2n$-gon $P_1P_2\ldots P_{2n}$ lies on a unit circle. Put $a_i=P_1P_{i+1}$ for $1\le i<n$. Prove $\prod_{i=1}^{n-1}(4/a_i^2-1)=1$.')
q(2011,6,'Algebra','Polynomials|Vieta’s formulas|Equations & systems',r'The three roots of $x^3-30x^2+rx-780$ are the side lengths of a right triangle. Find $r$.')
q(2012,1,'Number Theory','Squares & powers|Diophantine equations',r'Find the largest positive integer $n$ such that $4^n+2^{2012}+1$ is a perfect square.')
q(2012,5,'Algebra','Equations & systems|Factorisation',r'Prove that $(x+20)(y+12)(z-4)=(x+20)(y-12)(z+4)=(x-20)(y+12)(z+4)=1215$ has a unique real solution. Find the least integer $N>1215$ for which replacing all three right-hand sides by $N$ allows an integer solution.')
q(2013,1,'Geometry','Area|Similar triangles',r'In parallelogram $ABCD$, choose $P\in CD$. The line through $P$ parallel to $AD$ meets $AC$ at $Q$. Writing $[XYZ]$ for triangle area, prove $[BCP]^2=[QBP][ABP]$.')
q(2013,3,'Number Theory','Modular arithmetic|Induction|Squares & powers',r'If $n$ is a positive integer with $n\equiv3\pmod8$, prove for every integer $k>3$ that $2^k\mid n^{2^{k-3}}-2^{k-1}-1$.')
q(2013,5,'Number Theory','Squares & powers|Extremal arguments|Constructions',r'What is the largest possible number of distinct positive integers whose squares sum to $2013$?')
q(2013,6,'Combinatorics','Graphs|Parity|Pigeonhole principle',r'Among 2013 people, every group of three contains an odd number of acquainted pairs. Prove there are 1007 people who all know one another.')
q(2016,1,'Number Theory','Modular arithmetic|Squares & powers|Diophantine equations',r'Find all positive integers $n$ such that $2^n+7^n$ is a perfect square.')
q(2016,2,'Geometry','Power of a point|Circles & tangency',r'A circle meets the sides $BC,CA,AB$ of triangle $ABC$ at $U,V$; $W,X$; and $Y,Z$, respectively, in cyclic order $U,V,W,X,Y,Z$. If $AY=BZ$ and $BU=CV$, prove $CW=AX$.')
q(2016,5,'Algebra','Equations & systems|Factorisation',r'Find all real triples $(x,y,z)$ satisfying $xy+1=2z$, $yz+1=2x$, and $zx+1=2y$.')
q(2016,6,'Number Theory','Factorisation|Parity|Divisibility & GCD',r'Positive integers $a,b,c$ satisfy $a^3+b^3=2^c$. Prove $a=b$.')
q(2017,1,'Combinatorics','Permutations & arrangements|Constructions|Induction',r'For which integers $n\ge2$ can $1,2,\ldots,n$ be arranged in a row so that consecutive entries differ by either $2$ or $3$?')
q(2017,3,'Algebra','Functional equations|Substitution',r'Find all functions $f:\mathbb R\to\mathbb R$ satisfying $f(x^2+f(y))=f(xy)$ for all real $x,y$.')
q(2017,5,'Number Theory','Floor & ceiling functions|Divisibility & GCD|Counting',r'How many positive integers $n<10^6$ make $\sum_{k=1}^{n}\frac1{2\lfloor\sqrt{k}\rfloor+1}$ an integer?')
q(2018,1,'Number Theory','Factorials & binomial coefficients|Modular arithmetic|Squares & powers',r'Find all positive integer pairs $(n,k)$ satisfying $n!+8=2^k$.')
q(2018,3,'Geometry','Regular polygons|Concurrency|Trigonometry',r'For the regular 14-gon $ABCDEFGHIJKLMN$, prove that $AE,BG,CK$ pass through one point.')
q(2018,5,'Number Theory','Sequences & recurrences|Divisibility & GCD|Factorials & binomial coefficients',r'Define $a_1=1$ and $a_n=n(a_1+\cdots+a_{n-1})$ for $n\ge2$. Prove $2018^2\mid a_{2018}$.')
q(2018,6,'Geometry','Circles & tangency|Angle chasing|Collinearity',r'Points $P,Q,R$ lie on circle $C$ with $PQ=PR>QR$. Circle $D$ has centre $P$ and passes through $Q,R$. The circle centred at $Q$ through $R$ meets $C$ again at $X$ and $D$ again at $Y$. Prove $P,X,Y$ are collinear.')
q(2019,1,'Algebra','Polynomials|Inequalities|Extremal arguments',r'Find all real $r$ for which exactly one real $a$ makes every coefficient of $(x+a)(x^2+rx+1)$ nonnegative.')
q(2019,2,'Number Theory','Diophantine equations|Algebraic identities|Figurate numbers',r'Let $a<b<c$ be three consecutive positive triangular numbers. If $a+b+c$ is triangular, prove that $b$ is three times a triangular number.')
q(2020,1,'Number Theory','Diophantine equations|Squares & powers|Factorisation',r'Find all nonnegative integer pairs $(a,b)$ satisfying $\frac{a+b}{2}-\sqrt{ab}=1$.')
q(2021,1,'Number Theory','Diophantine equations|Counting|Factorisation',r'A cuboid of positive integer dimensions $a,b,c$ is built from unit cubes, and its exterior is painted red. Once separated, the cubes have as many red faces as unpainted faces in total. Find all possible values of $abc$.')
q(2021,5,'Algebra','Inequalities|Equations & systems',r'Find all real pairs $(a,b)$ satisfying $a^{20}+b^{20}=a^{21}+b^{21}=1$.')
q(2024,8,'Number Theory','Digits & bases|Irrationality|Valuations',r'Let $r=0.d_0d_1d_2\ldots$ in decimal, with $d_0=6$. For each $n\ge0$, put $e_n=\sum_{i=0}^n10^id_i$, allowing leading zeroes. Suppose $e_n^2\equiv e_n\pmod{10^{n+1}}$ for every $n$. Prove $r$ is irrational.')


q(2021,4,'Number Theory','Integer polynomials|Valuations|Divisibility & GCD',r'Let $P,Q$ be integer-coefficient polynomials, with $P$ monic. If $P(n)^n\mid Q(n)^{n+1}$ for infinitely many positive integers $n$, prove $P(n)\mid Q(n)$ for infinitely many positive integers $n$.')
q(2023,2,'Combinatorics','Subsets|Modular arithmetic|Bijections',r'How many subsets of $\{1,2,\ldots,2023\}$ have an element sum congruent to $3$ modulo $4$?')
q(2024,1,'Number Theory','Factorials & binomial coefficients|Parity|Diophantine equations',r'Find all positive integer triples $(k,m,n)$ satisfying $k!+m!=k!n!$.')


q(2022,5,'Algebra','Inequalities|Sequences & recurrences',r'Real numbers $x_1,\ldots,x_{2022}$ have positive sum. For some $1\le k<2022$, $x_i\le0$ when $i\le k$ and $x_i\ge0$ when $i>k$. Prove $\sum_{i=1}^{2022}ix_i>0$.')
q(2021,1,'Geometry','Similar triangles|Angle bisectors|Parallel lines',r'Quadrilateral $ABCD$ has $\angle DAB=\angle CDA=90^\circ$, and its diagonals meet at $M$. A point $K\in AD$ satisfies $\angle ABK=\angle DCK$. Prove $KM$ bisects $\angle BKC$.',senior=True)
q(2022,1,'Number Theory','Modular arithmetic|Factorials & binomial coefficients|Diophantine equations',r'Find all positive integer triples $(a,b,n)$ with $2^a+b^2=n!+14$.',senior=True)
q(2022,2,'Algebra','Inequalities|AM–GM inequality',r'For nonnegative reals $x_1,\ldots,x_n$, where $n\ge2$, prove $$\sum_{i=1}^{n-1}x_ix_{i+1}\le\frac{(x_1+\cdots+x_n)^2}{4}.$$ ',senior=True)
q(2024,1,'Combinatorics','Colouring|Symmetry|Modular arithmetic',r'A row contains $1\,000\,001$ coloured beads. Beads 100 positions apart have the same colour, and the colour sequence reads identically from either end. What is the maximum number of colours?',senior=True)


q(2018,1,'Algebra','Radicals|Inequalities|Factorisation',r'For distinct nonnegative reals $a,b$ satisfying $a+\sqrt b=b+\sqrt a$, determine the largest value of $a+b$.',senior=True)
q(2018,3,'Combinatorics','Pigeonhole principle|Counting',r'Fourteen players play three matches, each time forming two teams of seven, with one winning team and one losing team. Nobody loses all three matches. Prove some three players are teammates in every match.',senior=True)
q(2019,1,'Geometry','Angle chasing|Telescoping sums|Parity',r'Points $A_1,\ldots,A_n$ have strictly increasing $x$-coordinates, where $n\ge3$. The consecutive segments have slopes alternating positive, negative, positive, and so on. Let $P$ and $V$ be the sums of the angles below $180^\circ$ at the internal peaks and valleys, respectively. Prove $P\le V$ implies $n$ is even.',senior=True)
q(2019,2,'Number Theory','Divisibility & GCD|Fractions & approximation',r'Find all integers expressible as $\frac1{a_1}+\cdots+\frac1{a_{10}}$, where the $a_i$ are nonzero integers and any two have no common positive divisor greater than one.',senior=True)
q(2020,1,'Algebra','Polynomials|Discriminants|Inequalities',r'For all real $a,b$, prove that at least one of $x^2+2ax+b=0$, $ax^2+2bx+1=0$, and $ax^2+2x+b=0$ has a real solution.',senior=True)

# The following solution papers were verified through the organiser/UWA archive.
for item in rows:
 parts=item['id'].split('_');year=int(parts[2]);number=int(parts[3])
 if parts[1]=='amoc':item['solutionUrl']=f'https://enrichedmaths.maths.uwa.edu.au/Olympiad/SMC/SMC{year}wsoln.pdf'
 elif year>=2016:item['solutionUrl']=f'https://enrichedmaths.maths.uwa.edu.au/Olympiad/AMO/AMO{year}wsoln.pdf'
 elif year==1997 and number in (1,2,3,4,6,7):item['solutionUrl']=f'https://enrichedmaths.maths.uwa.edu.au/Olympiad/AMO/AMO{year}wsoln.pdf'
 elif year==2003 and number in (1,2,4,8):item['solutionUrl']=f'https://enrichedmaths.maths.uwa.edu.au/Olympiad/AMO/AMO{year}wsoln.pdf'
 elif year==2004 and number in (4,5,6,8):item['solutionUrl']=f'https://enrichedmaths.maths.uwa.edu.au/Olympiad/AMO/AMO{year}wsoln.pdf'
 elif (year,number) in ((2004,1),(2004,2),(2006,5),(2010,1),(2010,6)):
  item['solutionUrl']='https://enrichedmaths.maths.uwa.edu.au/Olympiad/'
  item['notes']='The UWA archive index links a worked video or PDF solution for this question; open its AMO year entry.'
 elif (year==2006 and number==1) or (year==2007 and number in (1,2,4,6)) or (year==2008 and number in (1,2,5,6,7)) or (year==2009 and number in (1,2,3,5)) or (year==2011 and number in (1,2)):
  item['solutionUrl']=f'https://enrichedmaths.maths.uwa.edu.au/Olympiad/AMO/AMO{year}wsoln.pdf'
  if year in (2007,2008):item['notes']='The linked UWA paper supplies worked solutions and hints; see the section for this question.'

if __name__=='__main__':
 target=P/'restored-australia-statements.json'
 target.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
 print('Recovered Australian statements:',len(rows))
