"""Restore 28 already-assessed 2025 junior semifinal statements.

English mathematical paraphrases use the official paper's indexed text and its
matching public transcription; retained individual reviews verify the formulas.
The unrelated Q16 proof hold remains unrated.
"""
import json
from pathlib import Path
P=Path(__file__).parent;R=json.loads((P/'reviews.json').read_text())
S={
1:r'Place $1,2,\ldots,9$, each once, in a $3\times3$ array. What is the largest possible number of primes among the three row sums and three column sums?',
2:r'Triangle $ABC$ has orthocentre $H$. Given $AH=1$, $AB=15$ and $BC=18$, determine $CH$.',
3:r'Integers $m,n,k$ satisfy $4^m14^n21^k=2016$. Find $m^2+n^2+k^2$.',
4:r'Count the ordered positive-integer triples $(x,y,z)$ with $x+y+z=100$ and $13\mid x+z$.',
5:r'Two circles touch externally at $A$. A common external tangent touches them at $B,C$. If $AB=20$ and $AC=21$, determine $BC$.',
6:r'Positive integers $x,y,z$ satisfy $1/x+1/y-1/z=1$. Evaluate $x^2+y^2-z^2$.',
7:r'A geometric progression $(b_n)$ satisfies $b_1+b_{10}=9$ and $b_2+\cdots+b_9=10$. Evaluate $\dfrac{10b_2+b_1b_2+b_1^2}{b_1}$.',
8:r'The medians of triangle $ABC$ meet at $G$. If $\angle AGB=90^\circ$ and $AB=20$, determine the length of the median from $C$.',
9:r'Find the least positive integer $n$ for which the decimal representation of $25n+1$ contains an $8$ or a $9$.',
10:r'Find the absolute value of the least integer $x\ne0$ satisfying $x\ge2015/x$.',
11:r'Find the sum of the smallest and largest real roots of $4^x+64=2^{x^2-5x}$.',
12:r'Points $A,D,E,C$ are collinear in that order, with $AD=3$, $DE=5$, $EC=24$. A point $B$ satisfies $\angle ABE=\angle DBC=90^\circ$. Determine $3AB$.',
13:r'From five mathematics teachers, three physics teachers and two chemistry teachers, choose a group containing at least one teacher of every subject. How many groups are possible?',
14:r'The real numbers $a,b,c$ are consecutive terms of an arithmetic progression. So are $1/c,1/(b+1),1/(a+2)$, in that order, with all denominators nonzero. Find $b-a$.',
15:r'Count all ordered integer solutions of $(100-x)^2+(100-y)^2=(x+y)^2$.',
17:r'Count positive-integer solutions of $x+y+z=64$ in which $y$ is even.',
18:r'Two pupils leave for school simultaneously at equal speeds. After three minutes one turns back for a book, increases speed by $60$ metres per minute, and keeps this increased speed on the return journey to school. They arrive simultaneously. Each home is $400$ metres from school, and retrieving the book takes no time. Find their original speed.',
19:r'For real $x\ne0$ satisfying $x-1/x=1$, evaluate $\sqrt5\,|x^8-x^{-8}|$.',
20:r'If $2015$ is a sum of $k$ consecutive positive integers, what is the largest possible $k$?',
21:r'The points $(-1,5)$, $(2,6)$, $(4,4)$ and $(0,1)$ lie on four different sides of a square. Determine its area.',
22:r'Count the three-digit positive integers whose decimal digit sum is a perfect square.',
23:r'Positive integers $p,q$ have the property that $p,q,p^2+q^2,p^3+q^3$ are all prime. Evaluate $p+q+p^2+q^2+p^3+q^3$.',
25:r'In how many ways can $\{1,2,3,4,5,6,7,8\}$ be partitioned into two unlabelled subsets whose element sums are both prime?',
26:r'Evaluate $\dfrac1{50^2}\sum_{k=1}^{50}\bigl(k^2-k(101-k)+(101-k)^2\bigr)$.',
27:r'How many three-digit multiples of $11$ have pairwise distinct decimal digits?',
28:r'The angles adjacent to the longer base of a trapezium are $15^\circ$ and $75^\circ$. The segment joining the midpoints of its diagonals has length $20$. Find its height.',
29:r'Real numbers $a,b,c$, with all denominators below nonzero, satisfy $\dfrac{a^3}{4a^2+2ab+b^2}+\dfrac{b^3}{4b^2+2bc+c^2}+\dfrac{c^3}{4c^2+2ca+a^2}=10$ and $\dfrac{b^3}{4a^2+2ab+b^2}+\dfrac{c^3}{4b^2+2bc+c^2}+\dfrac{a^3}{4c^2+2ca+a^2}=12$. Find $a+b+c$.',
30:r'Count the four-digit strings over $\{1,2,3,4,5\}$ which do not contain the consecutive block $23$.'
}
for n,s in S.items():
 k=f'aze_2025_j_{n}';R[k]['statement']=s
 R[k]['notes']+=' Restored as an English mathematical question without the multiple-choice alternatives. Public matching transcription: https://www.scribd.com/document/1001269135/8-9. The original-source URL is retained.'
 # The official booklet supplies questions, not worked solutions.
 R[k].pop('solutionUrl',None);R[k]['solution']='';R[k]['solutionKind']='unavailable';R[k]['noSolutionLink']=True
(P/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2));print('Restored',len(S))
