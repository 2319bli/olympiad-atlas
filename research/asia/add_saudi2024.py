import json,pathlib
P=pathlib.Path('/workspace/sites/olympiad-atlas/research/asia');raw=P.parent/'raw'/'asia';r=json.loads((P/'reviews.json').read_text())
def add(short,diff,reason,solution=None,statement=None,omit=None):
 slug='sau_2024_'+short;d=json.load(open(raw/(slug+'.json')))
 sec=d['section']
 if 'EGMO' in sec:comp='Saudi Arabia EGMO team selection — Test 1'
 elif 'Preselection' in sec:comp='Saudi Arabia IMO programme — Preselection '+sec.split(' - ')[-1]
 else:comp='Saudi Arabia IMO programme — Camp '+sec.split(' - ')[-1]
 v={'difficulty':diff,'reason':reason,'competitionOverride':comp,'note':'Exact provenance: '+d['booklet_title']+', '+sec+'. This is a programme selection/camp paper appearance; original sources of reused questions are not established.'}
 if solution:v['solutionOverride']=solution
 if statement:v['statementOverride']=statement
 if omit:v['omitReason']=omit
 r[slug]=v
add('f13b64',5.5,'After finding the natural shifted power, subtract it and compare the highest degree of the error terms to force rigidity.',r'''The leading coefficient $a$ satisfies $a=a^3$, hence $a=\pm1$. Negating a solution gives another solution, so assume $P$ is monic of degree $n\ge1$.

The identity $x^3-7x+6=(x-1)(x-2)(x+3)$ shows that $(x+6)^n$ is a solution. Write
$$P(x)=(x+6)^n+Q(x),\qquad\deg Q<n.$$
If $Q\ne0$ has degree $m$ and leading coefficient $b$, substitute this expression into the equation and cancel the common term $(x^3-7x+6)^n$. The left side has degree $3m$. On the right, the three terms containing one factor $Q$ have total leading term $3b x^{2n+m}$. Terms containing two or three factors $Q$ have strictly smaller degrees, since $m<n$. Hence the right side has degree $2n+m>3m$, impossible.

Thus $Q=0$, and all solutions are $\boxed{P(x)=\pm(x+6)^n\ (n\ge1)}$.''')
add('3907b5',2,'The midpoint of IO has perpendicular distance R/2 to all four lines by the triangle midline theorem.')
add('72ce2c',6,'Select prime divisors in one residue class so that two successive Euler-theorem applications can construct a term avoiding all of them.',r'''Every term $a_n$ is odd and congruent to $2$ modulo $3$, so it has a prime divisor congruent to $2$ modulo $3$. Suppose only finitely many such primes ever occur, say $p_1,\ldots,p_k$, and put $M=p_1\cdots p_k$.

Since each $p_i\equiv2\pmod3$, neither $M$ nor $\varphi(M)=\prod_i(p_i-1)$ is divisible by $3$. Choose $n=\varphi(\varphi(M))$. Euler's theorem gives
$$3^n\equiv1\pmod{\varphi(M)},$$
so $\varphi(M)\mid3^n-1$. A second application gives
$$3^{3^n-1}\equiv1\pmod M.$$
Therefore $a_n\equiv3\pmod M$, and none of the $p_i$ divides $a_n$. Yet $a_n$ must have a prime divisor congruent to $2$ modulo $3$, contradicting the list. Thus infinitely many primes divide the sequence.''')
add('2a7c3e',6.5,'Use prime-period binary necklaces to make long forbidden words eliminate only one orbit; a careful orbit count beats the sum of all exclusions.',r'''No. Consider binary words of length $13$, up to cyclic rotation, and repeat each around an infinite periodic sequence. Since $13$ is prime, the two constant words have rotation orbits of size one and all other words have orbit size $13$. There are therefore
$$2+\frac{2^{13}-2}{13}=632$$
periodic sequences up to a shift.

A fixed word of length $\ell\le13$ can occur in at most $2^{13-\ell}$ such sequences: rotate its starting point to the beginning of a period and complete the remaining letters. A word longer than $13$ can occur in at most one sequence, because its first $13$ letters determine the period.

Consequently the chosen words of lengths $5$ through $30$ can eliminate at most
$$\sum_{\ell=5}^{13}2^{13-\ell}+17=511+17=528$$
sequences. At least one sequence avoids every chosen word. Any block of $300$ consecutive letters from it is the required counterexample.''')
add('f72f97',4,'A short finite-state recurrence counts binary strings avoiding two different forbidden runs.',r'''Encode delivery by $1$ and no delivery by $0$. We must count length-$19$ strings with neither $11$ nor $000$.

Let $A_n,B_n,C_n$ count valid strings ending respectively in $1$, in a single trailing $0$, and in two trailing zeros. For $n=1$ they are $(1,1,0)$, and appending a symbol gives
$$(A_{n+1},B_{n+1},C_{n+1})=(B_n+C_n,A_n,B_n).$$
In particular $S_n=A_n+B_n+C_n$ satisfies $S_n=S_{n-2}+S_{n-3}$ for $n\ge4$, with $S_1=2,S_2=3,S_3=4$. Iteration gives
$$S_4,\ldots,S_{19}=5,7,9,12,16,21,28,37,49,65,86,114,151,200,265,351.$$
Hence there are $\boxed{351}$ patterns.''')
add('1ad8bc',4,'Exploit the ordering through a product of two differences, then apply a weighted Cauchy bound; the upper bound comes from expanding the constraint.',r'''Write $P=x^2+z^2+xy+yz+zx$. Expanding the constraint gives
$$25=(2x+y+2z)^2=4P+y^2+4xz\ge4P.$$
Thus $P\le25/4$, with equality precisely at $(x,y,z)=(5/2,0,0)$.

Because $(y-x)(y-z)\le0$, we have $xy+yz\ge y^2+xz$, and hence
$$P\ge(x+z)^2+y^2\ge\frac{(2(x+z)+y)^2}{5}=5.$$
The second inequality is Cauchy's inequality. Equality requires both $y=x$ or $y=z$ and $x+z=2y$, forcing $x=y=z=1$.''')
add('4d9615',7,'Combines a radical-axis observation, isogonality, Simson collinearity and a spiral similarity; several geometry ideas must be coordinated.')
add('0695e4',5,'Coloring the triangular cells in one half of the hexagon turns the diagonal-crossing count into a fixed color imbalance.',r'''Subdivide the regular hexagon into the unit equilateral triangles underlying its rhombus tiling. Color upward-pointing triangles red and downward-pointing triangles blue, rotating the picture so the chosen main diagonal is horizontal. Every diamond consists of one triangle of each color.

Consider the half above the diagonal. It consists of $n$ horizontal strips of triangular cells. In each strip, the lower row of triangle bases is one unit longer than the upper row, so the strip contains one more red than blue triangle. The half-hexagon therefore has exactly $n$ more red triangles.

A diamond entirely inside this half contributes one triangle of each color. A diamond crossing the diagonal is cut into its two constituent triangles, and its upper triangle is always red. Consequently the color excess equals exactly the number of diamonds bisected by the diagonal, which is $n$. Rotating the argument handles each main diagonal.''')
add('2de6ed',7.5,'The solution passes through parallel triangles, a harmonic pencil, a harmonic cyclic quadrilateral and intersecting tangents; this exceeds accessible BMO2.')
add('6778a3',5.5,'Reduce the three sides to a ratio of symmetric quadratic forms, determine its triangle range, and optimize the resulting one-variable sharp bound.',r'''Put $S=a^2+b^2+c^2$, $Q=ab+bc+ca$, and $t=\sqrt{Q/S}$. Since $Q\le S$ and the triangle inequalities give
$$2Q-S=a(b+c-a)+b(c+a-b)+c(a+b-c)>0,$$
we have $1/\sqrt2<t\le1$.

For $t=1$ the triangle is equilateral and the proposed inequality is an equality for every $k$. Otherwise rearranging it gives
$$k\le F(t):=\frac{1+2t^2}{2(1+t)}.$$
This function is increasing on $[1/\sqrt2,1]$: its derivative has the sign of $2t^2+4t-1$, which is positive there. Thus $F(t)>F(1/\sqrt2)=2-\sqrt2$, so $k=2-\sqrt2$ works for every triangle.

Taking $a=b=1$ and $c\to0^+$ gives $t\to1/\sqrt2$ and shows that every larger $k$ fails for sufficiently small $c$. Therefore $\boxed{k_{\max}=2-\sqrt2}$.''')
add('5429e4',5.5,'Track the parity of odd entries and use a prime-divisor backward invariant; the two exceptional primes require the no-nontrivial-cube-root lemma.',r'''Let $N=2023^{2024}$. The replacement
$$F(a,b)=\gcd(2024ab,a^2+254ab+b^2)$$
is odd exactly when $a,b$ have different parity. Thus the parity of the number of odd board entries is unchanged. Since $N\equiv1\pmod4$, initially there are $(N+1)/2$ odd entries, an odd number. The final entry is therefore odd.

For every odd prime $p$, we claim that $p\mid F(a,b)$ implies $p\mid a$ and $p\mid b$. If $p\ne11,23$, this follows from $p\mid ab$ and $p\mid a^2+254ab+b^2$. For $p=11$ or $23$, note $254\equiv1\pmod p$. If $b$ is nonzero modulo $p$, put $t=a/b$; the equation is $t^2+t+1=0$. It gives $t^3=1$, but $p\equiv2\pmod3$, so the only cube root of $1$ is $1$, which does not satisfy the quadratic. Thus $p\mid b$, and then $p\mid a$.

If an odd prime divided the final entry, applying this claim backwards through every merge would make it divide every original entry, including $1$, impossible. The final entry is odd and has no odd prime factor, so it is always $\boxed1$.''',r'''The board initially contains all integers $1,2,\ldots,2023^{2024}$. A move erases two entries $a,b$ and writes
$$\gcd(2024ab,a^2+254ab+b^2).$$
After repeated moves only one entry $x$ remains. Determine all possible values of $x$.''')
add('f08d2c',6.5,'Inclusion-exclusion modulo two interacts with a multiplicative residue character, making all integers with two distinct prime factors cancel.',r'''Negative $n$ and $n=1$ contribute no such $k$, so consider positive odd $n>1$. Define $w(t)=\lfloor t/4\rfloor\pmod2$ for odd positive $t$. Its values modulo $8$ are $0,0,1,1$ at residues $1,3,5,7$, respectively. Checking these four residues shows
$$w(uv)=w(u)+w(v)\pmod2.$$
Let the distinct prime factors of $n$ be $p_1,\ldots,p_r$. Inclusion-exclusion, whose signs all become plus modulo two, gives the desired count's parity as
$$\sum_{J\subseteq\{1,\ldots,r\}}w\!\left(\frac{n}{\prod_{j\in J}p_j}\right).$$
The multiplicative rule rewrites a summand as $w(n)+\sum_{j\in J}w(p_j)$. Summing over all subsets gives
$$2^r w(n)+2^{r-1}\sum_{j=1}^rw(p_j)\pmod2.$$
If $r\ge2$ this vanishes. If $r=1$, it is $w(p_1)$, which is odd exactly when $p_1\equiv5$ or $7\pmod8$. Thus the answers are $\boxed{n=p^a}$, where $a\ge1$ and $p\equiv5,7\pmod8$ is prime.''')
add('6b61a0',2.5,'Pigeonhole forces five distinct values if no value occurs n times; two four-term progressions sharing three values then contradict distinctness.')
add('6972c9',6.5,'Positivity forces a global quadratic lower bound, which pins down the least parameter; integer inputs and an unbounded shift then prove uniqueness.',r'''First, $f(y)\ge y^2$ for every $y>0$: otherwise choose $x=y^2-f(y)>0$ in the equation, and cancel $f(y^2)$ to get a sum of positive terms equal to zero.

Put $u=f(1)\ge1$. At $x=y=1$,
$$(1+u)^2\le f(1+u)=2u+m/u,$$
so $m\ge u^3+u\ge2$.

For $m=2$, the function $f(x)=x^2$ works. We prove it is unique. The preceding inequality forces $f(1)=1$. Taking $y=1$ gives
$$f(x+1)=f(x)+\frac{2x^5}{f(x)^2}+1,$$
and induction yields $f(n)=n^2$ for all positive integers $n$.

Now put $y=n$ in the original equation and use the lower bound at $x+n^2$:
$$f(x)+\frac{2x^5n^2}{f(x)^2}+n^4\ge(x+n^2)^2.$$
Equivalently,
$$f(x)-x^2\ge2xn^2\left(1-\frac{x^4}{f(x)^2}\right).$$
If $f(x)>x^2$, the right side tends to infinity as $n\to\infty$, a contradiction. Thus $f(x)=x^2$ everywhere. The least parameter is $\boxed{m=2}$.''')
add('f4a1ee',6,'Use reflection symmetry of the ordered reduced residues to force an alternating residue pattern, then construct coprime numbers near n/2 that violate it.',r'''The answers are $\boxed{2,4,10}$, whose reduced-residue lists are $(1)$, $(1,3)$ and $(1,3,7,9)$.

Assume $n$ has the stated property. If $n\ge3$ is odd, its first two reduced residues are $1,2$, impossible. Thus $n$ is even. If $3\mid n$, the two reduced residues straddling $n/2$ sum to $n$, again impossible.

Now $3\nmid n$. Reflection $a\mapsto n-a$ reverses the reduced-residue list. If consecutive residues have sum $s$, the reflected pair has sum $2n-s$. Neither can be zero modulo $3$, so necessarily $s\equiv n\pmod3$. Starting at $a_1=1$, all reduced residues must therefore alternate between $1$ and $n-1$ modulo $3$.

If $n\equiv2\pmod3$ and $n>2$, the reduced residue $3$ contradicts this pattern, which in this case permits only residue $1$. Thus $n\equiv1\pmod3$, and the pattern permits only residues $0,1$.

If $n=12k+4$ with $k\ge1$, the positive integer $n/2-3=6k-1$ is coprime to $n$: a common divisor would divide $6$, while $6k-1$ is odd and not divisible by $3$. But it is $2$ modulo $3$, contradiction. If $n=12k+10$ with $k\ge1$, use instead $n/2-6=6k-1$; its gcd with $n$ divides $12$ and is again $1$. The only remaining cases are $n=4,10$, together with $2$.''')
add('58cf0d',8,'The intended solution uses harmonic quadrilaterals, symmedians and an external mixtilinear circle.',omit='Withheld: statement says the median meets the circle at D, whereas its first proof step requires the A-symmedian (ABDC harmonic). Exact original statement must be checked.')
(P/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
