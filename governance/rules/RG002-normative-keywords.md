---
id: RG002
type: rule

title: Use Normative Keywords

status: active
version: 1.0

owner: Project Zero

created: 2026-07-28
last-reviewed: 2026-09-05
---

# Statement

Governance requirements MUST use normative keywords consistently.

The following keywords have defined meanings:

- MUST
- SHOULD
- MAY

---

# Rationale

Different requirement strengths require different enforcement levels.

Using normative keywords makes governance both human-readable and machine-interpretable.

This enables future validation tooling.

---

# Consequences

Following this rule:

- eliminates ambiguity,
- enables automated validation,
- distinguishes mandatory requirements from recommendations.

Ignoring this rule creates inconsistent governance.

---

# Applies To

- Governance
- Policies
- Rules
- Constraints
- Documentation

---

# Exceptions

Exceptions require explicit documented justification.

---

# Related Artifacts

- governance/G000-governance-model.md (G000)
- governance/rules/RG007-governance-execution.md (RG007)
- governance/manifest.json (manifest)