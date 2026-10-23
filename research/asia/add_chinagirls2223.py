import json,pathlib
p=pathlib.Path('research/asia/reviews.json');r=json.loads(p.read_text());raw=pathlib.Path('research/raw/asia')
def add(y,k,d,reason,sol=None,**kw):
 r[f'chn_{y}_{k}']={'difficulty':d,'reason':reason,**kw}
 if sol:r[f'chn_{y}_{k}']['solutionOverride']=sol
add(2022,'0993d3',5,'Partitions teams by few wins or few losses, then combines internal game counts with a sharp bipartite bound.')
add(2022,'3fdfdd',8,'Requires a sophisticated collision count for a cubic over a finite field, including a conic point count and multiplicity analysis.')
add(2022,'5809fa',4.5,'Introducing the second circle intersections converts the angle hypotheses to parallel lines, and power of a point finishes.')
add(2022,'808a94',8,'Requires a substantial chain of auxiliary points, orthocenter relations and cyclic quadrilaterals beyond the target range.')
add(2022,'a104dd',6,'Combines an odd-modulus construction, a lifting principle and an exceptional power-of-two construction with small-case impossibility.',r'''The answer is all positive integers except $1,2,4$. Regard $A,B$ as sets of residues; the three sets $A,B,A+B$ must partition the residue classes.

For an odd modulus $n=2k+1\ge3$, choose $A=\{k\}$ and $B=\{k+1,\ldots,2k\}$. Their sumset gives the remaining residues $0,\ldots,k-1$.

If a construction works modulo $n$, it works modulo every multiple $dn$: take all inverse images of $A$ and $B$ under reduction modulo $n$. Their sumset is exactly the inverse image of $A+B$, so disjointness and coverage persist. Hence every integer with an odd factor greater than one works. Modulo $8$, use $A=\{1,2\}$ and $B=\{3,6\}$; their sumset is $\{0,4,5,7\}$. Lifting covers all powers of two at least $8$.

Three nonempty disjoint residue sets require $n\ge3$. For $n=4$, if $A,B$ are singletons then the union has only three elements. Otherwise one has at least two elements, and translating it by any element of the other set gives at least two elements in $A+B$. The total size is then at least $2+1+2=5$, impossible. This completes the classification.''')
add(2022,'e97c48',8.5,'Several stages of strict smoothing reduce eleven variables to three, followed by a nonlinear extremal system and a calibrated AM-GM proof.')
add(2022,'f9d3e8',5.5,'Pairs separated sequence terms to prove a sharp universal index, then designs a two-slope sequence to rule out the next index.')
add(2023,'5c51dc',6.5,'A chain of parallel constructions and cyclic quadrilaterals turns the product relation into a circle-center condition.')
add(2023,'5d5695',5.5,'The essential step is a common scaling that places half the intervals below one and half above, enabling sharp reciprocal bounds.',r'''Put $y_i=x_i/2^{11}$ for every $i$. The product of sums is unchanged by this common scaling. For $i\le11$, the interval for $y_i$ lies below $1$, where $t+1/t$ decreases; hence
$$y_i+1/y_i\le2^{12-i}+2^{i-12}.$$
For $i\ge12$, it lies above $1$, where that function increases; hence
$$y_i+1/y_i\le2^{i-11}+2^{11-i}.$$
Writing $U=\sum y_i$, $V=\sum1/y_i$, we obtain
$$UV\le\frac{(U+V)^2}{4}\le\left(\sum_{j=1}^{11}(2^j+2^{-j})\right)^2=\left(2^{12}-1-2^{-11}\right)^2.$$
Take $x_i=2^{i-1}$ for $i\le11$ and $x_i=2^i$ for $i\ge12$. The resulting $y_i$ occur in reciprocal pairs, so $U=V$ and all bounds are equalities. Thus the maximum is $\boxed{(2^{12}-1-2^{-11})^2}$.''')
add(2023,'85e679',7.5,'A difficult auxiliary circumcircle point identifies the radical axes; excluding the parallel case adds substantial configuration work.')
add(2023,'935930',6.5,'Uses coprimality to force a full prime power into a cross-sum or cross-difference, then contradicts a quadratic-form identity.')
add(2023,'bd15af',5.5,'A nonstandard geometric-mean smoothing inequality preserves the four-variable product and reduces the expression to AM-GM.',r'''For $a,c\in[0,1]$ and $X\ge1$, direct simplification gives
$$\frac1{X+a}+\frac1{X+c}-\frac2{X+\sqrt{ac}}=\frac{(\sqrt a-\sqrt c)^2(\sqrt{ac}-X)}{(X+a)(X+c)(X+\sqrt{ac})}\le0.$$
Apply this with $X=1+b$ and $X=1+d$. Replacing $a,c$ by $u=\sqrt{ac}$ therefore cannot decrease the left side, and it preserves $abcd$. Apply the same argument to $b,d$, replacing them by $v=\sqrt{bd}$. The left side is now at most $4/(1+u+v)$. Finally $u+v\ge2\sqrt{uv}=2\sqrt[4]{abcd}$, proving the desired bound. The argument includes zero variables because all denominators remain positive.''')
add(2023,'bd7869',5.5,'Transforms Manhattan distance into a maximum of two coordinate differences, then uses grid pigeonhole and a matching lattice construction.',r'''Set $u=x+y$ and $v=x-y$. For any pair of points,
$$d(P,Q)=\max(|u_P-u_Q|,|v_P-v_Q|).$$
Let $D$ be the largest distance. All transformed points lie in a square of side $D$. Divide each side into $44$ intervals, assigning boundary points consistently, to form $44^2=1936$ cells. Since there are $2023$ points, two share a cell and have distance at most $D/44$. Thus $\lambda\ge44$.

For equality, take any $2023$ of the $2025$ transformed lattice points $(u,v)$ with $u,v\in\{0,1,\ldots,44\}$, and map them back by $(x,y)=((u+v)/2,(u-v)/2)$. Their minimum distance is at least $1$ and their maximum at most $44$, so $\lambda\le44$. The lower bound already proved forces equality.''',topic='Combinatorics')
add(2023,'d22a16',6.5,'Uses the number of bounded regions to prove a sharp removal bound, and an L-triomino pattern supplies the extremal construction.',note='The supplied construction diagram was inspected: it consists of 21 bounded L-triomino regions and one unit square opened to the exterior.')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2));print(len(r))
