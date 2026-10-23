# Executed by build.py after statement/solution compilation.
groups=collections.defaultdict(list)
for d in decisions:
 if d['competition']=='Olympic Revenge':continue # Misattributed raw records, not Portuguese papers.
 groups[(d['country'],d['competition'],d['year'],d['section'])].append(d)
def nums(a,b):return list(map(str,range(a,b+1)))
def expected_for(c,comp,y,s):
 s=s or ''
 if c=='Austria':return nums(4,6) if '(Day 2)' in s else nums(1,3) if '(Day 1)' in s else nums(1,4)
 if c=='Germany':return nums(1,3)
 if c=='Netherlands':return nums(1,5 if 'March' in s else 4)
 if c=='Estonia':return None # An explicitly selected booklet, not a full official contest paper.
 if c=='Poland':return nums(4,6) if 'day 2' in s else nums(1,3)
 if c=='Russia':return [s.split()[-1]+'.'+str(k) for k in range(1,9)]
 if c=='Spain':return nums(1,6)
 if c=='Serbia':return nums(4,6) if s=='Day 2' else nums(1,3)
 if c=='Greece':return nums(1,4)
 if c=='Italy':return nums(15,17) if 'proof problems' in s else nums(13,14) if 'numerica' in s else nums(1,12)
 if c=='Czech Republic':return nums(1,4 if 'regional' in s else 6)
 if c=='Belarus':
  start={'First':1,'Second':5,'Third':9,'Fourth':13}[s.split()[0]];return nums(start,start+3)
 if c=='Hungary':return nums(1,3)
 if c=='France':return nums(1,4) if 'Junior' in s else nums(5,7)
 if c=='Slovakia':return nums(1,6)
 if c=='Romania':
  if 'Selection Test' in comp:
   k=int(s.split()[-1]);return nums(1,{1:5,2:4,3:5,4:4}[k]) if 'Junior' in comp else (nums(1,{1:4,2:5,3:3}[k]) if k<=3 else None)
  if comp=='Romanian Master of Mathematics':return nums(1,6)
  return nums(1,4)
 if c=='Bulgaria':return None if 'TST' in comp and s=='Day 1' else nums(1,6 if s=='National final' else 4)
 if c=='Ukraine':
  if 'Kyiv City' in comp:return nums(1,4)+['3.1','4.1'] if s.endswith('Grade 7') else nums(1,5)+['4.1','5.1']
  g=re.search(r'(\d+)th',s)[1];start=1 if 'First Day' in s else 5;return [g+'-'+str(i) for i in range(start,start+4)]
 if c=='Switzerland':return nums(1,8) if s=='Final Round' else nums(1,12) if s=='IMO Selection' else ['N1','N2','C1','C2','G1','G2']
 if c=='Slovenia':return None if 'Technical' in comp else ['A1','A2','A3','B1','B2','B3']
 if c=='Croatia':return None if 'Junior' in comp else nums(1,7 if 'School/City' in s else 5 if 'County' in s or 'National Competition' in s else 4)
 if c=='North Macedonia':return nums(1,5) if comp=='Macedonian Mathematical Olympiad' else nums(1,4) if 'BMO' in comp else nums(4,6) if s=='Day 2' else nums(1,3)
 if c=='Portugal':return nums(4,6) if 'Day 2' in s else nums(1,3)
 if c=='Moldova':return nums(5,8) if 'Day 2' in s else nums(1,4)
 if c in ['Albania','Georgia']:return nums(1,5)
 if c=='Azerbaijan':return nums(1,30) if y==2025 else nums(1,20)
 if c in ['Montenegro','Cyprus']:return nums(1,4)
 if c=='Armenia':return nums(1,4) if s.endswith('Grade 7') else nums(1,3) if 'Day 1' in s else nums(4,6)
 if c=='Bosnia and Herzegovina':return nums(1,3) if y==2011 or 'Day 1' in s else nums(4,6)
 return None
papers=[]
for (c,comp,y,s),items in groups.items():
 expected=expected_for(c,comp,y,s);seen=sorted({str(d['number']) for d in items});rated=sorted({str(d['number']) for d in items if d['difficulty'] is not None and d['status'] not in ['quarantined','outside-BMO-prerequisites']})
 complete=expected is not None and set(expected)<=set(rated)
 papers.append({'country':c,'competition':comp,'year':y,'section':s,'complete':complete,'screeningComplete':expected is not None and set(expected)<=set(seen),'expectedQuestionNumbers':expected,'questionNumbers':rated,'inspectedQuestionNumbers':seen,'unratedQuestionNumbers':sorted(set(seen)-set(rated)),'missingQuestionNumbers':None if expected is None else sorted(set(expected)-set(seen)),'sourceUrls':sorted({d['sourceUrl'] for d in items}),'note':'Compilation identifiers 1–23 have been screened, but original grade/day mapping is unverified; this is not a full original-paper completeness claim.' if c in ['Soviet Union','Commonwealth of Independent States'] and comp=='CIS Mathematical Olympiad' else 'The booklet publishes Day 1 questions 1 and 2; the author calls the last Day 2 question aggregate problem 8, so omitted Day 1 material remains unverified and no full-paper completeness is asserted.' if c=='Bulgaria' and 'TST' in comp and s=='Day 1' else 'Only the selected booklet was screened; this is not full-round coverage.' if c=='Estonia' else 'Original within-paper question numbers have not yet been verified; compilation topic labels are retained explicitly.' if c=='Croatia' and 'Junior' in comp else ''})
papers.sort(key=lambda x:(x['country'],x['year'],x['competition'],x['section'] or ''))
counts=collections.Counter(d['status'] for d in decisions)
countryYears=collections.defaultdict(set)
for d in decisions:
 if d['competition']!='Olympic Revenge':countryYears[d['country']].add(d['year'])
coverage={'reviewedCount':sum(d['difficulty'] is not None and d['status'] not in ['quarantined','outside-BMO-prerequisites'] for d in decisions),'inspectedAppearanceCount':len(decisions),'ratedAppearanceCount':sum(d['difficulty'] is not None and d['status'] not in ['quarantined','outside-BMO-prerequisites'] for d in decisions),'distinctRatedCount':sum(d['difficulty'] is not None and d['status'] not in ['duplicate-appearance','quarantined','outside-BMO-prerequisites'] for d in decisions),'includedCount':len(out),'difficultyInclusionPolicy':'All source-verified, individually assessed problems rated 1–10 are included. The preferred practice range is 4–7; it is not an ingestion cutoff. Unresolved proofs and uncalibrated problems remain explicitly pending.','status':'in-progress','countsByDecision':dict(counts),'papers':papers,'decisions':decisions,'historicalCoverage':[{'country':c,'inspectedYears':sorted(ys),'remainingYears':'All unlisted years remain unreviewed in this contribution. Within listed years, only the exact papers and question numbers above have been screened.'} for c,ys in sorted(countryYears.items())],'archiveGaps':[
 {'country':'Azerbaijan','sourceUrl':'https://arti.edu.az/2025/03/06/respublika-f%C9%99nn-olimpiadalarinin-respublika-m%C9%99rh%C9%99l%C9%99sinin-yarimfinal-turunun-sual-kitabcalari/','status':'2025 junior semifinal: all 30 statements inspected, 29 independently assessed, question 16 pending proof verification. Senior semifinals and 2026 papers located but not fully reviewed. A verified public national-final source remains to be found.'},
 {'country':'Luxembourg','sourceUrl':'https://www.script.lu/en/news/2025-09/olympiades-de-mathematiques-2024-2025-plus-de-3300-eleves-mobilises','status':'Official SCRIPT report identifies participation in the Belgian OMB plus international OFM, Benelux, EGMO and IMO. No separate Luxembourg national paper was located; Belgian and international papers retain their own provenance.'},
 {'country':'Bosnia and Herzegovina','sourceUrl':'https://umks.pmf.unsa.ba/takmicenja/matematicka-olimpijada-bih/','status':'The Sarajevo archive intermittently fails retrieval. The Tuzla Mathematical Association archive supplied complete national papers and solutions for 2011, 2013, 2014 and 2015; other years remain pending.'},
 {'country':'Portugal','sourceUrl':'https://www.olimpiadas.spm.pt/index.php?id=75&tipo=1','status':'Official archive lists 2001–2026. Only the 2025 Category B national final is assessed here; other years, rounds, and categories remain pending.'},
 {'country':'Switzerland','sourceUrl':'https://imosuisse.github.io/exams/','status':'Official archive lists papers from 2004 onward. Only 2023 final, selection and second-round papers were inspected here.'},
 {'country':'Moldova','sourceUrl':'https://ance.gov.md/content/ol23matematic%C4%83testebareme','status':'All 48 questions of the 2023 Grades 7–12 national final inspected. Five calculus/determinant questions are outside BMO prerequisites and have no calibrated rating.'},
 {'country':'Albania','sourceUrl':'https://www.ama.org.al/documents/','status':'2025 and 2026 final upper/lower secondary papers inspected; earlier years and preliminary rounds pending.'},
 {'country':'Montenegro','sourceUrl':'https://www.iccg.me/provjera-znanja/takmicenja/testovi-srednje-skole?page=1','status':'2025 and 2026 national secondary Years I–II and III–IV papers assessed. Primary-school papers, earlier years, and Olimpijada znanja remain pending.'}],
 'limitations':['This is selected-year coverage, not an exhaustive historical search. Every unlisted paper or question remains pending.','reviewedCount counts numerically assessed appearances, including duplicate appearances. inspectedAppearanceCount additionally includes quarantined and out-of-scope inspections. distinctRatedCount excludes duplicate appearances and questions without a verified individual numerical assessment. Prerequisites alone do not exclude a numerically assessed problem.','complete is true only when all source-verified expected question identifiers have numerical mathematical assessments. screeningComplete may additionally include quarantined or out-of-scope decisions.','Estonian F/O/S labels and Croatian junior topic labels are compilation identifiers and are not represented as original within-paper numbers.','Four records mislabelled as Portugal Olympic Revenge actually concern a Brazilian competition; they remain quarantined and do not create Portuguese paper coverage.','Official-source errors and incomplete transcriptions are recorded explicitly; no target problem is published without an individual mathematical assessment.']}
(p.parent/'europe-coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2))
