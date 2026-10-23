import json,re
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text())
rows=[
('5136f9',1.5,'Number Theory',['Digits'],'Subtracting the reversed three-digit numbers forces the units digit to exceed the hundreds digit by six; the digit sum leaves 137 and 218.'),
('eb7aa0',2.5,'Algebra',['Algebraic identities'],'The two symmetric identities give a+b=5 and ab=5, so the reciprocal sum is one.'),
('77cb82',2,'Geometry',['Angle chasing','Isosceles triangles'],'The first 20–20–140 triangle makes DC=DA=DB, leaving a second isosceles triangle with base angles 70 degrees.'),
('419582',2,'Combinatorics',['Counting','Rotation'],'The centre is fixed and the other cells form six rotation orbits, yielding 2^7 colourings.'),
('ad88ff',2.5,'Number Theory',['Diophantine equations','Factorisation'],'Completing the product gives (m+2)(n+5)=131; the four signed factor pairs give all integer solutions.'),
('8a4c00',3.5,'Combinatorics',['Colouring','Extremal arguments'],'The divisibility chain 2,4,8,16,32 forces five colours; grouping numbers between consecutive powers of two attains five.'),
('4df0ce',2,'Algebra',['Complex numbers','Equations'],'The right side is real, forcing z real or purely imaginary; the imaginary case is impossible and the real case gives the cube root of two.'),
('d91c48',2,'Number Theory',['Primes','Integer roots'],'Vieta and prime q force integer roots −1 and −q, so consecutive primes p=q+1 must be 3 and 2. The raw solution wrongly allows negative primes.'),
('ccede5',2,'Algebra',['Equations'],'Substituting xy=−6−y² reduces to (y²−9)(y²+15)=0 and gives the two ordered solutions.'),
('418450',3.5,'Combinatorics',['Counting','Permutations'],'Classifying by the longest black run, while identifying reflections as well as rotations, gives 1+2+4+1=8 bracelets.'),
('957c0e',3.5,'Geometry',['Circles','Optimisation','Pythagoras'],'Move the circle against the two walls opposite the bath, then tangency to the bath corner gives (4−r)²+(4.5−r)²=r² and r=2.5.'),
('8ed713',4,'Combinatorics',['Graph theory','Extremal arguments'],'Choose a vertex of maximum outdegree; any vertex not reachable in two steps would beat it and all its out-neighbours, contradicting maximality.'),
('81d8f2',1.5,'Algebra',['Trigonometry'],'Reduce tangent angles modulo 180 degrees and apply the tangent addition formula for 12+48=60 degrees.'),
('10b55a',1.5,'Geometry',['Solid geometry','Pythagoras'],'The face altitude is sqrt(8²+6²)=10, so the base and four triangular faces have total area 384.'),
('d208b1',2.5,'Algebra',['Logarithms','Equations'],'Using the common logarithm value makes (4/3)^t=(4/3)^(3/2), then a³=75.'),
('c6226b',3,'Number Theory',['Valuations','Extremal arguments'],'Any 803 chosen integers contain three multiples of five and an even integer; all 800 nonmultiples of five together with 5 and 10 attain 802.'),
('de858e',4.5,'Geometry',['Angle bisectors','Similarity','Sine rule'],'An auxiliary angle bisector gives b²=ac+c², while the given bisector gives c²=ab−bc; adding forces a=b and angles 72,72,36 degrees.'),
('464abc',3.5,'Combinatorics',['Double counting','Extremal arguments','Construction'],'The six distinct line totals sum to twice the coin count and at least fifteen; a matrix with row totals 0,2,6 and column totals 1,3,4 attains eight coins.'),
('ac44fe',1.5,'Algebra',['Sequences','Algebraic identities'],'The product of terms adjacent to the third is a_3²−d², so a_3=0 and the requested product vanishes.'),
('66f996',3,'Algebra',['Binomial coefficients','Equations'],'Ratios of consecutive binomial coefficients give two linear equations in n and the middle index, yielding n=62.'),
('6fa81f',2.5,'Number Theory',['Modular arithmetic','Digits'],'Since 10≡3 modulo seven, the repeated-twos geometric sum is congruent to 3^n−1.'),
('89249b',4,'Algebra',['Complex numbers','Trigonometry','Counting'],'For nonzero z, polar form forces angle kπ/2019; a sign check of (−1)^k cos(kπ/2019) leaves 2018 positive radial solutions, plus zero.'),
('d1cd2d',2.5,'Combinatorics',['Probability','Geometric counting'],'By quadrant symmetry the probability is the area remaining after three small triangles are removed from a 2-by-2 square, namely 5/8.'),
('937ea7',4,'Geometry',['Coordinates','Parabola','Locus'],'Parameterize B and C by their y-coordinates; perpendicular chords yield a quadratic in the coordinate of C whose discriminant is b(b−4), giving b≤0 or b≥4.'),
('154e8a',4,'Combinatorics',['Combinatorial geometry','Extremal arguments','Construction'],'The upward unit triangles have disjoint edge sets and force at least n(n+1)/2 uncoloured edges; colouring two directions reaches n(n+1).'),
('ce41d3',1.5,'Geometry',['Area','Similarity'],'Similar triangular areas scale as squared quarter-lengths; the middle strip is 5/16 of the whole and has area five.'),
('490db9',1.5,'Algebra',['Inequalities'],'The identity x+y=1 places both variables in (0,1), so each sum of higher powers is below one and their product cannot equal two.'),
('3d8657',3.5,'Geometry',['Area','Trigonometry','Perimeter'],'Projection gives BN=BC/2 and MN equal to the altitude; these two identities make both the areas and perimeters equal.'),
('897179',4,'Combinatorics',['Games','Induction'],'The losing positions are exactly 2^k−1; taking eleven pebbles leaves 31, and every reply can be answered by reaching the next smaller losing position.'),
('98444d',3,'Algebra',['Vieta','Equations'],'Vieta turns the squared-root sum into p^4+7p²−44=0; positivity of both roots selects p=2 from ±2.'),
('c2e772',2.5,'Number Theory',['Valuations','Diophantine equations'],'The product a²(a²−3)=2^n forces a to be a power of two; its odd factor must be one, leaving a=2,n=2.'),
('5e7940',3.5,'Algebra',['Inequalities','Factorisation'],'After clearing positive denominators, the difference factors as (a−b)²(1−ab); the sum bound ensures ab≤1.'),
('fa98b1',2.5,'Geometry',['Circles','Tangency','Pythagoras'],'The tangent right triangle fixes the projection of T onto AB; a second Pythagorean calculation gives PT=1/sqrt(3).'),
('e8ab45',4,'Combinatorics',['Extremal arguments','Construction','Chessboard'],'Six nonattacking rooks leave only four cells for kings; an explicit arrangement of five rooks and five kings reaches the upper bound ten.'),
('550cc5',2,'Algebra',['Trigonometry','Equality cases'],'The three cosine terms attain their individual upper bounds; x and y are integer multiples of π with the same parity.'),
('1f7461',2.5,'Number Theory',['Factorisation','Primes'],'The coprime factors 3^m−1 and 3^m+2 multiply to 2p^n; the even factor is two, forcing m=n=1 and p=5.'),
('de2db3',4,'Geometry',['Cyclic quadrilaterals','Sine rule','Cosine rule'],'The equal pedal chords give 56sin A=40sin B=35sin C; sine-rule ratios followed by the cosine rule give angle B=60 degrees.'),
('0b9dc1',5,'Combinatorics',['Counting','Sets','Permutations'],'The smaller members of the pairs must sum to 24, leaving exactly three possible sets; counting admissible matchings gives 360+384+360=1104.'),
('6f4303',3,'Number Theory',['Factorials','Integer bounds'],'Completing the square gives (a+b)²=b²+131−b!; factorial growth excludes b≥6 and the six remaining cases leave (1,5).'),
('aabd8b',3,'Geometry',['Area','Geometric series'],'Successive semicircle radii have ratio 1/sqrt(2); summing alternating area differences as a geometric series gives π/3.'),
('5cd593',2.5,'Combinatorics',['Counting','Inclusion-exclusion','Permutations'],'Start with n! rook permutations and exclude the two forbidden corners by inclusion–exclusion, giving n!−2(n−1)!+(n−2)!.'),
('7d3d78',4,'Algebra',['Cyclic system','Extremal arguments','Inequalities'],'The equations force positivity and xyz=1; after choosing x maximal, y,z≤1 and x+1/x=z³+z forces equality throughout, so all variables are one.'),
('58a6f2',5,'Combinatorics',['Double counting','Extremal arguments','Construction'],'Counting cross-gender games yields (b−21)(g−12)≥252 and b+g≥65; a cyclic five-group construction realizes 35 boys and 30 girls.')]
statements={
'8ed713':r'For every pair of distinct cities, exactly one of the two directed flights between them exists. Prove that some city can reach every other city using at most two flights.',
'de858e':r'In triangle $ABC$, $\angle B=2\angle C$. Its internal angle bisector from $A$ meets $BC$ at $D$, and $AB=CD$. Determine $\angle A$.',
'89249b':r'How many complex numbers satisfy $z^{2019}=z+\overline z$?',
'937ea7':r'Fix $A=(0,2)$ on the parabola $y^2=x+4$. Determine all other points $B$ of this parabola for which a point $C$ on it makes $\angle ACB=90^\circ$.',
'154e8a':r'An equilateral triangle of side $n$ is subdivided by parallels to its sides into $n^2$ unit equilateral triangles. What is the largest number of unit grid edges that can be coloured red without three red edges forming an equilateral triangle?',
'897179':r'Two players alternately remove between one and half of the stones currently on a table, initially containing $42$ stones. The player who leaves exactly one stone wins. Determine which player has a winning strategy and prove it.',
'e8ab45':r'Place equally many rooks and kings on an $8\times8$ chessboard, with no piece attacking another. Rooks attack along rows and columns, and kings attack adjacent cells. Find the greatest possible total number of pieces.',
'de2db3':r'An interior point $T$ of triangle $ABC$ satisfies $AT=56$, $BT=40$ and $CT=35$. Its perpendicular feet on the three sides form an equilateral triangle. Determine $\angle ABC$.',
'0b9dc1':r'Count the partitions of $\{1,2,\ldots,12\}$ into six unordered pairs for which the sum of the absolute differences within the pairs is $30$.',
'7d3d78':r'Determine all real triples $(x,y,z)$ satisfying $$(x^2+1)y=z^2+1,\qquad(y^2+1)z=x^2+1,\qquad(z^2+1)x=y^2+1.$$',
'58a6f2':r'Boys and girls enter a chess tournament in which every pair plays once and no game is drawn. Every girl defeats at least $21$ boys and every boy defeats at least $12$ girls. Determine the smallest possible number of participants.'}
subs={'8ed713':['Graph theory','Extremal arguments'],'de858e':['Triangle geometry','Similarity & congruence','Trigonometry'],'89249b':['Complex numbers','Trigonometry'],'937ea7':['Coordinates & vectors','Constructions & loci','Projective geometry & conics'],'154e8a':['Combinatorial geometry','Extremal arguments'],'897179':['Games & strategies','Induction'],'e8ab45':['Extremal arguments','Algorithms & constructions'],'de2db3':['Angles & cyclic quadrilaterals','Trigonometry'],'0b9dc1':['Counting','Sets & partitions','Permutations & arrangements'],'7d3d78':['Equations & systems','Inequalities'],'58a6f2':['Double counting','Extremal arguments','Algorithms & constructions']}
archive='https://www.azoo.hr/natjecanja-i-smotre-arhiva/testovi-i-rjesenja-sa-skolske-zupanijske-i-drzavne-razine-natjecanja-iz-matematike-2019/'
for short,v,t,tags,why in rows:
 slug='hrv_2019_'+short;d=json.loads((p/(slug+'.json')).read_text());g,num=d['problem_number'].split('.')
 school='City' in d['section'];u='https://www.azoo.hr/app/uploads/uvezeno/datoteke/TESTOVI/'+('mat_skolsko.zip' if school else 'mat-zupanijsko.zip')
 filename='skolsko_rje_A varijanta.pdf' if school else 'zupanijsko_rje.pdf'
 x={'difficulty':v,'topic':t,'tags':tags,'reason':why,'competition':'Croatian Mathematical Competition','number':num,'section':('School/City Round' if school else 'County Round')+f' — Year {g}, Variant A','sourceUrl':archive,'solutionUrl':u,'sourceName':'Croatian Education and Teacher Training Agency — official 2019 papers and solutions','license':'Original contest rights retained; concise English paraphrase.','notes':f'Checked official {filename}, problem A-{g}.{num}.'}
 borrowed=re.search(r'\((United Kingdom \d{4}|Ukraine \d{4}|Japan \d{4}|Estonia \d{4})\)',d['problem_markdown'])
 if borrowed:x['notes']+=' The compilation also attributes this problem to '+borrowed[1]+'; this record is the verified Croatian appearance.'
 if short in statements:
  x['statement']=statements[short];x['subtopics']=subs[short];x['solution']=f'[Official worked solution: {filename}, problem A-{g}.{num}]({u}).';x['solutionKind']='source-link'
 r[slug]=x
# Restore five omitted problems to complete each exact official paper.
missing=[
('school1_7',1,7,4.5,'Geometry',['Similarity','Rectangles','Pythagoras'],r'In a unit square $ABCD$, with vertices in cyclic order, points $E\in BC$ and $F\in AD$ make $ABEF$ a rectangle. A congruent rectangle $KLMN$ has $K\in EF$, $L\in EC$, $M\in CD$ and $N\in FD$. Determine $BE$.','Congruent right triangles first force L to be the midpoint of BC; the unit side LM then makes a 30–60–90 triangle and gives BE=2−sqrt(3).',['Similarity & congruence','Quadrilaterals & polygons','Triangle geometry']),
('school2_3',2,3,2,'Geometry',['Cyclic quadrilaterals'],r'Five points A,B,C,D,E occur in this order on a circle, with AC and BE diameters. Given angle DAC=37 degrees and EBD=28 degrees, determine ACE.','The equal chord angles and the right angle on diameter AC give 90−37−28=25 degrees.',None),
('school3_3',3,3,2,'Number Theory',['Digits','Modular arithmetic'],r'Determine the final 2019 decimal digits of $2^{2019}5^{2018}9^{2017}$.','The factorization 2·9^2017·10^2018 gives 2018 terminal zeros preceded by eight.',None),
('county1_3',1,3,3.5,'Number Theory',['Divisibility','Parity'],r'Let a be the smallest divisor greater than one of a positive integer n>2. Find all n for which n=a³+d³ for some positive divisor d of n.','Odd n is impossible by parity, so a=2; then d divides eight, giving n=16,72,520.',None),
('county3_2',3,2,4.5,'Geometry',['Solid geometry','Tangency','Plane sections'],r'Four spheres of radius $R$ rest on the base of a right circular cone. Each touches the cone and two neighbouring spheres. A fifth sphere of the same radius lies above them and touches all four and the cone. Determine the volume of the cone.','The five centres form a square pyramid with all edges 2R; its diagonal section makes the cone apex angle 90 degrees and the height (1+2sqrt(2))R.',['Solid geometry','Circles & tangency','Triangle geometry'])]
for key,g,num,v,t,tags,statement,why,sub in missing:
 slug='hrv_2019_'+key;school=key.startswith('school');sec=('School/City Round' if school else 'County Round')+f' — Year {g}, Variant A';u='https://www.azoo.hr/app/uploads/uvezeno/datoteke/TESTOVI/'+('mat_skolsko.zip' if school else 'mat-zupanijsko.zip');fn='skolsko_rje_A varijanta.pdf' if school else 'zupanijsko_rje.pdf'
 (p/(slug+'.json')).write_text(json.dumps({'country':'Croatia','competition':'Croatian Mathematical Competition','year':2019,'section':sec,'problem_number':str(num),'problem_markdown':statement,'solutions_markdown':[]},ensure_ascii=False,indent=2))
 x={'difficulty':v,'topic':t,'tags':tags,'reason':why,'sourceUrl':archive,'solutionUrl':u,'sourceName':'Croatian Education and Teacher Training Agency — official 2019 papers and solutions','license':'Original contest rights retained; concise English paraphrase.','statement':statement,'solution':f'[Official worked solution: {fn}, problem A-{g}.{num}]({u}).','solutionKind':'source-link','notes':f'Restored omitted official problem A-{g}.{num} and checked the original worked solution.'}
 if sub:x['subtopics']=sub
 r[slug]=x
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
