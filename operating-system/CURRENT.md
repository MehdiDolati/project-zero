# Project Zero — Current State

## Current Direction

Continue the manual Question / Observation workflow with clear input
provenance, then resolve the open scope decisions in Q003 before proposing any
hypothesis or experiment.

## Current Objective

Build the fixed UTC+02 daily bars from the accepted EXP002 dataset and run the
frozen baseline SMA200 long-only backtest over `2020-09-28`–`2026-09-28`,
without examining strategy returns before the freeze.

## NEXT ACTION

Record the researcher's accepted decision on the open EXP002 format/route
deviations as [DEC002](../decisions/DEC002-accept-amended-exp002-registration.md)
(accept the delivered single combined `DateTime,Bid,Ask,Volume` CSV master
`XAUUSD-TICK-full.csv`, obtained via a manual SQX download, as the amended
EXP002 dataset registration) and reconcile the affected artifacts (`Q003`,
`SRC006`, EXP002 raw `README.md`/`provenance.md`, registries) to it. Then build
fixed UTC+02 daily bars from the accepted master — per side, first `Bid`/`Ask`
as the day's open, maximum as high, minimum as low, last as close, preserving
file order for duplicate timestamps, omitting empty days without
forward-filling — and run the frozen baseline SMA200 long-only backtest over
`2020-09-28`–`2026-09-28` without examining strategy returns before the freeze,
then inventory historical commissions and financing/swap charges.

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
- OPEN (carried caveat, not a blocker): The naive `DateTime` time zone and the
  meaning of the single `Volume` column remain unverified and must be disclosed
  in any derived evidence.

## Last Session

[S006 — Project Principles Elevated to First-Class Artifacts](../research/sessions/S006-project-principles-as-artifacts.md)

The four project requirements (provenance and fitness; raw data immutable and
derived data traceable; architecture is not an implementation plan; AI is part
of the operating model) were added as first-class principle artifacts PR002–PR005
under `principles/`. G001 now references them instead of restating them and was
bumped to version 1.1. All registries (README, artifact-registry.json,
manifest.json) were synchronized.

The earlier 2026-09-29 governance compliance review of Q001–Q003 changed no governance
rule, methodology, or major assumption, so it required no session artifact
(G001). Its outcome is recorded in the EXIT CHECK below and in commit
`1cd7d17`.

Latest work (2026-10-03): received and fully verified the complete
`XAUUSD-TICK-full.csv` master (32,121,180,517 bytes, SHA-256 `4921484a…ad17d4`,
732,112,910 rows, coverage 2003-05-05–2026-10-02) with an independent streaming
pass, recording the result in EXP002 raw `README.md`/`provenance.md` along with
the verification tooling and derived evidence. Synchronized the stale registry
versions (`Q003` → v3.6, `SRC006` → v2.2; `artifact-registry.json` → 1.19.1,
2026-10-03) to match artifact front matter (commit `5892610`). No session
artifact was required: no rule, methodology, or belief changed. The open
format/route deviations remain recorded and undecided.

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
- [ ] What is the exact next action? Reconcile `Q003`, `SRC006`, and the EXP002
  raw `README.md`/`provenance.md` (and registries) to DEC002; then build fixed
  UTC+02 daily bars from the accepted master and run the frozen baseline SMA200
  long-only backtest over `2020-09-28`–`2026-09-28` without examining strategy
  returns before the freeze, and inventory historical commissions and
  financing/swap charges.
