import json,pathlib
p=pathlib.Path('research/asia/reviews.json');r=json.loads(p.read_text());raw=pathlib.Path('research/raw/asia');official='https://library.hbcse.tifr.res.in/olympiads/uploads/inmo-sol-2011'
def add(k,d,reason,sol=None,**kw):
 r['ind_2011_'+k]={'difficulty':d,'reason':reason,**kw}
 if sol:r['ind_2011_'+k]['solutionOverride']=sol
add('07c81d',4,'A strengthened rational-root divisibility observation uses the vanished next-to-leading coefficient to rule out a prime denominator.',r'''Write $r=u/v$ in lowest terms with $v>0$, and put $p=a_n-b_n$. Subtracting $P(r)=Q(r)=0$ and clearing denominators gives
$$pu^n+(a_{n-2}-b_{n-2})u^{n-2}v^2+\cdots+(a_0-b_0)v^n=0.$$
For $n\ge2$ this implies $v^2\mid pu^n$. Coprimality gives $v^2\mid p$, so $v=1$. If $n=1$, the equality $a_0=b_0$ instead gives $pr=0$, hence $r=0$. In every case the common rational root is an integer.''',numberOverride='3',sourceUrl=official,statementOverride=json.loads((raw/'ind_2011_07c81d.json').read_text())['problem_markdown'].replace('a_n b_0 - a_{n-1} b_n','a_n b_0 - a_0 b_n'),note='Question number and constant-coefficient condition corrected against the official HBCSE INMO 2011 paper.')
add('1536f1',4,'Finds the nine possible chord directions and applies pigeonhole to the ten chords from five vertices.',r'''Label the nonagon vertices $0,1,\ldots,8$ counterclockwise. The direction of the chord joining $i$ and $j$, modulo $180^\circ$, depends only on $i+j\pmod9$, so there are nine possible directions. The five chosen vertices determine ten chords. Two chords therefore have the same direction. They cannot share an endpoint, since three distinct points of a circle are not collinear. Their four endpoints consequently form a quadrilateral with a pair of opposite sides parallel, which is the required trapezium.''',sourceUrl=official,topic='Combinatorics')
add('3546d2',5.5,'A hidden similarity between the inner and outer triangles leads to cyclic side ratios whose ordering forces equality.',r'''Write $a=BC$, $b=CA$, $c=AB$, $x=BD=CE=AF$ and $\theta=\angle BDF$. Angle chasing gives $\angle DFE=B$, $\angle EDF=C$ and $\angle FED=A$. Thus $FD=ka$, $DE=kb$, $EF=kc$ for some $k>0$.

Applying the sine rule in the three corner triangles yields
$$\frac{b(c-x)}a=\frac{c(a-x)}b=\frac{a(b-x)}c.$$
If two sides agree, this identity forces the third to agree too. Otherwise, cyclically relabel so $a$ is smallest. If $a<b<c$, the first and third ratios imply $b(c-x)<a(b-x)$, although both factors on the left exceed their counterparts on the right. If $a<c<b$, the first and second ratios imply $b^2(a-x)=ac(c-x)$; equivalently $(c-x)/(a/b)=(a-x)/(b/c)$, so $a-x<c-x$ forces $b/c<a/b$, or $b^2<ac$, again impossible. Therefore all sides are equal.''',sourceUrl=official)
# Correct a rearrangement in the explanatory text: the ratio equation is authoritative.
r['ind_2011_3546d2']['solutionOverride']=r['ind_2011_3546d2']['solutionOverride'].replace('the first and second ratios imply $b^2(a-x)=ac(c-x)$; equivalently','the first and second ratios can be written')
add('5511fb',4.5,'Uses the zero input to prove evenness, then swapping two inputs forces a quadratic form.',numberOverride='6',sourceUrl=official)
add('60c493',4,'The same nine-direction pigeonhole argument applies.',omitReason='Duplicate of INMO 2011 Q4 (ind_2011_1536f1); source labels this copy Q3, corrected against official paper.',numberOverride='4',sourceUrl=official)
add('6d43c4',5.5,'Constructs broad infinite families and proves the finite remainder by divisibility, rather than merely testing small values.',sourceUrl=official)
add('9fc5bb',5,'Interprets the equation as perpendicularity, then uses descent of integer squared distances to force eventual period two.',r'''Let $P_n=(a_n,b_n)$. The condition is a dot-product equation
$$(P_n-P_{n-1})\cdot(P_n-P_{n-2})=0.$$
By expanding squares, this gives
$$|P_{n-1}-P_{n-2}|^2=|P_n-P_{n-1}|^2+|P_n-P_{n-2}|^2.$$
Hence the nonnegative integer squared distances $|P_n-P_{n-1}|^2$ form a nonincreasing sequence. They eventually become constant. The identity then forces $|P_n-P_{n-2}|^2=0$ for every sufficiently large $n$, so both coordinate sequences eventually have period two. Since $2011^{2011}-2011$ is even, choosing $K$ far enough into this tail proves the desired equality.''')
add('a86186',7,'Requires a sustained configuration analysis, three similar corner triangles, and trigonometric reconstruction of the radius and weighted distances.',solutionKind='source-link')
add('c0e0a9',3.5,'Successive uses of the midpoint-of-hypotenuse theorem force the bisector to be perpendicular and both side equalities.')
add('ce10dc',5.5,'A half-angle chord identity and Ptolemy turn the hypothesis into an equality case forcing four diameters.',numberOverride='5',sourceUrl=official)
add('d8fd7b',6.5,'Combines a homothety between tangent circles with a half-turn and a final cyclic-quadrilateral angle argument.',solutionKind='source-link')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2));print(len(r))
