import json
from pathlib import Path
p=Path(__file__).parent;R=json.loads((p/'reviews.json').read_text())
def put(s,d,t,ts,why,**kw):R['blr_2024_'+s]={'difficulty':d,'topic':t,'tags':ts.split(','),'reason':why,**kw}
put('19675f',4.5,'Number Theory','squarefree integers,inclusion-exclusion,pigeonhole principle','The extremal set combines all squarefree numbers with eight carefully chosen nonsquare multiples of prime squares; an inclusion-exclusion count fixes the exact threshold.',solution=r'''There are 608 squarefree positive integers at most 1000. Inclusion-exclusion gives this as
$$1000-442+51-1=608,$$
where 442 counts multiples of single prime squares, 51 counts multiples of products of two distinct prime squares, and 1 counts the sole nonzero three-prime intersection, multiples of $2^23^25^2$.

Avoiding prime squares themselves, a number divisible by $p^2$ must be at least $2p^2$. Hence only the eight primes $2,3,5,7,11,13,17,19$ can be used. Since two selected numbers cannot share such a prime square, there are at most eight nonsquarefree selected numbers. This bounds the size by $608+8=616$.

The bound is attained by taking every squarefree number and the eight numbers $2p^2$ for those primes. They lie below 1000 and no two share a squared prime factor. Thus the requested threshold is $\boxed{617}$.''')
put('32812a',8,'Combinatorics','weighted double counting,triangular grid,extremal construction','The general bound uses a substantial weighted capacity argument, and the two sharpness constructions require separate residue cases; above the target band.')
put('41fa6d',6.5,'Combinatorics','permutations,invariants,composition','Writing the row operations as compositions reveals an invariant fourfold composition; checking its value at one position distinguishes the two tables.',solution=r'''Regard the rows as permutations $s,t$, read as functions from positions to entries. Operation A changes $(s,t)$ to $(t\circ s,t)$, and B changes it to $(s,s\circ t)$. Consider
$$C=s^{-1}\circ t^{-1}\circ s\circ t.$$
Direct cancellation shows that either operation leaves $C$ unchanged.

Initially $s$ swaps 1 and 2, while $t$ sends $1\to2\to\cdots\to n\to1$. Applying $C$ to 1 therefore gives $1\to2\to1\to n\to n$, so $C(1)=n$.

In the desired table, $s$ is the cycle $1\to2\to3\to1$ and $t$ is unchanged. Now $1\to2\to3\to2\to1$, so $C(1)=1$. Since $n\ge3$, these differ. The target is impossible.''',notes='The source’s displayed cycle expansion of its commutator is incorrect; this proof checks the invariant directly at one input.')
put('54321a',6.5,'Combinatorics','strategy games,intervals,induction','The winning invariant combines a strict majority of white length with a white endpoint neighbourhood; choosing an almost-full interval restores both after a difficult reply.',solution=r'''Olya wins. After every even round she maintains two properties: the white length exceeds $1/2$, and a neighbourhood of at least one endpoint is white. Initially both hold.

If Tolya chooses length 0 or 1, Olya chooses the same length in the following round, restoring the colouring except possibly at isolated endpoints. Otherwise $0<l<1$. If just one endpoint neighbourhood is black, Olya flips an interval of length $l$ adjacent to that endpoint; if both are white, she chooses an interior interval. In either case both endpoint neighbourhoods are now white.

If the white length still exceeds $1/2$, she chooses length 0 next. Otherwise choose $\eta>0$ so small that both endpoint intervals of length $\eta$ are white, and ask for length $1-\eta$. Every interval of that length contains all black points except possibly isolated boundaries, and leaves total length $\eta$ of white points unflipped. The final white length is therefore $1-L+\eta>1/2$, and at least one endpoint neighbourhood remains white. This completes the induction through 2024 rounds.''')
put('548b33',7.5,'Algebra','functional images,monotonicity,fixed points','The contradiction needs alternating intervals under iteration and a bounded monotone-limit argument; this is above the intended elementary band.')
put('79e0d5',5.5,'Number Theory','quadratic norms,prime factorisation,identities','The unwieldy cubic system conceals a multiplicative norm x²+3y²; the resulting prime factorisation forces two coordinates to vanish.',solution=r'''Put $u=ac+3bd$ and $v=ad-bc$. The two given expressions are $eu+3fv$ and $fu-ev$. Therefore
$$37=5^2+3\cdot2^2=(e^2+3f^2)(u^2+3v^2)=(e^2+3f^2)(a^2+3b^2)(c^2+3d^2).$$
These are positive integer factors of the prime 37, so two equal 1. If $r^2+3s^2=1$ with integers $r,s$, then $s=0$. Hence at least two of $b,d,f$ vanish, including at least one of $b,d$. Thus $abcde=0$. This occurs for $(a,b,c,d,e,f)=(1,0,1,0,5,2)$, so the only possible value is $\boxed0$.''')
put('a99734',8.5,'Number Theory','Gaussian integers,rational distance sets,prime factorisation','The proof needs factorisation in Gaussian integers and repeated denominator-removing rotations, beyond the requested level.')
put('b71bb1',5.5,'Algebra','functional equations,finite range,exceptional substitution','Putting one input zero limits nonzero inputs to two values, but the restriction x≠y requires careful mixed-value and opposite-input cases to force constancy.')
put('d8428f',8,'Combinatorics','regular bipartite graphs,Hall theorem,path rotations','After double counting degrees, the long-path bound uses a perfect matching and endpoint rotation; this is a substantial advanced graph argument.')
put('f14af4',7.5,'Geometry','rotation,reflection,angle chasing','The solution combines a tailored rotation and reflection creating an equilateral triangle with a long dependent angle calculation; above the upper edge.')
put('f3d838',6,'Algebra','polynomial factorisation,counting,geometric series','A useful overcount pairs coefficients of the two factors, gaining a uniform factor of four per pair; summing across factor degrees gives the two-to-one conclusion.',solution=r'''There are $101^n$ allowed monic polynomials. Suppose a polynomial factors into monic nonconstant factors of degrees $m\ge k\ge1$, $m+k=n$. All factor coefficients lie in $\{0,\ldots,100\}$, since each appears as a nonnegative contribution to a coefficient of the product. If the two factors have coefficients $b_i,c_i$, then $b_ic_i\le100$ for $0\le i<k$.

For each such pair, at least one entry is at most 10, so the number of possible pairs is at most $2\cdot11\cdot101<101^2/4$. The other $m-k$ coefficients have at most $101^{m-k}$ possibilities. Thus, allowing overcounting of polynomials with more than one factorisation, the number that factor is less than
$$\sum_{k=1}^{\lfloor n/2\rfloor}101^{n-2k}(101^2/4)^k<101^n\sum_{k=1}^\infty4^{-k}=\frac13\,101^n.$$
More than two thirds do not factor, proving the claim. For $n=1$ the conclusion is immediate.''')
for s,r in R.items():
 if s.startswith('blr_2024_'):r['competition']='Belarus IMO Selection Tests'
(p/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
