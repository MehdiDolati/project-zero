---
id: GOVPROV-2026-09-09-claim-provenance
type: governance-record

title: Claim Provenance Governance Implementation

status: active
version: 1.1

owner: Project Zero

created: 2026-09-09
last-reviewed: 2026-09-09

created-by-type: agent
created-by: AI assistant (Buffy) in Freebuff
created-by-version: not available
production-tools: Freebuff (Buffy coding agent), web search (Serper Google API)
created-at: 2026-09-09T15:52:19+03:30

---

# Purpose

Record the governance that applied to the creation of the claim-provenance
feature (RG009, G005 and G006 updates, the `sources/` registry, the artifact
template update, EXP001 v1.1, and this document).

This record follows the governance record pattern required by
[RG007](rules/RG007-governance-execution.md), as demonstrated by
[GOVPROV-2026-09-09](GOVPROV-2026-09-09.md).

---

# Context

A review of [EXP001](../experiments/EXP001/EXP001-momentum-replication.md) —
the project's foundational experiment — found that it relied on "published
literature" without naming a single paper, author, or URL. Data-file provenance
(URL, retrieval date, hash) was already required by G001, and authorship
provenance was formalized earlier the same day by RG008, but idea provenance —
where a claim, definition, or specification comes from — was required nowhere.

The gap meant:

- the origin of EXP001's central claim could not be traced,
- design parameters justified by "the literature" were unauditable,
- future validation (G006 Future Automation) had nothing to check citations
  against.

This session closes the gap by making external sources first-class artifacts.

---

# Governing Artifacts Applied

| ID | Title | Version | Status | Location |
|-----|-------|---------|--------|----------|
| G001 | Research Governance | 1.0 | active | governance/G001-research-governance.md |
| G002 | Documentation Governance | 1.0 | active | governance/G002-documentation-governance.md |
| G003 | Artifact Model | 1.0 | active | governance/G003-artifact-model.md |
| G005 | Traceability Model | 1.1 → 1.2 | active | governance/G005-traceability.md |
| G006 | Relationships Model | 1.0 → 1.1 | active | governance/G006-relationships.md |
| RG002 | Use Normative Keywords | 1.0 | active | governance/rules/RG002-normative-keywords.md |
| RG003 | Stable Artifact Identity | 1.0 | active | governance/rules/RG003-artifact-identity.md |
| RG004 | Relationships are First-Class | 1.0 | active | governance/rules/RG004-first-class-relationships.md |
| RG005 | Benchmark Before Innovation | 1.0 | active | governance/rules/RG005-benchmark-before-invention.md |
| RG008 | Artifact Authorship and Production-Tool Provenance | 1.0 | active | governance/rules/RG008-authorship-provenance.md |
| RG007 | Governed Work Records Its Governance | 1.0 | active | governance/rules/RG007-governance-execution.md |

---

# Governance Manifest Applied

Manifest version: 1.0.0
Governance version: 1.2.0 → 1.3.0
Effective-as-of: 2026-09-09

The work began under governance-version 1.2.0 and updated the manifest to
1.3.0 as part of the change.

---

# Artifacts Created or Modified

## New Artifacts

- `governance/rules/RG009-claim-provenance.md` (v1.0) — the rule: external
  claims MUST be cited via registered SRC artifacts.
- `sources/README.md` — SRC conventions and registry.
- `sources/SRC001-moskowitz-ooi-pedersen-2012-time-series-momentum.md` (v1.0) —
  Moskowitz, Ooi & Pedersen (2012), JFE 104(2), the paper that named
  time-series momentum.
- `sources/SRC002-antonacci-2013-absolute-momentum.md` (v1.0) — Antonacci
  (2013), SSRN 2244633, the published specification closest to EXP001's rule;
  the specification anchor.
- `sources/SRC003-hurst-ooi-pedersen-2017-century-of-evidence.md` (v1.0) —
  Hurst, Ooi & Pedersen (2017), JPM 44(1), century-scale documentation.
- This record.

## Modified Artifacts

- `governance/G006-relationships.md` — registered the `cites` relationship
  type (v1.0 → 1.1); external sources noted as first-class artifacts.
- `governance/G005-traceability.md` — external sources added as chain origins
  (v1.1 → 1.2).
- `governance/templates/artifact-template.md` — `cites` added to relationship
  examples; References section added.
- `experiments/EXP001/EXP001-momentum-replication.md` (v1.0 → 1.1) — cited
  SRC001–SRC003; re-anchored the IS/OOS boundary to 2013-12/2014-01 (the
  v1.0 boundary of 2005-12 predated every cited source); added RG008
  provenance fields. Changed before execution, while the specification was
  still frozen.
- `experiments/EXP001/GOVERNANCE.md` — revision v1.1 section added; SRC
  artifacts added to the referenced set.
- `experiments/README.md` — claim-provenance requirement added.
- `README.md` — sources section and registry rows added; RG009 registered;
  structure table and status snapshot updated.
- `GUIDE.md` — SRC ID family, `cites` vocabulary row, claim-provenance
  guidance.
- `governance/manifest.json` — RG009 added; G005/G006 versions updated;
  governance-version 1.3.0.
- `governance/artifact-registry.json` — RG009, SRC001–SRC003 added; EXP001
  bumped to 1.1 with `cites`; G005/G006 versions updated; **RG008 backfilled**
  (it had been added to the README table earlier the same day but omitted from
  this registry — a registration gap corrected here).

## Consistency corrections noted

- `governance/GOVPROV-2026-09-09.md` records G001 as bumped 1.0 → 1.1, but
  G001's front matter and manifest entry still say 1.0. G001's content does
  contain the authorship requirements, so the change itself landed; only the
  version numbering did not. Correcting G001's version here without its
  authorship would falsify the historical record; the discrepancy is therefore
  left visible and flagged for the G001 owner to reconcile in a G001-scoped
  change. The manifest continues to list G001 at 1.0.

---

# Exceptions or Waivers

None against governing rules. Two deliberate choices are recorded:

- The `SRC` ID family and `sources/` directory are introduced as new artifact
  infrastructure; the alternative (inline citations only) was rejected because
  relationships cannot point at inline text (G006, RG004).
- The `created-by` field for this session's artifacts records the Freebuff
  agent identity, consistent with RG008's requirement not to guess versions:
  `created-by-version: not available`.

---

# Rationale

- A traceability-first project must trace the origin of its claims, not only
  its internal artifact chains. EXP001's authority as a benchmark depends on
  which published claim it replicates.
- Registering sources as artifacts (rather than inline citations) reuses the
  existing identity, lifecycle, relationship, and validation machinery.
- Separating "names the effect" (SRC001), "defines the specification"
  (SRC002), and "documents the history" (SRC003) forces replication
  experiments to state exactly what they follow.
- EXP001's IS/OOS boundary was re-anchored **before execution** — while the
  specification was frozen and no data had been retrieved — so the change is a
  versioned design revision, not a result-driven adjustment.

---

# Addendum (v1.1, same day)

A follow-up question exposed an ambiguity: whether the new rule forces every
artifact to carry references. It does not, and the rule now says so:

- **Original work is citation-free by design.** Ideas, questions, and
  hypotheses originating inside the project require no `cites` relationships;
  absence of citations is not a compliance failure. Where novelty is
  load-bearing, the artifact SHOULD record that a benchmark search was
  performed (RG005).
- **Informal sources are registrable.** A video, blog post, or forum thread
  that an artifact relies on MAY be registered as a SRC artifact — no paper
  required. Such sources record their kind, retrieval date, and (where
  practical) an archival snapshot, and state plainly that they are not
  peer-reviewed.
- **Informal sources are not benchmarks of establishment.** An informal source
  supports exploration; it does not by itself establish that a practice is
  "established" or "widely replicated" under RG005.

Changes: RG009 1.0 → 1.1; `sources/README.md` conventions extended. Manifest
governance-version 1.3.0 → 1.3.1.

---

# Producer Notes

This change was produced by an AI agent (Buffy, via Freebuff) with source
metadata verified by web search against publisher and bibliographic records at
registration time. All three source artifacts state explicitly that full texts
were not read during registration, per RG009 statement 5.

---

# Revision History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | 2026-09-09 | Initial record. Establishes governance for RG009, the SRC registry, and EXP001 v1.1. |
| 1.1 | 2026-09-09 | Addendum: clarified citation-free original work and registrability of informal/volatile sources (RG009 v1.1, manifest 1.3.1). |
