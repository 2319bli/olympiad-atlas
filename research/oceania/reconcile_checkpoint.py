"""Reconcile the 23 October 2026 regional research checkpoint; no new ratings."""
from extend import data,cov,finish
from collections import Counter

finish()
ledger=cov['ledger']
AMO='Australian Mathematical Olympiad'
SMC='AMOC Senior Contest'
PAMO='Pan-African Mathematics Olympiad'
UWA='https://enrichedmaths.maths.uwa.edu.au/Olympiad/'

def assessed(p):
 return p.get('difficulty') is not None and p['status'] in ('reviewed','duplicate-appearance')

def inventory(comp,years,expected,source,unread='listed-not-retrieved',round_name=''):
 result=[]
 for y in years:
  rr=[p for p in ledger if p['competition']==comp and p['year']==y]
  n=expected
  pending=[p['id'] for p in rr if not assessed(p)]
  entry=dict(year=y,section=round_name,expectedQuestionCount=n,statementCount=len(rr),assessedCount=sum(assessed(p) for p in rr),includedCount=sum(p.get('included',False) for p in rr),pendingQuestionIds=pending,missingQuestionNumbers=[str(i) for i in range(1,n+1) if str(i) not in {p['number'] for p in rr}],status=('complete-individual-assessment' if len(rr)==n and not pending else 'partial-individual-assessment' if rr else unread),sourceUrls=sorted(set(p['sourceUrl'] for p in rr)) or [source])
  result.append(entry)
 return result

amo=inventory(AMO,range(1995,2025),8,UWA,unread='listed-retrieval-failed')
smc=inventory(SMC,range(1994,2025),5,UWA)
pamoyears=list(range(2000,2011))+[2012,2013]+list(range(2015,2020))+list(range(2021,2027))
pamo=inventory(PAMO,pamoyears,6,'https://www.pamoofficial.org/problems/')
nz1=inventory('New Zealand Mathematical Olympiad — Round 1',range(2019,2027),8,'https://www.mathsolympiad.org.nz/resources/','listed-retrieval-failed','Round 1')
nz2=inventory('New Zealand Mathematical Olympiad — Round 2',range(2019,2027),5,'https://www.mathsolympiad.org.nz/resources/','listed-retrieval-failed','Round 2')
# The 2026 index proves both papers exist, but their question counts have not been read.
for rr in [nz1[-1],nz2[-1]]:
 rr['expectedQuestionCount']=None;rr['missingQuestionNumbers']=[];rr['note']='Official index lists paper and solutions; paper contents and question count not retrieved.'

cov['status']='Publication checkpoint: partial historical coverage with individual assessments, explicit unread inventory, proof holds and source defects. No country or regional exhaustiveness claim.'
cov['countDefinitions']={
 'availableCorpusCount':'Ledger records, including deferred provenance records; this is not the size of the full historical archive.',
 'screenedCount':'Ledger records minus deferred provenance records; includes unreadable/source-held and proof-pending records.',
 'numericallyRatedCount':'All ledger records carrying a numerical rating, including four source-held records and one duplicate appearance.',
 'reviewedCount':'Numerically assessed records with status reviewed or duplicate-appearance; source-held records do not count as completed assessments.',
 'includedCount':'Unique published problem records in data/oceania-africa.json, across the full 1–10 scale; 4–7 is the preferred browsing range only.',
 'completePaper':'All expected question numbers present, and every question individually assessed with no source or proof hold. An assessed duplicate counts as reviewed, but is not published twice.'}
cov['checkpointDelta']={'baselineIncludedCount':245,'includedAdded':len(data)-245,'baselineLedgerCount':705,'ledgerRecordsAdded':len(ledger)-705,'newlyAssignedNumericalRatings':cov['numericallyRatedCount']-436,'newPaperStatementsRead':141,'newAMOPapers':17,'newAMOCSeniorPapers':1,'previousPAMOProofHoldsResolved':5}
cov['archiveInventory']={
 'verifiedOn':'2026-10-23',
 'downloadTerminology':'The UWA and PAMO statements were read through web retrieval/indexed PDFs or HTML; no local UWA/NZMO PDF download succeeded. MathNet JSON records and several African scans already exist in research/oceania. Retrieved text is not described as a downloaded PDF.',
 'AMO':{'sourceUrl':UWA,'requestedYears':[1979,2026],'indexedYears':list(range(1995,2025)),'indexedPaperCount':30,'indexedQuestionCount':240,'fullStatementPapersRead':26,'fullStatementQuestionsRead':208,'localPdfDownloadCount':0,'retrievalFailedYears':[2002,2005,2014,2015],'papers':amo,'historicalYearsWithoutRecoveredPrimaryFullPaper':list(range(1979,1995)),'recentPapersNotRecovered':[{'year':2025,'section':'AMO'},{'year':2026,'section':'Summer'},{'year':2026,'section':'Winter'},{'year':2026,'section':'Final'}],'accessNotes':'UWA archive index and direct HTTP requests return 403/520 intermittently. Indexed full PDFs were readable for the 26 listed years recorded in the ledger; retries for 2002, 2005, 2014 and 2015 did not recover full statements. AMT free past-paper index lists 2016–2020; historical books were identified but not accessed. AMO 2026 has separately named Summer, Winter and Final papers.'},
 'AMOCSenior':{'sourceUrl':UWA,'indexedYears':list(range(1994,2025)),'indexedPaperCount':31,'fullStatementPapersRead':7,'fullStatementQuestionsRead':35,'localPdfDownloadCount':0,'papers':smc,'unreviewedHistoricalYears':list(range(1994,2018)),'recentPaperNotRecovered':2025,'retiredAfter':2025,'retirementSourceUrl':'https://amt.edu.au/olympiad-program-update','accessNotes':'Historical index entries remain unread; they are not claimed to be blocked individually. SMC 2022 was recovered in this checkpoint. There is no AMOC Senior 2026 paper because AMT retired the contest after 2025.'},
 'PAMO':{'sourceUrl':'https://www.pamoofficial.org/problems/','indexedYears':pamoyears,'indexedPaperCount':24,'indexedQuestionCount':144,'fullStatementPapersRead':24,'fullStatementQuestionsRead':144,'unlistedYearsWithin2000To2026':[2011,2014,2020],'historicalBefore2000':'No primary full-paper inventory recovered; this does not assert no contests occurred.','proofPendingCount':sum(p['status']=='pending-solution-review' for p in ledger if p['competition']==PAMO),'papers':pamo},
 'NZMO':{'sourceUrl':'https://www.mathsolympiad.org.nz/resources/','indexedYears':list(range(2019,2027)),'indexedPapersPerYear':['Round 1','Round 2'],'indexedPaperCount':16,'localPdfDownloadCount':0,'papers':nz1+nz2,'accessNotes':'The official index explicitly lists both 2026 papers and solutions. Live archive/PDF retrieval returned 503 or failed. Existing MathNet transcriptions cover 2019–2025 incompletely. Papers before 2019 have no recovered primary inventory.'},
 'SAMO':{'sourceUrl':'https://www.samf.ac.za/en/past-papers','inventoryStatus':'Primary historical inventory not retrieved: HTTP 403. Known source corpus and exact paper-level gaps are recorded in papers and ledger, not treated as the complete SAMO archive.','knownSeniorFinalYears':sorted({p['year'] for p in ledger if p['competition']=='South African Mathematics Olympiad — Senior Final'}),'unrecoveredRecentYears':[2025,2026],'unrecoveredIntermediateYears':[2011,2013],'missingQuestionsInKnownPapers':[{'year':2010,'number':'5'},{'year':2016,'number':'1'}]},
 'Egypt':{'sourceUrl':'https://www.egyptmathematicalfoundation.org/','inventoryStatus':'No primary paper inventory recovered. The current official homepage has a Past Papers link, but following it returns to the homepage. No national paper was reviewed.'}}
cov['proofPendingQuestionIds']=[p['id'] for p in ledger if p['status']=='pending-solution-review']
cov['sourceHeldQuestionIds']=[p['id'] for p in ledger if p['status'].startswith('withheld')]
cov['fullPapersScreened'][1]='AMO: 1995–2001, 2003–2004, 2006–2013 and 2016–2024 statements fully read (26 papers, 208 questions); 184 individually assessed, 24 awaiting complete proof review. Complete assessments: 1997–1998, 2008, 2016–2020, 2022–2024.'
cov['fullPapersScreened'][2]='AMOC Senior Contest: 2018–2024 statements fully read (7 papers, 35 questions); 30 individually assessed, 5 proof holds. Complete assessments: 2018, 2020, 2024.'
cov['fullPapersScreened'][3]='PAMO: 2000–2010, 2012–2013, 2015–2019, 2021–2026 statements fully read (24 papers, 144 questions); 119 assessed appearances including one duplicate, 25 proof holds. Exact complete years and pending questions are in archiveInventory.PAMO.'
cov['gaps']=[
 'AMO: 1979–1994 primary full papers not recovered. UWA lists 1995–2024: full statements read for 26 of 30 papers; 2002, 2005, 2014 and 2015 retrieval failed. Of 208 read questions, 24 remain proof holds. AMO 2025 and separate 2026 Summer/Winter/Final papers not recovered.',
 'AMOC Senior: UWA lists 1994–2024. Only 2018–2024 have been read; 1994–2017 remain unread. Five proof holds remain among 2018–2024. The 2025 paper is unrecovered; the contest was retired after 2025, so no 2026 paper is expected.',
 'PAMO: all 24 listed papers from 2000–2026 have been read; the index does not list 2011, 2014 or 2020. Twenty-five questions still need complete proof reviews and carry no rating. No primary pre-2000 inventory was recovered.',
 'NZMO Round 1 missing from source corpus: 2020 Q5,Q8; 2021 Q8; 2022 Q6,Q7; 2024 Q8; 2025 Q3,Q6. Round 2 2022 Q2 missing. The official index lists both 2026 papers and solutions, but their contents were not recovered. No primary inventory before 2019 recovered.',
 'NZMO 2022 Round 1 Q3 statement conflicts with solution; 2025 Round 2 Q4 has an n=1 domain ambiguity; 2021 Round 1 Q6 has a row-direction wording error. Withheld pending primary comparison.',
 'SAMO 2010 Senior Final Q5 and 2016 Senior Final Q1 missing. Earlier years, 2011, 2013, 2025–2026 finals not recovered. The official archive returns 403, so an exhaustive primary year inventory has not been established. Mixed 2015–2016 lower-round records remain incomplete.',
 'SAMO 2014 Q5 repeats a comparison in extraction; 2015 second-round senior Q20 input list conflicts with its solution. These remain withheld. Six purported SAMO 2016 final records were corrected to 2017 using solution-image names and independent contest-index confirmation.',
 'Mauritania 7C final-round 2017, 2018, 2019 and 2023 incorporated; other years and rounds incomplete. Tunisia, Algeria, Morocco and Nigeria have partial paper reviews and explicit holds. Egypt has no recovered national-paper inventory. See countryAccess. No country, regional or worldwide exhaustiveness is claimed.'
]
for s in cov['sources']:
 if s['url']==UWA:s['access']='Indexed AMO 1995–2024 and AMOC Senior 1994–2024 inventory verified. 26 AMO and 7 AMOC Senior full papers read; exact unread years and proof holds in archiveInventory. Direct downloads failed with 403/520; no local UWA PDFs.'
 if s['url']=='https://www.mathsolympiad.org.nz/resources/':s['access']='Official index verifies both rounds and solutions for every year 2019–2026. Live archive/direct retrieval failed with 503; no 2026 statements recovered.'
 if s['url']=='https://www.pamoofficial.org/problems/':s['access']='All 24 listed 2000–2026 papers read; 119 assessed appearances including one duplicate, 25 proof holds. Archive omits 2011, 2014, 2020.'
for s in cov['countryAccess']:
 if s['country']=='Egypt':s.update(sourceUrl='https://www.egyptmathematicalfoundation.org/',notes='Current official Egyptian Mathematical Foundation homepage verified. Its Past Papers link returns to the homepage, so no actual paper archive or exact historical inventory was recovered. The earlier IdeasGym olympiad page also supplies no national-final papers. National problems remain unreviewed.')
cov['reproducibility']={'directory':'research/oceania','historicalBatchScripts':['batch_1995_1997.py','batch_1999_2007.py','batch_2008_2013.py','batch_1998_2004.py','batch_2009_smc2022.py','batch_pamo.py'],'helper':'extend.py','finalReconciliation':'reconcile_checkpoint.py','allDifficultiesRestoration':'restore-all-difficulties.py', 'instruction':'Run restore-australia.py, restore-pamo-statements.py and restore_africa_statements.py to regenerate statement overrides, then restore-all-difficulties.py and reconciliation. These scripts upsert the individually authored assessments into the existing regional checkpoint; run reconciliation last. They are not a replacement for the initial-corpus build scripts. Research scripts are ignored by repository .gitignore and must be explicitly preserved by the publishing owner if desired.'}
finish()
print({k:cov[k] for k in ['includedCount','availableCorpusCount','screenedCount','reviewedCount','numericallyRatedCount','deferredCount']})
