import json,re
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text())
def add(s,d,t,tags,reason,solution=None,statement=None,q=False):
 id='ukr_2023_'+s;r[id]={'difficulty':d,'topic':t,'tags':tags,'reason':reason}
 if solution:r[id]['solution']=solution
 if statement:r[id]['statement']=statement
 if q:r[id]['quarantine']=True
add('1f0ec0',4,'Number theory',['factorials','decimal digits'],'Trailing-zero divisibility eliminates large suffixes; small cases must then be checked.',r'''If $k\ge5$, every product of $k$ consecutive positive integers is divisible by $10$, so its suffix $k$ must be divisible by $10$. Thus $k\ge10$. Such a product is divisible by $k!$, because it equals $k!\binom{a+k-1}{k}$ for some positive $a$. Since $(k-1)!$ is divisible by $10$, the product is divisible by $10k$. It therefore has strictly more trailing zeroes than $k$, contradicting the suffix condition. Hence $k\le4$. For $k=3$ the product is even and cannot end in 3. The values $1,2,4$ occur in $1$, $1\cdot2$, and $1\cdot2\cdot3\cdot4=24$.''')
add('063ede',4,'Combinatorics',['pairing strategy','grid games'],'Pair cells to create impassable lines, limiting every yellow path to a two-row strip.')
add('1a89cd',None,'Geometry',['circle tangency'],'The recovered solution contains angle identities and an auxiliary lemma but omits the argument connecting them to the required tangency.',q=True)
add('fbff02',5.5,'Algebra',['sequences','convexity','floor function'],'Show successive differences are nondecreasing by exploiting minimal crossing indices, then telescope.')
add('b99495',4,'Algebra',['polynomial coefficients','counterexample construction'],'A triangular coefficient profile has bounded first differences but an arbitrarily high peak.')
add('77c112',5,'Number theory',['2-adic valuation','graphs','cycle argument'],'A cycle cannot have pairwise different edge valuations; one edge per valuation must therefore form a forest.',r'''Choose one pair realizing each distinct valuation and draw these pairs as edges on the $n$ numbers. This graph has no cycle. Otherwise, choose the edge of smallest valuation $v$ on a cycle. Every other edge difference is divisible by $2^{v+1}$; adding the signed differences around the rest of the cycle implies that the chosen edge difference is also divisible by $2^{v+1}$, a contradiction. A forest on $n$ vertices has at most $n-1$ edges.
Equality is attained by $1,1+2,1+2^2,\ldots,1+2^{n-1}$: the differences from 1 already realize $n-1$ distinct powers. Thus the answer is $n-1$.''')
add('8e13fc',5,'Combinatorics',['parity','perfect matchings','construction'],'Colour cross-part edges alike and same-part edges uniquely; the parity of every matching prevents even colour counts.',r'''Yes. Divide the vertices into two groups of odd size $2023$. Give every edge between groups one common colour, and give every edge within either group its own private colour. In a perfect matching let $t$ be the number of cross-group edges. The $2023-t$ remaining vertices in each group must be paired internally, so $t$ is odd. Also $t\ge1$. The matching therefore uses
$$1+(2023-t)=2024-t$$
distinct colours, always an odd number. Hence 1000 is impossible. To obtain 999 or 1001 colours, choose respectively $t=1025$ or $t=1023$ cross-group pairs, and pair all remaining vertices within each group. Both constructions are possible because each remaining group size is even.''')
add('5c0caa',3,'Number theory',['coprimality','extremal element'],'Three ordered entries would force their two larger, coprime values to divide a²+1, exceeding it.')
add('59d489',5,'Combinatorics',['double counting','extremal distance'],'Count each hypotenuse endpoint, excluding a farthest point; antipodal circle pairs attain the bound.')
add('56327b',7.5,'Geometry',['orthic quadrilaterals','circle tangency'],'The proof requires an orthic interpretation, paired angle-bisector constructions and several linked cyclic quadrilaterals.')
add('a8bad8',6.5,'Algebra',['functional equations','injectivity'],'Derive oddness and a square identity, then a zero dichotomy and injectivity before concluding.')
add('3cf1f0',6,'Algebra',['polynomial factorization','counterexample construction'],'A suitable pair of cyclotomic-style factorizations cancels every negative coefficient.',r'''No. Take
$$f(x)=(x^4-x^2+1)(x+1)=x^5+x^4-x^3-x^2+x+1,$$
$$g(x)=(x^2-x+1)(x^2+1)=x^4-x^3+2x^2-x+1.$$
Both have coefficients of both signs. But regrouping their four factors gives
$$f(x)g(x)=[(x^4-x^2+1)(x^2+1)][(x^2-x+1)(x+1)]=(x^6+1)(x^3+1).$$
The product is $x^9+x^6+x^3+1$, with no negative coefficients.''')
add('2ff2f6',4.5,'Geometry',['midpoints','power of a point'],'Two midpoint circles give a common power from A, which forces the desired cyclicity.',statement=r'In triangle $ABC$, $M$ is the midpoint of $BC$ and $K$ the midpoint of $AM$. Choose $X\in AB$, $Y\in AC$ with $AX>BX$, $AY>CY$, $\angle KXM=\angle ACB$ and $\angle KYM=\angle ABC$. Prove that $B,X,C,Y$ are concyclic.')
add('a08036',7.5,'Number theory',['ordered divisors','prime factorization'],'The classification tracks multiple transitions in the divisor sequence and pairs them through reciprocal divisors.')
add('8cc3d1',7.5,'Combinatorics',['edge colouring','connected components'],'The sharp monochromatic-component bound requires a nontrivial structural argument and a four-part extremal colouring.')
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
