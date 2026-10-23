"""Explicit source-checked Latin restorations, with unchanged ledger ratings.

Source figures were restated in words. The Ecuador trigonometry solution corrects
the organizer's missing second root; Costa Rica Q1 uses an arc, not an angle.
"""
import json
from pathlib import Path
P=Path(__file__).resolve().parent
records=[{'comp': 'OMM State Final',
  'y': 2013,
  'n': 1,
  'topic': 'Combinatorics',
  'tags': ['Graph theory', 'Double counting', 'Algorithms & constructions'],
  'statement': 'Nine teams play a round-robin tournament, with no drawn games. A team earns one point for each win. '
               'Every team with at most two points is eliminated. What is the largest possible number of eliminated '
               'teams?',
  'reason': 'Count the games played solely among eliminated teams to bound their number; a regular five-team '
            'tournament provides the matching construction.',
  'country': 'Mexico',
  'source': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/final13.pdf',
  'ident': 'mx-omm-state-final-2013-1',
  'solution': 'If $k$ teams are eliminated, their internal games already contribute $k(k-1)/2$ wins, whereas they have '
              'at most $2k$ wins in total. Hence $k\\le5$. To attain five, arrange the five teams cyclically and let '
              'each beat the next two and lose to the other two; let all five lose to each of the remaining four '
              'teams. Thus the maximum is $5$.',
  'solutionUrl': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/solfinal13.pdf'},
 {'comp': 'OMM State Final',
  'y': 2013,
  'n': 4,
  'topic': 'Geometry',
  'tags': ['Coordinates & vectors', 'Angle bisectors', 'Midpoints'],
  'statement': 'Triangle $ABC$ is right-angled at $B$ and $AB=2BC$. A point $D$ on the internal bisector of $\\angle '
               'ABC$ satisfies $AD=DC$. Prove that the line through $A$ perpendicular to $BD$ bisects segment $DC$.',
  'reason': 'The angle-bisector and equal-distance conditions become a single linear equation in coordinates. The '
            'required midpoint then lies on an immediately identified perpendicular.',
  'country': 'Mexico',
  'source': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/final13.pdf',
  'ident': 'mx-omm-state-final-2013-4',
  'solution': 'Scale so that $B=(0,0),A=(2,0),C=(0,1)$. Write $D=(t,t)$. The equation $AD^2=DC^2$ gives '
              '$(t-2)^2+t^2=t^2+(t-1)^2$, hence $t=3/2$. The midpoint of $DC$ is $(3/4,5/4)$, lying on $x+y=2$, the '
              'perpendicular to $BD$ through $A$.',
  'solutionUrl': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/solfinal13.pdf'},
 {'comp': 'OMM State Final',
  'y': 2013,
  'n': 6,
  'topic': 'Algebra',
  'tags': ['Functional equations', 'Sequences & recurrences', 'Periodicity'],
  'statement': 'Let $f(x)=1/x$ and $g(x)=1-x$. Find $(g\\circ f)^{100}(2013)$, where the superscript denotes repeated '
               'composition.',
  'reason': 'Recognising the order-three cycle reduces one hundred compositions to one evaluation.',
  'country': 'Mexico',
  'source': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/final13.pdf',
  'ident': 'mx-omm-state-final-2013-6',
  'solution': 'For $h=g\\circ f$, $h(x)=(x-1)/x$, $h^2(x)=1/(1-x)$ and $h^3(x)=x$. The orbit of $2013$ avoids the '
              'undefined values. Since $100\\equiv1\\pmod3$, the answer is $2012/2013$.',
  'solutionUrl': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/solfinal13.pdf'},
 {'comp': 'OMM State Final',
  'y': 2014,
  'n': 1,
  'topic': 'Number Theory',
  'tags': ['Primes', 'Factorials', 'Divisibility & GCD'],
  'statement': 'Let $n$ be a positive integer and $p$ a prime such that $p\\nmid(3n)!$ but $p\\mid(3n+1)!+(3n+2)!$. '
               'Prove that $3\\mid p-1$.',
  'reason': 'Factor the factorial sum and use the strong size restriction on a prime absent from (3n)!. This leaves '
            'only the factor 3n+1.',
  'country': 'Mexico',
  'source': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/final14.pdf',
  'ident': 'mx-omm-state-final-2014-1',
  'solution': 'We have $p>3n$ and the sum factors as $(3n)!(3n+1)(3n+3)$. A prime divisor of $3n+3=3(n+1)$ is at most '
              '$\\max(3,n+1)\\le3n$. Therefore $p\\mid3n+1$. Since $p>3n$, this forces $p=3n+1$.',
  'solutionUrl': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/solfinal14.pdf'},
 {'comp': 'OMM State Final',
  'y': 2014,
  'n': 3,
  'topic': 'Combinatorics',
  'tags': ['Colouring', 'Double counting', 'Matchings'],
  'statement': 'An equilateral triangle of side $7$ is divided into unit equilateral triangles. Its lattice vertices '
               'are coloured red, blue and green so that every unit triangle has one vertex of each colour. The '
               'vertices are partitioned into pairs, each pair joined by a unit edge. Prove that the number of '
               'red–blue pairs equals the number of red–green pairs.',
  'reason': 'The local colouring rule forces a periodic triangular-lattice colouring. Counting the equal colour '
            'classes then gives the matching identity.',
  'country': 'Mexico',
  'source': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/final14.pdf',
  'ident': 'mx-omm-state-final-2014-3',
  'solution': 'The colour of any adjacent pair forces the colour of the third vertex, so the colouring is the standard '
              'periodic three-colouring, up to permutation. Rows of lengths $1,2,\\ldots,8$ contain $12$ vertices of '
              'each colour (this follows by listing the three residues in each row). If $x,y,z$ count red–blue, '
              'red–green and blue–green edges, respectively, counting blue and green vertices gives $x+z=12=y+z$, so '
              '$x=y$.',
  'solutionUrl': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/solfinal14.pdf'},
 {'comp': 'OMM State Final',
  'y': 2014,
  'n': 4,
  'topic': 'Algebra',
  'tags': ['Inequalities', 'AM–GM'],
  'statement': 'Prove that $4a^2+2b^4+c^8+d^8\\ge8abcd$ for positive real numbers $a,b,c,d$.',
  'reason': 'This is a direct eight-term AM–GM inequality once repeated terms are recognised.',
  'country': 'Mexico',
  'source': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/final14.pdf',
  'ident': 'mx-omm-state-final-2014-4',
  'solution': 'Apply AM–GM to four copies of $a^2$, two copies of $b^4$, and one each of $c^8,d^8$. Their product is '
              '$(abcd)^8$, so their sum is at least $8abcd$.',
  'solutionUrl': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/solfinal14.pdf'},
 {'comp': 'OMM State Final',
  'y': 2015,
  'n': 3,
  'topic': 'Number Theory',
  'tags': ['Parity', 'Modular arithmetic', 'Algebraic identities'],
  'statement': 'Prove that there do not exist $2015$ integers whose sum and product are both $2015$.',
  'reason': 'Oddness of every factor permits a modulo-four product expansion; comparing it with the prescribed sum '
            'gives the contradiction.',
  'country': 'Mexico',
  'source': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/final15.pdf',
  'ident': 'mx-omm-state-final-2015-3',
  'solution': 'All the integers $a_i$ would be odd. Put $a_i=1+2b_i$. Modulo $4$, $\\prod a_i\\equiv1+2\\sum b_i=\\sum '
              'a_i-2014\\equiv1$, whereas $2015\\equiv3\\pmod4$, a contradiction.',
  'solutionUrl': 'https://www.ommenlinea.org/wp-content/uploads/practica/finales/solfinal15.pdf'},
 {'comp': 'OMM National',
  'y': 2015,
  'n': 1,
  'topic': 'Geometry',
  'tags': ['Orthocentres', 'Arc midpoints', 'Angle chasing'],
  'statement': 'In triangle $ABC$ with orthocentre $H$, points $P\\in AB$ and $Q\\in AC$ lie on a line through $H$ and '
               'satisfy $\\angle PHB=\\angle CHQ$. Let $M$ be the midpoint of the arc $BC$ not containing $A$ on the '
               'circumcircle of $ABC$. Prove that $MP=MQ$.',
  'reason': 'The given equal angles and the perpendicularities defining H constrain the transversal; combining these '
            'with the arc-midpoint equalities yields an isosceles triangle. The short angle chase is the main step.',
  'country': 'Mexico',
  'source': 'https://www.ommenlinea.org/wp-content/uploads/2016/03/Tzaloa-1-2016.pdf',
  'ident': 'mx-omm-national-2015-1'},
 {'comp': 'OMM National',
  'y': 2016,
  'n': 6,
  'topic': 'Geometry',
  'tags': ['Circles & tangency', 'Coordinates & vectors', 'Perpendicularity'],
  'statement': 'Let $ABCD$ be a cyclic quadrilateral. The line through $A$ parallel to $BC$ meets $DC$ at $E$, and the '
               'line through $B$ parallel to $AD$ meets $DC$ at $F$. The perpendicular to $AE$ through $A$ meets $BC$ '
               'at $P$, and the perpendicular to $BF$ through $B$ meets $AD$ at $Q$. Prove that the circumcircles of '
               '$ADE$ and $BFC$ are tangent if and only if $DP\\perp CQ$.',
  'reason': 'The two conditions involve different auxiliary configurations. A full equivalence requires expressing '
            'both circle tangency and perpendicularity in a common metric or coordinate identity; the algebra and '
            'degeneracy checks are substantial.',
  'country': 'Mexico',
  'source': 'https://www.ommenlinea.org/wp-content/uploads/2017/03/Tzaloa-1-2017.pdf',
  'ident': 'mx-omm-national-2016-6'},
 {'comp': 'Cono Sur Mathematical Olympiad',
  'y': 2024,
  'n': 1,
  'topic': 'Number Theory',
  'tags': ['Perfect squares', 'Algorithms & constructions'],
  'statement': 'Prove that there are infinitely many quadruples of positive integers $(a,b,c,d)$ for which $ab+1$, '
               '$bc+16$, $cd+4$ and $da+9$ are all perfect squares.',
  'reason': 'A common-parameter construction makes all four expressions consecutive quadratic squares; finding '
            'compatible offsets is the sole structural step.',
  'country': 'International',
  'source': 'https://www.obm.org.br/content/uploads/2024/09/ConeSul_2024.pdf',
  'ident': 'latam-cono-sur-mathematical-olympiad-2024-1',
  'solution': 'For any positive integer $t$, take $(a,b,c,d)=(t,t+2,t+10,t+6)$. The four expressions become '
              '$(t+1)^2,(t+6)^2,(t+8)^2,(t+3)^2$. Distinct $t$ give distinct quadruples.'},
 {'comp': 'Cono Sur Mathematical Olympiad',
  'y': 2024,
  'n': 3,
  'topic': 'Number Theory',
  'tags': ['Exponential Diophantine equations', 'Perfect squares', 'Modular arithmetic'],
  'statement': 'Find all positive integers $n$ for which $3^n-2^n-1$ is a perfect square.',
  'reason': 'Congruence obstructions alone do not settle every surviving exponent. The difficult part is excluding the '
            'remaining cases by a structured exponential-Diophantine argument, beyond routine testing or square '
            'bounds.',
  'country': 'International',
  'source': 'https://www.obm.org.br/content/uploads/2024/09/ConeSul_2024.pdf',
  'ident': 'latam-cono-sur-mathematical-olympiad-2024-3',
  'solutionAvailable': False},
 {'comp': 'Cono Sur Mathematical Olympiad',
  'y': 2024,
  'n': 5,
  'topic': 'Combinatorics',
  'tags': ['Permutations & arrangements', 'Counting', 'Recurrences & generating functions'],
  'statement': 'A permutation of $1,2,\\ldots,n$ is called magical if every entry $j$ has at least $\\lfloor '
               'j/2\\rfloor$ smaller entries to its left. Determine the number of magical permutations.',
  'reason': 'Insert entries in increasing order: the condition for the new largest entry gives an independent number '
            'of slots and does not affect older entries.',
  'country': 'International',
  'source': 'https://www.obm.org.br/content/uploads/2024/09/ConeSul_2024.pdf',
  'ident': 'latam-cono-sur-mathematical-olympiad-2024-5',
  'solution': 'Insert $j$ into a magical permutation of $1,\\ldots,j-1$. Of the $j$ slots, precisely $j-\\lfloor '
              'j/2\\rfloor=\\lceil j/2\\rceil$ have enough smaller entries to the left. Previous conditions are '
              'unchanged. Hence the answer is $\\prod_{j=1}^n\\lceil j/2\\rceil=\\lfloor n/2\\rfloor!\\,\\lceil '
              'n/2\\rceil!$.'},
 {'comp': 'Ibero-American Mathematical Olympiad',
  'y': 2024,
  'n': 1,
  'topic': 'Number Theory',
  'tags': ['Divisors', 'Sets', 'Divisibility & GCD'],
  'statement': 'For a positive integer $n$, let $d(n)$ be its number of positive divisors. Prove that $d(a)+d(b)\\le '
               'd(\\gcd(a,b))+d(\\operatorname{lcm}(a,b))$ for all positive integers $a,b$, and determine all equality '
               'cases.',
  'reason': 'Viewing divisors as sets makes the inequality an inclusion–exclusion statement. The equality '
            'classification requires noticing when the least common multiple belongs to the union.',
  'country': 'International',
  'source': 'https://www.obm.org.br/content/uploads/2024/09/Ibero_2024.pdf',
  'ident': 'latam-ibero-american-mathematical-olympiad-2024-1',
  'solution': 'Let $D(m)$ be the set of positive divisors of $m$. Then $D(a)\\cap D(b)=D(\\gcd(a,b))$ and $D(a)\\cup '
              'D(b)\\subseteq D(\\operatorname{lcm}(a,b))$. Inclusion–exclusion gives the inequality. Equality means '
              'the union is the latter entire set, so the least common multiple itself divides $a$ or $b$. Thus '
              'equality holds exactly when $a\\mid b$ or $b\\mid a$, which also plainly suffices.'},
 {'comp': 'Ibero-American Mathematical Olympiad',
  'y': 2025,
  'n': 1,
  'topic': 'Algebra',
  'tags': ['Sequences & recurrences', 'Inequalities', 'Integer constraints'],
  'statement': 'A sequence of real numbers $a_1,a_2,\\ldots$ satisfies $a_1>0$ and $a_1a_2\\cdots '
               'a_n=a_1+\\cdots+a_{n-1}$ for every $n\\ge2$. What is the maximum possible number of integer terms in '
               'the sequence?',
  'reason': 'Dividing consecutive product–sum identities gives a monotonic reciprocal recurrence. After the first few '
            'terms, a short interval contains no integers, leaving a finite endpoint analysis.',
  'country': 'International',
  'source': 'https://www.obm.org.br/content/uploads/2025/10/Prova_Ibero_2025.pdf',
  'ident': 'latam-ibero-american-mathematical-olympiad-2025-1',
  'solution': 'Put $t=a_1>0$ and $S_k=a_1+\\cdots+a_k$. The identities give $a_2=1$, $a_3=a_4=1+1/t$, and, by dividing '
              'consecutive identities, $a_{n+1}=1+a_n/S_{n-1}$. In particular $a_5=1+1/(t+1)$ lies strictly between '
              '$1$ and $2$. Since $S_3=t+2+1/t\\ge4$ and all terms are positive, the same recurrence inductively keeps '
              'every $a_n$ with $n\\ge5$ strictly between $1$ and $2$. Thus only the first four terms can be integers. '
              'Setting $t=1$ makes them $1,1,2,2$, so the maximum is $4$.'},
 {'comp': 'OBM Level 2',
  'y': 2022,
  'n': 1,
  'topic': 'Combinatorics',
  'tags': ['Invariants', 'Algorithms & constructions'],
  'statement': 'Initially there are ten piles of stones, of sizes $1,2,\\ldots,10$. A move either merges two piles of '
               'at least two stones and adds two stones to the result, or takes two stones from a pile of at least '
               'four and splits the remainder into two nonempty piles. Play stops when no move is possible. (a) Give a '
               'sequence that stops. (b) Tabulate the number of piles and total stones initially and after your first '
               'five moves. (c) Prove that every terminal position has the same number of one-stone piles.',
  'reason': 'The linear invariant total stones plus twice the number of piles determines the terminal singleton count '
            'after a short classification of possible terminal positions.',
  'country': 'Brazil',
  'source': 'https://www.obm.org.br/content/uploads/2022/11/obm2022_nivel2.pdf',
  'ident': 'br-obm-level-2-2022-1',
  'solution': 'Let $S$ be the number of stones and $P$ the number of piles. Both moves preserve $S+2P=75$. At '
              'termination all piles have size at most three and at most one has size greater than one. If there are '
              '$k$ singleton piles, the invariant gives either $3k=75$, $3k+4=75$, or $3k+5=75$. Only the first is '
              'possible, and $k=25$. For a terminating sequence, repeatedly split any pile of size $m\\ge4$ into sizes '
              '$1,m-3$ after removing two stones. This strictly reduces $S$. When only piles of sizes 1,2,3 remain, '
              'merge two nonsingleton piles if present, then resume splitting; this reduces their number. Starting by '
              'splitting piles $10,9,8,7,6$ gives $(P,S)=(10,55),(11,53),(12,51),(13,49),(14,47),(15,45)$. Continue '
              'the described process to reach 25 singletons.'},
 {'comp': 'OMAPA Final Level 3',
  'y': 2010,
  'n': 1,
  'topic': 'Geometry',
  'tags': ['Areas', 'Similarity & congruence'],
  'statement': 'A square $ABCD$ has side length $60$. Points $M\\in AD$ and $N\\in CD$ are chosen so that $BM$ and '
               '$BN$ divide the square into three regions of equal area. Find $DM$ and $DN$.',
  'reason': 'Each outer triangle must have one third of the square area; using the side as its height immediately '
            'determines the two boundary lengths.',
  'country': 'Paraguay',
  'source': 'https://www.omapa.org/wp-content/uploads/2015/01/ex-omapa-2010-juv-rf-n3-soluciones.pdf',
  'ident': 'py-omapa-final-level-3-2010-1',
  'solution': 'The square area is $3600$, so each outer triangle has area $1200$. Thus $60\\,AM/2=60\\,CN/2=1200$, '
              'giving $AM=CN=40$. Hence $DM=DN=20$.'},
 {'comp': 'OMAPA Final Level 3',
  'y': 2010,
  'n': 2,
  'topic': 'Combinatorics',
  'tags': ['Counting', 'Sequences & recurrences'],
  'statement': 'A diamond-shaped pattern of unit squares begins at step $0$ with one square. At step $1$ its '
               'horizontal rows have lengths $1,3,1$; at step $2$ they have lengths $1,3,5,3,1$. The pattern continues '
               'by adding a complete layer around the diamond at each step. How many unit squares are present at step '
               '$20$?',
  'reason': 'The successive layers have sizes 4,8,12 and so on, reducing the visual pattern to an arithmetic sum.',
  'country': 'Paraguay',
  'source': 'https://www.omapa.org/wp-content/uploads/2015/01/ex-omapa-2010-juv-rf-n3-soluciones.pdf',
  'ident': 'py-omapa-final-level-3-2010-2',
  'solution': 'The layer added at step $k$ has $4k$ squares. Therefore step $20$ contains '
              '$1+4(1+\\cdots+20)=1+4\\cdot210=841$ squares.'},
 {'comp': 'OMAPA Final Level 3',
  'y': 2010,
  'n': 3,
  'topic': 'Geometry',
  'tags': ['Angle chasing', 'Medians', 'Pythagoras'],
  'statement': 'In triangle $ABC$, $BM$ is a median, $BC=\\frac23MC$, and $\\angle BMC=2\\angle ABM$. Find $AB/AM$.',
  'reason': 'The angle relation makes ABM isosceles. The median then reveals a right triangle, after which the '
            'required ratio is a Pythagorean calculation.',
  'country': 'Paraguay',
  'source': 'https://www.omapa.org/wp-content/uploads/2015/01/ex-omapa-2010-juv-rf-n3-soluciones.pdf',
  'ident': 'py-omapa-final-level-3-2010-3',
  'solution': 'Write $\\theta=\\angle ABM$. Since $\\angle BMA=180^\\circ-2\\theta$, $\\angle BAM=\\theta$, so '
              '$AM=BM$. As $AM=MC$, the points $A,B,C$ lie on a circle with centre $M$ and diameter $AC$, giving '
              '$AB^2+BC^2=AC^2$. With $AM=MC=t$ and $BC=2t/3$, this gives $AB/AM=\\sqrt{4-4/9}=4\\sqrt2/3$.'},
 {'comp': 'OMAPA Final Level 3',
  'y': 2010,
  'n': 4,
  'topic': 'Number Theory',
  'tags': ['Digits & bases', 'Divisibility & GCD', 'Casework'],
  'statement': 'Find all four-digit numbers $\\overline{abcd}$ such that $11\\mid\\overline{abcd}$, '
               '$7\\mid\\overline{ac}$, and $a+b+c+d=d^2$.',
  'reason': 'The digit sum bounds d sharply. Combining the divisibility-by-11 alternating sum with the seven possible '
            'two-digit multiples of seven gives a small, complete case check.',
  'country': 'Paraguay',
  'source': 'https://www.omapa.org/wp-content/uploads/2015/01/ex-omapa-2010-juv-rf-n3-soluciones.pdf',
  'ident': 'py-omapa-final-level-3-2010-4'},
 {'comp': 'OMAPA Final Level 3',
  'y': 2012,
  'n': 1,
  'topic': 'Number Theory',
  'tags': ['Modular arithmetic', 'Sequences & recurrences'],
  'statement': 'An arithmetic progression starts with a one-digit positive integer and increases by $9$ at each step. '
               'One of its terms is $2012$. Determine its first term.',
  'reason': 'The first term is simply the unique one-digit positive representative of 2012 modulo nine.',
  'country': 'Paraguay',
  'source': 'https://www.omapa.org/wp-content/uploads/2015/01/ex-omapa-2012-juv-r5-soluciones.pdf',
  'ident': 'py-omapa-final-level-3-2012-1',
  'solution': 'Every term has the same residue modulo $9$. Since $2012\\equiv5\\pmod9$, the first term is $5$; indeed '
              '$2012=5+223\\cdot9$.'},
 {'comp': 'OMAPA Final Level 3',
  'y': 2012,
  'n': 3,
  'topic': 'Geometry',
  'tags': ['Medians', 'Areas', 'Right triangles'],
  'statement': 'A right triangle $ABC$, right-angled at $B$, is inscribed in a semicircle of diameter $AC=10$. The '
               'median from $B$ is the geometric mean of $AB$ and $BC$. Find the perpendicular distance from $B$ to '
               '$AC$.',
  'reason': 'The hypotenuse median is a radius, so its geometric-mean condition supplies the leg product. Comparing '
            'two area formulas gives the height.',
  'country': 'Paraguay',
  'source': 'https://www.omapa.org/wp-content/uploads/2015/01/ex-omapa-2012-juv-r5-soluciones.pdf',
  'ident': 'py-omapa-final-level-3-2012-3',
  'solution': 'The median to $AC$ has length $5$, so $AB\\cdot BC=25$. If $h$ is the distance to $AC$, area comparison '
              'gives $10h=AB\\cdot BC=25$. Hence $h=5/2$.'},
 {'comp': 'OMAPA Final Level 3',
  'y': 2012,
  'n': 4,
  'topic': 'Number Theory',
  'tags': ['Digits & bases', 'Modular arithmetic', 'Casework'],
  'statement': 'Find the four-digit numbers $\\overline{abcd}$ with four distinct digits such that '
               '$3\\mid\\overline{abcd}$ and $\\overline{ab}-\\overline{cd}=11$, where both displayed two-digit blocks '
               'have two digits.',
  'reason': 'The difference of the two blocks links the tens and units digits. Divisibility by three and the '
            'distinctness condition then reduce the possibilities to a short digit enumeration.',
  'country': 'Paraguay',
  'source': 'https://www.omapa.org/wp-content/uploads/2015/01/ex-omapa-2012-juv-r5-soluciones.pdf',
  'ident': 'py-omapa-final-level-3-2012-4'},
 {'comp': 'SEdeM Juvenile Level II',
  'y': 2024,
  'n': 1,
  'topic': 'Number Theory',
  'tags': ['Modular arithmetic'],
  'statement': 'Prove that among any three consecutive positive integers, one is divisible by $3$.',
  'reason': 'This follows directly from the three possible residues modulo three.',
  'country': 'Ecuador',
  'source': 'https://sedem.org.ec/archivos/pruebas/PruebasOlimpiadas2024.pdf',
  'ident': 'ec-sedem-juvenile-level-ii-2024-1',
  'solution': 'If the first integer has residue $0,1$ or $2$ modulo $3$, then respectively the first, third or second '
              'integer is divisible by $3$.'},
 {'comp': 'SEdeM Juvenile Level II',
  'y': 2024,
  'n': 2,
  'topic': 'Geometry',
  'tags': ['Areas', 'Cosine rule', 'Algebraic identities'],
  'statement': 'Squares constructed on the three sides of a triangular field have areas $505$, $233$ and $52$ '
               'hectares. Find the area of the triangular field.',
  'reason': 'The cosine rule determines the product of two sides times the cosine of their included angle; subtracting '
            'its square from the squared side product gives the area.',
  'country': 'Ecuador',
  'source': 'https://sedem.org.ec/archivos/pruebas/PruebasOlimpiadas2024.pdf',
  'ident': 'ec-sedem-juvenile-level-ii-2024-2',
  'solution': 'Let $a^2=505,b^2=233,c^2=52$ and let $A$ be opposite $a$. Then $bc\\cos A=(233+52-505)/2=-110$. Hence '
              '$(bc\\sin A)^2=233\\cdot52-110^2=16$. The area is $bc\\sin A/2=2$ hectares.'},
 {'comp': 'SEdeM Juvenile Level II',
  'y': 2024,
  'n': 3,
  'topic': 'Algebra',
  'tags': ['Sequences & recurrences', 'Sums of powers'],
  'statement': 'The first ten terms of an arithmetic progression sum to $-1$, while the terms in positions '
               '$2,4,6,8,10$ sum to $9/2$. Find the sum of the squares of the first ten terms.',
  'reason': 'Two linear equations determine the first term and common difference; the final calculation uses the '
            'standard sums of integers and their squares.',
  'country': 'Ecuador',
  'source': 'https://sedem.org.ec/archivos/pruebas/PruebasOlimpiadas2024.pdf',
  'ident': 'ec-sedem-juvenile-level-ii-2024-3',
  'solution': 'Write the terms as $a+kd$, $0\\le k\\le9$. Then $10a+45d=-1$ and $5a+25d=9/2$, so $d=2,a=-91/10$. Thus '
              '$\\sum_{k=0}^9(a+2k)^2=10a^2+180a+1140=3301/10$.'},
 {'comp': 'SEdeM Juvenile Level II',
  'y': 2024,
  'n': 4,
  'topic': 'Geometry',
  'tags': ['Circles & tangency', 'Pythagoras', 'Areas'],
  'statement': 'Two concentric circles have radii $R>r$. A chord of the larger circle, tangent to the smaller circle, '
               'has length $5$ cm. Find the area between the circles.',
  'reason': 'The radius to the point of tangency bisects the chord, giving the difference of the squared radii '
            'directly by Pythagoras.',
  'country': 'Ecuador',
  'source': 'https://sedem.org.ec/archivos/pruebas/PruebasOlimpiadas2024.pdf',
  'ident': 'ec-sedem-juvenile-level-ii-2024-4',
  'solution': 'The right triangle formed by the common centre, chord midpoint and endpoint gives $R^2-r^2=(5/2)^2$. '
              'Hence the annulus has area $\\pi(R^2-r^2)=25\\pi/4$ square centimetres.'},
 {'comp': 'SEdeM Juvenile Level II',
  'y': 2024,
  'n': 5,
  'topic': 'Number Theory',
  'tags': ['Divisibility & GCD', 'Inequalities'],
  'statement': 'Positive integers $a,b$ satisfy $\\frac{a+1}{b}+\\frac{b+1}{a}\\in\\mathbb Z$. Prove that '
               '$\\gcd(a,b)\\le\\sqrt{a+b}$.',
  'reason': 'Multiplying out the integer condition exposes a+b as a multiple of the square of the gcd; positivity '
            'supplies the bound.',
  'country': 'Ecuador',
  'source': 'https://sedem.org.ec/archivos/pruebas/PruebasOlimpiadas2024.pdf',
  'ident': 'ec-sedem-juvenile-level-ii-2024-5',
  'solution': 'Let $d=\\gcd(a,b)$ and let the displayed integer be $K$. Then $a+b=Kab-a^2-b^2$, which is divisible by '
              '$d^2$. Since $a+b>0$, we have $a+b\\ge d^2$.'},
 {'comp': 'SEdeM Juvenile Level III',
  'y': 2024,
  'n': 1,
  'topic': 'Geometry',
  'tags': ['Cyclic quadrilaterals', 'Ptolemy', 'Equilateral triangles'],
  'statement': 'An equilateral triangle $ABC$ is inscribed in a circle. A point $M$ lies on the arc $BC$ not '
               'containing $A$. Prove that $MA=MB+MC$.',
  'reason': 'Recognising the cyclic quadrilateral as a Ptolemy configuration turns the relation into one line after '
            'cancelling equal sides.',
  'country': 'Ecuador',
  'source': 'https://sedem.org.ec/archivos/pruebas/PruebasOlimpiadas2024.pdf',
  'ident': 'ec-sedem-juvenile-level-iii-2024-1',
  'solution': 'Ptolemy applied to the cyclic quadrilateral $ABMC$ gives $AM\\cdot BC=AB\\cdot MC+AC\\cdot MB$. Since '
              '$AB=BC=CA$, division by this common positive length proves the claim.'},
 {'comp': 'SEdeM Juvenile Level III',
  'y': 2024,
  'n': 2,
  'topic': 'Algebra',
  'tags': ['Trigonometry', 'Algebraic identities'],
  'statement': 'Does there exist a real number $x\\in[-\\pi,0]$ satisfying $2-\\cos2x+2\\sqrt2\\cos(x-\\pi/2)=0$?',
  'reason': 'Standard trigonometric identities complete a square in sin x, leaving a familiar exact-angle value.',
  'country': 'Ecuador',
  'source': 'https://sedem.org.ec/archivos/pruebas/PruebasOlimpiadas2024.pdf',
  'ident': 'ec-sedem-juvenile-level-iii-2024-2',
  'solution': 'The left side is $1+2\\sin^2x+2\\sqrt2\\sin x=(\\sqrt2\\sin x+1)^2$. It vanishes when $\\sin '
              'x=-1/\\sqrt2$. Thus such numbers exist: both $x=-\\pi/4$ and $x=-3\\pi/4$ work. The source solution '
              'overlooks the second value; the existence claim is unaffected.'},
 {'comp': 'SEdeM Juvenile Level III',
  'y': 2024,
  'n': 3,
  'topic': 'Algebra',
  'tags': ['Logarithms', 'Inequalities', 'AM–GM'],
  'statement': 'Compare each expression with $2$: (a) $\\frac1{\\log_2\\pi}+\\frac1{\\log_5\\pi}$; (b) '
               '$\\frac1{\\log_2\\pi}+\\frac1{\\log_\\pi2}$.',
  'reason': 'Changing logarithm bases simplifies the first comparison to pi squared versus ten, while the second is '
            'the elementary reciprocal AM–GM inequality.',
  'country': 'Ecuador',
  'source': 'https://sedem.org.ec/archivos/pruebas/PruebasOlimpiadas2024.pdf',
  'ident': 'ec-sedem-juvenile-level-iii-2024-3',
  'solution': '(a) The sum is $\\log_\\pi10>2$, since $\\pi^2<10$ (for example $\\pi<22/7$). (b) Put '
              '$t=\\log_2\\pi>0$. The expression is $t+1/t\\ge2$, with equality only for $t=1$. Since $\\pi\\ne2$, it '
              'is strictly greater than $2$.'},
 {'comp': 'OJM Final Year 3',
  'y': 2023,
  'n': 1,
  'topic': 'Number Theory',
  'tags': ['Diophantine equations', 'Factorisation', 'Casework'],
  'statement': 'Find all integer triples $(x,y,z)$ satisfying $xy+z=2023$ and $x+yz=2021$.',
  'reason': 'Subtracting the equations factors into a product equal to two, so only four signed factor pairs remain to '
            'check.',
  'country': 'Venezuela',
  'source': 'https://acmfiles.s3.amazonaws.com/A%C3%B1o%202023/ojm2023%20problemas%20y%20soluciones.pdf',
  'ident': 've-ojm-final-year-3-2023-1',
  'solution': 'Subtracting gives $(y-1)(x-z)=2$. For $(y-1,x-z)=(1,2)$, the first equation gives $2(z+2)+z=2023$, '
              'hence $(x,y,z)=(675,2,673)$. For $(2,1)$, it gives $3(z+1)+z=2023$, hence $(506,3,505)$. For $(-1,-2)$, '
              '$y=0$ and the original equations give $(2021,0,2023)$. For $(-2,-1)$, $y=-1$ and the first equation '
              'becomes $1=2023$, impossible. These three triples satisfy both equations.'},
 {'comp': 'OJM Final Year 3',
  'y': 2023,
  'n': 2,
  'topic': 'Geometry',
  'tags': ['Right triangles', 'Incircles', 'Areas'],
  'statement': 'Triangle $ABC$ has side lengths $5$, $12$ and $13$ cm. Find the radius of its incircle.',
  'reason': 'Recognising the Pythagorean triple gives the area immediately; dividing by the semiperimeter gives the '
            'inradius.',
  'country': 'Venezuela',
  'source': 'https://acmfiles.s3.amazonaws.com/A%C3%B1o%202023/ojm2023%20problemas%20y%20soluciones.pdf',
  'ident': 've-ojm-final-year-3-2023-2',
  'solution': 'The triangle is right-angled, so its area is $5\\cdot12/2=30$. Its semiperimeter is $15$. Since area '
              'equals inradius times semiperimeter, the radius is $2$ cm.'},
 {'comp': 'OJM Final Years 4–5',
  'y': 2023,
  'n': 1,
  'topic': 'Algebra',
  'tags': ['Exponential equations', 'Quadratic equations'],
  'statement': 'Find all real solutions of $2^x=\\sqrt{9\\cdot2^{x+2}-128}$.',
  'reason': 'The substitution u=2^x turns the equation into a quadratic, followed by a straightforward domain check.',
  'country': 'Venezuela',
  'source': 'https://acmfiles.s3.amazonaws.com/A%C3%B1o%202023/ojm2023%20problemas%20y%20soluciones.pdf',
  'ident': 've-ojm-final-years-4-5-2023-1',
  'solution': 'Square and put $u=2^x>0$. Then $u^2=36u-128$, so $(u-4)(u-32)=0$. Thus $x=2$ or $5$. Both satisfy the '
              'original equation.'},
 {'comp': 'OJM Final Years 4–5',
  'y': 2023,
  'n': 3,
  'topic': 'Geometry',
  'tags': ['Circles & tangency', 'Pythagoras', 'Quadratic equations'],
  'statement': 'A square $ABCD$ has side $2$ cm. Inside it lies a semicircle with diameter $AB$. A circle inside the '
               'square is externally tangent to this semicircle and tangent to sides $BC$ and $CD$. Find its radius.',
  'reason': 'The two tangencies to adjacent sides locate the centre in terms of the radius. One Pythagorean relation '
            'expresses the remaining circle tangency.',
  'country': 'Venezuela',
  'source': 'https://acmfiles.s3.amazonaws.com/A%C3%B1o%202023/ojm2023%20problemas%20y%20soluciones.pdf',
  'ident': 've-ojm-final-years-4-5-2023-3',
  'solution': 'Use $A=(0,0),B=(2,0),C=(2,2),D=(0,2)$. The semicircle centre is $(1,0)$ and the smaller circle centre '
              'is $(2-r,2-r)$. External tangency gives $(1-r)^2+(2-r)^2=(1+r)^2$, or $r^2-8r+4=0$. Only $r=4-2\\sqrt3$ '
              'fits inside the square.'},
 {'comp': 'OLCOMA Final Level III',
  'y': 2017,
  'n': 1,
  'topic': 'Geometry',
  'tags': ['Regular polygons', 'Angle chasing', 'Similarity & congruence'],
  'statement': 'A regular hexagon $ABCDEF$ is inscribed in a circle. Points $N\\in EC$ and $M\\in AC$ satisfy '
               '$AM/AC=CN/CE$. A point $R$ on the circle lies on the ray $DN$ beyond $N$. The arc $EFR$ has measure '
               '$90^\\circ$, and $AC=\\sqrt3$. Determine $AM$.',
  'reason': 'The regular hexagon supplies equal chords and fixed angles. Matching the two side ratios creates '
            'congruent triangles, reducing the length to a standard right-triangle ratio.',
  'country': 'Costa Rica',
  'source': 'https://revistas.tec.ac.cr/index.php/matematica/article/download/4233/3810/11561',
  'ident': 'cr-olcoma-final-level-iii-2017-1',
  'solution': 'Since $AC=CE$, we have $AM=CN$ and $CM=EN$. Also $BC=DE$ and $\\angle BCM=\\angle DEN=30^\\circ$, so '
              'triangles $BCM$ and $DEN$ are congruent. The inscribed angle $\\angle EDR$ subtends arc $EFR$, hence is '
              '$45^\\circ$. Thus $\\angle CBM=45^\\circ$. In triangle $BCM$, the sine rule gives '
              '$CM/BC=\\sin45^\\circ/\\sin105^\\circ=\\sqrt3-1$. Therefore $AM=AC-CM=\\sqrt3BC-(\\sqrt3-1)BC=BC=1$.'},
 {'comp': 'OLCOMA Final Level III',
  'y': 2017,
  'n': 4,
  'topic': 'Algebra',
  'tags': ['Quadratic equations', 'Vieta', 'Discriminants'],
  'statement': 'Find all real $k$ for which $kx^2+k=3x^2+2-2kx$ has two distinct real roots and the sum of its roots '
               'equals their product plus $k$.',
  'reason': 'Vieta converts the root condition into k squared equals two; the discriminant removes the negative '
            'choice.',
  'country': 'Costa Rica',
  'source': 'https://revistas.tec.ac.cr/index.php/matematica/article/download/4233/3810/11561',
  'ident': 'cr-olcoma-final-level-iii-2017-4',
  'solution': 'The quadratic is $(k-3)x^2+2kx+k-2=0$. With $k\\ne3$, Vieta gives $-2k/(k-3)=(k-2)/(k-3)+k$, hence '
              '$k^2=2$. Its discriminant is $20k-24$, which must be positive. Thus only $k=\\sqrt2$ works.'},
 {'comp': 'Cuban National Olympiad – Pre-university common day 1',
  'y': 2023,
  'n': 1,
  'topic': 'Algebra',
  'tags': ['Polynomials', 'Repeated roots', 'Discriminants'],
  'statement': 'Find all real numbers $a$ for which the polynomial $x^3+ax-2(a+4)$ has exactly two distinct real '
               'roots.',
  'reason': 'A fixed root factors out at once. Exactly two real roots then requires either a repeated quadratic root '
            'or a quadratic root shared with the fixed linear factor.',
  'country': 'Cuba',
  'source': 'https://es.scribd.com/document/880296012/Olimpiadas-Cuba-libro-de-olimpiadas-que-tienen-texto-y-graficos',
  'ident': 'cu-cuban-national-olympiad-pre-university-common-day-1-2023-1',
  'solution': 'Factor as $(x-2)(x^2+2x+a+4)$. If the quadratic has a repeated root, its discriminant $-4(a+3)$ '
              'vanishes, so $a=-3$; its root $-1$ differs from $2$. Otherwise it must have two distinct real roots, '
              'one of which is $2$. Substitution gives $a=-12$, with quadratic roots $2,-4$. Thus '
              '$a\\in\\{-3,-12\\}$.'},
 {'comp': 'Colombian Mathematical Olympiad, Superior Selection Round',
  'y': 2017,
  'n': 1,
  'topic': 'Geometry',
  'tags': ['Circle sectors', 'Equilateral triangles', 'Areas'],
  'statement': 'A circle with centre $O$ has diameters $AB$ and $CX$, with $OB=BC$. Its area is $315\\text{ cm}^2$. '
               'Find the combined area of the two opposite minor sectors $BOC$ and $AOX$.',
  'reason': 'The equal chord and radius form an equilateral triangle, fixing each central angle and hence the fraction '
            'of the circle shaded.',
  'country': 'Colombia',
  'source': 'https://oc.uan.edu.co/images/Olimpiadas/Matematicas/documentos/2020/nspSel.pdf',
  'ident': 'co-colombian-mathematical-olympiad-superior-selection-round-2017-1',
  'solution': 'Since $OB=OC=BC$, triangle $OBC$ is equilateral and $\\angle BOC=60^\\circ$. The opposite angle $AOX$ '
              'is also $60^\\circ$. The two sectors therefore occupy $120/360=1/3$ of the circle, giving $105\\text{ '
              'cm}^2$.'},
 {'comp': 'Colombian Mathematical Olympiad, Superior Selection Round',
  'y': 2017,
  'n': 2,
  'topic': 'Algebra',
  'tags': ['Ratios & proportions'],
  'statement': 'A model railway uses scale $1:87$. A model of Benjamin’s brother is $2$ cm tall. What is his actual '
               'height, in centimetres?',
  'reason': 'This is direct multiplication by the scale factor.',
  'country': 'Colombia',
  'source': 'https://oc.uan.edu.co/images/Olimpiadas/Matematicas/documentos/2020/nspSel.pdf',
  'ident': 'co-colombian-mathematical-olympiad-superior-selection-round-2017-2',
  'solution': 'The actual height is $2\\cdot87=174$ cm.'},
 {'comp': 'Colombian Mathematical Olympiad, Superior Selection Round',
  'y': 2017,
  'n': 3,
  'topic': 'Algebra',
  'tags': ['Sequences & recurrences', 'Periodicity'],
  'statement': 'Let $a_1=217$ and $a_{n+1}=(a_n-1)/a_n$. Find $a_{2017}$.',
  'reason': 'Computing three iterates reveals an exact period-three cycle; the large index is then reduced modulo '
            'three.',
  'country': 'Colombia',
  'source': 'https://oc.uan.edu.co/images/Olimpiadas/Matematicas/documentos/2020/nspSel.pdf',
  'ident': 'co-colombian-mathematical-olympiad-superior-selection-round-2017-3',
  'solution': 'For $f(x)=(x-1)/x$, $f^2(x)=1/(1-x)$ and $f^3(x)=x$. The orbit of $217$ is well-defined and repeats '
              'every three terms. Since $2017\\equiv1\\pmod3$, $a_{2017}=217$.'},
 {'comp': 'Colombian Mathematical Olympiad, Superior Selection Round',
  'y': 2017,
  'n': 4,
  'topic': 'Number Theory',
  'tags': ['Digits & bases', 'Powers', 'Counting'],
  'statement': 'How many three-digit positive integers $\\overline{ABC}$ have the property that $(A+B)^C$ is a '
               'three-digit integral power of $2$?',
  'reason': 'The base must be a power of two, and the exponent must yield 128,256 or512. Counting digit pairs for the '
            'resulting few bases completes the problem.',
  'country': 'Colombia',
  'source': 'https://oc.uan.edu.co/images/Olimpiadas/Matematicas/documentos/2020/nspSel.pdf',
  'ident': 'co-colombian-mathematical-olympiad-superior-selection-round-2017-4',
  'solution': 'The three-digit powers of two are $128,256,512$. Therefore $A+B$ must be one of $2,4,8,16$. For '
              '$A+B=2$, the exponents $C=7,8,9$ each allow two digit pairs, giving $6$ numbers. For $A+B=4$, only '
              '$C=4$ works, with four pairs. For $A+B=8$, only $C=3$ works, with eight pairs. For $A+B=16$, only $C=2$ '
              'works, with three pairs. Thus the total is $6+4+8+3=21$.'},
 {'comp': 'Colombian Mathematical Olympiad, Superior Selection Round',
  'y': 2017,
  'n': 5,
  'topic': 'Geometry',
  'tags': ['Solid geometry', 'Similarity & congruence', 'Volumes'],
  'statement': 'A regular tetrahedron has volume $724\\text{ cm}^3$. At each vertex, cut it by the plane through the '
               'midpoints of the three edges from that vertex, and remove the corner tetrahedron. What volume remains?',
  'reason': 'Each removed corner is a half-scale copy, so its volume is one eighth of the original.',
  'country': 'Colombia',
  'source': 'https://oc.uan.edu.co/images/Olimpiadas/Matematicas/documentos/2020/nspSel.pdf',
  'ident': 'co-colombian-mathematical-olympiad-superior-selection-round-2017-5',
  'solution': 'Four corners are removed, each with volume $724/8$. Thus the remaining volume is $724(1-4/8)=362\\text{ '
              'cm}^3$.'},
 {'comp': 'Colombian Mathematical Olympiad, Superior Selection Round',
  'y': 2017,
  'n': 6,
  'topic': 'Geometry',
  'tags': ['Pythagoras', 'Areas', 'Algebraic identities'],
  'statement': 'A right triangle has perimeter $180$, and the sum of the squares of its three side lengths is $12800$. '
               'Find its area.',
  'reason': 'Pythagoras determines the hypotenuse from the sum of squares, after which the leg sum determines their '
            'product.',
  'country': 'Colombia',
  'source': 'https://oc.uan.edu.co/images/Olimpiadas/Matematicas/documentos/2020/nspSel.pdf',
  'ident': 'co-colombian-mathematical-olympiad-superior-selection-round-2017-6',
  'solution': 'If the legs are $a,b$ and hypotenuse $c$, then $2c^2=12800$, so $c=80$ and $a+b=100$. Hence '
              '$2ab=(a+b)^2-(a^2+b^2)=10000-6400=3600$. The area is $ab/2=900$.'},
 {'comp': 'Colombian Mathematical Olympiad, Superior Selection Round',
  'y': 2017,
  'n': 7,
  'topic': 'Algebra',
  'tags': ['Absolute values', 'Systems of equations', 'Casework'],
  'statement': 'Real numbers $x,y$ satisfy $|x|+x+y=5$ and $x+|y|-y=10$. Find $x+y$.',
  'reason': 'The absolute values require a small sign split; the viable branch reduces to two linear equations.',
  'country': 'Colombia',
  'source': 'https://oc.uan.edu.co/images/Olimpiadas/Matematicas/documentos/2020/nspSel.pdf',
  'ident': 'co-colombian-mathematical-olympiad-superior-selection-round-2017-7',
  'solution': 'If $x<0$, the first equation gives $y=5$, contradicting the second. Thus $x\\ge0$. If $y\\ge0$, the '
              'second gives $x=10$, contradicting $2x+y=5$. Hence $y<0$ and $2x+y=5$, $x-2y=10$. These give '
              '$x=4,y=-3$, so $x+y=1$.'},
 {'comp': 'Colombian Mathematical Olympiad, Superior Selection Round',
  'y': 2017,
  'n': 8,
  'topic': 'Combinatorics',
  'tags': ['Logic', 'Casework'],
  'statement': 'After Thomas tells his first lie, he repeats the pattern: two true statements, then one lie. Before '
               'that first lie he may tell zero, one or two truths. About a two-digit number he says, in order: “One '
               'digit is 2”; “It is greater than 50”; “It is even”; “It is less than 30”; “It is divisible by 3”; “One '
               'digit is 7”. Find the sum of its digits.',
  'reason': 'There are only three phases for the truth pattern. Comparing paired size and digit statements quickly '
            'eliminates two phases.',
  'country': 'Colombia',
  'source': 'https://oc.uan.edu.co/images/Olimpiadas/Matematicas/documentos/2020/nspSel.pdf',
  'ident': 'co-colombian-mathematical-olympiad-superior-selection-round-2017-8',
  'solution': 'The three patterns are FTTFTT, TFTTFT and TTFTTF. The second requires a number below 30 that is even '
              'and has digits 2 and 7, impossible. The third requires both greater than 50 and less than 30. In the '
              'first, the number is above 50, even, divisible by 3, has digit 7 and has no digit 2. It must be $78$, '
              'so the digit sum is $15$.'},
 {'comp': 'Colombian Mathematical Olympiad, Superior Selection Round',
  'y': 2017,
  'n': 9,
  'topic': 'Geometry',
  'tags': ['Circles & tangency', 'Pythagoras', 'Areas'],
  'statement': 'Three circles with centres $A,B,C$ and radii $30,20,10$ are externally tangent in pairs. Find the area '
               'of triangle $ABC$.',
  'reason': 'The sides are sums of radii, giving the familiar 30–40–50 right triangle.',
  'country': 'Colombia',
  'source': 'https://oc.uan.edu.co/images/Olimpiadas/Matematicas/documentos/2020/nspSel.pdf',
  'ident': 'co-colombian-mathematical-olympiad-superior-selection-round-2017-9',
  'solution': 'The side lengths are $50,40,30$. Since $30^2+40^2=50^2$, the area is $30\\cdot40/2=600$.'},
 {'comp': 'Colombian Mathematical Olympiad, Superior Selection Round',
  'y': 2017,
  'n': 11,
  'topic': 'Combinatorics',
  'tags': ['Parity', 'Extremal arguments', 'Grids'],
  'statement': 'Integers are written in the nine cells of a $3\\times3$ grid. Entries in cells sharing a side differ '
               'by $1$, and the sum of all nine entries is $500$. Find the central entry.',
  'reason': 'Distance bounds from the centre restrict the possible values to a narrow interval, and the checkerboard '
            'parity pattern selects the unique even value.',
  'country': 'Colombia',
  'source': 'https://oc.uan.edu.co/images/Olimpiadas/Matematicas/documentos/2020/nspSel.pdf',
  'ident': 'co-colombian-mathematical-olympiad-superior-selection-round-2017-11',
  'solution': 'If the centre is $c$, the four side-neighbours differ from it by at most 1 and the four corners by at '
              'most 2. Thus $|500-9c|\\le12$, giving $c\\in\\{55,56\\}$. The five cells of the centre’s checkerboard '
              'colour have its parity and the other four the opposite parity, so the total has parity $c$. Since $500$ '
              'is even, $c=56$.'},
 {'comp': 'Uruguayan National Mathematical Olympiad Final Level V',
  'y': 2017,
  'n': 1,
  'topic': 'Algebra',
  'tags': ['Logarithms', 'Products'],
  'statement': 'Evaluate $\\displaystyle\\sum_{k=2}^{2017}\\frac1{\\log_k(2017!)}$.',
  'reason': 'Change of base turns the reciprocal logarithms into the logarithm of the factorial product.',
  'country': 'Uruguay',
  'source': 'https://drive.google.com/file/d/1rWAk6EkR96oxj-XoQDycsXRJY1j9W8kW/view',
  'ident': 'uy-uruguayan-national-mathematical-olympiad-final-level-v-2017-1',
  'solution': 'Each summand equals $\\log_{2017!}k$. Their sum is $\\log_{2017!}(2\\cdot3\\cdots2017)=1$.'},
 {'comp': 'Uruguayan National Mathematical Olympiad Final Level IV',
  'y': 2017,
  'n': 1,
  'topic': 'Geometry',
  'tags': ['Circles & chords', 'Pythagoras', 'Perpendicularity'],
  'statement': 'Points $A,B$ satisfy $AB=5$. Circles centred at $A,B$ with radii $3,4$ intersect at $O$. A circle '
               'centred at $O$ meets the first circle at $P_1,P_2$ and the second at $Q_1,Q_2$. Prove that '
               '$P_1P_2\\perp Q_1Q_2$.',
  'reason': 'Pythagoras makes the two lines of centres perpendicular, while each common chord is perpendicular to its '
            'own line of centres.',
  'country': 'Uruguay',
  'source': 'https://drive.google.com/file/d/113mP5KbUDldF0i7Ef1MfV_O7t3f9wMnp/view',
  'ident': 'uy-uruguayan-national-mathematical-olympiad-final-level-iv-2017-1',
  'solution': 'We have $AO=3,BO=4,AB=5$, so $AO\\perp BO$. The common chord $P_1P_2$ is perpendicular to $AO$, and '
              '$Q_1Q_2$ to $BO$. Therefore those chords are perpendicular to one another.'},
 {'comp': 'Uruguayan National Mathematical Olympiad Final Level IV',
  'y': 2017,
  'n': 2,
  'topic': 'Number Theory',
  'tags': ['Divisibility & GCD', 'Modular arithmetic', 'Counting'],
  'statement': 'How many positive integers $n\\le2017$ make the fraction $(2n+3)/(n+7)$ reducible?',
  'reason': 'Subtracting twice the denominator reduces the gcd to a fixed prime, leaving an arithmetic-progression '
            'count.',
  'country': 'Uruguay',
  'source': 'https://drive.google.com/file/d/113mP5KbUDldF0i7Ef1MfV_O7t3f9wMnp/view',
  'ident': 'uy-uruguayan-national-mathematical-olympiad-final-level-iv-2017-2',
  'solution': '$\\gcd(2n+3,n+7)=\\gcd(11,n+7)$, so reduction is possible exactly when $n\\equiv4\\pmod{11}$. The '
              'values $4,15,\\ldots,2017$ number $(2017-4)/11+1=184$.'},
 {'comp': 'ONM Final — Senior',
  'y': 2021,
  'n': 1,
  'topic': 'Number Theory',
  'tags': ['Modular arithmetic', 'Sequences & recurrences', 'Powers'],
  'statement': 'Let $a_1=7$ and $a_n=7^{a_{n-1}}$ for $n\\ge2$. Find the final decimal digit of $a_{2021}$.',
  'reason': 'The last digit of a power of seven has period four; only the preceding exponent modulo four is needed.',
  'country': 'Chile',
  'source': 'https://www.olimpiadadematematica.cl/index.php/pruebas-movil/category/17-pruebas-2021?download=47%3Afinal-2021-mayor',
  'ident': 'cl-onm-final-senior-2021-1',
  'solution': 'Every $a_n$ is odd and $a_n\\equiv3\\pmod4$, since an odd power of $7\\equiv-1\\pmod4$ is $-1$. Thus '
              'for $n\\ge2$, $a_n\\equiv7^3\\equiv3\\pmod{10}$. The requested last digit is $3$.'},
 {'comp': 'ONM Final — Junior',
  'y': 2021,
  'n': 1,
  'topic': 'Algebra',
  'tags': ['Inequalities', 'AM–GM', 'Products'],
  'statement': 'Which is larger: $99!$ or $50^{99}$? Prove your answer.',
  'reason': 'Pairing factors equidistant from 50 bounds each product by 50 squared.',
  'country': 'Chile',
  'source': 'https://www.olimpiadadematematica.cl/index.php/pruebas-movil/category/17-pruebas-2021?download=48%3Afinal-2021-menor',
  'ident': 'cl-onm-final-junior-2021-1',
  'solution': 'Pair $k$ with $100-k$ for $1\\le k\\le49$, leaving $50$. Since $k(100-k)=2500-(50-k)^2<2500$, we get '
              '$99!<50\\cdot2500^{49}=50^{99}$.'},
 {'comp': 'ONM Final — Junior',
  'y': 2021,
  'n': 2,
  'topic': 'Algebra',
  'tags': ['Algebraic identities', 'Integer constraints', 'Quadratic equations'],
  'statement': 'Positive reals $x>y$ satisfy $x^2+y^2=axy$, where $a>2$ is real. Find all possible $a$ for which '
               '$(x+y)/(x-y)$ is an integer.',
  'reason': 'Squaring the ratio expresses it directly in terms of a; imposing an integer value parametrizes every '
            'admissible case.',
  'country': 'Chile',
  'source': 'https://www.olimpiadadematematica.cl/index.php/pruebas-movil/category/17-pruebas-2021?download=48%3Afinal-2021-menor',
  'ident': 'cl-onm-final-junior-2021-2',
  'solution': 'Put $m=(x+y)/(x-y)>1$. Then $m^2=(a+2)/(a-2)$, so $a=2(m^2+1)/(m^2-1)$ for an integer $m\\ge2$. '
              'Conversely, for any such $m$, take $x=m+1,y=m-1$; these positive numbers realize precisely that $a$ and '
              'ratio $m$.'},
 {'comp': 'ONEM National Final Level 3',
  'y': 2024,
  'n': 1,
  'topic': 'Algebra',
  'tags': ['Inequalities', 'Series bounds', 'Geometric series'],
  'statement': 'Let $x=1+\\frac1{2^2}+\\frac1{3^3}+\\cdots+\\frac1{2024^{2024}}$. Find the integer $n$ such that '
               '$n\\le3x<n+1$.',
  'reason': 'A simple geometric comparison bounds the tail sharply enough to place the scaled sum between consecutive '
            'integers.',
  'country': 'Peru',
  'source': 'https://www.scribd.com/document/818167155/2024f4n3',
  'ident': 'pe-onem-national-final-level-3-2024-1',
  'solution': 'Clearly $x>1$. For $k\\ge3$, $k^k\\ge3^k$, with strict inequality for $k>3$, so '
              '$x<1+1/4+\\sum_{k=3}^{\\infty}3^{-k}=1+1/4+1/18=47/36<4/3$. Thus $3<3x<4$, giving $n=3$.'}]
path=P/'restoration-records.json'
old=json.loads(path.read_text());ids={x['ident'] for x in records}
old=[x for x in old if x.get('ident') not in ids]+records
path.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
print('Latin explicit records',len(records))
