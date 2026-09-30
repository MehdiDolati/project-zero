---
id: PR004
type: document
title: Architecture Is Not Implementation Plan

status: active
version: 1.0

owner: Project Zero

created: 2026-09-30
last-reviewed: 2026-09-30

created-by-type: human + agent
created-by: |
  Primary: Mehdi
  Agent-assisted by: AI assistant (Cline)
created-by-version: not available
production-tools: VS Code, AI assistant; versions not available
created-at: 2026-09-30T11:12:00+03:30
---

# Purpose

Keep the description of what the system must someday be separable from the plan
for what is built now, so that fidelity to the future does not force premature
implementation and present needs do not silently break the architecture.

---

# Context

Project Zero is a long-horizon system built incrementally. There is constant
pressure in two directions: to over-build today in the name of a future that may
change, and to under-design today in a way that later cannot be extended. This
principle draws the line between the two artifacts that carry those pressures.

---

# Content

- **Architect for the necessary future.** The architecture MUST describe the
  shape the system needs to reach: its layers, responsibilities, and boundaries.
  It is a statement of intent and constraint, not of sequence or schedule.
- **Implement for the present need.** Implementation MUST satisfy a present,
  evidenced need. It MUST NOT build capability merely because the architecture
  permits it.
- **Architecture is not an implementation plan.** An architecture document is
  not a build order, a roadmap, or a task list. Implementation plans are separate
  artifacts and MUST NOT be conflated with architecture.

---

# Rationale

When architecture and implementation plan are conflated, either the
implementation is dragged ahead of real need (building for imagined futures) or
the architecture is quietly narrowed to whatever was convenient to build now
(losing the necessary future). Separating them lets the architecture stay honest
about the future while the implementation stays honest about the present.

---

# Relationships

- related-to: governance/G001-research-governance.md (G001)
- related-to: governance/G003-artifact-model.md (G003)
- related-to: governance/G004-artifact-lifecycle.md (G004)
- related-to: governance/rules/RG005-benchmark-before-invention.md (RG005)
- related-to: decisions/DEC001-no-software-before-method.md (DEC001)
- related-to: principles/repository-as-source-of-truth.md (PR001)

---

# References

This principle does not rely on external claims.

> None.

---

# Representations

- Markdown

---

# Constraints

> None.

---

# Review

This principle SHOULD be reviewed whenever the artifact model (G003), the
artifact lifecycle (G004), or DEC001 change.

---

# Revision History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | 2026-09-30 | Initial version. Separates architecture from implementation planning. |