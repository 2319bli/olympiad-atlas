from pathlib import Path
import json
p=Path('/workspace/sites/olympiad-atlas/research')
r=json.loads((p/'international-reviews.json').read_text())
r.update({
'rmm_2021_07c4be':[5.5,'The key geometric recognition is that the four circle centres form a parallelogram. Projecting their midpoint identity onto the transversal then gives the required alternating chord-gap identity.'],
'rmm_2021_d11caf':[7,'Two overlapping queries and CRT give the upper bound; the difficult half is an adversarial cyclic reassignment using gcd compatibility to rule out every single query.'],
'rmm_2021_7ba909':[8.5,'The polynomial encoding, reduction over the field of 17 elements and coefficient extraction require several advanced ideas beyond the target band.'],
'rmm_2021_03b2ae':[6.5,'A strong-induction construction reduces the board to an evenly scaled interval; the odd-number pairings and exceptional residue classes require substantial discovery and checking.'],
'rmm_2021_b2930f':[8.5,'A delicate geometric peeling and lattice-like point construction must control perimeter, point counts and distances across several tiles.'],
'rmm_2021_b2e860':[9,'The classification requires deep polynomial interpolation and point-merging arguments under restricted operations, with separate leading-coefficient obstructions.'],
'zhk_2021_620b3f':[4.5,'A short but non-obvious scale change raises a small remainder past the threshold while keeping it below a fixed power of two.'],
'zhk_2021_68f19c':[6.5,'Parallel lines from equal arcs lead to auxiliary parallelograms; two tangent-circle power identities and a final similarity establish the midpoint.'],
'zhk_2021_ef5d05':[8,'The reduction to nonnegative entries is a substantial assignment-duality or matching-decomposition argument, substantially beyond elementary BMO1 combinatorics.'],
'zhk_2021_bd8594':[5,'The geometry gives a half-angle formula for each small radius, followed by a concavity bound and a reciprocal Cauchy inequality.'],
'zhk_2021_96d201':[8,'Both optimal strategies require careful local case analysis around the unique sparse stable configuration and a maintained partition invariant.'],
'zhk_2021_2a917c':[5.5,'Evaluating at one root of the irreducible polynomial gives at most n outputs; proving injectivity uses a concise but conceptual minimal-polynomial argument.'],
'ibe_2003_38dcd3':[4.5,'The total sum creates a parity obstruction, while the odd case needs an explicit interlaced permutation producing consecutive sums.'],
'ibe_2003_2960db':[5.5,'One must exploit the common circle to show the two circumcentres have the same homothety ratio with respect to the chord midpoints; the vector calculation is compact once set up.'],
'ibe_2003_06bf4f':[4.5,'Choosing the last unsaturated inequality reveals that the final positive coefficient dominates every preceding negative contribution through a geometric series.'],
'ibe_2003_e467f0':[5,'The extremal bound is elementary, but counting all maximisers requires encoding omitted points by nine bounded gaps and a stars-and-bars deficit count.'],
'ibe_2003_733d39':[6,'Two triangle inequalities are quick; the third needs a carefully chosen quarter-turn and a strict comparison of two angles, including endpoint cases.'],
'ibe_2003_447c32':[5,'Fermat reduces the recurrence for the product to (c+1)^2/c; the key is recognising the invariant nonzero quadratic-residue class and excluding minus one.']
})
(p/'international-reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
o={
'rmm_2021_d11caf':r'''Two moves are necessary and sufficient.

Ask first for the indices $\{17,18\}$ and then for $\{18,19\}$. The unique common answer identifies $a_{18}$ and therefore the other two answers. The three pairwise coprime moduli have product $5814>5000$, so the Chinese remainder theorem determines $N$ uniquely.

For the lower bound put $M=\operatorname{lcm}(1,\ldots,10)=2520$. Consider any proposed single query. An empty query gives no information. For a singleton $\{s\}$, the same answer can be given for $N=1$ and $N=1+s\leq21$.

For a query with at least two distinct indices, write them cyclically as $s_1,\ldots,s_k$. The gcd of two distinct integers at most 20 is at most 10 and hence divides $M$. Thus the simultaneous congruences
$$b_i\equiv1\pmod{s_i},\qquad b_i\equiv M+1\pmod{s_{i+1}}$$
are compatible. Choose positive, pairwise distinct solutions $b_i$, possible because each congruence class contains infinitely many integers. The unordered response $\{b_1,\ldots,b_k\}$ is consistent with either $N=1$ (assign $a_{s_i}=b_i$) or $N=M+1=2521$ (assign $a_{s_{i+1}}=b_i$). All unqueried entries can be filled with distinct sufficiently large integers of their required residues. Hence one move cannot suffice.''',
'zhk_2021_620b3f':r'''Write $H=10^{2021}$. Choose $M$ with $2^M>10H$, and let $r$ be the remainder of $3^M$ modulo $2^M$. It is odd and positive. If $r>H$, take $n=M$.

Otherwise choose the least positive $k$ with $3^kr>H$. Then $3^kr\leq3H<2^M$. For $n=M+k$ we have
$$3^n\equiv3^kr\pmod{2^M}.$$
The remainder modulo the larger modulus $2^n$ has the same residue modulo $2^M$, so it equals $3^kr+s2^M$ for some nonnegative integer $s$. It is therefore greater than $H$, as required.''',
'zhk_2021_bd8594':r'''Let $\alpha=A/2$, $\beta=B/2$, $\gamma=C/2$, so their sum is $\pi/2$. The centres of the incircle and the small circle in angle $A$ lie on its bisector, at distances $r/\sin\alpha$ and $r_1/\sin\alpha$ from $A$. External tangency gives
$$\frac{r-r_1}{\sin\alpha}=r+r_1,\qquad \frac{r_1}{r}=\frac{1-\sin\alpha}{1+\sin\alpha}.$$
There are analogous formulas at the other two vertices. Concavity of sine on $[0,\pi/2]$ gives $\sin\alpha+\sin\beta+\sin\gamma\leq3\sin(\pi/6)=3/2$. Cauchy's inequality therefore yields
$$\frac{r_1+r_2+r_3}{r}=2\sum_{t\in\{\alpha,\beta,\gamma\}}\frac1{1+\sin t}-3
\geq\frac{18}{3+\sin\alpha+\sin\beta+\sin\gamma}-3\geq1.$$
This is the required inequality; equality occurs for an equilateral triangle.''',
'zhk_2021_2a917c':r'''Fix a complex root $\alpha$ of $P$. For every permitted polynomial $Q$, divisibility gives $P(Q(\alpha))=0$, so $Q(\alpha)$ is one of at most $n$ roots of $P$.

No two distinct permitted polynomials have the same value at $\alpha$. Indeed, if $Q_1(\alpha)=Q_2(\alpha)$, then $P$ and $Q_1-Q_2$ share a root. Their greatest common divisor over $\mathbb Q$ is nonconstant: otherwise the Euclidean algorithm would give rational polynomials $U,V$ with $UP+V(Q_1-Q_2)=1$, contradicting evaluation at $\alpha$. Irreducibility of $P$ then implies $P\mid Q_1-Q_2$, impossible for a nonzero polynomial of degree below $n$. Thus the map $Q\mapsto Q(\alpha)$ is injective into a set of at most $n$ elements.''',
'ibe_2003_38dcd3':r'''Subtracting a fixed constant from every entry in each row does not affect the question, so assume both rows are permutations of $1,\ldots,N$. Their column sums have total $N(N+1)$. If they are consecutive integers, their average is $N+1$, so their smallest member must be $(N+3)/2$. Thus $N$ must be odd; in particular 2004 is impossible.

For $N=2m+1$, pair each odd first-row entry $2j+1$ with $m+1-j$ for $0\leq j\leq m$. These sums are $m+2,m+3,\ldots,2m+2$. Pair each even first-row entry $2j$ with $2m+2-j$ for $1\leq j\leq m$. These sums are $2m+3,\ldots,3m+2$. Every entry in each row is used exactly once, and all $N$ sums are consecutive. This supplies the construction for 2003.''',
'ibe_2003_2960db':r'''Take the centre of the semicircle as the vector origin and write its radius as $R$. Let the vectors of $A,C,D$ be $a,c,d$; then $B$ has vector $-a$ and $|a|=|c|=|d|=R$. The midpoint vectors are
$$m=(a+c)/2,\qquad n=(-a+d)/2,\qquad p=(c+d)/2.$$
The perpendicular bisector of chord $AC$ is the line through the origin and $m$, so the circumcentre of $ACP$ has vector $o=\lambda m$. Similarly the circumcentre of $BDP$ has vector $o'=\mu n$.

Their equal-distance conditions give
$$2\lambda m\cdot(p-a)=|p|^2-R^2,\qquad 2\mu n\cdot(p+a)=|p|^2-R^2.$$
But direct expansion shows
$$m\cdot(p-a)=n\cdot(p+a)=\frac{-R^2-a\cdot c+a\cdot d+c\cdot d}{4}.$$
The common right-hand side of the equal-distance conditions is negative because $P$ is the midpoint of a genuine chord, so the displayed dot products are nonzero. Hence $\lambda=\mu\ne0$. Therefore $o-o'=\lambda(m-n)$, proving $OO'\parallel MN$.''',
'ibe_2003_06bf4f':r'''Whatever the missing signs are, the unique maximising choice is $x_i=2^i$ for $0\leq i\leq2003$.

Suppose a permissible sequence has a strict inequality somewhere, and let $k$ be the last index with $x_k<2x_{k-1}$. All later constraints are equalities. Put $h=2x_{k-1}-x_k>0$ and increase $x_k$ by $h$, $x_{k+1}$ by $2h$, and so on, increasing $x_{2003}$ by $2^{2003-k}h$. The new sequence is still permissible.

Even if every affected coefficient before the last is negative, the expression increases by at least
$$h\left(2^{2003-k}-\sum_{j=0}^{2002-k}2^j\right)=h>0.$$
Repeat, moving to the last remaining strict constraint each time. In finitely many steps all constraints are equalities. Thus every other sequence gives a strictly smaller value, independently of the missing signs.''',
'ibe_2003_e467f0':r'''The maximum size is 41, and there are $\binom{12}{8}=495$ subsets of that size.

Each of the eight disjoint blocks $\{1,\ldots,6\},\ldots,\{43,\ldots,48\}$ must omit an element. Hence at least eight elements are omitted and the size is at most 41. Omitting $6,12,\ldots,48$ attains this bound.

For a subset of size 41, list its eight omitted elements in order. Let $g_0,\ldots,g_8$ count the chosen elements before the first omission, between successive omissions and after the last omission. The condition is precisely
$$0\leq g_i\leq5,\qquad \sum_{i=0}^8g_i=41.$$
Put $h_i=5-g_i$. Then $h_i\geq0$ and $\sum h_i=45-41=4$; the upper bounds $h_i\leq5$ are automatic. Stars and bars gives $\binom{4+9-1}{9-1}=495$ possibilities, each corresponding to exactly one subset.''',
'ibe_2003_733d39':r'''Scale the square to $A=(0,0)$, $B=(1,0)$, $C=(1,1)$, $D=(0,1)$. Put $P=(1,t)$ and $Q=(1-t,1)$ with $0<t<1$. Since $X\ne Y$, they cannot both equal $A$.

For $Y\ne A$, its second coordinate exceeds its first, so $DY<BY\leq BX+XY$. If $Y=A$, the same strict conclusion follows from the triangle inequality in the nondegenerate triangle $ABX$. Similarly $BX<DY+XY$, treating $X=A$ with the nondegenerate triangle $ADY$.

It remains to prove $XY<BX+DY$. Rotate $Y$ clockwise through $90^\circ$ about $A$ to $Y'$. This sends $D$ to $B$, so $BY'=DY$. Write $u=\arctan t$ and $v=\arctan(1-t)$. The angle between rays $AP$ and $AY'$ is $u+v$, whereas the angle between $AP$ and $AQ$ is $\pi/2-u-v$. Furthermore
$$\tan(u+v)=\frac1{1-t+t^2}>1,$$
so $u+v>\pi/4$ and the first angle is larger. If $X,Y\ne A$, the cosine rule and $AY'=AY$ give $XY<XY'$. Consequently
$$XY<XY'\leq BX+BY'=BX+DY.$$
If one of $X,Y$ is $A$, then $XY=XY'$ but the last triangle inequality is strict, since $B,X,Y'$ are noncollinear. All three strict triangle inequalities hold.''',
'ibe_2003_447c32':r'''Work modulo the prime $p=2003$. We show inductively that $c_n=a_nb_n$ is a nonzero quadratic residue. This holds for $c_0=4$.

Suppose it holds for $c_n$. Then both factors are nonzero. Fermat's little theorem gives $a_n^{2001}=a_n^{-1}$ and $b_n^{2001}=b_n^{-1}$, so
$$c_{n+1}=(a_n^{-1}+b_n)(b_n^{-1}+a_n)=\frac{(c_n+1)^2}{c_n}.$$
Since $2003\equiv3\pmod4$, minus one is not a quadratic residue. Thus $c_n+1\ne0$, and the displayed quotient is again a nonzero quadratic residue. This proves the induction. In particular neither $a_n$ nor $b_n$ can ever be divisible by 2003.'''
}
q=p/'international-extra-solutions.json'
old=json.loads(q.read_text()) if q.exists() else {}
old.update(o);q.write_text(json.dumps(old,ensure_ascii=False,indent=2))
