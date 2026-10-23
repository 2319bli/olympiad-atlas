"""Build the BMO1 paper shelf and empirical mock calibration.

This only groups existing individual assessments. It neither generates nor
changes a question rating. Historical original-paper formats remain explicit.
"""
import json
import statistics
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = 'https://bmos.ukmt.org.uk/home/bmo.shtml'


def build_papers(problems=None, ledger=None):
    if problems is None:
        problems = json.loads((ROOT / 'public/data/problems.json').read_text())
    if ledger is None:
        ledger = json.loads((ROOT / 'research/british-coverage.json').read_text())
    bank = {p['id']: p for p in problems}
    reviews = {(r['competition'], r['year'], str(r['number'])): r
               for r in ledger.get('historicalScreening', [])}
    reviews.update({('BMO' + str(r['round']), r['year'], str(r['number'])): r
                    for r in ledger['screening']})
    official = []
    for source in ledger['papers']:
        comp, year = source['competition'], source['archiveYear']
        if comp not in ('BMO1', 'BMO'):
            continue
        legacy = comp == 'BMO'
        questions = []
        dates = set()
        for number in source['questionNumbers']:
            ident = f'{comp.lower()}-{year}-q{number}'
            p = bank.get(ident)
            review = reviews.get((comp, year, str(number)), {})
            if p and p.get('sittingDate'):
                dates.add(p['sittingDate'])
            section = ''
            marks = None if legacy else 10
            if comp == 'BMO1' and year == 2021:
                section = 'Section A · answer only' if int(number) <= 4 else 'Section B · full proof'
                marks = 5 if int(number) <= 4 else 10
            questions.append({
                'id': ident, 'number': str(number), 'bankId': ident if p else None,
                'difficulty': p['difficulty'] if p else review.get('difficulty'),
                'topic': p.get('topic') if p else None,
                'subtopics': p.get('subtopics', []) if p else [],
                'section': section, 'marks': marks,
                'status': 'available' if p else 'source-hold',
                'note': '' if p else 'Statement withheld pending source clarification; consult the original paper.',
            })
        assert len(dates) <= 1, (comp, year, dates)
        sitting_date = next(iter(dates), None)
        count = source['questionCount']
        assert count == len(questions), (comp, year)
        complete = all(q['bankId'] and isinstance(q['difficulty'], (int, float)) for q in questions)
        season = f'{year-1}–{str(year)[-2:]}' if sitting_date and int(sitting_date[:4]) < year else str(year)
        duration = None if legacy else (150 if year == 2021 else 210)
        if legacy:
            note = 'Historical first-stage BMO, before the BMO1/BMO2 names. Follow the original paper’s timing, marking and choice-of-question rules. Listed alternatives are separate assessed entries.'
        elif year == 2021:
            note = 'Exceptional 2020–21 format: 2½ hours; four answer-only questions worth 5 marks each and three proof questions worth 10 marks each. The rating is an unweighted mean of all seven questions.'
        elif count == 5:
            note = 'Historical five-question BMO1. The paper rating averages all five question ratings; this format is not used to calibrate six-question mocks.'
        else:
            note = 'Six proof questions, 3½ hours, 10 marks per question.'
        official.append({
            'id': f'{comp.lower()}-{year}', 'kind': 'official', 'legacy': legacy,
            'competition': comp, 'archiveYear': year, 'season': season,
            'title': f'{"BMO (historical)" if legacy else "BMO1"} {season}',
            'sittingDate': sitting_date, 'sourceUrl': source['sourceUrl'],
            'questionIds': [q['bankId'] for q in questions], 'questions': questions,
            'questionCount': count, 'expectedQuestionCount': count,
            'availableCount': sum(bool(q['bankId']) for q in questions),
            'complete': complete,
            'rating': statistics.mean(q['difficulty'] for q in questions) if complete else None,
            'durationMinutes': duration,
            'totalMarks': sum(q['marks'] for q in questions) if not legacy else None,
            'formatNote': note,
        })
    official.sort(key=lambda p: (-p['archiveYear'], p['competition']))
    recent_last = max(p['archiveYear'] for p in official if not p['legacy'])
    recent_first = recent_last - 9
    reference_papers = [p for p in official if not p['legacy'] and p['complete']
                        and p['questionCount'] == 6 and recent_first <= p['archiveYear'] <= recent_last]
    templates = [{
        'id': p['id'], 'paperId': p['id'], 'archiveYear': p['archiveYear'],
        'title': p['title'], 'topics': [q['topic'] for q in p['questions']],
        'difficulties': [q['difficulty'] for q in p['questions']],
        'subtopics': [q['subtopics'] for q in p['questions']], 'mean': p['rating'],
    } for p in reference_papers]
    positions = []
    for i in range(6):
        ratings = [p['questions'][i]['difficulty'] for p in reference_papers]
        positions.append({
            'position': i + 1, 'count': len(ratings), 'min': min(ratings),
            'max': max(ratings), 'median': statistics.median(ratings),
            'mean': statistics.mean(ratings), 'ratings': ratings,
            'topicCounts': dict(Counter(p['questions'][i]['topic'] for p in reference_papers)),
        })
    return {
        'version': 1, 'updated': '2026-10-23', 'official': official,
        'scope': 'All 35 BMO1 papers (archive years 1992–2026) and all 19 accessible historical first-stage BMO papers (1973–1991). BMO2 and FIST are excluded.',
        'ratingMethod': 'Unweighted arithmetic mean of every question’s individual difficulty estimate. Historical papers use their actual question count. No whole-paper mean is shown when a question is unavailable. These are AI estimates, not official UKMT ratings.',
        'yearConvention': 'Archive years identify the competition cycle. A November/December sitting can occur in the preceding calendar year; exact sitting dates are retained where verified.',
        'gaps': [{'competition': 'BMO', 'years': '1965–1972', 'sourceUrl': ARCHIVE,
                  'reason': 'The official archive says original papers for these years are not available online. They are not included or rated here.'}],
        'calibration': {
            'version': 1, 'competition': 'BMO1', 'firstArchiveYear': recent_first,
            'lastArchiveYear': recent_last, 'referencePaperCount': len(reference_papers),
            'referenceQuestionCount': 6 * len(reference_papers), 'templates': templates,
            'positions': positions,
            'meanPaperRating': statistics.mean(p['rating'] for p in reference_papers),
            'observedSubtopics': dict(Counter(t for p in reference_papers for q in p['questions'] for t in q['subtopics'])),
            'method': 'Reuse topic sequences and individually reviewed difficulty profiles from complete six-question BMO1 papers in the last ten archived seasons. The exceptional seven-question 2020–21 paper is excluded. Real profiles need not increase strictly with question number. Templates guide selection only; they never assign a question rating.',
            'excludedReferencePapers': [{'id': 'bmo1-2021', 'reason': 'Seven-question exceptional format, including answer-only questions.'}],
            'suitabilityNote': 'Match elementary olympiad methods as well as rating; exclude calculus, advanced linear algebra and projective/conic prerequisites. Exclude all British BMO/BMO1/BMO2/FIST appearances, including known duplicate appearances under another contest name. Balkan competitions with the abbreviation BMO are distinct.',
        },
        'formatSources': [
            {'url': ARCHIVE, 'role': 'Official archive, six-question format, duration, historical format changes and unavailable years.'},
            {'url': 'https://bmos.ukmt.org.uk/home/bmo1-2026.pdf', 'role': 'Modern instructions and layout: A4 portrait, instruction cover, numbered proof questions, 3½ hours and 10 marks per question.'},
            {'url': 'https://bmos.ukmt.org.uk/home/bmo1-2021.pdf', 'role': 'Exceptional 2020–21 timing and section marking.'},
        ],
    }


if __name__ == '__main__':
    data = build_papers()
    output = ROOT / 'public/data/papers.json'
    output.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')) + '\n')
    print(json.dumps({'papers': len(data['official']), 'modernBmo1': sum(not p['legacy'] for p in data['official']),
                      'historicalBmo': sum(p['legacy'] for p in data['official']),
                      'complete': sum(p['complete'] for p in data['official']),
                      'availableQuestions': sum(p['availableCount'] for p in data['official']),
                      'expectedQuestions': sum(p['questionCount'] for p in data['official']),
                      'calibrationPapers': data['calibration']['referencePaperCount']}))
