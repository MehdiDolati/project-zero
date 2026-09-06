---
id: EXP001
type: experiment

title: Manual Replication of a Published Momentum Anomaly

status: draft
version: 1.0

owner: Project Zero

created: 2026-09-06
last-reviewed: 2026-09-06
---

# Purpose

Exercise the full research loop
([research-003](../../research/003-research-methodology.md)) once, manually, end
to end, on a concrete market claim that already exists in published literature.

This experiment has two objects of study, and both matter:

1. **The market claim.** Does a well-documented, simple momentum rule still
   produce a risk-adjusted advantage over buy-and-hold in the period after it
   was published?
2. **The process.** Can the documented methodology actually be executed by a
   solo researcher with free data and no custom software, and what does it cost
   in time and discretionary judgement?

The second object is not decoration. H000 asserts the project should not exist
unless the process itself creates value; the only way to produce evidence about
that is to run the process and record what it cost and what it caught.

---

# Context

No experiment has been executed in this project. The pipeline has been
deliberately unexercised
([DEC001](../../decisions/DEC001-no-software-before-method.md),
[RG001](../../governance/rules/RG001-automation-follows-stability.md)).

A published, widely replicated anomaly was chosen deliberately over an original
idea, per
[RG005](../../governance/rules/RG005-benchmark-before-invention.md): established
practice is studied before new methodology is introduced. Starting with a novel
signal would confound two unknowns — whether the signal has merit and whether
the process works. Starting with a known signal isolates the process.

The claim under test is time-series (absolute) momentum on a broad equity index:
hold the index when its trailing 12-month return is positive, hold cash
otherwise. This is the simplest published form of trend following, documented in
academic and practitioner literature for decades, which makes it a fair
benchmark and a poor candidate for accidental discovery.

---

# Content

## Hypothesis under test

EXP001 tests a narrow, falsifiable sub-claim. It does **not** test
[H001](../../hypotheses/H001-edge-is-emergent.md) as a whole; H001 is a
system-level claim that no single experiment can settle.

**Sub-claim (C1):** A published simple momentum rule retains a risk-adjusted
advantage over buy-and-hold in its post-publication out-of-sample period.

**Relevance to H001:** C1 speaks to H001 prediction 2 (strategy performance
degrades without adaptation). If C1 fails out-of-sample while holding
in-sample, that is consistent with H001. If C1 holds unchanged across decades
without any adaptation, that is mild evidence against H001.

**Relevance to H000:** the process metrics below produce the first evidence
about whether disciplined execution catches anything an unstructured reading of
the literature would have missed.

---

## Instruments and data

| Item | Choice | Reason |
|------|--------|--------|
| Market | US broad equity index, total return | Longest reliable free history |
| Primary series | Monthly closes | Rule operates monthly; avoids intraday data |
| Proxy | S&P 500 total return series (index level, dividends reinvested) | Free, widely available, avoids ETF inception limits |
| Cash proxy | 3-month US Treasury bill, monthly yield | Standard risk-free stand-in |
| Source | Single free public source, recorded with URL, retrieval date, and file hash | Provenance is required evidence |

Data MUST be downloaded once, stored unmodified under `evidence/raw/`, and never
edited. All derived series live in `evidence/derived/` and MUST be regenerable
from raw data by following the procedure below.

---

## Rule specification

Fixed before any data is examined. Parameters are not to be adjusted during
execution; see Assumptions.

- **Signal:** at the last trading day of month *t*, compute the trailing
  12-month total return of the index, R12 = (P_t / P_{t-12}) - 1.
- **Position for month *t+1*:** if R12 > 0, hold the index for the whole of
  month *t+1*; otherwise hold cash at the prevailing T-bill rate.
- **Rebalance:** monthly, at month end, at the close. One decision per month.
- **Costs:** 10 basis points charged on each switch (entry or exit), covering
  commission and slippage. No cost when the position is unchanged.
- **Leverage:** none. **Shorting:** none. **Position sizing:** all-or-nothing.
- **Benchmark:** buy and hold the same index, same cost model, no switches.

## Periods

- **In-sample (IS):** 1950-01 through 2005-12. Represents the era covered by the
  literature that documents the effect.
- **Out-of-sample (OOS):** 2006-01 through the last complete month at execution
  time. Represents the post-publication period.

The IS period is not used to fit anything. It exists to confirm that the rule as
specified reproduces the published-era result at all. If it does not, the
specification or the data is wrong, and that must be resolved before OOS results
are interpreted.

## Metrics

Computed for rule and benchmark, separately for IS and OOS:

- annualized return (geometric),
- annualized volatility (monthly, annualized by sqrt(12)),
- Sharpe ratio using the T-bill series as the risk-free rate,
- maximum drawdown on monthly closes,
- percentage of months invested,
- number of switches, and total cost drag.

Primary comparison metric: **Sharpe ratio difference (rule minus benchmark)**.
Secondary: **maximum drawdown difference**.

## Robustness checks

Run only after the primary result is recorded, and reported whether or not they
change the conclusion:

1. Lookback perturbation: 10, 11, 13, 14 months.
2. Cost perturbation: 0 bps and 30 bps per switch.
3. Signal timing: skip the most recent month (the classic 12-1 form).
4. Sub-period split: OOS first half versus second half.

A result that survives none of these is fragile regardless of its headline
number.

---

## Success criteria (experiment)

The experiment succeeds as research if all of the following hold, independent of
what the market claim turns out to be:

- Raw data is preserved with provenance (source, retrieval date, hash).
- The procedure is written such that an independent party can reproduce the
  numbers from raw data without asking questions.
- All metrics are reported for IS and OOS, for rule and benchmark.
- All robustness checks are executed and reported.
- Every discretionary choice made during execution is logged in
  `evidence/execution-log.md`, including choices that were tempting but rejected.
- A decision is recorded, including if the decision is "inconclusive".

## Failure criteria (experiment)

The experiment fails as research, and the result MUST NOT enter project
knowledge, if any of the following occur:

- Rule parameters are changed after seeing results, without recording the change
  as a separate, clearly labelled exploratory run.
- Raw data is edited in place, or provenance is lost.
- Metrics are reported for OOS only, or for the rule only.
- Robustness checks are skipped or selectively reported.
- The conclusion is stated more strongly than the evidence supports.

## Findings criteria (market claim C1)

Applied to the OOS period:

- **C1 supported:** Sharpe difference > 0 **and** maximum drawdown reduced,
  **and** the sign of the Sharpe difference survives all four robustness checks.
- **C1 weakened:** Sharpe difference <= 0, **or** the sign reverses under any
  robustness check.
- **Inconclusive:** Sharpe difference positive but small (< 0.1) and
  sign-unstable across checks, or OOS sample too short to distinguish from
  noise.

"Inconclusive" is an acceptable and expected outcome. It is not a failure.

## Process metrics (feeds H000)

Recorded during execution in `evidence/execution-log.md`:

- total manual effort in minutes, by phase (data, computation, analysis, write-up),
- count of discretionary choices encountered,
- count of points where the documented methodology prevented a shortcut that
  would otherwise have been taken,
- count of points where governance created work with no discernible research
  value.

The last metric matters as much as the third. If governance produces overhead
and catches nothing, that is evidence for H000 and MUST be recorded plainly.

---

## Procedure

1. Record the intended data source, then retrieve the index total-return monthly
   series and the T-bill monthly series. Store both unmodified in
   `evidence/raw/` alongside a `provenance.md` recording source URL, retrieval
   timestamp, and file hash.
2. In a spreadsheet, build a single monthly table: date, index level, index
   monthly return, T-bill monthly rate.
3. Add the R12 column. Add the position column (1 or 0) applied to the
   *following* month. Verify by hand that no row uses information from its own
   month or later — this is the single most likely source of error.
4. Add the rule return column, applying the cost model on position changes only.
5. Compute all metrics for IS and OOS, rule and benchmark. Save the workbook and
   a CSV export to `evidence/derived/`.
6. Record the primary result in `RESULTS.md` before running robustness checks.
7. Run the four robustness checks; append each to `RESULTS.md`.
8. Write the evaluation: what the evidence supports, what it does not, competing
   explanations, and remaining uncertainty.
9. Record the decision and confidence. Update H001 confidence only if the
   evidence genuinely bears on it; state explicitly if it does not.
10. Record the session and, if a belief changed, the resulting decision artifact.

Step 6 exists specifically to prevent the primary result from being quietly
reframed by whichever robustness check looks most flattering.

---

## Assumptions

Recorded before execution, because they are the most likely reasons a positive
result would be wrong:

- Monthly close data is accurate and survivorship-free at index level.
- Total return series correctly reinvests dividends; a price-only series would
  bias the benchmark downward and flatter the rule.
- 10 bps per switch approximates real transaction costs for a retail
  participant; the true figure varies by era and would have been much higher
  before the 1990s. The IS result is therefore optimistic by construction.
- Taxes are ignored. This is unrealistic for a taxable account and materially
  favours the rule, which realizes gains more often.
- Cash earns the T-bill rate with no friction.
- Backtested results assume the rule would have been followed exactly, which
  ignores decision psychology (research-001, section 3) entirely.

None of these assumptions are being defended. They are recorded so the result
can be discounted correctly.

---

## Explicitly out of scope

- Any custom software. Spreadsheet and manual work only
  ([DEC001](../../decisions/DEC001-no-software-before-method.md)).
- Multiple instruments, asset classes, or parameter searches.
- Any conclusion about H001 as a whole.
- Any capital allocation. This experiment produces evidence, not positions.

---

# Rationale

This experiment exists because the framework has never been run. A governance
model that has not survived contact with a real experiment is an untested
assumption, and the project's own methodology forbids treating untested
assumptions as knowledge.

A published anomaly was chosen so that a negative result is informative rather
than merely disappointing: if a rule this well documented does not survive its
own out-of-sample period under honest cost assumptions, that is a substantive
finding about how much weight published backtests deserve. If it does survive,
the project has a benchmark to beat before any original idea can claim value.

The process metrics are included because H000 cannot be tested any other way.
The project must be able to produce evidence against itself.

---

# Relationships

- depends-on: hypotheses/H001-edge-is-emergent.md (H001)
- derives-from: research/003-research-methodology.md (research-003)
- related-to: hypotheses/H000-project-should-not-exist.md (H000)
- related-to: research/002-edge.md (research-002)
- related-to: decisions/DEC001-no-software-before-method.md (DEC001)
- related-to: governance/rules/RG005-benchmark-before-invention.md (RG005)
- produces: experiments/EXP001/evidence/ (EXP001-evidence) [planned]
- created-in: research/sessions/S002-first-experiment-design.md (S002)

---

# Representations

- Markdown (this design artifact)
- Markdown (`RESULTS.md`, on execution) [planned]
- CSV (raw and derived series under `evidence/`) [planned]
- Spreadsheet (computation workbook under `evidence/derived/`) [planned]

---

# Constraints

- Manual execution only; no custom software (DEC001, RG001).
- Free, publicly available data only.
- Rule specification is frozen before data is examined.
- Evidence is immutable once written
  ([G001](../../governance/G001-research-governance.md)).

---

# Review

This design SHOULD be reviewed:

- before execution begins, to confirm the specification is still frozen and
  complete,
- after execution, against the success and failure criteria,
- if the data source becomes unavailable and a substitute is required, which
  MUST be recorded as a change to this artifact rather than an undocumented
  substitution.

---

# Revision History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | 2026-09-06 | Initial design. Not yet executed. |
