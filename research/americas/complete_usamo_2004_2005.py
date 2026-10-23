"""Add two individually reviewed papers; safe to rerun without duplicating rows.

Source statements and arguments checked in Evan Chen's author-maintained TeX
and PDF notes. These are personal solutions, not official MAA solutions.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
rows = []


def add(year, number, difficulty, topic, subtopics, statement, reason, solution=None):
    url = f'https://web.evanchen.cc/exams/USAMO-{year}-notes.pdf'
    rows.append(dict(
        id=f'us-usamo-{year}-{number}', country='United States',
        competition='USAMO', year=year, number=str(number),
        statement=statement, topic=topic, subtopics=subtopics,
        difficulty=difficulty, ratingReason=reason,
        sourceUrl=url, solutionUrl=url,
        solution=solution or f'[Read Evan Chen’s solution notes]({url}), Problem {number}.',
        solutionKind='original-exposition' if solution else 'source-link',
        reviewStatus='individually-assessed',
        notes='Statement independently paraphrased; difficulty assessed from the mathematical argument. Linked notes are author-maintained personal solutions, not official MAA solutions.'))


add(2004, 1, 5, 'Geometry',
    ['Circles & tangency', 'Geometric inequalities', 'Trigonometry'],
    r'A convex quadrilateral $ABCD$ has an incircle and every interior angle lies between $60^\circ$ and $120^\circ$, inclusive. Establish $\frac13|AB^3-AD^3|\le |BC^3-CD^3|\le3|AB^3-AD^3|$, and determine all equality cases.',
    'Equal tangent sums allow cancellation after factoring the cubes. Comparing both quadratic expressions with the same diagonal through the cosine rule gives the bounds; zero differences must be handled separately for equality.')
add(2004, 2, 7, 'Number Theory',
    ['Divisibility & GCD', 'Induction', 'Parity'],
    r'Integers $a_1,\ldots,a_n$ have gcd $1$. Suppose $S\subseteq\mathbb Z$ contains every $a_i$ and every $a_i-a_j$, including $i=j$. Whenever $x,y,x+y\in S$, assume also $x-y\in S$. Show that $S=\mathbb Z$.',
    'Bézout suggests the target, but ordinary closure under addition is unavailable. Building all integer linear combinations needs an induction on support and a parity adjustment of coefficients.')
add(2004, 3, 9, 'Combinatorics',
    ['Tilings & dissections', 'Algorithms & constructions', 'Extremal arguments'],
    r'Determine the positive real numbers $k$ for which a rectangle with side lengths $1,k$ admits a dissection into exactly two polygons that are similar but not congruent.',
    'Requires a scalable staircase construction covering every nonsquare aspect ratio, together with a separate impossibility argument for a square using the shared boundary and longest sides.')
add(2004, 4, 5.5, 'Combinatorics',
    ['Games & strategies', 'Invariants', 'Combinatorial geometry'],
    r'Alice moves first on an empty $6\times6$ board. Players alternate writing a previously unused rational number in an empty cell. After all cells are filled, mark the largest entry in each row. Alice wins if the marked cells connect the top edge to the bottom edge, with corner contacts allowed; otherwise Bob wins. Give a winning strategy and prove it works.',
    'Pairing cells in two adjacent rows with a three-column shift creates a barrier. The key is preserving the same relative order in the paired rows using the density of the rationals.')
add(2004, 5, 6, 'Algebra',
    ['Inequalities', 'Algebraic identities'],
    r'For $a,b,c>0$, establish $(a^5-a^2+3)(b^5-b^2+3)(c^5-c^2+3)\ge(a+b+c)^3$.',
    'The main step is discovering a simpler cubic lower bound for each factor. Its factorisation and a three-factor Hölder inequality then finish the proof.',
    r'For $t>0$, $(t^5-t^2+3)-(t^3+2)=(t^2-1)(t^3-1)\ge0$, since the two factors have the same sign. Hölder gives $(a^3+1+1)(1+b^3+1)(1+1+c^3)\ge(a+b+c)^3$. Combining the two inequalities proves the claim. Equality holds precisely at $a=b=c=1$.')
add(2004, 6, 8, 'Geometry',
    ['Circles & tangency', 'Geometric inequalities', 'Algebraic identities'],
    r'A convex quadrilateral $ABCD$ has an incircle with centre $I$. If $(AI+DI)^2+(BI+CI)^2=(AB+CD)^2$, prove that $ABCD$ is an isosceles trapezoid.',
    'Tangent-length coordinates turn the condition into an equality case of a nontrivial radical inequality. The constraint among four tangent lengths, a symmetric identity, and several simultaneous equality conditions must all be coordinated.')
add(2005, 1, 5, 'Number Theory',
    ['Divisibility & GCD', 'Primes', 'Algorithms & constructions'],
    r'Which composite positive integers $n$ allow their divisors greater than $1$ to be placed once each around a circle, with the gcd of every neighbouring pair greater than $1$?',
    'The construction groups divisors by a prime factor and uses products of adjacent primes as bridges. Prime powers and exactly two prime factors need separate treatment to isolate the obstruction.')
add(2005, 2, 6, 'Number Theory',
    ['Modular arithmetic', 'Diophantine equations', 'Squares & powers'],
    r'Show that no integers $x,y,z$ satisfy both $x^6+x^3+x^3y+y=147^{157}$ and $x^3+x^3y+y^2+y+z^9=157^{147}$.',
    'Adding the equations and completing a square exposes a modular obstruction. Choosing modulus 19 from the ninth power is the creative step; quadratic residues then give a short contradiction.')
add(2005, 3, 7, 'Geometry',
    ['Angles & cyclic quadrilaterals', 'Similarity & congruence', 'Concurrency & collinearity'],
    r'Let $ABC$ be acute and let distinct $P,Q$ lie inside side $BC$. Choose $C_1$ so that $APBC_1$ is a convex cyclic quadrilateral, $QC_1\parallel CA$, and $C_1,Q$ are on opposite sides of $AB$. Similarly choose $B_1$ with $APCB_1$ convex and cyclic, $QB_1\parallel BA$, and $B_1,Q$ on opposite sides of $AC$. Prove that $B_1,C_1,P,Q$ are concyclic.',
    'Introducing the second intersection of AC₁ with the other circle reveals a useful triangle similarity. A reverse construction then proves an unexpected collinearity and the required concyclicity.')
add(2005, 4, 4, 'Combinatorics',
    ['Counting', 'Combinatorial geometry'],
    r'Four equal parallel legs of length $n$ are attached at the corners of a square table, where $n$ is a positive integer. Label them cyclically $1,2,3,4$. Count the integer tuples $(k_1,k_2,k_3,k_4)$ with $0\le k_i\le n$ for which shortening leg $i$ by $k_i$ leaves all four endpoints coplanar, so the table can stand with every leg touching a flat floor. Legs of length zero are allowed.',
    'Coplanarity reduces to equality of the sums on opposite corners. Counting ordered pairs with each possible sum gives a triangular sequence, whose squared terms can be summed directly.')
add(2005, 5, 6, 'Combinatorics',
    ['Combinatorial geometry', 'Extremal arguments', 'Colouring'],
    r'For $n>1$, take $n$ red and $n$ blue points in the plane, with no three collinear. Call a line balanced if it contains one point of each colour and each open half-plane it bounds contains equally many red and blue points. Prove that at least two distinct balanced lines exist.',
    'The convex hull provides two cases. Mixed colours on the hull give immediate supporting lines; a monochromatic hull requires rotating a line at a hull vertex and tracking the red-minus-blue count.')
add(2005, 6, 9, 'Number Theory',
    ['Digits & bases', 'Pigeonhole principle', 'Extremal arguments'],
    r'Write $s(m)$ for the decimal digit sum of a positive integer $m$. A finite set $S$ of positive integers is $k$-stable when $s(\sum_{x\in X}x)=k$ for every nonempty $X\subseteq S$. For $n\ge2$, let $f(n)$ be the smallest $k$ admitting such a set of size $n$. Prove that absolute constants $0<C_1<C_2$ exist with $C_1\log_{10}n\le f(n)\le C_2\log_{10}n$.',
    'Both logarithmic bounds require invention: a family with controlled decimal complements, and a lower bound forcing a large digit sum in some subset. Modular pigeonholing plus a digit-sum lemma provides a rigorous alternative to a delicate grouping argument.',
    r'''For the upper bound, put $e=\lfloor\log_{10}(n(n+1)/2)\rfloor+1$ and $M=10^e-1$. Use $S=\{M,2M,\ldots,nM\}$. Every nonempty subset sum is $tM$ with $1\le t<10^e$. Since $tM=(t-1)10^e+(10^e-t)$, the two blocks are decimal complements and their digit sums total $9e$. Thus $f(n)\le9e\le18\log_{10}n+9<48\log_{10}n$ for $n\ge2$.

For the lower bound, first note that any positive multiple of $10^e-1$ has digit sum at least $9e$. Indeed, repeatedly replace an integer by the sum of its base-$10^e$ blocks. Positivity and the residue modulo $10^e-1$ are preserved, digit sum cannot increase, and the value strictly decreases until it is at most $10^e-1$. A positive multiple therefore ends at $10^e-1$.

Now let $n\ge9$ and $e=\lfloor\log_{10}(n+1)\rfloor$, so $10^e-1\le n$. Order the elements of a $k$-stable set and consider its $n+1$ partial sums, including zero. Two agree modulo $10^e-1$, yielding a nonempty subset sum divisible by that modulus. Hence $k\ge9e$. Also $n<10^{e+1}$ and $e\ge1$, giving $9e>\log_{10}n$. For $2\le n\le8$, the positive integer $k$ is at least $1>\log_{10}n$. Thus $C_1=1$ and $C_2=48$ work.''')


def read(name):
    return json.loads((ROOT / name).read_text())


def write(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


bank = read('data/americas.json')
ids = {p['id'] for p in rows}
bank = [p for p in bank if p['id'] not in ids] + rows
write('data/americas.json', bank)

coverage = read('research/americas-coverage.json')
for field in ['fullyScreened', 'partiallyScreened']:
    coverage[field] = [p for p in coverage[field]
                       if not (p['competition'] == 'USAMO' and p['year'] in (2004, 2005))]
for year in (2004, 2005):
    paper = [p for p in rows if p['year'] == year]
    coverage['fullyScreened'].append(dict(competition='USAMO', year=year,
        ratings=[p['difficulty'] for p in paper], source=paper[0]['sourceUrl']))
coverage['papersScreened'] = len(coverage['fullyScreened'])
coverage['problemAppearancesScreened'] = sum(
    sum(isinstance(v, (int, float)) for v in (p['ratings'].values() if isinstance(p['ratings'], dict) else p['ratings']))
    for p in coverage['fullyScreened'] + coverage['partiallyScreened'])
coverage['uniqueIncluded'] = len(bank)
coverage['gaps'] = [
    'US: all USAJMO 2010–2026 and USAMO 2004–2025 papers fully screened. USAMO 1972–1995 Q1–5 and 1996–2003 Q1–6 remain unassessed (168 questions in 32 papers), with usable historical archives located. USAMO 2026 Q1 and Q3 remain held for incomplete source proofs. See research/americas/historical-inventory.json for exact year-by-year inventory.'
    if gap.startswith('US: all USAJMO') else gap for gap in coverage['gaps']]
note = ('USAMO 2004–2005: all twelve statements and arguments individually reviewed. '
        '2004 Q5 uses the stated positive domain (the source unnecessarily claims its auxiliary inequality for all reals). '
        '2005 Q6 has an independent digit-block/pigeonhole proof, with a strict upper-bound exponent that also covers triangular numbers equal to powers of ten. '
        '2005 Q3 explicitly states distinct interior points, as required for a nondegenerate cyclic conclusion.')
if note not in coverage['verificationNotes']:
    coverage['verificationNotes'].append(note)
write('research/americas-coverage.json', coverage)

inventory = read('research/americas/historical-inventory.json')
for paper in inventory['papers']:
    if paper['competition'] == 'USAMO' and paper['year'] in (2004, 2005):
        paper.update(assessedNumbers=list(map(str, range(1, 7))), unratedNumbers=[],
                     status='complete', sourceStatus='reviewed')
inventory['summary'].update(
    uniqueIncludedBeforeRootDuplicateMerge=len(bank),
    numericAssessments=coverage['problemAppearancesScreened'],
    fullyAssessedPapers=coverage['papersScreened'],
    priorityNumericAssessments=sum(len(p['assessedNumbers']) for p in inventory['papers']),
    priorityUnrated=sum(len(p['unratedNumbers']) for p in inventory['papers']))
script = Path(__file__).name
if script not in inventory['reproductionOrder']:
    inventory['reproductionOrder'].append(script)
write('research/americas/historical-inventory.json', inventory)
print(f'Added or refreshed {len(rows)} reviewed questions across two complete papers.')
