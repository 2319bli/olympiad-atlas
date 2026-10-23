import json
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text())
def a(s,n,t,tags,reason,**kw):r['nld_2025_'+s]={'difficulty':n,'topic':t,'tags':tags,'reason':reason,**kw}
a('9177a5',3.5,'Number Theory',['Digit sums','Modular arithmetic'],'The cyclic-digit identity gives a multiple of11111; a second congruence modulo9 and the five-digit bound force equality.')
a('3dd376',5,'Combinatorics',['Induction','Signed sums'],'A useful inductive reduction combines the last two entries into their difference, with a separate equal-entry case and parity preserved throughout.')
a('3ad952',6.5,'Combinatorics',['Graph theory','Symmetry'],'The difficult step is reconstructing the labelled graph from common-neighbour counts: one fixed vertex forces a particular neighbour and then a vertex two positions away.')
a('bdca63',6.5,'Geometry',['Cyclic quadrilaterals','Concurrency'],'A carefully chosen second circle intersection serves as the concurrence point; three collinearities require two linked cyclic quadrilaterals and several angle comparisons.')
a('ee41ad',5.5,'Number Theory',['Prime factors','Modular arithmetic','Induction'],'Classify odd exponents using orders modulo3,5,7 and an obstruction modulo16; then descend through factorisation for even exponents.')
a('29b1cb',5.5,'Algebra',['Recurrences','Conjugate surds'],'Shift and rescale to an integral homogeneous recurrence, then use conjugate units to prove the non-obvious doubling identity x₂ₙ=2xₙ²−1.',solution=r'''Put $x_n=4y_n+2$. Then $x_0=1$, $x_1=2$ and $x_{n+1}=4x_n-x_{n-1}$, so every $x_n$ is an integer. Induction also shows $x_n>0$.

Writing $u=2+\sqrt3$ and $v=2-\sqrt3$, the sequence $(u^n+v^n)/2$ has these same first two terms and recurrence. Therefore $x_n=(u^n+v^n)/2$. Since $uv=1$, we get $x_{2n}=2x_n^2-1$. Consequently
$$2y_{2n}+\frac32=\frac{x_{2n}+1}{2}=x_n^2,$$
a positive integral square.''',notes='The transcription’s intermediate subscript typo is corrected in this independently checked solution.')
a('830db5',3,'Number Theory',['Quadratic residues','Digits'],'An alternating digit sum modulo11 is always8, which is not a quadratic residue; one well-chosen modulus finishes the question.')
a('7b381d',4.5,'Geometry',['Cyclic quadrilaterals','Angle chasing'],'Find an extra cyclic quadrilateral CBFD from the two supplied circles, then transfer the required angle through it.')
a('93f791',5.5,'Number Theory',['Diophantine equations','Primes','Factorisation'],'Factoring y²−x² exposes p as a divisor of one linear factor; tight bounds force the quotient and a parity case yields the unique triple.')
a('951e3a',7,'Number Theory',['Functional equations','Consecutive squares','Primes'],'After fixing f(1), prime values2k+1 force infinitely many fixed points; two separate growing square-gap arguments then rigidify the whole function.')
a('c55d08',6.5,'Number Theory',['Pythagorean triples','Constructive proof','Induction'],'The construction must add two vertices while preserving every square-sum edge and distinctness; a prime-controlled scaling of a Pythagorean triple achieves both.')
a('dec6e4',6.5,'Geometry',['Orthocentre','Circle centres','Midpoints'],'Reflection of the orthocentre identifies the auxiliary circle’s centre; two midpoint-line arguments then locate the original circumcentre on the desired line.')
a('ad0704',7.5,'Combinatorics',['Tilings','Parity','Graph theory'],'The lower bound requires the non-obvious medial-path graph of a triangulation, while extremal constructions must be handled separately; this lies just above the chosen band.')
a('fa202e',8,'Geometry',['Reflections','Shortest paths','Similarity'],'After unfolding the path, a second substantial angle-bisector/rhombus argument is needed to identify a hidden similar triangle; above the target band.')
a('a76dcf',7.5,'Number Theory',['Binomial coefficients','Valuations'],'Classifying all n requires delicate2-adic valuation counts or a cyclic-orbit recurrence plus the exceptional powers of2; above accessible BMO2 here.')
a('c909ef',8,'Combinatorics',['Sequences','Extremal problems','Construction'],'The monotonic-window lower bound is only half the problem; a carefully designed recursively split decreasing sequence is needed for equality.')
a('fe3206',6.5,'Combinatorics',['Games','Modular arithmetic'],'Same mathematical game as Austrian2024 final problem15; reviewed once and retained as an additional contest appearance.',duplicateOf='aut_2024_d3d84a')
# Translations of the same fully inspected mathematical questions, not additional bank questions.
for dup,main in {'0f8e5f':'bdca63','0facd5':'7b381d','393901':'ee41ad','3fc111':'29b1cb','44e4bd':'93f791','4807b0':'dec6e4','4ca37f':'9177a5','55d779':'3dd376','5a78e9':'3ad952','6c41c1':'830db5','cf84ec':'c55d08','d37253':'fa202e','fa2053':'951e3a','aaf48e':'ad0704'}.items():
 rr=r['nld_2025_'+main];r['nld_2025_'+dup]={**rr,'duplicateOf':'nld_2025_'+main,'reason':'Dutch-language duplicate of the individually assessed record nld_2025_'+main+'.'}
for key,rr in r.items():
 if not key.startswith('nld_2025'):continue
 rr['sourceUrl']='https://wiskundeolympiade.nl/phocadownload/jaarverslagen/DMO63-2024-2025.pdf'
 rr['solutionUrl']=rr['sourceUrl']
 if key[-6:] in ['9177a5','3dd376','3ad952','bdca63','ee41ad','0f8e5f','393901','4ca37f','55d779','5a78e9']:rr['section']='BxMO/EGMO Team Selection Test, March 2025';rr['competition']='Dutch Team Selection Tests'
 elif key[-6:] in ['29b1cb','3fc111','a76dcf','aaf48e','ad0704','d37253','fa202e']:rr['section']='IMO selection test I, 28 May 2025'
 elif key[-6:] in ['830db5','6c41c1','dec6e4','4807b0','951e3a','fa2053','fe3206']:rr['section']='IMO selection test II, 29 May 2025'
 else:rr['section']='IMO selection test III, 30 May 2025'
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
