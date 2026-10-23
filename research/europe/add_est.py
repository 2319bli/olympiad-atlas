import json
from pathlib import Path
p=Path(__file__).parent
R=json.loads((p/'reviews.json').read_text())
def put(s,d,t,ts,why,**kw):R['est_2025_'+s]={'difficulty':d,'topic':t,'tags':ts.split(','),'reason':why,**kw}
put('087156',2.5,'Combinatorics','counting,bounded choices','Choosing the numbers of apples and pears gives only a small bounded lattice-point count; below the target band.')
put('18de17',4.5,'Geometry','incircle,reflection,angle bisectors','The useful step is to reflect both endpoints in the incentre and show that their images lie on the opposite side, turning the required tangent into a parallel line.')
put('1ce03f',4.5,'Algebra','functional equations,substitution','Substitution at y=1 almost forces a quadratic, but the exceptional value f(1)=1 must be eliminated by a second substitution.',solution=r'''Write $P(x,y)$ for the identity. At $y=1$ its left side is $f(0)$, so
$$f(0)=f(1)+1+2(x^2-f(x))(f(1)-1).$$
If $f(1)\ne1$, this forces $f(x)=x^2+c$ for a constant $c$. Substitution into the original equation gives
$$c^2(y^2-1)^2+c=1+2c-c^2.$$
Comparing the coefficient of $y^4$ gives $c=0$, which then gives $0=1$, a contradiction. Hence $f(1)=1$ and the displayed identity gives $f(0)=2$. Now put $y=0$ in the original equation:
$$f(-2)=3+2(x^2-f(x)).$$
Again $f(x)=x^2+c$, but $f(0)=2$ gives $c=2$, contradicting $f(1)=1$. Thus no such function exists.''',quarantine=True,notes='The transcribed solution and equation disagree; this record is withheld pending comparison with the primary booklet.')
put('1d743a',6,'Geometry','extremal geometry,right angles,diameter','The construction is easy, but the upper bound needs a longest-pair argument and a careful classification of the other points on its diameter circle.')
put('25f413',7,'Combinatorics','grid,extremal construction,distinct sums','Counting adjacent pairs gives the sharp lower bound, while attaining it needs a substantial diagonal numbering construction and verification of all edge sums.')
put('274850',5.5,'Combinatorics','strategy games,finite configurations','One must enumerate the eight triples, discover their two-row intersection structure, and use it to force the opponent to run out of legal moves.')
put('29d115',3,'Geometry','area,rectangles','The six component triangles and congruent rectangles give a direct area decomposition, below the target.')
put('2d4f0c',5,'Number Theory','digit sums,modular arithmetic,construction','Tracking trailing nines converts the two square digit sums into a congruence modulo 9; the lower bound on length then needs a matching construction.',solution=r'''Suppose $n$ ends in exactly $k$ nines. Because $n$ and $n+1$ have equally many digits, incrementing $n$ gives
$$s(n)-s(n+1)=9k-1.$$
Thus if $s(n)=a^2$ and $s(n+1)=b^2$, then $a^2-b^2\equiv-1\pmod9$. The square residues modulo 9 are $0,1,4,7$, so necessarily $a^2\equiv0$ and $b^2\equiv1\pmod9$. In particular $a$ is divisible by 3. If there are at most nine digits, $a^2\le81$, hence $a=3,6,$ or $9$ (a positive integer cannot have digit sum 0). For $a=3$, the equation $b^2=10-9k$ forces $k=1,b=1$, but a number ending in 9 with digit sum 9 is just 9, so the digit length increases. For $a=6$, $b^2=37-9k$; the possible nonnegative values $37,28,19,10,1$ give only $k=4,b=1$, but four trailing nines already use the full digit sum 36, again forcing $n=9999$. For $a=9$, a number with at most nine digits and digit sum 81 must be $999999999$, which again changes length. Therefore at least ten digits are needed.

The ten-digit number $7888888899$ has digit sum $81$; its successor $7888888900$ has digit sum $64$. Hence the minimum is **10 digits**.''',notes='The worked exposition corrects a missing digit in the transcribed example.')
put('300772',4.5,'Algebra','cyclic sequences,extremal inequalities,construction','Closing the cycle forces positive and negative increments to balance; this bounds the smallest increment sharply, and an odd-cycle construction is also required.')
put('392c62',4,'Combinatorics','probability,product bounds','The complement is a product of thirteen factors; pairing factors around their common mean yields a short rigorous bound below one half.')
put('39c08c',3,'Algebra','symmetric equations','The first two power-sum identities reduce the problem immediately to a quadratic and a short case split.')
put('3addda',3.5,'Geometry','cyclic quadrilaterals,angle chasing','Two standard cyclic quadrilaterals and a short angle chase suffice; slightly below the target.')
put('3fc636',4.5,'Number Theory','prime powers,divisibility,minimality','Finding examples is insufficient: the minimality proof classifies odd integers divisible by two prime squares and checks the small possibilities.')
put('427d9e',3.5,'Combinatorics','invariants,grid,knight moves','A single residue class of x+y modulo 3 provides a safe frog; the invariant is the main observation and the rest is immediate.')
put('42ed5c',3,'Geometry','tangents,Pythagoras','A pair of right triangles at a tangent point gives the distance formula directly.')
put('4632c9',4.5,'Geometry','circle angles,reflection,Thales theorem','The midpoint reflection creates a useful right angle and parallel lines; combining this with two circumcircle angles proves the requested angle.')
put('46d098',3.5,'Number Theory','decimal representation,divisibility','Translating deletion into 24m=a10^k leaves a short divisibility and terminal-digit classification.')
put('4f6fb6',2.5,'Number Theory','gcd and lcm,divisors','Factoring 2024 and using the common divisor implied by the difference gives only a few cases.')
put('582da8',5.5,'Number Theory','prime factors,construction,consecutive integers','The key construction uses a square and the product of its composite neighbours; the three-term example also requires understanding how repeated prime factors control the condition.')
put('5b5036',2.5,'Algebra','AM-HM,inequalities','The syrup total rewrites as a constant minus a reciprocal sum, so AM-HM resolves it directly.')
put('68c56e',4,'Geometry','tangent circles,similar triangles','Introducing the midpoint of the chord exposes a parallel line through the second centre and a fixed similarity ratio.')
put('6e266c',4,'Combinatorics','graph colouring,handshake lemma,construction','The two parts combine a cyclic distance colouring with a parity obstruction from the handshake lemma.')
put('707b33',4,'Algebra','polynomials,reciprocal roots,AM-GM','Palindromic coefficients pair nonzero roots with their reciprocals; equality needs separate attention to repeated roots at 1 and -1.')
put('7ea00a',2.5,'Geometry','area,reflection','A direct decomposition into equal-area reflected triangles gives the constant ratio.')
put('84d00b',4,'Combinatorics','directed graphs,ordering,counterexamples','The one-parent condition lets earlier-parent ordering propagate through a rooted forest; removing it requires an explicit counterexample.')
put('89b8d2',6.5,'Geometry','incircle,tangent-chord theorem,power of a point','Several angle relationships must first force collinearity and tangency; a final power-of-a-point identity proves the second cyclicity.')
put('8a1de2',6,'Combinatorics','parity,Hamilton paths,inductive construction','Parity rules out even length, while the odd case needs a carefully joined multidimensional serpentine traversal.')
put('8aae0a',2.5,'Number Theory','modular arithmetic,existence','The small choice n=10 verifies both divisibilities; no general classification is demanded.')
put('8e09bb',4,'Geometry','angle bisectors,cyclic quadrilaterals','Recognising a circle with diameter AB turns the perpendicular-bisector condition into an angle identity.')
put('9333dd',5.5,'Geometry','orthic triangle,circle geometry,isosceles trapezium','The midpoint of the hypotenuse supplies equal radii, but the auxiliary trapezium and subsequent circle angle relationships are non-obvious.')
put('95aebd',3,'Algebra','sum of squares,polynomials','Completing the quartic to (x²-x-45)²+x² proves strict positivity in one step.')
put('95f4b2',2,'Algebra','percentages','Writing the percentage multipliers gives p=q and both comparisons directly.')
put('98578a',5.5,'Geometry','incircle,equal chords,parallelograms','Equal-radius auxiliary circles turn matching angles into two crosswise equal lengths, revealing a parallelogram whose diagonals bisect each other.')
put('9965b2',2,'Number Theory','calendar,remainders','Counting the accumulated one- or two-day annual shifts is elementary modular bookkeeping.')
put('9c1dc1',1.5,'Combinatorics','counting letters','Each letter occurs exactly three times across the three words, so subtraction immediately gives the answer.')
put('9d14b4',4.5,'Geometry','incentre,circumcentre,similar triangles','A hidden pair of similar triangles produces a spiral similarity, making the incentre equidistant from the required two points.',solution=r'''Put $\gamma=\angle ACB$ and let $M=OJ\cap AB$. Since $OA=OB$, the line $OJ$ is the perpendicular bisector of $AB$. Also $\angle AOM=\gamma$, so $\angle OAB=90^\circ-\gamma=\angle CAD$. Their half-angle equalities give
$$\angle JAO=\angle EAC,\qquad \angle AOJ=\gamma=\angle ACE.$$
Hence triangles $AJO$ and $AEC$ are similar, giving $AJ/AE=AO/AC=1$. (Here $AO=AC$ is not generally true; instead use the corresponding ratios $AJ/AE=AO/AC$ together with the equal included angles to obtain the spiral similarity $AJE\sim AOC$.) That similarity yields $AJ/JE=AO/OC=1$. Finally $JA=JB$ because $J$ lies on the perpendicular bisector of $AB$, and therefore $JB=JE$.''',quarantine=True,notes='Source solution has several missing half-angle factors; a clean verified exposition is pending.')
put('bb01de',1.5,'Number Theory','divisibility','The equations force b divisible by 6; taking the least such b minimises all three terms.')
put('bee95e',3.5,'Number Theory','factorials,inequalities','The gap between consecutive factorials forces z to equal max(x,y), leaving two short equations.')
put('c05fe0',6.5,'Algebra','rearrangement inequality,gcd and lcm,invariants','The multiset of each prime exponent is invariant. Rearrangement gives both extrema, but realising the reverse pairing through legal moves is an additional substantial step.')
put('c0a1eb',7.5,'Combinatorics','grid colouring,extremal construction','The sharp zigzag construction is paired with a delicate maximal-block lower bound; the amount of structural work exceeds the target band.')
put('c5e6a1',4.5,'Number Theory','digits,case analysis','The quotient must be a single digit, then leading and trailing digit constraints jointly eliminate every larger value in several nontrivial cases.')
put('c6939b',3,'Algebra','functional inequalities,substitution','Independent choice of x+y and (x-y)² forces every value both at least and at most 1.')
put('d099a0',3,'Geometry','angle bisectors,midpoint of hypotenuse','The midpoint of a hypotenuse gives one isosceles triangle; comparing two expressions for the same angle forces a square.')
put('d18606',3.5,'Number Theory','square factors,digits','The prime 23 restricts the two-digit factors to four cases, after which squarefree parts settle the count.')
put('d849f4',4.5,'Algebra','telescoping sums,inequalities','A telescoping upper bound controls the completed hours, but the proof must also bound the larger positions before each backward movement.')
put('d9f93c',None,'Number Theory','geometric progressions,prime exponents','The radical in part (b) is inconsistent between the statement and the proposed construction; withheld rather than rated from a corrupted problem.',quarantine=True)
put('e3a9e2',5.5,'Geometry','reflection,diameter,cyclic quadrilaterals','Reflecting A over the opposite side and introducing a diameter produces a parallelogram; identifying the second circle intersection then reduces the result to a midpoint-of-hypotenuse fact.')
put('e7b0e4',4,'Combinatorics','counting,reciprocal pairs,products','The count needs a complete split according to the presence of 1 and repeated pair-products, with attention to the exceptional equal products.')
put('e84a17',3.5,'Geometry','areas,similar triangles','One equal-area pair is automatic and an area sum forces the second pair; similar triangles then give the ratio.')
put('ec0fd7',2.5,'Geometry','congruence,perimeters','A single SAS congruence and perimeter subtraction resolve the configuration.')
put('f0453a',5.5,'Number Theory','cubic factorisation,quadratic forms,modular arithmetic','The cubic identity reduces the search to divisors of 225; ruling out the three remaining values requires a modular obstruction for a quadratic form.',solution=r'''Use
$$x^3+y^3+z^3-3xyz=(x+y+z)(x^2+y^2+z^2-xy-yz-zx).$$
Modulo 3, the given equation forces $x+y+z\equiv0$. Write $x+y+z=3m$ and $x=m-a$, $y=m+a-c$, $z=m+c$. Substitution gives
$$m(a^2-ac+c^2)=225.$$
The quadratic factor is positive, so $m$ is a positive divisor of $225$. If $a=0$, we obtain $m=1,9,25,225$ by choosing respectively $c=15,5,3,1$. If $a=2c$, we obtain $m=3,75$ by choosing respectively $c=5,1$.

Only $m=5,15,45$ remain. For these, $a^2-ac+c^2$ is divisible by 5 but not by 25. This is impossible: modulo 5, if $c\not\equiv0$ then $t=a/c$ would satisfy $t^2-t+1=0$, whose discriminant $-3\equiv2$ is a non-square. Thus $5\mid c$, and then $5\mid a$, making the form divisible by 25. The possible sums are therefore
$$\boxed{3,9,27,75,225,675}.$$''',notes='The worked exposition repairs a reversed divisibility symbol in the transcription.')
for slug,r in R.items():
 if slug.startswith('aut_'):r['competition']='Austrian Mathematical Olympiad'
(p/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
