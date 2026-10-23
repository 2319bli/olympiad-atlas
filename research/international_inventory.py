"""Build a finite main-paper inventory; pending slots are never difficulty ratings."""
import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
R = ROOT / 'research'
coverage = json.loads((R / 'international-coverage.json').read_text())
ledger = coverage['assessmentLedger']
existing = {(p['competition'], p['year']): p for p in coverage['paperCoverage']}

# Numbering is the main-paper numbering, not shortlist or question-position ratings.
series = [
    ('IMO', 1959, 2026, 6, 'https://www.imo-official.org/editions/'),
    ('APMO', 1989, 2026, 5, 'https://www.apmo-official.org/problems'),
    ('EGMO', 2012, 2026, 6, 'https://www.egmo.org/egmos/'),
    ('JBMO', 1997, 2026, 4, 'https://jbmo2026.ssmr.ro/'),
    ('Balkan Mathematical Olympiad', 1984, 2026, 4, 'https://www.imo-register.org.uk/2007-balkan-report.html'),
    ('MEMO', 2007, 2026, None, 'https://www.memo-official.org/MEMO/contests/previous/'),
    ('BxMO', 2009, 2026, 4, 'https://bxmo.org/'),
    ('NMC', 1987, 2026, 4, 'https://www.georgmohr.dk/nmcperm/probl/'),
    ('Baltic Way', 1990, 2026, 20, 'https://bw2026.lt/'),
]

def norm_number(n):
    return re.sub(r'^Problem\s*', '', str(n)).strip().rstrip('.')

def ranges(years):
    out = []
    for y in sorted(set(years)):
        if out and y == out[-1][-1] + 1:
            out[-1].append(y)
        else:
            out.append([y])
    return [str(a[0]) if len(a) == 1 else f'{a[0]}–{a[-1]}' for a in out]

papers = []
for comp, start, end, usual_count, archive in series:
    for year in range(start, end + 1):
        sections = [('Individual', 4), ('Team', 8)] if comp == 'MEMO' else [('Main paper', usual_count)]
        for section, count in sections:
            primary = archive
            count_status = 'standard-format; individual-year-paper-verification-pending'
            notes = []
            event_status = 'historical-paper-pending-source-verification'
            if comp == 'IMO':
                primary = f'https://www.imo-official.org/problems/{year}/'
                count = 7 if year in (1960, 1962) else 6
                count_status = 'official-main-paper-format-with-verified-early-exceptions'
                event_status = 'edition-listed-in-official-archive'
            elif comp == 'EGMO':
                primary = f'https://www.egmo.org/egmos/egmo{year-2011}/'
                count = 8 if year == 2012 else 6
                if year == 2012:
                    count_status = 'verified-official-edition-metadata'
                    notes.append('The first EGMO has eight problems across two days; do not apply the later six-problem format.')
                event_status = 'edition-listed-in-official-archive'
            elif comp in ('APMO', 'BxMO', 'NMC', 'MEMO', 'JBMO'):
                event_status = 'edition-listed-in-official-archive'
            elif comp == 'Baltic Way' and year == 2026:
                event_status = 'future-event-not-yet-held'
                notes.append('Official host schedules the event for 12–16 November 2026, after the inventory date. No released 2026 paper is claimed.')
            if comp == 'JBMO' and year == 1997:
                count = 5
                count_status = 'candidate-five-question-paper; original-paper-count-unverified'
                notes.append('A secondary index contains a fifth question. Five candidate slots prevent silent omission; neither the exact paper size nor its content is claimed verified.')
            if (comp == 'IMO' and year == 1980) or (comp == 'MEMO' and year == 2020 and section == 'Team'):
                count = 0
                count_status = 'verified-not-held'
                event_status = 'not-held'
                primary = archive if comp == 'IMO' else 'https://memo2024.bolyai.hu/about/statistics'
                notes.append('No IMO took place in 1980.' if comp == 'IMO' else 'The official MEMO history confirms that 2020 had only an individual contest.')
            relevant = [d for d in ledger if d['competition'] == comp and d['year'] == year]
            if comp == 'MEMO':
                relevant = [d for d in relevant if norm_number(d['number']).startswith('I-' if section == 'Individual' else 'T-')]
            reviewed = {norm_number(d['number']): d for d in relevant}
            held = {}
            for d in coverage.get('deferred', []):
                if d['competition'] == comp and d['year'] == year:
                    held[norm_number(d['number'])] = d
            questions = []
            for n in range(1, count + 1):
                number = ('I-' if section == 'Individual' else 'T-') + str(n) if comp == 'MEMO' else str(n)
                identifier_status = 'verified-paper-numbering' if comp == 'IMO' or (comp == 'EGMO' and year == 2012) else 'provisional-format-slot'
                q = {'number': number, 'status': 'pending-individual-assessment', 'identifierVerificationStatus': identifier_status, 'difficulty': None}
                if number in reviewed:
                    d = reviewed[number]
                    q.update({'status': 'individually-assessed', 'identifierVerificationStatus': 'verified-in-individual-assessment', 'reviewId': d['id'], 'decision': d['decision'], 'difficulty': d['difficulty'], 'sourceUrl': d['sourceUrl']})
                elif number in held:
                    d = held[number]
                    q.update({'status': 'held-unrated-source-or-proof-defect', 'holdId': d['id'], 'reason': d['reason']})
                elif event_status == 'future-event-not-yet-held':
                    q['status'] = 'future-paper-not-yet-published'
                    q['identifierVerificationStatus'] = 'future-format-placeholder'
                questions.append(q)
            assessed = [q for q in questions if q['status'] == 'individually-assessed']
            complete = bool(count and len(assessed) == count and 'candidate-' not in count_status)
            if complete:
                count_status = 'verified-individually-assessed-whole-paper'
            papers.append({'competition': comp, 'year': year, 'section': section,
                           'archiveUrl': archive, 'editionOrSourceUrl': primary, 'eventStatus': event_status,
                           'questionCount': count, 'questionCountStatus': count_status,
                           'paperFullyAssessed': complete, 'assessedCount': len(assessed),
                           'includedCount': sum(q.get('decision') == 'included' for q in questions),
                           'remainingNumbers': [q['number'] for q in questions if q['status'] != 'individually-assessed'],
                           'questions': questions, 'notes': notes})

summary = []

def totals(pp):
    questions = [q for p in pp for q in p['questions']]
    verified = [q for q in questions if q['identifierVerificationStatus'].startswith('verified-')]
    pending = [q for q in questions if q['status'] != 'individually-assessed']
    future = [q for q in pending if q['status'] == 'future-paper-not-yet-published']
    historical = [q for q in pending if q['status'] != 'future-paper-not-yet-published']
    return {'inventoriedSlotsIncludingProvisionalAndFuture': len(questions),
            'verifiedQuestionIdentifiers': len(verified),
            'assessedQuestions': sum(q['status'] == 'individually-assessed' for q in questions),
            'includedQuestions': sum(q.get('decision') == 'included' for q in questions),
            'historicalBacklogVerifiedQuestionIdentifiers': sum(q['identifierVerificationStatus'].startswith('verified-') for q in historical),
            'historicalBacklogProvisionalQuestionSlots': sum(q['identifierVerificationStatus'] == 'provisional-format-slot' for q in historical),
            'futureEventPlaceholderSlots': len(future),
            'fullyAssessedPaperSections': sum(p['paperFullyAssessed'] for p in pp)}

for comp, start, end, _, archive in series:
    pp = [p for p in papers if p['competition'] == comp]
    active = [p for p in pp if p['eventStatus'] != 'not-held']
    summary.append({'competition': comp, 'startYear': start, 'endYear': end,
                    'archiveUrl': archive, 'paperSections': len(active),
                    **totals(pp),
                    'fullyAssessedYears': ranges(y for y in range(start, end + 1) if all(p['paperFullyAssessed'] for p in active if p['year'] == y) and any(p['year'] == y for p in active)),
                    'yearsWithPendingQuestions': ranges(p['year'] for p in active if not p['paperFullyAssessed']),
                    'notHeld': [{'year': p['year'], 'section': p['section']} for p in pp if p['eventStatus'] == 'not-held']})

inventory = {'asOf': '2026-10-23', 'complete': False,
             'scope': 'Finite main-paper inventory for nine requested major international series. Other international series and shortlists remain separate in the assessment ledger.',
             'method': 'Verified question identifiers, provisional historical format slots, and future-event placeholders are separate categories. A provisional slot is a discovery task, not a verified question. Only the assessment ledger supplies ratings. No future event is counted as historical backlog.',
             'exceptions': ['IMO 1960 and 1962: seven problems; IMO 1980: not held.', 'EGMO 2012: eight problems.', 'MEMO 2020: individual contest only; no team paper.', 'JBMO 1997: five candidate slots, original paper count still unverified.', 'Baltic Way 2026: future event, 12–16 November 2026.'],
             'totals': totals(papers), 'summary': summary, 'papers': papers}
(R / 'international-historical-inventory.json').write_text(json.dumps(inventory, ensure_ascii=False, indent=2))
coverage['historicalInventory'] = {'path': 'research/international-historical-inventory.json', 'asOf': inventory['asOf'], 'complete': False, 'totals': inventory['totals'], 'summary': summary, 'exceptions': inventory['exceptions']}
coverage['gaps'] = [
    'IMO main papers 1990–2021 remain pending: 32 papers / 192 questions. Complete main-paper ranges are 1959–1979, 1981–1989 and 2022–2026; 1980 was not held.',
    'The finite main-paper inventory is research/international-historical-inventory.json. Verified historical identifiers, provisional historical format slots and future-event placeholders are counted separately. It is not a claim of exhaustive historical assessment.',
    'International shortlists and other series retain partial coverage; downloaded records are not counted as reviewed.',
    'Unresolved statement or proof defects are held unrated in deferred. Baltic Way 2026 has not yet taken place as of 2026-10-23.'
]
(R / 'international-coverage.json').write_text(json.dumps(coverage, ensure_ascii=False, indent=2))
print(json.dumps(summary, ensure_ascii=False, indent=2))
