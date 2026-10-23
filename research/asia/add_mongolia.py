import json,pathlib
p=pathlib.Path('research/asia/reviews.json');r=json.loads(p.read_text())
def add(key,diff,reason,sol=None,**kw):
 r['mng_2025_'+key]={'difficulty':diff,'reason':reason,**kw}
 if sol:r['mng_2025_'+key]['solutionOverride']=sol
add('53613a',6,'Combines the arc-midpoint incenter lemma, a power identity and a less obvious triangle similarity.',r'''Put $R=OB$ and let $r$ be the inradius. The arc-midpoint lemma gives $MI=MA=2R\sin(B/2)$, while $BI=r/\sin(B/2)$. Thus
$$BI\cdot IM=2Rr=BO\cdot II_B.$$
Also $OM\parallel II_B$, since both are perpendicular to $AC$. The equal base angles of triangle $BOM$, together with $B,I,M$ collinear, give the included-angle equality for triangles $BIO$ and $II_BM$. The displayed product identity gives their corresponding side ratios, so these triangles are similar. Consequently, using directed angles,
$$\angle BOI=\angle IMI_B=\angle BMD=\angle BED=\angle OBE.$$
Here the middle equality uses the cyclic quadrilateral $BMDE$, and the last uses $D,O,E$ collinear. Hence $OI\parallel BE$.''')
add('6ae951',4.5,'Turns the subset problem into an integer factorization and uses uniqueness of binary expansion; the empty-set case matters.',r'''Write $S(A)=2t$. Every integer $t$ from $0$ to $1023$ corresponds to exactly one subset $A$, by binary expansion, and $S(B)=2046-2t$. The equation is therefore equivalent to
$$(x+1)(2t+1-x)=2047=23\cdot89.$$
If $x$ is a positive root, the other root is $2t-x=S(B)/x\ge0$. Thus both displayed factors are positive. The factor pair $1,2047$ gives $t=1023$, with roots $0,2046$; the factor pair $23,89$ gives $t=55$, with roots $22,88$. There are no other positive factor pairs. Both values of $t$ give valid partitions, so the answer is $\boxed{2}$.''')
add('706550',3,'Fermat modulo 7 and a seven-residue check immediately contradict the equation.')
add('8b6a73',5.5,'Finds a forcing reply to increment moves, then proves digit-sum replies strictly descend without creating an opponent win.',r'''The first player wins. Whenever the number at the start of a pair of turns is $b\ge9$, the first player writes $b+1$. If the second player also adds $1$, the first player adds $1$ once more, producing the four-term arithmetic progression $b,b+1,b+2,b+3$.

Otherwise the second player writes $S(b+1)<b$. Indeed, for every integer $k\ge10$, $S(k)\le k-9$. The number at the start of the next pair of turns has therefore strictly decreased. Along this descent each new digit-sum value is smaller than every preceding value, so it cannot create a third occurrence. Nor can the second player create a four-term arithmetic progression: the successive differences alternate an increment of $1$ with a negative difference. If the second player instead increments, the previous difference was negative, except on the very first pair, when too few terms exist to finish.

Eventually a pair starts at $1\le b\le8$. The first player writes $u=b+1\le9$. If the second player writes $u+1$, the first player writes $u+2$ and wins by an arithmetic progression. If the second player writes $S(u)=u$, the first player repeats $u$ by taking its digit sum and wins by three equal terms. Earlier appearances of $u$ can only make the first player's first move win: among earlier descending pairs, $u$ could occur at most once. Thus the strategy always wins.''',topic='Combinatorics')
add('8e9a0b',5.5,'Uses two power-of-a-point identities to manufacture a cyclic quadrilateral, then repeats the argument symmetrically.',r'''The similarity $\triangle KMC\sim\triangle ABC$ gives $\angle MKC=\angle BAC$, hence $A,M,K,B$ are concyclic. Taking powers at $C$, first in this circle and then in $(AMP)$, gives
$$CB\cdot CK=CA\cdot CM=CP\cdot CX.$$
Thus $B,K,P,X$ are concyclic. Directed angles now give
$$\angle BXC=\angle BXP=\angle BKP=\angle BAC\pmod{180^\circ}.$$
(The signs are interpreted as directed angles, since $B,K,C$ are collinear.) Similarly, $A,N,L,C$ are concyclic; taking powers at $B$ shows $C,L,P,Y$ are concyclic, and gives $\angle BYC=\angle BAC\pmod{180^\circ}$. Therefore $\angle BXC=\angle BYC$, proving that $B,C,X,Y$ are concyclic.''')
add('cbc2b6',6.5,'A subtle irreducibility argument: rule out linear factors modulo 2, then constrain a quadratic factor by coefficient comparisons modulo 3 and 5.',r'''Modulo $2$, the polynomial has no root, so it has no integer root. If this monic quintic were reducible over the integers, its factors could therefore be grouped into monic factors of degrees $2$ and $3$. Write
$$X^5+61X+2025=(X^2+aX+b)(X^3-aX^2+cX+d).$$
Comparing the coefficients of $X^3$ and $X^2$ gives $c=a^2-b$ and $d=a(2b-a^2)$. The remaining comparisons give
$$3a^2b-a^4-b^2=61,\qquad bd=2025.$$
Modulo $3$, the first equation says $a^4+b^2\equiv2$, so neither $a$ nor $b$ is divisible by $3$. If $5\mid b$, the same equation modulo $5$ would give $-a^4\equiv1$, impossible because a fourth power is $0$ or $1$ modulo $5$. Thus $b$ is divisible by neither $3$ nor $5$; since $b\mid2025$, it follows that $b=\pm1$.

For $b=-1$ the left side of the first equation is negative. For $b=1$, putting $u=a^2$ gives $3u-u^2-1\le5/4<61$. Both cases are impossible, proving irreducibility.''')
add('dc7097',5.5,'Combines a sharp split into decimal blocks, leading-digit bounds and modular restrictions on the two possible digits.',r'''Write $S=10^nU+V$, where $1\le U\le10^{n-2}-1$ and $0\le V<10^n$. Since $S$ is divisible by $d=10^n-3$, so is $3U+V$. The latter is positive and less than $2d$, so
$$V+3U=10^n-3.$$
In particular $V\ge10^n-3\cdot10^{n-2}$, so its leading digit is $9$.

Let $u,v$ be the units digits of $U,V$. The identity implies $3u+v\equiv7\pmod{10}$. Therefore $u\ne v$, since $4u\equiv7$ has no solution. If $S$ used at most two digits, those two digits would be $u,v$, and one of them would be $9$. If $u=9$, then $v=0$, so every digit of $U,V$ is $0$ or $9$ and $9\mid V+3U$, contrary to $10^n-3\equiv7\pmod9$. If $v=9$, then $u=6$, so $3\mid V+3U$, contrary to $10^n-3\equiv1\pmod3$. Hence at least three different digits occur.''')
ineq=r'''First replace all negative variables simultaneously by $0$. Every negative summand becomes $0$, while every nonnegative summand can only increase, since its denominator cannot increase. It therefore suffices to consider $0\le t_i\le2$.

Put $x_i=t_i^2/4$, so $0\le x_i\le1$ and $t_i^3\le2t_i^2$. For any $0\le x,y\le1$,
$$\frac{x}{1+y}\le\frac{1-y+x}{2},$$
because after multiplication by $2(1+y)$ the difference is $(1-y)(1+y-x)\ge0$. Therefore, with cyclic indices,
$$\sum_i\frac{t_i^3}{t_{i+1}^2+4}\le2\sum_i\frac{x_i}{1+x_{i+1}}\le\sum_i(1-x_{i+1}+x_i)=n.$$
This proves the desired inequality.'''
add('ee11a5',5,'Handles unrestricted negative inputs, then discovers a cyclic telescoping bound on the unit interval.',ineq.replace('This proves the desired inequality.','Take $n=4$ to obtain the claimed bound $4$.'),topic='Algebra')
add('7eac62',5.5,'The main insight is a two-variable inequality whose cyclic sum telescopes; the negative-input reduction must be justified.',ineq,topic='Algebra')
add('510a85',3.5,'The standard totient product immediately gives the power-of-two bound and a ratio below one half.')
add('2e8d43',8.5,'Requires a carefully chosen inversion, several auxiliary diameter points and Pascal-type incidence; substantially above the target band.')
add('407690',7.5,'The first circle incidence is accessible, but the second conclusion requires substantial configuration and orientation casework.')
add('e9e8b0',6.5,'A decimal-block divisibility reduction followed by a nontrivial carry and digit-set analysis establishes a sharp minimum.',r'''Put $n=2025$ and $d=10^n+3$. The $2n$-digit number consisting of $n$ ones followed by $n$ threes equals $(10^n+3)(10^n-1)/9$, so $2n$ digits suffice.

Suppose a shorter positive multiple $N$ uses at most two digits. Removing trailing zeroes preserves divisibility by $d$, so assume its units digit is nonzero. Since $N\ge d$, it has more than $n$ digits. Write $N=10^nB+A$, with $1\le B<10^{n-1}$ and $0\le A<10^n$. Divisibility gives $d\mid A-3B$, while $|A-3B|<d$; hence $A=3B$.

View $A$ as a block of exactly $n$ digits, retaining leading zeroes. If its first digit were zero, the two available digits would be $0$ and some $k\ne0$. The units-digit equation forces $3k\equiv k\pmod{10}$, hence $k=5$. But multiplying a number made from $0,5$ and ending in $5$ by $3$ gives a tens digit $1$ or $6$, a contradiction.

Thus $A$ has $n$ digits. Its first digit is $1$ or $2$, and $B$ has $n-1$ digits. The units digits of $A,B$ are distinct (otherwise their common nonzero value would be $5$, incompatible with a leading digit $1$ or $2$). Their two digits are therefore exactly the digits used throughout $N$. The congruence between the units digits leaves four possible digit sets: $\{1,3\},\{1,7\},\{2,4\},\{2,6\}$.

For $\{1,3\}$, $3B\le10^{n-1}-1$, too short. For either $\{2,4\}$ or $\{2,6\}$, $3B<2\cdot10^{n-1}$, whereas $A$ begins with $2$. For $\{1,7\}$, if $B$ begins with $1$ then $3B<10^{n-1}$; if it begins with $7$ then $3B\ge2.1\cdot10^{n-1}$, whereas $A$ must begin with $1$. All cases are impossible. The required minimum is therefore $\boxed{4050}$.''')
p.write_text(json.dumps(r,ensure_ascii=False,indent=2));print(len(r))
