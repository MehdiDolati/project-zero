---
id: G005
type: governance

title: Traceability Model

status: active
version: 1.1

owner: Project Zero

created: 2026-07-28
last-reviewed: 2026-09-04
---

# Purpose

Define how knowledge is traced throughout the project.

Traceability ensures that every important conclusion, decision, and artifact
can be connected to its origin and supporting evidence.

---

# Principles

Traceability is a property of knowledge, not documents.

Every meaningful Artifact SHOULD be traceable.

Traceability MUST survive repository evolution.

---

# Traceability Chain

Project knowledge SHOULD form connected chains.

Typical examples include:

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

Rule

↓

Implementation

↓

Observation

↓

Revision

Not every chain requires every element.

---

# Traceability Requirements

Artifacts SHOULD reference their immediate dependencies.

Backward traceability MUST always be possible.

Forward traceability SHOULD be possible whenever practical.

Relationships SHOULD remain explicit.

---

# Traceability Granularity

Not every sentence requires traceability.

Traceability SHOULD exist at the Artifact level.

Future versions MAY support finer granularity.

---

# Broken Traceability

Broken links SHOULD be treated as governance issues.

Removing an Artifact MUST NOT silently break knowledge chains.

Deprecated Artifacts remain part of traceability.

---

# Review Policy

Traceability SHOULD be reviewed whenever:

- new Artifact types are introduced,
- repository structure changes,
- governance evolves.

---

# Future Automation

Future validators SHOULD detect:

- missing references,
- orphan Artifacts,
- broken chains,
- cyclic dependencies where prohibited.

---

# Related Artifacts

- governance/G003-artifact-model.md (G003)
- governance/G004-artifact-lifecycle.md (G004)
- governance/G006-relationships.md (G006)
- governance/rules/RG004-first-class-relationships.md (RG004)

---

# Revision History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | 2026-07-28 | Initial version (draft) |
| 1.1 | 2026-09-04 | Promoted from draft to active; metadata completed |