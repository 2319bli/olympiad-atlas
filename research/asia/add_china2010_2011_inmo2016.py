import json,pathlib
P=pathlib.Path('/workspace/sites/olympiad-atlas/research/asia');R=json.loads((P/'reviews.json').read_text())
def put(s,d,why,**kw):R[s]=dict(difficulty=d,reason=why,**kw)
put('chn_2011_833604',3,'If x+y<1 put z=1−x−y and apply (x+y)(y+z)(z+x)≥8xyz; otherwise the expression is nonpositive. Standard AM–GM gives maximum 1/8.')
put('chn_2011_debcf5',4.5,'Ordering the chosen integers reveals aᵢ₊₂≥2aᵢ, giving the sharp logarithmic bound; constructing two interleaved divisibility chains achieves 21.',statementOverride=r'Choose a subset $M\subseteq\{1,\ldots,2011\}$ so that every three distinct members include two for which one divides the other. What is the greatest possible size of $M$?',solutionOverride=r'''List the members increasingly as $a_1<\cdots<a_k$. If $a_{i+2}<2a_i$, no two of $a_i,a_{i+1},a_{i+2}$ divide one another. Hence $a_{i+2}\ge2a_i$. Were $k\ge22$, we would have $a_{22}\ge2^{10}a_2\ge2048$, impossible.

The bound $21$ is attained by
$$\{1,2,2^2,\ldots,2^{10}\}\ \cup\ \{3,6,3\cdot2^2,\ldots,3\cdot2^9\}.$$
Each of these two sets is a divisibility chain; any three chosen members contain two from the same chain.''')
put('chn_2011_135e53',5.5,'Construct a cyclic Gray-code ordering by reflection, then notice parity fixes every alternating sign and cancel each element contribution by toggling a different element. Construction and invariant are separate insights.',statementOverride=r'For $n\ge2$, prove that all subsets of $\{1,\ldots,n\}$ can be listed as $A_1,\ldots,A_{2^n}$ so that consecutive cardinalities differ by $1$, including the last and first. For every such cyclic listing, determine all possible values of $\sum_{i=1}^{2^n}(-1)^i\sum_{x\in A_i}x$.',solutionOverride=r'''For existence use the reflected Gray-code construction. Start with the cyclic list $\varnothing,\{1\}$. From a list $B_1,\ldots,B_{2^k}$ beginning with $\varnothing$, form
$$B_1,\ldots,B_{2^k},\ B_{2^k}\cup\{k+1\},\ldots,B_1\cup\{k+1\}.$$
Neighbours differ by one element, including the junctions and the last-to-first junction. Induction gives the required listing.

In any admissible listing, cardinality parity alternates, so the desired sum is, up to an overall sign,
$$\sum_{A\subseteq\{1,\ldots,n\}}(-1)^{|A|}\sum_{x\in A}x.$$
Fix an element $x$ and another element $y\ne x$. Among subsets containing $x$, toggling $y$ pairs one even and one odd cardinality subset. Thus the coefficient of $x$ in the sum is zero. Every element cancels, and the only possible value is $0$.''')
put('chn_2011_002f2e',4,'An odd cycle cannot alternate residues 1 and 3 modulo 4; the possible exceptional prime 2 needs a separate endpoint check, which produces the same parity obstruction.',statementOverride=r'Can an odd number $n\ge3$ of distinct primes be arranged cyclically so that the sum of every two neighbours is a perfect square? Prove your answer.',solutionOverride=r'''No. If all primes are odd, neighbouring sums are even squares and hence divisible by $4$. The residues of the primes must therefore alternate between $1$ and $3$ modulo $4$, impossible around an odd cycle.

Otherwise exactly one prime is $2$. Each of its two neighbours is $3\pmod4$, since an odd square is $1\pmod4$. The remaining $n-1$ odd primes form a path whose residues alternate. A path with an even number of vertices has opposite endpoint residues, contradicting the fact that both endpoints are $3\pmod4$.''')
put('chn_2011_6ce2fb',4,'Reviewed the same modulo-4 argument; this is a second transcription of CWMO 2011 Q5, with faulty cyclic indices.',omitReason='Duplicate of chn_2011_002f2e, the same CWMO 2011 Q5; retained only once in the bank.')
put('chn_2011_80acb2',5,'Substitute arbitrarily large primes to force a+b²=0, then twice a large prime to force b+1=0. Turning infinitely many divisibilities into exact integer equalities is the central insight.',statementOverride=r'Find every integer pair $(a,b)$ such that $n\mid a^n+b^{n+1}$ for every positive integer $n$.',solutionOverride=r'''If $b=0$, every prime divides $a$ by Fermat, so $a=0$. Now assume $b\ne0$. For every sufficiently large prime $p$, Fermat gives
$$0\equiv a^p+b^{p+1}\equiv a+b^2\pmod p.$$
An integer divisible by arbitrarily large primes is zero, hence $a=-b^2$.

Take $n=2q$, where $q$ is any sufficiently large prime not dividing $b$. Modulo $q$ the condition becomes
$$0\equiv b^{4q}+b^{2q+1}\equiv b^4+b^3=b^3(b+1).$$
Thus arbitrarily large primes divide $b+1$, forcing $b=-1$ and $a=-1$. Both $(0,0)$ and $(-1,-1)$ satisfy the required divisibilities.''',note='Corrected the exponent n−1 in the MathNet statement to n+1, as in its solution and the complete CWMO 2011 paper, AoPS collection 5205.')
put('chn_2010_3a1cdd',3.5,'Every summand is at most 1/2 because distinct intersecting sets have maximum size at least 2. Alternating singletons and consecutive pairs attains n; a straightforward sharp-bound construction.')
put('chn_2010_d1b8aa',5.5,'The reverse construction of F, a new cyclic quadrilateral through E,M,D, and the two isosceles angle identities make a compact but genuinely inventive geometry proof.',statementOverride=r'In an isosceles triangle $ABC$ with $AB=AC$, let $D$ be the midpoint of $BC$. Choose $E$ outside $ABC$ with $CE\perp AB$ and $BE=BD$, and let $M$ be the midpoint of $BE$. On the minor arc $AD$ of the circumcircle of $ABD$, choose $F$ with $MF\perp BE$. Prove $ED\perp FD$.',solutionKind='source-link')
put('chn_2010_b8733d',5.5,'Expanding the nested weighted expression reveals a product of weighted arithmetic and reciprocal means. A sharp endpoint bound k+n/k≤n+1 plus AM–GM proves it and identifies equality.',statementOverride=r'Let $n\ge2$ and $x_1,\ldots,x_n\in\mathbb R$ satisfy $\sum_{i=1}^n x_i^2=1$. Prove that $$\sum_{k=1}^n\left(1-\frac{k}{\sum_{i=1}^n i x_i^2}\right)^2\frac{x_k^2}{k}\le\left(\frac{n-1}{n+1}\right)^2\sum_{k=1}^n\frac{x_k^2}{k},$$ and find all equality cases.',solutionOverride=r'''Set $A=\sum kx_k^2$ and $B=\sum x_k^2/k$. Expanding the left side gives $B-1/A$. Thus the desired inequality is equivalent to
$$4nAB\le(n+1)^2.$$
For $1\le k\le n$, $(k-1)(n-k)\ge0$, so $k+n/k\le n+1$. Therefore
$$4nAB\le(A+nB)^2=\left(\sum_{k=1}^n(k+n/k)x_k^2\right)^2\le(n+1)^2.$$
Equality in the second step requires $x_2=\cdots=x_{n-1}=0$. Equality in the first requires $A=nB$, which then gives $x_1^2=x_n^2$. Along with the normalisation, the equality cases are $x_1^2=x_n^2=1/2$ and all intervening variables zero.''',note='The worked solution corrects several transcription slips in the source expansion and its equality statement.')
put('chn_2010_8ae09b',3.5,'The integer preimages of two increasing affine functions have equal least positive spacing, so their slopes agree and intercepts differ by an integer. A short arithmetic-progression argument.')
put('chn_2010_6536f0',6.5,'The sharp bound needs a deletion induction: three insertion positions would realise all three possible middle elements of one triple. The matching construction inserts each new maximum at an endpoint.',statementOverride=r'Let $n\ge3$. A family $\mathcal P$ of distinct permutations of $\{1,\ldots,n\}$ has this property: for every three distinct labels, one of them is never between the other two in any member of $\mathcal P$. Determine the largest possible size of $\mathcal P$.',solutionOverride=r'''The answer is $2^{n-1}$.

For the upper bound, delete the label $n$ from every permutation. The distinct resulting permutations still satisfy the condition. A single resulting order can have at most two preimages: if $n$ were inserted into three different gaps, choose a label $u$ between the first and second gaps and a label $v$ between the second and third. In the three orders, respectively, $u,n,v$ would each occur between the other two, a contradiction. Induction therefore gives $M_n\le2M_{n-1}$, with $M_2=2$, hence $M_n\le2^{n-1}$.

To attain this, start with $1$ and insert $2,3,\ldots,n$ successively, each at either end of the existing order. This produces $2^{n-1}$ distinct permutations. For every triple $a<b<c$, the largest label $c$ is never between $a,b$, because it was inserted at an end. Thus the construction works.''')
put('chn_2010_49eb42',7.5,'The minimum 261 is proved by a Pell-equation restriction and several residue/nonresidue cases for the common odd difference. The exhaustive number-theoretic analysis is substantially beyond the target band.')
url='https://olympiads.hbcse.tifr.res.in/wp-content/uploads/2026/10/sol-inmo16.pdf'
def ind(s,d,why,**kw):put(s,d,why,competitionOverride='Indian National Mathematical Olympiad (INMO)',sourceUrl=url,solutionUrl=url,**kw)
ind('ind_2016_03926f',4.5,'Using the symmetry axis, the orthocentre must be the top endpoint of the incircle diameter. A short coordinate or midpoint-similarity argument then fixes the side ratio.',solutionOverride=r'''Scale and place $B=(-1,0)$, $C=(1,0)$, $A=(0,h)$ with $h>0$. The orthocentre is $H=(0,1/h)$. Writing $s=\sqrt{1+h^2}$ for $AB$, the inradius is area/semiperimeter, namely $r=h/(s+1)$.

The incircle meets the symmetry axis at heights $0$ and $2r$. Since $H$ has positive height, $1/h=2r$. Thus $s+1=2h^2=2(s^2-1)$, or $(s+1)(2s-3)=0$. Hence $s=3/2$ and $AB/BC=s/2=\boxed{3/4}$. This gives a valid triangle and satisfies the original condition.''')
ind('ind_2016_346a97',4.5,'A counterexample to (I) comes from setting two variables equal and finding the golden ratio. For (II), choosing a maximum variable makes the cyclic equalities force all three equal.',solutionOverride=r'''Condition (I) does not suffice. Let $\varphi=(1+\sqrt5)/2$ and choose $a=b=\varphi$, $c=1$. Since $\varphi^2=\varphi+1$ and $\varphi^3=2\varphi+1$, direct substitution gives equality of all three expressions.

Condition (II) does suffice. By cyclic relabelling, take $a\ge b,c$. If $a>b$, then
$$a(a^3+b^3)=b(b^3+c^3)$$
forces $a^3+b^3<b^3+c^3$, hence $a<c$, a contradiction. Therefore $a=b$, and the same equality immediately gives $a=c$.''')
ind('ind_2016_6675c0',5,'The descent to 1 is easy, but counting iterated preimages requires a clean even/odd decomposition and a second-order recurrence. This matches the calibrated Fibonacci-type BMO1 difficulty.',solutionOverride=r'''If $n>1$ is even, $T(n)=n/2<n$. If $n>1$ is odd, $T^2(n)=(n+1)/2<n$. Strong induction proves eventual arrival at $1$.

Let $S_k=\{n:T^k(n)=1\}$ and let $e_k$ count its even members. Every $m\in S_k$ has the even preimage $2m$. It also has the odd preimage $m-1$ exactly when $m$ is even. Hence
$$c_{k+1}=c_k+e_k,\qquad e_{k+1}=c_k.$$
It follows that $c_{k+2}=c_{k+1}+c_k$. For example $S_1=\{2\}$ and $S_2=\{1,4\}$, consistent with $c_1=1,c_2=2$.''',note='Corrected a source slip claiming that 4 is the only two-step preimage of 1; 1 is also a two-step preimage.')
ind('ind_2016_0822ff',2.5,'Rotate any regular n-gon: only finitely many rotation angles hit a red point, so another angle works. Alternatively use 2017 disjoint regular n-gons and pigeonhole; below target.')
ind('ind_2016_5b4ea3',5.5,'Equal inradii relate both the two subtriangle areas and their contact lengths. Comparing two formulas for r′/r gives BD²=rs, after which the reciprocal identity follows.',solutionOverride=r'''Put $b=AC$, $d=BD$, and let $s$ be the semiperimeter of $ABC$. Let the two smaller incircles touch $AC$ at $P,Q$, and let the large incircle touch it at $X$. Comparing tangent lengths along the common angles at $A,C$ gives
$$\frac{r'}r=\frac{AP}{AX}=\frac{CQ}{CX}=\frac{AP+CQ}{b}.$$
If the smaller semiperimeters are $s_1,s_2$, then $s_1+s_2=s+d$ and $AP+CQ=(s_1-d)+(s_2-d)=s-d$. Thus $r'/r=(s-d)/b$.

Adding the two smaller areas also gives $r'(s+d)=rs$, so $r'/r=s/(s+d)$. Comparing yields $s^2-d^2=bs$, or $d^2=s(s-b)$. Because $ABC$ is right-angled, $r=s-b$, and hence $d^2=rs$.

Finally
$$\frac1{r'}=\frac{s+d}{rs}=\frac1r+\frac d{rs}=\frac1r+\frac1d,$$
as required.''')
ind('ind_2016_ce710c',6.5,'First prove rationality from two linear equations; then show pa and qa satisfy monic integer quadratics. Rational-root integrality and two coprimality arguments force both the initial term and common difference to be integers.',solutionOverride=r'''Write the progression as $a+jd$ for $j\ge0$, with $d\ne0$. There are nonnegative integers $k,l,m$ such that
$$a^2=a+kd,\quad(a+pd)^2=a+ld,\quad(a+qd)^2=a+md.$$
Subtracting the first relation from the other two and dividing by $d$ gives
$$2pa+p^2d=l-k,\qquad2qa+q^2d=m-k.$$
Since $p\ne q$, these equations have nonzero determinant, so $a,d$ are rational.

Multiplying $a^2=a+kd$ by $p^2$ and eliminating $p^2d$ shows that $pa$ satisfies
$$X^2-(p-2k)X-k(l-k)=0.$$
A rational root of a monic integer polynomial is an integer. Thus $pa\in\mathbb Z$; similarly $qa\in\mathbb Z$. As $\gcd(p,q)=1$, Bézout gives $a\in\mathbb Z$.

The two linear equations now show $p^2d,q^2d\in\mathbb Z$. Since $\gcd(p^2,q^2)=1$, another use of Bézout gives $d\in\mathbb Z$. Every term is therefore an integer.''')
(P/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
