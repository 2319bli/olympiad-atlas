import json,pathlib,collections,re,urllib.request,urllib.parse,html
ROOT=pathlib.Path('/workspace/sites/olympiad-atlas');P=ROOT/'research/asia'
r=json.load(open(P/'reviews.json'));m=json.load(open(P/'manifest.json'));cov=json.load(open(ROOT/'research/asia-coverage.json'));dec={d['id']:d for d in cov['decisions']}
files={f.stem:f for f in (ROOT/'research/raw/asia').glob('*.json')}; originalids=set(files); files.update({f.stem:f for f in (P/'extra').glob('*.json')})
raw={id:json.load(open(f)) for id,f in files.items()}; ids=[x[0] if isinstance(x,list) else x.get('slug',x.get('id')) for x in m]
countrymap={}
for row in m:
 if isinstance(row,list) and row[0] in raw:countrymap[row[1]]=raw[row[0]]['country']
bycountry=collections.defaultdict(list);manifestgroups=collections.defaultdict(list)
for row in m:
 id=row[0] if isinstance(row,list) else row.get('slug',row.get('id'))
 if isinstance(row,list):country=countrymap.get(row[1],row[1].replace('-',' ').title());year=row[2];comp=row[3]
 else:
  d=raw.get(id,row);country=d.get('country','Unknown');year=d.get('year');comp=d.get('competition','Unspecified')
 bycountry[country].append(id);manifestgroups[(country,comp,year)].append(id)
# A source record is not a paper: expose the actual available question numbers and duplicate IDs separately.
papers=collections.defaultdict(list)
for id,d in raw.items():
 if id in dec:q=dec[id];country,comp,section,number=q['country'],q['competition'],q['section'],q['number']
 else:
  country=d['country'];comp=d['competition'];section=d.get('section')or'';number=str(d['problem_number']).strip().rstrip('.')
  if 'selection of Indian Team' in (d.get('booklet_title')or''):comp='Indian team selection tests'
 papers[(country,comp,d['year'],section)].append((id,number))
plist=[]
for (country,comp,year,section),rows in sorted(papers.items()):
 rated=[id for id,num in rows if id in r and r[id]['difficulty'] is not None]; held=[id for id,num in rows if id in r and r[id]['difficulty'] is None]; pending=[id for id,num in rows if id not in r]
 expected=None;basis=None
 if country=='Japan' and year in [2022,2023,2024] and section.lower() in ['first round','final round']:
  expected=list(map(str,range(1,13 if section.lower()=='first round' else 6)));basis='Official JMO paper structure and available official archive links; original problem numbering retained.'
 if country=='China' and comp=='China Mathematical Olympiad (CMO)' and year in [2022,2023]:
  expected=list(map(str,range(1,4) if section=='Day One' else range(4,7)));basis='CMO two-day paper explicitly enumerates Q1–3 and Q4–6 in the source booklet.'
 if country=='India' and comp=='Indian National Mathematical Olympiad (INMO)' and year in [2012,2013,2014,2015,2017,2019,2020,2021,2023,2024]:
  expected=list(map(str,range(1,7)));basis='Six numbered tasks in the official HBCSE national-final paper/solutions.'
 if country=='South Korea' and year==2023:
  expected=list(map(str,range(1,4) if 'Day 1' in section else range(4,7)));basis='Two-day six-question national-final numbering; available source contains Q1,2,5,6.'
 if country=='China' and year==2002 and 'CGMO' in comp:
  expected=list(map(str,range(1,5) if section=='First Day' else range(5,9)));basis='Two-day CGMO numbering in the source booklet; Q4 is absent and Q2 contains only part (1).'
 if country=='China' and comp=='China Mathematical Olympiad (CMO)' and year==2024:expected=list(map(str,range(1,7)));basis='CMO national-final paper numbering; Q4 is not in the downloaded corpus.'
 nums=sorted(set(num for id,num in rows),key=lambda x:(int(x) if x.isascii() and x.isdigit() else 999,x))
 plist.append({'country':country,'competition':comp,'year':year,'section':section,'availableRecordIds':[id for id,num in rows],'availableQuestionNumbers':nums,'expectedQuestionNumbers':expected,'expectedBasis':basis,'missingQuestionNumbers':sorted(set(expected or [])-set(nums)),'reviewedRecords':len(rated)+len(held),'assessedRecords':len(rated),'heldUnratedIds':held,'pendingIds':pending,'includedRecords':sum(dec.get(id,{}).get('included',False) for id,num in rows),'availableCorpusComplete':not pending and not held,'originalPaperComplete':expected is not None and set(nums)==set(expected) and not pending and not held})
# Persist the exact official Japanese archive URL inventory without adding unreviewed problems to the question manifest.
jpfile=P/'japan/official-archive-links.json';jpfile.parent.mkdir(exist_ok=True)
if not jpfile.exists():
 url='https://www.imojp.org/domestic/jmo_overview.html'
 try:
  page=urllib.request.urlopen(url,timeout=30).read().decode('utf-8'); found=[]
  for row in re.findall(r'<tr\b[^>]*>(.*?)</tr>',page,re.S|re.I):
   clean=html.unescape(re.sub('<[^>]*>',' ',row));year=re.search(r'(20\d\d)年',clean)
   if not year:continue
   for href,label in re.findall(r'<a[^>]+href=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</a>',row,re.S|re.I):
    text=html.unescape(re.sub('<[^>]*>','',label)).strip()
    if text in ['予選','本選','代表選考合宿']:found.append({'year':int(year.group(1)),'round':{'予選':'First round','本選':'Final round','代表選考合宿':'Team selection camp'}[text],'sourceUrl':urllib.parse.urljoin(url,href)})
  jpfile.write_text(json.dumps({'archiveUrl':url,'verifiedDate':'2026-10-23','papers':found,'note':'Official site states that problem papers are available but worked solutions are not supplied.'},ensure_ascii=False,indent=2))
 except Exception as e:jpfile.write_text(json.dumps({'archiveUrl':url,'error':str(e)}))
countrylist=[]
for c,cids in sorted(bycountry.items()):
 available=set(cids)&set(raw);reviewed=set(cids)&set(r);held=[id for id in reviewed if r[id]['difficulty'] is None]
 countrylist.append({'country':c,'discoveredRecords':len(cids),'downloadedRecords':len(available),'reviewedRecords':len(reviewed),'assessedRecords':len(reviewed)-len(held),'heldUnratedIds':sorted(held),'includedRecords':sum(dec.get(id,{}).get('included',False) for id in cids),'pendingDownloadedIds':sorted(available-set(r)),'pendingUndownloadedIds':sorted(set(cids)-set(raw)),'fullNationalHistoryVerified':False})
for c in ['Pakistan','Nepal','Macau','Uzbekistan','Kyrgyzstan']:
 if c not in bycountry:countrylist.append({'country':c,'discoveredRecords':0,'downloadedRecords':0,'reviewedRecords':0,'assessedRecords':0,'includedRecords':0,'fullNationalHistoryVerified':False,'gap':'No verified national paper archive has been inventoried in this corpus; remains in scope.'})
result={'region':'Asia','snapshotDate':'2026-10-23','scope':'Exact discovered-record and downloaded-paper inventory. Neither this inventory nor completed individual papers establishes full national-history coverage.','manifestRecords':len(ids),'downloadedRecords':len(raw),'originalDownloadedQueueRecords':len(originalids),'originalDownloadedQueuePendingIds':sorted(originalids-set(r)),'originalDownloadedQueueHeldUnratedIds':sorted(id for id in originalids if id in r and r[id]['difficulty'] is None),'reviewedRecords':len(r),'assessedRecords':sum(v['difficulty'] is not None for v in r.values()),'heldUnratedRecords':sum(v['difficulty'] is None for v in r.values()),'pendingDownloadedIds':sorted(set(raw)-set(r)),'pendingUndownloadedIds':sorted(set(ids)-set(raw)),'countries':countrylist,'discoveredContestYearSets':[{'country':k[0],'competitionCode':k[1],'year':k[2],'recordCount':len(v),'recordIds':v,'roundsInventoried':all(id in raw for id in v)} for k,v in sorted(manifestgroups.items())],'downloadedPaperSets':plist,'verifiedArchives':[{'country':'India','url':'https://olympiads.hbcse.tifr.res.in/how-to-prepare/past-papers-sample-questions/','localLinkInventory':'research/asia/india/archive-links.json','scope':'Official INMO/RMO/IOQM archive links; full archive not all assessed.'},{'country':'Japan','url':'https://www.imojp.org/domestic/jmo_overview.html','localLinkInventory':'research/asia/japan/official-archive-links.json','scope':'Official first/final papers 2001–2026 and selection-camp links as individually enumerated.'},{'country':'South Korea','url':'https://www.kmo.or.kr/kmo/sub07.html','scope':'Official archive found; firewall blocks this retrieval, so exact full-year inventory is not asserted.'}], 'sourceHeldRecords':[dec[id] for id in r if r[id]['difficulty'] is None]}
(P/'archive-inventory.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
cov['downloadedRecords']=len(raw);cov['pendingDownloadedRecords']=len(result['pendingDownloadedIds']);cov['pendingUndownloadedRecords']=len(result['pendingUndownloadedIds']);cov['originalDownloadedQueuePendingRecords']=len(result['originalDownloadedQueuePendingIds']);cov['archiveInventoryPath']='research/asia/archive-inventory.json';cov['completeDownloadedPaperSets']=[{k:p[k] for k in ['country','competition','year','section','availableQuestionNumbers','includedRecords']} for p in plist if p['originalPaperComplete']]
# Preserve complete status on established Malaysia/Indonesia/Kazakhstan papers; update explicitly inventoried papers.
pidx={(p['country'],p['competition'],p['year'],p['section']):p for p in plist if p['expectedQuestionNumbers'] is not None}
for p in cov['papers']:
 q=pidx.get((p['country'],p['competition'],p['year'],p['section']))
 if q:p['complete']=q['originalPaperComplete'];p['expectedQuestionNumbers']=q['expectedQuestionNumbers'];p['missingQuestionNumbers']=q['missingQuestionNumbers']
(ROOT/'research/asia-coverage.json').write_text(json.dumps(cov,ensure_ascii=False,indent=2))
print({k:result[k] for k in ['manifestRecords','downloadedRecords','originalDownloadedQueueRecords','reviewedRecords','assessedRecords','heldUnratedRecords']});print('pending downloaded',len(result['pendingDownloadedIds']),'pending original',len(result['originalDownloadedQueuePendingIds']),'pending undownloaded',len(result['pendingUndownloadedIds']),'complete papers',len(cov['completeDownloadedPaperSets']))
