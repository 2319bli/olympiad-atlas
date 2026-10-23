"""Persist the historical British source-access checkpoint without rating unseen papers."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
path = root / 'research/british-coverage.json'
coverage = json.loads(path.read_text())
coverage.setdefault('sourceAudit', {})['historicalAccessCheck'] = {
    'checkedDate': '2026-10-23',
    'officialIndex': 'https://bmos.ukmt.org.uk/home/bmo.shtml',
    'unavailableOriginalPapers': ['BMO 1965–1972', 'FIST 1973'],
    'bookAlternative': {
        'title': 'The Mathematical Olympiad Handbook',
        'author': 'Tony Gardiner',
        'publisher': 'Oxford University Press',
        'year': 1997,
        'url': 'https://global.oup.com/academic/product/the-mathematical-olympiad-handbook-9780198501053',
        'scope': 'The official archive identifies this book as containing BMO statements from 1965–1996, with hints and outline solutions for 1975–1996.',
        'accessResult': 'The linked publisher page returned a JavaScript/robot-verification gate. No book pages or unavailable original papers were obtained or assessed.'
    },
    'secondarySearchLeads': [
        {'url': 'https://schoolexercisebooks.blogspot.com/2010/08/1st-british-mathematical-olympiad-1965.html', 'status': 'Search surfaced a secondary reproduction; not verified against an original or authorized book page, so it was not promoted to assessed coverage.'},
        {'url': 'https://imogeometry.blogspot.com/p/british.html', 'status': 'Partial geometry-only secondary index; it cannot establish complete-paper coverage.'}
    ],
    'fist1973': 'No verifiable accessible alternative paper found.',
    'fist1987': 'The official archive states no FIST was held; a Reading Selection Test replaced it. Its paper is not linked in the archive.',
    'result': 'British counts and assessed ranges are unchanged; the inaccessible years remain explicit source gaps.'
}
path.write_text(json.dumps(coverage, ensure_ascii=False, indent=2))
