import json
from pathlib import Path
p=Path(__file__).parent
r=json.loads((p/'reviews.json').read_text())
def update(slug,**kw):
 x=r[slug];x.pop('quarantine',None);x.update(kw)
update('deu_2022_923967',difficulty=5,topic='Combinatorics',tags=['Extremal arguments','Induction','Geometric progression'],subtopics=['Extremal arguments','Induction'],
 reason='Ordering the set and fixing its largest element turns the forbidden triple condition into geometric growth of successive gaps; four iterations supply a factor 81/16 greater than 5.',
 statement=r'Let $m$ be a positive integer and let $A$ contain $4m+2$ distinct integers from $0$ to $5^m$, inclusive. Prove that some $a<b<c$ in $A$ satisfy $c+2a>3b$.',
 solution=r'Write the elements as $x_0<\cdots<x_{4m+1}$ and put $c=x_{4m+1}$. If the claimed triple does not exist, then $c+2x_i\le3x_{i+1}$ for $0\le i\le4m-1$. Hence $c-x_i\ge\tfrac32(c-x_{i+1})$. Iterating gives $$c-x_0\ge(\tfrac32)^{4m}(c-x_{4m})\ge(81/16)^m>5^m,$$ contradicting $0\le x_0<c\le5^m$.',
 sourceUrl='https://www.mathe-wettbewerbe.de/fileadmin/Mathe-Wettbewerbe/AIMO/Aufgaben_und_Loesungen_AIMO/2022_IMO_Auswahlklausuren_HP.pdf',
 solutionUrl='https://www.mathe-wettbewerbe.de/fileadmin/Mathe-Wettbewerbe/AIMO/Aufgaben_und_Loesungen_AIMO/2022_IMO_Auswahlklausuren_Lsg_HP.pdf#page=5',
 notes='The separate official question paper confirms 4m+2. The earlier MathNet 4m+1 transcription is incorrect; the solution PDF clips the end of the statement line.',sourceName='Bundesweite Mathematik-Wettbewerbe — official 2022 selection papers',solutionKind='original-exposition',license='Original contest rights retained; English paraphrase and original exposition.')
update('ita_2024_7e473a',difficulty=4,topic='Geometry',tags=['Tangential quadrilaterals','Area','Homothety'],subtopics=['Quadrilaterals & polygons','Circles & tangency','Area & dissection','Transformations'],
 reason='Recognising the converse of Pitot establishes an incircle; the boundary strip is then handled by a homothety of ratio 2/3 and area scaling.',
 statement=r'A convex quadrilateral has consecutive side lengths $14,24,26,16$ and area $360$. Find the area of the part inside it whose distance from its boundary is at most $3$.',
 solution=r'The opposite side sums are both $40$. By the converse of Pitot\'s theorem for convex quadrilaterals, there is an incircle. If its radius is $r$, splitting the quadrilateral into four triangles from its centre gives $360=40r$, so $r=9$. The points whose distance from every side is at least $3$ form a quadrilateral homothetic about that centre with ratio $(9-3)/9=2/3$. Its area is $360(2/3)^2=160$. The requested area is therefore $360-160=\boxed{200}$.',
 notes='The formerly questioned tangency inference is the valid converse of Pitot for convex quadrilaterals; verified against the official solution and the theorem stated in Das, Juyal and Moody, A Note on Tangential Quadrilaterals (NIST publication 957078).',
 solutionUrl='https://olimpiadi.dm.unibo.it/wp-content/uploads/2024/02/soluzioni2024.pdf#page=14',solutionKind='original-exposition',license='Original contest rights retained; English paraphrase and original exposition.')
update('bgr_2024_769b65',difficulty=5.5,topic='Number Theory',tags=['GCD','Primes','Perfect powers','Factorisation'],subtopics=['Divisibility & GCD','Primes','Squares & powers'],
 reason='Removing the gcd reduces the prime quotient to d^(k−1)=p²−1; excluding every larger exponent requires factoring z^q+1 for an odd prime divisor q, beyond the partial source argument.',
 statement=r'Determine all positive integers $k$ for which positive integers $x,y$ make $x^ky/(y^2-x^2)$ a prime number.',
 solution=r'Let the prime be $p$ and write $x=du$, $y=dv$, where $\gcd(u,v)=1$ and $v>u$. For $k=1$, the equality $u v=p(v^2-u^2)$ is impossible because the denominator is coprime to $uv$ and greater than $1$. For $k\ge2$, coprimality implies $v^2-u^2\mid d^{k-1}$, and the quotient is $p=u^kv\,[d^{k-1}/(v^2-u^2)]$. Thus $u=1$, $v=p$, and $d^{k-1}=p^2-1$. Put $n=k-1$. If $n=1$, any prime $p$ gives $d=p^2-1$, so $k=2$ works. If $n$ is even, $p^2-(d^{n/2})^2=1$ is impossible. If $n>1$ is odd, choose an odd prime $q\mid n$ and put $z=d^{n/q}\ge2$. Then $$p^2=z^q+1=(z+1)(z^{q-1}-z^{q-2}+\cdots-z+1).$$ Both factors exceed $1$, so both equal $p$, and the second equals $z+1$. For $q=3$ this forces $z=2$; for $q\ge5$ the alternating sum is strictly larger than $z+1$ (group its leading terms into positive pairs, with the final $z^2-z+1$). Therefore $d=2,n=3,p=3$. This gives $k=4$, attained by $(x,y)=(2,6)$. Exactly $\boxed{k=2,4}$ work.',
 sourceUrl='https://mathnet.mit.edu/explorer.html?p=bgr_2024_769b65',solutionUrl='https://mathnet.mit.edu/explorer.html?p=bgr_2024_769b65',solutionKind='original-exposition',notes='The final exclusion of k>4 has been supplied and independently checked; the source transcription stops after exhibiting k=4.')
# A complete, explicit Hamilton cycle replaces the missing construction diagram.
path=json.loads((p/'king_construct.json').read_text())['path']
assert len(path)==64 and len(set(map(tuple,path)))==64
D=lambda a:(2*a[0]-7)**2+(2*a[1]-7)**2
edges=list(zip(path,path[1:]+path[:1]))
assert all(max(abs(a[0]-b[0]),abs(a[1]-b[1]))==1 for a,b in edges)
assert sum(D(b)<D(a) for a,b in edges)==44
cycle='; '.join('('+str(a+1)+','+str(b+1)+')' for a,b in path)
update('rus_2025_cd1fbb',difficulty=6.5,topic='Combinatorics',tags=['Hamilton cycles','Extremal counting','Grid'],subtopics=['Graph theory','Extremal arguments','Combinatorial geometry'],
 reason='The sharp bound separates three disjoint classes of unavoidable non-decreasing moves by distance layers; attaining it requires a globally consistent Hamilton cycle.',
 statement=r'A king makes a closed tour of an $8\times8$ board, visiting each square exactly once before returning to the starting square on move $64$. A move is pleasant when the distance from the occupied square\'s centre to the board\'s centre decreases. What is the largest possible number of pleasant moves?',
 solution=r'The maximum is $\boxed{44}$. Index squares by $(i,j)$ with $1\le i,j\le8$, and compare the squared-distance labels $D=(2i-9)^2+(2j-9)^2$. There are four squares of label $2$, eight of label $10$, thirty-two with label at least $50$, and twenty with label greater than $50$. All four moves leaving label $2$ are non-pleasant. At least four of the eight moves leaving label $10$ are non-pleasant, since only the four label-$2$ squares can be pleasant destinations. At least twelve moves entering the thirty-two squares of label at least $50$ are non-pleasant, since a pleasant such move must leave one of the twenty squares with larger label. These last moves do not leave labels $2$ or $10$: one king move from those squares has label at most $34$. Thus at least $4+4+12=20$ of the $64$ moves are non-pleasant.\n\nFor attainment, follow this explicit list of squares in order and return to its first entry: $'+cycle+r'$. Each square occurs once, successive squares (including last to first) are king-adjacent, and direct comparison of the labels gives $44$ decreases.',
 notes='An explicit 64-square traversal was constructed and its uniqueness, adjacency and 44 distance decreases checked independently. This resolves the original diagram-only construction.',solutionKind='original-exposition',license='Original competition rights retained; concise English paraphrase and original exposition.')
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
