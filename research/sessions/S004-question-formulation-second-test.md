---
id: S004
type: session
title: Second Question Formulation Test
status: completed
version: 1.0

owner: Project Zero

created: 2026-09-28
last-reviewed: 2026-09-28

created-by-type: human + agent
created-by: |
  Primary: Mehdi
  Agent-assisted by: AI assistant (Copilot SDK in VS Code)
created-by-version: not available
production-tools: VS Code, AI assistant (Copilot SDK); versions not available
created-at: 2026-09-28T14:00:00+03:30
---

# Session Objective

Apply the draft AC001 to a second free-form research idea and test whether the contract still preserves the required distinctions without forcing the user into a form or prematurely turning the idea into a hypothesis.

This session is a manual validation of the contract before any automation is considered.

---

# What Was Done

- Applied AC001 to a second free-form idea involving relative mean reversion in major crypto pairs.
- Preserved the raw user input verbatim in a new question artifact.
- Separated the observation from interpretations, evidence, and mechanism concerns.
- Recorded the question under `questions/` as a draft artifact.
- Checked whether the output exposed any missing instruction, unnecessary clarification, or ambiguity in the contract.

---

# What Was Learned

## The contract remains structurally sound on a second, different input

The second idea contained a vague market impression, a suspicion about a mechanism, and a possible exploitability question all at once. AC001 still separated those concerns into the correct sections without forcing the human to answer a rigid form.

## A minor gap is the handling of informal or mixed-language input

The raw input was in Persian and mixed informal language with market shorthand. The contract does not explicitly say that non-English or informal wording must be preserved exactly under `Raw Input`, even when it contains vague jargon. This is not a blocker, but it is a candidate for a small wording addition if the contract is refined.

## The distinction between empirical question and mechanism remains essential

The initial idea conflated three independent items: the observed pattern, a plausible explanation, and the question of whether it can be traded. The draft contract correctly kept those separate in the artifact, which is the main behavior this validation set out to test.

---

# Decisions

- Keep AC001 as the manual boundary for the Question / Observation stage; no automation was introduced.
- Preserve the second run as a draft question artifact rather than a hypothesis or strategy.
- Record the mixed-language/raw-input nuance as a candidate contract refinement rather than a reason to change the workflow manually.

---

# Artifacts Created

- questions/Q002-crypto-relative-mean-reversion.md (Q002) — second manual Question / Observation artifact, status draft.
- research/sessions/S004-question-formulation-second-test.md (S004) — this session.

---

# Outcome

The second manual use of AC001 passed the expected boundary check: it converted a free-form idea into a draft Question / Observation artifact without converting it into a hypothesis, a strategy, or a claim. The contract correctly kept empirical behavior, mechanism, and exploitability separate.

The only notable issue was a minor clarity gap around preserving mixed-language or informal input exactly as written. That is a refinement candidate, not a failure of the draft contract.

---

# Relationships

- related-to: questions/Q002-crypto-relative-mean-reversion.md (Q002)
- related-to: governance/agent-contracts/AC001-question-formulation.md (AC001)
- derives-from: research/003-research-methodology.md (research-003)
- related-to: governance/rules/RG001-automation-follows-stability.md (RG001)
- related-to: governance/rules/RG008-authorship-provenance.md (RG008)
