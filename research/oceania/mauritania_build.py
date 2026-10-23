import json
P='/workspace/sites/olympiad-atlas/research/oceania/'
urls={2017:'https://maurimath.net/documents/Olympiades/Olympiades7cT3%20.pdf',2018:'https://maurimath.net/documents/Olympiades/CorrigesT3OlympM7C2018.pdf',2019:'https://maurimath.net/documents/Olympiades/Olymp7C19T3.pdf',2023:'https://maurimath.net/documents/Olympiades/Olymp7CT3M2023.pdf'}
solurls={2018:urls[2018],2019:'https://maurimath.net/documents/Olympiades/CorrectionOlympiade7C2019T3.pdf',2023:'https://maurimath.net/documents/Olympiades/Corrig%C3%A9T3OLy7C2023.pdf'}
items=[];ledger=[]
def add(y,n,d,topic,tags,s,sol,r):
 id=f'mrt_7c_t3_{y}_{n}';comp='Mauritanian National Olympiad — 7C, Round 3'
 items.append(dict(id=id,country='Mauritania',competition=comp,year=y,number=str(n),statement=s,solution=sol,sourceUrl=urls[y],solutionUrl=solurls.get(y),topic=topic,tags=tags,difficulty=d,ratingReason=r,reviewStatus='individually-assessed',solutionKind='original-exposition',notes='French Ministry of Education paper archived by Maurimath; final-year secondary level (7C), third round. English mathematical paraphrase and independently written solution. Linked suggested solutions, where present, are by AMIMATHS. Original scaffolding is retained.'))
 ledger.append(dict(id=id,country='Mauritania',competition=comp,year=y,number=str(n),difficulty=d,status='reviewed',included=True,reason=r,sourceUrl=urls[y]))
def skip(y,n,d,r,status=None):ledger.append(dict(id=f'mrt_7c_t3_{y}_{n}',country='Mauritania',competition='Mauritanian National Olympiad — 7C, Round 3',year=y,number=str(n),difficulty=d,status=status or ('reviewed' if d else 'pending-solution-review'),included=False,reason=r,sourceUrl=urls[y]))
skip(2017,1,3,'The reflected orthocentre is the antipode of A, and the sine rule at angle30 degrees immediately gives AD=2BC.')
skip(2017,2,3.5,'Bounding the three remaining price percentages between77 and99 leaves the factors85,92,95, hence discounts15,8,5 percent.')
skip(2017,3,3.5,'Similarity gives the two inscribed-square side lengths; their comparison reduces to (a−b)(a−c)>0.')
skip(2017,4,3.5,'The four-digit palindrome abba has rank99+10a+b; the ratio22 becomes71a+8b=198, giving2772.')
add(2017,5,4.5,'Geometry',['paper folding','coordinates','optimization','AM-GM'],r'A rectangular sheet $ABCD$ has $AB=4,BC=6$. Points $R\in AB,T\in AD$ define a fold that reflects $A$ to $S\in BC$. Put $x=AR,y=AT$. Find the minimum and maximum possible $x$, a relation between $x,y$, and the value of $x$ minimizing the area of $SRT$. What kind of triangle is $AST$ at the minimum?',r'''Put $A=(0,0),B=(4,0),C=(4,6),D=(0,6)$ and $S=(4,s)$. Reflection gives $RA=RS$ and $TA=TS$, so
$$s^2=8x-16,\qquad 2sy=16+s^2=8x.$$
Thus $y=4x/\sqrt{8x-16}$. The constraints $x\le4$ and $y\le6$ are equivalent to
$$9-3\sqrt5\le x\le4.$$
Throughout this interval $0<s\le4<6$, so $S$ also lies on the required side, and the equal-distance conditions ensure the line $RT$ is the perpendicular bisector of $AS$.

The folded triangle has the same area as $ART$, namely
$$K=\frac{xy}{2}=\frac{x^2}{\sqrt{2x-4}}.$$
Write $x=2+t$, $t>0$. Applying AM-GM to $t,2/3,2/3,2/3$ gives $(t+2)^4\ge256t(2/3)^3$. Hence $K^2\ge1024/27$, with equality exactly when $t=2/3$, or $x=8/3$; this lies in the permitted interval. At that value $s=4/\sqrt3$ and $y=8/\sqrt3$. Since $AS=8/\sqrt3=AT=ST$, triangle $AST$ is equilateral.''','The fold must first be translated into two distance equations and feasible bounds; a separate sharp inequality then optimizes the area without calculus.')
skip(2018,1,None,'Logarithmic inequality and product estimate use curriculum outside the intended elementary BMO question bank.','excluded-outside-topic')
add(2018,2,4.5,'Number Theory',['exponential Diophantine equations','2-adic valuations','bounding'],r'For integers $x,y$, consider $1+2^x+2^{2x+1}=y^2$. Find an example solution. Show that if $x\ne0$, then $x\ge3$ and $y=2^{x-1}m\pm1$ for some odd integer $m$. Determine every integer solution.',r'''The solutions are $(0,\pm2)$ and $(4,\pm23)$. Negative $x$ gives a value strictly between one and four that is not an integer square; $x=0$ gives $y=\pm2$, while $x=1,2$ give $11,37$ and fail.

For $x\ge3$, $y$ is odd and
$$(y-1)(y+1)=2^x(1+2^{x+1}).$$
Exactly one of the consecutive even factors has 2-adic valuation one, so the other has valuation $x-1$. This proves the stated form with odd $m$.

By symmetry assume $y>0$. The equation gives $2^x<y<2^{x+1}$. In the form $y=2^{x-1}m+\varepsilon$, with $m$ odd and $\varepsilon=\pm1$, these bounds force $m=3$. Substitution then yields
$$2^{x-2}=1-3\varepsilon.$$
Only $\varepsilon=-1$ is possible, giving $x=4,y=23$. Restoring both signs of $y$ proves the classification.''','The supplied scaffold still leaves a valuation argument and a tight size bound that reduces an exponential equation to one odd coefficient.')
skip(2018,3,None,'Logarithmic trigonometric integral lies outside elementary olympiad topic scope.','excluded-outside-topic')
add(2018,4,5,'Geometry',['cyclic polygons','area maximization','trigonometry'],r'A convex cyclic octagon $A_1A_2\cdots A_8$ has alternate vertices $A_1,A_3,A_5,A_7$ forming a square of area $5$, while $A_2,A_4,A_6,A_8$ form a rectangle of area $4$. Find the maximum possible area of the octagon.',r'''The maximum is $3\sqrt5$. Let the common circumradius be $R$, so $2R^2=5$. Choose the square's vertex angles as $0,\pi/2,\pi,3\pi/2$. The rectangle's angles are $a,b,a+\pi,b+\pi$, where $0<a<\pi/2<b<\pi$. Put $\delta=b-a$. The rectangle area condition is
$$2R^2\sin\delta=4,\qquad\sin\delta=4/5.$$
Summing the eight central triangle areas gives the octagon area
$$R^2(\sin a+\cos a+\sin b-\cos b)
=2\sqrt2R^2\sin\frac{a+b}{2}\cos\left(\frac\pi4-\frac\delta2\right).$$
The squared cosine factor is $(1+\sin\delta)/2=9/10$, and the sine factor is at most one. Therefore the area is at most $3\sqrt5$.

Equality is attainable: choose $a=(\pi-\delta)/2$ and $b=(\pi+\delta)/2$, where either angle $0<\delta<\pi$ satisfying $\sin\delta=4/5$ may be used. This preserves the alternating vertex order and makes $a+b=\pi$.''','Both inscribed quadrilaterals must be parametrized on a common circle; summing central triangle areas exposes the independent rotation parameter to optimize.')
skip(2018,5,3.5,'The two polynomial equations are simply real and imaginary parts of (x+iy)^5=32e^(iπ/12); fifth roots complete the calculation.')
skip(2019,1,3,'The two shaded regions have equal areas by inclusion-exclusion; the overlap is two elementary circular segments.')
skip(2019,2,3.5,'The guided factorization and remainder calculations reduce the divisor problem to a finite divisor list; for n=3 the answers are−5 and9.')
skip(2019,3,None,'Definite integration with inverse trigonometric functions is outside elementary BMO topic scope.','excluded-outside-topic')
skip(2019,4,None,'Continuity and a logarithmic integral limit are outside elementary BMO topic scope.','excluded-outside-topic')
add(2019,5,6.5,'Geometry',['orthocentres','nine-point circle','inversion','concurrence'],r'In acute triangle $ABC$, altitudes $AD,BE$ meet at $H$, and $M$ is the midpoint of $AB$. Circles $DEM$ and $ABH$ meet at $P,Q$, with $P$ on the same side of line $CH$ as $A$. Set $R=DE\cap PH$. Prove: (a) $\angle RDA=\angle RPA$ and $B,P,R,E$ are cyclic; (b) $R$ lies on circle $ABC$; (c) $DE,PH,MQ$ concur at $R$.',r'''Use directed angles and let $F$ be the foot of the altitude from $C$. Since $A,B,D,E$ lie on the circle with diameter $AB$ and $A,B,H,P$ are cyclic,
$$\angle RDA=\angle EDA=\angle EBA=\angle HBA=\angle HPA=\angle RPA.$$
Thus $A,D,P,R$ are cyclic. It follows that
$$\angle PBE=\angle PBH=\angle PAH=\angle PAD=\angle PRD=\angle PRE,$$
so $B,E,P,R$ are cyclic as well.

The points $D,E,F,M,P$ lie on the nine-point circle of $ABC$. Using the two newly established circles gives
$$\angle ARB=\angle ARP+\angle PRB=\angle ADP+\angle PEB.$$
Split the last two angles through $F$. Their terms $\angle FDP$ and $\angle PEF$ cancel, because $D,E,F,P$ are cyclic. The remainder is
$$\angle ADF+\angle FEB=\angle ACF+\angle FCB=\angle ACB,$$
using circles $ACDF$ and $BCEF$. Hence $A,B,C,R$ are cyclic.

For the concurrence, invert about $M$ with radius $MA=MB=MD=ME$. Circle $DEM$, which passes through $M$, maps to line $DE$. Circle $ABH$ maps to circle $ABC$: these circles have equal radius $AB/(2\sin\angle ACB)$, share $A,B$, and have centres reflected in $M$; an inversion with the stated radius interchanges them.

Therefore the images $P',Q'$ are precisely the two intersections of $DE$ with circle $ABC$. One is $R$ by part (b). The image $P'$ lies on $MP$, whereas $R$ lies on $HP$, so it is the other intersection (the two lines meet at $P$, which is not on $DE$). Hence $R=Q'$, which lies on $MQ$. This proves the final concurrence.''','The scaffold still requires several connected cyclicity arguments and an inversion that exchanges the altitude circle with the circumcircle.')
skip(2023,1,2.5,'Short direct logical elimination identifies a short suspect with a white shirt, red trousers and no bracelet; the printed repetition shortcut is unnecessary.')
skip(2023,2,2.5,'Four direct AM-GM bounds give each summand at most(4−a)/27 and equality only at a=b=c=d=1.')
add(2023,3,4.5,'Geometry',['tangents','circle symmetry','cyclic quadrilaterals'],r'Circle $\Gamma_1$ is internally tangent to circle $\Gamma_2$ at $A$. From $P\in\Gamma_2$, $P\ne A$, draw tangents to $\Gamma_1$ touching at $B,C$. Lines $PB,PC$ meet $\Gamma_2$ again at $Q,R$. Prove $\angle QAR=2\angle BAC$. If line $BC$ meets $\Gamma_2$ at $E,F$ and $PE=PF$, prove $B,C,Q,R$ are cyclic.',r'''For the first claim, combine the inscribed-angle theorem on the outer circle with the tangent-chord theorem on the inner one. In directed-angle form,
$$\angle QAR=\angle QPR=\angle QBC+\angle BCR=\angle BAC+\angle BAC.$$
The specified configuration gives the stated ordinary-angle equality.

For the second claim, let $O_1,O_2$ be the two centres. Equal tangents $PB=PC$ put $P,O_1$ on the perpendicular bisector of $BC$. The assumption $PE=PF$ puts $P,O_2$ on the perpendicular bisector of $EF$, which is the same line because $B,C,E,F$ are collinear. Thus $P,O_1,O_2$ lie on one line.

Reflection in this line preserves both circles, swaps $B,C$, and swaps $Q,R$. Hence $BC$ and $QR$ are parallel and the other two sides of quadrilateral $BCRQ$ are equal. It is an isosceles trapezoid, so it is cyclic. This is the required cyclicity of the four points.''','The angle part combines the two circle configurations; the additional equal-distance condition must then be recognized as forcing a common symmetry axis.')
skip(2023,4,2,'Expanding the square of the sum gives sum of squares36, and equality in Cauchy forces all four variables to equal3.')
skip(2023,5,None,'The equation itself is absent from both text extractions, although the solution factors it; withheld until the original equation is visually recovered.','withheld-malformed')
json.dump(items,open(P+'mauritania.json','w'),indent=2)
json.dump(ledger,open(P+'mauritania-ledger.json','w'),indent=2)
print(len(items),len(ledger))
