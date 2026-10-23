import json
from pathlib import Path
R=Path(__file__).resolve().parents[2];data=json.loads((R/'data/americas.json').read_text());c=json.loads((R/'research/americas-coverage.json').read_text());new=[];rr={};nn={}
def a(y,n,d,t,s,st,why):
 rr.setdefault(y,{})[str(n)]=d;nn.setdefault(y,{})[str(n)]=why
 if not 4<=d<=7:return
 u=f'https://cms.math.ca/wp-content/uploads/2019/07/sol{y}.pdf'
 new.append(dict(id=f'ca-cmo-{y}-{n}',country='Canada',competition='CMO',year=y,section='National final',number=str(n),statement=st,solution=f'[Read the official worked solution, Problem {n}]({u}).',sourceUrl=f'https://cms.math.ca/wp-content/uploads/2019/07/exam{y}.pdf',solutionUrl=u,solutionKind='source-link',topic=t,tags=s,subtopics=s,difficulty=d,ratingReason=why,reviewStatus='individually-assessed',notes='Statement restated in original wording. Official CMS scanned solution reviewed with OCR and mathematical reconstruction.'))
a(1995,1,3,'Algebra',[],None,'Pair x with 1−x: for f(x)=9^x/(9^x+3), the two values sum to 1, with the middle term 1/2.')
a(1995,2,5,'Algebra',['Inequalities'],r'Prove that $a^a b^b c^c\ge(abc)^{(a+b+c)/3}$ for all positive real $a,b,c$.','After cubing and dividing, factor the ratio into (a/b)^(a−b)(b/c)^(b−c)(a/c)^(a−c). Each factor is at least 1; identifying this pairwise-difference factorization is the substantive step.')
a(1995,3,5,'Geometry',['Area & dissection','Combinatorial geometry'],r'A convex $s$-gon is partitioned into $q$ simple quadrilaterals with pairwise disjoint interiors. Exactly $b$ of the pieces have a reflex interior angle. Prove $q\ge b+(s-2)/2$.','Every reflex vertex is interior and belongs to only one reflex quadrilateral, so it contributes a full 2π angle sum in the subdivision. Combine these disjoint contributions with the boundary angle sum and compare with 2πq.')
a(1995,4,4,'Number Theory',['Diophantine equations','Squares & powers'],r'For fixed integers $n\ge1$ and $k\ge0$, prove that $x_1^3+\cdots+x_n^3=y^{3k+2}$ has infinitely many positive integer solutions.','Set all xᵢ equal and balance the two exponents of n: xᵢ=n^(2k+1)q^(3k+2), y=n²q³. The problem reduces to choosing exponents so that 1+3(2k+1)=2(3k+2).')
a(1995,5,5.5,'Algebra',['Sequences & recurrences','Inequalities'],r'Fix $0<u<1$ and define $f(x)=0$ on $0\le x\le u$, while $f(x)=1-(\sqrt{ux}+\sqrt{(1-u)(1-x)})^2$ on $u\le x\le1$. Let $u_1=f(1)$ and $u_n=f(u_{n-1})$ for $n>1$. Prove that some $u_k$ is zero.','Cauchy keeps every iterate nonnegative. For x≥u, bound the cross radical below by u(1−x) to obtain f(x)≤x−u. This uniform decrease, stronger than mere monotonicity, forces an iterate into the zero interval.')
a(1994,1,3,'Algebra',[],None,'Split (n²+n+1)/n! into (n+1)/(n−1)!+(n+1)/n!, so the alternating sum telescopes.')
a(1994,2,4.5,'Number Theory',['Squares & powers','Sequences & recurrences'],r'For each positive integer $n$, show that $(\sqrt2-1)^n=\sqrt m-\sqrt{m-1}$ for some positive integer $m$.','Pair the power with its reciprocal (√2+1)^n. Their half-sum and half-difference have squares differing by 1; conjugation and parity of n show both squares are integers.')
a(1994,3,4.5,'Combinatorics',['Monovariants','Parity'],r'Twenty-five people sit around a circle and simultaneously vote yes or no at each round. At the next round, a person keeps the previous vote if at least one neighbour agreed, and switches if both disagreed. Prove that eventually no vote ever changes.','Any adjacent agreeing pair remains fixed forever. Odd cycle length guarantees such a pair, and the set of fixed agreeing voters expands across every boundary until the entire circle stabilizes.')
a(1994,4,3.5,'Geometry',[],None,'The diameter gives two right triangles. Multiplying the cosine ratios gives cos²(angle APB)=st, with sign determined by whether P is outside or inside the circle.')
a(1994,5,5,'Geometry',['Concurrency & collinearity','Similarity & congruence'],r'In acute triangle $ABC$, let $AD\perp BC$ and take $H$ inside segment $AD$. Lines $BH,CH$ meet $AC,AB$ at $E,F$. Prove $\angle EDH=\angle FDH$.','Extend DE and DF to the parallel to BC through A. Similar triangles express the two intercepts, and Ceva makes them equal. The altitude then bisects the resulting isosceles triangle angle.')
ids={r['id'] for r in new};data=[r for r in data if r['id'] not in ids]+new
# Canonical category fixes; tags may still describe additional methods.
for p in data:
 if p['id']=='ca-cmo-2003-5':p['subtopics']=['Combinatorial geometry','Extremal arguments']
 if p['id']=='ca-cmo-1997-1':p['subtopics']=['Divisibility & GCD','Primes']
 if p['id']=='ca-cmo-2008-4':p['subtopics']=['Primes','Modular arithmetic','Divisibility & GCD']
(R/'data/americas.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
for y,rs in rr.items():
 c['fullyScreened']=[x for x in c['fullyScreened'] if not(x['competition']=='CMO' and x['year']==y)]
 c['fullyScreened'].append(dict(competition='CMO',year=y,ratings=rs,source=f'https://cms.math.ca/wp-content/uploads/2019/07/sol{y}.pdf',assessmentNotes=nn[y]))
for y,note in {2008:'Q3 above target: maximizing a boundary-path component and carefully rerouting edges enables induction after peeling a zigzag strip. The need to preserve the number of components while preventing cycles makes this a substantially advanced combinatorial argument.',2009:'Q3 above target: existence requires a tiling-preserving lower-left induction, while uniqueness overlays two tilings into alternating cycles and propagates a staircase to a forced orientation contradiction. The simply connected hypothesis is essential.'}.items():
 p=next(x for x in c['partiallyScreened']+c['fullyScreened'] if x['competition']=='USAMO' and x['year']==y)
 for key in ['partiallyScreened','fullyScreened']:c[key]=[x for x in c[key] if not(x['competition']=='USAMO' and x['year']==y)]
 p['ratings']['3']=9;p.pop('pending',None);p['assessmentNotes']={'3':note};p['source']=f'https://web.evanchen.cc/exams/USAMO-{y}-notes.pdf';c['fullyScreened'].append(p)
c['papersScreened']=len(c['fullyScreened']);c['problemAppearancesScreened']=sum(len(x['ratings']) for x in c['fullyScreened']+c['partiallyScreened']);c['uniqueIncluded']=len(data)
c['gaps'][0]='Canada: CMO 1994–2026 fully screened except CMO 2001 Q5, held for an undefined 0/0 ratio in its published formulation. CMO 1969–1993 remains under review; the official archive has papers but no linked solutions for those years. All CJMO 2020–2026 fully screened.'
(R/'research/americas-coverage.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n');print(len(new),'new;',len(data),'total;',c['papersScreened'],'complete')
