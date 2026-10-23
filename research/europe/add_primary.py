import json
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text())
def add(id,country,comp,year,section,num,statement,diff,topic,tags,reason,url,page=None,duplicate=None):
 d={'country':country,'competition':comp,'year':year,'section':section,'problem_number':str(num),'problem_markdown':statement,'solutions_markdown':[],'booklet_title':comp+' '+str(year),'booklet_organization':'Official competition archive'}
 (p/(id+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2))
 link=url+(('#page='+str(page)) if page else '')
 r[id]={'difficulty':diff,'topic':topic,'tags':tags,'reason':reason,'sourceUrl':url,'solutionUrl':link,'sourceName':'Official competition archive','solutionKind':'source-link','solution':'[Official worked solution]('+link+').','license':'Original competition rights retained; concise mathematical paraphrase.'}
 if duplicate:r[id]['duplicateOf']=duplicate
u='https://komal.hu/oldal?lap=KurschakBeszamolo2025'
add('hun_2025_kurschak_1','Hungary','Kürschák Mathematical Competition',2025,'National competition, 10 October',1,r'Arrange $0,1,\ldots,n-1$ in a row. Call $k$ special if exactly $k$ other entries form inversions with it. What is the greatest possible number of special entries?',4,'Combinatorics',['permutations','parity','extremal construction'],'A parity restriction on positions must be matched by a construction.',u)
add('hun_2025_kurschak_2','Hungary','Kürschák Mathematical Competition',2025,'National competition, 10 October',2,r'Leading zeroes are allowed. Prove that the number of positive $2n$-digit decimal strings whose value equals the square of the sum of their two $n$-digit halves is a power of $2$.',5.5,'Number theory',['Chinese remainder theorem','digits','bijections'],'Find the idempotent congruence and prove the counting bijection.',u)
add('hun_2025_kurschak_3','Hungary','Kürschák Mathematical Competition',2025,'National competition, 10 October',3,'',7.5,'Combinatorics',['convex hulls','colouring'],'The minimal convex-hull hitting-set argument, or a carefully controlled recolouring, is substantially beyond the target band.',u)
u='https://www.bolyai.hu/files/Kurschak_2024_megoldasok.pdf'
add('hun_2024_kurschak_1','Hungary','Kürschák Mathematical Competition',2024,'National competition',1,r'A quadrilateral is tiled by cyclic quadrilaterals. Tile interiors are disjoint, and no tile vertex lies inside a side of another tile or of the original quadrilateral. Prove that the original quadrilateral is cyclic.',6.5,'Geometry',['planar graphs','bipartite graphs','angle sums'],'Prove bipartiteness, then compare the two colours’ total angles.',u,1)
add('hun_2024_kurschak_2','Hungary','Kürschák Mathematical Competition',2024,'National competition',2,'',8,'Combinatorics',['recursive construction','nearest neighbours'],'The upper construction uses geometric halving; the universal obstruction needs a nested median construction with controlled nearest neighbours.',u,2)
add('hun_2024_kurschak_3','Hungary','Kürschák Mathematical Competition',2024,'National competition',3,r'Let $p$ be prime and $H\subseteq\mathbb Z/p\mathbb Z$ be nonempty. For each $a\in H$, suppose there are $b,c\in H\setminus\{a\}$ with $b+c=2a$. Prove $p<4^{|H|}$.',7,'Number theory',['pigeonhole principle','modular arithmetic','dilation'],'Simultaneous modular compression by pigeonhole defeats an extremal element.',u,4)
u='https://maths-olympiques.fr/wp-content/uploads/2025/10/Corrige-Test-2-2024-2025.pdf'; comp='French Olympiad Team Selection Test'
add('fra_2025_january_1','France',comp,2025,'15 January — Junior',1,'',3,'Geometry',['angle chasing'],'Direct tangent-chord and central-angle identities establish cyclicity.',u,2)
add('fra_2025_january_2','France',comp,2025,'15 January — Junior',2,r'Find all positive integers $c$ for which $m^3-m=c!$ for some positive integer $m$, while $m^2-1$ has at most six positive divisors.',5.5,'Number theory',['divisor counting','factorials'],'Divisor restrictions lead to a prime and a factorial bound.',u,4)
add('fra_2025_january_3','France',comp,2025,'15 January — Junior',3,r'Prove that at least $51\%$ of all subsets of $\{1,\ldots,2024\}$ contain a three-term arithmetic progression of distinct elements.',4.5,'Combinatorics',['counting','complement counting'],'Count independent disjoint triples to bound the exceptional subsets.',u,6)
add('fra_2025_january_4','France',comp,2025,'15 January — Junior',4,r'For nonnegative integers $x_0,\ldots,x_n$ satisfying $\sum_{i=0}^n x_i=n$, determine the minimum of $\sum_{i=0}^n2^ix_i^2$.',5.5,'Algebra',['discrete optimization','binary valuations'],'Marginal costs enumerate distinct integers; equality needs a construction.',u,9)
add('fra_2025_january_5','France',comp,2025,'15 January — Senior',5,'',5.5,'Algebra',['discrete optimization'],'Same problem as Junior Q4.',u,12,'fra_2025_january_4')
add('fra_2025_january_6','France',comp,2025,'15 January — Senior',6,r'In convex pentagon $ABCDE$, $M$ bisects $AB$. The circle $CME$ touches $AB$ at $M$, and $D$ lies on circles $AME,BMC$. Put $K=AD\cap ME$, $L=BD\cap MC$. Points $P,Q\in CE$ satisfy $\angle PDC=\angle EDQ=\angle ADB$. Prove $KP,LQ,MD$ concur.',7,'Geometry',['cyclic quadrilaterals','parallel lines','concurrency'],'Several cyclicity steps reveal parallel lines and a midpoint.',u,16)
add('fra_2025_january_7','France',comp,2025,'15 January — Senior',7,'',8,'Combinatorics',['potential functions','adjacent swaps'],'A sharp circular swapping bound requires the nontrivial crossed/separated chord potential and a separate extremal lower bound.',u,22)
# Czech and Slovak national problems coincide: record additional appearances rather than duplicate questions.
u='https://skmo.sk/dokument.php?id=5396'
ids=['b3facd','1bb427','7cae1e','bb8f92','d36a7f','d12126']
for i,suffix in enumerate(ids,1):
 orig='cze_2025_'+suffix;v=r[orig]
 add('svk_2025_national_'+str(i),'Slovakia','Slovak Mathematical Olympiad',2025,'National round — Category A',i,'',v['difficulty'],v['topic'],v['tags'],'Shared Czech–Slovak paper; mathematical assessment matches the Czech appearance: '+v['reason'],u,None,orig)
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
