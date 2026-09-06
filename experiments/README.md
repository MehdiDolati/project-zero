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
- be reproducible.

No claim becomes project knowledge without experimental evidence. A failed
experiment is a successful research outcome when it is preserved with its
reasoning.

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
