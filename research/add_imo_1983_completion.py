from international_completion_helpers import add,save
add(1983,1,'Algebra',5,'The limit first eliminates a scaling period, giving an involution and then multiplicativity; powers of a nonunit fixed point contradict the limit.',r'Find all functions $f:(0,\infty)\to(0,\infty)$ satisfying $f(xf(y))=yf(x)$ and $\lim_{x\to\infty}f(x)=0$.',r'''Put $c=f(1)$. Setting $y=1$ gives $f(cx)=f(x)$. If $c>1$, iterating this equality contradicts the limit; if $c<1$, use $f(x/c)=f(x)$ instead. Hence $c=1$.

Setting $x=1$ now gives $f(f(y))=y$. Substituting $f(y)$ for $y$ in the original equation gives $f(xy)=f(x)f(y)$. In particular $f(1/t)=1/f(t)$.

For any $x$, put $k=xf(x)$. The original equation gives $f(k)=k$. If $k>1$, multiplicativity gives $f(k^n)=k^n$, contradicting the limit. If $k<1$, the same contradiction applies to the fixed point $1/k>1$. Therefore $xf(x)=1$ for every $x$. The function $f(x)=1/x$ directly satisfies both conditions and is the unique answer.''',['Functional equations','Multiplicativity','Limits','Iteration'])
add(1983,2,'Geometry',5.5,'Use the common tangent normals to locate both chord midpoints, then compare half-angle formulas in the two triangles; the unequal radii enter only through their difference.',r'Two intersecting circles with distinct radii have centres $O_1,O_2$ and a common point $A$. Their two common tangents touch them at $P_1,P_2$ and $Q_1,Q_2$. If $M_i$ is the midpoint of $P_iQ_i$, prove $\angle O_1AO_2=\angle M_1AM_2$.',r'''Take $O_1=(0,0)$, $O_2=(d,0)$, radii $r_1,r_2$, and $A=(x,y)$ with $y>0$. The common external tangents have unit normals $(u,\pm\sqrt{1-u^2})$, where $u=(r_1-r_2)/d$. Hence
$$M_1=(r_1u,0),\quad M_2=(d+r_2u,0),\quad x=\frac{d^2+r_1^2-r_2^2}{2d}.$$
Thus $x$ is the midpoint of the two midpoint coordinates. Put $h=M_1M_2/2=[d^2-(r_1-r_2)^2]/(2d)>0$. The angle $\phi=\angle M_1AM_2$ has $\tan(\phi/2)=h/y$.

Subtracting the two circle equations, or using the altitude formula, gives
$$y^2=\frac{((r_1+r_2)^2-d^2)(d^2-(r_1-r_2)^2)}{4d^2}.$$
For $\theta=\angle O_1AO_2$, the cosine rule yields
$$\tan^2(\theta/2)=\frac{d^2-(r_1-r_2)^2}{(r_1+r_2)^2-d^2}=\frac{h^2}{y^2}=\tan^2(\phi/2).$$
Both half-angles lie in $(0,\pi/2)$, so $\theta=\phi$.''',['Coordinates','Circles','Tangency','Trigonometry'])
add(1983,3,'Number Theory',5.5,'Choose three bounded residues independently modulo the pairwise coprime parameters; their combined upper bound leaves a nonnegative multiple of abc, while the proposed exception forces all three residues maximal.',r'For pairwise coprime positive integers $a,b,c$, prove that $2abc-ab-bc-ca$ is the largest integer not expressible as $xbc+yca+zab$ with nonnegative integers $x,y,z$.',r'''Set $F=2abc-ab-bc-ca$. If $F=xbc+yca+zab$, reduction modulo $a,b,c$ gives $x\equiv-1\pmod a$, $y\equiv-1\pmod b$, $z\equiv-1\pmod c$. Nonnegativity then implies
$$xbc+yca+zab\ge(a-1)bc+(b-1)ca+(c-1)ab=F+abc>F,$$
a contradiction.

Now take any integer $N>F$. Choose $0\le x<a$, $0\le y<b$, $0\le z<c$ such that $xbc\equiv N\pmod a$, $yca\equiv N\pmod b$, $zab\equiv N\pmod c$. Pairwise coprimality makes these choices possible. For $S=xbc+yca+zab$, the difference $N-S$ is divisible by $abc$. Since $S\le F+abc$ and $N>F$, we have $N-S>-abc$. Thus $N-S=tabc$ for an integer $t\ge0$, and $N=(x+ta)bc+yca+zab$ is represented. The argument also covers parameters equal to one.''' ,['Chinese remainder','Divisibility','Extremal arguments','Nonnegative representations'])
add(1983,4,'Combinatorics',5.5,'Three specially placed boundary points contain a same-colour pair whose perpendicular line forces almost an entire side to the other colour; repeating this creates a monochromatic altitude triangle.',r'Colour every point on the boundary of an equilateral triangle with one of two colours. Must there be three same-coloured points forming a right triangle?',r'''Yes. Mark $X,Y,Z$ two-thirds along the directed sides $BC,CA,AB$, respectively. Then $XY\perp BC$, $YZ\perp CA$, and $ZX\perp AB$. Two marked points share a colour; by cyclic relabelling suppose $X,Y$ are red.

If no monochromatic right triangle exists, every point of $BC$ other than $X$ must be blue. Let $W$ be the perpendicular foot of $Z$ on $BC$; it is an interior point distinct from $X$. The points $B,W$ are blue, so $Z$ must be red, or $BWZ$ would be a blue right triangle.

Now $Y,Z$ are red, forcing every point of $CA$ except $Y$ blue. In particular $A,C$ are blue. The midpoint $M$ of $BC$ is also blue, and $AM\perp BC$. Thus $AMC$ is a blue right triangle, a contradiction.''',['Colouring','Pigeonhole principle','Combinatorial geometry','Construction'])
add(1983,5,'Combinatorics',4.5,'Base-three digits restricted to zero and one prevent carries in the arithmetic-progression equation, giving a large explicit progression-free set.',r'Can one select 1983 distinct integers from $1,\ldots,100000$ with no three forming an arithmetic progression? Prove the answer.',r'''Yes. Consider all integers with at most eleven ternary digits, each digit zero or one. There are $2^{11}=2048$ such integers, ranging from zero to $(3^{11}-1)/2=88573$.

If three members satisfy $x+z=2y$, neither the addition on the left nor the doubling on the right involves carries in base three. Digitwise, $x_i+z_i=2y_i$ with all digits in $\{0,1\}$. If $y_i=0$, both other digits are zero; if $y_i=1$, both are one. Thus $x=y=z$, so no nonconstant three-term progression occurs.

Add one to every member. This preserves the absence of progressions and produces 2048 positive integers at most 88574. Any 1983 of them are a valid selection.''',['Digits','Construction','Arithmetic progressions','Counting'])
add(1983,6,'Algebra',4.5,'The triangle-side substitution exposes a cyclic reciprocal sum; Cauchy–Schwarz proves it and its equality condition gives the equilateral case.',r'For the side lengths $a,b,c$ of a nondegenerate triangle, prove $a^2b(a-b)+b^2c(b-c)+c^2a(c-a)\ge0$ and determine equality.',r'''Write $a=y+z$, $b=z+x$, $c=x+y$ with $x,y,z>0$. Expanding the target expression gives
$$2\bigl(xy^3+yz^3+zx^3-xyz(x+y+z)\bigr)
=2xyz\left(\frac{y^2}{z}+\frac{z^2}{x}+\frac{x^2}{y}-x-y-z\right).$$
Cauchy–Schwarz gives
$$\frac{y^2}{z}+\frac{z^2}{x}+\frac{x^2}{y}\ge\frac{(x+y+z)^2}{x+y+z}=x+y+z.$$
Equality requires $y/z=z/x=x/y$, forcing $x=y=z$ because they are positive. Thus equality holds exactly when $a=b=c$.''',['Inequalities','Cauchy–Schwarz','Substitution','Equality cases'])
save()
