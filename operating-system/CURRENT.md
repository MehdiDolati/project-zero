# Project Zero — Current State

## Current Direction

Continue the manual Question / Observation workflow with clear input
provenance, then resolve the open scope decisions in Q003 before proposing any
hypothesis or experiment.

## Current Objective

Validate the reported one-tick-per-row structure, equal per-row OHLC values,
second-level timestamp duplicates, Bid/Ask alignment, and historical costs
without examining strategy returns.

## NEXT ACTION

Obtain/inspect the full separate Bid and Ask exports; verify one tick per row,
OHLC equality per tick, timestamp precision/order/timezone, coverage, and
alignment, then inventory historical commissions and financing/swap charges.

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

- Full exports must verify tick/OHLC semantics, timestamps, coverage, and
  Bid/Ask alignment before daily bars or the backtest can be produced.

## Last Session

[S005 — Gold Question Formulation Test](../research/sessions/S005-gold-question-formulation-test.md)

The 2026-09-29 governance compliance review of Q001–Q003 changed no governance
rule, methodology, or major assumption, so it required no session artifact
(G001). Its outcome is recorded in the EXIT CHECK below and in commit
`1cd7d17`.

## EXIT CHECK

- [x] What did I actually do? Verified Q001–Q003 against the governance stack
  (G001–G006, RG002–RG009, the Question/Observation template, AC001, and all
  three registries), fixed the findings, and committed them (1cd7d17).
- [x] What did I learn? The three questions are compliant apart from
  mechanical gaps. Origin-side back-links must use `related-to`, because G006
  requires `derives-from` to be expressed from the derived artifact toward
  its origin. G006 registers no inverse or auxiliary types, so existing
  `cited-by` (SRC001–SRC006) and `created-in` lines are unregistered
  vocabulary — a candidate governance evolution, not a blocker.
- [x] What changed? Filled Q001's empty last-reviewed date; deduplicated
  Q002's revision history and added an inline invalidation pointer (Q002
  v1.2, registry synced); gave research-003 v1.1 backward `related-to` links
  to Q001–Q003 and a revision history.
- [ ] What is the exact next action? Obtain/inspect the full exports to
  verify one tick per row, equal per-row OHLC, timestamp precision and
  ordering, time-zone interpretation, Bid/Ask timestamp alignment, and
  historical cost inputs without examining strategy returns.
