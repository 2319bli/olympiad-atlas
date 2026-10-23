import json
P='/workspace/sites/olympiad-atlas/research/oceania/'
items=[];ledger=[]
urls={2018:'https://drive.google.com/file/d/13ntL170SGpdpcFh6hi9sfIYeIfcOooxk/view',2019:'https://drive.google.com/file/d/1uHXSpX8FFra0-ziRDmgrzS8wDmAppee6/view',2020:'https://drive.google.com/file/d/1uT0UigKhfie2dmSA4o1VwXJ6be3n_P-8/view'}
def meta(y,n):return dict(id=f'nga_senior_r2_{y}_{n}',country='Nigeria',competition='Nigerian Mathematics Olympiad — Senior Round 2',year=y,section='',number=str(n),sourceUrl=urls[y])
def add(y,n,d,t,tags,s,sol,r):
 m=meta(y,n);items.append(dict(**m,statement=s,solution=sol,solutionUrl=None,topic=t,tags=tags,difficulty=d,ratingReason=r,reviewStatus='individually-assessed',solutionKind='original-exposition',notes='National Mathematical Centre original paper, publicly mirrored by Special Maths Academy; scan visually checked including cover date. Independently written mathematical paraphrase and proof.'))
 ledger.append(dict(**m,difficulty=d,status='reviewed',included=True,reason=r))
def skip(y,n,d,r,status=None):ledger.append(dict(**meta(y,n),difficulty=d,status=status or ('reviewed' if d is not None else 'pending-solution-review'),included=False,reason=r))
add(2018,1,4.5,'Number Theory',['divisibility','symmetric expressions','Egyptian fractions'],r'Find all triples of distinct integers $x,y,z>1$ for which $z\mid xy-1$, $x\mid yz-1$ and $y\mid xz-1$.',r'''The triples are the six permutations of $(2,3,5)$.

Each pair of variables is coprime: a common divisor of $x,y$, for example, would divide both $yz$ and $yz-1$. The integer $xy+xz+yz-1$ is divisible by each of $x,y,z$, and hence by their product. Therefore
$$K=\frac1x+\frac1y+\frac1z-\frac1{xyz}$$
is an integer. Assume $2\le x<y<z$. Clearly $K>0$, and $K<1/2+1/3+1/4<2$, so $K=1$. If $x\ge3$, then $K<1/3+1/4+1/5<1$, impossible. Thus $x=2$.

The equation $K=1$ becomes $2y+2z+yz-1=2yz$, or $(y-2)(z-2)=3$. With $y<z$ this gives $y=3,z=5$. The three divisibilities are immediate for these values.''','Pairwise coprimality allows the three congruences to be combined into one small positive integer; an ordering bound then reduces the classification to a factorization.')
skip(2018,2,3.5,'The identity(a²+c²)(b²+d²)=(ab+cd)²+(ad−bc)²=2017, a prime, forces the sum of the two factors to be2018; (a,b,c,d)=(1,44,0,9) attains it.')
skip(2018,3,None,'The printed statement allows AC andBD to have the same midpointW, making E=F=W and the claimed third triangle degenerate; e.g.A=(1,0),C=(−1,0),B=(0,1),D=(0,−1). Withheld pending confirmation of intended nondegeneracy.','withheld-malformed')
skip(2018,4,None,'The relation has no stated nonzero or defined-recurrence assumptions. A sequence with only a2017=1 and all other terms0 satisfies every displayed relation but violates a2017=a1. Withheld rather than silently imposing a domain.','withheld-malformed')
add(2018,5,4,'Algebra',['factorization','telescoping products','perfect squares'],r'''Prove that the product
$$\prod_{r=2}^{22}\frac{r^6-1}{r^2-1}$$
is a perfect square.''',r'''Factor each quotient as
$$\frac{r^6-1}{r^2-1}=r^4+r^2+1=(r^2+r+1)(r^2-r+1).$$
The second factor equals $(r-1)^2+(r-1)+1$. Thus every intermediate factor occurs twice, leaving
$$\prod_{r=2}^{22}\frac{r^6-1}{r^2-1}
=3(22^2+22+1)\left(\prod_{r=2}^{21}(r^2+r+1)\right)^2.$$
Since $3(22^2+22+1)=3\cdot507=39^2$, the original product is the square of $39\prod_{r=2}^{21}(r^2+r+1)$.''','A quartic factorization must be combined with a shifted index; the deliberately chosen endpoint makes the two unpaired factors a square.')
add(2018,6,4.5,'Combinatorics',['grid counting','finite-state recurrence','probability'],r'Independently colour each cell of a $3\times4$ rectangular grid red or green, with both colours equally likely. Find the probability that no $2\times2$ block is entirely green.',r'''There are $2^{12}=4096$ equally likely colourings. Encode each column by a three-bit mask, with1 meaning green. Two successive masks are compatible exactly when their intersection does not contain two consecutive1s.

Among the eight masks, five ($000,001,010,100,101$) contain no consecutive1s; each can follow any mask. The masks $011,110$ each forbid itself and $111$ as the previous mask. Mask $111$ forbids $011,110,111$.

Let $a_j$ be the number of valid $j$-column grids ending in any one specified mask of the first group, $b_j$ the corresponding number for either of $011,110$, and $c_j$ the number ending in $111$. Symmetry and the compatibility rules give
$$a_{j+1}=5a_j+2b_j+c_j,\quad b_{j+1}=5a_j+b_j,\quad c_{j+1}=5a_j.$$
Starting with $(a_1,b_1,c_1)=(1,1,1)$ gives successively
$$(8,6,5),\qquad(57,46,40),\qquad(417,331,285).$$
Hence there are $5\cdot417+2\cdot331+285=3032$ permitted grids, and the probability is
$$\frac{3032}{4096}=\frac{379}{512}.$$''','The overlapping forbidden blocks prevent independent-event counting; reducing column patterns to three state classes gives a compact exact enumeration.')
skip(2018,7,3,'Use11·1024 one-bits in0..2047 and complement the29 omitted numbers2019..2047 with0..28; the answer is11012.')
skip(2018,8,3.5,'AB is a diameter, so AC is perpendicular to the tangentBC and parallel to OT. The equal base angles of isoscelesAOT imply equal chord lengthsBD=CD on the first circle.')
skip(2018,9,2.5,'The Fibonacci addition identity gives F(2n−1)=F(n)²+F(n−1)² directly; the addition identity follows by a one-variable induction.')
skip(2018,10,3.5,'The kth-largest entry in column4 cannot exceed(37−3k)² because it and all larger fourth-column entries need two still-larger row mates. Values34²,31²,...,19² attain the bound4371 with consecutive triples in columns4–6.')
exec(open(P+'nigeria_extra.py').read())
json.dump(items,open(P+'nigeria.json','w'),indent=2)
json.dump(ledger,open(P+'nigeria-ledger.json','w'),indent=2)
print(len(items),len(ledger))
