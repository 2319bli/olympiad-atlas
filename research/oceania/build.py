import json, glob, re, collections, os
BASE='/workspace/sites/olympiad-atlas/'
P=BASE+'research/oceania/'
# The canonical checkpoint also contains later regional batches and verified fixes.
# Incremental rebuilds reconcile it without replacing those records with this legacy seed.
if os.path.exists(BASE+'data/oceania-africa.json') and os.path.exists(BASE+'research/oceania-africa-coverage.json'):
    import runpy
    runpy.run_path(P+'restore-all-difficulties.py',run_name='__main__')
    raise SystemExit(0)
reviews=json.load(open(P+'reviews.json'))
overrides={
 'zaf_2015_2b154d':{
  'statement':r'A positive divisor $d$ of $n$ is special when $d+1$ also divides $n$. Show that no more than half of the divisors of $n$ are special, and classify the equality cases.',
  'solution':r'''Consecutive integers are coprime. Thus, if $d$ is special, $d(d+1)\mid n$, and in particular $d<\sqrt n$. Pairing each divisor with its complementary divisor proves the bound.

For equality, $n$ is not a square and every divisor below $\sqrt n$ is special. Starting with $1$, this forces $1,2,\ldots,k+1$ to divide $n$, where $k=\lfloor\sqrt n\rfloor$. The largest divisor below $\sqrt n$ and the smallest above it are complementary, so $n=k(k+1)$. For $k>1$, the divisibility $k-1\mid k(k+1)$ gives $k-1\mid2$. Therefore $k=1,2,3$, producing $n=2,6,12$. Direct inspection verifies equality for all three.''',
 },
 'zaf_2015_2dc78b':{
  'statement':r'Place $20$ vertices on one bank of a straight river and $15$ on the other. Count the connected graphs whose edges are straight bridges between opposite banks, with no two bridges crossing except at a common endpoint.',
  'solution':r'''Let $F(a,b)$ count the configurations with $a,b$ villages, listed in order along the banks. The two first villages must be joined: otherwise their respective connections to the rest would cross. Moreover, when $a,b>1$, exactly one of these villages can have another incident edge. The other is a leaf. Removing that leaf gives
$$F(a,b)=F(a-1,b)+F(a,b-1).$$
The boundary values are $F(a,1)=F(1,b)=1$, since all bridges are forced. Pascal's identity therefore gives
$$F(a,b)=\binom{a+b-2}{a-1}.$$
The answer is $\binom{33}{19}=818809200$.''',
 },
 'zaf_2015_6185c8':{
  'statement':r'Players alternately place non-overlapping dominoes on a $5\times5$ chessboard, stopping when none fits. Prove that an odd number of cells remain empty, determine which colour has more empty cells, and find the largest possible number of empty cells. Assume the four corner cells are black.',
  'solution':r'''There are always an odd number of empty cells, because each domino removes two cells from an initial total of $25$. Every domino covers one black and one white cell, so exactly one more black cell than white cell remains empty. The maximum number of empty cells is $7$.

The source's worked proof of the sharp bound and its attaining arrangement use two board diagrams. Open the source solution below to view those diagrams and the complete case argument.''',
  'solutionKind':'source-link',
 },
 'zaf_2015_7a2a5b':{
  'statement':r'An integer $a$ has the property that $n!+a$ divides $(2n)!$ for infinitely many positive integers $n$. Prove that $a=0$.',
  'solution':r'''Suppose $a\ne0$. Since
$$(2n)!=\binom{2n}{n}(n!)^2,$$
reduction modulo $n!+a$ shows that $n!+a$ must divide $a^2\binom{2n}{n}$. But $\binom{2n}{n}\le4^n$, and $n!/4^n\to\infty$: after any fixed index, successive ratios are $(n+1)/4$, which eventually exceed $2$.

Consequently, for every sufficiently large $n$,
$$0<a^2\binom{2n}{n}<n!+a.$$
The claimed divisibility is then impossible. Hence $a=0$, which indeed works for every $n$.''',
 },
 'zaf_2015_d3d293':{
  'statement':r'In acute triangle $ABC$, $AB<AC$. Choose $D\in AC$ and $E\in BC$ with $AD=AE=AB$. Circle $ABE$ meets line $AC$ again at $F$ and line $DE$ again at $P$. Prove that $PB=PD=PF$.',
  'solution':r'''Since $AD=AE$, the base angles of $ADE$ coincide. The cyclic quadrilaterals $ABPE$ and $ABPF$ therefore give
$$\angle ABP=\angle ADE=\angle ADP,\qquad
\angle ABP=\angle DFP.$$
Thus $\angle FDP=\angle DFP$, and $PD=PF$.

Also $AB=AE$, so $\angle ABE=\angle AEB$. Reading these angles on circle $ABEP$ gives $\angle APB=\angle APD$. Triangles $ABP$ and $ADP$ now have two equal angles and the common side $AP$, so they are congruent. Hence $PB=PD=PF$, as required.''',
 },
 'nzl_2024_c850b6':{},
}

def image_paths(s):
    return re.sub(r'\]\(images/', '](https://mathnet.mit.edu/images/', s)

items=[]
for f in sorted(glob.glob(P+'full/*.json')):
    x=json.load(open(f)); v=reviews[x['slug']]
    if v['status']!='reviewed' or v['difficulty'] is None or not 1<=v['difficulty']<=10:continue
    nz=x['country']=='New Zealand'
    section=x.get('section') or ''
    compraw=x.get('competition_raw') or ''
    roundnum=1 if ('One' in section+compraw or 'Round 1' in section+compraw) else 2 if ('Two' in section+compraw or 'Round 2' in section+compraw) else None
    competition=f'New Zealand Mathematical Olympiad — Round {roundnum}' if nz else 'South African Mathematics Olympiad — '+('Junior Final' if 'Junior' in section else 'Senior Final')
    year=v.get('correctedYear',x['year'])
    url='https://mathnet.mit.edu/explorer.html?p='+x['slug']
    notes=['Difficulty is an editorial estimate based on this problem and its solution, not the question number.','Source transcription: MathNet; original organiser credited in provenance.']
    if year!=x['year']:notes.append('Year corrected from the MathNet label 2016 to 2017: the 2017 solution-page image names and contest archive corroborate the paper.')
    if nz:notes.append('Original organiser: New Zealand Mathematical Olympiad Committee.')
    else:notes.append('Original organiser: South African Mathematics Foundation.')
    topics=[]
    for t in x.get('topics',[]):topics+=t[2:]
    item=dict(id=x['slug'],title=x.get('short_title',''),country=x['country'],competition=competition,year=year,number=str(x['problem_number']).strip('. '),statement=image_paths(x['problem_markdown']),solution=image_paths('\n\n'.join(x['solutions_markdown'])),sourceUrl=url,solutionUrl=url,topic=x['primary_domain'],tags=list(dict.fromkeys(topics)),difficulty=v['difficulty'],ratingReason=v['ratingReason'],reviewStatus='individually-assessed',notes=' '.join(notes),solutionKind='sourced',provenance={'archive':'MathNet','slug':x['slug'],'originalOrganisation':'NZMOC' if nz else 'SAMF'})
    if os.path.exists(P+'fixes.json'):
        overrides.update(json.load(open(P+'fixes.json')))
    if x['slug'] in overrides and overrides[x['slug']]:
        item.update(overrides[x['slug']]); item['solutionKind']=overrides[x['slug']].get('solutionKind','original-exposition')
        item['notes']+=' Statement paraphrased and solution exposition written for this bank.'
    items.append(item)

if os.path.exists(P+'australia.json'):items+=json.load(open(P+'australia.json'))
if os.path.exists(P+'pamo.json'):items+=json.load(open(P+'pamo.json'))
if os.path.exists(P+'amoc.json'):items+=json.load(open(P+'amoc.json'))
if os.path.exists(P+'mauritania.json'):items+=json.load(open(P+'mauritania.json'))
if os.path.exists(P+'africa-extra.json'):items+=json.load(open(P+'africa-extra.json'))
if os.path.exists(P+'nigeria.json'):items+=json.load(open(P+'nigeria.json'))
if os.path.exists(P+'morocco.json'):items+=json.load(open(P+'morocco.json'))
os.makedirs(BASE+'data',exist_ok=True)
json.dump(items,open(BASE+'data/oceania-africa.json','w'),indent=2,ensure_ascii=False)
print('Published',len(items),'items:',dict(collections.Counter(x['country'] for x in items)))
ledger=[]
for f in sorted(glob.glob(P+'full/*.json')):
    x=json.load(open(f));v=reviews[x['slug']]
    ledger.append(dict(id=x['slug'],country=x['country'],competition=x['competition_raw'],section=x['section'],year=v.get('correctedYear',x['year']),number=x['problem_number'],difficulty=v['difficulty'],status=v['status'],reason=v['ratingReason'],included=any(z['id']==x['slug'] for z in items),sourceUrl='https://mathnet.mit.edu/explorer.html?p='+x['slug']))
for extra in ['australia-ledger.json','pamo-ledger.json','amoc-ledger.json','mauritania-ledger.json','africa-extra-ledger.json','nigeria-ledger.json','morocco-ledger.json']:
    if os.path.exists(P+extra): ledger+=json.load(open(P+extra))
counts=collections.Counter(v['status'] for v in ledger)
coverage={
 'region':'Oceania and Africa', 'updated':'2026-10-22', 'status':'Research continuing: 69 Australian,60 Pan-African and5 Mauritanian questions included; 2 AMO,3 AMOC Senior and30 PAMO proof assessments remain pending, with additional archive gaps explicitly logged.',
 'reviewedCount':sum(v['difficulty'] is not None for v in ledger),
 'screenedCount':sum(v['status']!='deferred-training-provenance' for v in ledger),
 'includedCount':len(items),'availableCorpusCount':len(ledger),'deferredCount':counts['deferred-training-provenance'],
 'method':'Every published problem was read together with a solution or mathematically worked, and assigned its own numerical rating and content-specific rationale. Lower-round routine statements were screened individually. No ratings inferred from contest or question number.',
 'scale':'1–10 in half steps; all 1–10 ratings eligible; preferred browsing range 4–7. 4=lower hard BMO1; 5–6=core hard BMO1; 7=upper accessible BMO2. Editorial estimates, not measured empirical ratings.',
 'sources':[
 {'url':'https://mathnet.mit.edu/','coverage':'82 New Zealand entries, 299 South African entries downloaded and inspected; 77 training or monthly-set reprints deferred because original competition provenance is not established.'},
 {'url':'https://www.mathsolympiad.org.nz/resources/','access':'503 from archive and direct PDFs; search index verifies some organiser PDFs. The corpus is incomplete for several papers; see gaps.'},
 {'url':'https://samf.ac.za/en/sa-mathematics-olympiad','access':'403; MathNet archival transcriptions used with explicit source attribution.'},
 {'url':'https://enrichedmaths.maths.uwa.edu.au/Olympiad/','access':'Archive index/direct HTTP403; individual AMO PDFs accessible through web retrieval. Full-paper research in progress.'},
 {'url':'https://maurimath.net/Olympiades.php','access':'Ministry of Education 7C third-round papers2017,2018,2019,2023 read; AMIMATHS suggested solutions used where available.'},
 {'url':'https://www.pamoofficial.org/problems/','access':'Public archive accessible through web retrieval; research in progress.'}],
 'fullPapersScreened':[
 'Mauritania National Olympiad7C Round3:2017,2018,2019,2023 (5 questions each);4 calculus/logarithm problems outside elementary topic scope;2023Q5 equation missing from extraction.',
 'AMO:2016–2024 statements fully screened (8 per paper); 2021Q3,Q8 await full solution assessment; all other 70 questions numerically assessed.',
 'AMOC Senior Contest:2018,2019,2020,2021,2023,2024 (5 per paper);2019Q4,2021Q5,2023Q4 await proof assessment.',
 'PAMO:2000–2010,2012–2013,2015–2019,2021–2026 statements fully screened (24 papers;144 problems); pending proof reviews explicitly identified in ledger.',
 'NZMO Round1+Round2:2019,2023 (13 problems per year).',
 'NZMO Round2:2020,2021,2024,2025 (5 per year).',
 'SAMO Senior Final:2012,2014,2015,2017,2018,2019,2020,2021,2022,2023,2024 (6 per paper).'],
 'gaps':[
 'NZMO Round1 missing from corpus:2020 Q5,Q8;2021 Q8;2022 Q6,Q7;2024 Q8;2025 Q3,Q6. NZMO2022 Round2 Q2 missing. Earlier than2019 and2026 not yet recovered.',
 'SAMO2010 Senior Final Q5 and2016 Senior Final Q1 missing. Earlier years,2011,2013,2025–26 finals not yet recovered. Mixed2015–16 annual-report lower rounds are incomplete.',
 'NZMO2022 Round1 Q3 statement conflicts with solution;NZMO2025 Round2 Q4 leaves n=1 domain ambiguity;NZMO2021 Round1 Q6 has row-direction wording error. Withheld pending primary comparison.',
 'SAMO2014Q5 repeats the same comparison in its extracted statement;2015 second-round seniorQ20 input list disagrees with its solution. Withheld.',
 'Six purported SAMO2016 final records are2017; corrected using2017 solution-image names and independent contest index confirmation.',
 'AMO2025 and restructured AMO2026 Summer/Winter/Final official papers not recovered. AMT free past-paper index stops at2020; UWA archive lists through2024 and intermittently returns520. Earlier AMO and AMOC Senior before2018 remain incomplete;AMOC2022 PDF inaccessible,2025–26 not recovered.',
 'PAMO archive lists2000 onward with no2011,2014,2020 paper; no pre-2000 paper recovered. Thirty listed statements still need a complete proof review; they have no numerical rating.',
 'Mauritanian7C third-round2017,2018,2019,2023 incorporated; earlier and other years, and earlier rounds remain incomplete. No primary Nigerian/Tunisian national archive recovered. This is not a claim of regional or worldwide exhaustiveness.'
 ], 'countsByReviewStatus':dict(counts),'ledger':ledger}
exec(open(P+'coverage_normalize.py').read())
json.dump(coverage,open(BASE+'research/oceania-africa-coverage.json','w'),indent=2,ensure_ascii=False)
