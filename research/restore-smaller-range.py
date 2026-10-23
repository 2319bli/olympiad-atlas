"""Restore individually reviewed questions irrespective of preferred difficulty.

Statements/subtopics in the four TSVs were manually checked against the cached
original papers. Ratings and reasoning are copied unchanged from the review
ledgers. No rating is inferred here. Safe to rerun after a regional builder.
"""
import json, re, datetime, sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'research'))
from subtopics import TAXONOMY
TOPICS={'A':'Algebra','N':'Number Theory','C':'Combinatorics','G':'Geometry'}
ALIASES={'Angle chasing':'Angles & cyclic quadrilaterals','Cyclic quadrilaterals':'Angles & cyclic quadrilaterals','Angles':'Angles & cyclic quadrilaterals','Angle bisectors':'Triangle geometry','Power of a point':'Power of a point & radical axes','Floor functions':'Floors & fractional parts','Geometric loci':'Constructions & loci','Tiling & dissection':'Tilings & dissections','Probability & expectation':'Probability','Factorials':'Factorials & binomial coefficients','Binomial coefficients':'Factorials & binomial coefficients','Telescoping':'Sequences & recurrences','Periodicity':'Sequences & recurrences','Partial sums':'Sequences & recurrences','Logarithms':'Functions & graphs','Convexity':'Geometric inequalities','Inclusion–exclusion':'Counting'}
ALL_TAGS=set().union(*map(set,TAXONOMY.values()))
def read(file):return json.loads((R/file).read_text())
def write(file,data):(R/file).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def key(x):return x['country'],x['year'],x.get('section',''),str(x['number'])
def main(regions=None):
 for region in regions or ['ireland','nordic','baltic','belgium']:
  statements={}
  for line in (R/f'research/{region}/range-statements.tsv').read_text().splitlines():
   short,topic,tags,statement=line.split('|',3)
   tags=[ALIASES.get(t,t) for t in tags.split(',')]
   if topic=='G':tags=[{'Inequalities':'Geometric inequalities','Complex numbers':'Coordinates & vectors'}.get(t,t) for t in tags]
   if topic=='C':tags=[{'Sequences & recurrences':'Recurrences & generating functions','Factorials & binomial coefficients':'Counting'}.get(t,t) for t in tags]
   if topic=='N':tags=[{'Equations & systems':'Diophantine equations','Polynomials':'Integer polynomials'}.get(t,t) for t in tags]
   if topic=='A':tags=[{'Factorials & binomial coefficients':'Algebraic identities'}.get(t,t) for t in tags]
   if topic=='G':tags=[{'Tilings & dissections':'Area & dissection'}.get(t,t) for t in tags]
   tags=list(dict.fromkeys(t for t in tags if t in TAXONOMY[TOPICS[topic]]));assert tags,(short,tags)
   statements[short]={'topic':TOPICS[topic],'tags':tags,'subtopics':tags,'statement':statement.replace(r'\n','\n')}
  rows=read(f'data/{region}.json'); cov=read(f'research/{region}-coverage.json');byid={p['id']:p for p in rows};added=[]
  if region=='ireland':
   # Reuse the original source-page/date logic without running its dataset builder.
   path=R/'research/ireland/build.py'; env={'__file__':str(path)}
   exec(path.read_text().split('add(2026,2,')[0],env)
  for d in cov['decisions']:
   if d.get('difficulty') is None or d.get('duplicateOf'):continue
   if region=='ireland':short=d['id'].removeprefix('irmo-'); ident=d['id']
   elif region=='nordic':short=f"{d['country'].lower()}-{d['year']}-{d['number']}";ident='nordic-'+short
   elif region=='belgium':short=f"{d['year']}-{d['section'].split()[0].lower()}-{d['number']}";ident='belgium-omb-'+short
   else:short=f"{d['country'].lower()}-{d['year']}-{d['section'].replace(' ','-')}-{d['number']}";ident='baltic-'+short
   if short not in statements:continue
   if region=='ireland':
    md=env['meta'](d['year'],int(d['number']),int(d['section'][-1])); meta={'sourceUrl':env['base']+f"#page={md['page']}",'sittingDate':md['date']}
   else:
    candidates=[p for p in cov['papers'] if p['country']==d['country'] and p['year']==d['year'] and p.get('section','')==d.get('section','')]
    assert len(candidates)==1,(region,d,candidates)
    meta={k:v for k,v in candidates[0].items() if k in ['sourceUrl','solutionUrl','sittingDate']}
   p={k:d[k] for k in ['country','competition','year','section','number','difficulty']}
   p.update(meta);p.update(statements[short]);p.update(id=ident,ratingReason=d.get('ratingReason',d.get('reason')),reviewStatus='individually-assessed')
   p['notes']='English mathematical paraphrase checked against the original paper. The original individual difficulty assessment is retained; 4–7 is a preferred browsing range, not an inclusion cutoff.'
   if region=='ireland':p['notes']+=' The UCD compendium provides statements and selected hints, not complete worked solutions; no worked solution is asserted for this entry.'
   else:p.update(solutionKind='source-link',solutionCredit='Official competition worked solutions, in the original language')
   if 'assets/range-restoration/' in p['statement']:p['notes']+=' Diagram reproduced from the linked official competition paper.'
   if region=='nordic' and ident=='nordic-iceland-2026-6':p['notes']+=' The official Icelandic problem/solution booklet explicitly requires capture regardless of initial positions; that condition is missing from the English translation and is restored here.'
   if ident not in byid:rows.append(p);byid[ident]=p;added.append(ident)
   else:byid[ident].update(p)
   d.update(id=ident,included=True)
  # Preserve a separate appearance when the newly restored Lithuanian geometry task
  # appears unchanged in both age groups.
  if region=='baltic':
   p=byid['baltic-lithuania-2025-Grades-9–10-2']
   appearance={k:p[k] for k in ['country','competition','year','number','sourceUrl','solutionUrl','sittingDate']}|{'section':'Grades 11–12'}
   if appearance not in p.setdefault('appearances',[]):p['appearances'].append(appearance)
   for d in cov['decisions']:
    if d.get('duplicateOf') and d['country']=='Lithuania' and d['year']==2025 and d['number']=='2':d['included']=True
  if region=='ireland':
   held=next(d for d in cov['decisions'] if d['id']=='irmo-1988-15');held['status']='withheld-source'
   cov['excludedCount']=sum(not d.get('included') and isinstance(d.get('difficulty'),(int,float)) for d in cov['decisions'])
   cov['solutionGapIds']=[p['id'] for p in rows if not p.get('solution') and p.get('solutionKind')!='source-link']
   cov['gaps']=[n.replace('every addition from the 2003–2024 completion pass has independently checked exposition or an exact official solution link.','the restored out-of-range entries retain the compendium statement source, and missing worked solutions are recorded explicitly.') for n in cov['gaps']]
  cov['includedCount']=len(rows)
  cov['inclusionPolicy']='All valid individually assessed questions are eligible on the 1–10 scale; 4–7 is only the preferred browsing range. Genuine unresolved source/proof issues remain held.'
  # Paper completeness is a review property and stays unchanged.
  for paper in cov.get('papers',[]):
   for field in ['included','includedCount']:
    if field in paper:paper[field]=sum(p['country']==paper['country'] and p['year']==paper['year'] and p.get('section','')==paper.get('section','') for p in rows)
  write(f'data/{region}.json',rows);write(f'research/{region}-coverage.json',cov)
  print(region,'added',len(added),'total',len(rows))
if __name__=='__main__':main(sys.argv[1:] or None)
