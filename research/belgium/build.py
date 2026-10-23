"""Individual assessments of official OMB final papers and original expositions."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
rows=[];decisions=[];papers=[]
def paper(year,level):
    global ctx
    url='https://omb.sbpm.be/modules/news/visit.php?fileid='+('54' if level=='MAXI' else '53')
    ctx=dict(country='Belgium',competition='Olympiade Mathématique Belge',year=year,section=level+' final',sourceUrl=url,solutionUrl=url)
    papers.append(ctx|dict(complete=True,expectedNumbers=['1','2','3','4']))
def add(n,r,t,s,why,tags,sol):
    p=ctx|dict(id=f"belgium-omb-{ctx['year']}-{ctx['section'].split()[0].lower()}-{n}",number=str(n),difficulty=r,topic=t,statement=s,ratingReason=why,tags=tags,solution=sol,solutionKind='original-exposition',solutionCredit='Independent mathematical exposition for Olympiad Atlas',reviewStatus='individually-assessed',notes='English mathematical paraphrase checked against the organiser’s French question and worked-solution booklet.')
    rows.append(p);decisions.append({k:p[k] for k in ['id','country','competition','year','section','number','difficulty','ratingReason']}|dict(included=True))
def ex(n,r,why):decisions.append({k:ctx[k] for k in ['country','competition','year','section']}|dict(number=str(n),difficulty=r,included=False,reason=why))
paper(2022,'MAXI')
add(1,5,'Number Theory',r'Let $P=1!\,2!\cdots100!$. (a) Can $a!$ be a square for an integer $2\le a\le100$? (b) Is $P$ a square? (c) Determine all $a\in\{1,\ldots,100\}$ such that $P/a!$ is a square. If there are none, investigate instead division by $a!b!$ for distinct $a,b$ in that range.','Pairing factorials reveals their square-free contribution. Finding one removable factorial is easy afterward, but proving uniqueness requires additional prime-exponent restrictions.',['factorials','prime valuations','pairing'],r'''For every $a$ between $2$ and $100$ there is a prime $p$ with $p\le a<2p$. One can check this range using just $p=2,3,5,7,13,23,43,83$: their intervals $[p,2p-1]$ cover it. The prime $p$ occurs exactly once in $a!$, which is therefore not a square.

Pair consecutive factorials:
$$P=(1!\,3!\cdots99!)^2(2\cdot4\cdots100)=\bigl(2^{25}1!\,3!\cdots99!\bigr)^2 50!.$$
Thus $P$ is not a square, and $P/50!$ is a square.

For uniqueness, the exponents of every prime in $a!$ and $50!$ must have the same parity. The prime $47$ forces $47\le a\le93$; the prime $53$ then forces $a\le52$. Among $47,48,49,50,51,52$, only $50$ works. Indeed, for $47$ the product $48\cdot49\cdot50$ has an odd exponent of $3$; for $48,49$ the quotient $50!/a!$ has an odd exponent of $2$; and for $51,52$ the quotient $a!/50!$ has an odd exponent of $3$.

Therefore $\boxed{a=50}$ is unique. The conditional two-factorial question does not arise.''')
add(2,4.5,'Geometry',r'A square $ABCD$ of side $x$, where $0<x<1$, is contained in a rhombus $AECF$ of side $1$; the two figures have the same opposite vertices $A,C$. Find the area inside the rhombus and outside the square, and the value of $x$ which maximises it.','The diagonal geometry gives a radical expression. Completing a unit-circle expression provides an elementary sharp maximum without calculus.',['rhombus diagonals','inequalities','optimisation'],r'''The rhombus diagonals are perpendicular bisectors. Since $AC=\sqrt2x$ and its side is $1$, the other diagonal is $EF=\sqrt{4-2x^2}$. The required area is
$$A=x\sqrt{2-x^2}-x^2.$$
Put $v=1-x^2$, so $0<v<1$. Then $A=\sqrt{1-v^2}+v-1$. By Cauchy–Schwarz,
$$\sqrt{1-v^2}+v\le\sqrt{2((1-v^2)+v^2)}=\sqrt2.$$
Equality holds exactly at $v=1/\sqrt2$. Hence the maximum area is $\boxed{\sqrt2-1}$, attained for $\boxed{x=\sqrt{1-1/\sqrt2}}$.''')
add(3,4.5,'Geometry',r'Build a square externally on each side of triangle $ABC$. At each vertex of the triangle, join the two new square vertices adjacent to that vertex; build another square on this joining segment. Find the ratio of the total area of these three new squares to the total area of the original three squares, first for a right triangle and then for any triangle.','The right-angle rotations change each included angle to a supplement. Applying the cosine rule twice makes the three resulting expressions telescope.',['squares','cosine rule','area identity'],r'''Write $a=BC,b=CA,c=AB$. At vertex $A$, the two relevant sides of the original squares have lengths $b,c$ and included angle $180^\circ-\angle A$. Thus the new square there has area
$$b^2+c^2+2bc\cos A=2b^2+2c^2-a^2,$$
using the cosine rule in $ABC$.

Adding the analogous expressions at $B,C$ gives $3(a^2+b^2+c^2)$. The original square areas total $a^2+b^2+c^2$, so the ratio is $\boxed3$ for every triangle, including a right triangle.''')
add(4,4,'Combinatorics',r'Distribute $590$ pupils into $25$ classes, each containing between $18$ and $28$ pupils inclusive. (a) Can $22$ classes have equal size? (b) What is the largest possible number of equal-sized classes? (c) Can every size occur at most twice? (d) What is the largest number of equal-sized classes guaranteed in every distribution?','Pigeonhole gives one bound, but both extremal answers also need constructions meeting the exact total and class-size restrictions.',['pigeonhole principle','extremal construction','integer bounds'],r'''(a) Yes: $22\cdot23+3\cdot28=590$.

(b) All $25$ cannot be equal since $25\nmid590$. If $24$ classes had size $q$, the remaining class would imply $562\le24q\le572$, which contains no multiple of $24$. But $23\cdot24+2\cdot19=590$, so the answer is $\boxed{23}$.

(c) There are only $11$ allowed sizes. If each occurred at most twice, there would be at most $22$ classes, a contradiction.

(d) Thus three equal sizes are guaranteed. To show four are not, use sizes $18,20,21,22,23,24,25,26,27,28$ with respective multiplicities
$$2,1,3,3,3,3,3,2,3,2.$$
These multiplicities total $25$, their weighted sum is $590$, and none exceeds $3$. The sharp guarantee is $\boxed3$.''')
paper(2023,'MAXI')
ex(1,2.5,'Expanding the base-ten and base-seven numerals gives2x=4y+z, leaving a short bounded digit enumeration.')
add(2,5,'Geometry',r'Two congruent upright rectangles of height $a$ and width $b$, with $a>b>0$, initially occupy $[-b,0]\times[0,a]$ and $[0,b]\times[0,a]$. Rotate the left rectangle clockwise about $(0,0)$ until its initially upper-right corner first reaches the right edge of the stationary rectangle. (a) Prove the stationary upper-left corner lies on the rotated rectangle’s left edge. (b) Find the overlap area. (c) If $a,b$ and the overlap area are positive integers, minimise $a$.','The rotation must first be related to a right triangle. Computing the intersection and then enforcing integrality combines geometry with a small Pythagorean-triple classification.',['rotation','overlapping rectangles','Pythagorean triples'],r'''Put $c=\sqrt{a^2-b^2}$. At the stopping angle $\theta$, we have $\sin\theta=b/a$, $\cos\theta=c/a$ and the moved corner is $F=(b,c)$.

The lower-left corner of the moved rectangle is $D=(-bc/a,b^2/a)$, and its left edge has unit direction $(b/a,c/a)$. Since
$$D+c(b/a,c/a)=(0,(b^2+c^2)/a)=(0,a),$$
the stationary upper-left corner $A=(0,a)$ lies on that edge.

Let $G$ be the intersection of the moved top edge with $y=a$. Its horizontal coordinate is $g=a(a-c)/b$. The overlap is the quadrilateral $OFG A$, where $O=(0,0)$. Triangles $OAG$ and $OFG$ are congruent right triangles, with common hypotenuse $OG$ and equal legs $OA=OF=a$. Thus the area is
$$\boxed{\frac{a^2}{b}\bigl(a-\sqrt{a^2-b^2}\bigr)}.$$
If the area and $a,b$ are integers, then $c$ is rational, hence an integer because $c^2$ is an integer. For $a<10$, the only positive integer right triangle is the $3,4,5$ triangle; the two orientations give areas $25/3$ and $25/2$, neither integral. With $a=10,b=8,c=6$, the area is $50$. Hence $\boxed{a=10}$ is minimal.''')
add(3,4.5,'Algebra',r'Find all real triples $(x,y,z)$ satisfying $x+y+1/z=x+1/y+z=1/x+y+z=3$.','Subtracting equations gives a useful factorisation, but the possibility of opposite signs prevents simply declaring all variables equal.',['symmetric system','factorisation','sign cases'],r'''All variables are nonzero. Subtraction shows
$$x-1/x=y-1/y=z-1/z.$$
For two variables, this equality factors as $(x-y)(xy+1)=0$. Thus any two are equal or negative reciprocals.

If all three are equal to $t$, then $2t+1/t=3$, so $t=1$ or $1/2$.

Otherwise, exactly two of the three coincide: a quadratic $u^2-cu-1=0$ has at most two roots. Write the triple, up to permutation, as $(t,t,-1/t)$. Substitution into the equation whose reciprocal falls on one of the repeated entries gives $t=3$.

The complete answer is $\boxed{(1,1,1),\ (1/2,1/2,1/2)}$ and the three permutations of $\boxed{(3,3,-1/3)}$. Each satisfies the original system.''')
add(4,4,'Geometry',r'Three spheres lie on the same side of a plane, touch that plane, and are externally tangent to each other. Their three contact points on the plane form a triangle with side lengths $3,4,6$. Determine the radii.','A spatial configuration becomes a right-triangle relation between each radius pair; the resulting three product equations must then be solved consistently.',['three-dimensional geometry','tangency','Pythagoras'],r'''If two radii are $r,s$ and their contact points are distance $d$ apart, their centres differ in height by $r-s$ and are distance $r+s$ apart. Pythagoras gives
$$(r+s)^2=d^2+(r-s)^2,\qquad 4rs=d^2.$$
Choose labels with contact distances $AB=6$, $BC=3$, $CA=4$. Then $r_Ar_B=9$, $r_Br_C=9/4$ and $r_Cr_A=4$. Dividing products gives $r_A^2=16$, and positivity gives
$$\boxed{r_A=4,\quad r_B=9/4,\quad r_C=1}.$$
These values yield precisely the stated centre distances, so they are attainable.''')
paper(2024,'MAXI')
ex(1,3,'The time from dawn to the meeting has square equal to the product of the two post-meeting journey times4 and9, so dawn is6am.')
ex(2,2,'Every integer satisfiesx³≡x modulo3, immediately proving all parts including any number of summands.')
add(3,4.5,'Geometry',r'Points $B,C,D,E$ lie on a line in that order. Triangle $ABE$ is right-angled at $B$, and $\angle BAC=\angle CAD=\angle DAE$. Express $DE$ in terms of $a=BC$ and $b=CD$.','Equal angles must be converted into a relation among three successive intersections; a carefully chosen trigonometric or auxiliary-perpendicular argument eliminates the altitude.',['angle trisection','tangent addition','similarity'],r'''Let $AB=h$ and each of the three equal angles be $\theta$. Then $\tan\theta=a/h$ and $\tan2\theta=(a+b)/h$. The double-angle identity gives
$$\frac{a+b}{h}=\frac{2a/h}{1-a^2/h^2},\qquad h^2=\frac{a^2(a+b)}{b-a}.$$
Consequently, by tangent addition,
$$BE=h\tan3\theta=\frac{(a+b)+a}{1-a(a+b)/h^2}=\frac{a(2a+b)}{2a-b}.$$
Subtracting $BD=a+b$ yields $\boxed{DE=b^2/(2a-b)}$. The configuration has $3\theta<90^\circ$, which ensures the denominator is positive.''')
ex(4,3.5,'Expanding by decimal place shows that each digit contributes a geometric sum to all proper prefixes, givingn−S(n)=9T(n).')
paper(2022,'MIDI')
ex(1,3,'The two isosceles triangles give the relevant base angles; subtracting them from angleB leaves(180°−B)/2.')
add(2,4,'Number Theory',r'Find all three-digit decimal numbers $100a+10b+c$ satisfying $100a+10b+c=a!+b!+c!$, where $0!=1$.','Factorial growth progressively restricts every digit; a disciplined case reduction is needed to avoid an unjustified brute-force list.',['decimal digits','factorials','bounding'],r'''A digit at least $7$ would contribute at least $5040$, impossible. If any digit were $6$, the sum would be at least $722$, whereas the leading digit is at most $6$, also impossible. Thus all digits are at most $5$.

Now the sum is at most $360$, so $a\le3$. If $a=3$, it is at most $6+120+120=246<300$. If $a=2$, both other digits would need to be $5$ to reach $200$, but $255\ne2+120+120$. Hence $a=1$.

Exactly one of $b,c$ must be $5$: without it the sum is at most $49$, and with both it exceeds $199$. If $b=5$, the equation $150+c=121+c!$ has no solution for $c=0,1,2,3,4$. If $c=5$, the equation $105+10b=121+b!$ gives only $b=4$. Therefore $\boxed{145}$ is the unique answer.''')
ex(3,3.5,'Resolve each tilted side into perpendicular componentsx,y. The bounding rectangle gives4x+2y=12 and2x+2y=7, followed by Pythagoras.')
ex(4,3,'Two surviving neighbouring runners would shift equally, so survivors form a nonadjacent subset of the line. Alternating removal attains the bound50.')
paper(2023,'MIDI')
ex(1,3.5,'The two concatenated age squares differ by2323=23·101. Factoring their difference determines roots39,62 and ages15,21.')
ex(2,3,'Pairing a second rotated triangle gives equal-area bands in a parallelogram, hence the grey:white ratio(n+1):(n−1).')
ex(3,2.5,'ForN≥4 the factorial sum ends in3, excluding squares; direct checking givesN1 or3.')
add(4,4.5,'Geometry',r'Three adjacent upright squares of side lengths $2,5,3$, in that left-to-right order, stand on the base $AB$ of a triangle $ABC$. The upper-left vertices of the first and second squares lie on $AC$; the upper-right vertices of the second and third lie on $BC$. Find the triangle’s area.','Several local similarities must be combined to recover both the full base and the remaining height above the central square.',['similar triangles','area','linear equations'],r'''The left side rises $3$ units while moving $2$ units horizontally between the relevant square corners, so its slope is $3/2$. On the right, the magnitude of the slope is $2/3$.

The base therefore extends $2/(3/2)=4/3$ beyond the first square and $3/(2/3)=9/2$ beyond the third. Thus
$$AB=\frac43+2+5+3+\frac92=\frac{95}{6}.$$
Let the height above the middle square be $y$. The horizontal distances from its top corners to the vertical through $C$ are $2y/3$ and $3y/2$, whose sum is $5$. Hence $y=30/13$, and the triangle’s full height is $5+y=95/13$.

Its area is $\boxed{\frac12\cdot\frac{95}{6}\cdot\frac{95}{13}=\frac{9025}{156}}$.''')
paper(2024,'MIDI')
ex(1,3,'Subtracting the equations gives(b−1)(a−c)=−1, so b is0 or2 and both remaining linear systems are immediate.')
ex(2,2.5,'Conservation of each liquid shows equal foreign volumes; their proportions are inversely related to the original container volumes.')
ex(3,3.5,'The first radius is6; two right-triangle tangency equations give the remaining radii4 and3. The earlier subparts guide the setup.')
ex(4,3,'Counting multiples of successive powers of2 gives the factorial valuation; the scaffolded parts culminate in50+25+12+6+3+1=97.')
cov=dict(reviewedCount=len(decisions),includedCount=len(rows),decisions=decisions,papers=papers,archiveUrl='https://omb.sbpm.be/modules/news/article.php?storyid=221',gaps=['OMB MAXI and MIDI finals2022–2024 are complete. Other years, the MINI category and preliminary rounds remain pending.','The Flemish VWO official website returned gateway errors during this pass; a public historical archive1995–2020 was located but is not yet screened.'],method='Each task was read and mathematically assessed individually. Included statements are English mathematical paraphrases, with independently checked worked expositions. Ratings are AI judgments, not official contest statistics.')
for name,v in [('data/belgium.json',rows),('research/belgium-coverage.json',cov)]:
    (R/name).write_text(json.dumps(v,ensure_ascii=False,indent=2))
print({'reviewed':len(decisions),'included':len(rows)})


# Restore reviewed questions outside the preferred browsing band.
if __name__ == "__main__":
    import runpy
    runpy.run_path(str(Path(__file__).resolve().parents[1] / "restore-smaller-range.py"))["main"](["belgium"])
