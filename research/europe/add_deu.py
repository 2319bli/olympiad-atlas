import json
from pathlib import Path
p=Path(__file__).parent;R=json.loads((p/'reviews.json').read_text())
def put(s,d,t,ts,why,st,sol):
 raw=json.loads((p/('deu_2022_'+s+'.json')).read_text());R['deu_2022_'+s]={'difficulty':d,'topic':t,'tags':ts.split(','),'reason':why,'statement':st,'solution':sol,'competition':'German IMO Selection Tests','section':raw['section'].replace('1. Auswahlklausur','Selection test 1').replace('2. Auswahlklausur','Selection test 2'),'solutionKind':'original-exposition','sourceUrl':'https://www.mathe-wettbewerbe.de/fileadmin/Mathe-Wettbewerbe/AIMO/Aufgaben_und_Loesungen_AIMO/2022_IMO_Auswahlklausuren_Lsg_HP.pdf','solutionUrl':'https://www.mathe-wettbewerbe.de/fileadmin/Mathe-Wettbewerbe/AIMO/Aufgaben_und_Loesungen_AIMO/2022_IMO_Auswahlklausuren_Lsg_HP.pdf'}
put('43206f',5.5,'Number Theory','cube-free integers,prime valuations,divisibility','Eliminating the denominator exposes a cube; the cube-free restriction converts that identity into a divisibility relation that sharply bounds n.',r'''Find all positive integers $n$ for which positive integers $a,b$ satisfy both: no prime cube divides $a^2+b+3$, and
$$\frac{ab+3b+8}{a^2+b+3}=n.$$''',r'''Writing $D=a^2+b+3$, rearrangement gives
$$(a+3-n)D=(a+1)^3.$$
The factor $t=a+3-n$ is positive. For each prime $p$, the exponent of $p$ in $D$ is at most 2. If the exponent in $t$ were smaller than that in $a+1$, then the identity would force the exponent in $D$ to be at least 3, impossible. Hence $a+1\mid t=a+3-n$. Positivity gives $n\le2$. If $n=1$, it would say $a+1\mid a+2$, impossible for positive $a$. Thus $n=2$, realised by $a=b=2$, for which $D=9$.''')
put('49eeeb',6,'Geometry','area bounds,grid points,extremal construction','The main insight bounds every quadrilateral by half the sum of squared distances to a common centre; rotation orbits attain the bound simultaneously.',r'''Fix a positive integer $k$. Partition the $4k^2$ lattice points $(x,y)$ with $0\le x,y<2k$ into $k^2$ groups of four, each group forming a nondegenerate quadrilateral. What is the maximum sum of the quadrilateral areas?''',r'''Let $O=(k-\tfrac12,k-\tfrac12)$. For any quadrilateral with consecutive vertices $A_1,\ldots,A_4$, decomposition into triangles and $2uv\le u^2+v^2$ give
$$[A_1A_2A_3A_4]\le\frac12\sum_{i=1}^4 OA_i\,OA_{i+1}\le\frac12\sum_{i=1}^4 OA_i^2,$$
where indices are cyclic. Therefore the total is at most half the sum of $OA^2$ over all lattice points.

Rotation through $90^\circ$ about $O$ permutes the lattice set and has orbits of exactly four points. Each orbit forms a square centred at $O$, attaining equality in both estimates. Summing squared distances gives
$$\frac12\sum_{x,y=0}^{2k-1}\left[(x-k+\tfrac12)^2+(y-k+\tfrac12)^2\right]=\boxed{\frac{k^2(4k^2-1)}3}.$$''')
put('9c37f9',6,'Number Theory','infinite pigeonhole principle,gcd,graphs','Two applications of the infinite pigeonhole principle create a four-vertex pattern; one then has to prove that this pattern forces exactly two gcd values on a triangle.',r'''Let $S$ be an infinite set of positive integers. Suppose four distinct elements $v,w,x,y$ satisfy $\gcd(v,w)\ne\gcd(x,y)$. Prove that some distinct $a,b,c\in S$ satisfy
$$\gcd(a,b)=\gcd(a,c)\ne\gcd(b,c).$$''',r'''Colour each edge between two members of $S$ by their gcd. Every vertex sees finitely many colours, since its gcds divide that vertex. Some vertex $a$ sees two colours: otherwise all edges incident to each vertex would have one colour, forcing every edge in the complete graph to share a colour.

Choose an infinite set $T$ with all edges from $a$ coloured $g$, and a vertex $d$ with edge $ad$ coloured $h\ne g$. There are distinct $b,c\in T$ such that $bd,cd$ have the same colour $q$. If $q=g$, triangle $abd$ has exactly two colours. If $q\ne g$, consider the colour of $bc$: unless it is $g$, triangle $abc$ has exactly two colours; if it is $g$, triangle $bcd$ has exactly two colours. In every case, relabel the vertices of the resulting triangle to obtain the required equality and inequality.''')
put('cd4037',6.5,'Algebra','floor functions,extremal construction,induction','Ordering reduces to distinct integers; a dyadic induction with replacement of a large entry proves the lower bound, and an unusual permutation-like construction achieves it.',r'''Real numbers $a_1,\ldots,a_{2022}\ge1$ satisfy $|a_i-a_j|\ge1$ whenever $i\ne j$. Find the smallest possible value of
$$\sum_{i=1}^{2022}\left\lfloor\frac{a_i}{i}\right\rfloor.$$''',r'''The answer is 11. Replacing the smallest entry by 1, the next by 2, and so on cannot increase the sum, so it suffices to bound sums for distinct positive integers.

We prove that for $2^t$ distinct positive integers the first $2^t$ terms have sum at least $t+1$. The base $t=0$ is clear. Let $h=2^{t-1}$ and choose an entry at least $2h$. If its index exceeds $h$, it contributes at least 1 beyond the first half, which contributes at least $t$ by induction. If its index $i$ is at most $h$, choose an integer $b\in\{1,\ldots,h\}$ absent from that half. Replacing the large entry by $b$ decreases its floor by at least 1, because the original entry is at least $b+i$. The modified half still has distinct positive entries, so its sum is at least $t$, giving at least $t+1$ before replacement.

The first 1024 terms therefore contribute at least 11. For equality, set $a_i=i-1$ when $i$ is not a power of two, and $a_{2^s}=2^{s+1}-1$. All entries are distinct. Only the eleven power-of-two positions contribute, each contributing 1.''')
put('fc9ef6',5,'Geometry','cyclic quadrilaterals,concurrency,directed angles','Two auxiliary cyclic quadrilaterals must be found before a final angle equality forces the desired three lines to meet.',r'''In parallelogram $ABCD$, suppose $AC=BC$. Take $P$ on ray $AB$ beyond $B$. The circle $(ACD)$ meets $PD$ again at $Q$, and the circle $(APQ)$ meets $PC$ again at $R$. Prove that $CD,AQ,BR$ are concurrent.''',r'''Use directed angles modulo $180^\circ$. The length condition and parallel sides give
$$\angle BAC=\angle CBA=\angle DCA=\angle ADC.$$
Let $S=AQ\cap CD$. Since $CD\parallel AP$ and $A,P,Q,R$ are cyclic, $\angle CSQ=\angle PAQ=\angle CRQ$, so $C,S,R,Q$ are cyclic. Also
$$\angle CRA=-\angle ARP=\angle DQA=\angle DCA=\angle CBA,$$
so $A,B,R,C$ are cyclic. It follows that
$$\angle SRC=\angle SQC=\angle ADC=\angle BAC=\angle BRP.$$
As $P,R,C$ are collinear, this says $S,R,B$ are collinear, proving concurrence.''')
(p/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
