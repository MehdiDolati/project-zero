# Project Zero — Current State

## Current Direction

The gold trend-following question (Q003) has been **parked** (DEC003) after its
frozen baseline returned a weak/negative result. With no open experiment, the
next direction is to select a **new single research question** under the manual
Question / Observation workflow (AC001) with clear input provenance — not to
re-tune or revive the parked gold question.

## Current Objective

Choose and register the next single research question now that Q003 has been
parked by DEC003, keeping the project's one-question-at-a-time discipline and
not carrying over any assumption from the parked gold work.

## NEXT ACTION

The researcher chose option (c) and parked the gold question, recorded in
[DEC003](../decisions/DEC003-park-gold-question.md). Q003 remains `draft` with
all EXP002 evidence preserved and is listed under Questions and Things to
Revisit in the [Parking Lot](PARKING-LOT.md); parking is a prioritization
decision, not a lifecycle transition. No experiment is currently open.

Next: select and register a **new single research question** through the manual
AC001 workflow, with explicit input provenance, before proposing any hypothesis
or experiment. Do not tune the frozen EXP002 rules against the already-examined
`2020-09-28`–`2026-09-28` window, and do not resume Q003 except with a fresh
out-of-sample window or a materially different, separately frozen design.

## Why This Matters

The actual second manual AC001 test is now recorded in Q003 and S005. The
selected instrument is spot XAU/USD, and the evaluation is a six-year
historical backtest. It only qualifies as out of sample if the strategy rules
are frozen before examining its results. Positive net returns after costs are
the primary success criterion, with comparison to buy-and-hold reported
separately. Each position must be closed no later than one year after entry.
The researcher reports separate Dukascopy public-site exports with `Tick`
selected for Bid and Ask, matching timestamps, and displayed coverage
`5/5/2003`–`28/9/2026`. Shared rows contain OHLCV fields and a
`Europe/Amsterdam` time-zone label. The researcher confirms each row is one
tick and its timestamp is the tick's recorded time, and corrected the Ask
sample to show equal OHLC values per row with multiple ticks sharing
second-level timestamps. Fixed UTC+02 daily boundaries and OHLC aggregation
are approved, preserving file order for duplicate timestamps and omitting
empty days without forward-filling. Full-file conventions remain
unvalidated. The
inclusive six-year window `2020-09-28`–`2026-09-28` is fixed. A baseline
SMA200 long-only strategy, its execution, sizing, time stop, cost treatment,
and buy-and-hold benchmark are frozen before results are examined. The
researcher reports no SMA200 returns from the holdout were reviewed before
the freeze. The full files and historical costs remain unvalidated.

## Blockers

- RESOLVED: The delivered EXP002 raw file was a partial slice; the full master
  (`XAUUSD-TICK-full.csv`, 32,121,180,517 bytes, SHA-256 `4921484a…ad17d4`,
  732,112,910 rows, coverage 2003-05-05–2026-10-02) has now arrived and passed a
  full streaming verification — 0 malformed rows, 0 bad timestamps, 0 bad
  numerics, 0 crossed quotes, 0 ordering violations — and spans the fixed
  `2020-09-28`–`2026-09-28` holdout window.
- RESOLVED (2026-10-06): The researcher accepted an amended registration for the
  delivered format/route. DEC002 records the accepted single combined
  `DateTime,Bid,Ask,Volume` CSV master (manual SQX download) as the EXP002
  dataset, with the original two-file pre-registration preserved and the
  residual unknowns (naive time zone, single `Volume`, gap structure) carried as
  explicit caveats. Daily bars and the backtest are now unblocked.
- RESOLVED (2026-10-07): The fixed UTC+02 daily bars were built from the accepted
  master (2,260 bars, 2018-01-02→2026-10-02, SHA-256 `57c5b63e…da1f5b`) and the
  frozen baseline SMA200 long-only backtest was run over
  `2020-09-28`–`2026-09-28` without tuning. Result: +9.91% total / +1.59% CAGR /
  -25.92% max drawdown versus buy-and-hold +121.02% / +14.14% / -26.60%.
- RESOLVED (2026-10-07): Historical commission and financing/swap inventory is
  complete — no reliable records exist, so the result is net of quoted spread
  only, disclosed explicitly; it MUST NOT be called fully net of costs.
- OPEN (carried caveat, not a blocker): The naive `DateTime` time zone and the
  meaning of the single `Volume` column remain unverified and are disclosed in
  the EXP002 derived evidence.

## Last Session

[S007 — EXP002 Frozen Baseline: Result Interpretation and Gold Question Stance](../research/sessions/S007-exp002-baseline-interpretation.md)

Work (2026-10-09): interpreted the recorded EXP002 frozen baseline SMA200
long-only result and updated Q003's stance. The baseline returned **+9.91% total
/ +1.59% CAGR** net of quoted spread only (-25.92% max drawdown) versus
buy-and-hold **+121.02% / +14.14% CAGR** (-26.60% max drawdown) over
`2020-09-28`–`2026-09-28`. Recorded as a **weak/negative result** that does not
establish a profitable edge; the long-run gold premise stays user-reported and
unverified; no hypothesis was created and the locked rules were not tuned. Q003
remains `draft`; its related-but-independent questions remain open. Registry
versions synchronized — `Q003` → v3.8, `artifact-registry.json` → 1.19.3
(2026-10-09).

Work (2026-10-09): recorded DEC003, parking the gold question (Q003) after the
weak/negative EXP002 baseline. Q003 is retained as `draft` with evidence
preserved (no lifecycle transition); added to the Parking Lot; no hypothesis
created and no rules tuned. Registry versions synchronized — `Q003` → v3.9,
`artifact-registry.json` → 1.19.4 (2026-10-09).

Prior work (2026-10-07, no session artifact; no rule, methodology, or belief
changed — G001): built the fixed UTC+02 daily bars from the accepted EXP002
master (`tools/build_daily_bars.py` → `evidence/derived/daily-bars-utc02.csv`,
2,260 bars, SHA-256 `57c5b63e…da1f5b`) and ran the frozen baseline SMA200
long-only backtest (`tools/backtest_sma200.py`) over `2020-09-28`–`2026-09-28`
without tuning. Historical commission and financing/swap inventory completed —
no reliable records exist, so the result is net of quoted spread only and MUST
NOT be described as fully net of costs.

## EXIT CHECK

- [x] What did I actually do? Fully verified the received complete
  `XAUUSD-TICK-full.csv` master (32,121,180,517 bytes, SHA-256 `4921484a…ad17d4`,
  732,112,910 rows, coverage 2003-05-05–2026-10-02) with an independent
  streaming pass, recorded it in EXP002 raw `README.md`/`provenance.md` with
  verification tooling and derived evidence, and synchronized the stale
  registry versions (commit `5892610`).
- [x] What did I learn? The full master is structurally sound: 0 malformed rows,
  0 bad timestamps, 0 bad numerics, 0 crossed quotes, and 0 ordering violations
  across 732M rows, and its coverage spans the frozen holdout. The delivered
  format/route still differ from the pre-registration and remain an explicit,
  recorded deviation rather than a silent acceptance.
- [x] What changed? EXP002 raw evidence (`README.md`, `provenance.md`), new
  independent tooling (`tools/verify_full.py`, `tools/check_status.py`) and
  derived evidence (status/report/log); registry versions `Q003` → v3.6,
  `SRC006` → v2.2, `artifact-registry.json` → 1.19.1. No belief, decision,
  methodology, or governance rule changed.
- [x] What is the exact next action? Build fixed UTC+02 daily bars from the
  accepted master and run the frozen baseline SMA200 long-only backtest over
  `2020-09-28`–`2026-09-28` without examining strategy returns before the freeze,
  and inventory historical commissions and financing/swap charges (done
  2026-10-07; recorded in EXP002 `evidence/derived/README.md`).
- [x] What is the exact next action? Interpret the frozen baseline result and
  update the gold question/hypothesis stance (done 2026-10-09; recorded in
  S007 and Q003 v3.8).
- [x] What is the exact next action? Decide the next research step after S007:
  address a related-but-independent question in Q003 (long-run trend; robust
  trend/exit definitions; acceptable risk/drawdown; benchmark gap), refine or
  re-scope the gold question with a new frozen design, or park the question. Do
  not tune the frozen rules against the already-examined evaluation period.
  (Done 2026-10-09: option (c) park; recorded in DEC003.)
- [ ] What is the exact next action? Select and register a new single research
  question via the manual AC001 workflow with explicit input provenance — now
  that Q003 is parked and no experiment is open. Do not re-tune the parked
  rules or carry over its assumptions.
