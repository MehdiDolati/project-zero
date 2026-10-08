---
id: Q003
type: question
title: Long-Only Trend Following in Gold
status: draft
version: 3.8

owner: Project Zero

created: 2026-09-28
last-reviewed: 2026-10-09

created-by-type: human + agent
created-by: |
  Primary: Mehdi
  Agent-assisted by: AI assistant (Copilot SDK in VS Code)
created-by-version: not available
production-tools: VS Code, AI assistant (Copilot SDK); versions not available
created-at: 2026-09-28T15:35:35+03:30
---

# Purpose

Structure the question of whether a long-only trend-following strategy on gold
can earn positive net returns over a six-year evaluation horizon, with each
position held no longer than one year, without treating the long-run price
premise as verified evidence.

---

# Context

The researcher asks whether a buy-only trend-following strategy can profit
from a perceived long-term upward tendency in gold. The maximum holding period
has been set at one year per position by the researcher.

The selected research instrument is spot gold quoted in US dollars
(XAU/USD), per the researcher's clarification on 2026-09-28.

The researcher selected a six-year historical backtest for assessing
profitability and confirmed inclusive dates of `2020-09-28` through
`2026-09-28`. Whether this period is genuinely out of sample depends on
freezing the strategy specification before inspecting its results.

The researcher selected daily observations for this backtest.

The researcher subsequently confirmed that each position must be closed no
later than one year after entry; this is now a fixed design constraint.

The researcher selected Dukascopy's public historical export. On 2026-09-29,
the researcher provided small Bid and Ask excerpts downloaded separately
with the site's `Tick` option. The observed columns are a time-zone label
(`Europe/Amsterdam`), `Open`, `High`, `Low`, `Close`, and `Volume`; the
researcher reports matching timestamps between the separate exports and now
confirms that each row represents one tick, with its timestamp marking when
that tick was recorded. The researcher corrected the previously shared Ask
excerpt: in the corrected sample, Open, High, Low, and Close are equal within
each row, consistent with one price per tick. Several ticks share the same
second-level timestamp. This corrected example supports, but does not
independently verify, the reported row and timestamp semantics. The full files
have not been provided to Project Zero.

On 2026-09-29, the researcher approved and froze the baseline strategy rules
below before examining any backtest returns. The researcher reports that no
SMA200 results from the evaluation period were viewed or used before the rules
were frozen; the holdout designation depends on this report and later data
validation.
The researcher confirmed the inclusive six-year evaluation window
`2020-09-28` through `2026-09-28` on 2026-09-29, using the reported latest
file date. The date boundaries and baseline rules were fixed before examining
strategy returns.

The public export dialog observed 2026-09-28 offered separate Bid/Ask choices
and period options from Tick through Hour, although the publisher FAQ describes
timeframes up to monthly. The researcher reports that the Tick-selected
Bid/Ask exports cover `5/5/2003` through `28/9/2026`. The supplied excerpts
show OHLCV rows rather than a simple price-per-tick layout, so the meaning of
the `Tick` selection for these records remains unresolved. Project Zero has
not received the full files.

This is the second valid manual application of AC001 to a user-provided idea.
Q002 and S004 were previously created with assistant-invented input and have
been explicitly corrected; they are not evidence of a prior user idea or a
valid AC001 test.

On 2026-09-30 and 2026-10-02, the researcher placed raw datasets in
`experiments/EXP002-gold-trend-following/evidence/raw/`. The delivered master
(`XAUUSD-TICK-full.csv`, received 2026-10-02) is a **single combined CSV** with
columns `DateTime,Bid,Ask,Volume` — both quote sides on one row, a single
`Volume` column, and **no OHLC columns** — obtained by a **manual SQX download**
rather than the Dukascopy public-site widget named below. Its observed coverage
is `2003-05-05`–`2026-10-02`, which spans the frozen `2020-09-28`–`2026-09-28`
holdout, and its structure was verified by a full streaming pass with no
strategy returns computed. The earlier delivered file (`XAUUSD-TICK.csv`,
received 2026-09-30) covered only `2003-05-05`–`2005-12-30` and is retained as
an immutable partial slice. The **coverage** deviation is therefore resolved,
but the **format** (combined Bid/Ask, single `Volume`, no OHLC, vs two
Tick-selected OHLCV exports) and **route** (manual SQX download vs the
public-site widget) deviations from the pre-registration remain open. Per
RG009, they are recorded explicitly and are not treated as silently accepted;
the frozen daily-bar construction below cannot be applied as written to a
combined Bid/Ask file without an amended registration. See
`evidence/raw/provenance.md` and `evidence/raw/README.md` for the full record.

On 2026-10-06, the researcher resolved both deviations by **accepting an
amended registration**. Decision
[DEC002](../../decisions/DEC002-accept-amended-exp002-registration.md) records
the delivered single combined `DateTime,Bid,Ask,Volume` CSV master
(`XAUUSD-TICK-full.csv`, manual SQX route) as the EXP002 dataset, in place of
the pre-registered two-file Dukascopy public-site Tick OHLCV exports — the
original pre-registration is preserved, not erased. The frozen fixed-UTC+02
daily aggregation is applied per side directly to the tick `Bid`/`Ask` fields
(first as open, maximum as high, minimum as low, last as close). The locked
baseline rules are unchanged. The naive `DateTime` time zone, the meaning of the
single `Volume` column, and the internal gap/empty-day structure remain
unverified and MUST be disclosed in any derived evidence.

---

# Evaluation Outcome (EXP002 Frozen Baseline)

The locked baseline was executed as
[EXP002](../experiments/EXP002-gold-trend-following/) against the DEC002
amended master, before any tuning. Over the fixed inclusive window
`2020-09-28`–`2026-09-28` (1,549 daily bars) the strategy returned
**+9.91% total / +1.59% CAGR** with a **-25.92%** maximum drawdown, versus
buy-and-hold **+121.02% / +14.14% CAGR** with a **-26.60%** maximum drawdown.
Activity: 32 trades; invested 45.19% of the time; 31 signal exits, 1 one-year
time stop, 0 window-end exits.

The result is **net of quoted spread only** (Ask entries / Bid exits).
Reliable commission and financing/swap records were unavailable, so those
costs are excluded and the result MUST NOT be described as fully net of costs.

**Stance.** For the frozen baseline the primary success criterion is, at best,
marginally and fragilely met: the +9.91% spread-only margin would plausibly be
erased by unmodelled commissions and any overnight financing, and the strategy
was dwarfed by buy-and-hold. The outcome is recorded as a **weak/negative
result**; it does **not** establish a profitable edge. The long-run gold price
premise remains user-reported and unverified, and the observed buy-and-hold
rise over this single window is not promoted to a project claim. The locked
rules were not tuned against the evaluation period. See
[S007](../research/sessions/S007-exp002-baseline-interpretation.md) and the
[derived evidence README](../experiments/EXP002-gold-trend-following/evidence/derived/README.md)
for the full record. No hypothesis was created.

---

# Content

## Raw Input

> طلا در بلند مدت همیشه صعودی بوده. آیا می تونیم یک استراتژی
> Buy only
> به روش trend following روی طلا داشته باشیم که در طولانی مدت سودده باشه؟ البته این طولانی مدت باید کاملا تعریف شده باشه مثلا بگیم حداکثر 1 سال بعد از باز کردن پوزیشن باید ببندیمش

## Core Observation / Question

The researcher believes gold has always risen over the long term and asks
whether a profitable long-only trend-following strategy can be defined for
gold, with a one-year maximum holding period per position. Neither the premise
nor the strategy's profitability has been verified in Project Zero.

## Context

The idea specifies a long-only (buy-only) trend-following approach and a
one-year maximum holding duration per position. Spot gold quoted in US dollars
(XAU/USD) has been selected. Dukascopy Bank is the intended data provider, but
the export file, account-feed match, and availability of historical charges
remain unverified. The SMA200 signal and baseline execution rules are specified
below.

## Existing Evidence

- The researcher asserts that gold has always risen over the long term.

## Evidence Status / Provenance

The long-run upward tendency is a user-reported premise, not verified
Project Zero evidence. No supporting dataset, time period, or prior analysis
has been provided or registered.

## Assumptions / Interpretations

- "Always risen over the long term" may assume a particular instrument,
  currency, starting point, and definition of the long term.
- A long-only strategy might benefit from an upward trend, but that does not
  establish that a trend-following rule can be profitable within the selected
  one-year maximum holding period.
- The maximum holding period for each position is one year, per the
  researcher's clarification.
- The primary evaluation is a six-year historical backtest from
  `2020-09-28` through `2026-09-28`, inclusive, as confirmed by the
  researcher. Calling it out of sample requires the strategy specification
  to be frozen before inspecting that period's results.
- Daily observations have been selected for the evaluation.
- Historical XAU/USD data from Dukascopy's public export has been selected.
  The researcher reports separate Tick-selected Bid and Ask OHLCV downloads;
  full files and the meaning of one row remain unverified.
- The public export dialog showed separate Bid/Ask choices and no visible
  Daily option. The researcher shared small Tick-selected Bid/Ask OHLCV
  excerpts with displayed coverage `5/5/2003` through `28/9/2026`; the full
  files have not been provided to Project Zero.

## Unknowns

- What aggregation unit does the public export's `Tick` setting produce, and
  how should its timestamp and OHLCV rows be interpreted?
- Can the full Bid/Ask exports, timestamps, coverage, ordering, and missing
  records be verified?
- What start and end dates or horizon support the claim about gold's
  long-term direction?
- Which performance measures should accompany the primary net-return success
  criterion, such as volatility or drawdown?
- Which historical commission and financing/swap records are available for
  the evaluation period, and where are there gaps?
- Can the reported tick data and historical cost inputs be validated before
  the backtest is executed?

## Locked Baseline Strategy

The researcher approved this exact baseline on 2026-09-29, before examining
its evaluation-period returns. Do not tune these rules against the evaluation
results.

- Signal: simple moving average (SMA) of the latest 200 completed daily Bid
  Close prices, including the current signal bar. Use pre-evaluation daily
  bars as warm-up data so the first in-period signal has a full 200-bar
  history. Use the latest 200 available generated daily bars; do not fill
  missing dates with synthetic bars or forward-filled prices.
- Daily-bar construction: interpret timestamps using the export's
  `Europe/Amsterdam` context and explicit offsets where present, convert each
  instant to fixed UTC+02, and bucket into `[00:00, 00:00 next day)`. For Bid
  and Ask independently, aggregate first row Open, maximum High, minimum
  Low, and last row Close; the corrected sample has equal OHLC values per
  tick. Preserve source row order for ticks sharing a timestamp. Omit days
  with no records and do not forward-fill. Full-file conventions and
  alignment remain unverified.
- Entry: while flat, a daily Bid Close above the SMA200 triggers a long entry
  at the next daily bar's Open Ask. Hold at most one position; do not pyramid
  or short.
- Signal exit: a daily Bid Close at or below the SMA200 triggers an exit at
  the next daily bar's Open Bid.
- Maximum holding time: one calendar year from the entry timestamp. If no
  signal exit occurs first, close at the Bid Close of the last available
  daily bar ending on or before the one-year anniversary.
- Re-entry after the time stop: remain flat until a daily Bid Close is at or
  below SMA200 and a subsequent daily Bid Close is above SMA200; enter at the
  next daily Open Ask after that renewed above-SMA signal.
- Exposure: allocate 100% of current equity at 1x exposure while invested;
  compound gains and losses. Cash earns zero return while flat. This is a
  research model, not account-specific lot sizing.
- Costs: Ask entries and Bid exits capture the quoted spread. Include
  historical commissions and financing/swap charges where reliable records
  are available. Identify missing costs explicitly; do not describe results
  as fully net of costs when material costs are unavailable.
- Evaluation window: `2020-09-28` through `2026-09-28`, inclusive. Close any
  remaining position at the final evaluation bar's Bid Close.
- Benchmark: buy-and-hold with the same starting capital and 1x exposure,
  entering at the first evaluation bar's Open Ask and liquidating at the
  final evaluation bar's Bid Close, with the same available cost treatment.

## Primary Research Question

For spot gold quoted in US dollars (XAU/USD), can a pre-specified long-only
trend-following strategy with each position held no longer than one year
achieve positive net returns after costs over a six-year historical period,
with that period reserved as out of sample after the rules are frozen?

## Related but Independent Questions

1. Has the selected gold instrument shown a persistent long-run upward trend
   over a clearly stated historical period, after accounting for currency and
   inflation where relevant?
2. Which trend definition and exit rules, if any, are sufficiently robust to
   test without selecting them based on the same evaluation data?
3. What risk and drawdown profile would be acceptable even if the strategy
   achieves positive net returns?
4. How does the strategy compare with buy-and-hold after accounting for risk,
    transaction costs, and other instrument-specific expenses?

## Scope

- Instrument: spot gold (XAU/USD).
- Market/currency: US-dollar quote.
- Desired data frequency: daily, generated from the public site's
  Tick-selected Bid and Ask OHLCV exports.
- Intended provider: Dukascopy public historical export. The researcher
  reports separate Bid and Ask downloads with matching timestamps and
  displayed coverage `5/5/2003`–`28/9/2026`. The shared excerpt labels time as
  `Europe/Amsterdam`; the researcher says each row represents one tick and
  the corrected Ask example has equal OHLC values within each row. This is
  not independently verified against the full files.
- Daily bars: generated using fixed UTC+02 calendar days and Bid/Ask OHLC
  aggregation specified in the Locked Baseline Strategy section.
- Evaluation: six-year historical backtest from `2020-09-28` through
  `2026-09-28`, inclusive, confirmed by the researcher based on the latest
  date reported for the Dukascopy export. These dates are fixed before examining
  results. The researcher reports that no SMA200 returns from this period
  were reviewed before the rules were frozen; designate it as the holdout
  subject to this report and data validation.
- Strategy direction: long-only, with no short positions.
- Strategy family: locked daily SMA200 long-only baseline, as specified above.
- Holding constraint: close each position no later than one year after entry.
- Focus: formulate a testable research question, not recommend or authorize
  trading.
- Excludes: any claim that gold always rises, that trend following is
  profitable, or that a particular strategy is suitable for deployment.

## Open Clarifications

1. Do the full exports consistently represent one tick per row with equal
   OHLC values, and can their timestamp precision, ordering, timezone, Bid/Ask
   alignment, coverage, and missing records be verified?
2. What does the `Volume` field represent, and is it relevant to the test?
3. What minimum return and risk criteria, beyond positive net returns after
   costs, should be reported?
4. Which historical commission and financing/swap data can be retrieved for
   the full evaluation period?
5. What objective evidence threshold would justify formulating a hypothesis?

---

# Rationale

The claim about gold's long-term direction is separated from the strategy
question. The one-year holding limit was initially offered as an example and
was made a fixed design constraint only after the researcher confirmed it.
The researcher confirmed inclusive evaluation dates of `2020-09-28` through
`2026-09-28`, provided small OHLCV excerpts from separate Bid and Ask exports,
and approved fixed-UTC+02 daily aggregation and a single SMA200 long-only
baseline before examining returns. The researcher reports that each row is one tick and its timestamp marks when
that tick was recorded. After correcting the previously shared Ask excerpt,
the sample has equal OHLC values per row and repeated second-level timestamps,
consistent with this report. Full-file conventions and alignment are not
independently verified. The researcher reports that no SMA200 returns for the
evaluation period were examined before the rules were frozen; the period is
designated as a holdout subject to that report and subsequent data validation.

---

# Relationships

- depends-on: governance/templates/question-observation.md (ART-QUESTION-OBSERVATION)
- derives-from: research/003-research-methodology.md (research-003)
- related-to: research/001-problem-definition.md (research-001)
- related-to: research/002-edge.md (research-002)
- related-to: governance/agent-contracts/AC001-question-formulation.md (AC001)
- cites: sources/SRC006-dukascopy-historical-data-export.md (SRC006)
- resolved-by: decisions/DEC002-accept-amended-exp002-registration.md (DEC002)

---

# References

> None.

---

# Representations

- Markdown

---

# Constraints

- This artifact MUST preserve the original researcher input.
- The long-run gold claim MUST remain user-reported unless supported by
  traceable evidence.
- The artifact MUST NOT claim that gold always rises, that trend following is
  profitable, or that any trading edge has been established.
- Each position MUST be closed no later than one year after entry, as confirmed
  by the researcher after the initial example was clarified.
- Any later hypothesis MUST specify the instrument, horizon, benchmark, costs,
  and measurable success criteria.

---

# Review

Review this artifact after the open clarifications are answered and before a
Draft → Review transition. Any empirical result produced afterward must be
preserved as Evidence from a reproducible experiment.

---

# Revision History

| Version | Date | Summary |
| ------- | ---- | ------- |
| 1.0 | 2026-09-28 | Second valid manual use of AC001 on the researcher's gold trend-following idea. |
| 1.1 | 2026-09-28 | Set the instrument to spot gold quoted in US dollars (XAU/USD), per researcher clarification. |
| 1.2 | 2026-09-28 | Recorded that one year was only an example; separated net profitability from benchmark outperformance. |
| 1.3 | 2026-09-28 | Set positive net returns after costs as the primary success criterion; compare with buy-and-hold separately. |
| 1.4 | 2026-09-28 | Set the out-of-sample evaluation horizon to six years, per researcher clarification. |
| 1.5 | 2026-09-28 | Set the maximum holding period to one year per position, per researcher clarification. |
| 1.6 | 2026-09-28 | Set the evaluation approach to a six-year historical out-of-sample backtest; exact dates remain open. |
| 1.7 | 2026-09-28 | Defer exact dates until data frequency and source are selected, while requiring dates to be frozen before results are examined. |
| 1.8 | 2026-09-28 | Clarified how the six-year historical evaluation dates will be set, before results are examined. |
| 1.9 | 2026-09-28 | Selected daily observations for the six-year historical backtest. |
| 2.0 | 2026-09-28 | Recorded daily frequency, confirmed one-year maximum per position, and the six-year historical evaluation process with dates frozen before results. |
| 2.1 | 2026-09-28 | Selected historical daily bid/ask data from the intended trading broker/platform. |
| 2.2 | 2026-09-28 | Named Dukascopy Bank as the intended provider, pending verification of the exact feed and history. |
| 2.3 | 2026-09-28 | Clarified that a historical six-year backtest is out of sample only if the strategy rules are frozen before inspecting that period. |
| 2.4 | 2026-09-28 | Recorded the public export widget's unresolved daily-frequency and separate bid/ask availability. |
| 2.5 | 2026-09-28 | Recorded the researcher's initial description of JForex daily XAU/USD history from 2003 with combined Bid/Ask; later clarified as tick data. |
| 2.6 | 2026-09-29 | Recorded the researcher's report of viewing daily Bid/Ask data from `5/5/2003`; latest date and file conventions remain open. |
| 2.7 | 2026-09-29 | Recorded latest file date `28/9/2026` and proposed inclusive six-year boundaries `2020-09-28`–`2026-09-28`, pending confirmation. |
| 2.8 | 2026-09-29 | Fixed the inclusive six-year evaluation window at `2020-09-28`–`2026-09-28`, as confirmed by the researcher; out-of-sample status still depends on freezing strategy rules. |
| 2.9 | 2026-09-29 | Recorded preliminary daily-bar timezone/boundary details; superseded by the tick-data clarification in 3.1. |
| 3.0 | 2026-09-29 | Froze the researcher-approved SMA200 long-only baseline, execution, sizing, cost treatment, and buy-and-hold benchmark before examining evaluation returns. |
| 3.1 | 2026-09-29 | Clarified the source as tick data with timestamp and Bid/Ask per tick; froze fixed-UTC+2 daily OHLC aggregation and missing-day handling. |
| 3.2 | 2026-09-29 | Recorded the researcher's report that no SMA200 results from the evaluation window were reviewed before rule freeze; designated the period as the holdout, subject to data validation. |
| 3.3 | 2026-09-29 | Recorded separate Tick-selected Bid/Ask OHLCV excerpts, matching-timestamp report, Europe/Amsterdam label, unresolved row unit, and approved fixed-UTC+02 daily resampling. |
| 3.4 | 2026-09-29 | Recorded the researcher's confirmation that each row is one tick and its timestamp marks tick time; flagged conflicting intrarow Ask OHLC values and blocked daily-bar construction pending price-field semantics. |
| 3.5 | 2026-09-29 | Recorded the correction that each Ask tick has equal OHLC values and repeated second-level timestamps; reinstated the approved fixed-UTC+02 daily aggregation pending full-file validation. |
| 3.6 | 2026-10-02 | Recorded the delivered raw master `XAUUSD-TICK-full.csv`: a single combined `DateTime,Bid,Ask,Volume` CSV (no OHLC) obtained via manual SQX download, observed coverage `2003-05-05`–`2026-10-02`, structure verified by a full streaming pass with no returns computed. Coverage deviation resolved; format and route deviations from the pre-registered two-file Tick OHLCV public-site exports remain open and require reconciliation before use. |
| 3.7 | 2026-10-06 | Recorded DEC002: the researcher accepted an amended registration for the delivered single combined `DateTime,Bid,Ask,Volume` CSV master (manual SQX route), superseding the pre-registered two-file Tick OHLCV public-site exports; the fixed-UTC+02 daily aggregation is applied per side to the `Bid`/`Ask` tick fields and the locked baseline is unchanged. Residual unknowns (naive time zone, single `Volume`, gap structure) carried as explicit caveats. Format/route deviations resolved; daily bars and the backtest unblocked. |
| 3.8 | 2026-10-09 | Recorded the EXP002 frozen-baseline evaluation outcome and stance: +9.91% total / +1.59% CAGR net of quoted spread only, -25.92% max drawdown, versus buy-and-hold +121.02% / +14.14% CAGR. Recorded as a weak/negative result that does not establish a profitable edge; premises kept unverified, rules not tuned, no hypothesis created. See S007. |
