"""Assemble reviewed contributions without inventing ratings or coverage."""
from pathlib import Path
import json, re, collections, hashlib
from subtopics import classify, RULES, COMMON
from bmo_overview import build_overview

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public'/'data';OUT.mkdir(exist_ok=True)
files=['british','americas','oceania-africa','asia','europe','international','ireland','nordic','baltic','belgium']
asset_map=json.loads((ROOT/'data/asset-map.json').read_text()) if (ROOT/'data/asset-map.json').exists() else {}
problems=[];ledgers={};issues=[]
topic_overrides=json.loads((ROOT/'data/topic-overrides.json').read_text())
country_aliases={'Czechia':'Czech Republic','Turkey':'Türkiye','BMO-SL':'Balkan Olympiad','Balkan MO Shortlist':'Balkan Olympiad','Balkan Mathematical Olympiad':'Balkan Olympiad','IMO-SL':'International Mathematical Olympiad','Ibero-American Mathematical Olympiad':'Ibero-American Olympiad','International Zhautykov Olympiad':'Zhautykov Olympiad','Baltic Way Shortlist':'Baltic Way','Pan-African Olympiad':'Pan-African'}
def clean_number(number):
    n=re.sub(r'^(Problem|Opgave|Aufgabe)\s+', '', str(number), flags=re.I)
    return re.sub(r'\.\s*(Problem)?$', '', n, flags=re.I).strip()
def country_name(country):return country_aliases.get(country,country)
for name in files:
    f=ROOT/'data'/f'{name}.json'
    if f.exists():
        rows=json.loads(f.read_text())
        if isinstance(rows,dict): rows=rows.get('problems',rows.get('included',[]))
        for p in rows:
            p=dict(p)
            required=['id','country','competition','year','number','statement','sourceUrl','topic','difficulty','ratingReason']
            missing=[k for k in required if p.get(k) is None or p.get(k)=='']
            if missing: issues.append({'id':p.get('id'),'issue':'Missing fields','fields':missing});continue
            if p.get('reviewStatus')!='individually-assessed':issues.append({'id':p['id'],'issue':'Not individually assessed'});continue
            d=p['difficulty']
            if not isinstance(d,(int,float)) or not(1<=d<=10) or d*2!=int(d*2):issues.append({'id':p['id'],'issue':'Invalid rating; expected 1–10 in half-point steps'});continue
            p['number']=clean_number(p['number']);p['year']=int(p['year'])
            p['topic']={'Number theory':'Number Theory','Combinatorial Geometry':'Geometry','Combinatorial geometry':'Geometry','Discrete Mathematics':'Combinatorics'}.get(p['topic'],p['topic'])
            if p['topic'] not in ['Number Theory','Algebra','Geometry','Combinatorics']:issues.append({'id':p['id'],'issue':'Unrecognised topic','topic':p['topic']});continue
            p['topic']=topic_overrides.get(p['id'],p['topic'])
            p['tags']=p.get('tags') or []
            p['subtopics']=classify(p)
            if not p['subtopics']:issues.append({'id':p['id'],'issue':'Missing subtopic review'})
            if p['country']=='International':p['country']={'APMO':'Asia-Pacific','EGMO':'European Girls’ Olympiad','BMO':'Balkan Olympiad','JBMO':'Junior Balkan Olympiad','IMO':'International Mathematical Olympiad','IMO Shortlist':'International Mathematical Olympiad','Baltic Way':'Baltic Way','MEMO':'Middle European Olympiad','BxMO':'Benelux Olympiad','NMC':'Nordic Olympiad','RMM':'Romanian Master of Mathematics','IZhO':'Zhautykov Olympiad'}.get(p['competition'],p['competition'])
            p['country']=country_name(p['country'])
            if p.get('solution') and not p.get('solutionKind'):p['solutionKind']='original-exposition' if name=='british' else 'reviewed-source'
            if p.get('solutionUrl') and not p.get('solution') and not p.get('solutionKind'):p['solutionKind']='source-link'
            if p.get('solutionSource') and not p.get('solutionCredit'):p['solutionCredit']=p['solutionSource']
            appearances=[]
            for origin in (p.get('appearances') or [])+(p.get('alternateOrigins') or []):
                if isinstance(origin,dict):
                    origin=dict(origin);origin['number']=clean_number(origin.get('number',''))
                    if origin.get('country'):origin['country']=country_name(origin['country'])
                    if (origin.get('competition'),origin.get('year'),origin['number'],origin.get('section',''))==(p['competition'],p['year'],p['number'],p.get('section','')):continue
                if origin not in appearances:appearances.append(origin)
            p['appearances']=appearances
            p['originCountries']=sorted({p['country']}|{a['country'] for a in appearances if isinstance(a,dict) and a.get('country')})
            p['originCompetitions']=sorted({p['competition']}|{a['competition'] for a in appearances if isinstance(a,dict) and a.get('competition')})
            p['originYears']=sorted({p['year']}|{int(a['year']) for a in appearances if isinstance(a,dict) and str(a.get('year','')).isdigit()})
            p['contribution']=name
            # Rendering safety: the page parser permits only HTTPS or local figures.
            for key in ['statement','solution']:
                if p.get(key):
                    p[key]=re.sub(r'!\[([^\]]*)\]\((images/[^)]+)\)',r'![\1](https://mathnet.mit.edu/\2)',p[key])
                    for url,local in asset_map.items():p[key]=p[key].replace(']('+url+')',']('+local+')')
            problems.append(p)
    f=ROOT/'research'/f'{name}-coverage.json'
    if f.exists():ledgers[name]=json.loads(f.read_text())

unique={};duplicates=[]
for p in problems:
    if p['id'] in unique:
        duplicates.append({'id':p['id'],'type':'same ID'});continue
    unique[p['id']]=p
problems=list(unique.values())
# Only mathematically confirmed cross-contribution matches are merged.
merges=[]
merge_path=ROOT/'data'/'duplicate-map.json'
for match in json.loads(merge_path.read_text()) if merge_path.exists() else []:
    keep=unique.get(match['keep']);other=unique.get(match['merge'])
    if not keep or not other:continue
    appearance={k:other[k] for k in ['country','competition','year','section','number','sourceUrl','sittingDate'] if k in other}
    if appearance not in keep['appearances']:keep['appearances'].append(appearance)
    for a in other.get('appearances',[]):
        if a not in keep['appearances']:keep['appearances'].append(a)
    keep['notes']=(keep.get('notes','')+' '+match.get('note','')).strip()
    if not keep.get('solution') and other.get('solution'):
        for k in ['solution','solutionKind','solutionCredit','solutionUrl']:
            if k in other:keep[k]=other[k]
    keep['originCountries']=sorted(set(keep['originCountries'])|set(other['originCountries']))
    keep['originCompetitions']=sorted(set(keep['originCompetitions'])|set(other['originCompetitions']))
    keep['originYears']=sorted(set(keep['originYears'])|set(other['originYears']))
    problems=[p for p in problems if p['id']!=other['id']]
    merges.append(match)
# Interleave sources without assigning or changing their difficulty.
groups=collections.defaultdict(list)
for p in problems:groups[p['country']].append(p)
for a in groups.values():a.sort(key=lambda p:(-p['year'],p['competition'],p['number']))
ordered=[]
while any(groups.values()):
    for country in sorted(groups):
        if groups[country]:ordered.append(groups[country].pop(0))
for i,p in enumerate(ordered):p['order']=i
problems=ordered
paper_groups={}
def assessed(record):
    return isinstance(record.get('difficulty'),(int,float)) and not str(record.get('status','')).startswith(('withheld','quarantined','pending'))
def paper_record(country,competition,year,section,number,complete=False):
    if not(country and competition and year):return
    country=country_name(country);section=section or ''
    key=(country,competition,str(year),section)
    g=paper_groups.setdefault(key,{'country':country,'competition':competition,'year':year,'section':section,'numbers':set(),'complete':False})
    if number is not None:g['numbers'].add(clean_number(number))
    g['complete']=g['complete'] or complete
for p in problems:
    paper_record(p['country'],p['competition'],p['year'],p.get('section'),p['number'])
    for a in p.get('appearances',[]):
        if isinstance(a,dict):paper_record(a.get('country',p['country']),a.get('competition'),a.get('year'),a.get('section'),a.get('number'))
for name,d in ledgers.items():
    if name=='british':
        for x in d.get('screening',[]):
            if x.get('difficulty') is not None:paper_record('United Kingdom','BMO'+str(x['round']),x['year'],'',x['number'])
        for x in d.get('historicalScreening',[]):
            if x.get('difficulty') is not None:paper_record('United Kingdom',x['competition'],x['year'],'',x['number'])
        for x in d.get('papers',[]):
            if x.get('status')=='fully-screened':
                for num in x.get('questionNumbers',[]):paper_record('United Kingdom',x['competition'],x['archiveYear'],'',num,True)
    elif name=='americas':
        for x in d.get('fullyScreened',[])+d.get('partiallyScreened',[]):
            country='Canada' if x['competition'] in ['CMO','CJMO'] else 'United States' if x['competition'] in ['USAMO','USAJMO'] else x.get('country')
            rat=x.get('ratings',[])
            for num in ([num for num,value in rat.items() if isinstance(value,(int,float))] if isinstance(rat,dict) else [i for i,value in enumerate(rat,1) if isinstance(value,(int,float))]):
                paper_record(country,x['competition'],x['year'],x.get('section'),num,x in d.get('fullyScreened',[]))
    for x in d.get('decisions',[])+d.get('ledger',[]):
        if assessed(x):paper_record(x.get('country'),x.get('competition'),x.get('year'),x.get('section'),x.get('number'))
    if isinstance(d.get('papers'),list):
        for x in d.get('papers',[]):
            if x.get('complete'):
                for q in d.get('decisions',[])+d.get('ledger',[]):
                    if all(q.get(k)==x.get(k) for k in ['country','competition','year','section']):paper_record(q['country'],q['competition'],q['year'],q['section'],q['number'],True)
    if name=='international':
        for x in d.get('excluded',[]):
            comp=x.get('competition','');prefix=x.get('id','').split('_')[0]
            country={'apm':'Asia-Pacific','egm':'European Girls’ Olympiad','bmo':'Balkan Olympiad','jbm':'Junior Balkan Olympiad','imo':'International Mathematical Olympiad','nmc':'Nordic Olympiad','bxm':'Benelux Olympiad','mem':'Middle European Olympiad','rmm':'Romanian Master of Mathematics'}.get(prefix)
            if country and x.get('difficulty') is not None:paper_record(country,comp,x.get('year'),x.get('section'),x.get('number'))
paper_reviews=[]
for g in paper_groups.values():
    g['numbers']=sorted(g['numbers'],key=lambda s:(not s.isdigit(),int(s) if s.isdigit() else s))
    paper_reviews.append(g)
paper_reviews.sort(key=lambda g:(g['country'],-int(g['year']),g['competition'],g['section']))
sources=[]
for country in sorted({c for p in problems for c in p['originCountries']}):
    a=[p for p in problems if country in p['originCountries']]
    origins=[{'competition':p['competition'],'year':p['year'],'sourceUrl':p['sourceUrl']} for p in a if p['country']==country]
    origins.extend(o for p in a for o in p.get('appearances',[]) if isinstance(o,dict) and o.get('country')==country)
    years=sorted({p['year'] for p in origins});comps=sorted({p['competition'] for p in origins})
    desc=f"Individually assessed entries from {', '.join(comps)}. Included years: {', '.join(map(str,years))}. This does not mean every paper in those years was screened."
    papers=[g for g in paper_reviews if g['country']==country]
    details='Assessed question identifiers (an entire paper is complete only where explicitly stated):\n\n'+'\n'.join('- **'+g['competition']+' '+str(g['year'])+(' · '+g['section'] if g['section'] else '')+'** — '+', '.join(g['numbers'])+(' · complete paper' if g['complete'] else '') for g in papers)
    if country=='United Kingdom':details+='\n\n'+ledgers.get('british',{}).get('yearConvention','')
    archive=next((o['sourceUrl'] for o in origins if o.get('sourceUrl')),a[0]['sourceUrl'])
    sources.append({'name':country,'country':country,'included':len(a),'status':'partial','completePapers':sum(g['complete'] for g in papers),'partialPapers':sum(not g['complete'] for g in papers),'description':desc,'details':details,'archiveUrl':archive})
planned=['United Kingdom','United States','Canada','Australia','New Zealand','China','India','Japan','South Korea','Taiwan','Hong Kong','Macau','Mongolia','Singapore','Vietnam','Thailand','Indonesia','Malaysia','Philippines','Bangladesh','Pakistan','Sri Lanka','Nepal','Iran','Türkiye','Israel','Kazakhstan','Uzbekistan','Kyrgyzstan','Armenia','Azerbaijan','Georgia','Russia','Soviet Union','Ukraine','Belarus','Poland','Czech Republic','Slovakia','Hungary','Romania','Bulgaria','Serbia','Croatia','Slovenia','Bosnia and Herzegovina','Montenegro','North Macedonia','Albania','Greece','Cyprus','Moldova','Ireland','France','Germany','Austria','Switzerland','Italy','Spain','Portugal','Belgium','Netherlands','Luxembourg','Denmark','Norway','Sweden','Finland','Iceland','Estonia','Latvia','Lithuania','Brazil','Argentina','Mexico','Chile','Peru','Colombia','Uruguay','Paraguay','Bolivia','Ecuador','Venezuela','Costa Rica','Cuba','South Africa','Morocco','Tunisia','Algeria','Egypt','Nigeria','Pan-African Olympiad','Balkan Olympiad','Junior Balkan Olympiad','Asia-Pacific','European Girls’ Olympiad','Middle European Olympiad','Baltic Way','Nordic Olympiad','Benelux Olympiad','Ibero-American Olympiad','May Olympiad','International Mathematical Olympiad','Romanian Master of Mathematics','Zhautykov Olympiad','Tuymaada']
present={r['country'] for r in sources}
planned=list(dict.fromkeys(country_name(x) for x in planned))
for name in planned:
    if name not in present:sources.append({'name':name,'country':name,'included':0,'status':'pending','description':'Within the agreed search scope; no individually assessed problems published from this source yet.'})
def reviewed_count(name,d):
    if name=='british':return sum(x.get('difficulty') is not None for x in d.get('screening',[])+d.get('historicalScreening',[]))
    if name=='americas':
        return sum(sum(isinstance(v,(int,float)) for v in (p.get('ratings',{}).values() if isinstance(p.get('ratings'),dict) else p.get('ratings',[]))) for p in d.get('fullyScreened',[])+d.get('partiallyScreened',[]))
    for field in ['decisions','ledger']:
        if isinstance(d.get(field),list):return sum(assessed(x) for x in d[field])
    for k in ['reviewedCount','problemAppearancesScreened','screenedCount','assessedCount']:
        if isinstance(d.get(k),int):return d[k]
    for k in ['screening','decisions','reviewed']:
        if isinstance(d.get(k),list):return len(d[k])
    return 0
screened=sum(reviewed_count(name,d) for name,d in ledgers.items())
remaining_work=[]
region_names={'british':'United Kingdom','ireland':'Ireland','americas':'Americas','asia':'Asia','europe':'Continental Europe','international':'International & regional contests','oceania-africa':'Oceania & Africa','nordic':'Nordic countries','baltic':'Baltic countries','belgium':'Belgium'}
for name,d in ledgers.items():
    notes=[]
    if name=='asia' and isinstance(d.get('pendingRecords'),int):
        notes.append(f"{d['pendingRecords']:,} discovered questions await review: {d.get('pendingDownloadedRecords',0):,} downloaded and {d.get('pendingUndownloadedRecords',0):,} not yet downloaded. This inventory is not a count of every question ever published in Asia.")
    if name=='ireland' and d.get('unresolved'):
        notes.append(f"{len(d['unresolved'])} questions have unresolved statement, diagram or proof checks; their exact identifiers are retained in the ledger.")
    for field in ['gaps','knownGaps','archiveGaps']:
        for gap in d.get(field,[]):
            if isinstance(gap,str):notes.append(re.sub(r'research/[A-Za-z0-9_./-]+\.json','the downloadable coverage ledger',gap))
            elif isinstance(gap,dict):
                if gap.get('fullyScreenedPapers'):continue
                detail=gap.get('detail') or gap.get('status') or gap.get('description')
                label=gap.get('country') or gap.get('range')
                if detail:notes.append((str(label)+': ' if label else '')+str(detail))
    if notes:remaining_work.append({'region':region_names.get(name,name),'notes':list(dict.fromkeys(notes))})
archive_inventories={}
for name,relative in {'asia':'asia/archive-inventory.json','international':'international-historical-inventory.json','europe':'europe/completion-checkpoint.json','americas':'americas/historical-inventory.json'}.items():
    path=ROOT/'research'/relative
    if path.exists():archive_inventories[name]=json.loads(path.read_text())
coverage={
 'updated':'23 October 2026',
 'ratingScale':{'minimum':1,'maximum':10,'step':0.5,'preferredMinimum':4,'preferredMaximum':7},
 'publicationPolicy':'All source-verified, individually assessed questions are eligible regardless of difficulty. The preferred 4–7 range is only the default browsing filter. Source and proof holds remain separate.',
 'difficultyDistribution':{'belowPreferred':sum(p['difficulty']<4 for p in problems),'preferred':sum(4<=p['difficulty']<=7 for p in problems),'abovePreferred':sum(p['difficulty']>7 for p in problems)},
 'summary':'A worldwide, historical search with individual mathematical assessment. Every published problem has a numerical rating and a specific reason. The full search scope is larger than the reviewed collection; gaps are shown explicitly below.',
 'scopeNote':'Archive coverage is incomplete: more years, rounds and competitions remain to be reviewed. This is separate from whether a listed paper has been fully assessed.',
 'screenedCount':screened,'completePaperCount':sum(g['complete'] for g in paper_reviews),'includedCount':len(problems),'sources':sources,'reviewedPapers':paper_reviews,'reviewLedgers':ledgers,
 'remainingWork':remaining_work,
 'archiveInventories':archive_inventories,
 'anchors':[
  {'label':'BMO1 1994, Problem 5','rating':5,'reason':'Alternating-parity subsequences lead to a Fibonacci recurrence.'},
  {'label':'BMO1 1997, Problem 3','rating':4.5,'reason':'A structured coin-change count with useful grouping.'},
  {'label':'BMO2 1998, Problem 3','rating':5.5,'reason':'An Egyptian-fraction relation reveals a gcd and square structure.'},
  {'label':'BMO1 1997, Problem 4','rating':2,'reason':'A short Varignon area argument, below the preferred range despite its question number.'}
 ],
 'subtopicMethod':'Canonical labels normalize reviewed technique tags. Missing and ambiguous metadata have been checked against the question and individual solution analysis; explicit edits are retained. Subtopics do not determine numerical ratings.',
 'subtopics':{t:sorted({s for p in problems if p['topic']==t for s in p['subtopics']}) for t in RULES},
 'method':'Every published rating is an individual AI mathematical assessment in half-point steps, using statement and solution analysis. Not an official rating, contest-position formula, or solve-rate measurement.',
 'compilationIssues':issues,'duplicates':duplicates,'confirmedMerges':merges
}
def write_atomic(path,data):
    temp=path.with_suffix('.tmp');temp.write_text(json.dumps(data,ensure_ascii=False,separators=(',',':')));temp.replace(path)
write_atomic(OUT/'problems.json',problems);write_atomic(OUT/'coverage.json',coverage)
write_atomic(OUT/'bmo-overview.json',build_overview(problems,ledgers['british']))
write_atomic(ROOT/'research'/'compilation-report.json',{'included':len(problems),'screened':screened,'issues':issues,'duplicates':duplicates,'confirmedMerges':merges,'byContribution':dict(collections.Counter(p['contribution'] for p in problems))})
print(json.dumps({'included':len(problems),'screened':screened,'countriesAndBodies':len(present),'issues':issues,'duplicates':len(duplicates)},ensure_ascii=False))

# Official first-round paper catalogue and empirical mock templates.
from build_papers import build_papers
(OUT / "papers.json").write_text(json.dumps(build_papers(problems=problems), ensure_ascii=False, indent=2) + "\n")
