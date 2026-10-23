# Review and publication checkpoints

The authoritative reviewed collection is `data/*.json`, with decisions and
coverage in `research/*-coverage.json`. These records preserve individual
mathematical assessments; compilation never assigns a difficulty.

To assemble and check the existing reviewed collection:

```bash
python research/reconcile-confirmed-duplicates.py
python research/compile.py
node research/validate.cjs
```

When validation lists new external diagram URLs, run
`python research/cache-diagrams.py`, then compile and validate again. The cache
helper reads the validation report, so validation must precede caching newly
added diagrams.

All individually reviewed questions with verified statements are eligible on
the 1–10 scale. The 4–7 range is only the browser's default practice filter.
Source and proof holds remain withheld; unreviewed archives are not assigned
ratings or included by this policy change. Each region retains its restoration
scripts and statement overrides alongside the original review ledger. These
restore existing individual assessments, rather than estimating difficulty
from a question number or competition.

`research/subtopics.py` respects explicit reviewed classifications and the
overrides in `data/`, then normalizes legacy technique tags. The duplicate map
contains only pairs checked mathematically, with scope differences explained.
The reconciliation script records explicit editorial reassessments made when
comparing repeated appearances.

Regional Python scripts retain manually written assessments and original
expositions. They are historical research checkpoints, not a single pipeline:
some depend on downloaded public PDFs, text extraction, or raw archive records;
some baseline builders replace their regional output. Do not run all scripts
indiscriminately. Reconstruct a region only with its own documented sequence,
then run the reconciliation and compilation steps above.

The Asia archive inventory, international historical inventory, and European
checkpoint are embedded in the downloadable website coverage ledger. Other
regional inventories are embedded directly in their regional ledgers. Verified
question identifiers, provisional paper-size assumptions, future events,
unread material, and source or proof holds remain separate. None of these
inventories establishes worldwide historical exhaustiveness.

Source documents can be retrieved again from their recorded URLs. Tracked
assessment data and prose are the durable result; a source-access failure does
not justify reconstructing a missing problem from its question number.

The additive USAMO 2004–2005 checkpoint is
`python research/americas/complete_usamo_2004_2005.py`, followed by the standard
reconciliation, compilation and validation commands above. It updates the
question bank and both Americas coverage records idempotently. When rebuilding
the historical Americas sequence, run this after `check_historical_checkpoint.py`.
