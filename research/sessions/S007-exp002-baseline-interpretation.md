---
id: S007
type: session
title: EXP002 Frozen Baseline — Result Interpretation and Gold Question Stance
status: completed
version: 1.0

owner: Project Zero

created: 2026-10-09
last-reviewed: 2026-10-09

created-by-type: human + agent
created-by: |
  Primary: Mehdi
  Agent-assisted by: AI assistant (Cline)
created-by-version: not available
production-tools: VS Code, AI assistant (Cline); versions not available
created-at: 2026-10-09T00:50:00+03:30
---

# Session Objective

Interpret the recorded EXP002 frozen baseline SMA200 long-only result and
update the stance of the gold trend-following question
([Q003](../../questions/Q003-long-only-gold-trend-following.md)) accordingly —
without tuning the frozen rules against the evaluation period and without
describing the result as fully net of costs.

---

# What Was Done

- Read the recorded EXP002 derived evidence
  ([derived/README.md](../../experiments/EXP002-gold-trend-following/evidence/derived/README.md))
  and the frozen baseline rules in Q003.
- Interpreted the frozen baseline result against the primary success criterion
  and the buy-and-hold benchmark, and against the mandatory cost caveat.
- Updated Q003 with the evaluation outcome and the resulting stance
  (version 3.7 → 3.8).
- Registered this session in
  [README.md](../../README.md) and synchronized Q003's version in
  [artifact-registry.json](../governance/artifact-registry.json).
- Updated [CURRENT.md](../operating-system/CURRENT.md) with the new NEXT ACTION.

No hypothesis, experiment, code, or rule was created. The frozen baseline rules
were not modified.

---

# The Result Being Interpreted

From `evidence/derived/README.md`, over the fixed inclusive window
`2020-09-28`–`2026-09-28` (1,549 daily bars):

| Metric | Strategy | Buy-and-hold |
|--------|----------|--------------|
| Final equity (start 1.0) | 1.099101 | 2.210240 |
| Total return | **+9.91%** | +121.02% |
| CAGR | **+1.59%** | +14.14% |
| Max drawdown | **-25.92%** | -26.60% |

Activity: 32 trades; average holding 31.1 days; maximum 365 days; invested
45.19% of the time; exits 31 signal / 1 time stop / 0 window end.

Cost status: net of **quoted spread only** (Ask entries / Bid exits). No
reliable commission or financing/swap records exist for the period, so those
costs are excluded and the result **MUST NOT** be called fully net of costs.

---

# What Was Learned

## The primary success criterion was not met in a robust sense

Q003's primary criterion is positive net returns after costs. On this frozen
baseline the strategy returned **+9.91% total / +1.59% CAGR** net of quoted
spread only. That margin is small enough that unmodelled commissions and any
overnight financing/swap would plausibly erase it. So the criterion is, at
best, marginally and fragilely met and is best read as a **weak/negative
result**, not a positive one.

## The instrument rose; the strategy did not capture it

Buy-and-hold returned **+121.02%** over the same window with a similar maximum
drawdown (-26.60% vs -25.92%). The price premise moved strongly upward, yet the
SMA200 long-only rule captured little of it: after the 2024-10-18 time stop the
rule stayed flat through the largest advance and only re-entered on 2026-08-20.
This separates the two things Q003 deliberately kept apart — the long-run price
premise and the strategy's profitability. The premise trending up did not imply
the strategy profited.

## A negative result is legitimate progress

Per the operating rules, a rejected hypothesis is progress. The frozen baseline
did not establish a profitable edge, and it is recorded as evidence, not a
green light. No tuning of the frozen rules is permitted against this period.

---

# Decisions

- Record the EXP002 frozen baseline outcome as a **weak/negative result** for
  Q003's primary success criterion: it does not establish a profitable edge.
- Keep the long-run gold price premise as **user-reported and unverified**; the
  observed buy-and-hold rise over this single window is **not** promoted to a
  project claim about gold's long-run direction.
- **Do not** create a hypothesis from this result; the evidence does not
  warrant one.
- **Do not** tune the locked baseline rules against the evaluation period.
- Keep Q003 in `draft`: its primary question is answered negatively for the
  frozen baseline, while its related-but-independent questions (long-run trend;
  robust trend/exit definitions; acceptable risk/drawdown; benchmark gap) remain
  open and unaddressed.
- Carry the mandatory caveats forward unchanged: the naive `DateTime` time
  zone, the single `Volume` column meaning, and the source gap/empty-day
  structure remain unverified.

---

# Artifacts Created

- research/sessions/S007-exp002-baseline-interpretation.md (S007) — this session

# Artifacts Modified

- questions/Q003-long-only-gold-trend-following.md (Q003) — recorded the
  evaluation outcome and stance; version 3.7 → 3.8; `last-reviewed` updated.
- README.md — added S007 to the Sessions table.
- governance/artifact-registry.json — synchronized Q003 to version 3.8;
  registry version 1.19.2 → 1.19.3.
- operating-system/CURRENT.md — new NEXT ACTION and exit check.

---

# Outcome

Q003's primary question is answered **negatively** for the frozen baseline: the
pre-registered long-only SMA200 strategy did not produce a robust positive net
return over `2020-09-28`–`2026-09-28` and was dwarfed by buy-and-hold. The
result is preserved as EXP002 derived evidence, not as a discovery. No
hypothesis was created, no rule was changed, and the frozen baseline was not
tuned. The disposition of Q003 beyond this interpretation is left to the
researcher's next decision.

---

# Relationships

- related-to: questions/Q003-long-only-gold-trend-following.md (Q003)
- related-to: decisions/DEC002-accept-amended-exp002-registration.md (DEC002)
- related-to: sources/SRC006-dukascopy-historical-data-export.md (SRC006)
- related-to: principles/PR002-data-provenance-and-fitness.md (PR002)
- related-to: principles/PR003-raw-data-immutable-derived-traceable.md (PR003)
- related-to: governance/rules/RG001-automation-follows-stability.md (RG001)
- related-to: governance/rules/RG009-claim-provenance.md (RG009)
- relates-to: experiments/EXP002-gold-trend-following/ (EXP002 evidence)
- derives-from: research/003-research-methodology.md (research-003)