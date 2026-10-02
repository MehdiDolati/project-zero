# Project Zero — Current State

## Current Direction

Continue the manual Question / Observation workflow with clear input
provenance, then resolve the open scope decisions in Q003 before proposing any
hypothesis or experiment.

## Current Objective

Reconcile the delivered EXP002 raw file against its pre-registration. The full
`2003`–`2026` export has now arrived and passed full-range independent
verification, so the coverage blocker is resolved; the remaining objective is a
researcher decision on the open format/route deviations before daily bars are
built.

## NEXT ACTION

Obtain the researcher's decision on the open EXP002 format/route deviations: the
delivered file (`XAUUSD-TICK-full.csv`) is a single combined
`DateTime,Bid,Ask,Volume` CSV with one `Volume` and no OHLC, delivered by a
manual SQX download, whereas the pre-registration specifies two separate
Dukascopy public-site exports with `Tick` selected for Bid and Ask, OHLCV fields,
a `Europe/Amsterdam` time-zone label, and displayed coverage
`5/5/2003`–`28/9/2026`. Decide whether to accept an amended registration for the
delivered format/route or obtain conforming exports. After that decision, build
fixed UTC+02 daily bars (OHLC aggregation, preserving file order for duplicate
timestamps, omitting empty days without forward-filling), run the frozen
baseline SMA200 long-only backtest over `2020-09-28`–`2026-09-28` without
examining strategy returns before the freeze, then inventory historical
commissions and financing/swap charges.

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
- OPEN: The delivered format (single combined Bid/Ask/Volume CSV, no OHLC) and
  route (manual SQX download) differ from the pre-registered Dukascopy
  public-site two-file OHLCV tick exports. This requires a researcher decision
  (accept an amended registration or obtain conforming exports) before daily
  bars or the backtest can be produced.

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
- [ ] What is the exact next action? Obtain the researcher's decision on the
  EXP002 format/route deviations (amend the registration for the delivered
  single `DateTime,Bid,Ask,Volume` CSV via SQX, or obtain conforming Dukascopy
  public-site two-file OHLCV tick exports); then build fixed UTC+02 daily bars
  and run the frozen baseline SMA200 long-only backtest over
  `2020-09-28`–`2026-09-28` without examining strategy returns before the
  freeze, and inventory historical commissions and financing/swap charges.
