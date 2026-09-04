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

# Status

This directory is intentionally empty.

As of 2026-09-04 no experiment has been executed. The first experiment
(EXP001) is planned to test the central hypothesis
[H001-edge-is-emergent](../hypotheses/H001-edge-is-emergent.md), and must be
performed manually before any automation is considered
([DEC001](../decisions/DEC001-no-software-before-method.md),
[RG001](../governance/rules/RG001-automation-follows-stability.md)).

New experiments are created from
[governance/templates/artifact-template.md](../governance/templates/artifact-template.md)
and registered in the root [artifact registry](../README.md#artifact-registry).
