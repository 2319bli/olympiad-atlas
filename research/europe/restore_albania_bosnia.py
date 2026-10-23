"""Restored English statements from the cached original national papers."""
import json
from pathlib import Path
P=Path(__file__).parent;R=json.loads((P/'reviews.json').read_text())
S={
'alb_2025_upper_1':r'Two circles have centres $O_1,O_2$, radii $1$ cm and $2$ cm, and $O_1O_2=2$ cm. They meet at $A,B$. Let $AD$ and $AE$ be their respective diameters. Segment $DO_2$ meets the first circle again at $M$, and ray $AM$ meets the second circle again at $C$, beyond $M$. Find $AC$.',
'alb_2025_upper_3':r'For positive integers $a>1$ and $b$, prove $\gcd(a-1,b)=\gcd((a^b-1)/(a-1),a-1)$.',
'alb_2025_upper_5':r'A function $f:(0,\infty)\to\mathbb R$ satisfies $f(x)+2f(1/x)=2^x+2^{1/x}$. Prove that its minimum is attained at $x=1$.',
'alb_2025_lower_1':r'Find all integer pairs $(x,y)$ satisfying $x^2+6y^2=5xy$ and $x^2+y^2=10$.',
'alb_2025_lower_2':r'A bus normally travels at constant speed $V$ km/h. One day it leaves twelve minutes late and compensates by driving the first six kilometres at $V+20$ km/h, then resumes speed $V$. Determine $V$ to the nearest kilometre per hour.',
'alb_2025_lower_3':r'Prove $\sqrt[4]5+\sqrt[3]5+\sqrt5>5$.',
'alb_2025_lower_5':r'For positive integers $a,b$, suppose $a+2b\mid a^2+2ab+4b^2$. Prove $(a+2b)^2\mid a^4+16b^4$.',
'alb_2026_upper_1':r'In acute triangle $ABC$, altitudes $CE$ to $AB$ and $BD$ to $AC$ meet at $H$. The circle with diameter $DE$ meets $AB$ again at $F$ and $AC$ again at $G$. Let $K=FG\cap AH$. Given $BC=25$ cm, $BD=20$ cm and $BE=7$ cm, find $AK$.',
'alb_2026_upper_2':r'Define $x_1=x_2=1$ and $x_{n+2}=x_n+1/x_{n+1}$ for positive integers $n$. Find $x_{2026}$.',
'alb_2026_lower_1':r'In acute triangle $ABC$, let $D$ be the midpoint of $BC$ and $E$ the foot of the altitude from $A$ to $BC$. Given $AB=12$ cm and $DE=6$ cm, prove $\angle ABC=2\angle ACB$.',
'alb_2026_lower_2':r'Find all increasing quadruples of primes $x<y<z<t$ satisfying $xy+yz+zt+tx=882$. How many are there?',
'alb_2026_lower_3':r'For $0<x,y,z<1$ with $x+y+z=2$, prove $\dfrac{x}{1-x}\dfrac{y}{1-y}\dfrac{z}{1-z}\ge8$.',
'alb_2026_lower_4':r'Solve over the real numbers, with all radicals and denominators defined, the system $\dfrac1{\sqrt{2x}}+\sqrt{2-\dfrac1{2y}}=2$, $\dfrac1{\sqrt{2y}}+\sqrt{2-\dfrac1{2x}}=2$.',
'alb_2026_lower_5':r'Two workers together finish a job in six days. If the first works alone for four days and then the second joins, they finish in seven days altogether. Assuming constant work rates, how long would each take alone?',
'bih_2011_1':r'Triangle $ABC$ satisfies $BC=(AB+AC)/2$. Let $M,N$ be the midpoints of $AB,AC$. Prove that the incentre of $ABC$ lies on the circumcircle of $AMN$.',
'bih_2011_5':r'For positive reals $a+b+c=1$, prove $a\sqrt[3]{1+b-c}+b\sqrt[3]{1+c-a}+c\sqrt[3]{1+a-b}\le1$.',
'bih_2014_1':r'Points $A,B$ on a circle are not diametrically opposite, and $C$ lies on the minor arc $AB$. Let $D,E,F$ be the perpendicular feet from $C$ to line $AB$ and the tangents at $A,B$, respectively. Prove $CD^2=CE\cdot CF$.',
'bih_2014_4':r'The sequence $(a_n)$ is given by $a_1=1/2$ and $a_m=a_{m-1}/(2ma_{m-1}+1)$ for $m>1$. Find $a_1+\cdots+a_k$ for every positive integer $k$.',
'bih_2014_5':r'A regular polygon has $n\ge6$ vertices. How many triangles with vertices among these have all three sides equal to diagonals of the polygon?',
'bih_2015_1':r'For positive reals $a,b,c$ with $a+b+c\le3$, determine the minimum of $\dfrac{a+1}{a(a+2)}+\dfrac{b+1}{b(b+2)}+\dfrac{c+1}{c(c+2)}$.'
}
for k,s in S.items():R[k]['statement']=s;R[k]['notes']=(R[k].get('notes','')+' English mathematical paraphrase checked against the official paper and worked solution.').strip()
(P/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2));print('Restored',len(S))
