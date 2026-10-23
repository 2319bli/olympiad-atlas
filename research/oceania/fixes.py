import json
P='/workspace/sites/olympiad-atlas/research/oceania/'
d={
'nzl_2025_1a7685':r'''The answer is $\binom n2$. For an upper bound, look at the position where the target row has $n$. If this position currently contains $k$, swap labels $k,k+1$, then $k+1,k+2$, and so on until $n$ occupies that position. This uses $n-k\le n-1$ moves. Leave $n$ fixed and repeat on the other labels. The total is at most $(n-1)+(n-2)+\cdots+1$.

For the lower bound, take the reversed row and the increasing target row. Count inversions: pairs of labels occurring in decreasing order. Swapping the labels $a,a+1$ changes this count by exactly one. Their mutual order changes, while their total contribution with any other label does not. The inversion count must drop from $\binom n2$ to zero, so at least that many moves are needed.''',
'nzl_2024_953689':r'''First, $n=9$ fails, because the two arguments of the gcd coincide. If a prime $p\ne3$ divides $n-9$, choose a positive integer $x$ with $9x\equiv-1\pmod p$. Then both $9x+1$ and $nx+1$ are divisible by $p$, so this $n$ fails.

Thus $n-9=\pm3^k$ for an integer $k\ge0$. Conversely, let $g=\gcd(9x+1,nx+1)$ for such an $n$. We have $g\mid3^kx$ and $\gcd(g,x)=1$, hence $g\mid3^k$. But $3\nmid9x+1$, so $g=1$.

Within $0<n<2024$, the answers are
$$6,8,10,12,18,36,90,252,738.$$''',
'nzl_2021_059a42':r'''Rearrange the equation as
$$(x-y)^2=y^2(y-1)(y^2-y-1).$$
For $y\le-1$, the right side is negative, so there are no solutions. The cases $y=0,1$ give $(x,y)=(0,0),(1,1)$.

For $y\ge2$, the positive integers $y-1$ and $y^2-y-1$ are coprime, since the latter is congruent to $-1$ modulo $y-1$. After removing the square factor $y^2$, each must therefore be a square. If $y>2$, however,
$$(y-1)^2<y^2-y-1<y^2,$$
which is impossible. Finally, $y=2$ gives $x(x-4)=0$. The complete answer is
$$(0,0),(1,1),(0,2),(4,2).$$''',
'nzl_2021_3b49fd':r'''Cross multiplication and factorisation give
$$(a-c)(a+b+c+d)=0.$$
Since $a>c$, the total sum is zero. In particular $a>0$. If $c\le0$, then $ac\le0$, so only $c>0$ can maximise the product.

For positive $c$, use $b\ge c+1$ and $d\ge-2021$ to obtain
$$a=-b-c-d\le2020-2c.$$
Consequently
$$ac\le(2020-2c)c=510050-2(c-505)^2\le510050.$$
The tuple $(1010,506,505,-2021)$ satisfies the strict order and both nonzero-denominator conditions, and attains this bound. The maximum is $510050$.''',
'nzl_2024_c850b6':r'''Let $a_i$ count the red points in row $i$, for $1\le i\le2024$. A pair of columns can be red together in at most one row. Hence
$$\sum_{i=1}^{2024}\binom{a_i}{2}\le\binom{40}{2}=780.$$
For every nonnegative integer $a$, $a\le1+\binom a2$. Summing this inequality gives at most $2024+780=2804$ red points.

To attain the bound, use $780$ rows, one for each pair of columns, and place red points in that pair. Put one red point in each remaining row. No column pair occurs twice, so no forbidden rectangle exists.''',
'zaf_2024_b1b718':r'''Write the radii of $\Gamma_1,\Gamma_2,\Gamma_3$ as $a,b,c$, and put $s=a+c$. As the large-circle centre is on $O_1O_3$, the two endpoint circles occupy a diameter: its radius is $s$, with $OO_1=c$ and $OO_3=a$.

Take $O_1=(0,0)$, $O_3=(s,0)$ and $O=(c,0)$, and write $O_2=(u,v)$. External and internal tangency give
$$u^2+v^2=(a+b)^2,\quad (u-s)^2+v^2=(b+c)^2,\quad (u-c)^2+v^2=(s-b)^2.$$
Subtracting the first two gives $u=a+b(a-c)/s$. Substitution into the third then yields
$$b=\frac{acs}{a^2+ac+c^2}.$$
In particular $bs>ac$. Therefore
$$(a+b)^2+(b+c)^2-(a+c)^2=2(b^2+bs-ac)>0.$$
By the cosine rule in $O_1O_2O_3$, the angle at $O_2$ is strictly less than $90^\circ$.''',
'zaf_2023_3961a2':r'''View the flight network as a tree rooted at Kimberley. A permissible removed set is downward closed: removing a vertex requires removing all its descendants. Deleting any $k$ original leaves gives the lower bound $\binom tk$ (interpreted as zero for $k>t$).

Partition all non-root vertices into $t$ downward paths, each ending at a different original leaf. Such a partition can be obtained by having each non-leaf vertex choose one child to continue its path. In any permissible removed set, its intersection with each fixed path is a suffix, because all descendants of a removed vertex are removed. Thus the removed set is uniquely determined by the $t$ suffix lengths $k_1,\ldots,k_t$.

These are nonnegative integers summing to $k$. There are $\binom{t+k-1}{k}$ such weak compositions, so the desired upper bound follows.'''
}
fixes={k:{'solution':v,'solutionKind':'original-exposition'} for k,v in d.items()}
fixes['zaf_2023_3961a2']['statement']=r'''A finite tree has a distinguished root and $t$ leaves other than the root. Let $C$ count the sets of $k$ non-root vertices whose deletion leaves every remaining vertex connected to the root. Prove
$$\binom tk\le C\le\binom{t+k-1}{k}.$$
Here $\binom tk=0$ when $k>t$. This is the mathematical form of the original airport-network problem.'''
json.dump(fixes,open(P+'fixes.json','w'),indent=2)
