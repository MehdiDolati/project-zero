---
id: RG001
type: rule

title: Automation Follows Stable Manual Practice

status: active
version: 1.0

owner: Project Zero

created: 2026-07-28
last-reviewed: 2026-09-04
---

# Statement

Automation MUST only be introduced after a manual process has demonstrated repeated value and stability.

---

# Rationale

Automation amplifies existing processes.

It should never be used to discover whether a process is valuable.

Manual execution provides the evidence required to justify automation.

---

# Consequences

Following this rule:

- reduces premature engineering,
- keeps attention on solving the real problem,
- prevents unnecessary tooling.

Ignoring this rule increases the risk of automating ineffective processes.

---

# Applies To

- Repository tooling
- Validation
- Research workflows
- Documentation workflows

---

# Exceptions

Exceptions require explicit documented justification.

---

# Related Artifacts

- decisions/DEC001-no-software-before-method.md (DEC001)
- governance/G001-research-governance.md (G001)