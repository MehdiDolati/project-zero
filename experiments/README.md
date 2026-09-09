# Experiments

The Experiment is the atomic unit of learning in Project Zero
([research-003](../research/003-research-methodology.md)).

An experiment is a repeatable process designed to generate evidence that
supports or challenges a hypothesis, or that investigates an unexpected
observation.

---

# Requirements

Every experiment MUST, per
[G001-research-governance](../governance/G001-research-governance.md):

- reference one or more hypotheses,
- define success criteria,
- define failure criteria,
- preserve raw evidence,
- record assumptions,
- record methodology,
- record authorship and production-tool provenance,
- be reproducible.

No claim becomes project knowledge without experimental evidence. A failed
experiment is a successful research outcome when it is preserved with its
reasoning.

---

# Authorship and Tool Provenance

Every experiment artifact and execution log MUST identify who produced it and
how it was produced. This metadata describes the producer; it does not replace
the artifact owner or the governing-work record required by
[RG007-governance-execution](../governance/rules/RG007-governance-execution.md).

Use the following fields in the artifact front matter or, for evidence, at the
top of the execution log:

| Field | Required value |
|-------|----------------|
| `created-by-type` | `human` or `agent` |
| `created-by` | Human name, or agent name and provider |
| `created-by-version` | Agent/model version when applicable; `not available` when it cannot be observed |
| `production-tools` | Tool names and versions when available (for example, VS Code and its extension or CLI) |
| `created-at` | Timestamp with timezone |

An agent MUST NOT be recorded as a human. If several people or agents
contributed, record each contributor and distinguish the primary producer from
reviewers. Missing version information MUST be stated explicitly rather than
guessed.

This README change is recorded as follows:

| Field | Value |
|-------|-------|
| `created-by-type` | `agent` |
| `created-by` | AI assistant using Copilot SDK in VS Code |
| `created-by-version` | `not available` |
| `production-tools` | VS Code/Copilot SDK; `apply_patch` |
| `created-at` | `2026-09-09T08:42:05+03:30` |

---

# Knowledge Flow

Experiment results produce evidence. Evidence that survives repeated
evaluation becomes a discovery (see [discoveries/](../discoveries/README.md)).

Experiment → Evidence → Decision → Knowledge

---

# Layout

Each experiment lives in its own directory containing:

| File | Role |
|------|------|
| `EXPNNN-<slug>.md` | The experiment artifact: design, criteria, assumptions, procedure |
| `GOVERNANCE.md` | Governance record pinning governing artifacts by identity and version ([RG007](../governance/rules/RG007-governance-execution.md)) |
| `evidence/` | Raw data with provenance, derived series, execution log. Immutable once written |
| `RESULTS.md` | Findings, written on execution |

---

# Status

| ID | Title | Status | Location |
|----|-------|--------|----------|
| EXP001 | Manual Replication of a Published Momentum Anomaly | draft | [EXP001/](EXP001/EXP001-momentum-replication.md) |

EXP001 is designed but **not executed**. No evidence exists yet, so no
experiment has produced project knowledge.

Execution is manual — spreadsheet only, no custom software
([DEC001](../decisions/DEC001-no-software-before-method.md),
[RG001](../governance/rules/RG001-automation-follows-stability.md)).

---

New experiments are created from
[governance/templates/artifact-template.md](../governance/templates/artifact-template.md)
and registered in the root [artifact registry](../README.md#artifact-registry).
