import json
from pathlib import Path
p=Path(__file__).parent;R=json.loads((p/'reviews.json').read_text())
U3='https://www.matematickaolympiada.cz/media/3796212/a74iii.pdf';U4='https://www.matematickaolympiada.cz/media/3820843/a74iv.pdf'
def put(s,d,t,ts,why,**kw):
 raw=json.loads((p/('cze_2025_'+s+'.json')).read_text());regional='January' in raw['section'];R['cze_2025_'+s]={'difficulty':d,'topic':t,'tags':ts.split(','),'reason':why,'sourceUrl':U3 if regional else U4,'solutionUrl':U3 if regional else U4,'section':'Category A, regional round (14 January 2025)' if regional else 'Category A, national final (17–18 March 2025)',**kw}
put('15733c',4.5,'Geometry','tangent-chord theorem,fixed point,cyclic quadrilaterals','The tangent conditions reveal a fixed isosceles right triangle; two circles with diameters then yield the constant angle.',solution=r'''Let $S=BE\cap CD$, considering first triangles $ABC$ on one fixed side of $BC$. The tangent-chord theorem gives $\angle CBE=\angle BCD=45^\circ$. Hence $SBC$ is the fixed isosceles right triangle with hypotenuse $BC$.

Both $\angle DPB$ and $\angle DSB$ are right, so $B,P,S,D$ are cyclic. If $\beta=\angle ABC$, this gives $\angle BSP=90^\circ-\beta$. Likewise $C,Q,S,E$ are cyclic and $\angle QSC=90^\circ-\gamma$, where $\gamma=\angle ACB$. Therefore
$$\angle PSQ=90^\circ-[(90^\circ-\beta)+(90^\circ-\gamma)]=\beta+\gamma-90^\circ=45^\circ.$$
Reflecting $A$ across $BC$ does not change its projection points $P,Q$, so the same fixed choice of $S$ works for triangles on either side.''')
put('e16bfb',2.5,'Algebra','factorisation,sum of squares','Cancelling a-b gives a²+ab+b²=1; the bounds follow directly from the squares of a+b and a-b.')
put('f7ba19',3.5,'Number Theory','percentages,divisibility','The vote equation gives n(99-n)=100a; divisibility by 25 and 4 leaves only two total vote counts and the same a=18.')
put('b3facd',3.5,'Algebra','symmetric equations,opposite pairs','The vanishing first and third symmetric sums make the root polynomial even, pairing the variables into opposites; the possible equality counts are then immediate.')
put('1bb427',5.5,'Geometry','extremal angles,construction','The lower bound averages four angles after a careful planar decomposition, and a nearly limiting symmetric construction is needed to make the integer threshold sharp.',solution='The answer is 135. The official worked solution proves the strict lower bound by summing four angles around the two interior points, then constructs a symmetric configuration with every angle at most 136°. The linked PDF includes both the construction diagram and the complete angle verification.',solutionKind='source-link')
put('7cae1e',7,'Number Theory','subset sums,binary representation,prime factors','The local uniqueness condition must classify n as a power of 2 or a power of 2 times a special prime power; a mixed-base representation then proves global uniqueness.',solution='The official solution classifies the possible prime factorisations and then uses uniqueness of binary and base-p expansions. Open the linked PDF, problem 3, for the complete worked proof.',solutionKind='source-link')
put('bb8f92',4.5,'Number Theory','largest prime factor,extremal argument,circular arrangement','Working backwards from the largest two prime outputs forces three primes spaced by 2; divisibility by 3 pins down the set, and an explicit cycle verifies it.',solution=r'''Let $p$ be the largest prime in the set; then $p\ge5$. To obtain $p$ as a largest prime factor, two distinct entries must have sum divisible by $p$ but less than $2p$, hence sum exactly $p$. Thus they are $2$ and $p-2$, so both belong to the set and $p-2$ is the second largest entry.

To obtain output $p-2$, a pair sum is either $p-2$ or $2(p-2)$, since its maximum is $2p-2<3(p-2)$. In the first case the pair is $2,p-4$; in the second, the larger entry must be $p$, leaving $p-4$. Thus $p,p-2,p-4$ are all prime. One is divisible by 3, forcing these to be $7,5,3$. Together with 2, the only possible set is $\{2,3,5,7\}$.

The circular order $2,5,3,7$ gives pair sums $7,8,10,9$, whose largest prime factors are $7,2,5,3$. Hence this set works.''')
put('d36a7f',6.5,'Combinatorics','grid construction,nonattacking kings,modular arithmetic','The obstruction uses two-row occupancy and a special n=7 contradiction; the general construction combines two modular patterns and needs a separate n=8 example.',solution=r'''Exactly $n\ge8$ work. For $n\ge2$, the four marked cells in two adjacent rows must occupy four columns separated by at least one unused column, forcing $n\ge7$. If $n=7$, they must occupy columns $1,3,5,7$. Apply this to row pairs $(1,2),(3,4),(5,6)$: column 1 would contain at least three marked cells, impossible. The case $n=1$ is immediate.

For $n=8$, mark the following column pairs in successive rows:
$$(2,4),(6,8),(2,4),(6,8),(1,3),(5,7),(1,3),(5,7).$$
Every column appears twice, and successive row pairs have no columns within distance 1.

For $n\ge9$, index rows and columns by $0,\ldots,n-1$ and mark
$$(k,2k\bmod n),\qquad(k,(2k+5)\bmod n),\quad 0\le k<n.$$
There are two per column. For odd $n$, each pattern hits every row once; for even $n$, the first hits every even row twice and the second every odd row twice. Within a column the cyclic row-distance is at least 4. Between adjacent columns, possible cyclic row-differences are $2,3,7$ up to sign, each having distance at least 2 modulo $n\ge9$. Thus no two marked cells touch.''')
put('d12126',5.5,'Geometry','antipodal point,orthocentre,cyclic quadrilaterals','Introducing the point opposite A creates a midpoint relation with H; showing this point lies on the second circle turns two radii into perpendicular bisectors.',statement=r'''Let $ABC$ be acute, with circumcentre $O$, circumcircle $\omega$, orthocentre $H$, and midpoint $M$ of $BC$. The line $AH$ meets $\omega$ again at $D$, and $DM$ meets $\omega$ again at $E$. Let $F\ne E$ be the second intersection of $AE$ with the circle $(OME)$. Prove $FH=FA$.''',solution=r'''Let $X$ be the point opposite $A$ on $\omega$. The quadrilateral $BXCH$ is a parallelogram, since $BX\parallel CH$ and $CX\parallel BH$. Therefore $M$ is also the midpoint of $HX$.

As $OM\parallel AD$, cyclic angles give
$$\angle MOX=\angle DAX=\angle DEX=\angle MEX.$$
Hence $O,M,E,X$ are cyclic. Because $AX$ is a diameter of $\omega$, $AE\perp EX$, so $FE\perp EX$. Thus $FX$ is a diameter of the circle $(OME)$, giving $FO\perp OX$ and $FM\perp MX$.

Since $O$ is the midpoint of $AX$, $FO$ is its perpendicular bisector, so $FA=FX$. Since $M$ is the midpoint of $HX$, $FM$ is its perpendicular bisector, so $FH=FX$. Therefore $FA=FH$.''',notes='The original official paper says F≠E; the MathNet statement incorrectly says F≠A. Corrected against the national-final PDF.')
if (p/'cze_2025_4aea8b.json').exists():put('4aea8b',3,'Combinatorics','double counting,pigeonhole principle','Each round puts 11 of the 21 pairs together; averaging over rounds gives a pair together more than half the time.')
(p/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
