---
id: S003
type: session
title: Question / Observation Workflow Test
status: completed
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

# Session Objective

Test the first stage of the research workflow manually: turn unstructured
human input into a traceable Question / Observation artifact, and identify
what the workflow needs before agent automation is designed.

This session does not supersede or alter the pre-registered EXP001 execution
plan. It establishes the upstream Question / Observation stage that can frame
future research without asserting an experimental result.

---

# What Was Done

- Reviewed the generic artifact template and active governance requirements.
- Completed the draft Question / Observation template with authorship,
  provenance, relationship, and lifecycle information.
- Applied the template manually to the AUDCAD, AUDNZD, and NZDCAD
  mean-reversion idea.
- Established `questions/` and the `Q` identity family as the canonical home
  for persisted Question / Observation artifacts.
- Created Q001 as the first question artifact.

---

# What Was Learned

## User-reported results are not project evidence

The researcher had useful prior results, but their data, settings, costs, and
parameter-search history are not yet preserved. The workflow must distinguish
such reports from reproducible project evidence rather than placing both in an
undifferentiated Evidence field.

## One initial idea can contain several independent questions

The initial input contained three separate uncertainties: whether a behavior
exists, what could explain it, and whether it is exploitable. Combining them
would have hidden the conditions under which each could be challenged.

## The research loop needed a persisted question stage

The repository had a Question → Hypothesis transition but no canonical location
or identity family for a Question / Observation artifact. The `questions/`
directory and `Q` identity family close that gap without creating a hypothesis
or asserting a finding.

---

# Decisions

- Question / Observation artifacts are first-class project artifacts stored in
  `questions/` with stable identities in the `Q` family.
- Q001 remains `draft`; no claim, hypothesis, evidence, or strategy decision
  has been accepted.
- The next design step is a manual-first Question Formulation Agent Contract,
  not agent automation or trading-strategy implementation.

---

# Artifacts Created

- governance/templates/question-observation.md (ART-QUESTION-OBSERVATION) —
  draft output template for Question / Observation artifacts.
- questions/Q001-conditional-mean-reversion-aud-crosses.md (Q001) — first
  manual workflow result, status draft.
- questions/README.md — location, identity, and lifecycle guidance.
- research/sessions/S003-question-observation-workflow.md (S003) — this
  session.

---

# Outcome

The first workflow stage can accept free-form human input while preserving the
distinction between observations, unverified reports, assumptions, unknowns,
and research questions. Q001 now makes the next uncertainty explicit without
claiming an answer.

The next action is to draft the Question Formulation Agent Contract from the
validated manual behavior and Q001's open clarifications.

---

# Relationships

- related-to: questions/Q001-conditional-mean-reversion-aud-crosses.md (Q001)
- related-to: governance/templates/question-observation.md (ART-QUESTION-OBSERVATION)
- derives-from: research/003-research-methodology.md (research-003)
- related-to: governance/G001-research-governance.md (G001)
- related-to: governance/rules/RG001-automation-follows-stability.md (RG001)
