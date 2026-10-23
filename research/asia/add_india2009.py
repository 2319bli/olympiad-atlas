import json,pathlib
p=pathlib.Path('research/asia/reviews.json');r=json.loads(p.read_text());raw=pathlib.Path('research/raw/asia')
def add(key,diff,reason,sol=None,**kw):
 slug='ind_2009_'+key;r[slug]={'difficulty':diff,'reason':reason,**kw}
 if sol:r[slug]['solutionOverride']=sol
add('0eac96',6,'Strengthens the claim to vectors of length at most one, then merges a suitably signed close pair to enable induction.',r'''Prove the stronger assertion for vectors of length at most $1$. For two vectors, the parallelogram law gives $|u+v|^2+|u-v|^2\le4$, so one sign works.

For at least three nonzero vectors, among the six directions of $\pm v_1,\pm v_2,\pm v_3$ two belonging to different original vectors are separated by at most $60^\circ$. Call these signed vectors $u,v$, with lengths $a\ge b$. Then
$$|u-v|^2\le a^2+b^2-ab\le a^2\le1.$$
Replace those two original vectors by $u-v$ and apply induction to the resulting list of one fewer vectors. Expanding the selected sign of $u-v$ gives allowable signs on both original vectors. Zero vectors may simply be removed. This proves the stronger assertion and hence the claim.''')
add('2819b6',6.5,'Uses the top-degree homogeneous terms to identify roots-of-unity slopes, then shifts two linear factors to derive polynomial rotational symmetry.',r'''The case $n=1$ is immediate. Assume $n>1$ and let $\omega$ be a primitive $n$th root of unity. Comparing the coefficient of $x^n$ shows that all $a_j$ are nonzero and their product is $1$. Normalize each factor to have $x$ coefficient $1$. Comparing the degree-$n$ homogeneous parts then yields, after reordering,
$$f(x)-g(y)=\prod_{j=1}^n(x-\omega^j y+\beta_j).$$
Choose shifts $u,v$ so that $u-v+\beta_n=0$ and $u-\omega v+\beta_1=0$; these have a unique solution because $\omega\ne1$. Set $F(x)=f(x+u)$ and $G(y)=g(y+v)$. Their difference has factors $x-y$ and $x-\omega y$. Substituting $x=y$ gives $F=G$, and substituting $x=\omega y$ gives $F(\omega y)=F(y)$.

Every coefficient of degree $1,\ldots,n-1$ in $F$ is therefore zero, because $\omega^k\ne1$ for these exponents. Monicity gives $F(x)=G(x)=x^n+c$. Reversing the shifts proves the required forms.''')
add('54bd4b',3,'Odd divisor count characterizes squares; their increasing gaps immediately prevent eventual periodicity.')
add('54d8bb',4.5,'Matches the two multisets by a permutation and follows each cycle to obtain unequal powers of the same nonzero number.',r'''Match the two equal multisets, retaining multiplicities, to obtain a permutation $\sigma$ satisfying $a_j^k=a_{\sigma(j)}^l$. If the cycle containing $j$ has length $t$, repeated substitution gives
$$a_j^{k^t}=a_{\sigma^t(j)}^{l^t}=a_j^{l^t}.$$
Since $a_j\ne0$ and $k^t\ne l^t$, this implies $a_j^{|k^t-l^t|}=1$. Thus every $a_j$ is a root of unity.''')
add('5bf86d',6.5,'A carefully weighted dot-product argument about the centroid is combined with a median-length bound.',r'''Let $G$ be the centroid and put $Q=GA^2+GB^2+GC^2=(a^2+b^2+c^2)/3$. Since $\overrightarrow{GA}+\overrightarrow{GB}+\overrightarrow{GC}=0$,
$$PA\,GA+PB\,GB+PC\,GC\ge\sum_{\mathrm{cyc}}\overrightarrow{PA}\cdot\overrightarrow{GA}=Q.$$
If $m_a$ is the median from $A$, then $GA=2m_a/3$. The median formula and $2uv\le u^2+v^2$ give
$$\sqrt3\,a m_a=\frac{\sqrt3a\sqrt{2b^2+2c^2-a^2}}2\le\frac{a^2+b^2+c^2}{2}.$$
Thus $a\,GA\le Q/\sqrt3$, and the corresponding bounds hold at $B,C$. Therefore
$$\frac{PA}{a}+\frac{PB}{b}+\frac{PC}{c}\ge\frac{PA\,GA+PB\,GB+PC\,GC}{\max(a\,GA,b\,GB,c\,GC)}\ge\sqrt3.$$''')
add('5c0da3',5,'Uses bounded deterministic dynamics to force a constant cycle, then preserves the gcd of adjacent terms.',r'''All terms are odd and positive, and $a_n\le(a_{n-1}+a_{n-2})/2\le\max(a_{n-1},a_{n-2})$. Thus every term is at most $\max(a,b)$. There are only finitely many possible ordered adjacent pairs, and the update is deterministic, so the sequence eventually repeats periodically.

Let $M$ be the largest term of this repeating cycle. Its two preceding terms $u,v$ satisfy $M\le(u+v)/2\le M$, forcing $u=v=M$. Two equal odd terms produce the same value again, so the periodic tail is constant at $M$.

The gcd of adjacent terms is invariant: removing a power of $2$ from the sum of two odd integers does not change its gcd with either odd summand. Hence $\gcd(a_{n-1},a_n)=\gcd(a,b)$ for every $n$. In the constant tail this gcd is $M$, which proves the result.''')
add('60c394',4.5,'A reflection construction or a compact coordinate reduction connects the angle condition to the given midpoint length.',json.loads((raw/'ind_2009_60c394.json').read_text())['solutions_markdown'][1])
add('707e31',4,'Recognizes the sum and product constraints as matching cubic coefficients, then evaluates their difference at the largest root.')
add('807378',4.5,'The key area decomposition gives a sum of three orthocenter-to-altitude ratios equal to two.',r'''Let $AD,BE,CF$ be the altitudes. Since $H$ is inside the acute triangle, area ratios give
$$\frac{AH}{AD}=\frac{[AHB]+[AHC]}{[ABC]}=1-\frac{[BHC]}{[ABC]}.$$
The analogous identities at $B,C$ sum to
$$\frac{AH}{AD}+\frac{BH}{BE}+\frac{CH}{CF}=2.$$
Each denominator is at most $h_{\max}$, so $(AH+BH+CH)/h_{\max}\le2$, as required.''')
add('84f562',4.5,'The coefficient denominators conceal a dilation telescoping identity; a sign-change argument then locates the root.',r'''Directly from the definitions, $f(x)=g(2x)-g(x)$. Consequently
$$f(1)+f(2)+\cdots+f(2^n)=g(2^{n+1})-g(1)=0.$$
If any of the first $n$ terms is zero, the desired root is already found. Otherwise these terms either include both signs, giving a root between two of their arguments, or all have the same sign. In the latter case $f(2^n)$ has the opposite sign, again giving a root strictly below $2^n$ by continuity.''')
add('88f876',5,'Combines the angle bisector geometry with Menelaus and a power-of-a-point identity to force a right angle.')
add('8bad34',5.5,'Translates pairwise divisibility into a product of residue classes; two coordinates force a common class, while three permit a CRT counterexample.',r'''For $n=2$, every prime triple works. For $n\ge3$, the property holds exactly when $p,q,r$ are not all distinct.

With one distinct prime the assertion is immediate. With two distinct primes $p,q$, suppose the numbers are not all congruent modulo $p$. Choose $a,b$ incongruent modulo $p$; they must be congruent modulo $q$. Any other number $c$ not congruent to them modulo $q$ would have to be congruent to both $a,b$ modulo $p$, impossible. Hence all the numbers are congruent modulo $q$.

For three distinct primes, use the Chinese remainder theorem to select positive integers with residue triples
$$(0,0,1),\quad(0,1,0),\quad(1,0,0)\pmod{(p,q,r)}.$$
Every pair agrees in one coordinate, but no coordinate is common to all three. For larger $n$, append further distinct positive representatives of the first residue triple, adding suitable multiples of $pqr$. These still satisfy pairwise divisibility and still have no common prime divisor of all differences. This gives the required counterexamples.''',topic='Number Theory')
add('95b288',6.5,'A substantial coefficient-extraction transformation and a finite geometric sum reduce the identity to half a binomial expansion.')
add('9d8a26',5.5,'The midpoint of the incenter segment is shown to lie on both circles by a delicate but short angle chase.',r'''Let $I$ be the incenter and let $T'$ be the midpoint of $AI$. Since $\angle A=60^\circ$, the right triangle formed by $I$ and an incircle contact point gives $AI=r/\sin30^\circ=2r$. Thus $AT'=IT'=r$, so $T'$ lies on the incircle.

Let $D,E,F$ be the midpoints of $BC,CA,AB$. The midpoint theorem gives $FT'\parallel BI$ and $ET'\parallel CI$. Together with $FD\parallel AC$ and $ED\parallel AB$, these imply
$$\angle T'FD=180^\circ-A-B/2,\qquad \angle T'ED=180^\circ-A-C/2.$$
Their sum is $180^\circ$, because $A=60^\circ$ and $B+C=120^\circ$. Hence $D,E,F,T'$ are concyclic, so $T'$ lies on the nine-point circle. It must therefore be the specified tangency point $T$, and $AT=r$.''',note='The stated tangency point presupposes distinct incircle and nine-point circle; the coincident equilateral case has no unique such point.')
add('a8f4a2',5.5,'Bounds the integer inradius, enumerates constrained reciprocal-altitude triples and then reconstructs the triangle areas.')
add('b6140d',5.5,'The least prime divisor and the multiplicative order of 3/4 modulo that prime force the prime to be 7.')
add('ca5154',3.5,'After shifting by one, the floor equation is solved directly on each integer interval.')
add('e883e8',6,'An unusual division by the two positive differences turns the cubic relation into a usable AM-GM bound.',r'''The hypothesis gives $c>a,b$. Since $a^3=(c-b)(c^2+cb+b^2)$ and similarly for $b^3$, we obtain
$$\frac{a^2+b^2-c^2}{(c-a)(c-b)}=\frac{c^2+cb+b^2}{ca}+\frac{c^2+ca+a^2}{cb}.$$
For completeness, combine $a^2/(c-b)+b^2/(c-a)$ over a common denominator; its numerator is $c(a^2+b^2)-(a^3+b^3)=c(a^2+b^2-c^2)$, which proves the identity.

Because $c>b$ and $c>a$, the inequalities $c^2+b^2>2cb$ and $c^2+a^2>2ca$ are strict. The displayed ratio is therefore greater than
$$3\left(\frac ba+\frac ab\right)\ge6.$$
Multiplying by the positive denominator proves the result.''')
add('f3300f',4.5,'The decisive finite configuration is a regular heptagon; pigeonhole and its four three-arc partitions complete the argument.',topic='Combinatorics')
add('f939c0',7,'Counts runs with specified parities by compositions, then collapses a nontrivial sum with Vandermonde’s identity.',topic='Combinatorics')
add('fec309',6,'Separates coprime factors and exponents, reducing the equation to a rigid exponential equation with just one solution.',r'''Let $d=\gcd(a,b)$, $a=dx$, $b=dy$, with $x,y$ coprime positive integers. Taking absolute values in the equation gives
$$d^y|x-y|^{x+y}=x^x.$$
Since $\gcd(x,|x-y|)=1$, necessarily $|x-y|=1$, and $d^y=x^x$. As $\gcd(x,y)=1$, comparison of prime exponents shows $x=k^y$ and $d=k^x$ for a positive integer $k$.

If $y=x+1$, then $k=1$ forces $x=1,y=2,d=1$, but the original equation has negative left side. For $k\ge2$, the equality $x=k^{x+1}$ is impossible. If $y=x-1$, then $x\ge2$ and $k\ge2$; for $x\ge3$, $k^{x-1}\ge2^{x-1}>x$. Thus $x=2$, $y=1$, $k=2$, $d=4$, giving $(a,b)=(8,4)$. Direct substitution verifies this pair, so it is the unique solution.''')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2));print(len(r))
