from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research');r=json.loads((p/'international-reviews.json').read_text())
r.update({
'btw_2023_236a65':[3,'A direct application of Holder, or weighted Jensen to the power three-halves, gives the entire inequality.'],
'btw_2023_f8098f':[5.5,'Subtracting consecutive sum identities gives a doubling recurrence; parity strengthens strict increase to gaps of two, after which strong induction forces the sequence.'],
'btw_2023_c5f4ad':[5,'The useful route is a contrapositive: isolate the unique term at least one, bound it using a binomial estimate, and split the remaining exponents at the midpoint.'],
'btw_2023_c14e22':[5,'Cubing and subtracting the constant term produces a monotone additive function; substitution then reduces the classification to a polynomial identity.'],
'btw_2023_3a179b':[5.5,'Reciprocal symmetry provides two disjoint injections for the lower bound; the upper bound comes from counting binary expression trees with two operation types.'],
'btw_2023_22414b':[4,'Parity controls which variable dominates, while odd exponents require a sign-reversal counterexample with three distinct coordinates.'],
'btw_2023_9cdd34':[3.5,'Multiplying the cyclic constraints, applying AM-GM and then the vector triangle inequality gives the sharp value directly.'],
'btw_2023_49de42':[4.5,'The sharp constant requires both a twice-squared inequality and a limiting family close to equality; it is more than a direct mean inequality.'],
'btw_2023_100db6':[5,'Freeing the product variable forces the third iterate to be linear, after which the excluded points in the domain determine the remaining constant.'],
'btw_2023_78199f':[4,'The coefficients suggest two different weighted AM-GM applications; discovering the matching factorisations of 2023 is the main step.'],
'btw_2023_955aea':[5.5,'Specialisations force invariance on prime powers and multiplicativity on coprime inputs; the answer is a family indexed by arbitrary subsets of primes.'],
'btw_2023_90f36a':[6,'First classify the possible trailing octal carries for x, then translate carries for y into a decimal divisibility equation and eliminate the remaining patterns.'],
'btw_2023_63fd11':[4.5,'A finite Fibonacci generating-sum identity produces a long block of trailing binary ones; a simple growth bound then controls all other digits.'],
'btw_2023_566210':[5,'The construction combines positive and negative squares and uses primes congruent to three modulo four to keep both polynomial images nonzero and disjoint.'],
'btw_2023_641459':[6.5,'A necessary-and-sufficient prime-factor criterion for complete divisor subset sums is the conceptual core; it then settles factorials and large powers.'],
'btw_2023_ca27be':[4.5,'The binomial expansion must be retained modulo the square of the prime, requiring control of each coefficient after removing its single prime factor.'],
'btw_2023_79a624':[3,'The standard product formulas for divisor count and Euler phi make each prime factor contribute at least one, with equality immediately classified.'],
'btw_2023_db4b31':[5.5,'A digit-length estimate sharply bounds both parameters; congruences modulo nine reduce the remaining search to a short explicit check.'],
'btw_2023_73ec51':[7,'The large-image case is pigeonhole; the equality case needs a multiplicative subgroup argument, identification of quadratic residues, and a nonzero difference-of-squares construction.'],
'btw_2023_aaf831':[6.5,'The difficult insight is to bound gaps between nonzero digits using powers of two dividing truncated decimal expansions, then iterate this bound.'],
'btw_2023_a9bf63':[5.5,'The colour adjacency graph must be a path or cycle. Central grid cells give a radius bound, with a separate repeated-diagonal-colour case when n is even.'],
'btw_2023_38796d':[5,'Alternating coordinate changes give divisibility by four; excluding length eight and constructing every later multiple require separate geometric arguments.'],
'btw_2023_409ecd':[6,'One case needs a permutation avoiding the four multiples of 13; the other needs a primitive-root construction whose exponent sum is independent of the rook placement.'],
'btw_2023_f1476e':[6,'Successive largest-prime reports almost determine the walk; handling the exceptional houses two and four and enumerating initial states yields a finite capture strategy.'],
'btw_2023_8b7d30':[7.5,'A sharp extremal area bound needs rotated coordinates, parity-sensitive boundary estimates and a nontrivial explicit construction.'],
'btw_2023_bff74d':[4.5,'The key construction uses the altitude of a right triangle with leg ratio ten, followed by a square-number subdivision of one similar piece.'],
'btw_2023_227d69':[4.5,'A parity invariant rules out odd sizes; a two-step reduction reduces the constructive direction to a four-point configuration.'],
'btw_2023_1f3051':[5.5,'Translate both word counts into finite power sums; the quadratic binomial coefficients have vanishing third differences, giving the high-power congruence.'],
'btw_2023_b9b607':[5,'A region-count induction gives a quadratic upper bound; generic rotations of congruent triangles attain it without triple intersections.'],
'btw_2023_2631fd':[4.5,'Label the blocks to convert partitions into surjections, then apply inclusion-exclusion and Fermat before cancelling a factorial modulo p.'],
'btw_2023_58a295':[3,'A short backward game table, organised by residues modulo six until the first exceptional square, determines the winner.'],
'btw_2023_b1cac2':[5.5,'Two spiral similarities link the reflected excentre to the altitude foot; their angle identities produce the required cyclicity.'],
'btw_2023_6c3187':[4.5,'Two incenter/circumcenter angle calculations reveal one cyclic quadrilateral; an angle bisector then gives the equal chords.'],
'btw_2023_efdb2f':[6.5,'The angle condition must be converted into a metric relation involving the inradius and altitude; a coordinate proof uses tangent subtraction and the semiperimeter.'],
'btw_2023_f3f121':[6,'The circumcentres are best handled through scalar products with centroid at the origin; both X and the midpoint of EF lie on the perpendicular bisector of BC.'],
'btw_2023_2c5c1f':[5.5,'Tangent-chord angles place five points on one circle, while equal tangent lengths produce a second cyclic quadrilateral through power of a point.'],
'bmo_2023_83afda':[5.5,'A useful incircle contact-chord lemma forces a right angle in the original triangle; applying the same lemma again finishes the unusual incidence claim.'],
'bmo_2023_e5c358':[9,'The polynomial classification needs a Schur-type prime-divisor lemma and a substantial simultaneous-prime construction, well outside the target band.'],
'bmo_2023_be5fcc':[7.5,'After the extremal sum bound, the difficult direction needs complementary target sums, many disjoint pairs and delicate small-remainder estimates.']
})
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
o=json.loads((p/'international-extra-solutions.json').read_text())
o.update({
'btw_2023_c14e22':r'''The solutions are the constants $0,\sqrt2,-\sqrt2$ and the functions $f(x)=\sqrt[3]x$, $f(x)=-\sqrt[3]x$.

Put $c=f(0)$. Substitution at zero gives $c^3=2c$, and substitution $y=0$ gives $f(x^3)=f(x)^3-c$. Thus $h(x)=f(x)^3-2c$ satisfies $h(x+y)=h(x)+h(y)$. It is monotone because $f$ is monotone. The usual rational approximation argument for a monotone additive function gives $h(x)=kx$ for some real $k$.

Consequently $f(x)^3=kx+2c$ and $f(x^3)=kx+c$. Cubing the latter identity and applying the former at $x^3$ gives
$$(kx+c)^3=kx^3+2c\quad\hbox{for every real }x.$$
Comparison of coefficients yields $k^3=k$, $k^2c=0$, and $c^3=2c$. If $c=0$, then $k=0,1,-1$ and the three stated cube-root functions result. If $c\ne0$, then $k=0$ and $f$ is the constant $c=\pm\sqrt2$. Direct substitution checks all five possibilities.''',
'btw_2023_3a179b':r'''Think of each element of $A_n$ as the value of a fully parenthesised expression using exactly $n$ copies of one and the two binary operations
$$u+v,\qquad u\mathbin{\|}v=(u^{-1}+v^{-1})^{-1}.$$
Induction shows that every $A_n$ is closed under reciprocals: taking a reciprocal interchanges the two operations and reciprocates each input.

For every $x\in A_n$, both $1+x$ and $1/(1+x)$ belong to $A_{n+1}$. Each of these two maps is injective, and their images lie respectively above and below one. Therefore $|A_{n+1}|\geq2|A_n|$, proving $|A_n|\geq2^{n-1}$.

For the upper bound, the expression has a rooted ordered binary tree with $n$ leaves and $n-1$ internal nodes. Its preorder list of leaf/internal-node symbols determines its shape, so there are fewer than $2^{2n-1}$ possible shapes. There are at most $2^{n-1}$ choices of operations at the internal nodes. Every element has at least one such expression, hence
$$|A_n|\leq2^{2n-1}2^{n-1}<8^n.$$
Different expressions may have the same value, which only strengthens this upper bound.''',
'btw_2023_100db6':r'''The unique solution is $f(x)=1/(1-x)$ on $D$.

Putting $y=a/x$ shows
$$f(f(a))=1-\frac{x}{a f(f(f(x)))}\qquad(a,x\in D).$$
Hence $x/f(f(f(x)))$ is a fixed nonzero constant, say $1/C$. Thus
$$f(f(f(x)))=Cx,\qquad f(f(x))=1-\frac1{Cx}.$$
Replace $x$ by $f(x)$ in the second identity to obtain
$$Cx=1-\frac1{Cf(x)},\qquad f(x)=\frac1{C(1-Cx)}.$$
Because $f$ is defined at every $x\in D$, its denominator cannot vanish there. Thus $1/C$ must be either zero or one. It is nonzero, so $C=1$. The resulting function maps $D$ to itself, has third iterate equal to the identity, and satisfies the given equation directly.''',
'btw_2023_955aea':r'''Choose an arbitrary set $\mathcal P$ of primes. The solutions are exactly
$$f(n)=\prod_{\substack{p\mid n\\p\in\mathcal P}}p,$$
with an empty product equal to one.

Since $f(1)\mid1$, we have $f(1)=1$. Setting $m=1$ in the equation gives $f(n^2)=f(n)$ for every $n$. For a prime $p$, $f(p)$ is either one or $p$. The equation with $n=p,m=p^j$ now proves inductively that $f(p^j)=f(p)$ for every $j\geq1$.

If $\gcd(u,v)=1$, then $f(u)\mid u$ and $f(v)\mid v$ imply that $u f(u)$ and $f(v)$ are coprime. The equation with $n=u,m=v$ therefore gives
$$u f(uv)=\operatorname{lcm}(u f(u),f(v))=u f(u)f(v).$$
Thus $f$ is multiplicative on coprime arguments, proving the displayed classification.

Conversely, check the original equation prime by prime. For a selected prime, the exponent in $f(nm)$ is one precisely when it divides $n$ or $m$; the maximum of the two exponents on the lcm side is exactly its exponent in $n$ plus this indicator. For an unselected prime both sides have just its exponent in $n$. Divisibility $f(n)\mid n$ is immediate.''',
'btw_2023_63fd11':r'''Let $S_n=\sum_{i=1}^n(-2)^{i-1}F_i$. A direct induction using the Fibonacci recurrence gives, for $n\geq2$,
$$S_n=-(-2)^nF_{n-2}-1.$$
Indeed it holds at $n=2$, and adding $(-2)^nF_{n+1}$ changes the right-hand side to $(-2)^n(F_{n+1}-F_{n-2})-1=2(-2)^nF_{n-1}-1$.

For $n=2023$ this gives $N=2^{2023}F_{2021}-1$. Thus the last 2023 binary digits are all ones. Also $F_{2021}<2^{2020}$, so $N<2^{4043}$. It has at most 4043 binary digits, of which at least 2023 are ones and at most 2020 are zeros. This proves the claim.''',
'btw_2023_566210':r'''Take $f(x)=(x^2+1)^2$ and $g(y)=-(y^2+1)^2$.

For a prime $p\equiv3\pmod4$, minus one is not a square modulo $p$. Therefore $u^2+v^2\equiv0\pmod p$ forces $u\equiv v\equiv0$: if $v\ne0$, division by $v^2$ would make minus one a square.

If $f(x)\equiv g(y)\pmod p$, apply this fact to $u=x^2+1$, $v=y^2+1$. It gives $x^2\equiv-1\pmod p$, a contradiction. The two images are therefore disjoint.

Finally, infinitely many such primes exist by the standard Euclid argument: if they were $p_1,\ldots,p_k$, the number $4p_1\cdots p_k-1$ would have a prime divisor congruent to three modulo four, different from every $p_i$.''',
'btw_2023_ca27be':r'''For $1\leq k\leq p-1$, use
$$k\binom pk=p\binom{p-1}{k-1}\equiv p(-1)^{k-1}\pmod{p^2}.$$
The last congruence follows by reducing the product formula for $\binom{p-1}{k-1}$ modulo $p$. Also $\binom pk$ is divisible by $p$. Dividing the identity by $p$ and using $ka_k\equiv1\pmod p$ gives
$$\frac1p\binom pk\equiv(-1)^{k-1}a_k\pmod p.$$
Sum over $k=1,\ldots,p-1$ and multiply by $p$. The binomial theorem gives the sum on the left as $2^p-2$, proving the required alternating congruence.''',
'btw_2023_73ec51':r'''All arithmetic below is in the field modulo $p$. Put $P=\{ab:a,b\in A\}$. Choosing a nonzero element of $A$ shows $|P|\geq|A|$. If $|P|\geq(p+1)/2$, then $P$ and $r+P$ intersect by pigeonhole, proving the assertion.

The remaining case has $|P|=|A|=(p-1)/2$. Scale $A$ by a nonzero constant so that $1\in A$; the assertion is invariant under this scaling because products scale by its square. Now $A\subseteq P$, so $A=P$. Its nonzero elements form a multiplicative subgroup, since a finite nonempty set of nonzero elements closed under multiplication is a group.

If $0\in A$, this subgroup has order $(p-3)/2$. Its order divides $p-1$, hence divides two, which is impossible for $p>7$. Therefore $A$ itself is a subgroup of order $(p-1)/2$. Every element satisfies $x^{(p-1)/2}=1$. The nonzero squares also give exactly $(p-1)/2$ roots of this polynomial, so $A$ is precisely the set of nonzero squares.

For $r=0$ use identical products. Otherwise choose a nonzero $t$ with $t^2\ne r,-r$, possible because at most four nonzero elements are forbidden and $p-1>4$. Then
$$a=\left(\frac{t+r/t}{2}\right)^2,\qquad c=\left(\frac{t-r/t}{2}\right)^2$$
are nonzero squares and satisfy $a-c=r$. With $b=d=1$, this proves the claim.''',
'btw_2023_a9bf63':r'''The maximum is $2n-1$, except that it is four for $n=2$. Colour cell $(i,j)$ by $i+j$ to attain $2n-1$; each colour then touches only its immediate predecessor and successor. The case $n=2$ allows four distinct colours.

Form the graph whose vertices are colours, joining colours that touch. It is connected and every degree is at most two, so it is a path or a cycle. A path or cycle in which every vertex is at distance at most $r$ from some fixed vertex has at most $2r+1$ vertices.

For odd $n$, every cell is within $n-1$ grid steps of the central cell. Thus every colour is within graph distance $n-1$ of its colour, giving at most $2n-1$ colours.

For even $n$, inspect the central four cells. If two adjacent ones have the same colour, every cell is within $n-1$ steps of at least one of this pair, giving the same bound. If an opposite pair has the same colour but no adjacent pair does, the other two colours either coincide, giving at most two colours in the connected degree-two graph, or are distinct, giving a three-cycle and hence exactly three colours. If all four central colours differ, they form a four-cycle, so there are exactly four colours. Combining these cases proves the bound.''',
'btw_2023_1f3051':r'''Set $N=2023$. Counting by length gives
$$|B|=\sum_{k=0}^N9^k,\qquad |M|=\sum_{k=0}^N\binom{k+2}{2}3^k.$$
In the second formula, choose the two positions of the letter $t$ in a word of length $k+2$, then choose any of three letters at each remaining position.

The coefficients $\binom{k+2}{2}$ have zero third finite difference. Consequently, multiplication and cancellation of coefficients give the polynomial congruence
$$(1-z)^3\sum_{k=0}^N\binom{k+2}{2}z^k\equiv1\pmod{z^{N+1}}.$$
Put $z=3$ to obtain $-8|M|\equiv1\pmod{3^{N+1}}$. The geometric-sum identity also gives $8|B|=9^{N+1}-1\equiv-1\pmod{3^{N+1}}$. Subtract and cancel eight, which is coprime to three. The difference is in fact divisible by $3^{2024}$, and hence by $3^{2023}$.''',
'btw_2023_f3f121':r'''Use the centroid $G$ as vector origin. Write the vectors of $A,B,C$ as $a,b,c$, so $a+b+c=0$. Use lower-case vectors for the other points too. Since the circumcircles in the problem pass through the origin, their centres satisfy
$$2d\cdot b=|b|^2,\quad2d\cdot c=|c|^2,$$
$$2e\cdot a=2f\cdot a=|a|^2,\quad2e\cdot c=|c|^2,\quad2f\cdot b=|b|^2.$$
Let $v=c-b$ and $m=(e+f)/2$, the midpoint vector of $EF$. The first two identities give
$$d\cdot v=\frac{|c|^2-|b|^2}{2}.$$
Using $a+b+c=0$ in the remaining identities gives the same formula for $m\cdot v$.

The defining perpendiculars through $X$ give $x\cdot(b-a)=e\cdot(b-a)$ and $x\cdot(c-a)=f\cdot(c-a)$. Subtract them to obtain
$$x\cdot v=f\cdot(c-a)-e\cdot(b-a)=\frac{|c|^2-|b|^2}{2}.$$
Hence $D,X$ and the midpoint of $EF$ all lie on the line $z\cdot v=(|c|^2-|b|^2)/2$, the perpendicular bisector of $BC$. Thus $DX$ bisects $EF$.''',
'btw_2023_efdb2f':r'''Put $B=(0,0)$, $C=(a,0)$ and $A=(u,v)$, with $v>0$. Write $b=CA$, $c=AB$, $s=(a+b+c)/2$ and $r=ID$. Acuteness gives $0<u<a$, and $c<b$ gives $u<a/2$.

The contact point is $D=(s-b,0)$, and the orthocentre is $H=(u,h)$ with $h=u(a-u)/v$. Moreover
$$s-b-u=\frac{a-2u+c-b}{2}=\frac{(a-2u)(s-a)}{b+c}>0,$$
where we used $b-c=a(a-2u)/(b+c)$. Taking tangents in the given angle equality therefore yields
$$\frac{s-b-u}{h}=\tan(B-C)=\frac{v(a-2u)}{u(a-u)+v^2}.$$
Substitute the expressions above and cancel the positive factors. The result is
$$(s-a)v^2=s\,u(a-u),\qquad \frac hv=\frac{s-a}{s}.$$
Since $AH=v-h$, it follows that $AH=av/s$. Finally the area identity $rs=av/2$ gives $AH=2r=2ID$.''',
'bmo_2023_83afda':r'''We use the following lemma: if $D,E,F$ are the incircle contact points of triangle $ABC$, and $I$ is its incentre, then $S=EF\cap BI$ lies on the circle with diameter $BC$. Indeed, angle chasing gives $\angle BIC=\angle EFC$, so $S,F,I,C$ are concyclic. Since $IF\perp FC$, this circle has diameter $IC$, and therefore $\angle ISC=90^\circ$. As $B,I,S$ are collinear, the lemma follows.

Applying the lemma to both bisectors $BI,CI$, the two intersections of $EF$ with the circle of diameter $BC$ lie on those bisectors. But $\angle BXC=90^\circ$, so $X$ is one of these intersections. Thus either $BX$ or $CX$ bisects its corresponding angle. Because each makes $45^\circ$ with $BC$, either $B$ or $C$ is a right angle.

Assume $B=90^\circ$. The arc midpoint $M$ lies on $AI$, and $\angle AMC=90^\circ$ because $AC$ is a diameter. Apply the same lemma with the vertex labels permuted: $AI\cap DF$ lies on the circle of diameter $AC$. Its second intersection with $AI$ is $M$, proving $M\in DF$. The case $C=90^\circ$ similarly gives $M\in DE$.'''
})
# Retain complete sourced arguments with local transcription repairs.
raw=p/'international-raw'
for slug in ['btw_2023_db4b31','btw_2023_b1cac2','btw_2023_2631fd']:
 d=json.loads((raw/(slug+'.json')).read_text());s=d['solutions_markdown'][0]
 if slug=='btw_2023_db4b31':s=s.replace('Let us consider the case', 'Let $k$ be the number of decimal digits of $a$. Then $10^{(k-1)b}\\leq a^b=S(a^{b+1})\\leq9k(b+1)$.\n\nLet us consider the case')
 if slug=='btw_2023_b1cac2':s=s.replace('since $BJ$ bisects $\\angle CBA$','since the line $BJ$ is the external angle bisector at $B$')
 if slug=='btw_2023_2631fd':s=s.split('\n\nLemma:')[0]
 o[slug]=s
(p/'international-extra-solutions.json').write_text(json.dumps(o,ensure_ascii=False,indent=2))
