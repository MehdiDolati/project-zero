---
id: S006
type: session
title: Project Principles Elevated to First-Class Artifacts
status: completed
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
created-at: 2026-09-30T11:30:00+03:30
---

# Session Objective

Record the researcher's four stated project requirements — provenance and
fitness, immutability and traceability, architecture versus implementation,
and AI as part of the operating model — as first-class principle artifacts,
without violating the governance model's separation of concerns.

---

# What Was Done

- Added four principle artifacts under `principles/`:
  - PR002 — Data Provenance and Fitness Evidence
  - PR003 — Raw Data Immutable, Derived Data Traceable
  - PR004 — Architecture Is Not Implementation Plan
  - PR005 — AI Is Part of the Operating Model
- Removed the inline statement of these principles from
  [G001](../governance/G001-research-governance.md) and replaced it with a
  reference list, so that principles live only in the `principles/` layer and
  each has a single authoritative definition (per G003 and the artifact model).
- Bumped G001 to version 1.1 and updated `last-reviewed` to 2026-09-30.
- Registered PR002-PR005 in the Artifact Registry in
  [README.md](../../README.md) and updated the Structure table.
- Synchronized G001 to version 1.1 in
  [artifact-registry.json](../governance/artifact-registry.json) (registry
  version 1.19.0) and
  [manifest.json](../governance/manifest.json) (governance-version 1.4.0,
  effective 2026-09-30).

---

# What Was Learned

## Requirements can already be governance; capturing them must not duplicate it

Two of the four requirements were already operationalized by existing rules
(RG009 claim provenance, RG008 authorship/production-tool provenance) and by
G001's evidence requirements. The correct action was to add the principles as a
distinct layer and let them reference the rules, rather than restate rule text.
This preserves single-source-of-truth and avoids creating process for its own
sake.

## Principles are first-class artifacts

The governance model already treats principles as an artifact layer. The four
new requirements belong there with stable identities (PR002-PR005), not as
inline text inside a governance document.

---

# Decisions

- Represent the four requirements as principle artifacts PR002-PR005 with
  `status: active`.
- Keep each principle definition in exactly one place; G001 references them
  instead of restating them.
- Do not encode any principle as automation. PR005 (AI in the operating model)
  does not weaken RG001 (automation follows stable manual practice); AI work
  remains subject to the same evidence and provenance standards.

---

# Artifacts Created

- principles/PR002-data-provenance-and-fitness.md (PR002)
- principles/PR003-raw-data-immutable-derived-traceable.md (PR003)
- principles/PR004-architecture-not-implementation-plan.md (PR004)
- principles/PR005-ai-in-operating-model.md (PR005)
- research/sessions/S006-project-principles-as-artifacts.md (S006) — this session

# Artifacts Modified

- governance/G001-research-governance.md (G001) — replaced the inline
  principles with a reference list; version 1.0 → 1.1.
- governance/artifact-registry.json — registry version 1.19.0; G001 version
  synchronized to 1.1.
- governance/manifest.json — governance-version 1.4.0; G001 version
  synchronized to 1.1.
- README.md — registered PR002-PR005 in the Principles table, updated the
  Structure table, and added S006 to the Sessions table.

---

# Outcome

The four stated requirements are now first-class principle artifacts (PR002-PR005),
each with a single authoritative definition, registered in the Artifact Registry,
and referenced by Research Governance. No governance rule was contradicted: the
principles complement, rather than duplicate or override, the existing rules and
the evidence discipline. No hypothesis, experiment, or code was created.

---

# Relationships

- related-to: principles/repository-as-source-of-truth.md (PR001)
- related-to: principles/PR002-data-provenance-and-fitness.md (PR002)
- related-to: principles/PR003-raw-data-immutable-derived-traceable.md (PR003)
- related-to: principles/PR004-architecture-not-implementation-plan.md (PR004)
- related-to: principles/PR005-ai-in-operating-model.md (PR005)
- related-to: governance/G001-research-governance.md (G001)
- related-to: governance/rules/RG001-automation-follows-stability.md (RG001)
- related-to: governance/rules/RG008-authorship-provenance.md (RG008)
- related-to: governance/rules/RG009-claim-provenance.md (RG009)
- derives-from: research/003-research-methodology.md (research-003)