# Olympiad Atlas

Worldwide olympiad problem bank with a default practice range calibrated to harder BMO1 and accessible BMO2.

## Requirements agreed with the user

- Worldwide and historical search; the country list is not a cap.
- Every published problem individually assessed numerically, using mathematical statement and solution analysis. No formula based on competition or question number.
- Rating scale 1–10 in half points; preferred range 4–7. Include all reviewed questions from 1–10; difficulty never determines eligibility. Ratings are AI estimates, not official difficulty measurements.
- Include exact competition, year, round/section, question number, source, broad topic, consistent subtopics and detailed technique tags.
- Worked solutions hidden where reliable and available. Link to the precise official solution when reproduction rights are unclear.
- Preserve honest coverage: discovered/downloaded is different from individually reviewed. Never represent partial work as exhaustive.
- Deduplicate equivalents and retain alternate appearances. Quarantine inconsistent statements or solutions.

## Data workflow

Regional contributors write `data/*.json` and `research/*-coverage.json`. Run `python research/compile.py` to validate and assemble the browser collection in `dist/data/`.

Explicit reviewed subtopics are preserved; legacy technique tags are normalized by `research/subtopics.py`. Missing or ambiguous metadata were individually checked against the statements and solution-analysis notes; those explicit classifications are retained in `data/subtopic-overrides.json`. Broad-topic corrections are in `data/topic-overrides.json`. Every compiled question must have at least one subtopic.

The compilation does not generate ratings. Missing ratings, missing provenance, invalid ratings and unknown review status are held out and recorded in `research/compilation-report.json`.

Large unreviewed downloads in `research/raw/` are temporary and git-ignored. Reviewed data and review ledgers are tracked. Website assets live in `public/`, with the root HTML in `atlas.html`. Vinext builds the account API and assets into generated `dist/` output.

## Runtime

Search, filters, random selection, hidden solutions and rating notes, and browser-local save/attempt/solve state. Progress can be exported and restored from My practice. KaTeX and Marked are vendored with licences.

## Hosting

The frontend is published at https://2319bli.github.io/olympiad-atlas/ using GitHub Pages. GitHub Actions builds the static question bank, mock generator and PDF tools on every push to `main`.

The standalone account API is in `cloudflare/` and runs on Cloudflare Workers with D1. Google sign-in uses Google Identity Services; cloud accounts stay disabled until the API and Google client ID are configured. See [GitHub Pages and Cloudflare setup](docs/github-pages-cloudflare.md) for deployment, account migration and verification.

This repository includes source, reviewed question data, assets and schema-only migrations. Production credentials and account records are excluded. The original Site build is retained for continuity; its identity belongs in the ignored `.openai/hosting.json`, using `.openai/hosting.example.json` as a template.

## Collection checkpoint — 23 October 2026

4,402 included problems, 4,552 problem/appearance assessments, 98 countries and regional bodies. The ledger marks 578 papers or grade-specific papers fully reviewed. The collection contains 1,358 questions below 4, 2,736 in the preferred 4–7 range and 308 above 7. Country-wide historical coverage remains incomplete; these counts do not imply exhaustive archives.

The Coverage view lists remaining work by region and exposes precise archive inventories in its downloadable ledger. See `research/REPRODUCIBILITY.md` before rebuilding regional contributions. Confirmed duplicate IDs redirect to their retained entry and saved practice progress is migrated.

## Recent BMO overview

The `#bmo` page lists every question from the last ten archived BMO seasons, including ratings outside the preferred practice range. `research/bmo_overview.py` assembles it during compilation from the British review ledger and reviewed subject metadata in `data/bmo-overview-extra.json`. Sitting dates and season labels distinguish BMO1 archive years from calendar years. The initial release contains 101 questions in 20 papers (2016–17 to 2025–26), including the seven-question 2020–21 BMO1 format.

## Papers and configurable mocks

`#papers` combines 35 official BMO1 papers (archive years 1992–2026), 19 separately labelled pre-split historical papers, and browser-local mock snapshots. The compiler builds `papers.json` with `research/build_papers.py`. Incomplete historical transcriptions have no aggregate rating.

The BMO1 preset retains nine recent six-question topic/rating profiles. BMO2 uses ten reviewed four-question profiles from the last ten archived seasons. Both match each individual rating within 0.5, use 3½ hours and 10 marks per question, exclude advanced prerequisites, and allow at most two questions per country/body. British BMO/FIST, recorded alternate appearances and identical statements remain excluded in every mode; Balkan BMO remains eligible.

Custom papers support 4–10 questions, 15–600 minutes, 1–20 marks per question, difficulty bands in half-point steps, rising/midpoint/random profiles, target tolerance, selected topics with balanced or free mixes, primary-origin country/year filters, country/competition limits, advanced-prerequisite and diagram toggles. Availability controls exclude earlier mocks or attempted questions and optionally require solutions. Selection uses bounded backtracking; it fails explicitly without saving partial papers or relaxing constraints. All original question ratings remain unchanged.

`public/paper-builder.js` owns form controls and browser-local preferences; `paper-engine.js` owns validated settings, selection and snapshots. Version-2 snapshots save the full generation settings, timing and marking; version-1 six-question backups remain readable. The account service shares the engine's validation and normalization. Deploy the updated Cloudflare backend alongside this frontend so cloud sync accepts BMO2 and custom papers; GitHub Pages deployment updates the frontend only.

Client-side A4 PDF exports contain an instructions cover, numbered question pages and separate source credits. They omit solutions and rating/topic hints, label mocks unofficial, and retain original official PDF links. Vendored jsPDF and html2canvas render KaTeX at 240 dpi. Tests: `node tests/paper-engine.cjs`. Browser QA confirmed generation, reload persistence and PDF render completion; cloud-browser policy prevented inspecting/downloading the generated blob PDFs, so final PDF visual verification remains limited.

## Accounts and cloud sync

Atlas remains public. The Account page uses dispatch-owned Sign in with ChatGPT; no app password database or custom OAuth routes. `app/chatgpt-auth.ts` resolves the current visitor, and server queries always scope records to that stable Site user ID. Identity responses and account data are private/no-store. The D1 binding is `DB`; schema-only migrations are generated in `drizzle/` and applied by Sites at publish time.

Account mocks keep immutable question snapshots. Practice updates write individual records rather than replacing an entire collection, so changes to different questions on another device are retained. For conflicting edits to the same practice record, the last update received wins. Account-scoped per-record outboxes retry after reconnect; Web Locks serialize sync across tabs where supported. A signed-in user must explicitly import guest data; import merges papers and preserves solved progress, leaving guest storage intact. Account switches are checked client- and server-side before uploading queued data.

Validation: `node tests/account-service.mjs`, `node tests/account-client.mjs`, `node tests/paper-engine.cjs`, and the Sites build. API tests exercise ownership isolation using the actual SQL migrations, authentication, CSRF, malformed/oversized requests, immutable mock retries, and updates to separate progress records. Client tests cover pending queues, retries, cloud refresh, account changes and guest separation. Managed preview supports anonymous UI QA; hosted ChatGPT authentication is dispatch-owned and cannot be exercised through the local managed preview.

## Google sign-in on the original Site

Google login is implemented as an optional additional provider, with explicit linking to an existing ChatGPT-backed Atlas account. It remains disabled until `GOOGLE_CLIENT_ID` and secret `GOOGLE_CLIENT_SECRET` are configured and the version is redeployed. See `docs/google-sign-in-setup.md` for the exact callback URL, activation and linking steps. Existing Site-owned ChatGPT routes and account IDs are preserved. Tests: `node tests/google-auth.mjs`; real Google consent cannot be verified without the OAuth application credentials.

### Topic guide

The **Topic guide** (`#learn`) explains all 63 subtopic labels currently in the bank, grouped into four mathematical areas and shared proof methods. Each entry includes question styles, techniques, an original worked example, a common trap and live practice links. Learning stages describe prerequisites, not contest difficulty or an official syllabus. Content lives in `public/data/study-guide.json`; `public/study-guide.js` renders the searchable index and deep-linked entries. Practice links clear unrelated filters and include all difficulties. Run `node tests/study-guide.cjs` to check taxonomy coverage, matching problems, links and mathematical typesetting.

### All-time leaderboards

The **Leaderboard** (`#leaderboard`) ranks opted-in users by distinct solved questions by default. Its second ranking sums `1 + difficulty` for each distinct solve. It uses synced practice marks, canonical question IDs and server-held ratings; repeated attempts, repeat syncs and known duplicate appearances cannot add extra points. Ties share ranks, and the page includes pagination and your own rank. Users choose a public display name and can leave without losing private progress. Totals are self-reported, and corrected marks remove contributions. See `docs/github-pages-cloudflare.md` for the catalog migration/deployment steps. Run `node tests/leaderboard.mjs` for scoring, privacy, authentication and pagination checks.
