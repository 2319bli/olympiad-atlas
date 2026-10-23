import json
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text())
def add(s,d,t,tags,reason,solution=None,dup=None,quarantine=False):
 id='bgr_2024_'+s;raw=json.loads((p/(id+'.json')).read_text());sec=raw.get('section') or '';num=raw['problem_number'];rnd=raw.get('competition_raw','')
 if 'Final Round' in rnd:sec='National final';num=num.split('.')[-1]
 elif 'Regional Round' in rnd:sec='Regional round — Grade 12';num=num.split('.')[-1]
 elif raw['competition']=='Bulgarian Winter Tournament':sec='Grade '+sec.split('.')[0];num=raw.get('section','').split('.')[-1]
 r[id]={'difficulty':d,'topic':t,'tags':tags,'reason':reason,'section':sec,'number':num}
 if solution:r[id]['solution']=solution
 if dup:r[id]['duplicateOf']='bgr_2024_'+dup
 if quarantine:r[id]['quarantine']=True
add('0001a6',4.5,'Geometry',['centroid','contraction'],'The centroid stays fixed; a simple vector identity shows the maximum side shrinks geometrically.',r'''Let $G$ be the centroid of $A_0B_0C_0$. The construction gives
$$A_{n+1}=\frac{B_n+2C_n}{3},\quad B_{n+1}=\frac{C_n+2A_n}{3},\quad C_{n+1}=\frac{A_n+2B_n}{3}.$$
Their sum equals $A_n+B_n+C_n$, so every triangle has centroid $G$, which is strictly inside it. Moreover
$$A_{n+1}-B_{n+1}=G-A_n.$$
If $D_n$ is the largest side length of the $n$th triangle, then $|G-A_n|\le(AB+AC)/3\le2D_n/3$. Applying this cyclically gives $D_{n+1}\le2D_n/3$. Thus the diameters tend to zero. Any point in every triangle is within $D_n$ of $G$ for every $n$, so it must be $G$.''')
add('c63f08',4.5,'Geometry',['centroid','contraction'],'Duplicate transcription of the centroid contraction problem.',dup='0001a6')
add('453e7e',3.5,'Algebra',['induction','AM-GM'],'AM-GM bounds x_n² by the preceding sum; direct induction with n/2+c completes the estimate.')
add('55a9f7',None,'Geometry',['incentres'],'No worked solution available in the recovered record; not assigned a publishable difficulty.',quarantine=True)
add('46d18a',None,'Number theory',['power sums'],'Exponent transcription is inconsistent and no solution was recovered; quarantined.',quarantine=True)
add('7f13d3',8,'Number theory',['valuations','LTE','arithmetic progressions'],'Constructing two consecutive prime valuations requires tailored multiplicative orders and several controlled exponent choices.')
add('206a10',6,'Geometry',['trigonometry','auxiliary construction'],'Translate the half-angle condition into a relation between two intersecting cevians.',r'''Write $BC=AM=s$ and $BM=CP=t$, so $AB=s+t$ and $BP=s-t$. Put $\theta=\angle ABC$, $B=(0,0)$, $A=(s+t,0)$, $M=(t,0)$, $C=s(\cos\theta,\sin\theta)$ and $P=(s-t)(\cos\theta,\sin\theta)$. The cevians meet internally, and the angle between the vectors $u=P-A$ and $v=C-M$ is $\angle AOM=\theta/2$. Their scalar product and cross-product magnitude are
$$u\cdot v=s^2+t^2-(s^2+2st-t^2)\cos\theta,\qquad |u\times v|=(s^2+t^2)\sin\theta.$$
Consequently,
$$\frac{1+\cos\theta}{\sin\theta}=\cot\frac\theta2=\frac{s^2+t^2-(s^2+2st-t^2)\cos\theta}{(s^2+t^2)\sin\theta}.$$
After cancellation, $2s(s+t)\cos\theta=0$. Hence $\theta=90^\circ$. Conversely, taking any $s>t>0$ with this right-angle configuration makes the displayed cotangent equal to $1$, so the required angle condition holds.''')
add('b9ef11',6,'Geometry',['trigonometry'],'Duplicate transcription of the final-round angle problem.',dup='206a10')
add('63b187',None,'Algebra',['functional equations'],'The candidate f(x)=1/x satisfies the equation, but completeness has not been established from the available material.',quarantine=True)
add('ecdb84',5,'Algebra',['sum of squares','periodicity'],'A sum-of-squares identity produces a fractional-linear recurrence of period three.')
r['bgr_2024_ecdb84']['statement']=json.loads((p/'bgr_2024_ecdb84.json').read_text())['problem_markdown']+'\n\nIndices are cyclic: $a_{2025}=a_1$.'
add('95f5ff',None,'Combinatorics',['extremal set systems'],'No verified sharp upper bound and construction recovered; no rating published.',quarantine=True)
add('b139aa',7.5,'Geometry',['circle tangency','spiral similarity'],'The proof needs a carefully chosen auxiliary intersection, Menelaus, power of a point and a tangency lemma.')
add('b8c162',7.5,'Geometry',['circle tangency'],'Duplicate final-round tangency problem.',dup='b139aa')
add('0185aa',3,'Number theory',['modular arithmetic'],'For primes outside 2,3,5 fourth powers agree modulo 240; checking those exceptions gives maximum 5/7.')
add('0d5bd9',2.5,'Combinatorics',['probability','symmetry'],'Pair the first 2023 tosses by symmetry; the additional fair coin splits the tie case.')
add('0f8d5c',2,'Algebra',['finite sums'],'Subtracting the sum from twice itself reduces to a geometric series.')
add('2952e6',5,'Combinatorics',['counting','divisibility'],'Count colourings with two indistinguishable balls, then solve the prime-divisibility restrictions.')
add('2dde4d',5.5,'Number theory',['infinite descent','modular arithmetic'],'Descent at 3 and 2 rules out one summand; a scaled identity supplies two.',r'''Here the parameters in a represented number are positive integers. Suppose $a^2+6ab+b^2=36^{2024}$. Modulo $3$, both $a,b$ must be divisible by $3$. Repeatedly dividing by $9$ leaves positive $u,v$ with $u^2+6uv+v^2=2^{4048}$. Remove their common powers of $2$. The remaining equation is $s^2+6st+t^2=2^{2h}$, with at least one of $s,t$ odd. Parity makes both odd, and the left side is at least $8$, so $h\ge2$. But
$$(s+3t)^2-8t^2=2^{2h}.$$
Modulo $8$, $s+3t$ is divisible by $4$. Modulo $16$, the left side is therefore $8$, a contradiction. One summand is impossible.
Finally $36=(1^2+6\cdot1\cdot1+1^2)+(3^2+6\cdot3\cdot1+1^2)$. Scale all four parameters by $6^{2023}$ to obtain two summands. The minimum is $2$.''')
r['bgr_2024_2dde4d']['statement']=r'Call an integer representable if it equals $a^2+6ab+b^2$ for positive integers $a,b$. Find the smallest number of representable integers, repetitions allowed, whose sum is $36^{2024}$.'
add('4385ef',1.5,'Algebra',['radicals','factorization'],'Recognizing the two squared radicals and factoring at a=1 gives an immediate evaluation.')
add('4b5666',6,'Geometry',['incircle','similar triangles','angle bisectors'],'Two non-obvious similarities identify the internal and external angle bisectors.')
add('57ee64',None,'Combinatorics',['polygon diagonals','extremal graphs'],'Recovered solution changes floor/ceiling conventions and omits a verified two-colour extremal construction; quarantined.',quarantine=True)
add('769b65',None,'Number theory',['perfect powers','gcd'],'Recovered proof stops after k=4 and does not exclude larger exponents; no complete assessment.',quarantine=True)
add('82ee01',6,'Number theory',['linear recurrences','reciprocal polynomials'],'Solve the recurrence, extract a double polynomial root, and show its square factor survives cancellation.')
add('95ba3c',8,'Combinatorics',['graph cuts','spanning trees'],'The sharp strengthened cut bound needs a structural vertex-removal lemma and careful induction.')
add('b7edf2',7.5,'Combinatorics',['edge colouring','connected graphs'],'A minimal-counterexample analysis of monochromatic components is substantially deeper than a direct rainbow-triangle argument.')
add('e97493',2.5,'Geometry',['Ceva theorem','similar triangles'],'Two direct similarities translate the hypothesis exactly into Ceva’s identity.')
add('f5ecdb',2,'Algebra',['progressions','radicals'],'The progression relation and a displayed factorization reduce to a quadratic.')
add('2dfc50',7.5,'Number theory',['pigeonhole principle','algebraic norms'],'Combine small modular kernel vectors, a cubic norm, irreducibility and infinitely many primes in a residue class.')
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
