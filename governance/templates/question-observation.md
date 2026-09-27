---
id: ART-QUESTION-OBSERVATION
type: artifact-template
title: Question / Observation
status: draft
version: 1.0

owner: Project Zero
created: 2026-09-27
last-reviewed:

created-by-type: human + agent
created-by: |
  Primary: Mehdi
  Agent-assisted by: ChatGPT (OpenAI)
created-by-version: not available
production-tools: ChatGPT, Codex desktop, apply_patch; versions not available
created-at: 2026-09-27T23:10:33+03:30
---

# Purpose

Define the standard structure for capturing an initial research idea, question,
or observation without prematurely turning it into a hypothesis or research
conclusion.

---

# Context

This template defines the first structured output of the Project Zero research
workflow.

The initial input may be provided by the researcher in any informal form. The researcher is not required to follow a predefined input format.

The artifact should preserve the original input while separating observations, existing evidence, assumptions, unknowns, and the resulting research question.

---

# Content

## Raw Input

The original idea, question, or observation as provided by the researcher.

## Core Observation / Question

A concise formulation of what is actually being observed or asked.

## Context

Relevant context needed to understand the observation or question.

## Existing Evidence

Evidence already available to the researcher at this point.

> Existing evidence MUST be clearly distinguished from assumptions, interpretations, or expectations.

## Evidence Status / Provenance

For each item under Existing Evidence, state whether it is user-reported,
first-hand, or traceable to an existing Artifact. Traceable evidence MUST name
the source Artifact; user-reported evidence MUST NOT be treated as verified
project evidence.

## Assumptions / Interpretations

Claims or interpretations embedded in the initial idea that have not yet been established.

## Unknowns

Important things that are currently unknown and may need to be investigated.

## Primary Research Question

A clearly formulated question that can be investigated empirically where applicable.

## Related but Independent Questions

Questions raised by the input that require their own investigation and MUST NOT
be silently embedded in the Primary Research Question.

If none:

> None.

## Scope

The boundaries of the question, including relevant instruments, markets, assets, time periods, populations, conditions, or other constraints when applicable.

## Open Clarifications

Questions that must be answered before the Research Question can be considered sufficiently well-defined.

---

# Rationale

A structured Question / Observation artifact prevents an initial idea from
being prematurely treated as a hypothesis, evidence, or conclusion.

It also creates a stable handoff between the initial human input and subsequent
research workflow stages.

---

# Relationships

- depends-on: governance/G003-artifact-model.md (G003)
- depends-on: governance/G004-artifact-lifecycle.md (G004)
- depends-on: governance/G006-relationships.md (G006)
- depends-on: governance/rules/RG008-authorship-provenance.md (RG008)
- related-to: governance/G001-research-governance.md (G001)
- related-to: research/003-research-methodology.md (research-003)

---

# References

> None.

---

# Representations

- Markdown

---

# Constraints

- The original researcher input MUST be preserved.
- The artifact MUST distinguish observations from interpretations.
- Existing evidence MUST be distinguished from assumptions or expectations.
- Each existing-evidence item MUST state its status or provenance.
- User-reported evidence MUST NOT be represented as verified project evidence.
- The Research Question MUST NOT presuppose its answer.
- The Research Question SHOULD be sufficiently specific and testable.
- Important ambiguities MUST be explicitly identified.
- Multiple independent questions MUST NOT be unnecessarily collapsed into one Research Question.
- Hypotheses MUST NOT be presented as established findings at this stage.

---

# Review

Manual review before the Draft → Review lifecycle transition and during the
first complete execution of the research workflow.

The artifact template should be revised when practical use reveals missing information, unnecessary fields, or ambiguous responsibilities.

---

# Revision History

| Version | Date       | Summary |
| ------- | ---------- | ------- |
| 1.0     | 2026-09-27 | Initial version |
