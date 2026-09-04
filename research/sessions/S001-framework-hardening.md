---
id: S001
type: session

title: Framework Hardening

status: completed
version: 1.0

owner: Project Zero

created: 2026-09-04
last-reviewed: 2026-09-04
---

# Session Objective

Audit the repository against its own governance model and bring the framework
to a self-consistent state: complete governance, normalized artifact metadata,
resolved duplication, and accurate documentation.

This was a framework session, not a research session. No trading hypothesis
was tested; the research pipeline remains unexercised.

---

# Findings

The audit found the following issues:

1. governance/G006-relationships.md was an empty placeholder file, created on
   2026-07-28 and never written.
2. G004 (Artifact Lifecycle) and G005 (Traceability Model) were stuck in
   `draft` with unfilled `created: YYYY-MM-DD` dates.
3. research-002 and H001 carried the same hypothesis content under different
   identities and locations, creating ambiguity about which was canonical.
4. Frontmatter was inconsistent with the artifact template: many artifacts
   lacked `type`, `version`, or `owner`, and the review date key appeared both
   as `last_reviewed` and `last-reviewed`.
5. RG004 referenced a nonexistent "G006-traceability-model (future)" even
   though the traceability model is G005.
6. The root README was a stale directory tree; governance, experiments, and
   discoveries had no READMEs despite being referenced by the research README;
   the principles file carried no artifact identity.
7. No artifact registry existed, making the artifact inventory implicit.

---

# Decisions Made

- G006 is filled as the canonical Relationships Model and activated.
- G004 and G005 are promoted from draft to active with completed metadata.
- research-002 is the conceptual edge definition (type: document); H001 is
  the canonical falsifiable hypothesis. When they disagree, H001 prevails.
- Frontmatter is normalized project-wide to the template keys (including
  `last-reviewed`), with `type`, `version: 1.0`, and `owner: Project Zero`
  added where missing.
- The principles file receives identity PR001 so it satisfies RG003.
- Empty directories (experiments, discoveries, software) are documented as
  intentionally empty rather than omitted.
- The root README becomes the project entry point and authoritative artifact
  registry.

---

# Artifacts Created

- governance/G006-relationships.md (G006) — content written
- governance/README.md — governance index
- experiments/README.md — experiment index (empty by design)
- discoveries/README.md — discovery index (empty by design)
- software/README.md — software index (empty by design)
- README.md — rewritten as entry point with artifact registry
- research/sessions/S001-framework-hardening.md (S001) — this session

---

# Artifacts Modified

- research/000-north-star.md (research-000) — frontmatter, relationships
- research/001-problem-definition.md (research-001) — frontmatter, relationships
- research/002-edge.md (research-002) — reframed as conceptual definition
- research/003-research-methodology.md (research-003) — frontmatter, relationships
- hypotheses/H000-project-should-not-exist.md (H000) — frontmatter, relationships
- hypotheses/H001-edge-is-emergent.md (H001) — frontmatter, relationships
- decisions/DEC001-no-software-before-method.md (DEC001) — frontmatter, relationships
- research/sessions/S000-project-zero.md (S000) — frontmatter, relationships
- governance/G000-G005 — frontmatter normalization; G004/G005 activated
- governance/rules/RG001-RG006 — frontmatter normalization; dangling references fixed
- principles/repository-as-source-of-truth.md (PR001) — identity added
- research/README.md — status note for empty pipeline directories

---

# Outcome

The framework is now self-consistent with its own governance: every artifact
carries complete, normalized metadata; relationships are typed and traceable;
empty pipeline stages are intentional and documented; and the root README
registers every artifact.

The natural next step is the first manual experiment (EXP001) designed to test
H001 — executed manually before any automation, per DEC001.

---

# Relationships

- related-to: governance/G000-governance-model.md (G000)
- related-to: governance/G003-artifact-model.md (G003)
- related-to: governance/G004-artifact-lifecycle.md (G004)
- related-to: governance/G005-traceability.md (G005)
- related-to: governance/G006-relationships.md (G006)
- related-to: governance/rules/RG003-artifact-identity.md (RG003)
- related-to: governance/rules/RG004-first-class-relationships.md (RG004)
- related-to: research/003-research-methodology.md (research-003)
