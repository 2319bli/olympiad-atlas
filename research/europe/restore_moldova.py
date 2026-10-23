"""English paraphrases from the stored 2023 ANCE papers and solutions."""
import json
from pathlib import Path
P=Path(__file__).parent;R=json.loads((P/'reviews.json').read_text())
S={
'0cc3f1':r'Find all sequences of consecutive positive odd integers whose sum is $392$.',
'1dd141':r'In rectangular box $ABCDA_1B_1C_1D_1$, let $AB=a$, $BC=2a$, $AA_1=3a$. Points $M\in CC_1$, $N\in AD$ satisfy $C_1M=AN=a$. Find the angle between lines $AM$ and $NB_1$.',
'237afd':r'Square $ABCD$ has side $3$ cm. Points $M,N,P$ lie in the open sides $AB,BC,CD$, respectively. Quadrilateral $AMNP$ is a trapezium with parallel bases $MN,AP$ and perpendicular diagonals. Given $BN=1$ cm, determine its perimeter.',
'2d08c1':r'In triangle $ABC$, angle $A$ is obtuse. Write $a=BC$, $b=CA$, $c=AB$. Prove that $x^2-(a+b+c)x+b^2+c^2=0$ has two distinct real roots.',
'2fe8df':r'Positive integers $a,b,c$ satisfy $(a\sqrt{2023}+b)/(a+c\sqrt{2023})\in\mathbb Q$. Prove $a+b+c\mid a^2+b^2+c^2$.',
'382deb':r'Integers $m,n$ with $m+n\ne0$ satisfy $m+n\mid n^3$. Prove $m+n\mid2023m^4$.',
'44633a':r'Define $x_0=1$ and $x_{n+1}=x_n-x_n^2/2023$ for $n\ge0$. Prove that this sequence converges to zero.',
'5cb985':r'Acute triangle $ABC$ has $\angle BAC=60^\circ$ and $BC=a$. Let $M$ be the midpoint of $BC$, and $B_1,C_1$ the feet of the altitudes from $B,C$. Find the sum of the distances from the orthocentre of $ABC$ to the three sides of triangle $MB_1C_1$.',
'658a9a':r'A circle passes through the midpoint of one side of a square and the two vertices of the opposite side. Which is larger: the circle circumference or the square perimeter? Justify your answer.',
'7e2b80':r'Find all real parameters $a$ such that $2\left|2|x|-a^2\right|=x-a$ has exactly three real solutions.',
'a9d917':r'Real numbers $x,y,z$ have fixed sum $a$. Determine the maximum of $xy+yz+zx$ and every equality case.',
'b28f6a':r'A real polynomial $P$ satisfies $xP(x+2022)-(x+2023)P(x)=2022x-2023$ for all real $x$. Find its remainder upon division by $x^2+x$.',
'b5f7e9':r'Put $z=\tfrac12-\tfrac{\sqrt3}4+\tfrac14i$. Prove that $\sqrt3\,\operatorname{Re}(z^{2024})/\operatorname{Im}(z^{2024})$ is rational.',
'b9f7c8':r'For $x,y,z,t\in[1,3]$, find the minimum and maximum of $\dfrac{3(x+y)(z+t)}8\left(\dfrac1{xy}+\dfrac1{zt}\right)$.',
'ba034e':r'A point $H$ lies inside acute triangle $ABC$ and satisfies $AB^2+CH^2=BC^2+AH^2=AC^2+BH^2$. Prove that $H$ is its orthocentre.',
'bfcba9':r'For fixed real constants $a,b$, determine the functions $f:\mathbb R\to\mathbb R$ satisfying $f(x+a)f(x+b)=x$ for every real $x$.',
'c834fa':r'For positive $x,y,z$, prove $\dfrac{(x+y)(x+z)(y+z)}{4xyz}\ge\dfrac{x+z}{y+z}+\dfrac{y+z}{x+z}$.',
'e6fe19':r'Let $S(m)$ be the decimal digit sum of the nonnegative integer $m$. Find $S(S(S(2023^{2023})))$.',
'e7a0f3':r'Which real values of $a$ make $\sqrt{x-9}=ax+7a-3$ have exactly one real solution?',
'f6abd0':r'Solve $\cos2x-\sin2x+2\cos x+1=0$ for real $x$.',
'f713e2':r'In parallelogram $ABCD$, choose interior points $E\in BC$ and $F\in CD$ with $EB/EC=p$ and $FC/FD=q$. Put $M=AE\cap BF$ and $N=DE\cap BF$. Determine $AM/ME$ and $DN/NE$ in terms of $p,q$.',
'fc2107':r'Pyramid $VABC$ has $AB=AC=6\sqrt2$ cm and $BC=4\sqrt6$ cm. Each of $VA,VB,VC$ is $\sqrt{51}$ cm. Find the distance between the skew lines $AB,VC$.',
'grade7_1':r'A nonnegative integer $n$ and a real number $a$ satisfy $n=\left(\dfrac{a-1}{a+1517}+\dfrac{\sqrt{|a|-2023}+\sqrt{2023-|a|}}{a-2023}\right)^{2024}$, with all expressions defined. Determine the units digit of $n$.',
'grade7_2':r'Prove that from any seventeen nonnegative integers one can choose five whose sum is divisible by five.',
'grade7_3':r'In acute triangle $ABC$, the perpendicular to $AC$ through $A$ and the perpendicular to $AB$ through $B$ meet at $D$. An interior point $E$ of $AD$ satisfies $\triangle ABD\cong\triangle CAE$, with corresponding vertices in the indicated order. Given $AB=10$ cm and $EB\perp BC$, find the perimeter of $ABC$.',
'grade7_4':r'Find the positive integers $n$ having exactly four positive divisors whose sum is $2n$.',
'grade7_5':r'In triangle $ABC$, let $D$ lie in the open segment $BC$ with $AD\perp BC$. Let $E,F$ be the midpoints of $AD,CD$, respectively. If $BE\perp AF$, determine $\angle BAC$.',
'grade7_6':r'Find all three-digit perfect cubes $\overline{abc}$ whose digits satisfy $a(b+c-a)=b(a+c-b)=c(a+b-c)$.',
'grade7_7':r'Find all integer pairs $(m,n)$ satisfying $49n^2-7nm+3m=29$.',
'grade7_8':r'A positive integer $n$ and primes $p,q$ satisfy $3/\sqrt n=2/\sqrt p+1/\sqrt q$. Determine all possible values of $p+q-2n$.',
'grade8_1':r'Real numbers $p,q$ satisfy $2p^2-3p-1=0$, $q^2+3q-2=0$ and $pq\ne1$. Evaluate $(23p^4+125q^4)/(17p^4-q^4)$.',
'grade8_2':r'Write the decimal digits $20$ before the usual decimal representation of a nonnegative integer $x$, and $23$ after it. Find the smallest $x$ for which the resulting integer is divisible by $2023$.',
'grade8_3':r'In triangle $ABC$, let $D$ be the midpoint of $AC$ and $E$ an interior point of $BC$. If $\angle BEA=\angle CED$, determine $AE/DE$.',
'grade8_4':r'A $6\times7$ array contains only zeroes and ones. Its six row sums are pairwise distinct and its seven column sums are equal. Determine the first column sum.',
'grade8_5':r'Find all ordered pairs of nonnegative integers $(x,y)$ satisfying $|4x^2-4xy+y^2-3x-2y+56|+3x+2y=56$.',
'grade8_6':r'Find all ordered pairs of primes $(m,n)$ for which $2m+n$, $m+2n$ and $m+n-28$ are also prime.',
'grade8_7':r'In equilateral triangle $ABC$, points $D,E,F$ lie on the open sides $BC,CA,AB$, respectively. Suppose $DF\perp AB$ and $DE$ is the perpendicular bisector of $CF$. Determine $\angle DEF$.',
'grade8_8':r'Distribute $2020$ balls among boxes numbered $0,1,\ldots,15$, and label each ball with its box number. Relabel all balls in boxes $1,2,3$ as $0$ and move them to box $0$; relabel all balls in boxes $12,13,14$ as $15$ and move them to box $15$. The mean of the labels decreases by $1/10$. Prove that two boxes originally had numbers of balls differing by at least $34$.'
}
for suffix,s in S.items():
 k='mda_2023_'+suffix;R[k]['statement']=s;R[k]['solution']='';R[k]['solutionKind']='source-link';R[k]['notes']=(R[k].get('notes','')+' English paraphrase of the official ANCE problem; official worked solution linked.').strip()
R['mda_2023_f713e2']['notes']+=' Corrected the secondary transcription’s side BF to CD, as required by the original configuration and ratios.'
R['mda_2023_f713e2']['reason']='Affine coordinates, or Menelaus together with similar triangles, give both ratios after two linear intersection calculations.'
(P/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
print('Moldova statements restored:',len(S))
