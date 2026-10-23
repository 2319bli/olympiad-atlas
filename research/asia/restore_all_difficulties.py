"""Recover statements and subject metadata for already-rated, previously excluded tasks.

Ratings are retained unchanged from reviews.json. Statements below are independent
mathematical paraphrases of the cached official papers/solutions.
"""
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'research/asia'; reviews=json.loads((P/'reviews.json').read_text())
def fix(k,statement,subtopics,topic=None):
 r=reviews[k];r['statementOverride']=statement;r['subtopics']=subtopics
 if topic:r['topic']=topic
 note='Full statement restored from the reviewed source when the collection was expanded to all difficulties.'
 if note not in r.get('note',''):r['note']=(r.get('note','')+' '+note).strip()
def my(y,n,s,t,topic=None):fix(f'mys_{y}_imonst2_{n:02}',s,t,topic)
my(2020,1,r'Pentagon $ABCDE$ satisfies $\angle CAD=30^\circ$, $\angle DAE=40^\circ$, $\angle ADE=50^\circ$, $\angle ADB=25^\circ$ and $\angle BDC=35^\circ$. Determine $\angle ACE+\angle CED$.',['Angles & cyclic quadrilaterals'])
my(2020,2,r'For every positive integer $n$, establish the identity $1+3+5+\cdots+(2n-1)=n^2$.',['Sequences & recurrences','Induction'])
my(2020,3,r'Determine the four-digit positive integers $N$ whose digit sum is $2020-N$.',['Digits & bases'])
my(2020,4,r'A right triangle has legs $a,b$ and hypotenuse $c$. Show that its inradius is $(a+b-c)/2$.',['Triangle geometry','Circles & tangency','Area & dissection'])
my(2020,5,r'For every integer $n\ge6$, construct a dissection of an equilateral triangle into exactly $n$ smaller equilateral triangles. The smaller triangles need not be congruent.',['Tilings & dissections','Induction'])
my(2020,6,r'If integers $a,b$ satisfy $11\mid a^2+b^2$, prove that $11\mid a$ and $11\mid b$.',['Modular arithmetic','Squares & powers'])
my(2020,7,r'A trapezium has parallel sides of positive integer lengths $m,n$. Prove that it admits a dissection into finitely many congruent triangles.',['Area & dissection','Similarity & congruence'])
my(2020,8,r'Prove the identity $$\sum_{k=1}^{2020}\frac{(-1)^{k+1}}k=\sum_{k=1011}^{2020}\frac1k.$$',['Sequences & recurrences','Algebraic identities'])
my(2020,9,r'Determine all integers $n$ for which $12n^2+12n+11$ is a four-digit number with four equal digits.',['Digits & bases','Modular arithmetic','Diophantine equations'])
my(2020,11,r'Let $x_1,x_2$ be the two distinct real roots of $x^2+px+q=0$, where $p,q\in\mathbb R$. If $|x_1-x_2|=|p-q|=1$, show that $p,q,x_1,x_2$ are all integers.',['Equations & systems','Polynomials'])
my(2021,1,r'Nine lines parallel to the base divide an equilateral triangle into ten bands of equal width. Colour the bands alternately red and blue, starting with red at the apex. The areas of the two colours differ by $20\text{ cm}^2$. Find the area of the triangle.',['Area & dissection','Similarity & congruence'])
my(2021,2,r'Real numbers $a,b,c,d,e$ satisfy $$a+b<c+d<e+a<b+c<d+e.$$ Identify the smallest and the largest of the five numbers.',['Inequalities'])
my(2021,4,r'Points $A,B$ lie on a circle with centre $O$, with $OAB$ equilateral. A point $C$ outside the circle satisfies $\angle ACB=45^\circ$. Lines $CA,CB$ meet the circle again at $D,E$, respectively, with $A$ between $C,D$ and $B$ between $C,E$. Determine $\angle DBE$.',['Angles & cyclic quadrilaterals','Triangle geometry'])
my(2021,5,r'Can positive integers $a,b$ make both $a^2+b$ and $b^2+a$ perfect squares? Prove your answer.',['Squares & powers','Diophantine equations'])
my(2021,6,r'A sequence of positive integers satisfies $a_2>a_1$ and $a_{n+2}=3a_{n+1}-2a_n$ for every $n\ge1$. Prove that $a_{2021}>2^{2019}$.',['Sequences & recurrences'])
my(2021,7,r'Determine the possible perimeters $n$ of rectangles with positive integer side lengths and area $2n$.',['Diophantine equations','Divisibility & GCD'])
my(2021,9,r'For rational numbers $x,y$ satisfying $x^5+y^5=2x^2y^2$, prove that $\sqrt{1-xy}$ is rational.',['Rationality & irrationality','Algebraic identities'])
my(2022,1,r'How many diagonals does a polygon with ten vertices have?',['Counting','Combinatorial geometry'])
my(2022,2,r'List, in increasing order, all positive integers in which the digit $2$ occurs in more than half of the digit positions. The list begins $2,22,122,202,212,220,221,222,223,224,\ldots$. At what position does $2022$ occur?',['Counting','Digits & bases'])
my(2022,3,r'Prove that, for every positive integer $n$, $$\sum_{k=1}^n k(k+3)=\frac{n(n+1)(n+5)}3.$$',['Sequences & recurrences','Induction'])
my(2022,4,r'Let $ABCD$ be a cyclic quadrilateral, and let $R$ bisect arc $AB$. Set $S=RC\cap AB$ and $T=RD\cap AB$. Prove that $C,D,T,S$ are concyclic.',['Angles & cyclic quadrilaterals'])
my(2022,5,r'Compare $17^{24}$ and $31^{19}$ without a calculator.',['Inequalities','Squares & powers'])
my(2022,6,r'An integer $m$ is obtained by rearranging the decimal digits of an integer $n$. Prove that $m+n$ cannot equal $999999999$.',['Digits & bases','Parity'])
my(2023,1,r'Show that $1^3+2^3+\cdots+n^3$ is a perfect square for every positive integer $n$.',['Sequences & recurrences','Induction'])
my(2023,2,r'Fifty cats are divided into five colour classes, with each cat in exactly one class. The product of the five class sizes is $100000$. Determine all five sizes.',['Inequalities'])
my(2023,3,r'Find all positive integer pairs $(x,y)$ for which $x^3+y^3$ is prime.',['Primes','Divisibility & GCD'])
my(2023,4,r'Determine the greatest area of a right triangle whose hypotenuse has length $2024$.',['Geometric inequalities','Area & dissection'])
my(2023,5,r'Start with the entries $1,2,\ldots,10$ on a board. A move replaces two entries $a,b$ by the single entry $a+b-1$. Repeat until one entry remains. What values can that final entry have?',['Invariants'])
my(2023,6,r'In cyclic quadrilateral $ABCD$, both $\angle ABC$ and $\angle ADC$ are right angles. Let $E,F$ be the perpendicular projections of $A,C$, respectively, onto line $BD$. Prove that $BE=DF$.',['Coordinates & vectors','Circles & tangency'])
my(2023,8,r'Positive integers $x,y,n$ satisfy $x^{2024}+y^{2024}=2^n$. Prove that $x=y$.',['Valuations','Modular arithmetic'])
my(2023,9,r'For a fixed positive integer $n$, find the smallest positive integer $m$ for which an $m\times n$ chessboard can hold $n$ pairwise nonattacking queens. A queen attacks along its row, column and diagonals.',['Algorithms & constructions','Permutations & arrangements'])
my(2023,12,r'Can a parallelogram with integer side lengths and angles $60^\circ,120^\circ,60^\circ,120^\circ$ have a diagonal of length $\sqrt{2024}$? Prove your answer.',['Modular arithmetic','Diophantine equations'])
my(2024,1,r'Count the strings of length $12$ over the alphabet $\{I,M,O,N,S,T\}$ that contain the consecutive substring $IMONST$.',['Counting','Permutations & arrangements'])
my(2024,2,r'From a point $P$ outside a circle with centre $O$, draw tangents $PX,PY$, touching at $X,Y$. Choose $Q$ on segment $PX$ and $R$ beyond $Y$ on ray $PY$ so that $QX=RY$. Prove that $O,P,Q,R$ are concyclic.',['Similarity & congruence','Angles & cyclic quadrilaterals'])
my(2024,3,r'Construct positive integers $a_1,\ldots,a_{2024}$, all at least $10$, such that $a_i$ has exactly $a_{i+1}$ positive divisors for every $1\le i\le2023$, or prove that no such sequence exists.',['Arithmetic functions','Algorithms & constructions'])
my(2024,4,r'Let $m,n$ be coprime positive integers. (a) Find positive integers $p,q$ with $$\gcd(pm+q,n)\gcd(m,pn+q)=mn.$$ (b) Show that no positive integers $r,s$ can satisfy $$\operatorname{lcm}(rm+s,n)\operatorname{lcm}(m,rn+s)=mn.$$',['Divisibility & GCD'])
my(2024,7,r'Positive real numbers satisfy $a\ge b\ge c\ge d$ and $ab^2c^3d^4=1$. Prove that $a+b+c+d\ge4$.',['Inequalities'])
my(2024,10,r'For each $n\ge1$, let $a_n$ be the number of the form $k/2^n$, with $k\in\mathbb Z$, nearest to $1/3$. Prove that $2a_{i+2}=a_{i+1}+a_i$ for every $i\ge1$.',['Sequences & recurrences','Modular arithmetic'])
my(2025,1,r'Partition the integers $0,1,\ldots,101$ into $51$ pairs. Prove that an odd number of these pairs contain one odd integer and one even integer.',['Parity','Counting'])
my(2025,2,r'Do there exist ten distinct positive integers whose sum is divisible by each of them? Give a construction or prove impossibility.',['Divisibility & GCD','Algorithms & constructions'])
my(2025,3,r'A staircase region consists of left-aligned rows of $1,2,\ldots,10$ unit squares. Tile it using one rectangle of each size $1\times1,1\times2,\ldots,1\times10$, allowing rotations. How many tilings are possible?',['Tilings & dissections','Recurrences & generating functions'])
my(2025,4,r'In rectangle $ABCD$, $AB=111\text{ cm}$. Let $M$ be the midpoint of $AD$ and let $P\in AB$ satisfy $\angle APM=\angle BPC$. Find $AP$.',['Similarity & congruence'])
my(2025,5,r'Begin with positive real numbers $a_0>b_0$. Repeatedly replace the pair by $$a_k=\frac{a_{k-1}+b_{k-1}}2,\qquad b_k=\frac{a_{k-1}-b_{k-1}}2.$$ After some positive number of steps, the two entries are $20$ and $25$ in some order. If one initial entry was $720$, determine the other.',['Sequences & recurrences','Parity'])
my(2025,6,r'Find the greatest positive integer $n$ such that $n!$ can be expressed as a sum of factorials of smaller positive integers, with each factorial used at most twice.',['Factorials & binomial coefficients','Induction'])
my(2025,7,r'The multiset $\{(a_i+1/4)^2:1\le i\le10\}$ equals the multiset $\{a_i:1\le i\le10\}$, where all $a_i$ are real. Prove that every $a_i=1/4$.',['Algebraic identities','Inequalities'])
my(2025,8,r'In cyclic quadrilateral $ABCD$, let $E=AB\cap CD$ and $F=AD\cap BC$. The internal bisector of $\angle AED$ meets lines $AD,BC$ at $X,Y$, respectively. Prove that $FX=FY$.',['Angles & cyclic quadrilaterals','Triangle geometry'])
my(2025,12,r'Find all real triples $(a,b,c)$ with $a,b,c\ge3$ and $ab+bc+ca+9=3a+4b+5c$.',['Equations & systems','Inequalities'])
my(2025,13,r'Determine all arithmetic progressions $(a_n)_{n\ge1}$ of positive integers for which $\gcd(a_n,a_{2n})=n$ for every positive integer $n$.',['Divisibility & GCD','Sequences & recurrences'])
my(2025,15,r'Box $i$ contains one red ball and $i$ blue balls, for $1\le i\le100$. Select one ball uniformly and independently from each box. What is the probability of selecting an odd number of red balls?',['Probability','Parity'])
my(2025,22,r'A tile is a finite edge-connected union of unit squares. Do there exist five pairwise distinct, nonrectangular tiles, all of the same area, such that an $m\times n$ rectangle can be tiled using copies of these tiles exactly when both $m$ and $n$ are divisible by $2025$? Rotations are permitted, reflections are forbidden, and a tiling need not use every tile type.',['Tilings & dissections','Algorithms & constructions'])
fix('kaz_2024_national_g10_q3',r'Determine every function $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfying $$f\left(x+\frac{f(xy)}x\right)=f(xy)f\left(y+\frac1y\right)$$ for all positive real $x,y$.',['Functional equations','Inequalities'])
fix('kaz_2024_national_g10_q4',r'Player $A$ hides an object at an integer lattice point in the plane. In one query, player $B$ chooses three distinct lattice points and is told whether a circle passes through those points and the hidden point. Can $B$ always locate the object after finitely many queries?',['Algorithms & constructions','Logic & information','Combinatorial geometry'])
fix('kaz_2024_national_g10_q6',r'The incircle $\omega$ of a scalene triangle $ABC$, with centre $I$, touches $BC,CA,AB$ at $D,E,F$. The circumcircles of $ABC$ and $AEF$ meet again at $K$. Define $X=EF\cap AK$, $Y=EF\cap BC$ and $Z=AK\cap BC$. The tangents from $Y,Z$ to $\omega$ other than $BC$ touch at $P,Q$, respectively. Let $R=AP\cap KQ$ and let $M$ be the midpoint of $YZ$. Prove that $IR\perp XM$.',['Projective geometry & conics','Circles & tangency','Concurrency & collinearity'])
def idn(y,section,n,s,t):fix(f'idn_{y}_{section}_q{n}',s,t)
idn(2021,'national',1,r'Insert a plus or minus sign between each consecutive pair in $1,2,3,4,5,6,7,8,9$, without changing their order or joining digits. What is the least positive odd integer that cannot be the value of the resulting expression?',['Sets & partitions','Counting'])
idn(2021,'national',5,r'A monic quadratic $P(x)=x^2+rx+s$ has two distinct real roots, both less than $-1$, whose difference in absolute value is less than $2$. Prove that $P(P(x))>0$ for every real $x$.',['Polynomials','Inequalities'])
idn(2022,'national',2,r'An integer-coefficient polynomial $P$ satisfies $P(1)=10$ and $P(-1)=22$. (a) Give an example for which $P$ has an integer root. (b) Prove that, if also $P(0)=4$, then $P$ has no integer root.',['Integer polynomials','Divisibility & GCD'])
idn(2022,'national',5,r'Let $N\ge2$ and let $a_1,\ldots,a_{N+1}$ be integers such that no product $a_i a_{i+1}\cdots a_j$, with $1\le i\le j\le N+1$, is congruent to $1$ modulo $N$. Prove that at least one $a_i$ is not coprime to $N$.',['Pigeonhole principle','Modular arithmetic','Divisibility & GCD'])
idn(2024,'province_short',1,r'The two-digit decimal numbers $\overline{ab}<\overline{cd}$ have product $777$. Find $a+b$.',['Divisibility & GCD','Digits & bases'])
idn(2024,'province_short',2,r'Affine functions $f,g:\mathbb R\to\mathbb R$ satisfy $f(x+g(y))=7x+2y+11$ for all real $x,y$. If $g(7)=3$, find $g(-11+f(4))$.',['Functional equations','Equations & systems'])
idn(2024,'province_short',5,r'How many positive integers $a<209$ satisfy $\gcd(a,209)=1$ and $209\nmid a^2-1$?',['Arithmetic functions','Modular arithmetic'])
idn(2024,'province_short',7,r'Let $N$ count the ordered pairs of subsets $(A,B)$ of $\{1,2,\ldots,18\}$ for which $|A\cap B|\le2$. Find $N/3^{16}$.',['Counting','Sets & partitions'])
idn(2024,'province_proof',1,r'Let $C\le2$ be real. Prove that all positive real $x,y$ with $xy=1$ satisfy $$\sqrt{\frac{x^2+y^2}{2}}+\frac C{x+y}\ge1+\frac C2.$$',['Inequalities'])
def bd(cat,n,s,t):fix(f'bgd_2024_national_{cat}_q{n}',s,t)
bd('primary',1,r'Find the smallest two-digit positive integer whose units digit is seven less than its tens digit.',['Digits & bases'])
bd('primary',3,r'A nine-digit integer divisible by $41$ has its third and seventh digits erased. The remaining visible blocks are $30$, $032$ and $99$ in that order, so the original form is $\overline{30a032b99}$ with decimal digits $a,b$. Find every possible original integer.',['Digits & bases','Modular arithmetic'])
bd('primary',5,r'Call positive integers $u,v$ friends when $\gcd(u,v)+\operatorname{lcm}(u,v)=u+v$. What is the largest friend of $961$ that is smaller than $961$?',['Divisibility & GCD'])
bd('primary',6,r'Let $P=2^9\cdot3^8\cdot4^7\cdot5^6\cdot6^5$. (a) How many unordered pairs of positive integers $(a,b)$ satisfy $ab=P$? (b) How many positive divisors of $P$ are perfect squares?',['Arithmetic functions','Valuations','Squares & powers'])
bd('junior',1,r'A state consists of a nonnegative number of eggs $e$ and a positive number of people $p$, initially $(e,p)=(112,2)$. One operation replaces $e$ by $\lfloor e/p\rfloor$; the other increases $p$ by one. What is the fewest operations needed to make $e=0$?',['Extremal arguments','Algorithms & constructions'])
bd('junior',2,r'For every positive integer $x$, prove that $4x^4-8x^3+12x^2-8x+4$ is a perfect square.',['Algebraic identities'])
bd('junior',3,r'In triangle $AFG$, points $B\in AF$ and $C\in AG$ satisfy $FB=BC=CG$. The internal bisectors of $\angle ABC$ and $\angle ACB$ meet $AG$ and $AF$ at $E$ and $D$, respectively. Prove that $DE\parallel FG$.',['Triangle geometry','Similarity & congruence'])
bd('junior',4,r'Club $A$ has nine members owning the first nine prime numbers of books, one count per member. Club $B$ has one member for each integer book count from $123$ through $231$. A single person transfers from one club to the other, increasing both clubs’ average book counts. How many possible transfers have this property?',['Inequalities','Equations & systems'])
bd('secondary',1,r'Find all nonnegative integer solutions of $x^3y+x+y=xy+2xy^2$.',['Diophantine equations','Divisibility & GCD'])
bd('secondary',3,r'Real numbers $a,b$ satisfy $a+b\ne0$ and $$\frac a{a^2-5}=\frac b{5-b^2}=\frac{ab}{a^2b^2-5},$$ with all denominators nonzero. Find $a^4+b^4$.',['Equations & systems','Algebraic identities'])
bd('secondary',4,r'For any integers $a_1,a_2,a_3$, show that one can choose $b_1,b_2,b_3\in\{-1,0,1\}$, not all zero, such that $7\mid a_1b_1+a_2b_2+a_3b_3$.',['Pigeonhole principle','Sets & partitions','Modular arithmetic'])
bd('higher_secondary',4,r'Given integers $a_1,\ldots,a_{11}$, prove that there exist $b_1,\ldots,b_{11}\in\{-1,0,1\}$, not all zero, with $2024\mid\sum_{i=1}^{11}a_i b_i$.',['Pigeonhole principle','Sets & partitions','Modular arithmetic'])
bd('higher_secondary',6,r'Find all polynomials $P$ for which some real sequence $(a_n)_{n\ge1}$ satisfies $a_m+a_n=P(mn)$ for every pair of positive integers $m,n$.',['Polynomials','Sequences & recurrences'])
fix('isr_2023_gillis_q1',r'Solve over the real numbers: $$\begin{cases}5x+5y+5xy-2xy^2-2x^2y=20,\\3x+3y+3xy+xy^2+x^2y=23.\end{cases}$$',['Equations & systems','Algebraic identities'])
fix('isr_2023_gillis_q2',r'For a real number $t$, write $\{t\}=t-\lfloor t\rfloor$. A positive integer $x$ satisfies $$\left\{\frac x3\right\}+\left\{\frac x5\right\}+\left\{\frac x7\right\}+\left\{\frac x{11}\right\}=\frac{248}{165}.$$ Determine all possible values of $$\left\{\frac{2x}3\right\}+\left\{\frac{2x}5\right\}+\left\{\frac{2x}7\right\}+\left\{\frac{2x}{11}\right\}.$$',['Floors & fractional parts','Modular arithmetic'])
fix('isr_2023_gillis_q3',r'Arrange equal circular cells in a triangular lattice with $5784$ rows: row $i$ contains $i$ cells, with adjacent rows offset so that neighbouring circles touch. Partition all cells into pairs of touching cells. Call a pair diagonal if its cells lie in different rows. What is the smallest possible number of diagonal pairs?',['Parity','Algorithms & constructions','Combinatorial geometry'])
fix('isr_2023_gillis_q7',r'A rook and a target square are placed on an infinite square board. There are $n$ blocked squares, which the rook may neither enter nor pass through. Suppose the target is reachable. Decide separately whether every such arrangement admits a route of at most (a) $1.99n+100$ moves; (b) $2n-2\sqrt{3n}+100$ moves. A move travels any positive distance along one row or column.',['Combinatorial geometry','Extremal arguments','Graph theory'])
def sl(n,s,t):fix(f'lka_2018_slmc_q{n}',s,t)
sl(1,r'A coded numeral has symbol pattern $ABCDEEDFCGHE$, where distinct letters represent distinct decimal digits. Which numeral can it represent: $201877841637$, $201877841222$, $201877841333$, $201877841444$, or $201877841555$?',['Logic & information'])
sl(2,r'You have two identical sweets of one type and three identical sweets of another type. How many distinct nonempty selections can you put on a plate?',['Counting'])
sl(3,r'Using each of the digits $2,0,1,8$ exactly once as a separate number, and only addition, multiplication and parentheses, what is the largest value obtainable?',['Inequalities','Equations & systems'])
sl(4,r'How many pairwise noncongruent triangles have a side of length $4\text{ cm}$ and area $2018\text{ cm}^2$?',['Area & dissection','Constructions & loci'])
sl(5,r'A $4\times4$ table has row sums $14,\,?,\,15,\,16$ and column sums $21,13,12,18$. Find the missing row sum.',['Algebraic identities'])
sl(6,r'Which inequality holds for every real $a$? (A) $7a>3a$; (B) $7a^2>3a^2$; (C) $7(a+1)>3(a+1)$; (D) $5-7a>5-3a$; (E) $217+a>3+a$.',['Inequalities'])
sl(7,r'A right triangle has hypotenuse $2018\text{ cm}$ and one leg $1118\text{ cm}$. Find the other leg. You may use $\sqrt{3136}=56$.',['Triangle geometry'])
sl(8,r'For how many integers $n\ge3$ does a regular $n$-gon have interior angles that are an integer number of degrees?',['Divisibility & GCD','Arithmetic functions'])
sl(9,r'Seventy-five students take part in at least one of events $A,B,C$. The three participation totals are in the ratio $2:5:4$. Every participant in $A$ also participates in $B$, and no one participates in all three. The number in both $B,C$ is one third of the number in $A$. How many students participate in exactly one event?',['Counting','Sets & partitions'])
sl(10,r'Triangle $ABC$ is right isosceles at $B$, with $AB=BC=2$. Let $Q$ be the midpoint of $AC$. A line through $Q$ meets segment $BC$ at $X$; its perpendicular through $Q$ meets segment $AB$ at $Y$. Find the area of quadrilateral $XQYB$.',['Coordinates & vectors','Area & dissection'])
sl(11,r'Sumana has coins of denominations $2,5,10$ rupees. She has three times as many $5$-rupee coins as $10$-rupee coins. The total value of her $2$-rupee coins exceeds that of her $5$-rupee coins by three rupees. If she has at least ten $2$-rupee coins, what is the least possible total value of her coins?',['Diophantine equations','Parity'])
sl(12,r'Find the smallest six-digit positive integer divisible by $9$ such that deleting its first and last digits leaves a four-digit integer whose only prime divisor is $11$.',['Digits & bases','Primes'])
sl(14,r'Concatenate the positive integers to form $0.123456789101112\ldots$. What is the $2018$th digit after the decimal point?',['Counting','Digits & bases'])
sl(15,r'Figure 1 is an equilateral triangle. At every stage, subdivide each smallest triangle into four by joining its side midpoints. The numbers of smallest triangles in two consecutive figures sum to $20480$. Which figures are they? You may use $4^6=4096$.',['Sequences & recurrences'])
sl(17,r'A sum of copies of $1/3$ equals a sum of copies of $1/5$. The total number of terms on both sides is strictly between $20$ and $26$. Determine that total.',['Diophantine equations','Divisibility & GCD'])
sl(18,r'Real numbers $a_1,\ldots,a_{2018}$ satisfy $a_1=1$ and $a_{n+1}+a_n=a_{n+1}^2-a_n^2$ for $1\le n<2018$. Determine the smallest possible $a_{2018}$.',['Sequences & recurrences','Induction','Inequalities'])
sl(20,r'Choose $T$ on side $BC$ of triangle $ABC$. Points $Z,Y,X$ divide $AT$ in that order from $A$ into four equal segments. Let $S$ be the combined area of triangles $ABZ$, $BYX$, $ACZ$ and $CYX$, and let $U$ be the area of the rest of $ABC$. Decide whether $S=U$ only when $AT\perp BC$, only when $T$ is the midpoint of $BC$, or for every position of $T$.',['Area & dissection'])
sl(21,r'Two players alternately toss a fair coin until someone first gets heads; that player wins. What is the probability that the player who starts wins?',['Probability','Recurrences & generating functions'])
sl(22,r'Each cell of a $10\times10$ board is coloured red or blue. How many colourings make every $2\times2$ subboard contain an odd number of blue cells? Different cells are distinguished.',['Colouring','Parity','Counting'])
sl(23,r'Write $1,2,\ldots,2018$ on a board. Two players alternate replacing two entries by their nonnegative difference until one entry remains. The first player wins if that entry is odd; the second wins if it is even. Which player wins, and does the outcome depend on the moves?',['Invariants','Parity'])
sl(24,r'A set contains $2019$ integers, and every sum of $2018$ of its elements is divisible by $2018$. Which assertions must hold: (I) every element is divisible by $2018$; (II) all elements have the same residue modulo $2018$; (III) at least one element is divisible by $2018$?',['Modular arithmetic'])
sl(25,r'How many four-digit positive integers have the property that every rearrangement of their digits that is still a four-digit number is divisible by $5$? A rearrangement beginning with zero is not a four-digit number.',['Counting','Digits & bases'])
sl(26,r'Exactly one of five people broke a vase. Their statements are: Kanchana: “If Ranjan did not do it, Pooja or Roshan did.” Damitha: “Ranjan did it.” Ranjan: “Pooja did it.” Pooja: “Roshan did it.” Roshan: “Kanchana did it.” Exactly one statement is true. Who broke the vase?',['Logic & information'])
sl(27,r'Sarath, Ragavan and Mohamed play a series of two-player carrom games. The loser of each game sits out the next one. Sarath plays $9$ games, Ragavan $14$, and Mohamed $15$. Which statements hold: (I) Sarath and Ragavan play game $13$; (II) Ragavan and Mohamed play game $15$; (III) there are $19$ games in all?',['Counting','Parity'])
sl(28,r'In increasing order, list the positive integers expressible as sums of distinct nonnegative powers of $3$: $1,3,4,9,10,12,13,\ldots$. Find the $100$th entry.',['Digits & bases'])
sl(29,r'Positive integers $a,b$ satisfy: $a^b$ has exactly five positive divisors and $b^a$ has exactly seven. How many positive divisors does $ab$ have?',['Arithmetic functions','Valuations'])

# Corrected statements and compact mathematical paraphrases of publisher-held sources.
fix('mng_2025_706550',r'Prove that no integer pair $(x,y)$ satisfies $x^4+x^3+x^2+x=y^6+61$.',['Modular arithmetic','Diophantine equations'])
fix('mng_2025_510a85',r'Let $\phi$ be Euler’s totient function. Nonnegative integers $a,b,c,d$ satisfy $$\phi(2^a(2b+1))=2^c(2d+1).$$ Assuming $b\ge1$, prove both $a\le c$ and $b\ge2d+1$.',['Arithmetic functions','Valuations'])
fix('mng_2025_2e8d43',r'Triangle $ABC$ is scalene, with incenter $I$ and circumcircle $\omega$. Let $M\ne B$ be the second intersection of $BI$ with $\omega$, and reflect $I$ in $AC$ to obtain $I_B$. A point $H$ on the minor arc $AM$ satisfies $BH\perp HI_B$. Put $T=II_B\cap AC$, let $N\ne H$ be the second intersection of $HT$ with $\omega$, and set $R=MN\cap AC$. Show that triangle $IRM$ is isosceles.',['Triangle centres','Circles & tangency','Transformations'])
fix('mng_2025_407690',r'Triangle $ABC$, with $AB\ne AC$, has orthocenter $H$. Choose $T$ on the circumcircle’s arc $BC$ not containing $A$. The line through $H$ parallel to $BC$ meets $TB,TC$ at $P,Q$. The circumcircles of $PAB,QAC$ meet again at $S$. If $\angle PAQ=2\angle BAC$, prove (a) $B,H,C,S$ are concyclic; (b) either $\angle PAH=\angle HAQ$ or $\angle PAB=\angle BAH$.',['Angles & cyclic quadrilaterals','Triangle centres'])
fix('chn_2013_2e07c9',r'How many ordered pairs $a,b\in\{1,\ldots,2013\}$ make the values $ak^3+bk$, for $1\le k\le2013$, pairwise distinct modulo $2013$?',['Integer polynomials','Modular arithmetic'],'Number Theory')
fix('chn_2013_768547',r'Can integers $a,b,c$ make all three numbers $a^2bc+2$, $ab^2c+2$ and $abc^2+2$ perfect squares?',['Modular arithmetic','Squares & powers'])
fix('chn_2013_cd06ba',r'For $0<t<1$, let $D$ be the closed triangular region bounded by $x=1$, $y=0$ and $y=t(2x-t)$. Put $P=(t,t^2)$ and $Q=(1,0)$. Prove that every triangle contained in $D$ and having $P,Q$ as two vertices has area at most $1/4$.',['Coordinates & vectors','Geometric inequalities','Area & dissection'])
fix('chn_2012_4d98f1',r'Determine the least positive integer $n$ for which $$\sqrt{\frac{n-2011}{2012}}-\sqrt{\frac{n-2012}{2011}}<\sqrt[3]{\frac{n-2013}{2011}}-\sqrt[3]{\frac{n-2011}{2013}}.$$',['Inequalities','Equations & systems'])
fix('chn_2012_b348db',r'For a composite positive integer $n$, let $F(n)$ be the sum of its three smallest positive divisors and $G(n)$ the sum of its two largest. Determine all $n$ for which $G(n)=F(n)^k$ for some positive integer $k$.',['Divisibility & GCD','Diophantine equations'])
fix('chn_2012_bd05d8',r'For nonnegative real numbers $a_1,\ldots,a_n$, prove $$\sum_{k=1}^n\frac{\prod_{j=1}^{k-1}a_j}{\prod_{j=1}^k(1+a_j)}\le1,$$ where an empty product is $1$.',['Inequalities','Sequences & recurrences'])
fix('chn_2011_dd25aa',r'Positive real numbers $a,b,c,d$ have product $1$. Establish $$\frac1a+\frac1b+\frac1c+\frac1d+\frac9{a+b+c+d}\ge\frac{25}4.$$',['Inequalities'])
fix('chn_2011_1750ef',r'For each real $\alpha\ge0$, determine the least real $\lambda$ such that $$|z_1-xz_2|\le\lambda|z_1-z_2|$$ whenever $z_1,z_2\in\mathbb C$, $0\le x\le1$, and $|z_1|\le\alpha|z_1-z_2|$.',['Complex numbers','Inequalities'])
fix('chn_2011_833604',r'Find and prove the maximum of $$\frac{xy(1-x-y)}{(x+y)(1-x)(1-y)}$$ over $0<x,y<1$.',['Inequalities'])
fix('chn_2010_3a1cdd',r'Let $n>2$. Choose $2n$ pairwise distinct nonempty subsets $A_1,\ldots,A_{2n}$ of $\{1,\ldots,n\}$ and put $A_{2n+1}=A_1$. Find the maximum possible value of $$\sum_{i=1}^{2n}\frac{|A_i\cap A_{i+1}|}{|A_i|\,|A_{i+1}|}.$$',['Sets & partitions','Extremal arguments','Algorithms & constructions'])
fix('chn_2010_8ae09b',r'Strictly increasing affine maps $f,g:\mathbb R\to\mathbb R$ satisfy $f(x)\in\mathbb Z$ if and only if $g(x)\in\mathbb Z$. Show that $f(x)-g(x)$ is an integer for every real $x$.',['Functions & graphs','Equations & systems'])
fix('chn_2010_49eb42',r'Find the least odd integer $a>5$ for which positive integers $m_1,m_2,n_1,n_2$ satisfy $$a=m_1^2+n_1^2,\quad a^2=m_2^2+n_2^2,\quad m_1-n_1=m_2-n_2.$$',['Diophantine equations','Squares & powers'])
fix('chn_2002_2488b3',r'Determine all positive integers $n$ with $20n+2\mid2003n+2002$.',['Divisibility & GCD'])
fix('chn_2002_1d1d7c',r'Find the positive integers $k$ such that every positive triple $a,b,c$ satisfying $$k(ab+bc+ca)>5(a^2+b^2+c^2)$$ is the side-length triple of a nondegenerate triangle.',['Inequalities'])
fix('chn_2002_e8a6d2',r'If $n\ge2$ and $(P_1,\ldots,P_n)$ is a permutation of $(1,\ldots,n)$, prove $$\sum_{i=1}^{n-1}\frac1{P_i+P_{i+1}}>\frac{n-1}{n+2}.$$',['Inequalities'])
fix('chn_2002_0cf4b1',r'Let $D,E,F$ be the feet of the altitudes from $A,B,C$ of an acute triangle. Prove that $DE+EF+FD\le(AB+BC+CA)/2$.',['Geometric inequalities','Triangle geometry'])
# Explicit subject review where the source had no technique tags.
metadata={
'ind_2001_83815e':('Algebra',['Inequalities']),
'ind_2006_748949':('Combinatorics',['Bijections','Counting']),
'ind_2006_8a81d7':('Combinatorics',['Invariants','Algorithms & constructions']),
'sgp_2025_51172c':('Combinatorics',['Games & strategies','Modular arithmetic','Parity']),
'sgp_2025_bbcd49':('Number Theory',['Modular arithmetic','Pigeonhole principle']),
'sgp_2025_cb149f':('Combinatorics',['Recurrences & generating functions','Parity','Counting']),
'phl_2023_7f39a8':('Number Theory',['Diophantine equations','Divisibility & GCD']),
'phl_2023_98642e':('Number Theory',['Factorials & binomial coefficients','Digits & bases']),
'phl_2023_bd8fcd':('Number Theory',['Diophantine equations','Divisibility & GCD','Squares & powers']),
'phl_2023_d11b49':('Combinatorics',['Probability','Graph theory','Recurrences & generating functions']),
'phl_2023_fa73ce':('Combinatorics',['Counting','Permutations & arrangements']),
'chn_2021_13a5c8':('Combinatorics',['Sets & partitions','Counting']),
'chn_2021_2228bf':('Algebra',['Algebraic identities','Equations & systems']),
'chn_2021_237717':('Combinatorics',['Probability','Pigeonhole principle','Combinatorial geometry']),
'chn_2021_248190':('Algebra',['Functions & graphs','Equations & systems']),
'chn_2021_4a44dc':('Algebra',['Functions & graphs','Equations & systems']),
'chn_2021_854f88':('Algebra',['Equations & systems']),
'chn_2021_8c05bb':('Algebra',['Trigonometry','Equations & systems']),
'chn_2021_bf8435':('Combinatorics',['Sets & partitions','Counting']),
'chn_2020_c412ea':('Algebra',['Equations & systems']),
'chn_2020_439128':('Combinatorics',['Counting','Sets & partitions']),
'jpn_2024_70520f':('Number Theory',['Digits & bases','Primes']),
'jpn_2024_851b05':('Combinatorics',['Induction','Extremal arguments']),
'jpn_2023_faa0e3':('Combinatorics',['Permutations & arrangements','Extremal arguments','Graph theory'])}
for k,(t,subs) in metadata.items(): reviews[k]['topic']=t;reviews[k]['subtopics']=subs
# Keep links instead of reproducing known faulty source expositions.
for k in ['ind_2003_193fab','chn_2002_1d1d7c','chn_2024_5ac422']:reviews[k]['solutionKind']='source-link'
reviews['chn_2021_4a44dc']['duplicateOf']='chn_2021_248190'
reviews['chn_2021_4a44dc']['omitReason']='Equivalent alternate paper appearance of chn_2021_248190: B1 Q10 asks for a minimum, while A1 Q9 asks for the value; the hypotheses force the same constant. Both appearances are retained on the canonical entry.'
duplicate_note='Also First Round, Test Paper B1, Question 10, asking for the minimum of the same forced constant.'
if duplicate_note not in reviews['chn_2021_248190'].get('note',''):reviews['chn_2021_248190']['note']=(reviews['chn_2021_248190'].get('note','')+' '+duplicate_note).strip()
for duplicate,canonical in {'tha_2017_124959':'tha_2017_819f39','ind_2011_60c493':'ind_2011_1536f1','chn_2011_6ce2fb':'chn_2011_002f2e'}.items(): reviews[duplicate]['duplicateOf']=canonical

fix('jpn_2025_fef72c',r'Seven regular hexagonal cells form a cluster: one central cell and its six edge-neighbours. Place the integers $1,\ldots,7$ in the cells, one per cell. Each pair of cells sharing an edge must have labels summing to at most $10$. How many placements are possible? Rotations and reflections are counted separately.',['Counting','Permutations & arrangements','Graph theory'])
fix('jpn_2023_c14de8',r'A regular hexagon $PQRSTU$ lies inside rectangle $ABCD$, with $P$ on $AD$, $Q$ on $AB$, $S$ on $BC$ and $T$ on $CD$. The other two vertices $R,U$ lie strictly inside the rectangle. Triangle $APQ$ has area $20$, and quadrilateral $QBSR$ has area $23$. Find the area of the hexagon.',['Similarity & congruence','Area & dissection','Quadrilaterals & polygons'])
# In these statements all incidences are already specified in words; the figures
# are illustrative and can be omitted without losing any mathematical data.
for k in ['ind_2010_cdcaa7','ind_2011_c0e0a9','chn_2023_85e679','jpn_2024_f20229','jpn_2023_b18329','jpn_2022_7ae500']:
 rawpath=ROOT/'research/raw/asia'/(k+'.json')
 if not rawpath.exists():rawpath=P/'extra'/(k+'.json')
 raw=json.loads(rawpath.read_text())
 st=reviews[k].get('statementOverride',raw['problem_markdown'])
 st=re.sub(r'!\[[^\]]*\]\([^)]*\)','',st).strip().replace('As shown in the figure, in an acute triangle','In an acute triangle')
 reviews[k]['statementOverride']=st
(P/'reviews.json').write_text(json.dumps(reviews,ensure_ascii=False,indent=2))
