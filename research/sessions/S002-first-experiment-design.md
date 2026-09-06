---
id: S002
type: session

title: First Experiment Design

status: completed
version: 1.0

owner: Project Zero

created: 2026-09-06
last-reviewed: 2026-09-06
---

# Session Objective

Design the first experiment (EXP001) and, by doing so, put the research pipeline
under load for the first time.

Until this session the repository contained a complete framework and zero
experiments. Every governance artifact was an untested assumption about how
research would be conducted. The purpose here was not to produce a trading
result but to find out whether the framework can actually carry an experiment.

---

# What Was Decided

## EXP001 replicates a published anomaly rather than testing an original idea

Time-series (absolute) momentum on a broad equity index: hold the index when its
trailing 12-month return is positive, hold cash otherwise.

The reasoning is isolation of unknowns. An original signal would confound two
questions — whether the signal has merit and whether the process works. A
well-documented signal makes the process the only variable. RG005 requires
benchmarking before invention, and this satisfies it concretely rather than
rhetorically.

A secondary reason: a negative result stays informative. If a rule this widely
published fails its own out-of-sample period under honest cost assumptions, that
is a substantive finding about how much weight published backtests deserve.

## EXP001 tests a sub-claim, not H001

H001 asserts that edge is emergent from an entire system. No single experiment
can settle that. EXP001 therefore tests sub-claim C1 — that a published momentum
rule retains a risk-adjusted advantage post-publication — and states explicitly
which H001 prediction C1 bears on (prediction 2, degradation without
adaptation).

This is recorded as a deliberate scope limit in the EXP001 governance record so
a later reader cannot mistake a C1 result for an H001 verdict.

## The experiment measures its own process

EXP001 carries process metrics: effort by phase, count of discretionary choices,
count of shortcuts the methodology prevented, and count of points where
governance produced work that caught nothing.

The last metric was added deliberately. H000 asserts the project should not
exist unless the process creates value, and H000 cannot be tested if the project
only records evidence flattering to itself. The execution log has a dedicated
section for governance overhead with no research value.

## Success criteria separate research quality from market outcome

The experiment succeeds as research if evidence is preserved with provenance,
the procedure is reproducible, all metrics are reported for both periods and
both arms, robustness checks are all run and reported, and a decision is
recorded — including "inconclusive". Whether C1 turns out true is a separate
question with its own findings criteria.

This separation exists so that an inconclusive market result cannot be
experienced as a failed experiment. Under research-003, rejecting a weak idea is
successful research.

## The primary result is recorded before robustness checks are run

Procedure step 6 freezes the headline result before perturbations are computed.
Without this ordering the primary result can be quietly reframed by whichever
robustness check looks most flattering. This is a specific, cheap defence
against a specific, common failure.

---

# Framework Observations

Designing a real experiment surfaced things the framework did not previously
have to answer:

1. **Evidence needed a home with rules, not just a folder.** G001 says evidence
   is immutable, but nothing stated where it lives or how a correction is made.
   EXP001 now separates `raw/` (never edited, hashed, provenance recorded) from
   `derived/` (regenerable), and corrections are made by superseding files
   rather than editing.

2. **RG007's governing set is a judgement call.** The distinction between an
   artifact that governs work and one the work merely references is not
   mechanical. DEC001 constrains EXP001 to manual execution but is a decision,
   not governance; it is made operational by RG001. The governance record now
   lists DEC001 under "referenced but not governing" with that reasoning stated,
   and adds a column showing how each governing artifact was actually satisfied
   rather than merely cited.

3. **The relationship vocabulary held.** No new relationship type was needed.
   The `[planned]` marker in G006 did real work for the not-yet-existing
   evidence link.

4. **Nothing in the framework told the researcher what to study.** Governance
   constrains how research is conducted, not what question is worth asking. The
   choice of momentum came from RG005 and judgement, not from any artifact. That
   is probably correct, but it is worth naming: the framework is a discipline,
   not a research agenda.

No governance change is proposed from this session. The framework carried the
experiment without amendment, which is the first weak evidence that it is
usable. Whether it is worth its cost is a question for the execution log.

---

# Artifacts Created

- experiments/EXP001/EXP001-momentum-replication.md (EXP001) — experiment design, status draft
- experiments/EXP001/evidence/README.md — evidence layout and immutability rules
- experiments/EXP001/evidence/execution-log.md — process metric capture, not started
- research/sessions/S002-first-experiment-design.md (S002) — this session

---

# Artifacts Modified

- experiments/EXP001/GOVERNANCE.md — governing set completed with satisfaction notes and scope limit
- hypotheses/H001-edge-is-emergent.md (H001) — tested-by relationship resolved to the real EXP001 path
- experiments/README.md — status updated; directory is no longer empty
- README.md — EXP001 and S002 registered
- governance/artifact-registry.json — EXP001 registered

---

# Outcome

The pipeline is no longer unexercised at the design stage. EXP001 exists as a
frozen specification with success criteria, failure criteria, assumptions, and
scope limits recorded before any data has been looked at.

Nothing has been executed. No evidence exists. No confidence value has moved.
H001 remains at 0.5 and H000 at 0.8, correctly, because a design is not
evidence.

The next step is execution: retrieve the data, record provenance, and work
through the procedure manually while keeping the execution log honest about what
the process costs.

---

# Relationships

- related-to: experiments/EXP001/EXP001-momentum-replication.md (EXP001)
- related-to: hypotheses/H001-edge-is-emergent.md (H001)
- related-to: hypotheses/H000-project-should-not-exist.md (H000)
- related-to: research/003-research-methodology.md (research-003)
- related-to: governance/rules/RG005-benchmark-before-invention.md (RG005)
- related-to: governance/rules/RG007-governance-execution.md (RG007)
- related-to: decisions/DEC001-no-software-before-method.md (DEC001)
- derives-from: research/sessions/S001-framework-hardening.md (S001)
