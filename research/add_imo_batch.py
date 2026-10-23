from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');r=json.loads((p/'international-reviews.json').read_text());o=json.loads((p/'international-extra-solutions.json').read_text());raw=p/'international-raw'
r.update({
'imo_2023_2e005b':[5,'The decisive step reverses the ordered divisors using complementary divisors, producing a prime-divisibility contradiction at the first new prime.'],
'imo_2023_1ae32a':[6.5,'Two cyclicities give a right angle at P; an auxiliary diameter and a second intersection of the tangent produce parallel corresponding sides and a homothety centre.'],
'imo_2023_d4d6f3':[8.5,'The classification needs monotonicity via infinite descent, uniform coefficient comparison and an extremal argument forcing eventual arithmetic progression before a backward extension.'],
'imo_2023_7a9af0':[5.5,'AM-GM controls the increment, but the key is studying equality twice: consecutive unit increments force two forbidden equal x-values.'],
'imo_2023_a99802':[7,'The optimal logarithmic construction and a row-sum potential are both needed; the latter amplifies a maximum path count across successively doubled row ranges.'],
'imo_2023_1fa49d':[9.5,'Several unexpected circumcentres, two radical-centre constructions and delicate nondegeneracy arguments are required to obtain a shared secant line.'],
'imo_2023_da43cf':[6,'An isosceles-triangle symmetry suggests reflecting P in CD; one carefully chosen congruence then proves both required perpendicularities.'],
'imo_2023_7d3fd0':[6,'An iterate inequality gives a fixed positive decrease along even iterates unless f is an involution; positivity rules this out, leaving a reciprocal family.'],
'imo_2023_1ffb42':[6,'Introduce the divisibility quotients; infinitely many prime factors make them unbounded, and their one-step growth bound forces a crossing yielding divisibility by any n.'],
'imo_2023_73cc8d':[9,'The sharp Hamiltonian-path colouring bound requires a substantial edge-recolouring scheme and a structural reduction before the logarithmic extremal argument.'],
'imo_2022_b034b8':[6,'Track the number of monochromatic blocks, isolate the cyclic last-block obstruction, and construct counterexamples on both sides of the permitted interval.'],
'imo_2022_e1fe8a':[5,'Uniqueness first excludes unequal admissible pairs by AM-GM; a nearby input then rules out strict inequality in the bound f(x)≤1/x.'],
'imo_2022_cd4ff4':[4.5,'SSS congruence creates a second triangle similarity, whose length relation gives the auxiliary cyclic quadrilateral needed for the final angle chase.'],
'imo_2022_230fa0':[6.5,'Prime valuation and factorial growth first force a=p; the final obstruction is a tailored congruence modulo (p+1) squared.'],
'imo_2022_34151b':[8,'The path-count lower bound is accessible, but equality requires a difficult general construction of an induced spanning tree with independent complement in every grid size.']
})
o['imo_2023_2e005b']=r'''Exactly the composite prime powers $n=p^r$ with $r\geq2$ work: their divisors are consecutive powers of $p$, so the divisibility conditions are immediate.

Suppose instead that $n$ has at least two prime divisors. Let $p<q$ be its two smallest prime divisors. Just before the first divisor $q$ not divisible by $p$, the ordered list begins
$$1,p,p^2,\ldots,p^j,q$$
for some $j\geq1$. Reversing the list by the bijection $d\mapsto n/d$ shows that three consecutive divisors are
$$\frac nq,\quad\frac n{p^j},\quad\frac n{p^{j-1}}.$$
The condition therefore makes $\frac nq$ divide $\frac n{p^j}(p+1)$. Equivalently $q(p+1)/p^j$ is an integer, impossible since $p$ divides neither $q$ nor $p+1$. Thus $n$ has only one prime divisor.'''
o['imo_2022_e1fe8a']=r'''The unique solution is $f(x)=1/x$. This works because $x/y+y/x\geq2$, with equality only when $y=x$.

Call $(x,y)$ admissible when $xf(y)+yf(x)\leq2$. Suppose an admissible pair has $x\ne y$. By uniqueness, neither $(x,x)$ nor $(y,y)$ is admissible, so $xf(x)>1$ and $yf(y)>1$. But AM-GM gives
$$xf(y)+yf(x)\geq2\sqrt{xf(x)\,yf(y)}>2,$$
a contradiction. Thus the admissible partner of every $x$ is $x$ itself, and $f(x)\leq1/x$ for all $x>0$.

If $f(x)<1/x$ for some $x$, choose $a$ with $x<a<1/f(x)$. Then
$$af(x)+xf(a)\leq af(x)+x/a<1+1=2.$$
This makes $(x,a)$ admissible with $a\ne x$, another contradiction. Hence $f(x)=1/x$ everywhere.'''
o['imo_2022_230fa0']=r'''The solutions are $(a,b,p)=(2,2,2)$ and $(3,4,3)$.

Clearly $a>1$. If $a<p$ and $a\leq b$, then $a$ divides $b!$ and $a^p$, so $a\mid p$, impossible. If instead $b<a<p$, then $b!\leq a!<a^p-p$, also impossible. For the last inequality, $p\geq3$ and $a!\leq a^{p-1}$ give $a^p-a!\geq(a-1)a^{p-1}\geq2^{p-1}>p$.

Suppose $a>p$. Then $b!=a^p-p>p!$, so $b>p$ and $p\mid a$. The valuation of $a^p-p$ at $p$ is exactly one, hence $b<2p$. If $p<a<p^2$, the integer $a/p$ is between two and $p-1$, so it divides both $b!$ and $a^p$ and consequently divides $p$, a contradiction. If $a\geq p^2$, then
$$a^p\geq p^{2p}>(2p-1)!+p\geq b!+p.$$
Here $(2p-1)!\leq p^{2p-1}$ follows by pairing $j$ with $2p-j$ for $1\leq j<p$. This again contradicts the equation.

Thus $a=p$. The primes two and three give precisely the two listed solutions. For $p\geq5$, we have $b! =p^p-p>p!$, so $b\geq p+1$. The distinct integers $2$ and $(p+1)/2$ occur in $p!$, showing $p+1\mid p!$ and therefore $(p+1)^2\mid b!$. On the other hand, binomial expansion at $p=(p+1)-1$ gives
$$p^p-p\equiv p(p+1)-1-p=p^2-1\not\equiv0\pmod{(p+1)^2}.$$
This final contradiction excludes all larger primes.'''
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));(p/'international-extra-solutions.json').write_text(json.dumps(o,ensure_ascii=False,indent=2))
