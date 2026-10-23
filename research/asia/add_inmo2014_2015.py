import json,pathlib
P=pathlib.Path('/workspace/sites/olympiad-atlas/research/asia');R=json.loads((P/'reviews.json').read_text())
def put(s,d,why,**kw):
 year=s.split('_')[1];url='https://olympiads.hbcse.tifr.res.in/wp-content/uploads/2026/10/'+('inmo-2014.pdf' if year=='2014' else 'inmosol-15.pdf')
 R[s]=dict(difficulty=d,reason=why,sourceUrl=url,solutionUrl=url,**kw)
put('ind_2014_da207b',4.5,'A cyclic trapezoid of centroids supplies equal medians, hence equal sums of squares. Combining this with the given sum and excluding the swapped-root case by the triangle inequality takes several linked observations.',solutionOverride=r'''Let $G_1,G_2$ be the two centroids. Since $G_1G_2\parallel BC$, the cyclic trapezoid $BG_1G_2C$ is isosceles, so $BG_1=CG_2$.

The median-length formula gives
$$9BG_1^2=2AB^2+2BD^2-AD^2,$$
$$9CG_2^2=2AC^2+2CD^2-AD^2.$$
Hence $AB^2+BD^2=AC^2+CD^2$. Together with $AB+BD=AC+CD$, this says that the unordered pairs $\{AB,BD\}$ and $\{AC,CD\}$ coincide. The swapped possibility $AB=CD$, $AC=BD$ would give $AB+AC=BC$, impossible for a triangle. Therefore $AB=AC$.''')
put('ind_2014_7f7e39',4,'Interpret the floor sum as lattice points under ij≤n, then pair (i,j) with (j,i). The unpaired diagonal consists of exactly floor(sqrt(n)) points.',solutionOverride=r'''The sum $S=\sum_{i=1}^n\lfloor n/i\rfloor$ counts ordered pairs of positive integers $(i,j)$ with $ij\le n$. Every pair with $i\ne j$ is paired with the distinct pair $(j,i)$. The remaining pairs are $(i,i)$ with $i\le\sqrt n$, so there are $\lfloor\sqrt n\rfloor$ of them. Thus $S\equiv\lfloor\sqrt n\rfloor\pmod2$, proving the result.''')
put('ind_2014_7fcb78',4.5,'Bound gcd+lcm by ab+1 and use integrality to reduce a hypothetical failure to |a−b|≤1. A small divisibility obstruction and precise equality cases finish it.',solutionOverride=r'''Let $g=\gcd(a,b)$ and $l=\operatorname{lcm}(a,b)$. Since $(g-1)(l-1)\ge0$ and $gl=ab$, we have $g+l\le ab+1$.

If $|a-b|\ge2$, then $ab+1\le(a+b)^2/4$, giving the desired bound. If $a=b$, the quotient is $1$, and $ab>2$ gives $a=b\ge2$. If, say, $a=b+1$, divisibility would give
$$2b+1\mid b^2+b+1,$$
hence $2b+1\mid4(b^2+b+1)-(2b+1)^2=3$. This forces $b=1$, excluded by $ab>2$.

Equality occurs for $a=b=2$, or when $|a-b|=2$ and $g=1$. The latter means that $a,b$ are consecutive positive odd integers. Conversely these pairs do give equality: writing them as $2k-1,2k+1$, the quotient is $4k^2/(4k)=k$.''')
put('ind_2014_8036c9',5,'The key is to monitor the polynomial at 2 rather than its discriminant. One player can drive this value downward despite the opponent, with a short final correction preventing an overshoot.',solutionOverride=r'''Calvin initially keeps decreasing the coefficient of $x$. Let $v$ be the value of the current polynomial at $2$, observed just after each move by Hobbes. Each full round decreases $v$ by either $1$ or $3$. Starting from $2020$, it therefore eventually reaches $0$, $1$, or $2$.

At $v=0$ Calvin has already won. At $v=2$, decreasing the coefficient of $x$ once makes $v=0$. At $v=1$, Calvin decreases it, leaving $v=-1$; Hobbes then makes $v=0$ or $-2$. In the second case Calvin increases the coefficient of $x$, giving $v=0$.

Thus the polynomial acquires the integer root $2$. Since it is monic with integer coefficients, its other root is also an integer.''')
put('ind_2014_5cee0f',5.5,'The synthetic route finds a shared circle through the two circumcentres, the original circumcentre, A and the new orthocentre. Coordinating the perpendicular-bisector and altitude angle chases is the main difficulty.',solutionKind='source-link',statementOverride=r'Let $ABC$ be acute and $D$ lie in the interior of $BC$. Write $O_1,O_2$ for the circumcentres of $ABD,ACD$, $O$ for the circumcentre of $ABC$, and $K$ for the orthocentre of $O_1O_2D$. Prove that $O,K$ lie on a line parallel to $BC$ (equivalently, either $O=K$ or $OK\parallel BC$).',note='The formulation explicitly permits O=K, an exceptional configuration suppressed by the original wording “the line joining”.')
put('ind_2014_5520b5',5,'Pair subsets differing in one fixed element for the easy bound; the demanding part is proving the only equality cases are the two parity classes. A connected-hypercube edge count makes that classification rigorous.',solutionOverride=r'''Pair every subset not containing $n$ with the set obtained by adjoining $n$. At most one member of each pair belongs to $\mathcal F$, giving $|\mathcal F|\le2^{n-1}$.

For equality, form the graph whose vertices are all subsets of $X$, with an edge when two sets differ in exactly one element. It has $n2^{n-1}$ edges and every vertex has degree $n$. No edge joins two members of $\mathcal F$. If $|\mathcal F|=2^{n-1}$, the $n|\mathcal F|$ edges incident with it already account for every edge of the graph. Hence every edge has exactly one endpoint in $\mathcal F$.

Starting from the empty set and toggling one element at a time, membership in $\mathcal F$ must alternate. Therefore $\mathcal F$ consists either of all even-cardinality subsets or of all odd-cardinality subsets. Both collections satisfy the condition.''')
put('ind_2015_23cfda',5.5,'Connect the three incentres through the original angle bisectors, exploit the similar right triangles to relate their inradii, and identify the hypotenuse contact point as circumcentre. The auxiliary right-isosceles triangle is the key construction.',solutionKind='source-link')
put('ind_2015_0c5a48',4,'A rational-decimal denominator argument gives a sharp lower bound from the powers of 2 and 5; removing exactly these factors proves attainability, including the recurring-9 convention.',solutionOverride=r'''Write $n=2^u5^v m$ with $\gcd(m,10)=1$, and set $r=\max(u,v)$. The answer is $\boxed r$.

If the preperiod has length $t$ and the repeating block has length $s$, its value is a fraction whose denominator divides $10^t(10^s-1)$. Since $1/n$ is reduced and $10^s-1$ is coprime to $10$, necessarily $t\ge u,v$.

Conversely, multiplying $1/n$ by $10^r$ leaves a rational number with denominator coprime to $10$. If $m>1$, multiplication by $10$ permutes the nonzero remainders modulo $m$, so the fractional part repeats immediately. If $m=1$, use the recurring-$9$ representation of the resulting integer. Thus the expansion repeats after at most $r$ digits, proving equality.''')
put('ind_2015_5bb4a5',4.5,'Classify the zero set first: a nonzero root forces the zero function; otherwise a substitution forces x²−xf(x)=0. This is a clean but non-routine functional-equation pivot.',solutionOverride=r'''Taking $x=y=0$ gives $f(0)=0$. If $f(a)=0$ for some $a\ne0$, substituting $x=a$ gives $f(a^2)=a f(a+y)$ for every $y$. Hence $f$ is constant and therefore identically zero.

Otherwise the only zero is $0$. Set $y=-x$ to obtain $f(x^2-xf(x))=0$. Thus $x^2-xf(x)=0$, so $f(x)=x$ for $x\ne0$ and also for $x=0$. Both $f\equiv0$ and $f(x)=x$ satisfy the equation.''')
put('ind_2015_df7a08',3.5,'A direct two-state return/non-return recurrence gives xₙ₊₁=3ⁿ−xₙ, starting x₀=1, and x₇=546. The states are explicit and no hidden combinatorial structure is required.')
put('ind_2015_889079',6,'Express the four reciprocal altitudes via the diagonal parts, then establish equivalence with Pitot through two squared identities and the cosine rule. The converse and algebraic equivalence need care.',solutionKind='source-link')
put('ind_2015_6153f0',4.5,'First pair ten squares by parity so every difference is 0 modulo 4; then a three-term zero-sum argument among five residues modulo 3 produces the desired six distinct entries.',solutionOverride=r'''Among eleven squares, one parity class has odd size and the other even size. Pair entries within each parity class, leaving just one unpaired entry. We obtain five disjoint pairs $(u_i,v_i)$ of squares with $u_i-v_i$ divisible by $4$.

Consider the five differences modulo $3$. If some residue occurs at least three times, those three differences sum to $0\pmod3$. Otherwise each residue occurs at most twice; with five entries, all three residues occur, and one of each again sums to $0\pmod3$.

Choose the resulting three pairs. Their differences sum to a multiple of both $3$ and $4$, hence of $12$. The three first entries and three second entries are the required six squares.''')
(P/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
