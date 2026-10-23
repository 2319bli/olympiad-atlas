"""Content checks for individually assessed problems restored outside 4–7.

Executed by build_international.py. These edits preserve the review ratings.
"""
import sys
sys.path.insert(0,str(root/'research'))
from subtopics import classify
topic_fixes={
 'apm_2025_7619c0':'Number Theory','apm_2025_092270':'Number Theory',
 'apm_2023_effff8':'Combinatorics','apm_2020_f3d3c1':'Combinatorics',
 'apm_2019_3a3563':'Combinatorics','rmm_2021_7ba909':'Combinatorics',
 'zhk_2021_ef5d05':'Combinatorics','btw_2023_8b7d30':'Combinatorics',
 'bmo_2023_e5c358':'Number Theory','bmo_2024_0c40d1':'Number Theory',
 'imo_2024_95e706':'Combinatorics','imo_2024_1d16c9':'Number Theory',
 'imo_2024_3f4e9a':'Number Theory','imo_2024_7201b9':'Number Theory',
 'imo_1970_official_p2':'Number Theory',
}
explicit={
 'imo_2024_ce5613':['Functional equations','Sets & partitions','Squares & powers'],
 'imo_2025_official_p3':['Functional equations','Divisibility & GCD','Primes'],
 'imo_2025_official_p6':['Tilings & dissections','Extremal arguments','Combinatorial geometry'],
 'imo_2026_official_p3':['Games & strategies','Extremal arguments'],
 'imo_2026_official_p6':['Primes','Divisibility & GCD','Sequences & recurrences'],
 'imo_1959_official_p1':['Divisibility & GCD'],
 'imo_1959_official_p2':['Equations & systems'],
 'imo_1959_official_p3':['Trigonometry','Polynomials'],
 'imo_1959_official_p4':['Constructions & loci','Triangle geometry'],
 'imo_1960_official_p2':['Inequalities','Equations & systems'],
 'imo_1960_official_p3':['Trigonometry','Triangle geometry'],
 'imo_1960_official_p5':['Solid geometry','Constructions & loci','Coordinates & vectors'],
 'imo_1960_official_p7':['Constructions & loci','Quadrilaterals & polygons'],
 'imo_1961_official_p1':['Equations & systems','Polynomials'],
 'imo_1961_official_p2':['Geometric inequalities','Area & dissection'],
 'imo_1961_official_p3':['Trigonometry','Equations & systems'],
 'imo_1961_official_p4':['Area & dissection','Triangle geometry'],
 'imo_1961_official_p6':['Solid geometry','Coordinates & vectors','Constructions & loci'],
 'imo_1962_official_p1':['Digits & bases','Divisibility & GCD'],
 'imo_1962_official_p2':['Inequalities','Equations & systems'],
 'imo_1962_official_p3':['Solid geometry','Constructions & loci'],
 'imo_1962_official_p4':['Trigonometry','Equations & systems'],
 'imo_1962_official_p6':['Triangle centres','Circles & tangency'],
 'imo_1963_official_p1':['Equations & systems'],
 'imo_1963_official_p5':['Trigonometry','Algebraic identities'],
 'imo_1963_official_p6':['Permutations & arrangements','Logic & information'],
 'imo_1964_official_p1':['Modular arithmetic','Multiplicative order'],
 'imo_1964_official_p2':['Inequalities','Algebraic identities'],
 'imo_1964_official_p3':['Circles & tangency','Similarity & congruence','Area & dissection'],
 'imo_1965_official_p1':['Trigonometry','Inequalities'],
 'imo_1965_official_p2':['Linear algebra','Extremal arguments'],
 'imo_1966_official_p1':['Counting','Sets & partitions'],
 'imo_1966_official_p2':['Trigonometry','Triangle geometry'],
 'imo_1966_official_p4':['Trigonometry','Sequences & recurrences'],
 'imo_1966_official_p6':['Area & dissection','Geometric inequalities'],
 'imo_1968_official_p2':['Digits & bases','Diophantine equations'],
 'imo_1968_official_p3':['Sequences & recurrences','Equations & systems','Extremal arguments'],
 'imo_1968_official_p4':['Solid geometry','Geometric inequalities'],
 'imo_1968_official_p5':['Functional equations','Sequences & recurrences'],
 'imo_1970_official_p1':['Area & dissection','Circles & tangency','Triangle geometry'],
 'imo_1970_official_p2':['Digits & bases','Fractions & approximation'],
 'imo_1971_official_p4':['Solid geometry','Transformations','Geometric inequalities'],
 'imo_1972_official_p1':['Pigeonhole principle','Sets & partitions'],
 'apm_2025_e1a993':['Invariants','Graph theory','Algorithms & constructions'],
 'apm_2023_effff8':['Combinatorial geometry','Invariants','Induction'],
 'apm_2022_04f0c2':['Games & strategies','Invariants','Induction'],
 'egm_2025_b50ee2':['Colouring','Invariants','Combinatorial geometry'],
 'apm_2019_3a3563':['Invariants','Modular arithmetic','Combinatorial geometry'],
 'bmo_2024_22c656':['Games & strategies','Invariants','Induction'],
 'zhk_2021_ef5d05':['Graph theory','Invariants','Extremal arguments'],
 'zhk_2021_96d201':['Games & strategies','Invariants'],
 'btw_2023_8b7d30':['Combinatorial geometry','Extremal arguments','Algorithms & constructions'],
 'btw_2023_58a295':['Games & strategies','Modular arithmetic'],
 'bmo_2023_be5fcc':['Sets & partitions','Extremal arguments','Algorithms & constructions'],
 'imo_2024_34fef6':['Colouring','Invariants','Algorithms & constructions'],
 'imo_2024_7579e8':['Games & strategies','Logic & information','Combinatorial geometry'],
 'imo_2024_1fd9d0':['Games & strategies','Invariants'],
 'imo_2024_91fd1f':['Algorithms & constructions','Extremal arguments'],
 'imo_2024_95e706':['Recurrences & generating functions','Invariants','Extremal arguments'],
 'imo_2023_73cc8d':['Graph theory','Colouring','Extremal arguments'],
 'imo_2022_34151b':['Double counting','Extremal arguments','Combinatorial geometry'],
 'ibe_2002_a4c329':['Games & strategies','Invariants','Extremal arguments'],
}
paraphrases={
 'rou_2025_742b0e':r'Fix $n\ge3$. Find the least positive integer $k$ such that the following is possible for every tree on labelled vertices $v_1,\ldots,v_n$ and every choice of distinct complex numbers $z_1,\ldots,z_n$: a polynomial $P(X,Y)$ over $\mathbb C$, of total degree at most $k$, satisfies $P(z_i,z_j)=0$ exactly for those distinct $i,j$ whose vertices are adjacent.',
 'rou_2025_9e5c95':r'In acute triangle $ABC$ with $AB<AC$, write $H,O$ for the orthocentre and circumcentre, and let $\Gamma$ be circle $BOC$. Its second intersections with line $AO$ and with the circle centred at $A$ through $O$ are $A\prime$ and $F$, respectively. Prove that $\Gamma$, the circle with diameter $AA\prime$, and circle $AFH$ share a point.',
 'rou_2025_b5cc5a':r'For integers $k,m>1$, take $k$ disjoint sets $S_i$, each containing one red element and $m$ blue elements. Let $\mathcal F$ consist of all subsets of their union whose intersection with each $S_i$ is monochromatic, allowing the empty intersection. What is the maximum size of a pairwise-intersecting subfamily of $\mathcal F$?',
}
for item in out:
 ident=item['id']
 item['topic']=topic_fixes.get(ident,{'Number theory':'Number Theory'}.get(item['topic'],item['topic']))
 if ident in explicit:item['subtopics']=explicit[ident]
 if not item.get('subtopics'):item['subtopics']=classify(item)
 if ident=='egm_2025_af59a0':item['statement']=item['statement'].split('\n\nWhat is')[0]
 if ident=='imo_2024_7579e8':item['statement']=item['statement'].split('\nComment.')[0]
 if ident in paraphrases:
  item['statement']=paraphrases[ident];item['solution']=None;item['solutionKind']='source-link'
  item['notes']='Mathematical statement independently paraphrased from the official paper. The organiser’s worked solution is linked. Individual difficulty estimate preserved from the completed review.'
 if ident=='btw_2023_9cdd34':
  item['solution']=r'Put $Y=\sum_i\sqrt{y_i}$. Multiplying the cyclic inequalities yields $\prod_i y_i\ge1$, so AM–GM gives $Y\ge n$. The triangle inequality for the vectors $(x_i-x_{i-1},\sqrt{y_i})$ now gives $$\sum_{i=1}^n\sqrt{(x_i-x_{i-1})^2+y_i}\ge\sqrt{(x_n-x_0)^2+Y^2}\ge n\sqrt2.$$ Equality is attained by $x_i=i$ and $y_i=1$, which satisfy every condition. Thus the minimum is $n\sqrt2$.'
  item['solutionKind']='original-exposition'
 if ident=='imo_2024_bbfb5c':
  item['solution']=None;item['solutionKind']='source-link'
  item['notes']+=' The extracted proof has damaged angle notation; use the linked source for the worked solution.'
 if item.get('solution'):item['solution']=item['solution'].replace(r'\Varangle',r'\measuredangle')
 assert item['subtopics'],f'Missing subtopics: {ident}'
