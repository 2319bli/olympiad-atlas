"""Restore mathematically assessed questions outside the preferred 4–7 band.

These English statements were individually checked against the stored source
statements or original papers. Numeric ratings are retained unchanged.
"""
import json
from pathlib import Path
P=Path(__file__).parent
R=json.loads((P/'reviews.json').read_text())
S={
'est_2025_29d115':r'Congruent rectangles $ABZY$, $CDXZ$ and $EFYX$ lie inside the regular hexagon $ABCDEF$. What fraction of the hexagon is covered by their union?',
'rus_2025_21b815':r'For a function $f$ attaining a minimum, write $m(f)=\min_{x\in\mathbb R} f(x)$. Let $P_1,P_2$ be monic quadratic polynomials whose graph vertices are $A_1,A_2$. Suppose $m(P_1\circ P_2)-m(P_1)=m(P_2\circ P_1)-m(P_2)>0$. Determine the angle made by $A_1A_2$ with the horizontal axis.',
'rus_2025_522ea4':r'A cube of side $2N+1$, where $N$ is a positive integer, is subdivided into unit cubes. Colour some unit cubes black and the rest white. Every axis-aligned block of $2\times2\times2$ unit cubes contains at most four black cubes. Determine the maximum total number of black cubes.',
'rus_2025_92724f':r'Assign a real weight in $[-1,1]$ to each edge of the complete graph on $10^6$ vertices. For each set of six vertices, add the weights of its fifteen edges. Both positive and negative sums occur. What is the largest possible number $C$ such that every such sum has absolute value at least $C$?',
'rus_2025_ab106a':r'Let $ABCD$ be cyclic, with no parallel pair of sides, and let $\Omega$ be its circumcircle. Denote the incircles of $DAB,ABC,BCD,CDA$ by $\omega_a,\omega_b,\omega_c,\omega_d$. For each consecutive pair of these incircles, take their common external tangent other than the line containing a side of $ABCD$. In cyclic order these four tangents form a quadrilateral with circumcircle $\Gamma$. Prove that the lines joining the centres of $\omega_a,\omega_c$, of $\omega_b,\omega_d$, and of $\Omega,\Gamma$ meet at one point.',
'rus_2025_d73fb6':r'A rectangle is partitioned into smaller rectangles by horizontal and vertical segments, with no unused segment inside a part. Is it always possible to choose one diagonal in every part and colour the resulting triangles black or white so that triangles sharing a boundary segment have different colours?',
'grc_2024_97ff5b':r'Colour a $7\times7$ grid red and blue. Exactly four rows contain more blue than red cells, and exactly four columns contain more red than blue cells. What is the greatest possible side length of an axis-aligned square subgrid whose cells are all the same colour?',
'blr_2024_32812a':r'Take the triangular array of lattice positions with rows of lengths $1,2,\ldots,n$. For positive integers $k\le n$, place at most one checker at each position, with at most $k$ checkers on every lattice line parallel to any of the three sides. Let $T(k,n)$ be the largest number that can be placed. Prove $T(k,n)\le\left\lfloor k(2n+1)/3\right\rfloor$, and determine $T(1,n)$ and $T(2,n)$.',
'rou_2025_cf5c36':r'Prove that a positive rational number $r$ must be an integer if $r$ and $\sqrt{r+1}$ have equal fractional parts.',
'rou_2025_ee7809':r'Let $m>n>0$ and $a,b,c>0$. If $|ma-nb|\le(m-n)c$, $|mb-nc|\le(m-n)a$ and $|mc-na|\le(m-n)b$, prove $a=b=c$.',
'rou_2025_dbb6e2':r'Triangle $ABC$ is right isosceles at $A$. Let $O,M,E,D$ be the midpoints of $BC,AC,CO,AM$, respectively, and put $F=OD\cap AE$. Prove both $MF\perp OD$ and $FC=OC$.',
'rou_2025_bba028':r'Find all triples of nonnegative integers $(a,b,c)$ for which $p=ab+bc+ca$ is prime and $p\mid a^2b^2+b^2c^2+c^2a^2$.',
'rou_2025_3c3a53':r'Start with counters $x=y=0$. A move chooses a nonnegative integer $k$ and changes $(x,y)$ to $(x+k+1,y+k^2+2)$. Stop as soon as $x\ge N$, for a given positive integer $N$. Find the smallest attainable final value of $y$.',
'ukr_2023_ef78ef':r'In a convex pentagon $ABCDE$, suppose $AB\parallel CD$, $BC\parallel DE$ and $\angle BAE=\angle AED$. Show that $AB+BC=CD+DE$.',
'ukr_2023_56327b':r'In quadrilateral $ABCD$, the angles at $B,D$ are right angles. Write $P=AC\cap BD$, $Q=AB\cap CD$, $R=AD\cap BC$. Let $\ell$ be the midline of triangle $PQR$ parallel to $QR$. Prove that the circumcircles of the triangles bounded by $AB,AD,\ell$ and by $CD,CB,\ell$ are tangent.',
'ukr_2023_8cc3d1':r'Every edge of the complete graph on $2024$ vertices is coloured one of three colours. Determine the largest integer $m$ such that every colouring has a connected monochromatic subgraph on at least $m$ vertices. Equivalently, a traveller may choose one transport type and revisit cities, but each journey must use that type.',
'che_2023_b4de88':r'Triangle $ABC$ satisfies $2\angle CBA=3\angle ACB$. Points $D,E$ on $AC$, in the order $A,D,E,C$, trisect angle $ABC$: $\angle ABD=\angle DBE=\angle EBC$. The bisector of $\angle ACB$ meets $AB$ at $F$. Prove $BE\parallel DF$.',
'hrv_2019_1be61d':r'Write $D(n)$ for the number of positive divisors of $n$. Count the positive-integer quadruples $(a,b,c,d)$ with every entry below $10^6$, satisfying $b=a^2+1$, $c=b^2+1$, $d=c^2+1$, and with $D(a)+D(b)+D(c)+D(d)$ odd.',
'hrv_2019_2091aa':r'In triangle $ABC$, the lengths $AB,BC,CA$ are $4,7,5$. If $\alpha=\angle BAC$, calculate $\sin^6(\alpha/2)+\cos^6(\alpha/2)$.',
'hrv_2019_321ef6':r'A right triangle has integer side lengths and inradius $4$. Determine every possible pair of leg lengths.',
'hrv_2019_51b7ed':r'Two walkers stand together beside a railway. When the front of a constant-speed train reaches them, they begin walking at the same constant speed in opposite directions along the track. Each stops when the rear of the train reaches her. The walker travelling with the train covers $45$ metres, and the other covers $30$ metres. Find the train length.',
'hrv_2019_8808e0':r'Find all real $x\ne-2$ satisfying $\left\lfloor\frac{x^2+1}{x+2}\right\rfloor+\left\lfloor\frac{x-1}{2}\right\rfloor=\frac{x(3x+1)}{2(x+2)}$. Here $\lfloor t\rfloor$ is the greatest integer at most $t$.',
'hrv_2019_77ac9e':r'Among real pairs $(a,b)$ with $a^2+b^2=25$, determine all those minimizing $ab+a+b$.',
'mkd_2023_09c6cc':r'Let $p,q$ be odd primes and let $a$ be a positive integer with $p\mid a^q+1$ and $q\mid a^p+1$. Show that at least one of $p,q$ divides $a+1$.',
'mkd_2023_1df9d3':r'For $n>1$, let $s(n)$ be its least prime divisor and $d(n)$ its number of positive divisors. Can one choose positive integers $a_1,\ldots,a_{2022}$ with $a_1<a_2-1<\cdots<a_{2022}-2021$ such that, for every $1\le k\le2021$, $d(a_{k+1}-a_k-1)>2022^k$ and $s(a_{k+1}-a_k)>2022^k$?',
'mkd_2023_cc62f8':r'The positive sequence $(a_n)$ satisfies $a_1=1$, $a_2=2$ and $a_{n+1}^4/a_n^3=2a_{n+2}-a_{n+1}$. Prove that $\sum_{k=1}^N a_k^2/a_{k+1}<3$ for every integer $N>1$.',
'rou_2025_c3d5be':r'Seven positive integers, giving the numbers of marbles received from Monday to Sunday, are strictly increasing and total $72$. Friday\'s number is five times Monday\'s, Saturday\'s six times Tuesday\'s, and Sunday\'s seven times Wednesday\'s. Determine Thursday\'s number.',
'rou_2025_04865f':r'Find primes $a\le b$ and $c\le d$ such that $a+b=c+d+1$ and $a^2+b^2+c^2+d^2=3543$.',
'rou_2025_d83145':r'Call a three-element subset of $\{1,\ldots,2025\}$ admissible if its elements form an arithmetic progression and it contains both $b$ and $5b$ for some $b$. Count (a) the admissible subsets containing $225$, and (b) all admissible subsets.',
'rou_2025_463b42':r'Positive integers $a<b<c$ satisfy $b\mid a+b+2c$ and $c\mid a+b+2c$. Prove that $\gcd(a+b,c)=c$. Then find all positive integers $k<1000$ for which such a triple can satisfy $abc=k^2$.',
'rou_2025_76bd7e':r'A workshop can divide all its registered pupils into teams of three boys and one girl. On a day when two girls and one boy are absent, all remaining pupils can instead form teams of four boys and one girl. How many pupils are registered?',
'rou_2025_5b88e0':r'Distinct positive integers $x,y,z,t$ and a nonnegative integer $a$ satisfy $2^x+2^y+2^z+2^t=305\cdot2^a$. Find the remainder of $a+x+y+z+t$ on division by $5$.',
'rou_2025_3b80b5':r'Express $2025$ as a sum of $40$ distinct positive integers. What is the smallest possible value of the largest summand?',
'rou_2025_6af78e':r'For nonnegative integers $a,b,c$, suppose both $m=(5a+6b+7c+6)/(4a+3b+2c+3)$ and $n=(a+2b+3c+5)/(3a+b+2c+5)$ are integers. Prove $m\ge2$, and determine $m,n$.',
'rou_2025_ec5818':r'Find positive integers $a,b$ satisfying $a/g=b+48g/\ell$ and $b/g=a-312g/\ell$, where $g=\gcd(a,b)$ and $\ell=\operatorname{lcm}(a,b)$.',
'rou_2025_aaf971':r'In isosceles triangle $ABC$, $AB=AC$ and $\angle BAC=30^\circ$. A point $D$ on $AC$ and distinct points $E,F,G$ on $AB$ satisfy $BC=BD=DE=EF$ and $DG=DF$. Prove $BF=GE$, and determine $\angle BCG$.',
'rou_2025_95ee7d':r'Find all four-digit decimal numbers $\overline{abcd}$ for which a prime $p$ satisfies $\overline{cd}-\overline{ab}=p+2$ and $\sqrt{\overline{ab}-4}+\sqrt{\overline{cd}}=p^2$. The two-digit blocks are interpreted numerically, allowing a leading zero in the second block.',
'rou_2025_2b8e0d':r'Which rational numbers can be written as $(a+b)/2-\sqrt{ab}$ with nonnegative integers $a,b$?',
'rou_2025_37dfda':r'Let $A=\{(x,y)\in\mathbb R^2:x+y+1=0\}$ and $B=\{(x,y)\in\mathbb R^2:x^3+y^3+1=3xy\}$. Show $A\subset B$ and that exactly one point belongs to $B\setminus A$.',
'rou_2025_d10be4':r'In cube $ABCDA\prime B\prime C\prime D\prime$, choose $M\in BC$ and $N\in DD\prime$ with $BM=DN$. Prove that $A\prime M$ is perpendicular to the plane through $A,B\prime,N$.',
'rou_2025_fccbaf':r'The diagonals of parallelogram $ABCD$ meet at $O$. For every point $M$ in the open segment $AB$, prove there is exactly one pair $N\in OC$, $P\in OD$, both in the respective open segments, for which $O$ is the centroid of triangle $MNP$.',
'rou_2025_4f853d':r'Solve $1/\{x\}+1/\lfloor x\rfloor+1/x=0$ in real numbers, where $\{x\}=x-\lfloor x\rfloor$. Values at which a denominator vanishes are excluded.',
'rou_2025_29b819':r'Determine every real solution of $\log_7(6^x+1)=\log_6(7^x-1)$.',
'rou_2025_7c762b':r'Solve $3^x+3^{\lfloor x\rfloor}+3^{x-\lfloor x\rfloor}=4$ for real $x$.',
'hrv_2019_5136f9':r'A three-digit decimal integer has digit sum $11$. Reversing its digits increases it by $594$. Determine all such integers.',
'hrv_2019_eb7aa0':r'Positive reals $a,b$ satisfy $a/b+b/a=3$ and $a^2/b+b^2/a=10$. Find $1/a+1/b$.',
'hrv_2019_77cb82':r'In triangle $ABC$, $\angle CAB=20^\circ$. If $D$ is the midpoint of $AB$ and $\angle CDB=40^\circ$, determine $\angle ABC$.',
'hrv_2019_419582':r'How many black-and-white colourings of a fixed $5\times5$ grid remain unchanged after a quarter-turn about its centre?',
'hrv_2019_ad88ff':r'Determine every integer solution $(m,n)$ of $mn+5m+2n=121$.',
'hrv_2019_8a4c00':r'Colour the integers $2,3,\ldots,32$ so that two distinct numbers have different colours whenever one divides the other. Find the least number of colours needed.',
'hrv_2019_4df0ce':r'Find the nonzero complex numbers $z$ satisfying $z^2=1/z+1/\overline z$.',
'hrv_2019_d91c48':r'Find positive primes $p,q$ for which $x^2+px+q=0$ has two different integer roots.',
'hrv_2019_ccede5':r'Solve the system $xy^3=-135$, $(x+y)y=-6$ over the real numbers.',
'hrv_2019_418450':r'Count circular bracelets with four black and four white beads. Two arrangements represent the same bracelet when a rotation or a reflection matches their bead colours.',
'hrv_2019_957c0e':r'A $6\text{ m}\times6\text{ m}$ square room contains a rectangular $2\text{ m}\times1.5\text{ m}$ bath flush against the two walls of one corner. Find the greatest radius of a circular rug that fits on the remaining floor.',
'hrv_2019_81d8f2':r'Evaluate $\dfrac{\tan192^\circ+\tan48^\circ}{1+\tan168^\circ\tan408^\circ}$.',
'hrv_2019_10b55a':r'A right square pyramid has base side $12$ and vertical height $8$. Find its total surface area.',
'hrv_2019_d208b1':r'A positive real number $a$ satisfies $\log_{4a}(40\sqrt3)=\log_{3a}45$, with both logarithms defined. Determine $a^3$ and show it is an integer.',
'hrv_2019_c6226b':r'What is the largest number of distinct integers from $\{1,\ldots,999\}$ whose product is not divisible by $250$?',
'hrv_2019_464abc':r'Place coins in the cells of a $3\times3$ grid, allowing more than one coin per cell. The totals in the three rows and three columns must be six distinct numbers. Find the smallest possible total number of coins.',
'hrv_2019_ac44fe':r'An arithmetic progression has common difference $d$ and satisfies $a_2a_4=-d^2$. Determine $a_3a_5$.',
'hrv_2019_66f996':r'For which positive integers $n$ do three consecutive coefficients in the expansion of $(1+x)^n$ have ratio $3:4:5$?',
'hrv_2019_6fa81f':r'Let $R_n$ be the decimal integer consisting of $n$ digits, each equal to $2$. Prove $7\mid R_n-3^n+1$ for every positive integer $n$.',
'hrv_2019_d1cd2d':r'Choose $x,y$ independently and uniformly from $[-2,2]$. Find the probability that $|x|+|y|\ge1$ and $\bigl||x|-|y|\bigr|\le1$.',
'hrv_2019_ce41d3':r'Points $P_1,P_2,P_3$ divide $AB$ into four equal parts in that order. Lines through them parallel to $BC$ cut triangle $ABC$ into four regions. The region between the lines through $P_2,P_3$ has area $5$. Find the area of $ABC$.',
'hrv_2019_490db9':r'Show that no positive real pair $(x,y)$ satisfies $(x^3+y^3)(x^2+y^2)=2(x+y)=2$.',
'hrv_2019_3d8657':r'In isosceles triangle $ABC$ with $AB=AC<BC$, take $M\in BC$ with $BM=AB$, and let $N$ be the perpendicular projection of $M$ onto $AB$. Show that triangle $BMN$ and quadrilateral $ACMN$ have the same area and the same perimeter.',
'hrv_2019_98444d':r'For which real $p$ are the two roots of $(p-3)x^2+(p^2+1)x-11p+18=0$ the leg lengths of a right triangle with hypotenuse $\sqrt{17}$?',
'hrv_2019_c2e772':r'Find positive integers $a,n$ satisfying $a^4=3a^2+2^n$.',
'hrv_2019_5e7940':r'For $a,b\ge0$ with $a+b\le2$, prove $\dfrac1{1+a^2}+\dfrac1{1+b^2}\le\dfrac2{1+ab}$. Determine all equality cases.',
'hrv_2019_fa98b1':r'Let $AB=2$ and let $P$ be its midpoint. A tangent from $A$ touches the circle with diameter $PB$ at $T$. Calculate $PT$.',
'hrv_2019_550cc5':r'Find all real pairs $(x,y)$ satisfying $\cos2x+\cos2y+2\sin x\sin y+2\cos x\cos y=4$.',
'hrv_2019_1f7461':r'Determine positive integers $m,n$ such that $9^m+3^m-2=2p^n$ for some prime $p$.',
'hrv_2019_6f4303':r'Find integers $a,b$ with $b\ge0$ satisfying $a^2+2ab+b!=131$.',
'hrv_2019_aabd8b':r'Inside a semicircle, place a smaller semicircle with parallel diameter, its diameter endpoints on the larger arc, and its arc tangent to the larger diameter. Repeat indefinitely to obtain nested semicircles $K_1,K_2,\ldots$, starting with radius $1$. Colour $K_n\setminus K_{n+1}$ blue for odd $n$ and yellow for even $n$. Find the total blue area.',
'hrv_2019_5cd593':r'Remove two opposite corner cells from an $n\times n$ board, where $n\ge2$. In how many ways can $n$ identical rooks be placed on the remaining cells, with exactly one in every row and column?',
'ukr_2023_dbd666':r'Triangle $ABC$ is right-angled at $C$. On its circumcircle, let $W_A,N_A$ be the midpoints of the minor and major arcs $BC$, and let $W_B,N_B$ be the midpoints of the minor and major arcs $AC$. Put $P=AB\cap N_AW_B$ and $Q=AB\cap N_BW_A$. Prove $AP=BQ$.',
'rou_2025_2d74ee':r'An integer $n\ge3$ has a prime divisor $p\equiv1\pmod3$ such that $p^2\mid n$ and $n/p$ is square-free. Prove that twice the sum of the positive divisors of $n$, divided by their number, is an integer.',
'rou_2025_34c4bd':r'Nonzero integers $a_1,\ldots,a_n$, with $n\ge2$, have sum equal to product. Prove that $\prod_{i=1}^n(a_i^2-1)$ is a perfect square.',
'rou_2025_3262c3':r'Let $(a_n)$ be a positive real sequence. If its partial sums $\sum_{i=1}^n a_i$ are unbounded, prove the partial sums $\sum_{i=1}^n a_i/(1+a_i)$ are also unbounded.',
'rou_2025_3150d7':r'Define $a_1=1$ and $a_n=(a_{n-1}+1)^2$ for $n\ge2$. For every odd prime $p$, prove that $a_{2p}-a_p$ has at least $p$ distinct prime factors.',
'hun_2025_kurschak_3':r'Let $n\ge10$ points in the plane have no collinear triple. Show that they can be coloured red and blue so that every half-plane containing at least ten of the points contains both colours.',
'hun_2024_kurschak_2':r'Choose $n$ distinct points on a line and insert them one by one in some order. Each newly inserted point, except the first, is joined to its nearest earlier point; ties are broken in favour of the one inserted earlier. (a) For $n=10^6$, give a point set for which every insertion order produces a graph of maximum degree at most $41$. (b) For $n=10^{13}$, show that every point set has an insertion order producing a vertex of degree at least $42$.',
'fra_2025_january_1':r'Triangle $ACE$, with $AE<AC$, has circumcircle $\Omega$ centred at $O$. Its tangent at $A$ meets $CE$ at $B$. The circle centred at $B$ through $A$ meets line $AE$ again at $D$. Let $G=OE\cap BD$. Prove that $A,B,G,O$ are concyclic.'
}
for k,s in S.items():
 R[k]['statement']=s.replace("\\'", "'")
 # Explicitly retain official linked solutions for newly paraphrased copyright records.
 d=json.loads((P/(k+'.json')).read_text())
 if d.get('booklet_copyright_holder') and not R[k].get('solution'):
  R[k]['solution']='';R[k]['solutionKind']='source-link'
 R[k]['notes']=(R[k].get('notes','')+' English mathematical paraphrase; any auxiliary figure is described by the statement.').strip()
(P/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
print('Restored statements:',len(S))
