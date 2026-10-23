add(2000,3,4.5,'Number Theory',['harmonic sums','modular arithmetic','pairing'],r'If $p,q$ are coprime positive integers and $p/q=1-1/2+1/3-\cdots-1/1334+1/1335$, prove $2003\mid p$.',r'''The alternating sum equals $H_{1335}-H_{667}=\sum_{j=668}^{1335}1/j$. Pair each index $j$ with $2003-j$, which lies in the same range. Each pair contributes
$$\frac1j+\frac1{2003-j}=\frac{2003}{j(2003-j)}.$$
None of the denominators is divisible by the prime $2003$. Putting the paired sum over a common denominator therefore gives a numerator divisible by $2003$ and a denominator coprime to $2003$. Reducing the fraction cannot remove that numerator factor.''','Rewriting the alternating harmonic sum exposes a symmetric interval whose complementary denominator pairs sum to the target prime.')
add(2000,6,4.5,'Combinatorics',['set systems','double counting','locks and keys'],r'Five directors share access to ten locks, all of which must be opened. Any three directors must collectively have every key, but no pair may. Each director receives keys to exactly $n$ different locks. Determine all possible $n$.',r'''Each of the ten pairs of directors must be missing a key to some lock. A lock can be missing from at most two directors, since otherwise three directors would fail to open it. Thus one lock can obstruct at most one pair.

There are ten pairs and ten locks, so each pair must be the unique pair lacking a particular key. Consequently each lock's key is held by precisely the other three directors. A given director holds the keys whose excluded pair is chosen from the other four directors, so holds $\binom42=6$ keys. Conversely assigning keys in exactly this way meets both conditions. Therefore $n=6$.''','A tight correspondence between the ten obstructed pairs and ten locks forces the entire key distribution.')
add(2002,4,4,'Combinatorics',['partitions','distinguishing coordinates','greedy argument'],r'Seven pupils have distinct vectors of marks in twelve subjects. Prove that six subjects can be selected so that the pupils still have distinct mark vectors in the selected subjects.',r'''Start with no selected subjects, so all pupils belong to one class of indistinguishable mark vectors. If fewer than seven classes remain, choose two pupils in the same class. Their complete twelve-subject vectors differ, so some unselected subject separates them. Adding that subject increases the number of classes by at least one.

After at most six such additions there are seven classes, so all pupils are distinguished. If fewer than six subjects were needed, add arbitrary further subjects to bring the total to six; this cannot destroy a distinction.''','A greedy refinement must be measured by the number of equivalence classes, giving a bound independent of the number of subject coordinates.')
add(2002,5,4.5,'Geometry',['tangents','coordinates','altitudes'],r'In acute triangle $ABC$, the circle with diameter $AB$ meets $AC,BC$ again at $E,F$. Its tangents at $E,F$ meet at $P$. Prove that $P$ lies on the altitude from $C$.',r'''Set $A=(-1,0),B=(1,0),C=(u,v)$, so the diameter circle is the unit circle. The second point of line $AC$ on this circle is $E=A+t(C-A)$, where
$$t=\frac{2(u+1)}{(u+1)^2+v^2}.$$
Consider $P_0=(u,(1-u^2+v^2)/(2v))$. Direct substitution gives $P_0\cdot E=1$, which is the tangent equation at $E$. The analogous computation on line $BC$ gives $P_0\cdot F=1$. Thus $P=P_0$.

Its first coordinate is the same as $C$'s, so $CP$ is perpendicular to horizontal line $AB$.''','The desired altitude is encoded by the first coordinate; the two tangent equations must both be checked.')
add(2003,1,4.5,'Number Theory',['multiplicative functions','monotonicity','powers'],r'Find strictly increasing functions $f:\mathbb N_0\to\mathbb N_0$ with $f(2)=2$ and $f(mn)=f(m)f(n)$.',r'''Only $f(n)=n$ works. Strict increase and $f(2)=2$ force $f(0)=0,f(1)=1$. Multiplicativity gives $f(2^r)=2^r$ and $f(n^k)=f(n)^k$.

Fix $n\ge2$. For each positive $k$, choose $r$ with $2^r\le n^k<2^{r+1}$. Monotonicity then gives $2^r\le f(n)^k<2^{r+1}$. Dividing these bounds shows
$$\frac12<\left(\frac{f(n)}n\right)^k<2.$$
Since this holds for arbitrarily large $k$, the positive ratio must be one. Thus $f(n)=n$ for every $n$.''','Multiplicativity must amplify a possible discrepancy, while monotonicity traps it between consecutive powers of two.')
add(2003,4,6.5,'Combinatorics',['functional iteration','construction','orbits'],r'Does there exist a function $f:\mathbb N_0\to\mathbb N_0$ whose $2003$-fold iterate satisfies $f^{2003}(n)=5n$ for every $n$?',r'''Yes. Every positive integer has a unique form $5^t a$, where $t\ge0$ and $a$ is not divisible by five. List these bases as $a_1,a_2,\ldots$, and partition the list into consecutive groups of $2003$ bases.

Within each group $(b_1,\ldots,b_{2003})$, define
$$f(5^t b_i)=5^t b_{i+1}\quad(i<2003),\qquad f(5^t b_{2003})=5^{t+1}b_1.$$
Set $f(0)=0$. These rules define the function on every nonnegative integer exactly once. During $2003$ steps each starting point makes one full circuit of its group and increases its exponent of five by one. Therefore $f^{2003}(n)=5n$.''','The iteration requires interleaving countably many multiplication-by-five chains into blocks of 2003, rather than taking an ordinary numerical root.')
add(2004,5,4,'Number Theory',['digit permutations','modular arithmetic','construction'],r'A positive integer contains each of the decimal digits $1,3,7,9$. Prove that its digits can be rearranged to form a multiple of $7$.',r'''Reserve one occurrence of each of $1,3,7,9$ for the last four positions. Arrange all remaining digits as a prefix, choosing a nonzero first digit if one is available; leading zeros, if unavoidable, do not affect the resulting integer.

The seven permutations
$$1379,\ 1793,\ 3719,\ 1739,\ 1397,\ 1937,\ 1973$$
have residues $0,1,2,3,4,5,6$ modulo $7$, respectively. Whatever the prefix contributes after multiplication by $10^4$, select the suffix with the opposite residue. The resulting number is divisible by seven and uses exactly the supplied digits. If the remaining digits are all zeros, put these zeros between the first and remaining digits of a suitable reserved permutation instead; equivalently append all zeros to $1379$, which already is divisible by seven.''','A small reserved digit set supplies every residue class, allowing arbitrary remaining digits to be accommodated.')
add(2005,2,4.5,'Algebra',['polynomial roots','closure properties','construction'],r'A set $S$ of integers contains $0,1000$ and contains every integer root of every nonzero polynomial with coefficients in $S$. Prove that $-2\in S$.',r'''The polynomial $1000x+1000$ has coefficients in $S$ and integer root $-1$, so $-1\in S$. We may now use any polynomial whose coefficients are $0,-1,1000$.

In particular,
$$P(x)=1000-x^{10}-x^5-x^4-x^3$$
has all coefficients in $S$, and
$$P(-2)=1000-1024+32-16+8=0.$$
The closure assumption therefore gives $-2\in S$.''','One root first enlarges the available coefficient set; a signed-base representation then supplies a polynomial with the desired new root.')
add(2005,5,4.5,'Combinatorics',['matchings','augmenting paths','graphs'],r'Eight animal species must be paired into four cages. Each species is incompatible with at most three others. Prove that a pairing into compatible pairs exists.',r'''Join compatible species by edges. Every vertex has degree at least four. Choose a matching with as many edges as possible. If it is not perfect, choose two unmatched vertices $u,v$. They are not adjacent, and all their neighbours are matched, since otherwise one edge could be added.

For each matched edge $ab$, there can be at most two edges from $\{u,v\}$ to $\{a,b\}$. If there were three, one could replace $ab$ by two disjoint edges joining $u$ and $v$ to its endpoints, enlarging the matching. There are at most three matched edges, so $\deg(u)+\deg(v)\le6$, contradicting the lower bound eight. The matching is therefore perfect.''','A maximal matching alone is insufficient; a two-edge augmentation turns the degree condition into a contradiction.')
add(2005,6,4.5,'Algebra',['superadditivity','powers','bounding'],r'Let $f:\mathbb Z\to\mathbb Z$ satisfy $f(ab)\ge f(a)+f(b)$ for nonzero integers $a,b$. Prove that $f(a^n)=nf(a)$ for all nonzero $a$ and positive $n$ if and only if $f(a^2)=2f(a)$ for every nonzero $a$.',r'''Necessity is immediate. For sufficiency, fix a nonzero $a$. Repeated application of the given inequality gives $f(a^n)\ge nf(a)$. The assumed equality for squares, applied repeatedly to $a,a^2,a^4,\ldots$, gives $f(a^{2^k})=2^k f(a)$.

Choose $2^k>n$. Superadditivity and the lower bound at exponent $2^k-n$ give
$$2^k f(a)=f(a^{2^k})\ge f(a^n)+f(a^{2^k-n})\ge f(a^n)+(2^k-n)f(a).$$
Hence $f(a^n)\le nf(a)$, proving equality.''','Equality on powers of two must be used to bound arbitrary exponents from above, complementing the immediate lower bound.')
add(2006,2,4.5,'Number Theory',['rational root theorem','symmetric polynomials','integer ratios'],r'For nonzero integers $a,b,c$, both $a/b+b/c+c/a$ and $b/a+c/b+a/c$ are integers. Determine their possible values.',r'''Write $r=a/b,s=b/c,t=c/a$, so $rst=1$. The two given integers are $U=r+s+t$ and $V=rs+st+tr$. Thus $r,s,t$ are rational roots of the monic integer polynomial
$$X^3-UX^2+VX-1.$$
The rational root theorem makes each an integer divisor of one, hence each is $1$ or $-1$. Since their product is one, either all are one or exactly two are negative. The two sums are accordingly $(U,V)=(3,3)$ or $(-1,-1)$. Both occur, for example with $(a,b,c)=(1,1,1)$ and $(1,-1,1)$.''','The two cyclic ratios become the symmetric coefficients of a monic polynomial, allowing integrality to be strengthened to ±1.')
add(2007,1,4.5,'Number Theory',['digit sums','trailing digits','congruences'],r'Find all $1112$-digit integers $N$ containing a digit $1$ such that the digit sums of both $N$ and $N+1$ are divisible by $2000$.',r'''Let $r$ be the number of trailing nines and $s$ the digit sum of $N$. Addition of one changes the sum to $s+1-9r$. Hence $9r\equiv1\pmod{2000}$. Since $0\le r\le1111$, this forces $r=889$.

These trailing nines already contribute $8001$ to $s$, while $s\le9\cdot1112=10008$. The only possible multiple of $2000$ is therefore $s=10000$. The preceding $223$ digits have sum $1999$, eight below their maximum $2007$. Since one digit is $1$, that single digit accounts for the entire deficit; every other digit is $9$. The digit immediately before the trailing nines must not be nine, so it is the one.

Thus $N$ consists of $222$ nines, then $1$, then $889$ nines. Its digit sums before and after adding one are $10000$ and $2000$, so it works.''','Trailing-nine arithmetic gives a modular constraint, then a near-maximum digit-sum argument fixes every digit.')
add(2007,3,4.5,'Combinatorics',['graphs','longest paths','cycles'],r'In a finite graph, every vertex has degree three. Prove that the graph contains a closed route using no edge twice whose length is not divisible by three.',r'''Take a longest simple path $v_0,v_1,\ldots,v_k$. Every neighbour of $v_k$ lies on this path, since otherwise the path could be extended. Besides $v_{k-1}$, let two neighbours be $v_i,v_j$ with $i<j<k-1$.

If either cycle formed by the path segment from $v_i$ or $v_j$ to $v_k$ and the closing edge has length not divisible by three, we are done. Otherwise their lengths $k-i+1$ and $k-j+1$ are both divisible by three, so $j-i$ is divisible by three. But the path from $v_i$ to $v_j$, followed by the two edges through $v_k$ back to $v_i$, is a cycle of length $j-i+2$, not divisible by three.''','The endpoint of a longest path creates three related cycles whose lengths cannot all be multiples of three.')
add(2008,6,4.5,'Number Theory',['digit sums','Euler theorem','construction'],r'For every positive integer $n$, prove that some positive multiple of $n$ has decimal digit sum exactly $n$.',r'''Write $n=2^a5^b k$ with $\gcd(k,10)=1$. Choose $L>0$ such that $10^L\equiv1\pmod k$; Euler's theorem supplies one when $k>1$, and for $k=1$ any $L$ works. Let $t\ge\max(a,b)$ and set
$$m=10^t(1+10^L+10^{2L}+\cdots+10^{(n-1)L}).$$
There are precisely $n$ digits equal to one, in distinct positions, so the digit sum is $n$. The initial factor supplies divisibility by $2^a5^b$. Modulo $k$, the sum in brackets is congruent to $n$, hence zero. Thus $n\mid m$.''','The construction separates the factors 2 and 5 from the coprime part and spaces out ones to control both divisibility and digit sum.')
add(2009,3,4,'Number Theory',['fractional parts','rational approximation','Archimedean argument'],r'A real $x$ has, for every positive integer $q$, an integer $p$ with $|x-p/q|<1/(3q)$. Prove that $x$ is an integer.',r'''The condition means that every multiple $qx$ lies within distance $1/3$ of an integer. From $q=1$, write $x=m+\varepsilon$ with integer $m$ and $|\varepsilon|<1/3$. If $\varepsilon\ne0$, put $\delta=|\varepsilon|$ and choose $q=\lceil1/(3\delta)\rceil$. Then
$$\frac13\le q\delta<\frac13+\delta<\frac23.$$
Thus $qx$ is at distance at least $1/3$ from every integer, a contradiction. Hence $\varepsilon=0$.''','A carefully chosen denominator amplifies a small nonzero fractional part into the forbidden middle third.')
add(2009,4,4.5,'Combinatorics',['edge colouring','round-robin construction','modular arithmetic'],r'Each of $n\ge2$ children has a coloured hat, and each pair holds a coloured ribbon. At each child, all incident ribbon colours and that hat colour must differ. What is the minimum total number of colours?',r'''At least $n$ colours are required at any one child. For odd $n$, label children by residues modulo $n$, colour ribbon $ij$ by $i+j\pmod n$, and give child $i$ hat colour $2i$. Its incident ribbons have all colours except $2i$, so this uses exactly $n$.

For even $n$, construct an edge colouring of the complete graph using $n-1$ colours by the usual round-robin arrangement: label one vertex $\infty$ and the others modulo the odd integer $n-1$. For each $c$, colour the edge $\infty c$ and the pairs $c-t,c+t$ by colour $c$. These form a perfect matching, and every edge appears exactly once. Give every hat one new colour. Again the total is $n$, which is optimal.''','Both parity cases need explicit colour constructions, with the even case requiring a one-factorization of a complete graph.')
add(2009,5,6.5,'Algebra',['functional equations','minimal counterexample','support'],r'Find all $f:\mathbb N_0\to\mathbb N_0$ with $f(0)=0$ and $f(x^2-y^2)=f(x)f(y)$ whenever integers $x>y\ge0$.',r'''Besides the zero function, the solutions have exactly one nonzero value: choose any $k\equiv2\pmod4$ and any positive integer $c$, set $f(k)=c$, and set $f(n)=0$ elsewhere.

First $y=0$ gives $f(x^2)=0$. We show by induction that $f(n)=0$ whenever $n\not\equiv2\pmod4$. For odd $n>1$, write $n=((n+1)/2)^2-((n-1)/2)^2$. One of the two smaller arguments is odd, so its value is zero by induction; the case $n=1$ was already covered by squares. For $n=4r$, write $n=(r+1)^2-(r-1)^2$ when $r\ge1$. If $r$ is even both arguments are odd; if $r$ is odd, one is divisible by four. The smaller-index induction applies (and $n=4$ is a square). Thus these values also vanish.

If two distinct indices $u>v$, both congruent to two modulo four, had positive values, their squared difference would be divisible by sixteen, giving $0=f(u)f(v)>0$. Hence at most one nonzero value exists. Conversely a difference of two squares is never two modulo four, and two distinct inputs cannot both be that single supported index. Each proposed function therefore satisfies the equation.''','The equation permits exceptional nonzero functions; a congruence-sensitive induction and support argument are needed for a complete classification.')
add(2009,6,4,'Geometry',['polar lines','coordinates','tangents'],r'Chords $CD,EF$ of a circle with centre $O$ meet at $N$. The tangents at $C,D$ meet at $A$, and those at $E,F$ meet at $B$. Prove $ON\perp AB$.',r'''Use $O$ as origin and radius $R$. A tangent at point $C$ on the circle has equation $X\cdot C=R^2$. Since $A$ lies on the tangents at both $C,D$, we have $A\cdot C=A\cdot D=R^2$. Every point of line $CD$, in particular $N$, therefore satisfies $A\cdot N=R^2$.

Similarly $B\cdot N=R^2$. Subtraction yields $(A-B)\cdot N=0$, so $AB$ is perpendicular to $ON$.''','The two pairs of tangents encode the same linear equation at the chord intersection; this is the elementary coordinate form of polar duality.')
add(2010,1,4,'Combinatorics',['prime sums','pairings','extremal bounds'],r'(a) Pair $1,\ldots,10$ so that the five sums are distinct primes. (b) Can $1,\ldots,20$ be paired with ten distinct prime sums?',r'''For (a), use $(2,3),(1,6),(4,7),(5,8),(9,10)$, whose sums are $5,7,11,13,19$.

For (b), every pair sum is at most $39$, and no pair of distinct positive integers has sum $2$. The available primes are therefore among
$$3,5,7,11,13,17,19,23,29,31,37,$$
whose total is $195$. Even the sum of all eleven is less than $1+2+\cdots+20=210$. Ten distinct prime pair sums cannot have the required total, so no pairing exists.''','An explicit small matching must be paired with a global total-sum obstruction for the larger set.')
add(2010,6,4.5,'Algebra',['functional equations','integer domain','additivity'],r'Does a function $f:\mathbb Z\to\mathbb Z$ exist with $f(x+f(y))=f(x)-y$ for every pair of integers?',r'''No. Put $c=f(0)$. Taking $x=0$ gives $f(f(y))=c-y$, making $f$ injective and surjective. Taking $y=0$ gives $f(x+c)=f(x)$, so injectivity implies $c=0$.

Now $f(f(y))=-y$, and the original identity becomes $f(x+f(y))=f(x)+f(f(y))$. Since $f$ is surjective, this is additivity $f(x+z)=f(x)+f(z)$ for all integers. Hence $f(n)=nf(1)$. But $f(f(1))=-1$ would then say $f(1)^2=-1$, impossible for an integer.''','Nested substitutions first force bijectivity, then reveal additivity and an impossible integer square root of -1.')
add(2012,2,4,'Number Theory',['divisibility','exponential bounds','case analysis'],r'Find positive integers $m,n$ for which the nonzero integer $n^m-m$ divides $m^2+2m$.',r'''The solutions $(m,n)$ are
$$(1,2),(1,4),(2,1),(2,2),(3,2),(4,1),(4,2).$$
For $n=1$, reduction modulo $m-1$ gives $m-1\mid3$, yielding $m=2,4$; $m=1$ would give divisor zero. For $m=1$, we need $n-1\mid3$, giving $n=2,4$. For $m=2$, $n^2-2\mid8$ leaves $n=1,2$.

For $m\ge3,n\ge3$, the bound $n^m-m\ge3^m-m>m^2+2m$ rules out divisibility; the inequality begins at $m=3$ and persists by induction. For $n=2$, direct checks at $m=3,4,5$ give the first two only. At $m=6$ and thereafter, $2^m-m>m^2+2m$, again by induction. These cover every case.''','The small bases and exponents must be separated before exponential growth supplies a uniform finite bound.')
add(2013,1,4,'Number Theory',['prime valuations','difference of squares','construction'],r'If $n(n+2013)$ is a square for positive integer $n$, prove that $n$ is not prime, and exhibit one possible $n$.',r'''If $n=p$ were prime, the exponent of $p$ in the product would be odd unless $p\mid2013$. Thus $p\in\{3,11,61\}$. In each case the quotient $(p+2013)/p$ would need to be a square, but its values are $672,184,34$, none of which is square.

For an example, note that $1007^2-1006^2=2013$. Hence $n=1006^2$ gives $n+2013=1007^2$, so their product is $(1006\cdot1007)^2$.''','Prime exponents reduce the impossibility claim to divisors of 2013, while consecutive squares provide a separate existence construction.')
add(2013,2,4.5,'Algebra',['functional equations','associativity','affine functions'],r'Find all $f:\mathbb R\to\mathbb R$ satisfying $f(x)f(y)+f(x+y)=xy$ for all real $x,y$.',r'''The solutions are $f(x)=x-1$ and $f(x)=-x-1$. Taking $y=0$ gives $f(x)(f(0)+1)=0$. The zero function fails the original equation, so $f(0)=-1$.

Evaluate $f(x+y+z)$ first by grouping $x+y$ and $z$, then by grouping $x$ and $y+z$. Substituting the original identity and cancelling gives
$$xy(1+f(z))=yz(1+f(x)).$$
Set $y=z=1$. Then $f(x)+1=x(f(1)+1)$, so $f(x)=cx-1$ for some real $c$. Substitution into the original equation forces $c^2=1$. Both resulting functions satisfy it.''','Associativity of addition supplies a new three-variable identity that forces the function to be affine.')
add(2015,4,4,'Number Theory',['odd parts','bijections','sums'],r'Let $d(k)$ be the greatest odd divisor of $k$. Evaluate $d(1008)+d(1009)+\cdots+d(2015)$.',r'''Every odd integer $u$ with $1\le u\le2015$ has exactly one power-of-two multiple in $[1008,2015]$: repeatedly double $u$ until it first reaches at least $1008$; that value is at most $2015$, and doubling it again leaves the interval.

Thus the odd parts of the integers in this interval are exactly $1,3,5,\ldots,2015$, each once. Their sum is the sum of the first $1008$ odd integers, namely $1008^2=1016064$.''','A dyadic scaling bijection replaces the irregular odd-divisor sum by consecutive odd integers.')
add(2016,3,4.5,'Number Theory',['polynomial values','gcd','prime valuations'],r'For positive integers $n$, let $P(n)=n\prod_{j=1}^{16}(jn+1)$. Find $\gcd(P(1),P(2),\ldots,P(2016))$.',r'''The answer is the product of the primes at most seventeen:
$$2\cdot3\cdot5\cdot7\cdot11\cdot13\cdot17=510510.$$
For such a prime $p$, if $p\mid n$ then $p\mid P(n)$. Otherwise $n$ is invertible modulo $p$, and the congruence $jn+1\equiv0\pmod p$ has a solution $1\le j\le p-1\le16$. Thus every listed prime divides every $P(n)$.

No larger prime can divide the gcd, since $P(1)=17!$. For each listed prime $p$, take $n=p$, which is among the permitted inputs. All factors $jp+1$ are coprime to $p$, so $P(p)$ contains only one factor of $p$. Hence the gcd is exactly the stated squarefree product.''','Universal divisibility is shown by inverses modulo each small prime, while strategically chosen inputs prove every exponent is sharp.')
add(2017,3,5,'Number Theory',['difference of squares','divisor counting','coprime factors'],r'For positive integer $n$, count positive integer pairs $(x,y)$ with $x^2-y^2=100\cdot30^{2n}$, and prove that this count is never a square.',r'''The integers $x,y$ have the same parity, so write $x-y=2u,x+y=2v$ with positive $u<v$. Then
$$uv=25\cdot30^{2n}=2^{2n}3^{2n}5^{2n+2}.$$
This is a square and has $(2n+1)^2(2n+3)$ divisors. Its unequal factor pairs number
$$\frac{(2n+1)^2(2n+3)-1}{2}=(n+1)(4n^2+6n+1).$$
The two factors on the right are coprime, since the second is congruent to $-1$ modulo $n+1$. If the count were square, each factor would be square. But
$$(2n+1)^2<4n^2+6n+1<(2n+2)^2$$
for $n>0$, a contradiction.''','Divisor-pair counting must be followed by an unexpected coprime factorization to rule out a square count.')
add(2018,1,5,'Algebra',['functional equations','integer domain','exceptional solutions'],r'Find all $f:\mathbb Z\to\mathbb Z$ satisfying $f(x+y)^2=f(x^2)+f(y^2)$ for every pair of integers.',r'''Either $f$ is zero everywhere, or $f$ takes values in $\{-2,2\}$ and is $2$ at every nonnegative perfect square; values at all other integers may be chosen independently.

Let $c=f(0)$. Setting $x=y=0$ gives $c^2=2c$, so $c=0$ or $2$. Taking $y=-x$ gives $2f(x^2)=c^2$, hence $f(x^2)=c$. Taking $y=0$ then gives $f(x)^2=2c$ for every integer $x$.

If $c=0$, this forces $f\equiv0$. If $c=2$, it forces every value to be $\pm2$, with square inputs equal to $2$. Conversely any such choice gives left side $4$ and right side $2+2$, so all these functions work.''','The full classification contains freely chosen signs; it is necessary to distinguish square inputs from arbitrary integers and verify the exceptional family.')
add(2018,2,4,'Combinatorics',['tournaments','counting','divisibility'],r'A round-robin chess tournament has twice as many girls as boys, with no draws. Girls win $7/9$ as many games as boys. How many players are there?',r'''Let there be $b$ boys and $2b$ girls. The total number of games is $3b(3b-1)/2$, so the girls win $21b(3b-1)/32$ games. They win at least the $\binom{2b}{2}=b(2b-1)$ games played between girls. Comparing gives $b\le11$.

Integrality requires $32\mid b(3b-1)$. Among $1\le b\le11$, the only possibility is $b=11$: for odd $b$, one needs $3b\equiv1\pmod{32}$, giving $b\equiv11$; for even $b$, the odd factor $3b-1$ requires $32\mid b$, impossible in this range. Thus there are $33$ players. This is achievable by letting every boy beat every girl: the girls' $231$ internal wins and the boys' $55+242=297$ wins have ratio $7:9$.''','The gender counts alone do not determine the answer; a minimum-win bound and an integrality constraint must be combined.')
add(2018,3,5,'Number Theory',['recurrences','2-adic valuation','explicit orbits'],r'Let $g(x)$ be the largest odd divisor of $x$, and set $F(x)=x/2+x/g(x)$ for even $x$, while $F(x)=2^{(x+1)/2}$ for odd $x$. Starting at $x_1=1$, iterate $x_{n+1}=F(x_n)$. Prove that $2018$ occurs, find its first index, and decide whether it occurs again.',r'''For $x=2^k u$ with $u$ odd and $k\ge1$, the even rule is $F(x)=2^{k-1}(u+2)$. Therefore the orbit runs through blocks
$$2r-1\ \longrightarrow\ 2^r\ \longrightarrow\ 3\cdot2^{r-1}\ \longrightarrow\ 5\cdot2^{r-2}\ \longrightarrow\cdots\longrightarrow\ (2r-1)2\ \longrightarrow\ 2r+1.$$
The odd number $2r-1$ occurs at index $r(r+1)/2$, since the preceding block lengths are $2,3,\ldots,r$.

The number $2018=2\cdot1009$ has 2-adic valuation one, so it can only be the penultimate term of the block with $2r-1=1009$, namely $r=505$. Its index is
$$\frac{505\cdot506}{2}+505=128270.$$
Its odd part and 2-adic valuation determine this block uniquely, so it occurs exactly once.''','Factoring out powers of two exposes a block structure; tracking both block lengths and the unique valuation locates the desired term exactly.')
add(2018,5,4.5,'Algebra',['substitution','reciprocal inequalities','sharp bounds'],r'Nonzero pairwise distinct reals $a,b,c,d$ satisfy $a/b+b/c+c/d+d/a=4$ and $ac=bd$. Prove $a/c+b/d+c/a+d/b\le-12$, and show the bound is attained.',r'''Put $r=a/b$ and $s=b/c$. The condition $ac=bd$ makes $c/d=1/r,d/a=1/s$. Write $U=r+1/r,V=s+1/s$. Then $U+V=4$, while the required expression is $UV$.

For a nonzero real $r$, either $r+1/r\ge2$ or $r+1/r\le-2$. If $U,V$ were both at least two, they would both equal two, forcing $r=s=1$ and all four original numbers equal. Both cannot be negative. Thus one is at most $-2$ and the other is at least $6$. Under $U+V=4$, their product is at most $-12$.

Equality occurs with $r=-1,s=3+2\sqrt2$. For example take $b=1,a=-1,c=1/s,d=-1/s$. These four numbers are nonzero and distinct and meet all conditions.''','The multiplicative constraint turns the target into a product of two reciprocal sums; excluding the all-positive equality branch is essential.')
add(2019,2,4.5,'Number Theory',['prime products','factorization','bounding'],r'A collection of primes, with repetition allowed, has product equal to ten times its sum. Determine the collection.',r'''The product is divisible by ten, so remove one $2$ and one $5$. If the remaining primes are $q_1,\ldots,q_r$, their product must satisfy
$$q_1\cdots q_r-(q_1+\cdots+q_r)=7.$$
There must be at least two remaining primes. For $r=2$, the equation is $(q_1-1)(q_2-1)=8$, giving $q_1,q_2=3,5$ in some order.

For $r=3$, if at least two primes are at least three, the difference is at least $2\cdot3\cdot3-(2+3+3)=10$; if two are two, it is $3q-4$, never seven. For $r\ge4$, the difference is at least $2^r-2r\ge8$, since increasing any factor increases product-minus-sum. Therefore the only collection is $2,3,5,5$, which directly works.''','Removing the forced factors 2 and 5 reveals a product-minus-sum equation; monotonicity bounds the possible number of remaining primes.')
add(2019,3,4,'Geometry',['vectors','circumcentres','equal ratios'],r'Points $D,E,F$ lie inside $BC,CA,AB$, with $BD/DC=CE/EA=AF/FB$. If triangles $DEF$ and $ABC$ have the same circumcentre, prove that $ABC$ is equilateral.',r'''Use the common centre as origin and scale the outer radius to one. A common parameter $0<t<1$ gives
$$D=(1-t)B+tC,\quad E=(1-t)C+tA,\quad F=(1-t)A+tB.$$
Since $|A|=|B|=|C|=1$,
$$|D|^2=1-t(1-t)|B-C|^2,$$
and similarly for $E,F$. Their equal distances from the common centre therefore force $|B-C|=|C-A|=|A-B|$. Thus the triangle is equilateral.''','The shared division ratio gives identical quadratic distance formulas; equal inner radii then force equal outer chords.')
add(2019,6,5,'Number Theory',['binomial valuations','base representation','ranking'],r'Find the $2019$th positive integer $n$ for which $5$ does not divide $\binom{2n}{n}$.',r'''The exponent of five in $\binom{2n}{n}$ is
$$\sum_{j\ge1}\left(\left\lfloor\frac{2n}{5^j}\right\rfloor-2\left\lfloor\frac n{5^j}\right\rfloor\right),$$
which counts carries when adding $n+n$ in base five. Thus it is zero exactly when every base-five digit of $n$ is $0,1,$ or $2$.

These admissible positive integers, in increasing order, are obtained by writing the positive integers in base three and reading the same digit strings in base five. Since $2019=(2202210)_3$, the answer is
$$ (2202210)_5=2\cdot5^6+2\cdot5^5+2\cdot5^3+2\cdot5^2+5=37805.$$''','A binomial valuation must be interpreted as a carry condition, and the resulting digit language ranked by changing bases.')
add(2021,3,4.5,'Number Theory',['smallest prime factor','recurrences','eventual cycles'],r'Let $a_1\ge2$, let $p_n$ be the smallest prime divisor of $a_n$, and define $a_{n+1}=a_n+a_n/p_n$. Prove that eventually $a_{n+3}=3a_n$ at every index.',r'''For an even term $a$, the next term is $3a/2$. For an odd term, its smallest prime divisor is odd, so $a(p+1)/p$ is even. Consequently the sequence soon contains an even term, whose successor is divisible by three.

Repeated even steps reduce the exponent of two until an odd term divisible by three is reached. From any such term $u$, the next three terms are
$$u\longrightarrow\frac{4u}{3}\longrightarrow2u\longrightarrow3u.$$
The final term is again odd and divisible by three, so this pattern repeats forever. Each of the three phase subsequences is multiplied by three from one block to the next, giving $a_{n+3}=3a_n$ at every sufficiently large index.''','The dynamics must first be brought into an odd multiple of three; then a stable three-phase pattern emerges.')
add(2021,5,4,'Algebra',['functional equations','squares','contradiction'],r'Find all $f:\mathbb R\to\mathbb R$ satisfying $(f(x)+y)(f(y)+x)=f(x^2)+f(y^2)+2f(xy)$ for every real $x,y$.',r'''The only solution is $f(x)=x$. Put $c=f(0)$. The case $x=y=0$ gives $c^2=4c$, so $c=0$ or $4$. The case $y=0$ gives $f(x^2)=(c+x)f(x)-3c$, while the case $y=x$ gives $(f(x)+x)^2=4f(x^2)$. Eliminating $f(x^2)$ yields
$$(f(x)-x)^2-4cf(x)+12c=0.$$
If $c=0$, this says $f(x)=x$. If $c=4$, take $x=-4$; the equation becomes $(f(-4)-4)^2+48=0$, impossible over the reals. Finally the identity function satisfies the original equation.''','Two specializations create a universal square identity; a carefully chosen negative input rules out the nonzero constant term.')
# Individually worked routine exclusions, below the chosen band.
low={
2000:{1:(3,'Elementary trigonometric factorization.'),2:(3,'Compose the shifts and expand the single translated cubic.'),4:(3.5,'Subtract the two cone equations and use equality in Cauchy–Schwarz.')},
2001:{1:(3,'Polynomial division bounds n before a short check.'),4:(2.5,'Each summand is at most a squared, with equality only at the endpoints.'),5:(2.5,'Group floor square roots between consecutive squares.')},
2002:{1:(2.5,'The attained minimum starts an induction forcing f(n)=n+1.'),2:(3.5,'Equating two squared distances produces a fixed linear centre condition.'),3:(3.5,'Prepending either 1 or 2 preserves the old power of two and selects the next parity.'),6:(3.5,'Expand the squared sum and bound each cross term using monotonicity.')},
2003:{2:(3,'Opposite midpoint arcs sum to a straight angle, making the two diagonals perpendicular.'),3:(2,'Already the first base-b number factors as (b squared+b+1)(b squared-b+1).'),5:(3,'Reduce separately modulo three and seven.'),6:(3,'Subtract the y=0 identities to force an affine function.')},
2004:{1:(3,'Cubic residues modulo nine rule out every residue of n.'),2:(2,'Both nested radicals are elementary quadratic surds that cancel.'),3:(3,'The window condition forces period gcd(268,20)=4.'),4:(2.5,'Subtracting the sum-of-squares identity gives z(z+x+y)=0 and a discriminant obstruction.')},
2005:{1:(2.5,'Two standard Cauchy–Schwarz or reciprocal-pair inequalities.'),3:(3,'Area is proportional to the product of two side fractions.'),4:(3,'Writing x as integer plus fractional part leaves only integer parts zero and -1.')},
2006:{1:(3.5,'Direct unit-circle coordinate calculation.'),3:(3.5,'The rational expression simplifies to a+b+c.'),4:(2.5,'Count multiples of each power of two.'),5:(3.5,'Count proper three-colourings of a path, remove two-colourings, then divide by six.')},
2007:{2:(3,'A fixed rotation and dilation maps the moving line to another line.'),4:(2.5,'Monotonicity or maximum/minimum bounds force x=y=z=3.'),5:(3,'Modulo 9 and 223 both conditions reduce to n being odd.')},
2008:{1:(3,'The inputs zero and opposite numbers force f(x)=x.'),4:(2,'The difference factors as (x-y)(x to n+1-y to n+1).')},
2009:{1:(2.5,'The desired sum would require an odd number of negative neighbouring products, contradicting their total product one.')},
2010:{2:(3,'Every valid ordering decreases to its minimum and then increases, so choose the left subset.'),4:(3.5,'The relative vertex offsets form a twelfth-circle lattice.'),5:(3,'Every multiplication by nine is followed by digit deletion, decreasing the original number.')},
2012:{3:(3.5,'Set x=k+t and solve the resulting single quadratic inequality for 0<=t<1.'),4:(2,'The product of one plus each entry is invariant and telescopes.'),5:(3.5,'Oddness and the substitutions x and -x force linearity.')},
2013:{6:(3.5,'Three positive gaps and AM–HM force equality in both inequalities.')},
2015:{1:(2.5,'Cauchy gives nine, and its equality equations are inconsistent.'),3:(3.5,'Two of the 2048 subset sums coincide modulo 2015.'),5:(3.5,'The final total is 127 exactly when the last card is one of the five larger cards, with probability 5/7.')},
2016:{2:(3,'After t moves there are t+1 piles and 2016-t cards, giving an impossible congruence.')},
2017:{1:(2.5,'Solve x_n=2 to n-1 and complete the square.'),4:(3.5,'The integer part lies in 1..4, leaving a short half-unit case analysis.'),5:(3,'Only the parity of the count coprime to 30 matters.')},
2018:{4:(3,'Cyclic-angle equality and the two perpendicular lines directly give the equivalence.')},
2019:{1:(3,'The recurrence has the explicit positive integer solution 2 to n times (2+(-1) to n).')}
}
for y,qs in low.items():
 for n,(d,r) in qs.items():skip(y,n,d,r)
