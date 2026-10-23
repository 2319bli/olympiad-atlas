"""English statements and source corrections for restored reviewed entries."""
import json
from pathlib import Path
P=Path(__file__).parent;R=json.loads((P/'reviews.json').read_text())
S={
'rou_2025_4efe32':r'Let $I$ be the set of positive perfect squares at most $2025$, and let $F$ be the set of positive multiples of $45$ at most $2025$. Find (a) $|I|$, (b) $|I\cap F|$, and (c) the number of nonnegative integers at most $2025$ belonging to neither set. In part (c), zero is included in the ambient set but belongs to neither $I$ nor $F$.',
'che_2023_selection6':r'Find all integers $n\ge2$ for which there are distinct real numbers $a_1,\ldots,a_n$ and $r>0$ satisfying $\{a_j-a_i:1\le i<j\le n\}=\{r,r^2,\ldots,r^{\binom n2}\}$.',
'che_2023_selection11':r'Let $\mathcal F$ consist of all functions $f:\mathbb R\to\mathbb R$ satisfying $f(x+f(y))=f(x)+f(y)$ for every real $x,y$. Determine the rational numbers $q$ such that every $f\in\mathcal F$ has some real $z$ with $f(z)=qz$.',
'fra_2025_january_7':r'Around a circular table sit $2n$ people, paired into $n$ pairs of brothers. A pair can shake hands whenever they occupy neighbouring seats. A move exchanges the occupants of two neighbouring seats. Find the smallest $k$, in terms of $n$, such that from every starting arrangement at most $k$ moves suffice for every pair to have shaken hands at some time during the process.',
'prt_2025_finalb_1':r'A sequence begins with $25$. From the fourth term onward, each term is the average of the preceding three. Its first six terms are positive integers, and its sixth term is $8$. Determine its fifth term.',
'prt_2025_finalb_4':r'Square $ABCD$ has side $2$ cm and centre $T$. A rhombus $ARTE$ has $E$ on line $DC$. Find its area.',
'svn_2023_0486ef':r'In a three-question contest, $90\%$, $80\%$ and $70\%$ of contestants solve the first, second and third questions, respectively. What is the least possible percentage solving all three? Choices: $30,35,40,50,70$.',
'svn_2023_082d89':r'Find the smallest positive integer $n$ such that $[(n+8)/2,(2n+14)/3]$ contains at least four positive integers. Choices: $16,17,18,19$, or none of these.',
'svn_2023_0c098f':r'Evaluate $2^{0^{2^3}}+0^{2^{3^2}}+2^{3^{2^0}}+3^{2^{0^2}}$. Choices: $3,4,7,12$, or a number greater than $100$.',
'svn_2023_16be38':r'Quadrilateral $ABCD$ has right angles at $A,C$. The perpendicular projections of $D,B$ onto segment $AC$ are $E,F$, respectively. If $AE=3$, $DE=5$ and $CE=7$, determine $BF$.',
'svn_2023_3c2a7a':r'The decimal expansion of $n$ consists of $2023$ ones. Find the digit sum of $1111n$. Choices: $8080,8083,8086,8092,8101$.',
'svn_2023_3d3276':r'In cube $ABCDEFGH$, where $AE,BF,CG,DH$ are corresponding edges, let $P$ be the centre of face $EFGH$ and $R$ the midpoint of $AB$. The plane through $C,P,R$ meets $EF,GH$ at $X,Y$. Prove $EX:XF=GY:YH=1:3$, and find the ratio of the volumes into which this plane divides the cube.',
'svn_2023_64bbf9':r'A proper divisor here means a positive divisor other than $1$ and the number itself. How many positive integers have largest proper divisor $17$? Choices: $0,1,3,5,7$.',
'svn_2023_690820':r'Mix $320$ g of an alloy containing $90\%$ gold with $160$ g of an alloy containing $54\%$ gold. What percentage of the resulting alloy is gold? Choices: $33,48,65,72,78$.',
'svn_2023_78ed1f':r'A clock divides each half-day into ten hours of one hundred minutes. At noon it reads $10.00$, while an ordinary clock reads $12.00$. What ordinary time in the morning corresponds to $8.25$ on this clock? Choices: $7.54,8.15,8.25,9.15,9.54$.',
'svn_2023_7cde01':r'Find the smallest value of $|25^m-36^n|$ for positive integers $m,n$.',
'svn_2023_7ff433':r'Sketch the region described by $|x|\le2$, $-2\le y\le4$ and $y\le x$. Find its area and perimeter.',
'svn_2023_82a64a':r'Triangle $ABC$ has $\angle ACB=32^\circ$. Points $D,E$ lie on the extensions of $AB$ beyond $A,B$, respectively, with $AD=AC$ and $BE=BC$. Find $\angle DCE$. Choices: $90^\circ,96^\circ,100^\circ,106^\circ,116^\circ$.',
'svn_2023_8ae9cc':r'Find the exact supremum of $a_n=n(20/23)^n$ over positive integers $n$.',
'svn_2023_9af862':r'Find the intersection points of $y=x^4-2x^3-7x+2$ and $y=3x^3-8x^2-1$. Determine the slope of the line through those points and the tangent of its smaller angle with $3x+2y-11=0$.',
'svn_2023_9e7091':r'A square formed by every other vertex of a regular octagon has area $2\text{ cm}^2$. Find the octagon\'s area. Choices: $1+\sqrt2,\ 5/2,\ 2\sqrt2,\ 3,\ 3\sqrt2-1$ square centimetres.',
'svn_2023_a87a13':r'Simplify $\left(\dfrac1{x^4-27x}-\dfrac1{x^4-3x^3}\right)\div\dfrac{x^{n+2}-9x^n}{x^{n+5}+3x^{n+4}+9x^{n+3}}$, for real $x\notin\{0,3,-3\}$ and positive integer $n$.',
'svn_2023_c9c438':r'A two-digit positive integer $n$ has the property that $(n+1)+(n+2)+(n+3)$ is a two-digit integer with the same two digits as $n$. How many positive divisors does $n$ have? Choices: $3,4,5,6,8$.',
'svn_2023_d77b1f':r'Circle $\mathcal K$ has diameter $AB$. Points $C,D$ on the same side of line $AB$ lie on the circle, and $BD$ bisects $\angle CBA$. Let $E=AC\cap BD$. Given $AE=169$ and $CE=119$, find $DE$.',
'svn_2023_de8ad5':r'Find all real $a\ne-1$ such that the two roots of $(2a+2)x^2+(2a+3)x+1=0$ have ratio $1:3$ in some order.',
'svn_2023_ea84c1':r'Right trapezium $ABCD$ has $AB\parallel CD$, right angles at $B,C$, and base lengths $AB=120$ mm, $CD=30$ mm. Its diagonals meet at $E$. Find the distance from $E$ to $BC$. Choices: $21,22,23,24,25$ mm.',
'svn_2023_eb35e6':r'A polynomial $6z^{10}+a_9z^9+\cdots+a_1z+9216$ has real coefficients and roots $1+i,2+2i,3+3i,4+4i,1/2$. Determine $a_9$.',
'svn_2023_fd0871':r'Triangle $ABC$ is right-angled at $A$. Points $D\in AB$, $E\in BC$, $F\in CA$ satisfy $BD=BE$ and $CF=CE$. Determine $\angle FED$. Choices: $30^\circ,37.5^\circ,45^\circ,52.5^\circ$, or a value depending on $\angle CBA$.',
'svn_2023_fec8d7':r'A circle of radius $R$ is split into three sectors. The sum of the two smaller areas equals the largest area, while their difference is one third of the largest area. Inscribe the largest possible circle in each sector. Express, in terms of $R$, the area left outside these three smaller circles.'
}
for k,s in S.items():
 R[k]['statement']=s.replace("\\'", "'")
 R[k]['notes']=(R[k].get('notes','')+' English statement checked against the source; figure information is explicit where needed.').strip()
 if k.startswith('svn') or k=='rou_2025_4efe32':R[k]['solution']='';R[k]['solutionKind']='source-link'
R['rou_2025_4efe32']['notes']+=' The official definition restricts both named sets to positive integers; part (c) additionally counts zero. This corrects the secondary English transcription.'
R['hrv_2019_6f4303']['reason']='Completing the square gives (a+b)²=b²+131−b!; factorial growth excludes b≥6 and the remaining cases give b=5 and a=1 or a=−11.'
(P/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
print('Translated or recovered',len(S))
