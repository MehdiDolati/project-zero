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

Snapshot as of 2026-09-28:

| Area | State |
|------|-------|
| Research foundation | Complete: problem, edge concept, methodology defined |
| Questions | Q001 and Q003 are drafts; Q002 is deprecated because its input was assistant-invented; no claim or evidence accepted |
| Agent contracts | AC001 v1.1 reflects two valid manual Question / Observation tests; no automation approved |
| Governance framework | Complete and self-consistent (G000-G006, RG001-RG009) |
| Hypotheses | H000 (project should not exist) and H001 (edge is emergent) are active, untested |
| Experiments | EXP001 design active; execution step 1 complete — sources verified pre-download, raw data retrieved, hashed, and provenance-recorded (TB3MS verified; workbook verifies at step 2). The manual computation phase (steps 2–7) is fully pre-registered — spreadsheet recipes, metric definitions, robustness variants, and the stage-gated [RESULTS.md](experiments/EXP001/RESULTS.md) scaffold, all committed and pushed before any data examination; the manual build has not started |
| Discoveries | None. Correct: no evidence has been produced |
| Software | None. Deliberate: [DEC001](decisions/DEC001-no-software-before-method.md) prohibits custom software until the manual method proves itself |
| Sessions | S000-S003; S004 retained with a provenance correction; S005 records the second valid AC001 test |

The framework is deliberately "method before automation"
([RG001](governance/rules/RG001-automation-follows-stability.md)). The next
milestone is not code — it is executing
[EXP001](experiments/EXP001/EXP001-momentum-replication.md) manually, starting
with the workbook verification in its
[step-2 recipe](experiments/EXP001/evidence/derived/step2-spreadsheet-recipe.md),
and keeping its [execution log](experiments/EXP001/evidence/execution-log.md)
honest about what the process costs.

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
10. [experiments/EXP001/EXP001-momentum-replication.md](experiments/EXP001/EXP001-momentum-replication.md) — the first experiment, and what the framework looks like under load

---

# Structure

The repository organizes knowledge by maturity. Information flows from raw
concepts to trusted knowledge as confidence increases.

| Directory | Role | Current contents |
|-----------|------|------------------|
| [principles/](principles/) | Timeless beliefs | PR001-PR005 |
| [research/](research/README.md) | Foundational concepts and research documents | research-000 to 003; sessions/ |
| [questions/](questions/README.md) | Structured uncertainties and observations | Q001, Q003 draft; Q002 deprecated |
| [hypotheses/](hypotheses/) | Testable claims | H000, H001 |
| [experiments/](experiments/README.md) | Investigations and their evidence | EXP001 (design accepted; computation phase pre-registered; not executed) |
| [discoveries/](discoveries/README.md) | Evidence-backed findings | Empty — no evidence produced yet |
| [decisions/](decisions/) | Operational and architectural decisions | DEC001 |
| [sources/](sources/README.md) | Registered external sources (papers, sites, datasets) | SRC001-SRC005, cited by EXP001 |
| [governance/](governance/README.md) | Long-term project rules and agent contracts | G000-G006, rules RG001-RG009, templates, agent contracts, manifest, registry |
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

## Questions

| ID | Title | Status | Location |
|----|-------|--------|----------|
| Q001 | Conditional Mean Reversion in AUDCAD, AUDNZD, and NZDCAD | draft | [questions/Q001-conditional-mean-reversion-aud-crosses.md](questions/Q001-conditional-mean-reversion-aud-crosses.md) |
| Q002 | Invalid Assistant-Generated Crypto Idea | deprecated | [questions/Q002-crypto-relative-mean-reversion.md](questions/Q002-crypto-relative-mean-reversion.md) |
| Q003 | Long-Only Trend Following in Gold | draft | [questions/Q003-long-only-gold-trend-following.md](questions/Q003-long-only-gold-trend-following.md) |

## Principles

| ID | Title | Status | Location |
|----|-------|--------|----------|
| PR001 | Repository as Source of Truth | active | [principles/repository-as-source-of-truth.md](principles/repository-as-source-of-truth.md) |
| PR002 | Data Provenance and Fitness Evidence | active | [principles/PR002-data-provenance-and-fitness.md](principles/PR002-data-provenance-and-fitness.md) |
| PR003 | Raw Data Immutable, Derived Data Traceable | active | [principles/PR003-raw-data-immutable-derived-traceable.md](principles/PR003-raw-data-immutable-derived-traceable.md) |
| PR004 | Architecture Is Not Implementation Plan | active | [principles/PR004-architecture-not-implementation-plan.md](principles/PR004-architecture-not-implementation-plan.md) |
| PR005 | AI Is Part of the Operating Model | active | [principles/PR005-ai-in-operating-model.md](principles/PR005-ai-in-operating-model.md) |

## Hypotheses

| ID | Title | Status | Confidence | Location |
|----|-------|--------|------------|----------|
| H000 | Project Should Not Exist | active | 0.8 | [hypotheses/H000-project-should-not-exist.md](hypotheses/H000-project-should-not-exist.md) |
| H001 | Edge is an Emergent Property | active | 0.5 | [hypotheses/H001-edge-is-emergent.md](hypotheses/H001-edge-is-emergent.md) |

## Experiments

| ID | Title | Status | Executed | Tests | Location |
|----|-------|--------|----------|-------|----------|
| EXP001 | Manual Replication of a Published Momentum Anomaly | active | no | H001 (sub-claim C1) | [experiments/EXP001/EXP001-momentum-replication.md](experiments/EXP001/EXP001-momentum-replication.md) |

## Decisions

| ID | Title | Status | Location |
|----|-------|--------|----------|
| DEC001 | No Software Before Method | accepted | [decisions/DEC001-no-software-before-method.md](decisions/DEC001-no-software-before-method.md) |

## Sources

Registered external sources that project artifacts cite
([RG009](governance/rules/RG009-claim-provenance.md)). See
[sources/README.md](sources/README.md) for conventions.

| ID | Title | Status | Location |
|----|-------|--------|----------|
| SRC001 | Time Series Momentum (Moskowitz, Ooi & Pedersen, 2012) | active | [sources/SRC001-moskowitz-ooi-pedersen-2012-time-series-momentum.md](sources/SRC001-moskowitz-ooi-pedersen-2012-time-series-momentum.md) |
| SRC002 | Absolute Momentum (Antonacci, 2013) | active | [sources/SRC002-antonacci-2013-absolute-momentum.md](sources/SRC002-antonacci-2013-absolute-momentum.md) |
| SRC003 | A Century of Evidence on Trend-Following Investing (Hurst, Ooi & Pedersen, 2017) | active | [sources/SRC003-hurst-ooi-pedersen-2017-century-of-evidence.md](sources/SRC003-hurst-ooi-pedersen-2017-century-of-evidence.md) |
| SRC004 | Shiller US Stock Market Data (ie_data.xls) | active | [sources/SRC004-shiller-ie-data-monthly-stock.md](sources/SRC004-shiller-ie-data-monthly-stock.md) |
| SRC005 | FRED TB3MS — 3-Month Treasury Bill Secondary Market Rate, Monthly | active | [sources/SRC005-fred-tb3ms-monthly.md](sources/SRC005-fred-tb3ms-monthly.md) |
| SRC006 | Dukascopy Bank Historical Data Export | active | [sources/SRC006-dukascopy-historical-data-export.md](sources/SRC006-dukascopy-historical-data-export.md) |

## Sessions

| ID | Title | Status | Location |
|----|-------|--------|----------|
| S000 | Project Zero (founding) | completed | [research/sessions/S000-project-zero.md](research/sessions/S000-project-zero.md) |
| S001 | Framework Hardening | completed | [research/sessions/S001-framework-hardening.md](research/sessions/S001-framework-hardening.md) |
| S002 | First Experiment Design | completed | [research/sessions/S002-first-experiment-design.md](research/sessions/S002-first-experiment-design.md) |
| S003 | Question / Observation Workflow Test | completed | [research/sessions/S003-question-observation-workflow.md](research/sessions/S003-question-observation-workflow.md) |
| S004 | Second Question Formulation Test (provenance corrected) | completed | [research/sessions/S004-question-formulation-second-test.md](research/sessions/S004-question-formulation-second-test.md) |
| S005 | Gold Question Formulation Test | completed | [research/sessions/S005-gold-question-formulation-test.md](research/sessions/S005-gold-question-formulation-test.md) |
| S006 | Project Principles Elevated to First-Class Artifacts | completed | [research/sessions/S006-project-principles-as-artifacts.md](research/sessions/S006-project-principles-as-artifacts.md) |

## Templates

| ID | Title | Status | Location |
|----|-------|--------|----------|
| ART-QUESTION-OBSERVATION | Question / Observation | draft | [governance/templates/question-observation.md](governance/templates/question-observation.md) |

## Agent Contracts

| ID | Title | Status | Location |
|----|-------|--------|----------|
| AC001 | Question Formulation Agent Contract (v1.1) | draft | [governance/agent-contracts/AC001-question-formulation.md](governance/agent-contracts/AC001-question-formulation.md) |

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
| RG007 | Governed Work Records Its Governance | active | [governance/rules/RG007-governance-execution.md](governance/rules/RG007-governance-execution.md) |
| RG008 | Artifact Authorship and Production-Tool Provenance | active | [governance/rules/RG008-authorship-provenance.md](governance/rules/RG008-authorship-provenance.md) |
| RG009 | Claim Provenance | active | [governance/rules/RG009-claim-provenance.md](governance/rules/RG009-claim-provenance.md) |

Templates for creating new artifacts and rules live in
[governance/templates/](governance/templates/). The machine-readable index is
[governance/artifact-registry.json](governance/artifact-registry.json) and the
effective rulebook is [governance/manifest.json](governance/manifest.json).

---

# Creating a New Artifact

Every new artifact follows the same procedure:

1. **Determine the type and identity.** Use the appropriate ID family:
   research-NNN, Q (question), H (hypothesis), EXP (experiment), DEC (decision),
   S (session), AC (agent contract), G (governance), RG (rule), SRC (external source). Identities are stable forever
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
