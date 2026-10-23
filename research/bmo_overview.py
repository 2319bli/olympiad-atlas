"""Complete recent BMO metadata, including questions outside the practice band.

Ratings come unchanged from the individual review ledger. Additional subject
classifications were checked against the official papers in the BMO compendium.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def build_overview(problems, ledger):
    extra = json.loads((ROOT/'data/bmo-overview-extra.json').read_text())
    last = max(p['archiveYear'] for p in ledger['papers'] if p['competition'] in ['BMO1','BMO2'])
    first = last - 9
    bank = {p['id']: p for p in problems}
    reviews = {(r['year'],r['round'],r['number']):r for r in ledger['screening']}
    papers = []
    for paper in ledger['papers']:
        year, comp = paper['archiveYear'], paper['competition']
        if comp not in ['BMO1','BMO2'] or not first <= year <= last:
            continue
        rd = int(comp[-1])
        dates = {p['sittingDate'] for p in problems if p['competition']==comp and p['year']==year and p.get('sittingDate')}
        assert len(dates)==1, f'Check exact sitting date: {comp} {year}'
        rows = []
        for number in paper['questionNumbers']:
            review = reviews[(year,rd,number)]
            ident = f'bmo{rd}-{year}-q{number}'
            metadata = bank.get(ident) or extra.get(ident)
            assert metadata and metadata.get('subtopics'), f'Topic review missing: {ident}'
            d = review['difficulty']
            assert isinstance(d,(int,float)) and 1<=d<=10 and d*2==int(d*2), ident
            if ident in bank:
                assert bank[ident]['difficulty']==d, f'Rating mismatch: {ident}'
            rows.append({'id':ident,'number':number,'topic':metadata['topic'],
                'subtopics':metadata['subtopics'],'difficulty':d,'ratingReason':review['reason'],
                'bankId':ident if ident in bank else None,
                'section':('Section A · answer only' if number<=4 else 'Section B · full proof') if rd==1 and year==2021 else ''})
        assert len(rows)==paper['questionCount']
        papers.append({'id':f'bmo{rd}-{year}','competition':comp,'archiveYear':year,
            'season':f'{year-1}–{str(year)[-2:]}','sittingDate':next(iter(dates)),
            'sourceUrl':paper['sourceUrl'],'questions':rows})
    papers.sort(key=lambda p:(-p['archiveYear'],p['competition']))
    assert len(papers)==20
    return {'firstArchiveYear':first,'lastArchiveYear':last,'paperCount':len(papers),
        'questionCount':sum(len(p['questions']) for p in papers),
        'method':'Individual AI estimates from the same review ledger as the practice bank; not official UKMT ratings. Topic classifications for out-of-band questions were checked against their official statements.',
        'papers':papers}
