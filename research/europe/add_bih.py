import json
from pathlib import Path
p=Path(__file__).parent;r=json.loads((p/'reviews.json').read_text())
gids={2011:31,2013:71,2014:80,2015:96}
rows={
2011:[
(3.5,'Geometry','Angle-bisector ratios produce two isosceles triangles and identify the incenter on a perpendicular bisector.',None,3),
(4,'Geometry','A double-angle identity gives d squared minus bd equals twice a squared; divisibility eliminates smaller diameters.',r'Points $C,D$ lie in that order from $B$ to $A$ on a semicircle of diameter $AB=d$. If $BC=CD=a$ and $DA=b$, where $a,b,d$ are distinct positive integers, find the least $d$.',5),
(4,'Combinatorics','Show that the smaller member of every opposite-order pair comes from the lower half; their total is fixed.',r'Partition $1,2,\ldots,2n$ into sequences $a_1<\cdots<a_n$ and $b_1>\cdots>b_n$. Prove that $\sum_{i=1}^n|a_i-b_i|$ is a square.',7),
(4,'Combinatorics','Removing the smallest entry sharpens the averaging bound; an explicit cyclic arrangement attains it.',r'Arrange $1,\ldots,10$ around a circle. Find the largest $a$ for which every arrangement has three consecutive entries whose sum is at least $a$.',9),
(2.5,'Algebra','Apply three-term AM-GM to each cube root; the weighted linear corrections cancel.',None,10),
(5.5,'Geometry','Two Menelaus relations combine with sine-rule identities; equal sums of angles leave cyclicity or the excluded parallel case.',r'In convex $ABCD$, assume $AD\not\parallel BC$ and put $E=AC\cap BD$. Choose $F\in AB,G\in DC$ with $AF/FB=DG/GC=AD/BC$. If $E,F,G$ are collinear, prove $ABCD$ cyclic.',11)],
2013:[
(4.5,'Geometry','Angle chasing makes each midpoint equidistant from the altitude endpoints, placing both on one perpendicular bisector.',r'In right triangle $ABC$, $\angle C=90^\circ$. The internal bisectors $AM,BN$ meet the opposite legs at $M,N$. The altitude $CH$ meets $AM,BN$ at $P,Q$. Prove that the line through the midpoints of $PM,QN$ is parallel to $AB$.',3),
(5,'Algebra','Guess a recurrence for the square roots; its quadratic invariant verifies the original inhomogeneous recurrence.',r'Let $a_0=a_1=1$ and $a_{n+1}=14a_n-a_{n-1}-4$ for $n\ge1$. Prove every $a_n$ is an integer square.',4),
(5.5,'Combinatorics','Strengthen the claim to unequal clique sizes and induct using Pascal’s identity.',r'Among $\binom{2n}{n}$ people, prove that $n+1$ are pairwise acquainted or $n+1$ are pairwise unacquainted. Acquaintance is mutual.',5),
(5,'Number theory','Combine the prime divisibilities; a multiplier coprime to thirty either factors a fixed product or bounds the smaller prime.',r'Find all primes $p,q$ satisfying $p\mid30q-1$ and $q\mid30p-1$.',6),
(4.5,'Algebra','Complementary cyclic pairs turn the five-variable case into a useful Cauchy bound.',r'For $x_i\ge0$ with $\sum_{i=1}^n x_i=1$, put $F_n=\sum x_i^2-2\sum x_ix_{i+1}$, where $x_{n+1}=x_1$. Prove $\min F_3=-1/3$, $\min F_4=-1/4$, and $\min F_5=-1/5$.',7),
(6,'Geometry','Reciprocal distances create cyclic quadrilaterals and an orthocentre; inversion or a circle equation locates the new circumcentre.',r'Let $I,O$ be the incenter and circumcentre of $ABC$. Points $P,Q,R$ lie on $IA,IB,IC$ and satisfy $IP\cdot IA=IQ\cdot IB=IR\cdot IC>0$. Prove that the Euler line of $PQR$ contains $I$ and $O$.',8)],
2014:[
(3,'Geometry','Two diameter circles and the tangent-chord theorem give directly similar right-foot triangles.',None,2),
(4.5,'Algebra','Two cyclic rational identities supply different lower bounds for two sums of squares.',r'For distinct real $a,b,c$, define $U_\pm(a,b)=(1\pm ab)/(a-b)$. Evaluate $\sum_{\rm cyc}U_\pm(a,b)U_\pm(b,c)$, then prove $$\sum_{\rm cyc}\frac{1+a^2b^2}{(a-b)^2}\ge\frac32$$ and determine whether equality is attainable.',2),
(5.5,'Number theory','Parity reduces the exponents; a modulo-125 restriction creates a fixed divisor with a prime factor other than five.',r'Find all nonnegative integers $x,y$ such that $7^x-2\cdot5^y=-1$.',2),
(2.5,'Algebra','Taking reciprocals gives an arithmetic sum, and the resulting reciprocal products telescope.',None,3),
(3,'Combinatorics','Count valid vertex pairs at a fixed vertex, subtract adjacent pairs, then divide by three.',None,3),
(5.5,'Geometry','The bisector-length identity forces a sixty-degree angle; reflection in that bisector and the circumradius identify congruent triangles.',r'In $ABC$, let $AD,BE$ be altitudes, $CF$ the internal angle bisector, and $O,I,H$ the circumcentre, incenter and orthocentre. If $CF/AD+CF/BE=2$, prove $OI=IH$.',3)],
2015:[
(2.5,'Algebra','Partial fractions and two reciprocal-sum inequalities give the minimum two.',None,8),
(6.5,'Geometry','Identify a new circle centre, add a diameter, and use two power identities to place the final point on that circle.',r'Let $D\in AB$ in triangle $ABC$. Circles $(BCD),(ACD)$ meet $AC,BC$ again at $E,F$. The perpendicular bisector of $EF$ meets $AB$ at $M$ and the perpendicular to $AB$ through $D$ at $N$. Put $T=AB\cap EF$ and let $U$ be the second intersection of $TC$ with $(CDM)$. Prove $NC=NU$. Assume the construction is nondegenerate.',8),
(6,'Number theory','Choose an exponential family whose exponent divides its value minus one; repeated squaring supplies both divisibility and compositeness.',r'Prove that infinitely many composite positive integers $n$ satisfy $n\mid3^{n-1}-2^{n-1}$.',9),
(4.5,'Number theory','Expand around the smallest entry; Cauchy and a short parity-controlled case analysis force equal sums.',r'Partition eight consecutive positive integers into two four-element sets. If their sums of squares agree, prove their sums agree.',10),
(4,'Combinatorics','An extremal subset sum can always be increased by one unless it is already half the total.',r'A finite multiset contains each weight $1,\ldots,N$ at least once and no other weights. Its total is even. Prove it splits into two equal-weight parts.',11),
(5.5,'Geometry','An auxiliary intersection with the incircle creates a midline; two power identities finish the parallelism.',r'The incircle of $ABC$, centred at $I$, touches $BC,CA,AB$ at $D,E,F$. Let $P$ be the foot from $I$ to $AD$, and $M$ the midpoint of $DE$. If $N=PM\cap AC$, prove $DN\parallel EF$.',12)]}
for y,rr in rows.items():
 src=f'https://www.umtk.info/index.php?option=com_docman&task=doc_download&gid={gids[y]}&Itemid=2'
 for k,(v,t,why,st,page) in enumerate(rr,1):
  n=k if y!=2011 or k<=3 else k-3;slug=f'bih_{y}_{k}';section='National Olympiad — Day '+('1' if k<=3 else '2')
  (p/(slug+'.json')).write_text(json.dumps({'country':'Bosnia and Herzegovina','competition':'Bosnia and Herzegovina Mathematical Olympiad','year':y,'section':section,'problem_number':str(n),'problem_markdown':st or 'See the official paper for the full statement.','solutions_markdown':[]},ensure_ascii=False,indent=2))
  su=src+f'#page={page}';sol='[Official worked solution, archived by the Tuzla Mathematical Association (umtk.info)]('+su+').';kind='source-link';notes='Day 2 numbering follows the original paper (1–3).' if y==2011 and k>3 else ''
  if (y,k)==(2013,2):
   sol=r'Define integers $b_0=b_1=1$ and $b_{n+1}=4b_n-b_{n-1}$. The expression $b_n^2+b_{n-1}^2-4b_nb_{n-1}$ is unchanged when $(b_{n-1},b_n)$ is replaced by $(b_n,b_{n+1})$, so it always equals $-2$. Consequently $$b_{n+1}^2=14b_n^2-b_{n-1}^2-4.$$ The sequences $(b_n^2)$ and $(a_n)$ have identical initial values and recurrence. Thus $a_n=b_n^2$ for every $n$.';kind='original-exposition'
  if (y,k)==(2013,6):
   sol=r'Write the common product as $k$. Similar triangles from $IP\cdot IA=IQ\cdot IB$ give cyclic $ABQP$; similarly $BCRQ$ and $ACRP$ are cyclic. The resulting angles are $\angle RPQ=90^\circ-\angle A/2$ and its cyclic counterparts, while $\angle IPQ=\angle B/2$. Hence $PI\perp QR$, and cyclically, so $I$ is the orthocentre of $PQR$. To locate its circumcentre, take $I$ as vector origin and write $o$ for the vector of $O$, $R_0$ for the circumradius of $ABC$. Its circle equation is $x\cdot x-2o\cdot x+c=0$, where $c=OI^2-R_0^2\ne0$. Under $p=kx/(x\cdot x)$ it becomes $$p\cdot p-2(k/c)o\cdot p+k^2/c=0.$$ Thus the circumcentre $S$ of $PQR$ has vector $(k/c)o$, and $S,I,O$ are collinear. Since $I$ is its orthocentre, this is the required Euler-line assertion. In the equilateral case all relevant centres coincide.';kind='original-exposition';notes='The equal-centre equilateral case is interpreted as the limiting Euler-line assertion. The exposition includes a circle-equation proof of the centre collinearity.'
  if (y,k)==(2015,2):notes='In the source solution, the first cyclic quadrilaterals should read BCDE and ACDF; the following complementary angle is 90 degrees minus angle C. These are label slips, and the geometric argument was checked with the corrected labels.'
  r[slug]={'difficulty':v,'topic':t,'tags':[],'reason':why,'number':str(n),'sourceUrl':src,'solutionUrl':su,'solutionKind':kind,'solution':sol,'sourceName':'Tuzla Mathematical Association — official national olympiad bulletin (umtk.info)','license':'Original competition rights retained. Concise English mathematical paraphrase; official exposition linked with archive attribution.','notes':notes}
(p/'reviews.json').write_text(json.dumps(r,ensure_ascii=False,indent=2))
q=p/'coverage_inventory.py';s=q.read_text().replace("if c=='Montenegro':return nums(1,4)","if c=='Montenegro':return nums(1,4)\n if c=='Bosnia and Herzegovina':return nums(1,3) if y==2011 or 'Day 1' in s else nums(4,6)")
s=s.replace("'status':'Official archive located but public retrieval returned 403/404; no national questions assessed yet.'","'status':'The Sarajevo archive intermittently fails retrieval. The Tuzla Mathematical Association archive supplied complete national papers and solutions for 2011, 2013, 2014 and 2015; other years remain pending.'")
q.write_text(s)
