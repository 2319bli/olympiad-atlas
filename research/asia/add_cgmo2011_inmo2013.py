import json,pathlib
P=pathlib.Path('/workspace/sites/olympiad-atlas/research/asia');R=json.loads((P/'reviews.json').read_text())
def put(s,d,why,**kw):R[s]=dict(difficulty=d,reason=why,**kw)
put('chn_2011_deb93e',4.5,'The useful move is factoring (x−n)(y−n)=n², then pairing divisors and exploiting the primality of 4021; a short but genuine olympiad divisor-count argument.',statementOverride=r'For which positive integers $n$ are there exactly $2011$ pairs of positive integers $x\le y$ satisfying $1/x+1/y=1/n$?')
put('chn_2011_dd25aa',7.5,'Reviewed the smoothing proof: establish existence of a minimum, equalise the first and third ordered variables, reduce to three equal variables, then prove a substantial degree-eight one-variable inequality. This is beyond the intended band.')
put('chn_2011_d0e2b5',5.5,'Requires both a parity-based tournament construction and a global impossibility argument: for even n, neighbour orientations propagate and the adjacency condition forces too many defeats.',statementOverride=r'A round-robin tennis tournament has $n>2$ players and no draws. It is possible to arrange the players cyclically so that, whenever $A,B$ are neighbours and $C$ is another player, at least one of $A,B$ defeated $C$. Determine all possible $n$.')
put('chn_2011_1750ef',3.5,'For the corrected α≥0 statement, write z₁−xz₂=(1−x)z₁+x(z₁−z₂); convexity gives max{α,1}, with endpoint examples proving sharpness. Below the target band.',note='The book transcription omits α≥0. The complete CGMO 2011 paper reproduced at AoPS collection 3676 includes it.')
put('chn_2011_97f115',4.5,'Factor the difference of squares into powers of 11, remove the exact 11-adic valuation of m, then Fermat modulo 11 gives 2≡−1. The valuation step is the main extra hurdle.',statementOverride=r'Determine whether positive integers $m,n$ can make $m^{20}+11^n$ a perfect square, and justify your answer.')
put('chn_2011_5019b8',6,'A non-obvious terminating process is needed before construction: lexicographic increase stabilises boxes 2,...,n, then a controlled sequence of firings transports each vacant box towards the surplus at box 1.',statementOverride=r'There are $n\ge2$ boxes $B_1,\ldots,B_n$ in a row containing a total of $n$ balls. A move at an endpoint box transfers one ball to its neighbour. A move at an interior box transfers one ball to each neighbour. A move is allowed only when the chosen box has enough balls. Prove that some finite sequence of moves leaves exactly one ball in every box.')
put('chn_2011_814a14',6.5,'Menelaus first proves FG parallel to BC. A second Menelaus reduction must then be combined with the A-excircle contact-length formula and the small incircle radius/altitude ratio. Several connected geometric reductions are required.',statementOverride=r'Let the $A$-excircle of triangle $ABC$ touch $BC$ at $M$. Points $D\in AB$ and $E\in AC$ satisfy $DE\parallel BC$. The incircle of $ADE$, with centre $O_1$, touches $DE$ at $N$, and $O$ is the centre of the $A$-excircle of $ABC$. Set $F=BO_1\cap DO$ and $G=CO_1\cap EO$. Prove that $MN$ passes through the midpoint of $FG$.',note='Corrected “inscribed circle” in the MathNet transcription to “A-excircle”. This is established by the original figure (large circle outside ABC), its contact-length formula, and the complete CGMO 2011 paper reproduced at AoPS collection 3676. The uncorrected version is false.')
put('ind_2013_12c6fe',5,'Equal tangent lengths place K on the radical axis; recognising K as both circumcentre and orthocentre of PQR finishes the proof. The configuration and two centre interpretations give a substantial geometry insight.',statementOverride=r'Two circles $\Gamma_1,\Gamma_2$, with centres $O_1,O_2$, are externally tangent at $R$. A line through $O_1$ touches $\Gamma_2$ at $P$, and a line through $O_2$ touches $\Gamma_1$ at $Q$. The two lines meet at $K$, and $KP=KQ$. Prove that $PQR$ is equilateral.',solutionOverride=r'''Equal tangent lengths give equal powers of $K$ with respect to the circles. Thus $K$ lies on their radical axis, the common tangent at $R$, and
$$KP=KQ=KR.$$
In particular $K$ is the circumcentre of $PQR$.

From $K$, the two tangents to $\Gamma_1$ touch at $Q,R$. The line joining $K$ to its centre $O_1$ is perpendicular to the chord $QR$. But $K,O_1,P$ are collinear, so $KP\perp QR$. Similarly $KQ\perp PR$. Thus the circumcentre is also the orthocentre. The altitude from each vertex therefore passes through the midpoint of the opposite side, so all three sides are equal.''',note='Corrected Γ₂ to Γ₁ in the second tangency condition: a line through O₂ cannot be tangent to its own circle. The solution and original construction explicitly use Q on Γ₁.')
put('ind_2013_ec8fdc',5,'The factorisation into (4m+1)(m²+3), a gcd dividing 49, and an exact 7-adic valuation reduce an unbounded prime-power equation to one solution.',solutionOverride=r'''Rewrite the equation as
$$(4m+1)(m^2+3)=3p^n.$$
Both factors exceed $3$, so both are divisible by $p$. Put $U=4m+1$, $V=m^2+3$. The identity $16V=U^2-2U+49$ shows that their gcd divides $49$, hence $p=7$.

Write $U=\varepsilon7^a$ and $V=(3/\varepsilon)7^b$, where $\varepsilon\in\{1,3\}$ and $a,b\ge1$. If $a=1$, the requirement $U\equiv1\pmod4$ forces $U=21$, hence $m=5$, but then $V=28$, impossible. If $a\ge3$, the displayed identity gives $v_7(V)=2$. Thus $V\le147$, so $m\le12$ and $U\le49$, contradicting $U\ge343$.

Consequently $a=2$. Since $U\equiv1\pmod4$, $U=49$ and $m=12$. Then $V=147$ and $n=4$. Direct substitution verifies the unique answer $(m,n,p)=(12,4,7)$.''')
put('ind_2013_26dd09',3.5,'For a positive integer root m, the equation forces m>a≥d while the constant term forces m|d; for a negative root −n, group n⁴+n²(an−b)+(cn−d)>0. These are short standard sign/divisibility checks.')
put('ind_2013_74b08d',4.5,'The parity is not obtained by counting subsets directly: toggle their integer average in or out. Identifying this involution and isolating singleton fixed exceptions is the key.',solutionOverride=r'''There are exactly $n$ good singleton subsets. Pair every other good subset $S$ with the subset obtained by toggling its arithmetic mean $m$:
- if $m\in S$, remove $m$;
- if $m\notin S$, adjoin $m$.

The resulting set is nonempty, is still not a singleton, and has the same mean $m$. Also $1\le m\le n$, so it remains a subset of the required set. Toggling again recovers $S$, and the two sets in each pair are distinct. Hence the number of non-singleton good subsets is even, giving $t_n\equiv n\pmod2$.''')
put('ind_2013_7c2fee',5.5,'Translate three different centre-based areas into trigonometric expressions, eliminate A to get a quadratic in sin²C, and check both resulting acute configurations. The elimination is moderately sustained.',solutionOverride=r'''Write $R$ for the circumradius and $\Delta$ for the area. Standard altitude and chord formulas give
$$[ODC]=\frac12R^2\sin A\cos A,$$
$$[HEA]=2R^2\sin C\cos C\cos^2A,$$
$$[GFB]=\frac{\Delta}{6}=\frac13R^2\sin A\sin B\sin C.$$
Equality of the first two yields $\tan A=4\sin C\cos C$. Equality of the first and third yields $3\cos A=2\sin B\sin C$. Using $\sin B=\sin(A+C)$ and cancelling $\cos A>0$ gives
$$3=2\sin^2 C(1+4\cos^2 C).$$
Thus, with $t=\sin^2C$, $(4t-3)(2t-1)=0$. Acuteness gives $C=60^\circ$ or $45^\circ$.

Both occur: the equilateral triangle gives $60^\circ$; for $45^\circ$, take $A=\arctan2$ and $B=\arctan3$. Their sum is $135^\circ$ and the area equalities above hold. Hence the answer is $\boxed{45^\circ,60^\circ}$.''')
put('ind_2013_374f99',4.5,'Constructing the difference of the two monic cubic root polynomials collapses it to kt. Opposite endpoint signs then force k=0. Short execution follows a useful polynomial encoding.',solutionOverride=r'''Consider
$$F(t)=(t-x)(t-y)(t-z)-(t-a)(t-b)(t-c).$$
The equal sums cancel the quadratic coefficients, and the equal products cancel the constants. Hence $F(t)=kt$ for some real $k$.

At $t=a$, all three factors of $(a-x)(a-y)(a-z)$ are nonpositive, so $ka\le0$ and $k\le0$. At $t=c$, all three factors are nonnegative, so $kc\ge0$ and $k\ge0$. Therefore $k=0$ and the two cubics coincide. Their ordered roots coincide, proving $a=x$, $b=y$, $c=z$.''')
(P/'reviews.json').write_text(json.dumps(R,ensure_ascii=False,indent=2))
