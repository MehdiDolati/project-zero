---
id: Q003
type: question
title: Long-Only Trend Following in Gold
status: draft
version: 2.8

owner: Project Zero

created: 2026-09-28
last-reviewed: 2026-09-28

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
profitability. Exact start and end dates will be fixed after verifying the
data source, but before results are examined. Whether this period is genuinely
out of sample depends on freezing the strategy specification before inspecting
its results.

The researcher selected daily observations for this backtest.

The researcher subsequently confirmed that each position must be closed no
later than one year after entry; this is now a fixed design constraint.

The researcher selected historical daily bid/ask data from the broker or
platform intended for actual trading and named Dukascopy Bank as the intended
provider. The researcher reports viewing a JForex file containing daily
XAU/USD Bid and Ask data beginning at the displayed date `5/5/2003` and with
latest date `28/9/2026`. The file has not been provided to Project Zero; its
bar conventions and match to the intended trading feed remain unverified.
The researcher confirmed the inclusive six-year evaluation window
`2020-09-28` through `2026-09-28` on 2026-09-29, using the reported latest
file date. This fixes the date boundaries before strategy results are
examined; it does not make the period out of sample unless the strategy rules
are also frozen before those results are inspected.

The public export dialog observed 2026-09-28 offered separate Bid/Ask choices
and period options from Tick through Hour, although the publisher FAQ describes
timeframes up to monthly. The researcher reports viewing a JForex daily
XAU/USD file with Bid and Ask data from `5/5/2003` through `28/9/2026`.
Project Zero has not independently inspected the file, and its bar
conventions remain unverified.

This is the second valid manual application of AC001 to a user-provided idea.
Q002 and S004 were previously created with assistant-invented input and have
been explicitly corrected; they are not evidence of a prior user idea or a
valid AC001 test.

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
its export fields, coverage, and the exact execution conventions remain
unverified; the trend rule is not yet defined.

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
- Historical daily bid/ask data from the intended trading broker/platform has
  been selected as the preferred source type; Dukascopy Bank was named as the
  intended provider, pending verification of the exact feed and history.
- The public export dialog showed separate Bid/Ask choices and no visible
  Daily option. The researcher reports viewing a JForex file with daily Bid
  and Ask data from `5/5/2003` through `28/9/2026`; the file has not been
  provided to Project Zero.

## Unknowns

- What timezone, daily bar conventions, and per-side fields does the JForex
  export use?
- What start and end dates or horizon support the claim about gold's
  long-term direction?
- How should a trend-following signal, entry, exit, and position sizing be
  defined?
- Which performance measures should accompany the primary net-return success
  criterion, such as volatility or drawdown?
- What transaction costs, financing, roll, and execution assumptions apply
  to the chosen instrument?
- Which buy-and-hold benchmark and comparison metrics should be reported?

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
- Desired data frequency: daily; the researcher reports viewing daily
  XAU/USD Bid and Ask data from `5/5/2003` in a JForex file.
- Intended provider: Dukascopy Bank; exact feed, history, and price conventions
  remain to be verified. The researcher reports that JForex provides Bid and
  Ask together; the public dialog showed Tick/Second/Minute/Hour and separate
  Bid/Ask selections.
- Evaluation: six-year historical backtest from `2020-09-28` through
  `2026-09-28`, inclusive, confirmed by the researcher based on the latest
  date reported in the JForex file. These dates are fixed before examining
  results. The period only qualifies as out of sample if the strategy rules
  are frozen before inspecting its results.
- Strategy direction: long-only, with no short positions.
- Strategy family: trend following; exact rules are not yet defined.
- Holding constraint: close each position no later than one year after entry.
- Focus: formulate a testable research question, not recommend or authorize
  trading.
- Excludes: any claim that gold always rises, that trend following is
  profitable, or that a particular strategy is suitable for deployment.

## Open Clarifications

1. What entry and exit convention will enforce the one-year per-position
   maximum?
2. What timezone, daily bar conventions, and per-side fields does the JForex
   export use? The researcher-viewed file has not been provided to Project
   Zero for independent inspection.
3. Can the selected six-year period be kept genuinely out of sample after the
   strategy rules are fixed, or is it only a historical exploratory test?
4. What minimum return and risk criteria, beyond positive net returns after
   costs, should be reported?
5. What buy-and-hold benchmark and comparison period should be used?
6. What realistic trading costs and other instrument-specific expenses should
   apply?
7. What objective evidence threshold would justify formulating a hypothesis?

---

# Rationale

The claim about gold's long-term direction is separated from the strategy
question. The one-year holding limit was initially offered as an example and
was made a fixed design constraint only after the researcher confirmed it.
The researcher confirmed inclusive evaluation dates of `2020-09-28` through
`2026-09-28` before examining results. The JForex file's timezone and daily
bar conventions remain unverified. This period qualifies as out of sample
only if the strategy rules are frozen before its results are inspected.

---

# Relationships

- depends-on: governance/templates/question-observation.md (ART-QUESTION-OBSERVATION)
- derives-from: research/003-research-methodology.md (research-003)
- related-to: research/001-problem-definition.md (research-001)
- related-to: research/002-edge.md (research-002)
- related-to: governance/agent-contracts/AC001-question-formulation.md (AC001)
- cites: sources/SRC006-dukascopy-historical-data-export.md (SRC006)

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
| 2.5 | 2026-09-28 | Recorded researcher-reported JForex daily XAU/USD history from 2003 with combined Bid/Ask; sample export remains unverified. |
| 2.6 | 2026-09-29 | Recorded the researcher's report of viewing daily Bid/Ask data from `5/5/2003`; latest date and file conventions remain open. |
| 2.7 | 2026-09-29 | Recorded latest file date `28/9/2026` and proposed inclusive six-year boundaries `2020-09-28`–`2026-09-28`, pending confirmation. |
| 2.8 | 2026-09-29 | Fixed the inclusive six-year evaluation window at `2020-09-28`–`2026-09-28`, as confirmed by the researcher; out-of-sample status still depends on freezing strategy rules. |
