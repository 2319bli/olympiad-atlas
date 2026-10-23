from international_completion_helpers import add,save
add(1987,1,'Combinatorics',2.5,'Counting a permutation together with one marked fixed point gives the identity immediately; this basic double count is below the target band.',r'Let $p_n(k)$ count permutations of $\{1,\ldots,n\}$ with exactly $k$ fixed points. Prove $\sum_{k=0}^n k\,p_n(k)=n!$.',r'''Count pairs $(\sigma,i)$ where $\sigma$ is a permutation and $\sigma(i)=i$. Grouping by the permutation gives $\sum k\,p_n(k)$. Choosing $i$ first gives $n$ choices and then $(n-1)!$ permutations of the other elements. Hence the same count is $n(n-1)!=n!$.''',['Double counting','Permutations'])
add(1987,2,'Geometry',4.5,'Use perpendicular diagonals to express the quadrilateral’s area, then combine one right-triangle identity with similarity through the angle-bisector chord.',r'In acute triangle $ABC$, the angle bisector from $A$ meets $BC$ at $L$ and the circumcircle again at $N$. Let $K,M$ be the feet from $L$ to $AB,AC$. Prove quadrilateral $AKNM$ has the same area as $ABC$.',r'''Set $\angle A=2\alpha$. The equal right triangles $AKL,AML$ give $KM\perp AN$. Also $AK=AL\cos\alpha$, so
$$KM=2AK\sin\alpha=AL\sin2\alpha.$$
Thus the quadrilateral has area $AN\cdot KM/2$.

Triangles $ABL$ and $ANC$ are similar: their angles at $A$ agree, and $\angle ABL=\angle ANC$ by the inscribed-angle theorem. Therefore $AB\cdot AC=AL\cdot AN$. Consequently
$$[ABC]=\tfrac12 AB\cdot AC\sin2\alpha=\tfrac12 AN\cdot AL\sin2\alpha=\tfrac12 AN\cdot KM=[AKNM].$$''',['Similarity','Area','Trigonometry','Circles'])
add(1987,3,'Combinatorics',4.5,'Place all bounded-coefficient linear combinations in an interval, use the smallest adjacent gap, and control the interval length by Cauchy–Schwarz.',r'If real $x_1,\ldots,x_n$ satisfy $\sum x_i^2=1$, prove that for each integer $k\ge2$ there are integers $a_i$, not all zero, with $|a_i|\le k-1$ and $|\sum a_ix_i|\le (k-1)\sqrt n/(k^n-1)$.',r'''Consider the $k^n$ sums $\sum b_i|x_i|$ for integer choices $0\le b_i\le k-1$. All lie in $[0,(k-1)\sum|x_i|]$, an interval of length at most $(k-1)\sqrt n$ by Cauchy–Schwarz.

If two sums coincide, subtract their distinct coefficient vectors to obtain a nonzero vector with dot product zero. Otherwise sort all sums increasingly. The $k^n-1$ consecutive gaps have total at most $(k-1)\sqrt n$, so one gap is at most $(k-1)\sqrt n/(k^n-1)$. Subtract the two coefficient vectors giving that gap. Their entries have absolute value at most $k-1$ and are not all zero. Finally reverse the sign of the corresponding coefficient wherever $x_i<0$ to replace $|x_i|$ by $x_i$.''',['Pigeonhole principle','Cauchy–Schwarz','Approximation','Counting'])
add(1987,4,'Algebra',6,'Injectivity allows the missing values of f and their images to partition the finite complement of the twice-iterated image into two equal parts, contradicting odd cardinality.',r'Prove no function $f:\mathbb Z_{\ge0}\to\mathbb Z_{\ge0}$ satisfies $f(f(n))=n+1987$ for every $n\ge0$.',r'''Suppose such an $f$ exists and let $N=\mathbb Z_{\ge0}$. The equation makes $f$ injective: equal values at $m,n$ would imply $m+1987=n+1987$.

Put $A=N\setminus f(N)$. Injectivity implies
$$f(A)=f(N)\setminus f(f(N)).$$
Indeed, the image of a point outside $f(N)$ cannot coincide with the image of a point inside $f(N)$, and every element of the displayed difference has such a preimage.

Consequently the disjoint sets $A,f(A)$ partition $N\setminus f(f(N))=\{0,1,\ldots,1986\}$. They are finite and have equal cardinality because $f$ is injective. Their union must therefore have even cardinality, contradicting its size 1987.''',['Functional equations','Injectivity','Sets','Parity'])
add(1987,5,'Geometry',4,'Integer points on a parabola simultaneously give nonzero rational determinants and distances involving integers strictly between consecutive squares.',r'For every integer $n\ge3$, construct $n$ plane points with all pairwise distances irrational and every three forming a nondegenerate triangle of rational area.',r'''Take $P_j=(j,j^2)$ for $j=1,\ldots,n$. For $j>i$,
$$P_iP_j=(j-i)\sqrt{1+(i+j)^2}.$$
The integer under the square root lies strictly between $(i+j)^2$ and $(i+j+1)^2$, so it is not a square and its square root is irrational. Multiplying by the nonzero integer $j-i$ preserves irrationality.

For $i<j<k$, the determinant area formula gives
$$[P_iP_jP_k]=\frac{(j-i)(k-i)(k-j)}2.$$
This is positive and rational. Thus the construction has both required properties.''',['Coordinates','Area','Irrationality','Construction'])
add(1987,6,'Number Theory',8,'The proof requires a strong induction combined with a nonstandard interval of coprimality tests; differences of polynomial values rule out every possible small divisor before a square-root bound finishes.',r'Let $n\ge2$. Suppose $k^2+k+n$ is prime for every integer $0\le k\le\sqrt{n/3}$. Prove it is prime for every integer $0\le k\le n-2$.',r'''Write $F(k)=n+k(k+1)$ and $r=\lfloor\sqrt{n/3}\rfloor$. Induct from the assumed range. Suppose $r<b\le n-2$ and all earlier $F(i)$ are prime. Since $n<3b^2$, we have $F(b)<(2b+1)^2$.

For $b+1\le j\le2b$, put $i=j-b-1$, so $0\le i<b$. Then $F(b)-F(i)=(b-i)j$. If $F(b)$ and $j$ shared a prime divisor, it would divide the prime $F(i)$, so $F(i)\mid j$. But $j\le2b\le2n-4<2F(i)$, forcing $j=F(i)$. The equality $b+i+1=n+i(i+1)$ becomes $b+1=n+i^2$, impossible because $b\le n-2$. Thus $F(b)$ is coprime to every integer in $(b,2b]$.

Every integer $d\le b$ has a power-of-two multiple in $(b,2b]$, so $F(b)$ is also coprime to every $d\le b$. It has no divisor between 2 and $2b$, while its square root is below $2b+1$. Hence it is prime. This completes the induction; $n=2$ is already in the assumed range.''',['Primes','Induction','Polynomial divisibility','Bounds'])
save()
