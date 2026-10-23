"""Restore individually reviewed questions previously omitted by the 4–7 filter.

This is additive and preserves the existing bank. Ratings are copied from the
review ledger; statements and topic classifications are explicit below or in
restoration-records.json. Source/proof holds and unrated questions stay held.
"""
import json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(R/'research'))
from subtopics import classify
P=R/'research/americas'
bank=json.loads((R/'data/americas.json').read_text())
cov=json.loads((R/'research/americas-coverage.json').read_text())
ratings={};papers={}
for p in cov['fullyScreened']+cov['partiallyScreened']:
 rs=p['ratings'];rs=dict(enumerate(rs,1)) if isinstance(rs,list) else rs
 for n,d in rs.items():ratings[p['competition'],p['year'],str(n)]=d;papers[p['competition'],p['year'],str(n)]=p
seen={(p['competition'],p['year'],str(p['number'])) for p in bank}
for p in bank:
 for a in p.get('appearances',[]):seen.add((a['competition'],a['year'],str(a['number'])))
new=[]
def add(comp,y,n,topic,tags,statement,reason='',country=None,source=None,solutionUrl=None,solution=None,ident=None,notes='',appearances=None,solutionAvailable=True):
 key=comp,y,str(n)
 if key in seen:return
 p=papers[key];d=ratings[key]
 assert isinstance(d,(int,float)) and 1<=d<=10,key
 if not reason:reason=p.get('assessmentNotes',{}).get(str(n),'')
 assert statement and reason and topic,key
 country=country or ('Canada' if comp in ['CMO','CJMO'] else 'United States')
 ident=ident or ('ca-' if country=='Canada' else 'us-')+comp.lower()+f'-{y}-{n}'
 if not source:source=(f'https://web.evanchen.cc/exams/{"JMO" if comp=="USAJMO" else "USAMO"}-{y}-notes.pdf' if country=='United States' else p.get('source'))
 row=dict(id=ident,country=country,competition=comp,year=y,number=str(n),difficulty=d,topic=topic,tags=tags,subtopics=tags,statement=statement,ratingReason=reason,reviewStatus='individually-assessed',sourceUrl=source,solutionUrl=solutionUrl or source,solutionKind='original-exposition' if solution else 'source-link',notes=notes or 'Restored from the individual review after removing the publication difficulty cutoff. Rating unchanged; statement and subject metadata checked against the source.')
 if country=='Canada' and y<1994 and not solution and not solutionUrl:
  row.pop('solutionUrl',None);row.pop('solutionKind',None)
 if not solutionAvailable:
  row.pop('solutionUrl',None);row.pop('solutionKind',None)
 if solution:row['solution']=solution
 if appearances:row['appearances']=appearances
 row['subtopics']=classify(row)
 new.append(row);seen.add(key)
 for a in appearances or []:seen.add((a['competition'],a['year'],str(a['number'])))

# Full statements retained in the reviewed MathNet transcriptions. Link to the
# author-maintained solution notes rather than reproduce potentially flawed OCR.
raw_reviews={
(2006,3):('Number Theory',['Polynomials','Primes','Modular arithmetic'],'The necessity direction combines infinitely many prime divisors of polynomial values with a bounded-residue argument to force very special linear factors; checking the proposed family is only the easy half.'),
(2006,5):('Combinatorics',['Invariants','Valuations','Extremal arguments'],'The key is a minimal counterexample and comparison of paths across a power-of-two barrier; the longest jump and its valuation must be controlled together.'),
(2007,2):('Geometry',['Circles & tangency','Geometric inequalities','Combinatorial geometry'],'A maximal empty disc converts a global infinite covering question into three tangencies and a sharp metric bound. Establishing that extremal configuration is the central difficulty.'),
(2007,5):('Number Theory',['Divisibility & GCD','Algebraic identities','Induction'],'Induction needs a non-obvious difference-of-squares factorization of the cyclotomic quotient, using the special power of seven to make both factors integral and greater than one.'),
(2007,6):('Geometry',['Inversion','Circles & tangency','Geometric inequalities'],'Inversion at a vertex exposes the distance between the two auxiliary centres; obtaining that formula in all three positions is substantially harder than the final AM–GM product bound.'),
(2010,3):('Algebra',['Inequalities','Sequences & recurrences','Extremal arguments'],'Pairing neighbouring indices gives a quick upper bound, but a highly structured backward recurrence is needed to attain it while satisfying every pairwise constraint.'),
(2010,6):('Combinatorics',['Probability','Extremal arguments','Algorithms & constructions'],'A biased random choice tuned to the golden ratio yields the guarantee; a matching extremal arrangement and integer rounding are both essential to the exact answer.'),
(2011,3):('Geometry',['Coordinates & vectors','Transformations','Concurrency & collinearity'],'The hidden model is formed by reflections of a triangle. Proving that the angle and side data force this model requires a careful vector uniqueness argument before concurrency follows.'),
(2012,3):('Number Theory',['Chinese remainder theorem','Algorithms & constructions','Sequences & recurrences'],'For the positive cases the infinite construction needs a specially ordered partition of the integers and repeated compatible Diophantine extensions; ordinary induction does not close.'),
(2013,2):('Combinatorics',['Counting','Recurrences & generating functions','Permutations & arrangements'],'The two circuits must be encoded through the nonadjacent points visited twice. Avoiding repeated moves creates a parity restriction that complicates both the count and recurrence.'),
(2013,3):('Combinatorics',['Linear algebra','Parity','Extremal arguments'],'Encoding line flips over the two-element field is only the beginning: one must determine all zero-effect operations and then optimize the shortest representative of each class.'),
(2013,5):('Number Theory',['Digits & bases','Modular arithmetic','Algorithms & constructions'],'A suitable repeating decimal creates cyclic shifts of the required digit strings. Removing powers of two and five while keeping the common multiplier valid is the substantial construction.'),
(2013,6):('Geometry',['Circles & tangency','Similarity & congruence','Constructions & loci'],'Several auxiliary circle centres and tangent-length identities are needed to show a seemingly variable ratio is fixed; the remaining quadratic then identifies both possible points.'),
(2014,4):('Combinatorics',['Games & strategies','Colouring','Algorithms & constructions'],'A three-colouring gives the obstruction, but proving the smaller target can be forced requires a finite trapping configuration and careful analysis of its occupied runs.'),
(2014,5):('Geometry',['Triangle centres','Circles & tangency','Transformations'],'Reflections of the circumcentre and orthocentre reveal the right auxiliary circles, but a further relation between the two new centres is needed for the fixed length.'),
(2014,6):('Number Theory',['Primes','Divisibility & GCD','Counting'],'The proof separates small and large common prime factors, counts how many index pairs each can cover, and converts many distinct large factors into an exponential lower bound.'),
(2025,5):('Number Theory',['Binomial coefficients','Modular arithmetic','Counting'],'The universal divisibility requires both obstructions for even exponents and a uniform argument for odd exponents; a single congruence or small-case pattern does not suffice.'),
(2025,6):('Combinatorics',['Graph theory','Extremal arguments','Algorithms & constructions'],'The personal circular partitions need not align. A global matching or allocation argument is required to reconcile all valuations while preserving each person’s threshold.'),
(2008,5):('Combinatorics',['Invariants','Infinite descent','Divisibility & GCD'],'Decreasing the displayed real numbers alone does not prove termination. One must instead choose an integer relation whose coefficient norm strictly decreases after a suitable subtraction.'),
(2008,6):('Combinatorics',['Graph theory','Parity','Linear algebra'],'The valid partitions form an affine system over the two-element field, but consistency must also be proved; an equivalent graph reduction carefully preserves or doubles the count.'),
(2009,5):('Geometry',['Circles & tangency','Similarity & congruence','Power of a point'],'The forward angle chase and the converse impose different demands; the cyclic trapezoid symmetry must be combined with a radical-axis or similarity argument to recover the angle bisector.'),
(2009,6):('Number Theory',['Divisibility & GCD','Rational numbers','Valuations'],'Pairwise integrality must be upgraded to a single scale valid for infinitely many rational numbers. Bounding denominators and then eliminating common factors is the core argument.')}
for (y,n),(topic,tags,reason) in raw_reviews.items():
 if ('USAMO',y,str(n)) in seen:continue
 candidates=[]
 for f in (P/'mathnet').glob(f'usa_{y}_*.json'):
  raw=json.loads(f.read_text())
  if str(raw.get('problem_number')).strip('. ')==str(n) and 'Junior' not in raw.get('competition','') and 'USAJMO' not in raw.get('competition',''):candidates.append((f,raw))
 assert candidates,(y,n)
 f,raw=candidates[0]
 st=raw['problem_markdown'];st=re.sub(r'\n\(?This problem was suggested by[^\n]*','',st)
 add('USAMO',y,n,topic,tags,st,reason,notes='Statement from the reviewed MathNet transcription (CC BY 4.0, original contest rights retained). Solution link: Evan Chen’s author-maintained notes. Rating unchanged from the individual assessment ledger.')
 new[-1]['secondarySourceUrl']='https://mathnet.mit.edu/explorer.html?p='+f.stem

records_path=P/'restoration-records.json'
if records_path.exists():
 for x in json.loads(records_path.read_text()):add(**x)
ids={p['id'] for p in new};bank=[p for p in bank if p['id'] not in ids]+new
(R/'data/americas.json').write_text(json.dumps(bank,ensure_ascii=False,indent=2)+'\n')
cov['uniqueIncluded']=len(bank)
cov['method']='Each numerical rating is an individual statement-and-solution assessment. Every supported reviewed question is included irrespective of difficulty; 4–7 is only the preferred browsing range. Common problems share one entry with alternate appearances.'
missing=[]
for key,d in ratings.items():
 if key not in seen:missing.append(dict(competition=key[0],year=key[1],number=key[2],difficulty=d,reason='Previously assessed; statement/metadata restoration pending. Not excluded by difficulty.'))
cov['restorationPending']=missing
(R/'research/americas-coverage.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2)+'\n')
print('Added',len(new),'total',len(bank),'remaining rated appearances',len(missing))
