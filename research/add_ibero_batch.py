from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');raw=p/'international-raw'
r=json.loads((p/'international-reviews.json').read_text());o=json.loads((p/'international-extra-solutions.json').read_text())
r.update({
'imo_2022_official_p3':[7.5,'The unusual interaction between a quadratic congruence and cycle uniqueness requires discovering a closure lemma for the two smaller prime neighbours, then inducting after deleting the largest prime.'],
'ibe_2002_098b42':[4.5,'Reverse the deletion map on the infinite list to obtain a rounded multiplication recurrence, then identify the last term below 2002.'],
'ibe_2002_95db74':[4.5,'A moving-point argument makes triangle containment into a parity invariant; the key is counting the six triangles that change at a crossed segment.'],
'ibe_2002_68f137':[5,'The locus requires identifying a second fixed point on the moving circumcircle, or deriving a linear relation between the two side parameters, and checking the entire open segment is attained.'],
'ibe_2002_4afa52':[4,'Reflect across the angle bisector and use two cyclic quadrilaterals; the auxiliary perpendicular foot links the two target angles.'],
'ibe_2002_779f08':[4.5,'A quantitative decrease estimate is needed, rather than merely proving eventual negativity; squaring the recurrence gives a suitable bound after controlling the small-value phase.'],
'ibe_2002_a4c329':[8,'The lower bound uses a three-colour invariant and a long delayed capture, while the upper bound needs a substantial pursuit strategy with several boundary configurations.'],
'ibe_2001_c98425':[4,'Construct decimal numbers divisible by all possible four-digit products; a fixed suffix and a digit-sum congruence give an unbounded family.'],
'ibe_2001_33a740':[5,'Reflecting in the two angle bisectors reveals that the contact triangle is similar to the original; translating the equal-distance hypothesis then forces equal base angles.'],
'ibe_2001_6d6ba6':[4.5,'Double-count pairwise symmetric differences by individual elements and apply t(k−t)≤k²/4, then convert a small symmetric difference into a large intersection.'],
'ibe_2001_7126e6':[3,'Counting progressions by their middle element immediately gives the sharp sum of minimum left/right counts, attained by consecutive integers.'],
'ibe_2000_a16b2e':[4,'A modular construction labels each edge by the average of its endpoints; invertibility of two simultaneously verifies both constraints.'],
'ibe_2000_c6fad8':[6.5,'Parity and two congruences set up a prime-valuation argument; simultaneous lifting of odd and even prime exponents gives an exponential lower bound that conflicts with a<b.'],
'ibe_2000_eed830':[4.5,'Three retained terms force the arithmetic difference to be rational, and unbounded denominator powers then force the geometric ratio to be integral; the constant case needs separate treatment.'],
'ibe_2000_6e6cb0':[6,'The previous move must be included in the game state; the winning invariant has four states modulo 13 and needs a complete legal-response table.']
})
q={'id':'imo_2022_official_p3','competition_code':'IMO','competition':'IMO','year':2022,'problem_number':'3','primary_domain':'Number theory','topics':[['Number theory','Quadratic congruences'],['Combinatorics','Graphs']], 'problem_markdown':r'Fix a positive integer $k$ and a finite set $S$ of odd primes. Show that, up to rotation and reflection, at most one circular ordering of $S$ has this property: the product of each pair of adjacent primes equals $x^2+x+k$ for some positive integer $x$.','solutions_markdown':[r'Allow $x=0$ as well. If $p<r$ and $pr=x^2+x+k$, then $0\leq x<r$. A quadratic congruence modulo the prime $r$ has at most two roots, so $r$ has at most two smaller possible neighbours. If these are $p<q<r$, write $pr=x^2+x+k$ and $qr=y^2+y+k$ with $x<y<r$. Vieta gives $x+y=r-1$, and subtraction gives $y-x=q-p$. Substitution yields $4pq=(r-p-q)^2+4k-1$. Since $r-p-q$ is odd, putting $z=(|r-p-q|-1)/2$ gives $pq=z^2+z+k$. Thus the two neighbours are themselves compatible. Induct on $|S|$: remove its largest prime from any valid circle. Its two neighbours are forced and the resulting smaller circle is valid, so induction determines the circle uniquely.'],'officialSourceUrl':'https://www.imo-official.org/assets/documents/problems/2022/2022_eng.pdf','officialSolutionUrl':'https://www.imo-official.org/assets/documents/problems/2022/IMO2022SL.pdf'}
(raw/(q['id']+'.json')).write_text(json.dumps(q,ensure_ascii=False,indent=2))
o['ibe_2002_098b42']=r'''Consider the deletion process on the infinite list of positive integers. Its surviving entries after one round, in order, are $2,3,5,6,8,9,\ldots$; the $j$th is
$$T(j)=\left\lceil\frac{3j}{2}\right\rceil.$$
If $a_t$ is the first survivor after $t$ rounds, then $a_0=1$ and $a_{t+1}=T(a_t)$, because applying the next rounds to the survivors is the same process on their indices. Iterating gives
$$1,2,3,5,8,12,18,27,41,62,93,140,210,315,473,710,1065,1598,2397.$$
There are survivors among $1,\ldots,2002$ after round 17, but none after round 18. At round 17 there is only one: if there were a second, it would survive the next deletion. Thus the answer is $1598$.'''
o['ibe_2002_95db74']=r'''Fix the other eight points and move $P$ along a path to a point outside their convex hull. Choose the path to avoid all vertices and intersections of joining lines, and to cross each encountered line transversely.

The number of containing triangles can change only when $P$ crosses the interior of a segment $QR$ joining two of the eight points. At such a crossing, each of the six triangles $QRX$ changes its containment status, while every other triangle keeps its status. Hence the parity does not change. Outside the convex hull the count is zero, so it was even initially.'''
o['ibe_2002_68f137']=r'''Scale the side length to one and use coordinates
$$B=(0,0),\quad A=(1,0),\quad C=(1/2,\sqrt3/2).$$
Write $M=(u,0)$ and $N=(v/2,\sqrt3v/2)$, where $0<u,v<1$. Their cevians intersect at
$$P=\left(\frac{2u+v-3uv}{2(1-uv)},\frac{\sqrt3v(1-u)}{2(1-uv)}\right).$$
The points inside $ABC$ seeing $AC$ under $120^\circ$ form the interior arc $AC$ of
$$x^2+y^2-2x-\frac2{\sqrt3}y+1=0.$$
Substitution of the coordinates of $P$ into the left side gives
$$\frac{(1-u)(1-v)(1-u-v)}{(1-uv)^2}.$$
Consequently the condition is exactly $u+v=1$.

The circumcentre of $BMN$ is
$$O=\left(\frac u2,\frac{2v-u}{2\sqrt3}\right)
=\left(\frac u2,\frac{2-3u}{2\sqrt3}\right).$$
As $u$ runs through $(0,1)$, these points describe the open segment with endpoints $(0,1/\sqrt3)$ and $(1/2,-1/(2\sqrt3))$. Every such value gives an interior point $P$ on the required arc, so every point of the open segment is attained.

Geometrically, let $G$ be the centroid of $ABC$. The answer is the open segment on the perpendicular bisector of $BG$ whose endpoints are the perpendicular projections of $A$ and $C$ onto that line.'''
o['ibe_2002_4afa52']=r'''Let $H$ be the perpendicular projection of $D$ onto $AB$. Reflection in the angle bisector $BD$ fixes $D,E$ and interchanges $H,M$, so $\angle DME=\angle DHE$.

The quadrilaterals $AHED$ and $CFDM$ are cyclic, since each has two right angles. Therefore
$$\angle DHE=\angle DAE=\angle DCF=\angle DMF,$$
where the middle equality uses $A,D,C$ collinear and $AE\parallel CF$. These angle equalities can be read as directed angles if the perpendicular feet lie on extensions. The angle-bisector theorem places $D$ between $E,F$ when they are distinct, so $MD$ is the internal bisector of $\angle EMF$, giving the claimed ordinary-angle equality. If $E=F$, the claim is immediate.'''
o['ibe_2002_779f08']=r'''No term is zero: $a_2=3135/56$, and a reduced fraction with odd numerator and even denominator is taken by $p/q\mapsto(p^2-q^2)/(pq)$ to another such fraction. In particular, no later term equals $1$.

While $a_n\geq2$, we have
$$a_{n+1}^2=a_n^2-2+\frac1{a_n^2}\leq a_n^2-\frac74.$$
Thus some $m\leq1791$ has $a_m<2$; otherwise $a_{1791}^2\leq3136-1790\cdot7/4=3.5<4$, a contradiction. If no term has yet become negative, then $0<a_m<2$. Since $t-1/t$ is increasing for $t>0$, the next positive terms, if they exist, satisfy
$$a_{m+1}<\frac32,\qquad a_{m+2}<\frac56,\qquad a_{m+3}<\frac56-\frac65<0.$$
So a negative term occurs by index $1794<2002$.'''
o['ibe_2001_c98425']=r'''The number $N=22223232$ is divisible by $16$ because its last four digits are $3232$, and by $9$ because its digit sum is $18$. Thus $144\mid N$.

Prepend $9t$ copies of the digit $2$, for any nonnegative integer $t$. The resulting number still has last four digits $3232$, and its digit sum has increased by $18t$, so it remains divisible by $144=2^4\cdot3^2$. It has only digits $2,3$, with just two occurrences of $3$. Therefore the product of any four selected digits divides $144$ and hence divides the number. The lengths tend to infinity with $t$.'''
o['ibe_2001_6d6ba6']=r'''For each element $x$ of the ground set, let $t_x$ be the number of the $k$ subsets containing it. It contributes $t_x(k-t_x)$ to the sum of all pairwise symmetric differences. Hence
$$\sum_{i<j}|S_i\mathbin{\triangle}S_j|
=\sum_x t_x(k-t_x)\leq\frac{nk^2}{4}.$$
Some pair therefore satisfies
$$|S_i\mathbin{\triangle}S_j|\leq\frac{nk}{2(k-1)}.$$
Since $|S_i|,|S_j|\geq r$, the identity
$$2|S_i\cap S_j|=|S_i|+|S_j|-|S_i\mathbin{\triangle}S_j|$$
gives the required bound.'''
o['ibe_2000_a16b2e']=r'''Work with labels modulo the odd integer $n$, identifying zero with the label $n$. Since two is invertible modulo $n$, label the edge joining distinct vertices $i,j$ with the unique residue $c$ satisfying
$$2c\equiv i+j\pmod n.$$
If $c=i$ or $c=j$, then $i=j$ modulo $n$, a contradiction. At a fixed vertex $i$, equal labels on edges $ij$ and $ik$ imply $i+j\equiv i+k$, so $j=k$. Thus the construction has both required properties.'''
o['ibe_2000_c6fad8']=r'''The only solution is $(m,a,b)=(2,2,3)$.

Reduction modulo $m+1$ shows $b$ is odd. Dividing $m^b+1$ by $m+1$ gives an alternating sum of an odd number of terms. If $m$ were odd, this sum would be odd, whereas it equals the even number $(m+1)^{a-1}$. Hence $m$ is even. Reduction modulo $m^2$ gives $m\mid a$, so $a$ is even. Also $b>a$, since $(m+1)^a>m^a+1$.

For a prime $p$, let $v_p(t)$ be the exponent of $p$ in $t$. The elementary lifting formulas for $(m+1)^a-1=m^b$ give, for every odd prime $p\mid m$,
$$v_p(a)=(b-1)v_p(m),$$
and, because $m,a$ are even,
$$v_2(a)=(b-1)v_2(m)-v_2(m+2)+1.$$
(These are the standard binomial-expansion formulas $v_p(x^t-1)=v_p(x-1)+v_p(t)$ for odd $p\mid x-1$, and $v_2(x^t-1)=v_2(x-1)+v_2(x+1)+v_2(t)-1$ for odd $x$ and even $t$.)

Combining the required prime powers in $a$ yields
$$a\geq\frac{m^{b-1}}{2^{v_2(m+2)-1}}\geq\frac{2m^{b-1}}{m+2}.$$
If $m\geq4$, the last expression is at least $4^{b-1}/3>b$ for every $b\geq3$, contradicting $a<b$. Thus $m=2$. The same valuation gives $a\geq2^{b-2}$; for odd $b\geq5$ this again contradicts $a<b$. Therefore $b=3$, and the original equation gives $a=2$, which indeed works.'''
o['ibe_2000_eed830']=r'''Exactly the positive integers are possible. Ratio one is realised by the constant arithmetic progression $1,1,1,\ldots$; each integer ratio greater than one is realised by retaining its powers from $1,2,3,\ldots$.

Conversely, a negative ratio would alternate signs infinitely often, which an arithmetic progression cannot do. Ratio zero would require infinitely many zero terms, also impossible for an arithmetic progression starting at one. If the arithmetic difference is negative, it has only finitely many positive terms, so it cannot contain the required infinite progression. If its difference is zero, the ratio is one.

It remains to consider positive arithmetic difference $d$. Write the second and third retained terms as $a=1+md$ and $a^2=1+nd$, with positive integers $m,n$. Then
$$d=\frac{n-2m}{m^2},$$
so both $d$ and $a$ are rational. All terms of the arithmetic progression have reduced denominators dividing one fixed denominator of $d$. If $a=u/v$ in lowest terms had $v>1$, its powers would have unbounded reduced denominators $v^j$, a contradiction. Thus $a$ is an integer.'''
o['ibe_2000_6e6cb0']=r'''The first player wins. Start by taking four stones, leaving $1996\equiv7\pmod{13}$. Maintain one of these states after each of the first player's turns:

* remainder $0$ modulo $13$;
* remainder $3$, with the last move equal to $3$;
* remainder $5$, with the last move equal to $5$;
* remainder $7$.

Here is the response table. Entries give the first player's reply to the second player's removal $s$; a dash denotes a move forbidden by the immediately preceding move.

| State before opponent moves | $s=1$ | $s=2$ | $s=3$ | $s=4$ | $s=5$ |
|---|---:|---:|---:|---:|---:|
| $0$ | 5 | 4 | 5 | 2 | 1 |
| $3$, last move 3 | 2 | 1 | — | 5 | 4 |
| $5$, last move 5 | 4 | 3 | 2 | 1 | — |
| $7$ | 3 | 5 | 4 | 3 | 2 |

Every reply differs from $s$ and returns to one of the four states. If the residue is $0$ and stones remain, there are at least 13, so every reply is affordable. For residues $3,5,7$, any row entry requiring more stones than that smallest representative occurs only when the opponent's own move already requires at least one extra block of 13. Thus all listed replies are legal whenever needed.

From a maintained state the second player can never take the last stone: at residues 3 and 5 the necessary removal is forbidden; at residues 0 and 7 it exceeds five. Since the pile strictly decreases and the first player always has a legal response, the first player eventually takes the last stone.'''
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));(p/'international-extra-solutions.json').write_text(json.dumps(o,ensure_ascii=False,indent=2))
