---
id: G001
type: governance

title: Research Governance

status: active
version: 1.0

owner: Project Zero

created: 2026-07-28
last-reviewed: 2026-09-04
---

# Purpose

Research Governance defines the minimum standards that every research artifact must satisfy.

Its objective is not to restrict research.

Its objective is to ensure that every conclusion can be understood, challenged, reproduced, and improved.

---

# Research Philosophy

Project Zero values disciplined learning over rapid experimentation.

Research quality is determined not by the number of ideas generated but by the quality of evidence produced.

---

# Research Lifecycle

Every research artifact should move through a defined lifecycle.

Question

↓

Hypothesis

↓

Experiment

↓

Evidence

↓

Decision

↓

Knowledge

↓

Review

↓

Archive (optional)

Knowledge is considered provisional at every stage.

---

# Artifact Requirements

## Question

A research question SHOULD:

- be specific,
- be answerable,
- be relevant to the North Star.

---

## Hypothesis

Every hypothesis MUST:

- have a unique identifier,
- describe a falsifiable claim,
- define at least one falsification criterion,
- state current confidence,
- reference the motivating question.

---

## Experiment

Every experiment MUST:

- reference one or more hypotheses,
- define success criteria,
- define failure criteria,
- preserve raw evidence,
- record assumptions,
- record methodology,
- be reproducible.

---

## Evidence

Evidence MUST:

- originate from an experiment,
- remain immutable,
- preserve provenance,
- record authorship and production-tool metadata.

Evidence MUST NOT be modified after creation.

Authorship and tool metadata MUST include:

- `created-by-type`: `human` or `agent`
- `created-by`: person's name, or agent name and provider
- `created-by-version`: agent/model version if applicable; `not available` if it cannot be observed
- `production-tools`: tool names and versions when available (e.g., VS Code, language version, CLI tools)
- `created-at`: timestamp with timezone

These fields MUST appear in the artifact front matter (YAML) or, for evidence documents, at the head of the file. Missing version information MUST be stated explicitly rather than guessed.

---

## Decision

Every research decision MUST:

- reference supporting evidence,
- explain rejected alternatives when applicable,
- state confidence,
- identify remaining uncertainty.

---

## Knowledge

Knowledge MUST:

- reference its supporting decisions,
- remain open to future revision,
- never be treated as absolute truth.

---

# Research Sessions

A research session SHOULD be recorded whenever one or more of the following occurs:

- a major assumption changes,
- a governance rule changes,
- a methodology changes,
- a significant hypothesis is accepted or rejected,
- a strategic project decision is made.

Sessions preserve reasoning rather than conversation.

---

# Review

Research artifacts SHOULD be periodically reviewed.

Review may result in:

- confirmation,
- revision,
- deprecation,
- archival.

---

# Negative Results

Negative findings are valuable.

Failed experiments reduce uncertainty and prevent repeated mistakes.

Negative evidence should be preserved whenever practical.

---

# Serendipity

Unexpected discoveries are encouraged.

However, every unexpected finding MUST pass through the same validation process as hypothesis-driven research.

Unexpected observations are inputs to research.

They are not knowledge.

---

# Automation

Automation should reduce cognitive load.

Automation MUST NOT replace scientific reasoning.

Every automated rule should first demonstrate value through repeated manual use.

---

# Continuous Improvement

The research process itself is an object of research.

Research Governance may evolve whenever evidence demonstrates a superior approach.