# Normalize paper keys for the site's coverage compiler. Preserve imported labels separately.
for z in ledger:
 z['number']=str(z['number']).strip('. ')
 if z['country'] in ('New Zealand','South Africa') and z['status']!='deferred-training-provenance':
  raw=(z.get('competition') or '')+' '+(z.get('section') or '')
  z['sourceCompetition']=z['competition'];z['sourceSection']=z.get('section')
  if z['country']=='New Zealand':
   rd=1 if any(q in raw for q in ['One','Round 1']) else 2
   z['competition']=f'New Zealand Mathematical Olympiad — Round {rd}';z['section']=''
  else:
   rd=1 if 'First' in raw else 2 if 'Second' in raw else 3
   div='Junior' if 'Junior' in raw else 'Senior'
   z['competition']='South African Mathematics Olympiad — '+(div+' Final' if rd==3 else f'{div} Round {rd}');z['section']=''
 else:z['section']=z.get('section') or ''
expected={}
def candidate(c,co,y,n,sec=''):expected[(c,co,y,sec)]=n
for y in range(2016,2025):candidate('Australia','Australian Mathematical Olympiad',y,8)
for y in [2018,2019,2020,2021,2023,2024]:candidate('Australia','AMOC Senior Contest',y,5)
for y in list(range(2000,2011))+[2012,2013]+list(range(2015,2020))+list(range(2021,2027)):candidate('Pan-African','Pan-African Mathematics Olympiad',y,6)
for y in [2017,2018,2019,2023]:candidate('Mauritania','Mauritanian National Olympiad — 7C, Round 3',y,5)
for y in range(2019,2026):
 candidate('New Zealand','New Zealand Mathematical Olympiad — Round 1',y,8)
 candidate('New Zealand','New Zealand Mathematical Olympiad — Round 2',y,5)
for y in [2010,2012,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]:candidate('South Africa','South African Mathematics Olympiad — Senior Final',y,6)
candidate('Tunisia','Tunisian Mathematical Olympiad — National Preselection',2021,4)
candidate('Tunisia','Tunisian Mathematical Olympiad — Sfax/Hammamet Test',2022,3)
for sec in ['Senior','Junior','Benjamin']:candidate('Algeria','Algerian Mathematical Olympiad',2025,6,sec)
for y,n in [(2018,10),(2019,6),(2020,6)]:candidate('Nigeria','Nigerian Mathematics Olympiad — Senior Round 2',y,n)
candidate('Morocco','Moroccan National Olympiad Programme — National Camp Contest',2024,4,'December')
candidate('Morocco','Moroccan National Olympiad Programme — National Camp Contest',2025,4,'January')
candidate('Morocco','Moroccan National Olympiad Programme — Team Selection Test',2025,6,'TST')
groups=collections.defaultdict(list)
for z in ledger:groups[(z['country'],z['competition'],z['year'],z['section'])].append(z)
coverage['papers']=[]
for (c,co,y,sec),n in expected.items():
 rows=groups.get((c,co,y,sec),[])
 nums={z['number'] for z in rows}
 allseen=len(nums)==n
 allrated=all(z.get('difficulty') is not None for z in rows)
 coverage['papers'].append(dict(country=c,competition=co,year=y,section=sec,complete=allseen and allrated,statementComplete=allseen,expectedCount=n,screenedCount=len(nums),reviewedCount=sum(z.get('difficulty') is not None for z in rows)))
coverage['countryAccess']=[
 dict(country='Tunisia',status='partial-paper-review',sourceUrl='https://benjedidiachokri.wixsite.com/website/ressources',notes='ATSM primary PDFs recovered:2021 national preselection and2022 Sfax/Hammamet test.2021Q1 has a counterexample under the printed nonzero-real domain and is withheld. Other years and finals still incomplete. ATCCM2024 Drive folder not retrievable by the web search service.'),
 dict(country='Algeria',status='partial-paper-review',sourceUrl='https://almo2025.com/',notes='Official2025 Senior and Junior both days, Benjamin Day1 fully read from indexed organiser PDFs.12 questions mathematically assessed;3 geometry proofs pending. Benjamin Day2 and historical years not recovered. Live source and ASMC summer-selection archive return502.'),
 dict(country='Morocco',status='partial-paper-review',sourceUrl='https://mathmaroc.org/divisions/olympiads',notes='Primary Math&Maroc2024/2025 report recovered from its public Drive link. Fourteen National Contest statements read:December2024 camp,January2025 camp,andMarch2025 TST. Thirteen mathematically assessed and12 included; TSTQ6 sharpness construction diagram remains pending. Earlier national stages and historical years incomplete. Used-in-Morocco provenance is explicit; no claim of original authorship.'),
 dict(country='Egypt',status='primary-paper-not-recovered',sourceUrl='https://ideasgym.com/pages/science-olympiads',notes='Organiser public olympiad page verified. It links international syllabuses but no Egyptian national-final paper archive. National problems remain unreviewed.'),
 dict(country='Nigeria',status='partial-paper-review',sourceUrl='https://nmc.edu.ng/',notes='NMC official page returns403. Special Maths Academy publicly links a Drive archive of NMC scanned question papers2013–2022; complete senior second-round papers2018,2019,2020 visually screened(22 statements),19 numerically assessed and8 included.2018Q3,Q4 and2020Q1 withheld for degenerate/missing/false assumptions. Earlier and2021+ papers remain pending; no third-round finals recovered.')]
coverage['status']='Research continuing: Australia,NZ,South Africa,PAMO,Mauritania,Tunisia,Algeria andNigeria have individually assessed entries. Explicit country-level access and proof gaps remain.'
coverage['gaps']=[x for x in coverage['gaps'] if not x.startswith('Mauritanian7C')]+['Mauritanian7C final-round2017,2018,2019,2023 incorporated; other years/rounds incomplete. Tunisia andAlgeria partial primary-paper reviews added. Morocco,Egypt andNigeria access/provenance progress is detailed in countryAccess. No regional or worldwide exhaustiveness is claimed.']
coverage['fullPapersScreened']+=['Nigeria:Senior Round2(2018:10questions;2019,2020:6each).19 mathematically assessed;3 malformed statements withheld.']
coverage['fullPapersScreened']+=['Tunisia:2021 national preselection(4 statements;Q1 malformed),2022 Sfax/Hammamet test(3 fully assessed).','Algeria:2025 Senior andJunior both days(6 each),Benjamin Day1(3); geometry proof gaps remain.']

coverage['fullPapersScreened'].append('Morocco:December2024 camp andJanuary2025 camp four problems each,March2025 TST six problems. Thirteen mathematically assessed;TSTQ6 proof diagram pending.')
