from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');o=json.loads((p/'international-extra-solutions.json').read_text())
o['bmo_2023_83afda']=o['bmo_2023_83afda'].replace('angle chasing gives $\\angle BIC=\\angle EFC$, so $S,F,I,C$ are concyclic. Since $IF\\perp FC$, this circle has diameter $IC$','the angle-bisector and tangency relations give $\\angle BIC=\\angle FEC=90^\\circ+A/2$. Since $S$ lies on $BI$ and $EF$, this makes $S,E,I,C$ concyclic (using directed angles if necessary). Since $IE\\perp EC$, this circle has diameter $IC$')
o['btw_2023_a9bf63']=r'''The maximum is $2n-1$, except that it is four for $n=2$. Colour cell $(i,j)$ by $i+j$ to attain $2n-1$; each colour then touches only the preceding and following colours. A two-by-two grid permits four distinct colours.

Form the connected graph of colours that touch. Its degrees are at most two, so it is a path or cycle. If it is a path, number the colours consecutively by integers. Adjacent grid cells have labels differing by at most one. Any two cells can be joined by at most $2n-2$ grid steps, so the difference between the largest and smallest labels is at most $2n-2$. Hence there are at most $2n-1$ colours.

For a cycle with $k\geq5$ colours, number them modulo $k$ in cyclic order. Along each directed grid edge, record the change as $-1,0$ or $1$. The sum around each elementary square is a multiple of $k$ with absolute value at most four, hence is zero. It follows by decomposing grid loops into elementary squares that the sum along a path depends only on its endpoints. Starting from one cell, these sums therefore define consistent integer labels for all cells, whose residues are the colour numbers. As before, adjacent integer labels differ by at most one and their total range is at most $2n-2$. Thus at most $2n-1$ different colours appear.

Cycles with at most four colours satisfy the same bound for $n\geq3$. The cases $n=1,2$ give the stated exceptions directly.'''
o['btw_2023_409ecd']=r'''(a) No. There is a nonattacking rook placement containing the cell labelled 13, so its product is divisible by 13. On the other hand, only four labels are multiples of 13. Let $R$ be the rows containing them, and choose $|R|$ distinct columns containing no such label; at least four such columns exist. Place one rook in each row of $R$ using these columns, then fill the other rows and columns arbitrarily. This product is not divisible by 13. The two products cannot be congruent modulo 65.

(b) Yes. Two has multiplicative order 100 modulo 101: its order divides 100 by Fermat, while
$$2^{10}\equiv14,\quad2^{20}\equiv-6,\quad2^{50}\equiv(-6)^2\cdot14\equiv-1\pmod{101}.$$
Every proper divisor of 100 divides 20 or 50, so neither can be the order. Hence the residues $2^0,\ldots,2^{99}$ are a permutation of $1,\ldots,100$.

Number rows and columns from zero to nine, and put the least positive residue of $2^{10i+j}$ in cell $(i,j)$. Every label occurs once. A nonattacking rook placement uses one cell in each row and column, so its product is congruent to
$$2^{10\sum_{i=0}^9i+\sum_{j=0}^9j}=2^{495}\pmod{101},$$
independently of the placement. Thus all differences are divisible by 101.'''
o['btw_2023_641459']=r'''The answer is $n=1$ and every even positive integer $n$.

We first use a criterion. If $N=\prod_{i=1}^k p_i^{a_i}$ with increasing primes, put $N_i=\prod_{j=1}^i p_j^{a_j}$ and $N_0=1$. Then $N$ is good exactly when
$$p_{i+1}\leq1+\sigma(N_i)\quad(0\leq i<k),$$
where $\sigma$ is the sum of positive divisors. Goodness means that every integer from zero to $\sigma(N)$ is a sum of distinct divisors: repeatedly subtract one from the sum of all divisors for necessity of this reformulation.

If the displayed inequality fails, the integer $1+\sigma(N_i)$ cannot be represented: divisors using only the first $i$ primes sum to too little, and every other divisor is too large. Conversely, suppose all inequalities hold. Inductively the divisors of $N_i$ represent every integer in $[0,L]$, where $L=\sigma(N_i)$. For the next prime $p\leq L+1$, adjoining the groups of divisors $pN_i,p^2N_i,\ldots,p^aN_i$ preserves a gap-free interval of subset sums. At stage $j$, the intervals
$$q p^j+[0,L(1+p+\cdots+p^{j-1})]\qquad(0\leq q\leq L)$$
overlap or touch, since $L(1+\cdots+p^{j-1})\geq p^j-1$. This proves the criterion.

Every factorial is good. Its primes are an initial segment of the primes, and the next prime is at most $1+p_1\cdots p_i\leq1+\sigma(N_i)$: take a prime divisor of $1+p_1\cdots p_i$ to see the first inequality.

If $n>1$ is odd, all divisors of $n^n$ are odd and only one is one, so two is not representable. Thus $n^n$ is not good. If $n$ is even, its factor two appears in $n^n$ with exponent at least $n$. For every later prime factor $p$ of $n$, we have
$$p\leq n<2^{n+1}\leq1+\sigma(2^{v_2(n^n)})\leq1+\sigma(N_i).$$
The first-prime condition is also satisfied, so the criterion proves that $n^n$ is good. Finally one is plainly good.'''
o['btw_2023_aaf831']=r'''We prove that the digit sum of $2^{4^t}$ exceeds $t$ for every positive integer $t$. The problem follows by taking $t=2^{2022}>2023$.

Write $m=4^t$ and let $0=e_0<e_1<\cdots<e_k$ be the positions of the nonzero decimal digits of $2^m$. The units digit is nonzero. All positions are smaller than $m$, since $2^m<10^m$.

For $j\geq1$, the lower-digit block $R_j=\sum_{i=0}^{j-1}d_i10^{e_i}$ is positive and divisible by $2^{e_j}$: both $2^m$ and the omitted higher block have this divisibility. Therefore
$$2^{e_j}\leq R_j<10^{e_{j-1}+1}<16^{e_{j-1}+1}.$$
It follows that $e_j\leq4e_{j-1}+3$, so induction gives $e_j\leq4^j-1$. Hence
$$2^m<10^{e_k+1}\leq10^{4^k}<2^{4^{k+1}}.$$
Thus $4^t=m<4^{k+1}$ and $k\geq t$. There are $k+1\geq t+1$ nonzero digits, so the digit sum exceeds $t$.'''
o['btw_2023_49de42']=r'''The answer is $\alpha=1/2$. For this value, squaring twice (all sides involved are nonnegative) reduces the desired inequality to
$$(x+y)^4\geq8xy(x^2+y^2),$$
which is exactly $(x-y)^4\geq0$.

For necessity choose $x=1+\varepsilon$, $y=1-\varepsilon$, where $0<\varepsilon<1$. The inequality forces
$$\alpha\geq\frac{\sqrt{1+\varepsilon^2}-1}{\sqrt{1+\varepsilon^2}-\sqrt{1-\varepsilon^2}}
=\frac{\sqrt{1+\varepsilon^2}+\sqrt{1-\varepsilon^2}}{2(\sqrt{1+\varepsilon^2}+1)}.$$
As $\varepsilon$ tends to zero, the right-hand side tends to one half. Therefore no smaller constant works.'''
(p/'international-extra-solutions.json').write_text(json.dumps(o,ensure_ascii=False,indent=2))
# Add the missing selected algebra problem directly, with original exposition.
d={'id':'baltic_2023_official_p4','competition_code':'Baltic Way','year':2023,'problem_number':'4','primary_domain':'Algebra','topics':[['Algebra','Functional equations']],'problem_markdown':r'Determine every function $f:\mathbb R\to\mathbb R$ for which $$f(f(x)+y)+xf(y)=f(xy+y)+f(x)$$ holds for all real $x,y$.','solutions_markdown':[r'''The possibilities are $f(x)=0$ and $f(x)=x$.

Write $P(x,y)$ for the stated equality and put $c=f(0)$. From $P(0,y)$, $f(y+c)=f(y)+c$, hence $f(-c)=0$. Also $P(x,0)$ gives $f(f(x))+xc=c+f(x)$. Use $x=-c$ in this identity to obtain $c-c^2=c$, so $c=0$ and $f(f(x))=f(x)$.

Putting $x=f(t),y=1$ in the equation and using idempotence yields $f(t)f(1)=f(t)$. Thus either $f$ is zero everywhere or $f(1)=1$. Assume the latter.

If $f(a)=0$, the identities $P(a,1)$ and $P(1,a)$ give $f(a+1)=a+1$ and $f(2a)=a$. Idempotence then gives $a=f(2a)=f(f(2a))=f(a)=0$. Thus zero has no other preimage.

Using $P(x,x-f(x))$ and cancelling $f(x)$ gives
$$x f(x-f(x))=f((x+1)(x-f(x))).$$
At $x=-1$, the right side is zero, so uniqueness of the zero gives $f(-1)=-1$. Now $P(-1,y)$ yields $f(y-1)=f(y)-1$. Finally $P(x,1)$ becomes
$$f(f(x))+1+x=f(x)+1+f(x),$$
so $f(x)=x$. Both displayed functions satisfy the equation directly.'''],'officialSourceUrl':'https://bw2025.lu.lv/fileadmin/user_upload/lu_portal/projekti/baltic_way_2013/BW_problems_solutions/bw2023_solutions.pdf','officialSolutionUrl':'https://bw2025.lu.lv/fileadmin/user_upload/lu_portal/projekti/baltic_way_2013/BW_problems_solutions/bw2023_solutions.pdf'}
(p/'international-raw/baltic_2023_official_p4.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
r=json.loads((p/'international-reviews.json').read_text());r['baltic_2023_official_p4']=[5.5,'A chain of substitutions establishes idempotence, a unique zero and translation by one before forcing the identity function; the zero solution must be separated.'];r['btw_2023_a9bf63'][0]=6;r['btw_2023_a9bf63'][1]='The colour graph is a path or cycle; in the cyclic case a consistent integer lift of grid colours supplies the diameter bound, with a special two-by-two exception.'
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
