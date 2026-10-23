"""Explicit mathematical reassessments after comparing repeated appearances.

Run after regional reconstruction and before compile.py. This file contains
editorial decisions, not a formula for assigning problem difficulty.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(name):
    return json.loads((ROOT / name).read_text())

def write(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

reason = ('The right triangles BAH and BNM are congruent: their hypotenuses '
          'AB and BN are equal and their angles at B coincide. Thus BM=BC/2 '
          'and MN=AH, immediately giving the area and boundary-length bisections. '
          'This is a short single-observation problem, reassessed below the preferred range.')
british = read('data/british.json')
for p in british:
    if p['id'] == 'bmo1-2018-q3':
        p.update(difficulty=3.5, ratingReason=reason)
write('data/british.json', british)
ledger = read('research/british-coverage.json')
for r in ledger['screening']:
    if r['year'] == 2018 and r['round'] == 1 and r['number'] == 3:
        r.update(difficulty=3.5, decision='include', reason=reason,
                 duplicateAppearance='Croatian Mathematical Competition 2019, County Round, Year 1 Variant A, Q4')
for p in ledger['papers']:
    if p.get('competition') == 'BMO1' and p.get('archiveYear') == 2018:
        p['includedCount'] = sum(x['competition'] == 'BMO1' and x['year'] == 2018 for x in british)
ledger['counts'].update(included=len(british),
    excluded=ledger['counts']['assessed']-len(british),
    withOwnWorkedSolution=sum(bool(x.get('solution')) for x in british),
    withOfficialSolutionLink=sum(bool(x.get('solutionUrl')) for x in british))
write('research/british-coverage.json', ledger)

reason = ('The upper construction puts all but the largest entry below 1/2. '
          'For the lower bound, interchange the two colours and use a discrete '
          'product identity: the two sums add to the product of their final '
          'entries plus strictly positive products of increments.')
solution = r'''Write $n=1012$. For any colouring, positivity gives
$$S=\sum_{i=1}^n r_i(b_i-b_{i-1})\le r_nb_n\le x_{2023}.$$
For (a), choose $x_i=i/4048$ for $1\le i\le2023$ and $x_{2024}=1$.
Then every colouring has $S<1/2$.

For (b), colour the two largest entries differently and distribute the others
so that each colour occurs $n$ times. Then $r_nb_n=x_{2023}$. Set $r_0=0$.
The colouring obtained by exchanging red and blue has sum
$$T=\sum_{i=1}^n b_i(r_i-r_{i-1}).$$
Put $\Delta r_i=r_i-r_{i-1}$ and $\Delta b_i=b_i-b_{i-1}$. The identity
$$r_i\Delta b_i+b_i\Delta r_i
=r_ib_i-r_{i-1}b_{i-1}+\Delta r_i\Delta b_i$$
telescopes to
$$S+T=r_nb_n+\sum_{i=1}^n\Delta r_i\Delta b_i>x_{2023}.$$
Every increment is positive. Hence at least one of these two colourings has
sum greater than $x_{2023}/2$, as required.'''
nordic = read('data/nordic.json')
for p in nordic:
    if p['id'] == 'nordic-denmark-2024-5':
        p.update(difficulty=4.5, ratingReason=reason, solution=solution,
                 solutionKind='original-exposition',
                 solutionCredit='Original English exposition; official Danish solution also linked',
                 subtopics=['Inequalities', 'Sequences & recurrences', 'Constructions'])
write('data/nordic.json', nordic)
ledger = read('research/nordic-coverage.json')
for r in ledger['decisions']:
    if r.get('id') == 'nordic-denmark-2024-5':
        r.update(difficulty=4.5, ratingReason=reason)
write('research/nordic-coverage.json', ledger)

merges = read('data/duplicate-map.json')
if not any(x['merge'] == 'hrv_2019_3d8657' for x in merges):
    merges.append({'keep':'bmo1-2018-q3','merge':'hrv_2019_3d8657',
                   'note':'The same triangle bisection problem appeared in the Croatian Mathematical Competition 2019, County Round, Year 1 Variant A, Q4. Both appearances are reconciled at difficulty 3.5.'})
if not any(x['merge'] == 'arm_2025_g11-12_6' for x in merges):
    merges.append({'keep':'nordic-denmark-2024-5','merge':'arm_2025_g11-12_6',
                   'note':'The same two-part colouring problem appeared in the Armenian National Mathematical Olympiad 2025, Grade 11–12, Q6.'})
if not any(x['merge'] == 'ca-cmo-1971-10' for x in merges):
    merges.append({'keep':'irmo-1989-7','merge':'ca-cmo-1971-10',
                   'note':'The same one-way telephone-information problem appeared as CMO 1971 Q10. Both appearances are reconciled at difficulty 4.5.'})
write('data/duplicate-map.json', merges)

reason = ('The first person to know everything provides a useful time cut; '
          'a connectivity lower bound before that moment must be combined '
          'with separate recipients afterwards.')
americas = read('data/americas.json')
for p in americas:
    if p['id'] == 'ca-cmo-1971-10':
        p.update(difficulty=4.5, ratingReason=reason)
write('data/americas.json', americas)
ledger = read('research/americas-coverage.json')
for p in ledger['fullyScreened']:
    if p['competition'] == 'CMO' and p['year'] == 1971:
        p['ratings']['10'] = 4.5
        p['assessmentNotes']['10'] = reason
write('research/americas-coverage.json', ledger)

# The 1992 CIS competition is a regional body, not a still-existing USSR.
europe = read('data/europe.json')
ledger = read('research/europe-coverage.json')
for r in europe + ledger.get('decisions', []) + ledger.get('papers', []):
    if r.get('country') == 'Soviet Union' and r.get('competition') == 'CIS Mathematical Olympiad':
        r['country'] = 'Commonwealth of Independent States'
write('data/europe.json', europe)
write('research/europe-coverage.json', ledger)
