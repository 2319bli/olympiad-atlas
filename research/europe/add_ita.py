import json
from pathlib import Path
p=Path(__file__).parent;R=json.loads((p/'reviews.json').read_text())
def put(s,d,t,ts,why,**kw):R['ita_2024_'+s]={'difficulty':d,'topic':t,'tags':ts.split(','),'reason':why,**kw}
put('08cd7a',5,'Combinatorics','binary strings,characterisation,counting','The count comes only after characterising failure by the two endpoint pairs; the existence proof partitions into maximal monotone runs.',statement=r'''A binary string is to be partitioned into blocks of two or three consecutive digits. The partition is valid if either every block is nondecreasing, or every block is nonincreasing.

(a) Prove that a string consisting of $m$ zeros followed by $n$ ones, with $m+n\ge2$, admits a valid partition.

(b) For $\ell\ge4$, prove that exactly $2^{\ell-3}$ binary strings of length $\ell$ admit no valid partition.''',solution=r'''(a) Any length at least 2 is a sum of 2s and 3s; every resulting block is nondecreasing.

(b) A nondecreasing-block partition is impossible if the string begins with 10 or ends with 10, since the first or last block would contain that descent. Conversely, if neither happens, split at every occurrence of 10. Each resulting substring is nondecreasing and has length at least 2: an interior substring contains both digits, and the two endpoint substrings are not singletons by the endpoint assumptions. Part (a) partitions them as required.

Similarly a nonincreasing-block partition exists exactly when the string neither begins nor ends with 01. Thus both kinds fail exactly for strings beginning 01 and ending 10, or beginning 10 and ending 01. Each class has $2^{\ell-4}$ members, yielding $2^{\ell-3}$.''',notes='The endpoint condition is stated explicitly to avoid a reversed initial digit in the transcription.')
put('10d89b',2.5,'Number Theory','divisor sums,prime factorisation','Ending in 50 fixes the exponent of 2 and bounds the exponent of 5, leaving a short product of geometric sums.')
put('2e8867',3,'Number Theory','divisibility,quadratic bounds','Divisibility forces n=1012k; substitution leaves a small bounded quadratic count.')
put('39e48e',4,'Combinatorics','rotational symmetry,counting','The count combines assignment of seven complementary face-pairs with the 24 rotations of a cube; one must justify that the rotation action has no stabilisers.',statement=r'''A truncated cube has six regular octagonal faces and eight equilateral triangular faces. Label its faces with $1,\ldots,14$, once each, so that opposite faces always have the same sum. How many different labellings are there, counting two as the same when a rotation takes one to the other?''',solution=r'''There are seven opposite-face pairs. Their common sum must be $105/7=15$, so the numerical pairs are $(1,14),(2,13),\ldots,(7,8)$. Assign them to the seven geometric pairs in $7!$ ways, and choose each pair's orientation in $2^7$ ways.

The truncated cube has 24 rotational symmetries: choose which of six octagonal faces goes on the bottom, then one of four rotations about the vertical axis. Every orbit of a labelling has exactly 24 members, since distinct labels prevent a nonidentity rotation from fixing it. Hence the required number is $2^7\cdot7!/24=\boxed{26880}$.''')
put('447cc7',3,'Combinatorics','bijections,ordered blocks','The three empty cells split the numbers into four ordered blocks; assigning each number to its block determines the internal order.')
put('511c40',3,'Geometry','solid geometry,Pythagoras','Pairwise perpendicular edges give three Pythagorean identities, immediately forcing all base angles to be acute.')
put('513435',3,'Number Theory','congruences,least common multiples','All conditions say that b-a is divisible by consecutive integers; the minimum follows from a small lcm.')
put('54f8a8',1,'Number Theory','modular arithmetic','The total is divisible by 5, so the omitted number must be a multiple of 5.')
put('671657',3,'Algebra','polynomial iteration,integer roots','Tracing integer preimages of 0,-1,2 quickly stabilises at {-1,0,1,2}.')
put('690d7e',4,'Geometry','angle bisectors,cyclic quadrilaterals,similar triangles','The first two parts guide the cyclic angle chase; the final reflected-point construction requires a parallelogram and the angle-bisector theorem.',statement=r'''In acute triangle $ABC$, let $AD$ be the internal angle bisector, with $D\in BC$. The circle $(ABD)$ meets line $AC$ again at $E$, and the circle $(ACD)$ meets line $AB$ again at $F$. Let $P=BE\cap CF$.

(a) Prove $PB=PC$.

(b) Prove $BD/BE=CD/CF$.

(c) Reflect $F$ in the midpoint of $BC$ to obtain $F'$. Prove that triangle $EBF'$ is similar to triangle $ABC$.''',solution=r'''(a) Cyclic angles give $\angle BCP=\angle DAF$ and $\angle CBP=\angle DAE$. These are equal because $AD$ bisects $\angle BAC$.

(b) The same cyclicities give $\angle DFC=\angle DAC=\angle DEB$ and $\angle DCF=\angle EBD$. Thus $FCD\sim EBD$, yielding the ratio.

(c) The reflection makes $CFBF'$ a parallelogram. Therefore $BF'=CF$, and the angle between $BE$ and $BF'$ is the sum of the two angles equal to the halves of $\angle BAC$, hence equals $\angle BAC$. Part (b), followed by the angle-bisector theorem, gives
$$\frac{BF'}{BE}=\frac{CF}{BE}=\frac{CD}{BD}=\frac{AC}{AB}.$$
The two sides about the equal angles are proportional, proving the required similarity.''')
put('7e473a',None,'Geometry','tangential quadrilaterals,area','The transcription uses a tangency inference without sufficient justification; withheld pending a verified proof.',quarantine=True)
put('8b59b6',4.5,'Combinatorics','grid colouring,propagation,counting','A same-colour adjacent pair forces an alternating pattern in the perpendicular direction; classifying the boundary row and column is needed to count without overlap.',statement=r'''Colour a $5\times5$ grid red or blue so that each cell shares a side with at most one cell of its own colour. How many colourings are possible?''',solution=r'''Any $2\times2$ block must have two cells of each colour: three of one colour would give a cell two same-colour neighbours. Consequently three entries of such a block determine the fourth, and the first row and column determine the whole grid.

If the first row contains an equal-colour adjacent pair, the two cells beneath it must both have the opposite colour, and this repeats down the grid. The whole grid is then forced to alternate the first row with its colour-complement. Such a first row may be any binary row with no three consecutive equal digits except the two alternating rows. The number of length-5 binary rows avoiding three equal digits is 16 (the counts for lengths 1 through 5 are $2,4,6,10,16$), so this gives 14 colourings.

Likewise, 14 colourings have a same-colour adjacent pair in the first column. These classes are disjoint, because in the first class the first column alternates. The remaining two possibilities are the checkerboards. Thus the answer is $14+14+2=\boxed{30}$.''')
put('b41d57',6,'Number Theory','extremal products,smoothing,prime valuations','Several exchange arguments force a nearly consecutive optimal set; only after proving this structure can the terminal-zero count be read from a factorial.',statement=r'''Let $N$ be the largest product of distinct positive integers whose sum is 2024. How many trailing zeros does the decimal representation of $N$ have?''',solution=r'''Let $A$ be an optimal set. It contains no 1: replacing 1 and the largest entry $M$ by $M+1$ increases the product. There is at most one missing integer between its minimum and maximum. Otherwise take $a<b$ in $A$ with distinct absent values $a+1,b-1$; replacing $a,b$ by these values preserves the sum and increases the product.

Write $m=\min A$. If $m\ge5$, replace $m$ by $2,m-2$, increasing the product. If $m=4$, the next entry is 5 or 6 because there is at most one gap. Replace $4,5$ by $2,3,4$, or $4,6$ by $2,3,5$, again improving the product. Hence $m=2$ or 3.

If $m=3$ and a gap $r\le M-2$ exists, replace $r+2$ by $2,r$, increasing the product. Thus in this case $A$ is either $\{3,\ldots,M\}$ or that set without $M-1$. Their sums are $M(M+1)/2-3$ and $M(M-1)/2-2$, neither of which is 2024. Therefore $m=2$.

Now $A$ is $\{2,\ldots,M\}$ with at most one gap. The sum condition forces $M=64$ and the missing value 55. Thus $N=64!/55$. There are many more factors 2 than 5, and
$$v_5(N)=\lfloor64/5\rfloor+\lfloor64/25\rfloor-1=12+2-1=\boxed{13}.$$''')
put('e75c1a',3,'Geometry','similar triangles,perpendicular bisector','A cyclic right angle gives a perpendicular bisector; one similarity fixes the required length.')
put('ebbd00',3.5,'Geometry','regular hexagons,areas','The shared diagonals fix the scale ratio, and a short dissection computes the overlap.')
put('f5856d',2.5,'Combinatorics','logic,cases','Split according to the common assertion being true or false, then minimise a linear vote margin.')
put('f842d9',2.5,'Algebra','quadratic discriminant','Substituting y/x reduces the condition directly to a nonnegative quadratic and b²≤4ac.')
for s,r in R.items():
 if s.startswith('ita_2024_'):
  raw=json.loads((p/(s+'.json')).read_text());r['section']='District round (21 February 2024)'+(' — '+raw['section'] if raw.get('section') else ' — proof problems');r['sourceUrl']='https://olimpiadi.dm.unibo.it/wp-content/uploads/2024/02/soluzioni2024.pdf';r['solutionUrl']=r['sourceUrl']
(p/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
