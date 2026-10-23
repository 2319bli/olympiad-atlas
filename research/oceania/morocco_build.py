import json
P='/workspace/sites/olympiad-atlas/research/oceania/'
URL='https://drive.google.com/file/d/1UWNoKcRrODCCpwoCBu4mUvtO83cRVb_B/view'
items=[];ledger=[]
def meta(y,sec,n):
 return dict(id=f'mar_{y}_{sec.lower().replace(" ","_")}_{n}',country='Morocco',competition='Moroccan National Olympiad Programme — '+('Team Selection Test' if sec=='TST' else 'National Camp Contest'),year=y,section=sec,number=str(n),sourceUrl=URL)
def add(y,sec,n,d,t,tags,s,sol,r):
 m=meta(y,sec,n)
 items.append(dict(**m,statement=s,solution=sol,solutionUrl=URL,topic=t,tags=tags,difficulty=d,ratingReason=r,reviewStatus='individually-assessed',solutionKind='original-exposition',notes='Primary Math&Maroc 2024/2025 preparation report, National Contest chapter. This is provenance for the Moroccan test use, not a claim that the problem was first invented there. English statement paraphrase and independently written proof.'))
 ledger.append(dict(**m,difficulty=d,status='reviewed',included=True,reason=r))
def skip(y,sec,n,d,r):ledger.append(dict(**meta(y,sec,n),difficulty=d,status='reviewed' if d is not None else 'pending-solution-review',included=False,reason=r))
add(2024,'December',1,4,'Geometry',['cyclic quadrilaterals','angle chasing','midpoints'],r'Let $ABC$ be acute with $AB<AC$. Let $D$ be the midpoint of $AC$, let $E$ be the foot of the altitude from $A$, and put $F=AB\cap DE$. On arc $BC$ of the circumcircle not containing $A$, choose $H$ with $\angle BHE=\angle ABC$. Prove that $BH\perp HF$.',r'''Write the angles at $B,C$ as $\beta,\gamma$. Because $D$ is the midpoint of the hypotenuse of right triangle $AEC$, we have $DA=DC=DE$. Angle chasing in these isosceles triangles gives $\angle EFA=\beta-\gamma$. The given condition and the cyclic quadrilateral $ABHC$ give $\angle EHA=\beta-\gamma$ as well. Consequently $A,E,H,F$ are concyclic.

Now $\angle AHF=\angle AEF=90^\circ+\gamma$, while $\angle AHB=\gamma$. Subtracting gives $\angle BHF=90^\circ$. These equalities can equivalently be read as directed-angle equalities modulo $180^\circ$.''','The midpoint of a right-triangle hypotenuse reveals a useful angle; a second, initially hidden cyclic quadrilateral completes the proof.')
add(2024,'December',2,6,'Algebra',['functional equations','positive rationals','injectivity'],r'Find all functions $f:\mathbb Q_{>0}\to\mathbb Q_{>0}$ for which some rational $\alpha>0$ satisfies $$f(x/y+y)=f(x)/f(y)+f(y)+\alpha x$$ for every positive rational $x,y$.',r'''The solution is $f(x)=x^2$, with $\alpha=2$.

Replacing $x$ by $xy$ gives
$$f(x+y)=\frac{f(xy)}{f(y)}+f(y)+\alpha xy.\tag{1}$$
Put $c=f(1)$. Comparing (1) at $(x,1)$ and $(1,x)$ yields $(1-c)(f(x)-c)=0$. If $c\ne1$, $f$ is constant, impossible in the original equation as $x$ varies. Thus $c=1$, and induction gives $f(n)=n+\alpha n(n-1)/2$ for integers $n\ge1$. Also $f(t)>\alpha(t-1)$ for $t>1$.

To prove injectivity, suppose $f(a)=f(b)$ with $a>b$. The original equation gives
$$f(t)=f\left(\frac ab(t-a)+b\right)\qquad(t>a).$$
The affine map on the right has fixed point $a+b$ and slope $a/b>1$. Starting at $t_0=a+b+1$ and iterating therefore gives $t_m\to\infty$ with $f(t_m)=f(t_0)$, contradicting the preceding lower bound. Hence $f$ is injective.

Symmetry of (1) now gives $f(xy)=f(x)f(y)$ whenever $x\ne y$. In particular $f(6)=f(2)f(3)$ gives
$$6+15\alpha=(2+\alpha)(3+3\alpha),$$
so $\alpha=2$. Thus $f(n)=n^2$ on the positive integers. For a nonintegral rational $x=p/q$, multiplicativity with the integer $q\ne x$ gives $p^2=f(qx)=q^2f(x)$, proving $f(x)=x^2$ everywhere. Direct substitution verifies the result.''','The main obstacle is proving injectivity without regularity; an expanding affine orbit and positivity supply it, after which multiplicativity determines the function.')
skip(2024,'December',3,3,'Each of15 four-member viewing sets contains4 triples. Since60>35, two films share a triple. Fifteen distinct4-subsets of7 show that sharing all4 is not forced. Thus k=3.')
add(2024,'December',4,6.5,'Number Theory',['perfect powers','prime factors','descent'],r'Find all composite integers $n>1$ such that every divisor $d>1$ of $n$ can be written $d=a^r+1$, where $a$ is a positive integer and $r>1$ is an integer.',r'''The only answer is $n=10$.

First every divisor $d>1$ must be one more than a square. Indeed, write $d-1=b^s$ with the exponent $s$ maximal. If $b=1$ this is immediate. Otherwise $b$ is not itself a perfect power, and $s>1$. If $s$ were odd, $b+1$ would divide $d$ and hence $n$. Applying the hypothesis to $b+1$ would make $b$ a perfect power, a contradiction. Thus $s$ is even.

No prime square can divide $n$, since $p^2=x^2+1$ has no positive integer solution. Hence $n$ is squarefree. Choose distinct prime divisors $p>q$, and write $p=x^2+1$, $q=y^2+1$, $pq=z^2+1$. We have $x<z<p$, and
$$p\mid z^2-x^2=(z-x)(z+x).$$
Since $0<z-x<p$ and $0<z+x<2p$, primality forces $z+x=p$. Substitution gives
$$q=\frac{(p-x)^2+1}{p}=(x-1)^2+1.$$
The primes $x^2+1$ and $(x-1)^2+1$ have opposite parity. The smaller must therefore be2, giving $x=2$ and $\{p,q\}=\{5,2\}$. Every pair of distinct prime factors must be this pair, so squarefreeness and compositeness give $n=10$. Its nontrivial divisors are $2=1^2+1$, $5=2^2+1$, and $10=3^2+1$.''','A maximal perfect-power representation first turns every exponent into an even one; squarefreeness and a sharp prime-divisibility interval then force the sole pair of prime factors.')
add(2025,'January',1,6,'Number Theory',['greatest common divisor','Pell equations','sharp bounds'],r'Find the least real constant $c>0$ such that $$\gcd\bigl(n,\lfloor n\sqrt2\rfloor\bigr)\le c\sqrt n$$ for every positive integer $n$.',r'''The least constant is $2^{3/4}$.

Write $d=\gcd(n,\lfloor n\sqrt2\rfloor)$, $n=dr$, and $\lfloor n\sqrt2\rfloor=ds$. The floor inequalities give
$$d^2s^2<2d^2r^2<(ds+1)^2.$$
Since the middle and left expressions are integers, $k=2r^2-s^2$ is a positive integer and $d^2k\le2ds$, hence $d\le2s/k\le2s<2\sqrt2\,r$. Therefore $d^2<2\sqrt2\,dr=2\sqrt2\,n$.

For sharpness, take the unbounded positive solutions $(s,r)$ of $s^2-2r^2=-1$, generated by
$$s+r\sqrt2=(1+\sqrt2)(3+2\sqrt2)^m.$$
Set $n=2sr$. We have
$$2s^2<n\sqrt2<2s^2+1,$$
because the squares of the latter two bounds differ from $2n^2$ by $4s^2$ and1 respectively. Thus $\lfloor n\sqrt2\rfloor=2s^2$. The Pell equation implies $\gcd(s,r)=1$, so the gcd is $2s$. Its ratio to $\sqrt n$ equals $\sqrt{2s/r}$, tending to $2^{3/4}$. No smaller constant works.''','Reparametrizing by the gcd gives the upper bound, but proving optimality requires constructing a Pell sequence and checking the floor and gcd exactly.')
add(2025,'January',2,4.5,'Combinatorics',['pigeonhole principle','colourings','monochromatic rectangles'],r'The positive integers are coloured with finitely many colours. Prove that there are four distinct positive integers $a,b,c,d$ of one colour such that $ad=bc$, $c/a=2024^n$, and $b/a=2025^m$ for some positive integers $n,m$.',r'''Suppose there are $k$ colours, and colour the lattice point $(i,j)$ by the colour of $2024^i2025^j$.

We first find a monochromatic rectangle. Use $k+1$ fixed rows and more than $k^{k+1}$ columns. Two columns have identical colour vectors. In their common vector, two of the $k+1$ entries share a colour; those two rows and columns form the desired rectangle.

Write its coordinates as $i_1<i_2$ and $j_1<j_2$, and set
$$a=2024^{i_1}2025^{j_1},\quad b=2024^{i_1}2025^{j_2},\quad c=2024^{i_2}2025^{j_1},\quad d=2024^{i_2}2025^{j_2}.$$
The four values are distinct because2024 and2025 are coprime and both exceed1. They have one colour and satisfy the required equations with $n=i_2-i_1$ and $m=j_2-j_1$.''','The multiplicative equations become a rectangular grid pattern; two nested pigeonhole arguments produce a monochromatic rectangle with all four entries distinct.')
add(2025,'January',3,6,'Geometry',['radical axis','power of a point','similar triangles'],r'Let $D$ and $E$ lie on the arcs $AB$ and $AC$ of the circumcircle of triangle $ABC$ that avoid $C$ and $B$, respectively. Put $M=DE\cap AB$ and $N=DE\cap AC$. Suppose circles $BDN$ and $CEM$ meet at $X,Y$. Prove that $A,X,Y$ are collinear if and only if $DE\parallel BC$.',r'''Let $B'$ be the second intersection of $AB$ with circle $BDN$, and $C'$ the second intersection of $AC$ with circle $CEM$. Use directed segments throughout.

Cyclic angles show $NB'\parallel AE$ and $MC'\parallel AD$. The corresponding similar triangles give
$$\frac{AB'}{MB'}=\frac{EN}{MN},\qquad \frac{AC'}{NC'}=\frac{DM}{MN}.$$
Taking their quotient and then using the powers of $M$ and $N$ with respect to the two small circles yields
$$\frac{AB'}{AC'}=\frac{MB'\,EN}{NC'\,DM}
=\frac{(MD\,MN/MB)\,EN}{(NE\,NM/NC)\,DM}=\frac{NC}{MB}.$$
Now $A$ lies on the common radical axis $XY$ exactly when
$$AB\cdot AB'=AC\cdot AC',$$
or $AB'/AC'=AC/AB$. Combining the ratio identity gives $NC/AC=MB/AB$, which is precisely the intercept-theorem condition for $MN\parallel BC$.''','Two auxiliary second intersections turn the common radical-axis condition into a length ratio; deriving that ratio requires both parallelisms and two circle powers.')
add(2025,'January',4,6.5,'Algebra',['integer-valued polynomials','modular arithmetic','divisibility'],r'A nonconstant real polynomial $f$ satisfies $$\frac{f(n+1)\cdots f(n+k)}{f(1)\cdots f(k)}\in\mathbb Z$$ for all positive integers $n,k$; in particular all the denominators are nonzero. Prove that $f(0)=0$.',r'''Multiplying $f$ by any nonzero constant leaves the hypothesis unchanged. Normalize $f(1)=1$. The case $k=1$ shows that $f$ takes integer values at every positive integer. Interpolation at $\deg f+1$ positive integers therefore gives rational coefficients. Clearing denominators, we may assume $f\in\mathbb Z[x]$.

Fix $k\ge1$ and put $g(x)=\prod_{j=1}^k f(x+j)$ and $M=g(0)\ne0$. The hypothesis says $M\mid g(n)$ for every positive integer $n$. Choose a positive $n\equiv-1\pmod{|M|}$. Since $g$ has integer coefficients, $g(-1)\equiv g(n)\equiv0\pmod M$. Hence
$$\frac{g(-1)}{M}=\frac{f(0)}{f(k)}\in\mathbb Z.$$
As $k\to\infty$, the nonconstant polynomial has $|f(k)|\to\infty$. The displayed integer tends to0, so it is eventually0; thus $f(0)=0$.''','Normalization and interpolation recover integral coefficients; a negative input is then accessed through positive congruent inputs, forcing an integer quotient to tend to zero.')
add(2025,'TST',1,4.5,'Combinatorics',['strategy games','symmetry','parity'],r'Points $1,2,\ldots,n$, with $n\ge4$, occur consecutively on a circle. Two players alternately draw chords joining labels of the same parity. Drawn chords may neither cross nor share endpoints. The player who makes the last move wins. Determine which player has a winning strategy.',r'''The second player wins exactly when $n\equiv2\pmod4$.

Only cyclic order matters, so arrange relevant points regularly whenever using a symmetry. For $n=4k+2$, the second player answers each chord by its half-turn image. This preserves the same-parity condition, and no legal chord is a diameter, since opposite labels have opposite parity. A chord and its half-turn image are disjoint. The paired position remains invariant, so the response always exists.

For $n=4k$, the first player begins with diameter $(1,2k+1)$, then answers by half-turn symmetry in the two separated semicircles.

For $n=4k+1$, the first player draws $(1,3)$, isolating point2. The remaining $4k-2$ points alternate in parity, and the first player can now act as the second player in the previous $4\ell+2$ strategy.

For $n=4k+3$, the first move is $(2k+1,2k+3)$, isolating $2k+2$. The other $4k$ points, in cyclic order, are $1,\ldots,2k,2k+4,\ldots,4k+3$. Pair corresponding points in these two blocks. Each pair has opposite parity, while the pairing reverses parity on every point. It therefore maps legal chords to legal chords and fixes none. Realize the remaining cyclic order as a regular $4k$-gon; the same half-turn response strategy wins.''','The usual pairing strategy must be adapted to all four residue classes, including an odd case where deleting three points changes the parity pattern.')
add(2025,'TST',2,6.5,'Geometry',['incentres','external angle bisector','coordinates'],r'In a triangle $ABC$ with $AB<AC$, let $I,O,R$ denote the incentre, circumcentre and circumradius. The external bisector of angle $A$ meets line $BC$ at $T$. Let $K$ lie on the perpendicular bisector of $BC$ with $IK\perp IT$. Prove that $OK=3R$.',r'''Scale to $B=(-1,0)$, $C=(1,0)$, and write $A=(u,v)$ with $v>0$. Put $b=AC$, $c=AB$, $q=b+c$, and $d=b-c>0$. The distance equations give
$$u=-\frac{dq}{4},\qquad 16v^2=(q^2-4)(4-d^2).$$
The standard weighted-coordinate formula for the incentre, and the external angle-bisector theorem, give
$$I=\left(-\frac d2,\frac{2v}{q+2}\right),\qquad T=\left(-\frac qd,0\right).$$
Write $I=(i,j)$ and $K=(0,k)$. The perpendicularity condition is
$$(-i,k-j)\mathbin\cdot(-q/d-i,-j)=0,$$
so
$$k=\frac{2v}{q+2}-\frac{(2q-d^2)(q+2)}{8v}.$$
Also $O=(0,o)$, where $o=(u^2+v^2-1)/(2v)=(q^2+d^2-8)/(8v)$. Substitution of the expression for $v^2$ simplifies the difference to
$$k-o=-\frac{3(q^2-d^2)}{8v}.$$
Finally the area of $ABC$ is $v$, so $R=BC\cdot AC\cdot AB/(4v)=bc/(2v)=(q^2-d^2)/(8v)$. Thus $|k-o|=3R$, proving the claim.''','The metric constant is not apparent from the diagram; side-sum and side-difference coordinates synchronize the external bisector, incentre and circumcentre.')
add(2025,'TST',3,6.5,'Number Theory',['prime divisors','polynomials','Chinese remainder theorem'],r'Let $a_1,\ldots,a_k$ be positive integers and let $f\in\mathbb Z[x]$ be nonconstant. Prove that infinitely many primes $p$ divide $$f(n)+a_1^n+\cdots+a_k^n$$ for infinitely many positive integers $n$.',r'''We first prove that a nonconstant integer polynomial $g$ has infinitely many prime divisors among its nonzero integer values. Suppose only primes in a finite set occur, and let $P$ be their product. Choose $t$ with $c=g(t)\ne0$. Then
$$h(m)=\frac{g(t+cPm)}{c}$$
is a nonconstant integer polynomial with $h(m)\equiv1\pmod P$. Choose $m$ with $|h(m)|>1$. A prime divisor of $h(m)$ divides a value of $g$, yet divides neither $P$ nor $c$, a contradiction.

Apply this lemma to $g(x)=f(x)+k$. Excluding the finitely many primes dividing $a_1\cdots a_k$ leaves infinitely many primes $p$, each with some integer $t$ satisfying $f(t)+k\equiv0\pmod p$.

For each such prime, the Chinese remainder theorem gives infinitely many positive $n$ with
$$n\equiv t\pmod p,\qquad n\equiv0\pmod{p-1}.$$
The polynomial values satisfy $f(n)\equiv f(t)\pmod p$, while Fermat's theorem gives $a_i^n\equiv1\pmod p$ for every $i$. Their sum is therefore divisible by $p$.''','One must establish an infinite-prime-divisor lemma, remove the exponential bases’ bad primes, and synchronize polynomial and exponential residues by CRT.')
add(2025,'TST',4,5,'Number Theory',['finite sets','divisibility','extremal principle'],r'Determine all finite tuples $(a_1,\ldots,a_n)$ of pairwise distinct positive integers such that, for every $i,j$, some $k$ satisfies $$a_i\equiv-2a_k\pmod{a_j}.$$ The order of the tuple is immaterial.',r'''The possibilities are a single positive integer $(t)$, or the two integers $(t,3t)$ in either order.

Divide all entries by their gcd; this preserves the condition. At least one normalized entry is odd. Fixing it as $a_i$, the condition says every $a_j$ divides an odd integer $a_i+2a_k$, so all entries are odd.

Order them as $a_1<\cdots<a_n=M$. For each $i<n$, choose $k$ with $M\mid a_i+2a_k$. We cannot have $k=n$, because then $M\mid a_i$. Hence the positive sum is less than $3M$. It is odd, so cannot be $2M$; therefore
$$a_i+2a_k=M.$$
The map $i\mapsto k$ is strictly decreasing and bijects $\{1,\ldots,n-1\}$ with itself. Thus $k=n-i$. Taking $i=1$ and $i=n-1$ gives
$$a_1+2a_{n-1}=M=a_{n-1}+2a_1,$$
forcing $a_1=a_{n-1}$. Consequently $n\le2$. In the two-entry case $M=3a_1$, and undoing the normalization gives $(t,3t)$. These tuples satisfy the condition directly.''','Normalizing by the gcd forces parity, and the largest modulus turns a congruence into an exact identity; its order-reversing permutation leaves at most two entries.')
add(2025,'TST',5,7,'Algebra',['functional equations','positivity','injectivity','geometric sequences'],r'Find every function $f:\mathbb R_{>0}\to\mathbb R_{>0}$ satisfying $$x+f(yf(x)+1)=xf(x+y)+yf(yf(x))$$ for all positive reals $x,y$.',r'''The unique solution is $f(x)=1/x$.

We first prove injectivity. Suppose $f(u)=f(v)$ with $u>v>0$. Comparing the equations at $(u,y)$ and $(v,y)$, and writing $C=u-v$, gives
$$f(t+C)-1=\frac vu\bigl(f(t)-1\bigr)\qquad(t>v).$$
Thus, for any fixed $t>v$, the sequence $f(t+nC)$ tends to1. Let $a_n=t+nC$. Substituting $y=a_n/f(x)$ in the original equation, for any fixed $x>0$, yields
$$x+f(a_n+1)=xf\left(x+\frac{a_n}{f(x)}\right)+\frac{a_n}{f(x)}f(a_n).$$
The left side tends to $x+1$, while positivity makes the right side at least $a_nf(a_n)/f(x)\to\infty$. This contradiction proves injectivity; no continuity assumption was used.

Now substitute $y=x/f(x)$ into the original equation. Cancellation gives
$$f(x+1)=xf\left(x+\frac{x}{f(x)}\right).$$
Taking $x=1$ and using injectivity gives $f(1)=1$. The original equation with $x=1$ then reduces to $1=yf(y)$, so $f(y)=1/y$. Direct substitution checks this function.''','Injectivity is hidden behind a nonlinear substitution; assuming a collision creates a geometric approach to1 along an arithmetic progression, which positivity contradicts.')
skip(2025,'TST',6,None,'Read statement and proposed graph-theoretic solution. The threshold1/4 upper bound follows from a tree component among degree3 vertices; sharpness depends on the non-colourable graph shown only in a diagram. Diagram and complete construction still require checking, so no rating assigned.')
json.dump(items,open(P+'morocco.json','w'),indent=2)
json.dump(ledger,open(P+'morocco-ledger.json','w'),indent=2)
print(len(items),len(ledger))
