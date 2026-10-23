"""Check the persisted Irish assessment ledger and entry metadata."""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(root / 'research'))
from subtopics import TAXONOMY

rows = json.loads((root / 'data/ireland.json').read_text())
coverage = json.loads((root / 'research/ireland-coverage.json').read_text())
decisions, holds = coverage['decisions'], coverage['unresolved']
row_ids = {p['id'] for p in rows}
decision_ids = {p['id'] for p in decisions}
hold_ids = {p['id'] for p in holds}
assert len(row_ids) == len(rows)
assert len(decision_ids) == len(decisions)
assert len(hold_ids) == len(holds)
assert not decision_ids & hold_ids
assert row_ids == {d['id'] for d in decisions if d['included']}
assert coverage['attemptedCount'] == len(decisions) + len(holds) == 395
assert coverage['reviewedCount'] == len(decisions) == 356
assert coverage['includedCount'] == len(rows) == 355
assert coverage['unresolvedCount'] == len(holds) == 39
for p in rows:
    assert 1 <= p['difficulty'] <= 10 and p['difficulty'] * 2 % 1 == 0, p['id']
    assert p['reviewStatus'] == 'individually-assessed', p['id']
    assert all(p.get(k) for k in ('country', 'competition', 'year', 'section', 'number', 'sourceUrl', 'statement', 'topic', 'tags', 'subtopics', 'ratingReason')), p['id']
    allowed = set(TAXONOMY[p['topic']])
    assert set(p['subtopics']) <= allowed, (p['id'], p['subtopics'])
for p in coverage['papers']:
    expected, assessed, held = map(set, (p['expectedQuestions'], p['assessedQuestions'], p['heldQuestions']))
    assert expected == assessed | held and not assessed & held, p
    assert p['complete'] == (expected == assessed), p
    assert set(p['pendingQuestions']) == held, p
assert coverage['completePapers'] == sum(p['complete'] for p in coverage['papers']) == 53
assert all(h['difficulty'] is None and not h['included'] and h['reviewStatus'] == 'held-unrated' for h in holds)
solution_gaps = [p['id'] for p in rows if not p.get('solution') and p.get('solutionKind') != 'source-link']
assert coverage['solutionGapIds'] == solution_gaps
print({'included': len(rows), 'new_in_2003_2024': sum(2003 <= p['year'] <= 2024 for p in rows), 'original_solutions': sum(bool(p.get('solution')) for p in rows), 'official_solution_links': sum(p.get('solutionKind') == 'source-link' for p in rows), 'legacy_solution_gaps': len(solution_gaps), 'complete_papers': coverage['completePapers'], 'unrated_holds': len(holds)})
