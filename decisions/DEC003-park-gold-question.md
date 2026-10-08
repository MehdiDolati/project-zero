---
id: DEC003
type: decision
title: Park the Long-Only Gold Trend-Following Question

status: accepted
version: 1.0

owner: Project Zero

created: 2026-10-09
last-reviewed: 2026-10-09
---

# Decision

Park the active pursuit of
[Q003](../questions/Q003-long-only-gold-trend-following.md) (long-only trend
following in gold) after the EXP002 frozen baseline returned a weak/negative
result, and direct the next work toward another question or back to the
[North Star](../research/000-north-star.md).

Q003 is retained as `draft`; it is **not** promoted, deprecated, or archived.

---

# Context

Q003 was the project's second valid manual application of
[AC001](../governance/agent-contracts/AC001-question-formulation.md). Its
frozen SMA200 long-only baseline was executed as
[EXP002](../experiments/EXP002-gold-trend-following/) against the
[DEC002](DEC002-accept-amended-exp002-registration.md) amended master.

S007 recorded the outcome: **+9.91% total / +1.59% CAGR** net of quoted spread
only, **-25.92%** maximum drawdown, versus buy-and-hold **+121.02% / +14.14%
CAGR**. The result was recorded as a **weak/negative result** that does not
establish a profitable edge; the long-run gold premise remains user-reported
and unverified, and the locked rules were not tuned
([S007](../research/sessions/S007-exp002-baseline-interpretation.md)).

After S007, the researcher was presented with three forward paths: (a) address
a related-but-independent question inside Q003, (b) refine or re-scope the gold
question with a new frozen design, or (c) park the question. The researcher
chose **(c) park the question** and move to another question or the North Star.

---

# Problem

A single frozen, untuned baseline produced a result that is, at best, marginal
and fragile, and clearly behind buy-and-hold. Continuing to work the same
question risks:

- implicitly tuning against the already-examined `2020-09-28`–`2026-09-28`
  evaluation period, which would destroy its holdout status;
- treating a weak result as a mandate to iterate, which
  [H000](../hypotheses/H000-project-should-not-exist.md) and the project's
  evidence discipline discourage;
- sinking further effort into a question whose premise (gold's long-run rise)
  is still unverified and whose baseline already disappointed.

At the same time, the project must not lose the thread: Q003 and its related
questions remain legitimate, and the recorded evidence must be preserved.

---

# Decision Drivers

- **Evidence discipline.** A weak/negative untuned baseline is legitimate
  progress ([daily-routine Rule 6](../operating-system/daily-routine.md)); the
  correct response is not to keep tinkering with a locked design.
- **Holdout integrity.** Any further use of the `2020-09-28`–`2026-09-28`
  window for tuning would contaminate it. Parking prevents that pressure.
- **Focus.** The daily routine is built around one direction at a time;
  switching targets deliberately is preferable to drifting within a
  disappointing one.
- **Traceability.** The question, its evidence, and the reason for pausing it
  must all remain recorded, not deleted.
- **Reversibility.** Parking is a prioritization choice, not a judgement that
  the question is false; it can be resumed.

---

# Decision

1. **Park Q003's active pursuit.** No further work is scheduled on Q003 as the
   current direction. Its open related-but-independent questions (long-run
   trend, robust trend/exit definitions, acceptable risk/drawdown, benchmark
   gap) remain recorded but unscheduled.

2. **Retain Q003 as `draft`.** Q003 keeps its identity, content, and `draft`
   status ([RG003](../governance/rules/RG003-artifact-identity.md)). No
   lifecycle transition is made: parking is a prioritization decision, not a
   governance lifecycle state ([G004](../governance/G004-artifact-lifecycle.md)).

3. **Preserve all EXP002 evidence.** The amended dataset, frozen rules, derived
   daily bars, backtest, and S007 interpretation remain immutable and
   reachable.

4. **Do not tune the frozen rules.** The `2020-09-28`–`2026-09-28` evaluation
   window MUST NOT be used to select or refine any strategy variant.

5. **Direct the next work elsewhere.** The next direction is to be chosen
   between the project's other open question(s) — currently
   [Q001](../questions/Q001-conditional-mean-reversion-aud-crosses.md) — and a
   return to the [North Star](../research/000-north-star.md) to reassess
   direction.

6. **Record the parking.** Add Q003 to the
   [Parking Lot](../operating-system/PARKING-LOT.md) under both `Questions` and
   `Things to Revisit`, and set a concrete `NEXT ACTION` in
   [CURRENT.md](../operating-system/CURRENT.md).

---

# Consequences

Positive:

- protects the holdout period from implicit tuning;
- frees the single project direction for a fresh target;
- preserves Q003 and its evidence for later resumption.

Negative:

- the project loses continuity on its most-developed question;
- Q001 (the only other live question) has never been advanced, so the next
  direction starts from a shallower base;
- a future resumption of Q003 should use a fresh out-of-sample window or a
  materially different, separately frozen design, which may require new data
  handling.

These costs are accepted because continuing a weak, untuned design risks the
project's evidence discipline for an uncertain payoff.

---

# Review Criteria

This decision should be revisited if:

- the researcher chooses to resume Q003 (for example after verifying the
  long-run gold premise, or with a new frozen design and a fresh evaluation
  window);
- another question or the North Star produces findings that make the gold
  question materially more or less attractive;
- the gold baseline's weak result is shown to be an artifact of an unverified
  data assumption (naive time zone, single `Volume`, gap structure).

---

# Relationships

- decides: questions/Q003-long-only-gold-trend-following.md (Q003)
- relates-to: decisions/DEC002-accept-amended-exp002-registration.md (DEC002)
- relates-to: research/sessions/S007-exp002-baseline-interpretation.md (S007)
- relates-to: experiments/EXP002-gold-trend-following/ (EXP002)
- relates-to: research/000-north-star.md (research-000)
- relates-to: questions/Q001-conditional-mean-reversion-aud-crosses.md (Q001)
- governed-by: governance/G001-research-governance.md (G001)
- governed-by: governance/G004-artifact-lifecycle.md (G004)
- derives-from: research/003-research-methodology.md (research-003)
- derives-from: operating-system/daily-routine.md