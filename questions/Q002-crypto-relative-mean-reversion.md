---
id: Q002
type: question
title: Crypto Relative Mean Reversion after Large Dislocations
status: draft
version: 1.0

owner: Project Zero

created: 2026-09-28
last-reviewed:

created-by-type: human + agent
created-by: |
  Primary: Mehdi
  Agent-assisted by: AI assistant (Copilot SDK in VS Code)
created-by-version: not available
production-tools: VS Code, AI assistant (Copilot SDK); versions not available
created-at: 2026-09-28T14:00:00+03:30
---

# Purpose

Preserve and structure a free-form observation about possible relative mean reversion in major crypto pairs so that it can be investigated without treating it as established evidence or a trading edge.

---

# Context

The researcher described a repeated impression that large dislocations between major crypto assets, especially BTC and ETH, are followed by partial reversion. The idea was reported as a pattern seen over recent market moves, not as a quantified result or a preserved dataset.

This artifact is the second manual use of the Question / Observation template and the second test of AC001.

---

# Content

## Raw Input

> من چند هفته‌ای می‌بینم وقتی BTC از ETH خیلی عقب می‌افتد و بعد از یک رالی شدید ETH دوباره به نسبت BTC برمی‌گردد، شاید در نسبت‌گیری‌های ارزهای دیجیتال هم رفتار بازگشت به میانگین وجود داشته باشد. بعضی وقت‌ها این الگو را در BTC/ETH، SOL/ETH و حتی ETH/BTC دیده‌ام. فکر می‌کنم شاید وقتی نوسان بالا می‌شود، این رفتار بیشتر خودش را نشان می‌دهد. ولی مطمئن نیستم که این فقط نویز است یا واقعاً یک الگوی بازار دارد. شاید این موضوع ربطی به ریسک‌پذیری و liquidity در بازار کریپتو دارد.

## Core Observation / Question

Large relative dislocations among major crypto assets may be followed by partial mean reversion. It is unknown whether this is a persistent market behavior, a regime-specific pattern, or a misleading impression shaped by recent volatility.

## Context

The initial observation is based on anecdotal monitoring of BTC/ETH and related relative pairs across recent volatile periods. The researcher did not provide the exact lookback windows, relative measures, or the number of instances observed.

## Existing Evidence

- The researcher reports repeated observations of BTC/ETH and related pairs re-centering after sharp relative moves.
- The researcher suspects the pattern may intensify during high-volatility periods.
- The researcher suggests the behavior may relate to crypto market microstructure, liquidity, and risk repricing.

## Evidence Status / Provenance

All items under Existing Evidence are user-reported and unverified. No dataset, parameter log, time series, or prior result archive has been preserved as Project Zero evidence. No registered Evidence artifact exists for this idea.

## Assumptions / Interpretations

- The observed pattern may reflect mean reversion in relative prices rather than a random sequence of volatile moves.
- The effect may be stronger in high-volatility or stress regimes than in quiet markets.
- Relative pricing among major crypto assets may have a plausible microstructure explanation involving liquidity and risk sentiment.
- A simple relative-spread rule may be able to exploit the effect, but this is not established.

## Unknowns

- The exact crypto pairs and ratios being observed.
- The timeframes, entry/exit windows, and thresholds used in the informal impression.
- Whether the behavior is specific to BTC/ETH or appears in other relative pairs.
- Whether the apparent effect is present only in high-volatility conditions.
- The data source, quote convention, and exchange selection for the observed pattern.
- Transaction costs, slippage, and market-impact assumptions for any potential strategy.
- Whether the pattern is statistically robust after multiple-testing correction and out-of-sample validation.

## Primary Research Question

For major crypto pairs such as BTC/ETH, does a pre-specified, cost-aware, out-of-sample research protocol find stable relative mean reversion after large dislocations, after controlling for volatility regime and multiple testing?

## Related but Independent Questions

1. What economic or market-structure mechanism, if any, plausibly explains the apparent reversion and under which regimes it should appear?
2. Can any identified relative-spread behavior be exploited robustly after realistic transaction costs and a disciplined out-of-sample test?
3. Is the effect tied to cross-asset risk sentiment, liquidity shocks, or purely statistical noise?

## Scope

- Instruments: major crypto pairs such as BTC/ETH, SOL/ETH, and related ratio-based comparisons.
- Initial observation: recent volatile periods, not yet formally bounded by date or market regime.
- Focus: empirical structure and research framing, not a recommendation to trade.
- Excludes: conclusions about causality, profitability, or mechanism until the related independent questions are investigated.

## Open Clarifications

1. Which exact pairs, ratios, and observation windows were considered?
2. What was the precise definition of a "large dislocation" or reversion event?
3. How many instances were seen, across which periods and exchanges?
4. What data source, exchange, and quote convention were used?
5. What transaction-cost and liquidity assumptions are relevant?
6. What objective threshold would justify moving from this question to a testable hypothesis?

---

# Rationale

The reported pattern is useful as a starting observation, but it is not yet project evidence. The structure keeps the empirical question separate from the mechanism and strategy questions, preventing a vague impression from being mistaken for a valid edge or a causal explanation.

---

# Relationships

- depends-on: governance/templates/question-observation.md (ART-QUESTION-OBSERVATION)
- derives-from: research/003-research-methodology.md (research-003)
- related-to: research/001-problem-definition.md (research-001)
- related-to: research/002-edge.md (research-002)
- related-to: governance/agent-contracts/AC001-question-formulation.md (AC001)

---

# References

> None.

---

# Representations

- Markdown

---

# Constraints

- This artifact MUST preserve the original researcher input.
- User-reported observations MUST NOT be treated as verified Project Zero evidence.
- The artifact MUST NOT imply that mean reversion, a mechanism, or a profitable strategy has been established.
- Any later hypothesis must preserve the distinction between the primary empirical question and the related explanatory and exploitability questions.

---

# Review

Review this artifact after the open clarifications are answered and before a Draft → Review transition. Any empirical result produced afterward must be preserved as Evidence from a reproducible experiment.

---

# Revision History

| Version | Date | Summary |
| ------- | ---- | ------- |
| 1.0 | 2026-09-28 | First manual use of AC001 on a second free-form crypto idea. |
