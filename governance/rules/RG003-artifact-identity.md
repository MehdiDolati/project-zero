---
id: RG003
type: rule

title: Stable Artifact Identity

status: active
version: 1.0

owner: Project Zero

created: 2026-07-28
last-reviewed: 2026-09-04
---

# Statement

Every persistent project knowledge element MUST be represented as an Artifact with a stable identity independent of its physical representations.

---

# Rationale

Knowledge persists longer than files.

Repository structure, filenames, and formats may evolve.

Artifact identity must remain stable.

---

# Consequences

Following this rule:

- enables reliable traceability,
- simplifies repository evolution,
- preserves long-term references.

Ignoring this rule creates broken references and unstable knowledge.

---

# Applies To

All Artifacts.

---

# Exceptions

None currently defined.

---

# Related Artifacts

- governance/G003-artifact-model.md (G003)