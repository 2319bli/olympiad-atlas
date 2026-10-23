import json,re
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text())
rows=[
# National final: missing grades 5, 6, 11 and 12.
('4efe32',5,'F',1.5,'Number Theory',['Squares','Divisibility'],'Count 45 positive squares and 45 multiples of 45 with three in their intersection; the original part (c) includes zero, so its answer is 1939.'),
('c3d5be',5,'F',3,'Number Theory',['Integer bounds','Equations'],'The weighted total 6a+7b+8c+d=72 bounds the first three increasing entries successively to 2,3,4, leaving d=7.'),
('04865f',5,'F',3.5,'Number Theory',['Primes','Modular arithmetic'],'Parity forces a prime 2, reduction of the remaining square sum modulo 3 forces a prime 3, and a short bounded prime check gives (2,43,3,41).'),
('ba6c41',5,'F',4,'Number Theory',['Digits','Modular arithmetic','Construction'],'The change in digit sum across a run of p terminal nines is 1−9p, forcing p≡5 modulo 11; a fixed prefix digit sum gives infinitely many examples.'),
('d83145',6,'F',2.5,'Combinatorics',['Counting','Arithmetic progressions'],'Classify the triples as {b,3b,5b} or {b,5b,9b}; direct bounded counts give six containing 225 and 630 in total.'),
('463b42',6,'F',3.5,'Number Theory',['Divisibility','Squares'],'The size bound forces a+b=c, then b divides 3a; the two ratio families reduce abc being square to squarefree-part constraints.'),
('f79824',6,'F',4,'Geometry',['Angle bisectors','Congruence','Equilateral triangles'],'Bisect the 40-degree angle between BA and BI to obtain a triangle congruent to IAB and an equilateral triangle on BC.'),
('7fbbe0',6,'F',4.5,'Combinatorics',['Graph theory','Parity','Colouring'],'Same-colour components are cycles because every vertex has degree two; the checkerboard bipartition forces every cycle even, and 2-by-2 blocks attain every even n.'),
('5a3274',11,'F',None,'Algebra',['Calculus'],'The solution uses continuity of second derivatives to force quadratic functions with the same leading coefficient; differentiability is outside BMO prerequisites.'),
('5d4bd8',11,'F',None,'Algebra',['Linear algebra'],'An affine map permutes the eigenvalues of AB; spectral theory and determinant invertibility are outside BMO prerequisites.'),
('61ff37',11,'F',None,'Algebra',['Calculus'],'The equivalence requires the mean-value theorem and the sequential characterization of continuous differentiability, outside BMO prerequisites.'),
('c270f6',11,'F',None,'Algebra',['Linear algebra'],'The question is about matrix commutators, determinants and traces; it is outside BMO prerequisites. The raw statement also confuses determinant and trace in part (b), so the official original is authoritative.'),
('78edd8',12,'F',None,'Algebra',['Abstract algebra'],'The proof uses units of a ring, characteristic three and the group of invertible elements; these algebraic structures are outside BMO prerequisites.'),
('e13840',12,'F',None,'Algebra',['Calculus'],'Integration by parts and integral Cauchy–Schwarz produce the constant 12; the entire question requires calculus.'),
('be14df',12,'F',None,'Algebra',['Calculus'],'The proof combines an exponential integrating factor with factorized differential operators; these prerequisites lie outside BMO.'),
('072a6e',12,'F',None,'Algebra',['Finite fields'],'The argument uses cyclic finite-field groups and a roots-of-unity coefficient filter in characteristic two, outside BMO prerequisites.'),
# District papers.
('76bd7e',5,'D',1,'Algebra',['Linear equations'],'With f girls and 3f boys, the official absence of two girls and one boy gives 3f−1=4(f−2), hence 28 pupils; the raw English statement reverses the genders.'),
('5b88e0',5,'D',2.5,'Number Theory',['Binary representation','Valuations'],'The binary expansion 305=2^8+2^5+2^4+1 determines the four exponents up to a common shift and gives remainder 2.'),
('3b80b5',5,'D',3,'Combinatorics',['Extremal arguments','Construction'],'Summing the forty largest distinct integers below a proposed maximum gives maximum at least 71, and {1,29,34,...,71} attains it.'),
('6af78e',6,'D',2.5,'Number Theory',['Integer bounds'],'Comparing positive numerator and denominator bounds n strictly between zero and two; substituting n=1 then bounds m between one and three.'),
('ec5818',6,'D',3.5,'Number Theory',['GCD','LCM','Divisibility'],'Remove the gcd to obtain coprime x,y with xy dividing 24; a linear relation restricts the gcd to six possibilities, leaving (a,b)=(16,6).'),
('aaf971',6,'D',3.5,'Geometry',['Congruence','Isosceles triangles'],'Congruence of BDF and EDG gives BF=GE, hence BG=BC; the remaining angle is half of 105 degrees.'),
('50f800',6,'D',4,'Number Theory',['Divisors','Extremal arguments','Parity'],'A composite solution must be even and divisible by three; its proper-divisor sum already contains n/2+n/3+n/6=n, forcing exactly those divisors and n=6.'),
('95ee7d',7,'D',2.5,'Number Theory',['Primes','Radicals'],'The radical sum is below twenty, restricting the prime to 2 or 3; solving the remaining radical equations leaves 2025.'),
('2b8e0d',7,'D',2,'Algebra',['Rationality','Squares'],'Rationality forces sqrt(ab) integral, so r is a nonnegative half-integer; a=m,b=4m attains every such value.'),
('59f943',7,'D',4.5,'Geometry',['Squares','Cyclic quadrilaterals','Congruence'],'The auxiliary right triangle makes H the midpoint of DF; cyclic angles then prove equal perpendicular diagonals for DIFJ.'),
('35fbfc',7,'D',5.5,'Geometry',['Orthocentre','Reflection','Angle bisectors'],'Two separate midpoint statements are needed: orthic cyclic quadrilaterals make A bisect MP, and reflecting A in the midpoint of BC makes it bisect NQ.'),
('37dfda',8,'D',2.5,'Algebra',['Algebraic identities','Sum of squares'],'Factor the sum-of-cubes identity, then use a sum of three squares to isolate the single exceptional point (1,1).'),
('439fc6',8,'D',4,'Number Theory',['Diophantine equations','Factorisation'],'Introducing d=x−y yields (d+2)(d+xy−2)=13; signed factor pairs and nonnegativity leave (x,y)=(1,16).'),
('718dde',8,'D',4.5,'Algebra',['Cyclic inequalities','Extremal arguments'],'A variable on either side of two forces all three to that side; multiplying the shifted inequalities contradicts the product bound unless all equal two.'),
('d10be4',8,'D',3.5,'Geometry',['Solid geometry','Vectors'],'With cube coordinates, A′M has direction (1,t,−1); its dot products with AB′=(1,0,1) and AN=(0,1,t) both vanish.'),
('fccbaf',9,'D',2.5,'Geometry',['Vectors','Centroid'],'Express OM in the independent directions OA,OB; the centroid vector equation determines the complementary coefficients on OC and OD uniquely.'),
('4f853d',9,'D',3.5,'Algebra',['Floors','Quadratic equations'],'Writing floor(x)=−k reduces to a quadratic; imposing the defining unit interval leaves k=1,2 and two negative roots.'),
('c30a6c',9,'D',4,'Algebra',['AM–GM','Equality cases'],'Adding four converts the expression to four ratios with telescoping product 81; equality in AM–GM forces every ratio to equal three.'),
('d7a13b',9,'D',4.5,'Combinatorics',['Induction','Subset sums'],'Prove the stronger coverage of every integer below 2x_n; subtracting the next term keeps the remaining target within the previous covered interval.'),
('29b819',10,'D',3,'Algebra',['Monotonicity','Logarithms'],'Introducing the common logarithm value gives equal values of 6^t+7^t, so x=y; a second monotonicity comparison yields x=1.'),
('7c762b',10,'D',2.5,'Algebra',['Floors','Exponential functions'],'Simple bounds exclude x outside [−1,1), and each of the two remaining unit intervals reduces to one exponential equation.'),
('bf76a3',10,'D',4.5,'Algebra',['Functional equations','Complex numbers','Triangle inequality'],'Equal arguments give norm preservation; the equation with one argument one forces equality in the complex triangle inequality and hence f(z)=cz with |c|=1.'),
('f67202',10,'D',6,'Geometry',['Complex numbers','Similarity','Centroid'],'Extend three alternate sides to an equilateral triangle centred at P, then sum three identical rotation-and-scaling relations to relate the centroids.'),
('df5099',11,'D',None,'Algebra',['Calculus'],'The sequence rationalizes to 1+a_(n+1)=sqrt(1+a_n), giving explicit logarithmic sums; the requested limits are outside BMO prerequisites.'),
('0fe4c5',11,'D',None,'Algebra',['Linear algebra'],'A determinant expansion identifies a symmetric adjugate; matrix invertibility and adjugates are outside BMO prerequisites.'),
('94e841',11,'D',None,'Algebra',['Calculus'],'The argument uses continuous inverse functions and asymptotic limits, outside BMO prerequisites.'),
('84e147',11,'D',None,'Algebra',['Linear algebra'],'Expanding the three real 2-by-2 commutators makes sums of entry squares vanish, but the statement requires matrix algebra outside BMO prerequisites.'),
('94000f',12,'D',None,'Algebra',['Abstract algebra'],'The proof relies on subgroup closure and translates in finite groups, outside BMO prerequisites.'),
('3f1caa',12,'D',None,'Algebra',['Abstract algebra'],'The question concerns group endomorphisms and the centre of a nonabelian group, outside BMO prerequisites.'),
('65fab9',12,'D',None,'Algebra',['Calculus'],'Vanishing integrals of strictly monotone functions constrain the eventual sequence values; integral calculus is essential and outside BMO prerequisites.'),
('4ffbdb',12,'D',None,'Algebra',['Calculus'],'The averaged integral function is treated by the fundamental theorem of calculus and endpoint limits, outside BMO prerequisites.')]
statements={
'ba6c41':r'Call a positive integer special when the digit sums of both it and its successor are divisible by $11$. Determine its final five decimal digits, and prove that infinitely many special integers exist.',
'f79824':r'Triangle $ABC$ has $\angle A=40^\circ$ and $\angle B=80^\circ$, and $I$ is its incenter. Prove that $AI=BC$.',
'7fbbe0':r'Determine all integers $n\ge2$ for which an $n\times n$ board admits a colouring such that every cell has exactly two side-adjacent neighbours of its own colour.',
'50f800':r'List the positive divisors of $n\ge2$ as $1=d_1<d_2<\cdots<d_k=n$. Determine all $n$ divisible by each proper initial sum $d_1+d_2+\cdots+d_j$ for $1\le j<k$.',
'59f943':r'Squares $ABCD$ and $BEFG$ are positioned with $B$ on segment $AE$ and $G$ on segment $BC$. Put $H=DF\cap EG$. The perpendicular to $DF$ through $H$ meets lines $AE,BC$ at $I,J$. Prove that $DIFJ$ is a square.',
'35fbfc':r'Let $ABC$ be acute with $AB\ne AC$, and let $D$ be the midpoint of $BC$. Let $I,J,K$ be the feet of the altitudes from $A,B,C$. The line through $A$ perpendicular to $AD$ meets lines $BJ,CK$ at $N,Q$. The line through $A$ parallel to $BC$ meets $IJ,IK$ at $M,P$. Prove that $MNPQ$ is a parallelogram.',
'439fc6':r'Find all nonnegative integers $x,y$ satisfying $x^2+y^2+xy(x-y)=17$.',
'718dde':r'Nonnegative reals $x,y,z$ satisfy $xy+4\le2(x+z)$, $yz+4\le2(y+x)$ and $zx+4\le2(z+y)$. Prove that $x=y=z$.',
'c30a6c':r'Find all positive reals $a,b,c,d$ with $a+b+c+d=80$ and $$a+\frac b{1+a}+\frac c{1+a+b}+\frac d{1+a+b+c}=8.$$',
'd7a13b':r'An unbounded nondecreasing sequence of positive integers starts with $x_1=1$ and satisfies $x_{n+1}\le2x_n$. Prove that every positive integer is a sum of finitely many terms with distinct indices.',
'bf76a3':r'Determine all functions $f:\mathbb C\to\mathbb C$ such that $$|wf(z)+zf(w)|=2|zw|$$ for every pair of complex numbers $z,w$.',
'f67202':r'A convex hexagon $ABCDEF$ has $\angle A=\angle C=\angle E$ and $\angle B=\angle D=\angle F$. An interior point $P$ is equidistant from sides $AB,CD,EF$. If the centroids $G_1,G_2$ of triangles $ACE,BDF$ are distinct, prove $\angle G_1PG_2=60^\circ$.'}
sub={
'ba6c41':['Digits & bases','Modular arithmetic'],
'f79824':['Triangle centres','Similarity & congruence','Triangle geometry'],
'7fbbe0':['Graph theory','Colouring','Parity'],
'50f800':['Divisibility & GCD','Extremal arguments','Parity'],
'59f943':['Quadrilaterals & polygons','Angles & cyclic quadrilaterals','Similarity & congruence'],
'35fbfc':['Triangle centres','Transformations','Angles & cyclic quadrilaterals'],
'439fc6':['Diophantine equations','Divisibility & GCD'],
'718dde':['Inequalities','Extremal arguments'],
'c30a6c':['Inequalities'],
'd7a13b':['Induction','Sets & partitions'],
'bf76a3':['Functional equations','Complex numbers','Inequalities'],
'f67202':['Coordinates & vectors','Similarity & congruence','Triangle centres']}
for short,g,round,v,t,tags,why in rows:
 slug='rou_2025_'+short;d=json.loads((p/(slug+'.json')).read_text());num=re.search(r'\d+',d['problem_number'])[0]
 u=f'https://ssmr.ro/files/onm2025/faza_nationala/{g:02d}_solutii_bareme_ONM_2025.pdf' if round=='F' else f'https://ssmr.ro/files/onm2025/faza_municipiu/barem_clasa{g}.pdf'
 x={'difficulty':v,'topic':t,'tags':tags,'reason':why,'number':num,'section':('National Final' if round=='F' else 'District Round')+f' — Grade {g}','sourceUrl':u,'solutionUrl':u,'sourceName':'Romanian Mathematical Society — official paper and worked solutions','license':'Original contest rights retained; concise English paraphrase.','notes':'Reviewed against the official paper and worked solution for problem '+num+'.'}
 if v is None:x['outOfScope']=True
 if short in statements:x['statement']=statements[short];x['subtopics']=sub[short];x['solution']=f'[Official worked solution, problem {num}]({u}).';x['solutionKind']='source-link'
 r[slug]=x
# The corpus omitted district Grade 5 Q3; restore the official item and assessment.
slug='rou_2025_district5_3';u='https://ssmr.ro/files/onm2025/faza_municipiu/barem_clasa5.pdf'
(p/(slug+'.json')).write_text(json.dumps({'country':'Romania','competition':'Romanian Mathematical Olympiad','year':2025,'section':'District Round — Grade 5','problem_number':'3','problem_markdown':'After 674 deletions of adjacent integer pairs from 1 through 2025, prove the surviving sum is not divisible by 6 but the surviving product is.','solutions_markdown':[]},indent=2))
r[slug]={'difficulty':2.5,'topic':'Number Theory','tags':['Parity','Divisibility'],'reason':'Each deletion removes one odd and one even number, leaving an odd sum; at most 674 of the 675 multiples of three disappear and 338 even survivors remain.','number':'3','sourceUrl':u,'solutionUrl':u+'#page=2'}
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
