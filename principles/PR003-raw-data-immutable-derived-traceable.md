---
id: PR003
type: document
title: Raw Data Immutable, Derived Data Traceable

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

Separate raw data from everything computed from it, so that the original record
can never be altered and every derived value can be traced back to its source.

---

# Context

Project Zero transforms data: exports become daily bars, bars become signals,
signals become results. Each transformation risks overwriting the original or
losing the path back to it. This principle makes the two halves of that risk
explicit and forbids them.

---

# Content

- **Raw data is immutable.** Once captured, raw data MUST NOT be modified,
  cleaned in place, normalized, or overwritten. Corrections and
  re-interpretations are recorded as new derived artifacts, never by editing the
  raw record.
- **Derived data is traceable.** Every artifact derived from raw data MUST
  record what it was derived from, how (the transformation), and when. A derived
  value that cannot be traced to its raw source is not admissible.

---

# Rationale

If raw data can change, no downstream result is reproducible, and provenance is
meaningless because "the source" is a moving target. If derived data is not
traceable, an error cannot be located or corrected. Together, immutability of
the source and traceability of the derivation are what make results auditable.

---

# Relationships

- related-to: governance/G001-research-governance.md (G001)
- related-to: governance/G005-traceability.md (G005)
- related-to: governance/G004-artifact-lifecycle.md (G004)
- related-to: governance/rules/RG009-claim-provenance.md (RG009)
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

This principle SHOULD be reviewed whenever the traceability model (G005) or the
artifact lifecycle (G004) changes.

---

# Revision History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | 2026-09-30 | Initial version. Establishes raw-data immutability and derived-data traceability. |