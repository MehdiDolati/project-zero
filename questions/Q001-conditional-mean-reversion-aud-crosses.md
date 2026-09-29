---
id: Q001
type: question
title: Conditional Mean Reversion in AUDCAD, AUDNZD, and NZDCAD
status: draft
version: 1.0

owner: Project Zero

created: 2026-09-27
last-reviewed: 2026-09-27

created-by-type: human + agent
created-by: |
  Primary: Codex (OpenAI)
  Source input and direction: Mehdi
created-by-version: not available
production-tools: ChatGPT, Codex desktop, apply_patch; versions not available
created-at: 2026-09-27T23:24:38+03:30
---

# Purpose

Preserve and structure a reported observation about possible mean-reverting
behavior in three AUD, CAD, and NZD currency crosses so that it can be
investigated without treating it as established evidence or a trading edge.

---

# Context

The researcher reported prior strategy tests using Bollinger Bands and a
Kaufman Efficiency Ratio regime filter. The reported results raised three
distinct concerns: whether conditional mean reversion exists, what could
explain it, and whether a robust strategy can exploit it without overfitting.

This artifact is the first manual use of the Question / Observation template.

---

# Content

## Raw Input

> من قبلا یک بررسی روی سه جفت ارز انجام دادم
> AUDCAD
> AUDNZD
> NZDCAD
> در تایمهای مختلف و با ستینگهای مختلف بولینجر بند به سوددهی رسیدم. البته از رژیم فیلتر kaufman efficienncy ratio هم استفاده کردم.
> بعد نگران این بودم که شاید تو بک تست ستینگهای مختلف دچار اورفیت شده باشم و ایده را رها کردم. مدلها تو سال 2023 تولید شده بودند. اخیرا که چک کردم این مدلها هنوز تا 2026 داشتند کار می کردند.
> به نظرت می تونیم استراتژی های بازگشت به میانگین برای این جفت ارزها بسازیم؟ بدون اینکه دچار اورفیت بشیم و از اون مهم تر یک دلیل منطقی و فاندامنتال پشت ایده مون وجود داشته باشه؟

## Core Observation / Question

AUDCAD, AUDNZD, and NZDCAD may exhibit conditional mean-reverting behavior.
The reported strategy results are promising, but it is unknown whether they
reflect a persistent market behavior or selection and parameter overfitting.

## Context

The initial strategy exploration used Bollinger Bands across multiple
timeframes and settings, with a Kaufman Efficiency Ratio regime filter. The
models were reportedly created in 2023 and rechecked through 2026.

## Existing Evidence

- The researcher reports profitable historical tests across multiple
  timeframes and Bollinger Band settings on the three currency crosses.
- The researcher reports that models created in 2023 still performed when
  rechecked through 2026.

## Evidence Status / Provenance

All items under Existing Evidence are user-reported and unverified. The data
source, strategy specifications, parameter-search space, code or platform
files, transaction-cost assumptions, and original result records have not yet
been preserved as Project Zero artifacts. No registered Evidence artifact
exists for these claims.

## Assumptions / Interpretations

- The reported profitability may reflect conditional mean reversion rather
  than a favorable historical sample or selection bias.
- Performance observed through 2026 may indicate persistence rather than luck,
  leakage, or unrecorded changes to the model or data.
- Economic relationships among Australia, Canada, and New Zealand may provide
  a plausible explanation for the behavior.
- A Bollinger Band and Kaufman Efficiency Ratio implementation may be capable
  of exploiting the behavior after realistic trading costs.

## Unknowns

- The precise entry, exit, sizing, and regime-filter rules.
- The complete parameter-search space and number of tested variants.
- Data provider, price convention, quality controls, and exact in-sample and
  out-of-sample periods.
- Spread, slippage, financing, execution, and liquidity assumptions.
- The statistical definition and regime conditions of mean reversion.
- Whether any observed behavior is stable across timeframes, market regimes,
  and the three individual pairs.
- The proposed economic mechanism and its observable predictions.

## Primary Research Question

For each of AUDCAD, AUDNZD, and NZDCAD, does a pre-specified, cost-aware,
out-of-sample research protocol find conditional mean-reverting behavior that
is stable enough to justify formulating a testable hypothesis?

## Related but Independent Questions

1. Which economic or market-structure mechanisms, if any, plausibly explain
   the identified behavior and predict the regimes in which it should appear?
2. Can a Bollinger Band and Kaufman Efficiency Ratio strategy exploit any
   identified behavior robustly after controls for multiple testing,
   overfitting, and realistic trading costs?

## Scope

- Instruments: AUDCAD, AUDNZD, and NZDCAD.
- Initial observation: models reportedly created in 2023 and rechecked through
  2026; the exact periods remain to be established.
- Focus: empirical behavior and research framing, not a trading recommendation
  or a claim of profitability.
- Excludes: a conclusion about economic causality or strategy viability until
  the related independent questions are investigated.

## Open Clarifications

1. What were the exact rules, parameter ranges, and number of variants tested?
2. Which data source, bid/ask convention, timeframes, and date ranges were
   used?
3. How were in-sample, validation, and out-of-sample periods separated?
4. Which costs and execution assumptions were included?
5. What result records, source files, or platform projects can be preserved?
6. What observable economic mechanism is currently suspected?
7. What objective threshold would justify moving from this question to a
   hypothesis?

---

# Rationale

The reported results are useful starting information, but neither an observed
backtest nor a later recheck establishes a persistent trading edge. Separating
the empirical question from the mechanism and strategy questions prevents a
single favorable result from being treated as proof of all three.

---

# Relationships

- depends-on: governance/templates/question-observation.md (ART-QUESTION-OBSERVATION)
- derives-from: research/003-research-methodology.md (research-003)
- related-to: research/001-problem-definition.md (research-001)
- related-to: research/002-edge.md (research-002)

---

# References

> None.

---

# Representations

- Markdown

---

# Constraints

- This artifact MUST preserve the original researcher input.
- User-reported results MUST NOT be treated as verified Project Zero evidence.
- The artifact MUST NOT claim that mean reversion, an economic mechanism, or a
  profitable strategy has been established.
- Any later hypothesis MUST preserve the distinction between the primary and
  related independent questions.

---

# Review

Review this artifact after the open clarifications are answered and before a
Draft → Review transition. Any empirical result produced afterward must be
preserved as Evidence originating from a reproducible experiment.

---

# Revision History

| Version | Date | Summary |
| ------- | ---- | ------- |
| 1.0 | 2026-09-27 | First manual Question / Observation workflow result. |
