import json,pathlib
P=pathlib.Path('/workspace/sites/olympiad-atlas/research/asia');RAW=P.parent/'raw'/'asia'
rev=json.loads((P/'reviews.json').read_text());man=json.loads((P/'manifest.json').read_text())
def write(country,year,comp,section,num,d,topic,reason,statement='',solution='',url='',solutionUrl=''):
 slug=f'{"isr" if country=="Israel" else "lka"}_{year}_{"gillis" if country=="Israel" else "slmc"}_q{num}'
 raw={'country':country,'competition':comp,'year':year,'section':section,'problem_number':str(num),'problem_markdown':statement or f'Problem {num}; see official paper','solutions_markdown':[solution],'primary_domain':topic,'topics':[],'booklet_title':f'{comp} {year} official paper','sourceDataset':'Weizmann Institute of Science' if country=='Israel' else 'Sri Lanka Olympiad Mathematics Foundation','sourceLicense':'Mathematical statement independently translated/paraphrased; worked solution independently rewritten.'}
 (RAW/(slug+'.json')).write_text(json.dumps(raw,ensure_ascii=False,indent=2))
 v={'difficulty':d,'reason':reason,'sourceUrl':url,'solutionUrl':solutionUrl or url,'note':'All seven tasks in the official paper dated 6 December 2023 were individually reviewed with the official solution booklet. Hebrew year 5784.' if country=='Israel' else 'All 30 questions in the official SLMC paper dated 7 April 2018 were individually reviewed, including the rendered diagrams and formula images. Original multiple-choice task; independent explanation provided for included questions.'}
 if solution:v['solutionOverride']=solution
 else:v['solutionKind']='source-link'
 rev[slug]=v
 if slug not in {x[0] for x in man}:man.append([slug,'israel-weizmann' if country=='Israel' else 'srilanka-official',year,comp,0,0,str(num)])
u='https://www.weizmann.ac.il/math/gillis/sites/math.gillis/files/uploads/Gillis2023.pdf';su=u.replace('.pdf','_solved.pdf')
def israel(n,d,t,r,s='',sol=''):write('Israel',2023,'Gillis Mathematical Olympiad','National',n,d,t,r,s,sol,u,su)
israel(1,3.5,'Algebra','Successive substitutions for sum and product turn the equations into a linear system and then two quadratics, with one discriminant negative.')
israel(2,3.5,'Number Theory','Clearing the fractional-part denominators determines every remainder independently; doubling those remainders gives the requested sum.')
israel(3,3.5,'Combinatorics','Each odd row requires a diagonal pair, while a snake-order matching uses exactly one per odd row, attaining the parity bound.')
israel(4,5.5,'Geometry','Reflecting the circumcenter in the altitudes puts four points on a circle centered at the orthocenter; an angle chase then identifies the concurrence on the original circumcircle.',r'''Triangle $ABC$ has circumcenter $O$. Reflect $O$ in the altitude lines from $A,B,C$ to obtain $U,V,W$, respectively. Through $A$ draw a line parallel to $VW$, through $B$ one parallel to $WU$, and through $C$ one parallel to $UV$. Prove that the three lines are concurrent. Assume the indicated directions are defined.''',r'''Let $H$ be the orthocenter. Since each reflection axis passes through $H$,
$$HU=HV=HW=HO.$$
Thus $O,U,V,W$ lie on a circle centered at $H$. Also $OU\parallel BC$, $OV\parallel CA$, and $OW\parallel AB$, because each segment from a point to its reflection is perpendicular to the reflection axis.

Let the first two proposed lines meet at $X$. Using directed angles modulo $180^\circ$ and the cyclicity just obtained,
$$\angle AXB=\angle VWU=\angle VOU=\angle ACB.$$
Hence $A,B,C,X$ are concyclic. Similarly the intersection of the first and third proposed lines lies on the same circumcircle. The line through $A$ has only one second intersection with that circle, so the intersections coincide. Limiting tangent configurations follow by the same directed-angle argument.''')
israel(5,6,'Number Theory','Odd-index divisibility gives one direction; in the other, a simultaneous Fermat exponent avoids every prime below a proposed bound.',r'''Let $a_1>2$ be an integer and define $a_{n+1}=a_n^n-1$. For an integer $k>1$, let $p(k)$ be its least prime divisor. Determine the values of $a_1$ for which there exists an integer $M$ with $p(a_n)<M$ for every $n\ge1$.''',r'''Exactly the odd values of $a_1$ work. Parity alternates at every step. Moreover
$$a_{2j+1}=(a_{2j-1}^{,2j-1}-1)^{2j}-1\equiv0\pmod{a_{2j-1}}.$$
Thus every odd-indexed term is divisible by $a_1$. If $a_1$ is odd, all even-indexed terms are even, so the least prime factors are bounded by $\max(2,p(a_1))$.

Conversely suppose $a_1$ is even and the least prime factors are bounded. List all primes below a proposed bound, enlarging the bound if necessary so that both $2$ and $3$ are present. Let $L$ be the product of $p-1$ over these primes, and set $n=L+1$, which is odd. For each such prime $p$, either $p\mid a_L$, or Fermat's theorem gives $a_L^L\equiv1\pmod p$. Hence
$$a_n=a_L^L-1\equiv-1\ \text{or}\ 0\pmod p.$$
Since $n$ is odd, $a_{n+1}=a_n^n-1$ is congruent to $-2$ or $-1$ modulo each odd listed prime, so none divides it. Because $a_1$ is even and $n+1$ is even, parity alternation makes $a_{n+1}$ odd; $2$ does not divide it either. This contradicts the proposed bound.''')
israel(6,7,'Geometry','The arc-midpoint incenter lemma identifies the direction of each common tangent; a homothety of tangential quadrilaterals then transfers the required diagonal direction.',r'''Let $ABCD$ be cyclic. Denote the incircles of $DAB,ABC,BCD,CDA$ by $\omega_A,\omega_B,\omega_C,\omega_D$. The common external tangent of $\omega_A,\omega_B$ other than $AB$ meets the common external tangent of $\omega_A,\omega_D$ other than $AD$ at $A'$. Likewise, define $C'$ using the common external tangents of $\omega_C,\omega_D$ other than $CD$, and of $\omega_C,\omega_B$ other than $BC$. Prove that $AA'\parallel CC'$.''')
israel(7,9,'Combinatorics','The two-part rook problem needs a near-extremal obstacle construction and a sharp counting argument involving rows, columns, and shortest-path landing squares.')
u='https://www.slmathsolympiad.org/pdf/resources/slmc/english/2018E.pdf'
simple={
1:(1,'Combinatorics','Match the repeated dancing-man symbols against the repeated digits in the five offered strings.'),
2:(1.5,'Combinatorics','Choose independently zero through two of one sweet and zero through three of the other, then exclude the empty plate.'),
3:(2,'Algebra','The zero is best added harmlessly, and grouping one with two before multiplying by eight gives the largest value.'),
4:(1.5,'Geometry','A fixed base and height allow infinitely many apex positions and noncongruent triangles.'),
5:(1,'Algebra','The total of the column sums minus the three known row sums is the missing row sum.'),
6:(1,'Algebra','Only the inequality whose variable cancels is strict for every real input; zero or a negative input rejects the others.'),
7:(1.5,'Geometry','Pythagoras and a difference of squares reduce the missing side to a direct square root.'),
8:(2.5,'Number Theory','An integer interior angle is equivalent to the side count dividing 360; count its divisors and exclude one and two.'),
9:(2.5,'Combinatorics','The containment and empty triple intersection reduce inclusion-exclusion to a single linear equation for the common ratio.'),
10:(3.5,'Geometry','Put the midpoint at fixed coordinates; perpendicular slopes make the two variable triangular areas cancel, leaving area one.'),
11:(2.5,'Number Theory','Express all coin counts using the number of ten-rupee coins; parity and the lower bound on two-rupee coins select the minimum.'),
12:(2,'Number Theory','The smallest four-digit power of eleven is 1331, and a digit-sum check chooses the smallest admissible outer digits.'),
14:(2,'Combinatorics','Subtract the one- and two-digit blocks, then locate the required position in the three-digit block.'),
15:(1.5,'Algebra','The smallest-triangle count is a power of four, so the sum of successive counts determines the index immediately.'),
17:(1.5,'Number Theory','Equality of the two repeated-fraction sums makes their term counts multiples of three and five; the given interval selects their common multiplier.'),
18:(3.5,'Algebra','Factoring the recurrence shows each move negates the previous term or adds one; an inductive interval bound is attained by adding until the last negation.'),
20:(2.5,'Geometry','On either side of the dividing cevian, equal subsegments give equal-area strips, so the alternating shaded total is always one half.'),
21:(2.5,'Combinatorics','After two tails the game restarts; the one-step probability recurrence gives two thirds.'),
22:(3.5,'Combinatorics','The first row and first column are free, and odd parity then uniquely determines every other cell.'),
23:(3,'Number Theory','Replacing two integers by their difference preserves the parity of the total sum, which starts odd.'),
24:(2.5,'Number Theory','Subtracting two allowed sums shows all entries have one common residue; a nonzero common residue supplies a counterexample to the stronger claims.'),
25:(3.5,'Combinatorics','Usually every digit must be zero or five; the exceptional numbers with only one nonzero digit must be counted separately because leading zeros are forbidden.'),
26:(1.5,'Combinatorics','Check the five possible culprits; exactly one true statement occurs only when Kanchana is responsible.'),
27:(3.5,'Combinatorics','The appearance counts give nineteen games; a player cannot miss consecutive games, and nine appearances force Sarath to play precisely the even-numbered games.'),
28:(3.5,'Number Theory','Replace the binary digits of the index by ternary place values, preserving order; 100 in binary gives ternary value 981.'),
29:(3.5,'Number Theory','Five and seven divisors force prime fourth and sixth powers; the exponent divisibility leaves a=3 and b=4.')}
def sl(n,d,t,r,s='',sol=''):write('Sri Lanka',2018,'Sri Lankan Mathematics Competition (SLMC)','National',n,d,t,r,s,sol,u)
for n,(d,t,r) in simple.items():sl(n,d,t,r)
sl(13,4,'Combinatorics','A sequential strategy gives six tests, while the eighteen matchings remaining after a failed first test cannot be distinguished by four binary answers.',r'''There are four keys and four locks. Each key fits exactly one lock, and different keys fit different locks. In the worst case, what is the minimum number of tests needed to identify all four matches?''',r'''Six tests suffice: try a chosen key in at most three locks, inferring its match if all three fail. Repeat with the three remaining keys and locks, using at most two tests, and then at most one test for the last two. The total is $3+2+1=6$.

Five cannot always suffice. Initially there are $4!=24$ possible matchings. Any first test succeeds for $3!=6$ of them and fails for the other $18$. If it fails, four further yes/no tests have at most $2^4=16$ outcome patterns, so they cannot distinguish all $18$ remaining matchings. Thus the worst-case minimum is $6$.''')
sl(16,4.5,'Combinatorics','Choose the two directions and the positive side lengths of a parallelogram, then count translations inside a triangular grid using a stars-and-bars sum.',r'''An equilateral triangle is divided into the regular triangular grid with eight unit segments on each side. How many parallelograms have all their sides on grid lines and lie inside the triangle?''',r'''There are three choices for the pair of grid directions forming the sides. By symmetry they give equal counts. Fix one pair, and let the side lengths in unit steps be positive integers $a,b$, with $a+b\le8$.

The number of possible translations is
$$\frac{(9-a-b)(10-a-b)}2=\binom{10-a-b}{2}.$$
Indeed, in coordinates along the two directions, the lower vertex has nonnegative integer coordinates whose sum is at most $8-a-b$.

Summing over $a,b\ge1$ counts nonnegative integer solutions of $a'+b'+i+j+k=6$, where $a'=a-1$, $b'=b-1$ and $k$ is unused space. By stars and bars, this is $\binom{10}{4}=210$. Multiply by three to obtain $630$.''')
sl(19,4.5,'Combinatorics','The nontrivial case uses strategy stealing: removing just the opposite corner lets the first player reproduce any allegedly winning reply from the original rectangle.',r'''A rectangular $x\times y$ chocolate bar consists of unit squares; only the bottom-left square is bitter. A move chooses a remaining square and removes it together with all remaining squares above and to its right. The player who must eat the bitter square loses. Determine which player has a winning strategy when $(x,y)\ne(1,1)$.''',r'''The first player always has a winning strategy. If one dimension is one, eat every square except the bitter one in a single move.

Now suppose both dimensions exceed one. Consider the move that removes only the upper-right square. If it leaves a losing position for the next player, it is a winning first move. Otherwise the next player has a move to a losing position. That reply removes a northeast rectangle, which would also have removed the upper-right square had it still been present. The first player can therefore make this reply directly on the original full bar, reaching exactly the same losing position. In either case the first player has a winning move. The argument uses the fact that this finite game has no draws.''')
sl(30,4.5,'Geometry','Decompose the star into its central pentagon and five isosceles spikes; pentagon similarity and elementary trigonometry express the area ratio in the stated side ratio.',r'''Extend the sides of a regular pentagon $PQRST$ to form a regular five-pointed star with tips $A,B,C,D,E$, where $A$ is opposite the inner side $TP$ and $A,P,Q,C$ are collinear. If $AP:PQ=m:1$, find the ratio of the area of the whole star to the area of its central pentagon.''',r'''Scale so every inner-pentagon side is $1$. Each spike, such as $APT$, has equal sides $m$ and apex angle $36^\circ$, hence area $m^2\sin36^\circ/2$. The pentagon has area $5\cot36^\circ/4$. Thus the desired ratio is
$$1+\frac{2m^2\sin^2 36^\circ}{\cos36^\circ}.$$
The standard pentagon similarity gives $m^2=m+1$ and $m=2\cos36^\circ$. For completeness, the latter also follows from $1=2m\sin18^\circ$ in a spike and $2\cos36^\circ$ being the positive root of $t^2-t-1=0$, obtained from $\cos108^\circ=-\cos72^\circ$.

Consequently $\sin^2 36^\circ=(3-m)/4$, and the area ratio becomes
$$1+m(3-m)=2m=\frac{6m+2}{m+2}.$$
So the ratio is $(6m+2):(m+2)$, equivalently $2m:1$.''')
(P/'reviews.json').write_text(json.dumps(rev,ensure_ascii=False,indent=2));(P/'manifest.json').write_text(json.dumps(man,ensure_ascii=False,indent=2))
print('Israel: 7 assessed, 3 included. Sri Lanka: 30 assessed, 4 included.')
