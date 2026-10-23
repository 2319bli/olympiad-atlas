"""Canonical subtopics derived from reviewed tags, with explicit per-problem edits.

This normalizes subject metadata only. It never assigns or changes difficulty.
Unclassified entries must be reviewed and added to subtopic-overrides.json.
"""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

RULES = {
 'Algebra': [
  ('Polynomials', r'polynom|vieta|irreducib|rational.?root|factor theorem|interpolat|degree argument|lowest coefficient'),
  ('Functional equations', r'functional|injectiv|surjectiv|additiv|multiplicativ|associativ|involution|^functions$'),
  ('Inequalities', r'inequal|am.gm|qm.am|cauchy|jensen|muirhead|majorization|convex|power mean|optim|schur|rearrangement|sharp bound|equality case|positivity|homogeneity|smoothing'),
  ('Sequences & recurrences', r'recurr|sequence|series|telescop|iteration|fibonacci|periodicity|summation|finite difference|generating function|sums of powers'),
  ('Equations & systems', r'^(?!.*functional).*equations|linear system|elimination|radicals|cube roots|quadratic functions|cyclic system|absolute value'),
  ('Algebraic identities', r'algebraic (identit|expression)|factorisation|factorization|sum of squares|cubic identit|symmetric (function|expression)|binomial'),
  ('Complex numbers', r'complex|roots of unity|conjugation'),
  ('Floors & fractional parts', r'floor|ceiling|fractional part|rounding'),
  ('Trigonometry', r'trigonom|sine|cosine|double.angle'),
  ('Rationality & irrationality', r'rationality|irrational|rational numbers|positive rationals'),
  ('Linear algebra', r'matrices|matrix|linear algebra|determinant|vector'),
  ('Calculus & modelling', r'calculus|modelling'),
  ('Functions & graphs', r'continuity|monotonicity|intermediate value|exponential function|affine function|^limits$|^range$|boundedness|^growth$'),
 ],
 'Combinatorics': [
  ('Pigeonhole principle', r'pigeonhole'),
  ('Invariants', r'invariant'),
  ('Monovariants', r'monovariant|termination'),
  ('Counting', r'counting|enumeration|binomial|factorial|catalan|stars and bars|inclusion.exclusion|probability|expectation|permutation|combinatorial identit'),
  ('Double counting', r'double counting|counting two ways|handshake'),
  ('Bijections', r'bijection|injection|complementation|equivalence classes'),
  ('Graph theory', r'graph|matchings?|ramsey|turán|turan|tournament|euler tour|hamilton|spanning tree|handshake|marriage lemma'),
  ('Colouring', r'colou?r|ramsey'),
  ('Games & strategies', r'games?|strategy|nim|winning'),
  ('Extremal arguments', r'extremal|optim|bounds?|averaging|means|convex'),
  ('Permutations & arrangements', r'permutation|arrangement|cyclic shift|inversions|binary strings|gray codes|latin squares|multiset'),
  ('Sets & partitions', r'\bsets?\b|subset|partition|set system|hitting sets'),
  ('Recurrences & generating functions', r'recurr|recurs|fibonacci|generating function|finite difference|catalan'),
  ('Tilings & dissections', r'tiling|dissection|polyomino|domino'),
  ('Combinatorial geometry', r'geometry|geometric|lattice|grid|covering|packing|noncrossing|spatial'),
  ('Algorithms & constructions', r'algorithm|greedy|construction|process|chip firing|sorting'),
  ('Logic & information', r'logic|information|weighing|decision|truth|liar'),
  ('Probability', r'probability|expectation|random'),
 ],
 'Number Theory': [
  ('Divisibility & GCD', r'divisib|divisors|factoriza|factorisa|greatest common|\bgcd\b|\blcm\b|coprim|common multiple|euclid|factor pairs|multiples|factor theorem'),
  ('Modular arithmetic', r'modul|congruence|residue|chinese remainder|fermat|euler|wilson|exponent reduction|remainders'),
  ('Diophantine equations', r'diophantine|pell|pythagorean|integer triangles|integer roots|quadratic forms|quadratic norm|integer constraints|vieta jumping|integer ratios|integer fractions|rational parametr'),
  ('Primes', r'prim(e|al)|composit|bertrand|pseudoprime|euclid argument'),
  ('Valuations', r'valuation|adic|prime exponents|highest power|lifting exponent|legendre formula'),
  ('Digits & bases', r'digit|decimal|binary|base (representation|three)|numeral|carr(y|ies|ying)|repdigit|bases|base representations'),
  ('Arithmetic functions', r'arithmetic function|number.theoretic function|divisor (function|sum|count)|number of divisors|sum of divisors|multiplicative function|totient|[τσφ]'),
  ('Squares & powers', r'squares|squarefree|perfect power|powers|cubes|cube.free|triangular numbers|between powers|sum of two squares'),
  ('Sequences & recurrences', r'recurr|sequence|fibonacci|progression|period|iteration|dynamics|cycles|orbits|geometric series'),
  ('Descent', r'descent|vieta jumping'),
  ('Factorials & binomial coefficients', r'factorial|binomial|trinomial|lucas theorem'),
  ('Multiplicative order', r'multiplicative order|primitive roots|multiplicative subgroup'),
  ('Fractions & approximation', r'egyptian|unit fractions|farey|approximation|rational squares|^rationals$|rational numbers'),
  ('Floors & fractional parts', r'floor|ceiling|fractional part|rounding'),
  ('Integer polynomials', r'polynom|factor theorem|rational.?root theorem|cyclotomic'),
 ],
 'Geometry': [
  ('Angles & cyclic quadrilaterals', r'angle chas|cyclic|concyclic|inscribed angles|circle angles|directed angles|angle sums|special angles'),
  ('Circles & tangency', r'circl|tangen|chord|diameter|arc midpoint|circumradius|incircle|inradius'),
  ('Similarity & congruence', r'similar|congruen|equal ratios|distance ratios'),
  ('Triangle centres', r'triangle cent|orthocent|circumcent|incent|excent|centroid|euler line|nine.point|symmedian|napoleon|fermat point'),
  ('Area & dissection', r'area|dissect|heron|geometric partition'),
  ('Coordinates & vectors', r'coordinat|vector|complex numbers|dot products|slopes|analytic|affine geometry'),
  ('Transformations', r'homothe|reflect|rotat|inversion|transform|isometr|central symmetry|point symmetry|affine construction'),
  ('Trigonometry', r'trigonom|cosine|sine|double.angle|half.angle|half angles'),
  ('Geometric inequalities', r'inequal|optim|bounds|minimum|minimisation|minimization|maximiz|sharp constant|am.gm|cauchy|jensen|extremal'),
  ('Constructions & loci', r'construct|loci|locus|fixed point|circle of apollonius|apollonius circle'),
  ('Solid geometry', r'solid|spatial|3d|three.dimensional|tetrahedr|volume|sphere|cones|dihedral|cylinder|skew lines|plane sections|surface area'),
  ('Power of a point & radical axes', r'power of a point|radical|coaxal'),
  ('Concurrency & collinearity', r'concurren|collinear|ceva|menelaus|simson|desargues|pappus'),
  ('Triangle geometry', r'triangl|bisector|altitude|median|cevians|midpoint|stewart|pythagoras|orthic'),
  ('Quadrilaterals & polygons', r'quadrilat|polygon|parallelogram|rhomb|rhombi|rectangle|trapez|square|pentagon|hexagon|ptolemy'),
  ('Combinatorial geometry', r'combinatori|pigeonhole|packing|covering|lattice|grid|convex hull|finite point|line arrangement|graph|geometric partition'),
  ('Projective geometry & conics', r'projective|polar|harmonic|conic|ellipse|parabol|isogonal|isotomic'),
 ]
}
COMMON = [
 ('Pigeonhole principle',r'pigeonhole'),
 ('Invariants',r'invariant'),
 ('Monovariants',r'monovariant'),
 ('Extremal arguments',r'extremal'),
 ('Parity',r'parity'),
 ('Modular arithmetic',r'modular|congruence'),
 ('Induction',r'\binduction\b|inductive'),
 ('Pairing',r'\bpairing\b'),
 ('Symmetry',r'\bsymmetr'),
]
# These bundled legacy labels do not identify which of their methods is used.
AMBIGUOUS = {'invariants / monovariants','coloring schemes, extremal arguments','techniques: modulo, size analysis, order analysis, inequalities','induction / smoothing','games / greedy algorithms','recursion, bijection','equations and inequalities','other','miscellaneous'}
OVERRIDES = json.loads((ROOT/'data/subtopic-overrides.json').read_text()) if (ROOT/'data/subtopic-overrides.json').exists() else {}
TAXONOMY = {topic: sorted(set(n for n,_ in rules+COMMON)) for topic,rules in RULES.items()}

def classify(problem):
    if problem['id'] in OVERRIDES:return OVERRIDES[problem['id']]
    if problem.get('subtopics'):
        aliases={'Extremal principle':'Extremal arguments','Centres & cevians':'Triangle centres','Exponents':'Squares & powers','Binary representation':'Digits & bases','Graphs':'Graph theory','Power of a point':'Power of a point & radical axes','Continuity':'Functions & graphs','Finite differences':'Sequences & recurrences'}
        # Restored reviews retain their precise technique tags. Normalize their
        # synonymous or narrower subtopic labels into the existing filter groups.
        groups={
            'Inequalities':['AM–GM','AM–GM inequality','Series bounds'],
            'Equations & systems':['Absolute values','Discriminants','Exponential equations','Quadratic equations','Radicals','Ratios & proportions','Systems of equations'],
            'Angles & cyclic quadrilaterals':['Angle chasing','Cyclic quadrilaterals','Parallel lines','Perpendicularity'],
            'Circles & tangency':['Arc midpoints','Circle sectors','Circles & chords','Incircles'],
            'Area & dissection':['Area','Areas'],
            'Extremal arguments':['Averaging'],
            'Modular arithmetic':['Chinese remainder theorem'],
            'Concurrency & collinearity':['Collinearity','Concurrency'],
            'Algorithms & constructions':['Constructions'],
            'Trigonometry':['Cosine rule'],
            'Divisibility & GCD':['Divisors'],
            'Triangle geometry':['Angle bisectors','Equilateral triangles','Medians','Midpoints','Pythagoras','Right triangles'],
            'Diophantine equations':['Exponential Diophantine equations','Integer constraints'],
            'Factorials & binomial coefficients':['Factorials'],
            'Squares & powers':['Figurate numbers','Perfect squares','Powers'],
            'Floors & fractional parts':['Floor & ceiling functions'],
            'Sequences & recurrences':['Geometric series','Periodicity','Sums of powers','Telescoping sums'],
            'Combinatorial geometry':['Grids'],
            'Descent':['Infinite descent'],
            'Transformations':['Inversion'],
            'Rationality & irrationality':['Irrationality'],
            'Algebraic identities':['Logarithms'],
            'Logic & information':['Logic'],
            'Graph theory':['Matchings'],
            'Functions & graphs':['Monotonicity'],
            'Triangle centres':['Orthocentres'],
            'Quadrilaterals & polygons':['Ptolemy','Regular polygons'],
            'Polynomials':['Repeated roots','Vieta','Vieta’s formulas'],
            'Sets & partitions':['Sets','Subsets'],
            'Similarity & congruence':['Similar triangles'],
            'Tilings & dissections':['Tilings & coverings'],
            'Geometric inequalities':['Triangle inequality'],
            'Solid geometry':['Volumes'],
        }
        aliases.update({alias:label for label,names in groups.items() for alias in names})
        aliases['Factorisation']='Divisibility & GCD' if problem['topic']=='Number Theory' else 'Algebraic identities'
        aliases['Binomial coefficients']='Counting' if problem['topic']=='Combinatorics' else 'Factorials & binomial coefficients'
        aliases['Rational numbers']='Fractions & approximation' if problem['topic']=='Number Theory' else 'Rationality & irrationality'
        # These broad descriptors remain available in hidden technique tags.
        labels=[aliases.get(s,s) for s in problem['subtopics'] if s not in {'Casework','Products','Sums & products','Substitution'}]
        return list(dict.fromkeys(labels or problem['subtopics']))
    tags=[str(t).lower().replace('–','-').replace('—','-') for t in problem.get('tags',[])]
    tags=[t for t in tags if t not in AMBIGUOUS]
    labels=[]
    for label,pattern in RULES[problem['topic']]+COMMON:
        if label not in labels and any(re.search(pattern,t) for t in tags):labels.append(label)
    # Keep all supported categories; the UI can display a compact summary.
    return labels

if __name__=='__main__':
    from collections import Counter
    problems=json.loads((ROOT/'dist/data/problems.json').read_text())
    missing=[]
    for p in problems:
        p['subtopics']=classify(p)
        if not p['subtopics']:missing.append({k:p.get(k) for k in ['id','topic','tags','statement','ratingReason']})
    (ROOT/'research/subtopic-unclassified.json').write_text(json.dumps(missing,ensure_ascii=False,indent=2))
    print(json.dumps({'classified':len(problems)-len(missing),'missing':len(missing),'counts':dict(Counter(s for p in problems for s in p['subtopics']))},indent=2))
