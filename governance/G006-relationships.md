---
id: G006
type: governance

title: Relationships Model

status: active
version: 1.0

owner: Project Zero

created: 2026-07-28
last-reviewed: 2026-09-04
---

# Purpose

Define how relationships between Artifacts are represented and governed.

Artifacts do not exist in isolation. Knowledge is created by the connections
between Artifacts. Relationships make those connections explicit, typed, and
traceable.

This model operationalizes the traceability requirements defined in G005 and
the relationship requirements defined in RG004.

---

# Principles

- Relationships are first-class elements of the knowledge model, not
  documentation convenience.
- Every relationship MUST have an explicit type.
- Relationships MUST reference Artifacts by stable identity, not by file path.
- Relationship direction MUST be meaningful and consistently applied.
- Removing an Artifact MUST NOT silently break the relationships it
  participates in.

---

# Relationship Vocabulary

The following relationship types form the canonical vocabulary of Project Zero.

| Type | Meaning | Example |
|------|---------|---------|
| motivates | Source raises the question addressed by the target. | Question -> Hypothesis |
| derives-from | Target originates from the content or reasoning of the source. | Hypothesis -> Research Concept |
| depends-on | Target requires the source to be meaningful or valid. | Experiment -> Hypothesis |
| tested-by | Source is examined by the target. | Hypothesis -> Experiment |
| produces | Source generates the target. | Experiment -> Evidence |
| supports | Source increases confidence in the target. | Evidence -> Decision |
| challenges | Source decreases confidence in the target. | Evidence -> Hypothesis |
| supersedes | Target replaces the source. | Decision -> Prior Decision |
| creates | Source brings the target into existence. | Decision -> Rule |
| enforced-by | Source is made operational by the target. | Rule -> Governance |
| related-to | Source and target are connected without one of the above meanings. | Concept -> Concept |

The relationship types above are normative for new Artifacts.

Additional types MAY be introduced only with explicit justification and MUST
be registered in this document before use.

---

# Direction

Each relationship type has a canonical direction.

- derives-from, depends-on, tested-by, and related-to are symmetric in meaning
  but MUST be expressed from the dependent or derived Artifact toward its
  origin whenever practical.
- motivates, produces, supports, challenges, supersedes, creates, and
  enforced-by are directional and MUST point from source to target.

Backward traceability MUST always be possible. When an Artifact declares
`depends-on: H001`, H001 SHOULD be discoverable as a dependency even if it
does not declare the inverse relationship.

---

# Representation

Relationships MUST be represented explicitly in the Artifact body under a
`# Relationships` heading using the following form:

```
# Relationships

- derives-from: research/002-edge.md (research-002)
- tested-by: experiments/EXP001-proposal.md (EXP001) [planned]
```

Each entry consists of:

- the relationship type,
- a relative path to the physical representation,
- the stable Artifact identity in parentheses.

A relationship whose target does not yet exist MAY be marked `[planned]` so
that future validation can distinguish an intended link from a broken one.

---

# Requirements

Every Artifact SHOULD declare at least one relationship.

Every new Artifact MUST declare its immediate dependencies.

Orphan Artifacts, defined as Artifacts with no declared relationships, SHOULD
be treated as governance issues.

The complete traceability chain Question -> Hypothesis -> Experiment ->
Evidence -> Decision -> Rule -> Implementation SHOULD remain reconstructible
through declared relationships.

---

# Review

The vocabulary SHOULD be reviewed whenever:

- a new Artifact type is introduced,
- an existing relationship type proves ambiguous in practice,
- the repository structure changes.

---

# Future Automation

Future validators SHOULD detect:

- relationships referencing unknown Artifact identities,
- relationships without a type,
- broken paths,
- orphan Artifacts,
- relationship types not registered in this document.

---

# Related Artifacts

- G003-artifact-model.md (G003)
- G005-traceability.md (G005)
- governance/rules/RG004-first-class-relationships.md (RG004)
- governance/rules/RG003-artifact-identity.md (RG003)

---

# Revision History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | 2026-09-04 | Initial version. Fills the placeholder created on 2026-07-28. |
