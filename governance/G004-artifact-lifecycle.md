---
id: G004
type: governance

title: Artifact Lifecycle

status: active
version: 1.1

owner: Project Zero

created: 2026-07-28
last-reviewed: 2026-09-04
---

# Purpose

Define the common lifecycle shared by all Artifacts.

This lifecycle governs how Artifacts evolve over time while preserving identity,
traceability, and knowledge quality.

---

# Principles

The Artifact Lifecycle is independent of Artifact type.

Every Artifact follows the same lifecycle regardless of whether it is a
Hypothesis, Decision, Rule, Experiment, Dataset, Session, or any future
Artifact type.

Domain-specific lifecycles MAY extend this lifecycle but MUST NOT replace it.

---

# Lifecycle States

## Draft

The Artifact is being created or substantially modified.

The content is incomplete and should not be relied upon.

---

## Review

The Artifact is undergoing evaluation.

Review MAY include technical, methodological, or governance validation.

---

## Active

The Artifact has been accepted and represents current project knowledge.

Active Artifacts MAY be referenced by other Artifacts.

---

## Deprecated

The Artifact has been superseded or is no longer recommended.

It remains available for historical traceability.

New work SHOULD reference the replacing Artifact whenever possible.

---

## Archived

The Artifact is retained only for historical purposes.

Archived Artifacts MUST remain immutable.

---

# Lifecycle Transitions

| From | To | Condition |
|------|----|-----------|
| Draft | Review | Ready for evaluation |
| Review | Draft | Revision requested |
| Review | Active | Accepted |
| Active | Deprecated | Superseded or no longer recommended |
| Deprecated | Archived | Historical retention only |

Transitions outside this model require explicit justification.

---

# Lifecycle Invariants

The following rules always apply.

- Every Artifact MUST have exactly one current lifecycle state.
- Artifact identity MUST remain stable across all state transitions.
- State transitions MUST be explicit.
- Every transition SHOULD be traceable.
- Archived Artifacts MUST NOT be modified.

---

# Review Policy

Artifacts SHOULD be reviewed whenever:

- related Artifacts change,
- new evidence becomes available,
- governance evolves,
- assumptions are invalidated.

Periodic review MAY also be performed.

---

# Relationship to Domain Lifecycles

This lifecycle defines the governance state of an Artifact.

Domain-specific progress is independent.

Example:

A Hypothesis MAY be:

- Active (governance lifecycle)
- Under Experiment (research lifecycle)

simultaneously.

---

# Future Extensions

Future Artifact types MAY define additional domain-specific states.

These extensions MUST remain compatible with the common Artifact Lifecycle.

---

# Related Artifacts

- G003 Artifact Model
- Governance Rules
- Artifact Template

---

# Revision History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | 2026-07-28 | Initial version (draft) |
| 1.1 | 2026-09-04 | Promoted from draft to active; metadata completed |