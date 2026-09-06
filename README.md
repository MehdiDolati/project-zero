# Project Zero

Project Zero is a research-first project with one question at its core:

> Can a solo researcher build a repeatable, evidence-based system for
> discovering and managing sustainable trading edge?

The purpose of this project is **not** to build software. It is to develop a
disciplined capability for finding, validating, managing, and retiring trading
opportunities under uncertainty — and ultimately to achieve the freedom to live
according to personal values. See the [North Star](research/000-north-star.md).

The repository is the long-term memory of the project
([PR001](principles/repository-as-source-of-truth.md)). It does not store
conversations or intentions; it stores **artifacts** — uniquely identified,
typed units of knowledge connected by explicit relationships
([G003](governance/G003-artifact-model.md), [G006](governance/G006-relationships.md)).

---

# Status

Snapshot as of 2026-09-04:

| Area | State |
|------|-------|
| Research foundation | Complete: problem, edge concept, methodology defined |
| Governance framework | Complete and self-consistent (G000-G006, RG001-RG006) |
| Hypotheses | H000 (project should not exist) and H001 (edge is emergent) are active, untested |
| Experiments | None yet — pipeline intentionally unexercised until the first hypothesis is tested manually |
| Software | None. Deliberate: [DEC001](decisions/DEC001-no-software-before-method.md) prohibits custom software until the manual method proves itself |
| Sessions | S000 (founding), S001 (framework hardening) |

The framework is deliberately "method before automation"
([RG001](governance/rules/RG001-automation-follows-stability.md)). The next
milestone is not code — it is the first manual experiment.

---

For a practical, step-by-step walkthrough of doing work in this framework
(creating artifacts, running experiments, registering knowledge, changing
governance), see [GUIDE.md](GUIDE.md).

---

# Reading Order

New contributors (human or AI) should read in this order:

1. [research/000-north-star.md](research/000-north-star.md) — why the project exists
2. [research/001-problem-definition.md](research/001-problem-definition.md) — what problem it addresses
3. [research/002-edge.md](research/002-edge.md) — how trading edge is understood
4. [research/003-research-methodology.md](research/003-research-methodology.md) — how research is conducted
5. [governance/README.md](governance/README.md) — how knowledge is governed
6. [hypotheses/H000-project-should-not-exist.md](hypotheses/H000-project-should-not-exist.md) — the kill-switch hypothesis
7. [hypotheses/H001-edge-is-emergent.md](hypotheses/H001-edge-is-emergent.md) — the central research hypothesis
8. [decisions/DEC001-no-software-before-method.md](decisions/DEC001-no-software-before-method.md) — the founding architectural decision
9. [research/sessions/S000-project-zero.md](research/sessions/S000-project-zero.md) — how the project restarted from first principles

---

# Structure

The repository organizes knowledge by maturity. Information flows from raw
concepts to trusted knowledge as confidence increases.

| Directory | Role | Current contents |
|-----------|------|------------------|
| [principles/](principles/) | Timeless beliefs | PR001 repository-as-source-of-truth |
| [research/](research/README.md) | Foundational concepts and research documents | research-000 to 003; sessions/ |
| [hypotheses/](hypotheses/) | Testable claims | H000, H001 |
| [experiments/](experiments/README.md) | Executed investigations | Empty by design |
| [discoveries/](discoveries/README.md) | Evidence-backed findings | Empty by design |
| [decisions/](decisions/) | Operational and architectural decisions | DEC001 |
| [governance/](governance/README.md) | Long-term project rules | G000-G006, rules RG001-RG006, templates |
| [software/](software/README.md) | Implementation | Empty by design (DEC001) |

The full governance model, including how governance itself evolves, is
described in [governance/README.md](governance/README.md).

---

# Artifact Registry

Every persistent knowledge element in this repository is an Artifact with a
stable identity, type, status, and owner. This registry is the authoritative
index; new artifacts MUST be registered here.

## Documents (research foundation)

| ID | Title | Status | Location |
|----|-------|--------|----------|
| research-000 | North Star | active | [research/000-north-star.md](research/000-north-star.md) |
| research-001 | Problem Definition | active | [research/001-problem-definition.md](research/001-problem-definition.md) |
| research-002 | Edge Definition | active | [research/002-edge.md](research/002-edge.md) |
| research-003 | Research Methodology | active | [research/003-research-methodology.md](research/003-research-methodology.md) |

## Principles

| ID | Title | Status | Location |
|----|-------|--------|----------|
| PR001 | Repository as Source of Truth | active | [principles/repository-as-source-of-truth.md](principles/repository-as-source-of-truth.md) |

## Hypotheses

| ID | Title | Status | Confidence | Location |
|----|-------|--------|------------|----------|
| H000 | Project Should Not Exist | active | 0.8 | [hypotheses/H000-project-should-not-exist.md](hypotheses/H000-project-should-not-exist.md) |
| H001 | Edge is an Emergent Property | active | 0.5 | [hypotheses/H001-edge-is-emergent.md](hypotheses/H001-edge-is-emergent.md) |

## Decisions

| ID | Title | Status | Location |
|----|-------|--------|----------|
| DEC001 | No Software Before Method | accepted | [decisions/DEC001-no-software-before-method.md](decisions/DEC001-no-software-before-method.md) |

## Sessions

| ID | Title | Status | Location |
|----|-------|--------|----------|
| S000 | Project Zero (founding) | completed | [research/sessions/S000-project-zero.md](research/sessions/S000-project-zero.md) |
| S001 | Framework Hardening | completed | [research/sessions/S001-framework-hardening.md](research/sessions/S001-framework-hardening.md) |

## Governance

| ID | Title | Status | Location |
|----|-------|--------|----------|
| G000 | Governance Model | active | [governance/G000-governance-model.md](governance/G000-governance-model.md) |
| G001 | Research Governance | active | [governance/G001-research-governance.md](governance/G001-research-governance.md) |
| G002 | Documentation Governance | active | [governance/G002-documentation-governance.md](governance/G002-documentation-governance.md) |
| G003 | Artifact Model | active | [governance/G003-artifact-model.md](governance/G003-artifact-model.md) |
| G004 | Artifact Lifecycle | active | [governance/G004-artifact-lifecycle.md](governance/G004-artifact-lifecycle.md) |
| G005 | Traceability Model | active | [governance/G005-traceability.md](governance/G005-traceability.md) |
| G006 | Relationships Model | active | [governance/G006-relationships.md](governance/G006-relationships.md) |

## Rules

| ID | Title | Status | Location |
|----|-------|--------|----------|
| RG001 | Automation Follows Stable Manual Practice | active | [governance/rules/RG001-automation-follows-stability.md](governance/rules/RG001-automation-follows-stability.md) |
| RG002 | Use Normative Keywords | active | [governance/rules/RG002-normative-keywords.md](governance/rules/RG002-normative-keywords.md) |
| RG003 | Stable Artifact Identity | active | [governance/rules/RG003-artifact-identity.md](governance/rules/RG003-artifact-identity.md) |
| RG004 | Relationships are First-Class | active | [governance/rules/RG004-first-class-relationships.md](governance/rules/RG004-first-class-relationships.md) |
| RG005 | Benchmark Before Innovation | active | [governance/rules/RG005-benchmark-before-invention.md](governance/rules/RG005-benchmark-before-invention.md) |
| RG006 | Persist Agreed Rules | active | [governance/rules/RG006-persist-agreed-rules.md](governance/rules/RG006-persist-agreed-rules.md) |

Templates for creating new artifacts and rules live in
[governance/templates/](governance/templates/).

---

# Creating a New Artifact

Every new artifact follows the same procedure:

1. **Determine the type and identity.** Use the appropriate ID family:
   research-NNN, H (hypothesis), EXP (experiment), DEC (decision), S (session),
   G (governance), RG (rule). Identities are stable forever
   ([RG003](governance/rules/RG003-artifact-identity.md)).
2. **Copy the relevant template** from
   [governance/templates/](governance/templates/). Every artifact requires:
   id, type, title, status, version, owner, created, and last-reviewed.
3. **Write content with evidence discipline.** Hypotheses MUST be falsifiable
   and state confidence ([G001](governance/G001-research-governance.md)).
   Experiments MUST define success and failure criteria, preserve raw evidence,
   and be reproducible.
4. **Declare relationships** under a `# Relationships` heading using the
   canonical vocabulary in [G006](governance/G006-relationships.md)
   ([RG004](governance/rules/RG004-first-class-relationships.md)).
5. **Register the artifact** in the tables above and update affected
   relationships elsewhere (backward traceability
   ([G005](governance/G005-traceability.md))).
6. **Record the session** if the work changed a belief, decision, methodology,
   or governance rule ([G002](governance/G002-documentation-governance.md)).

No claim becomes project knowledge without experimental evidence
([research-003](research/003-research-methodology.md)), and no artifact should
be created to satisfy process rather than reduce uncertainty
([G002](governance/G002-documentation-governance.md)).
