---
id: RG009
type: rule

title: Claim Provenance

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

Make knowledge that originates outside the repository traceable to its origin.

Project artifacts regularly rely on claims, definitions, specifications, and
data that come from published literature, websites, or datasets. Internal
traceability (G005, G006) connects project artifacts to each other, but it
cannot answer the question "where did this claim come from originally?" unless
external sources are themselves registered and citable. This rule closes that
gap.

---

# Statement

1. Every artifact whose content depends on a claim, definition, specification,
   name, or dataset that originates outside the repository MUST record that
   dependency using the `cites` relationship type registered in G006, pointing
   at a registered source artifact (ID family `SRC`, under `sources/`).

2. A source MUST be registered as a source artifact before it is cited. A
   source artifact MUST record at minimum:
   - the full citation (authors, title, venue or site, year, and DOI or URL
     where available; for informal media, the creator or channel name and the
     platform),
   - what the source claims, in the project's own words,
   - how the project uses it,
   - how the citation metadata was verified, and whether the full text has
     been read. Unverified details MUST be marked as such.

3. A replication experiment MUST cite the sources that document the effect it
   replicates and the source that defines the specification it follows. Where
   these differ, the experiment MUST state which source its specification is
   anchored to.

4. Design parameters or period boundaries that are justified by reference to
   published work MUST cite that work. Justifications such as "documented in
   the literature" without a citation MUST NOT appear in project artifacts.

5. Registered source artifacts SHOULD verify their citation metadata against
   the publisher's record or an equivalent authoritative source at
   registration time, and MUST record the verification method. If the full
   text has not been read, that MUST be stated; the project MUST NOT represent
   unread material as read.

### Original work

Ideas, questions, and hypotheses that originate inside the project do not
require citations. An artifact with no `cites` relationships is legitimate
whenever its content has no external dependency; absence of citations is not
a compliance failure.

Where a claim of novelty is load-bearing, the artifact SHOULD record that a
search for existing practice was performed and what it found, per
[RG005](RG005-benchmark-before-invention.md). This distinguishes an idea
unreferenced because nothing like it was found from an external dependency
that was never identified.

### Informal and volatile sources

A source does not need to be academic to be registered. A video, blog post,
forum thread, podcast, or dataset MAY be registered as a source artifact when
a project artifact relies on it. For such sources:

- the source kind MUST be recorded (e.g., paper, preprint, video, blog,
  dataset),
- the retrieval date MUST be recorded, and an archival snapshot (e.g.,
  web-archive URL) SHOULD be stored when practical, because volatile sources
  may change or disappear,
- where the source is not peer-reviewed, that MUST be stated plainly so that
  downstream work can weigh it accordingly.

An informal source supports exploration and benchmarking awareness; it does
not by itself establish that a practice is established or widely replicated
(RG005).

Normative keywords are used per [RG002](RG002-normative-keywords.md).

---

# Context

The gap was surfaced on 2026-09-09: [EXP001](../../experiments/EXP001/EXP001-momentum-replication.md)
— the project's foundational experiment — rested on "a published, widely
replicated anomaly" without naming a single paper, author, or URL. Data-file
provenance was already required (URL, retrieval date, hash), and authorship
provenance was formalized by RG008, but idea provenance was not required
anywhere. A project whose thesis is traceability of every claim could not trace
its most important external dependency.

The solution mirrors the approach taken for authorship (RG008): sources become
first-class artifacts with stable identity so that the existing relationship
machinery (G003, G006) applies to them unchanged.

---

# Rationale

- Unnamed sources make replication and audit impossible: a later researcher
  cannot check which version of a claim was relied on.
- Citing sources externally (in prose only) does not survive repository
  evolution; first-class artifacts make citations addressable by stable
  identity (RG003) and visible to future validation (G006 Future Automation).
- Distinguishing "the source that names the effect" from "the source that
  defines the specification" prevents a replication experiment from silently
  drifting from what its benchmark literature actually tested.
- Recording whether a source was actually read prevents over-claiming: citing
  a paper for a claim taken from its abstract is legitimate, but only when
  recorded as such.
- Requiring citations for internally generated ideas would add process
  overhead with no provenance value (G002); the rule triggers on external
  dependency, not on artifact creation.

---

# Applies To

- All research artifacts (questions, hypotheses, experiments, discoveries)
- Decisions that rely on external knowledge
- Governance artifacts when they justify requirements by external practice
- Evidence, at the data-source level (data-file provenance remains governed by
  G001)

---

# Exceptions

- General knowledge that a reasonable researcher could be assumed to hold
  (e.g., "compound returns accumulate geometrically") does not require a
  citation. If a dependency is contested or load-bearing, cite it.
- External sources that cannot be registered (e.g., a private conversation or
  an ephemeral chat message) MUST still be recorded in the citing artifact
  with whatever identity is available, and marked as unverifiable. A source
  with a stable URL (a video, blog post, or thread) is registrable and does
  not fall under this exception.

---

# Relationships

- creates: sources/README.md (SRC registry)
- enforces: governance/G005-traceability.md (G005, external chain origins)
- enforces: governance/G006-relationships.md (G006, `cites` type)
- enforces: governance/G001-research-governance.md (G001, evidence provenance)
- related-to: governance/rules/RG005-benchmark-before-invention.md (RG005)
- related-to: governance/rules/RG008-authorship-provenance.md (RG008)
- related-to: experiments/EXP001/EXP001-momentum-replication.md (EXP001)

---

# Representations

- Markdown (this artifact)

---

# Constraints

- Sources are referenced, not mirrored. A source artifact records metadata and
  usage; it MUST NOT reproduce the source's content in a way that substitutes
  for access to the source.
- Copyright: store citations and metadata, not copies of paywalled material.

---

# Review

This rule SHOULD be reviewed when:

- the first replication attempt reveals that the citation fields do not answer
  the provenance question in practice,
- the `cites` vocabulary proves ambiguous (e.g., datasets vs. papers),
- the sources directory conventions change,
- evidence emerges that citation discipline does or does not improve artifact
  quality.

---

# Enforcement

Current enforcement: manual.

Compliance is verified by review: any artifact using phrases like "published",
"documented in the literature", or "widely replicated" MUST carry `cites`
relationships resolving to registered source artifacts.

---

# Origin

Research process gap identified on 2026-09-09 during review of EXP001's
provenance. Originating artifact:
[governance/GOVPROV-2026-09-09-claim-provenance.md](../GOVPROV-2026-09-09-claim-provenance.md).

---

# Governed By / Manifest Snapshot

Accepted under governance manifest `governance/manifest.json` at
governance-version 1.3.0, effective-as-of 2026-09-09. Revised to v1.1 under
governance-version 1.3.1, same date.

---

# Revision History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | 2026-09-09 | Initial version. Requires external claims to be cited via registered SRC artifacts. |
| 1.1 | 2026-09-09 | Clarified that original, internally-originated work requires no citation; made informal and volatile sources (video, blog, forum) explicitly registrable with kind, retrieval date, and archival snapshot. |
