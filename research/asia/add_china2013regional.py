import json,pathlib
p=pathlib.Path('research/asia/reviews.json');r=json.loads(p.read_text());raw=pathlib.Path('research/raw/asia')
def add(k,d,reason,sol=None,**kw):
 r['chn_2013_'+k]={'difficulty':d,'reason':reason,**kw}
 if sol:r['chn_2013_'+k]['solutionOverride']=sol
add('2a047b',5.5,'Closure under modular averaging is converted into additive subgroup structure, requiring both finite-set closure and a gcd classification.',r'''Work in the residues modulo $99$. Translate $S$ by one of its elements so that $0\in S$; its size and the condition are unchanged. Taking $y=0$ shows that multiplication by $50$ sends $S$ into itself. This map is injective, hence bijective on the finite set $S$, so its inverse, multiplication by $2$, also preserves $S$. The average condition therefore implies that $x+y\in S$ whenever $x,y\in S$.

Repeated addition gives $-x=98x\in S$. Thus $S$ is an additive subgroup of the residues modulo $99$. If $d=\gcd(99,s_1,\ldots,s_m)$, Bézout and closure show that $d\in S$, while every element is a multiple of $d$. Hence $S$ consists precisely of the multiples of $d$ modulo $99$ and has size $99/d$.

Conversely every such subgroup is closed under averaging, since $2$ is invertible modulo $99$. Its possible sizes at least $3$ are $\boxed{3,9,11,33,99}$.''')
add('2e07c9',7.5,'Requires classification of cubic permutation polynomials modulo two primes by a quadratic-residue set argument, then CRT counting.')
add('34f199',4.5,'Finds a shift-and-delete bijection for good sets containing the largest element.',r'''Partition the good subsets of $\{1,\ldots,n+2\}$ into three classes. Those not containing $n+2$ are counted by $a_{n+1}$. The singleton $\{n+2\}$ contributes one.

For every remaining set, delete $n+2$ and subtract $1$ from each other element. If the original set has $k+1$ elements, its smallest element is at least $k+1$, so the new nonempty set has $k$ elements, minimum at least $k$, and maximum at most $n$. It is therefore a good set of degree $n$. Conversely, add $1$ to each element of any good set of degree $n$ and then adjoin $n+2$; this reverses the construction. This third class has $a_n$ members, proving $a_{n+2}=a_{n+1}+a_n+1$.''',topic='Combinatorics')
add('574514',6,'Encodes positions in binary, constructs a legal descending strategy and counts its skipped states by 2-adic valuation.',r'''Yes. Encode heads by $1$ and tails by $0$, with the leftmost coin the most significant binary digit. In each move choose the rightmost head and flip the longest odd-length block starting there.

If the current binary integer is $V$ and there are $k$ zeroes after its rightmost $1$, then the move decreases $V$ by $1$ when $k$ is even and by $2$ when $k$ is odd. Consequently the process ends at $0$. A skipped integer is always odd, so every positive even integer below $2^n$ is visited. The number of skipped integers is therefore exactly the number of $V$ with $1\le V<2^n$ and odd $2$-adic valuation:
$$\sum_{\substack{1\le j<n\\j\text{ odd}}}2^{n-j-1}=\left\lfloor\frac{2^n}{3}\right\rfloor.$$
Starting at $2^n-1$, the total decrease equals the number of moves plus the number of skipped integers. Thus the number of moves is
$$2^n-1-\left\lfloor\frac{2^n}{3}\right\rfloor=\left\lfloor\frac{2^{n+1}}3\right\rfloor,$$
as required.''',topic='Combinatorics')
add('62053d',6.5,'The intended configuration involves tangent-circle similarities and a bisector identification.',omitReason='Source conclusion says excenter, while the provided argument establishes equal distances to the three vertices, i.e. a circumcenter. The central term is mistranscribed; withheld pending original verification.')
add('6a34a4',6.5,'Proves a parity invariant under swaps of consecutive ranks, with careful adjacent and nonadjacent cases.',r'''Replace the numbers by their ranks $1,\ldots,n$; no comparison changes. Let $C$ be the number of crossings and $P$ the number of positive edges. We show that $C+P$ has invariant parity when two consecutive ranks $i,i+1$ are exchanged.

If their vertices are adjacent, exactly their common edge changes positivity. Among same-parity edge pairs, exactly the pair consisting of the other edge incident with each of these vertices changes crossing status. Thus both $C$ and $P$ change parity.

If the vertices are not adjacent, no edge changes positivity. Only edge pairs containing one of the two vertices each can change crossing status. There are exactly two eligible pairs with equal edge-index parity. Each exchanges two consecutive positions in the ordering of its four endpoint values, so its crossing status reverses. Thus $C$ changes by an even number.

Every ordering can be obtained by such swaps from the clockwise ordering $1,2,\ldots,n$. In that ordering $P=n-1$ is odd and $C=0$. Therefore $C+P$ is always odd, which is the claim.''',topic='Combinatorics')
add('6d6a00',6.5,'Universal divisibility first excludes odd prime factors of a, then exponential growth forces an equality between two polynomial exponents.',r'''Taking $n=6$ shows that $a$ is even. Suppose an odd prime $p$ divides $a$, and take $n=p^2-1\ge8$. Fermat gives $2^n\equiv1\pmod p$, while $n^2\equiv1\pmod p$. Thus $p\mid2^n-n^2$, but $a^n-n^a\equiv-(-1)^a=-1\pmod p$, a contradiction. Therefore $a=2^t$ for an integer $t\ge1$.

Modulo $2^n-n^2$, we have $a^n=(2^n)^t\equiv n^{2t}$. The required divisibility therefore implies
$$2^n-n^2\mid n^{2t}-n^{2^t}.$$
For fixed $t$, the absolute value of the right side is smaller than $2^n-n^2$ for all sufficiently large $n$, because an exponential eventually exceeds every fixed power. It must consequently be zero, giving $2t=2^t$. The only positive solutions are $t=1,2$; for $t\ge3$, $2^t>2t$ by induction.

Finally $a=2$ gives the divisor itself, and $a=4$ gives $(2^n-n^2)(2^n+n^2)$. Thus $\boxed{a=2,4}$.''')
add('6d8ac0',4,'The key is an asymmetric linear bound for each product whose weighted coefficients add to exactly the desired values.')
add('768547',3,'Modulo 4 first forces all three variables odd, then two equal residue classes contradict a square.')
add('76ac59',4.5,'Double-counts pairs of boys with a common girl, then compares degree with the number of pairs.',r'''Let $d_g$ be the number of boys known by girl $g$. Each pair of boys has at most one common girl, so
$$\sum_g\binom{d_g}{2}\le\binom n2.$$
For every integer $d\ge0$, $d\le1+\binom d2$. Summing over all $m$ girls yields
$$\#\{\text{known boy-girl pairs}\}=\sum_g d_g\le m+\sum_g\binom{d_g}{2}\le m+\binom n2.$$
This also accounts for girls who know no boys.''',topic='Combinatorics')
add('7d09ee',4.5,'Reduces real inputs to integers and pairs adjacent outputs of opposite parity after finding the endpoint of the range.')
add('8acca0',6.5,'Requires an excenter construction or substantial vector work, linking reflected excenters to the excircle contact cevian.',solutionKind='source-link')
add('aab84c',6,'Uses a sum invariant to reduce to five bottom-label sets and then counts constrained cyclic arrangements up to reflection.',solutionKind='source-link',topic='Combinatorics')
add('b1261c',4.5,'The intended positive-root version combines Vieta with AM-GM.',omitReason='The statement omits positivity of the roots. With only real roots, a=0,b=-1 already makes the requested expression undefined, and the positive-root AM-GM solution is inapplicable.')
add('b141e9',5.5,'Recognizes a nonlinear recurrence as the Pell recurrence and proves the adjacent-square addition identity.',r'''Define $P_0=0$, $P_1=1$, and $P_{n+1}=2P_n+P_{n-1}$. Induction gives the Cassini identity
$$P_{n+1}P_{n-1}-P_n^2=(-1)^n.$$
Indeed the expression for index $n+1$ is the negative of that for index $n$, and the base case is $-1$. Since $P_1=1$, $P_2=2$ and all subsequent terms are positive, this identity shows that $P_n$ satisfies the given nonlinear recurrence. Hence $a_n=P_n$.

The addition formula
$$P_{r+s}=P_rP_{s+1}+P_{r-1}P_s$$
follows by induction on $s$, since both sides obey the same recurrence and agree for $s=0,1$. Taking $r=n+1$, $s=n$ gives
$$a_{2n+1}=a_{n+1}^2+a_n^2.$$
Thus the sum in question is always another term of the sequence.''')
add('cd06ba',3.5,'The third vertex can be moved to a corner of the triangular region, after which two direct AM-GM bounds suffice.')
add('ef87dd',6.5,'The intended proof uses Menelaus and tangent-secant powers in a fairly elaborate configuration.',omitReason='The statement says the incircle touches both BC and AD at D and E, although AD passes through the first contact D; this is geometrically inconsistent. The source solution also starts with missing auxiliary definitions. Withheld.')
add('f3de84',5.5,'A divisor-count equation is solved by descending through the largest prime, with a parity obstruction excluding zero exponents.')
add('fa94c8',6,'Finds a sharp extremal concentration and proves sufficiency by comparing diagonal terms with a product of three constrained sums.',r'''Let $D_k=(k+\alpha)(k+\beta)(k+\gamma)$ and set
$$L=\frac{\alpha\beta\gamma}{(1+\alpha)(1+\beta)(1+\gamma)-\alpha\beta\gamma}.$$
Concentrating all three sequences at index $1$, with $a_1=\alpha/(1+\alpha)$ and analogously for $b_1,c_1$, shows that every admissible $\lambda$ must satisfy $\lambda\ge L$.

To prove sufficiency, observe that
$$\frac{k\alpha\beta\gamma}{D_k-\alpha\beta\gamma}=\frac{\alpha\beta\gamma}{k^2+k(\alpha+\beta+\gamma)+\alpha\beta+\beta\gamma+\gamma\alpha}\le L$$
for every $k\ge1$. Equivalently $k+L\le LD_k/(\alpha\beta\gamma)$. Nonnegativity then gives
$$\begin{aligned}
\sum_k(k+L)a_kb_kc_k&\le\frac{L}{\alpha\beta\gamma}\sum_kD_ka_kb_kc_k\\
&\le\frac{L}{\alpha\beta\gamma}\left(\sum_k(k+\alpha)a_k\right)\left(\sum_k(k+\beta)b_k\right)\left(\sum_k(k+\gamma)c_k\right)\le L.
\end{aligned}$$
Thus the minimum is exactly $\boxed L$.''')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2));print(len(r))
