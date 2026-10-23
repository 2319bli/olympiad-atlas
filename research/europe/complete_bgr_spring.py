import json,re
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text())
rows=[
('695008',8,1,3,'Algebra',['Sum of squares','Factorisation'],'Rearrange into x^4+5x²(y²+1)+(2y−1)²(y+2)²=0; all terms are nonnegative, so x=0 and y is −2 or 1/2.'),
('e72111',8,2,5,'Geometry',['Angles','Cyclic quadrilaterals','Tangency'],'The radius is routine, but the second part needs tangent–chord angles in two auxiliary circles to prove N lies on BC before extracting the 36-degree angle.'),
('c90eb7',8,3,4.5,'Combinatorics',['Games','Parity','Powers of two'],'Classify odd positions and even non-powers first, then isolate powers of two and alternate their exponent parity; the exceptions 128 and 512 give 448 winning starts.'),
('efc7b0',8,4,None,'Number Theory',['Fermat cubic equation','Rationality'],'The inequality part follows from a six-term AM–GM; the rational-attainment part reduces to Fermat’s cubic equation, whose nonexistence proof is not provided and is outside the elementary source treatment.'),
('586222',9,1,2,'Algebra',['Absolute value','Inequalities'],'Split at x=1 and exclude the pole x=4; the two factored rational inequalities give (−infinity,1] union (4,7].'),
('c14e0a',9,2,4,'Geometry',['Altitude','Area','Special angles'],'An altitude creates two equal-length isosceles configurations; finding angle ACM=30 degrees permits a second area calculation of ACM.'),
('354d99',9,3,3.5,'Combinatorics',['Counting','Combinatorial geometry','Extremal arguments'],'Counting incremental regions gives 1+n+xy+yz+zx; balancing the three direction classes yields S18=127 and S19=140.'),
('d01b15',9,4,5,'Number Theory',['Modular arithmetic','Multiplicative order','Extremal arguments'],'Recover n from its residue set: its smallest element t whose double is absent is (n+1)/2, requiring the inverse of two and closure under doubling.'),
('64a458',10,1,2.5,'Algebra',['Inequalities','Cauchy–Schwarz'],'Completing squares gives (x−3)²+(y−2)²≤20; Cauchy–Schwarz bounds x+2y between −3 and 17 with attainable equality.'),
('a60c50',10,4,5,'Combinatorics',['Graph theory','Induction','Construction'],'Inductively add either an isolated large prime or a universal vertex after scaling all previous labels; the edge-count intervals overlap from n=4 onward.'),
('2e44d9',11,1,None,'Algebra',['Logarithms','Limits'],'A discriminant gives the logarithmic parameter range, while rationalising gives the limit 1/2; the question explicitly requires calculus beyond BMO prerequisites.'),
('4ec86c',11,2,5.5,'Geometry',['Menelaus','Power of a point','Cyclic quadrilaterals'],'Two Menelaus identities remove the concurrency point, and tangent–secant powers turn the resulting ratio into a cyclic quadrilateral and equal semicircles.'),
('bc27a2',11,3,6,'Number Theory',['Arithmetic functions','LCM','Primes','Bertrand postulate'],'An exponent two obstructs a power-of-two divisor count; overlapping prime intervals [p²,p³) via Bertrand reduce the infinite search to n<9.'),
('bac7b2',11,4,6,'Combinatorics',['Parity','Double counting','Colouring','Triangulations'],'Antipodal labels force an odd count of boundary edges of type {1,−2}, whereas each triangle without an opposite pair contributes an even count.'),
('802550',12,1,3,'Algebra',['Sequences','Recurrences','Divisibility'],'Linearise the fractional recurrence to a_n=4−15/(2^n+3), then compare the possible denominators with the divisors of 15.'),
('1fcf3d',12,2,4.5,'Geometry',['Sine rule','Trigonometry'],'Apply the sine rule in two subsidiary triangles, then the whole triangle; the ratio BE/CD=2 becomes sin(beta)cos(gamma)=0.'),
('65c072',12,3,7.5,'Number Theory',['Modular arithmetic','Finite differences','Perfect powers'],'Modulo 67 forces twelve summands for one infinite family; a 32-fold finite difference supplies a uniform bounded representation for every integer.'),
('385c97',12,4,6.5,'Combinatorics',['Graph theory','Matchings','Pigeonhole principle'],'Restrict attention to a vertex, its neighbours and their matched partners; either a 4-cycle appears immediately or a deterministic alternating walk closes within 2d−2 steps.')]
paraphrases={
'e72111':r'Four points $A,B,Y,C$ occur in that order on a circle with centre $O$. Suppose $BC=2$, $\angle BAY=42^\circ$, and $\angle CAY=78^\circ$. The circle through $A,O,B$ is tangent to $BY$. A circle through $A,C$, tangent to $CY$, meets it again at $N$. Determine $BO$ and $\angle YAN$.',
'c90eb7':r'The initial number on a board is a three-digit positive integer. Players alternate subtracting a divisor of the current number other than $1$ and the number itself. A player with no legal move loses. How many starting numbers let the first player force a win?',
'c14e0a':r'In triangle $ABC$, let $M$ bisect $AB$. If $\angle ABC=30^\circ$ and $\angle BCM=105^\circ$, prove $CM\cdot AC=BM\cdot BC$.',
'd01b15':r'For each odd integer $n>1$, let $S_n$ be the set of least nonnegative residues of the positive powers of $2$ modulo $n$. Can distinct odd integers $m,r>1$ satisfy $S_m=S_r$?',
'a60c50':r'A graph is a divisibility graph if its vertices can be labelled by distinct positive integers so that two vertices are adjacent exactly when one label divides the other. Prove that, for every $n\ge1$ and $0\le e\le\binom n2$, such a graph exists with $n$ vertices and $e$ edges.',
'4ec86c':r'A circle through opposite vertices $A,C$ of a parallelogram $ABCD$ meets rays $AB,AD$ again at $E,F$. The lines $BD,EF$ and the tangent to the circle at $C$ pass through one point. Show that $AC$ is a diameter.',
'bc27a2':r'For which positive integers $n$ is the number of positive divisors of $\operatorname{lcm}(1,2,\ldots,n)$ a power of two?',
'bac7b2':r'A convex $2024$-gon and $1000$ points in its interior are triangulated, with no three of the $3024$ vertices collinear. Label every vertex by one of $1,-1,2,-2$, requiring opposite polygon vertices $A_i,A_{i+1012}$ to have opposite labels. Prove that some small triangle has two vertices with opposite labels.',
'1fcf3d':r'In triangle $ABC$, points $D$ on $AC$ and $E$ on $BD$ satisfy $\angle DAE=\angle AED=\angle ABC$. Prove that $BE=2CD$ holds exactly when $\angle ACB=90^\circ$.',
'385c97':r'The vertices of the $d$-dimensional cube, where $d\ge3$, are paired along cube edges. Prove there is a cycle of length at most $2d-2$ whose edges alternate between paired and unpaired edges. (Cube vertices are binary strings of length $d$; an edge changes one digit.)'
}
sub={
'e72111':['Angles & cyclic quadrilaterals','Circles & tangency'],
'c90eb7':['Games & strategies','Parity'],
'c14e0a':['Triangle geometry','Area & dissection','Angles & cyclic quadrilaterals'],
'd01b15':['Modular arithmetic','Multiplicative order','Extremal arguments'],
'a60c50':['Graph theory','Algorithms & constructions','Induction'],
'4ec86c':['Concurrency & collinearity','Power of a point & radical axes','Angles & cyclic quadrilaterals'],
'bc27a2':['Arithmetic functions','Divisibility & GCD','Primes'],
'bac7b2':['Parity','Double counting','Colouring'],
'1fcf3d':['Trigonometry','Triangle geometry'],
'385c97':['Graph theory','Pigeonhole principle','Algorithms & constructions']}
for short,g,num,v,t,tags,why in rows:
 slug='bgr_2024_'+short
 r[slug]={'difficulty':v,'topic':t,'tags':tags,'reason':why,'section':f'Grade {g}','number':str(num),'sourceUrl':f'https://maths.bg/pms2024-{g}-{num}','solutionUrl':'https://mathnet.mit.edu/explorer.html?p='+slug,'sourceName':'Bulgarian Spring Tournament — problem archive and worked booklet transcription','notes':'Original grade and within-paper number cross-checked against the Bulgarian archive; statement paraphrased in English when included.','license':'Original contest rights retained; English paraphrase.'}
 if v is None:r[slug]['outOfScope']=True
 if short in paraphrases:r[slug]['statement']=paraphrases[short];r[slug]['subtopics']=sub[short]
 if v is not None and 4<=v<=7:
  # The checked worked source is linked precisely; do not republish the booklet proof.
  r[slug]['solution']='A complete worked solution is available at the linked source for this exact problem. '+why
  r[slug]['solutionKind']='linked-worked-solution'
# Duplicate source-language/transcription records are appearances, not new problems.
for dup,canonical in [('32b25d','695008'),('a52955','e72111'),('bf3b7a','2e44d9'),('9c74d9','4ec86c'),('55efbc','65c072')]:
 x=dict(r['bgr_2024_'+canonical]);x['duplicateOf']='bgr_2024_'+canonical;x['notes']='Duplicate transcription of the same source question.'
 if dup=='55efbc':x['notes']='Corrupted power exponents repaired by comparison with the other transcription and the original question archive.'
 r['bgr_2024_'+dup]=x
# The same residues question also appears at Grade 10, Q3.
slug='bgr_2024_spring10_3';d={'country':'Bulgaria','competition':'Bulgarian Spring Tournament','year':2024,'section':'Grade 10','problem_number':'3','problem_markdown':paraphrases['d01b15'],'solutions_markdown':[]}
(p/(slug+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2));x=dict(r['bgr_2024_d01b15']);x.update(section='Grade 10',number='3',duplicateOf='bgr_2024_d01b15',sourceUrl='https://maths.bg/pms2024-10-3');r[slug]=x
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
