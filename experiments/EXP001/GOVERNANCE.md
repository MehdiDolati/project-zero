# EXP001 Governance Record

This file records the governance that applied to EXP001 at implementation time.

It is not a restatement of the governing artifacts. It is the record that makes
them reconstructable by identity and version, by any person or agent taking over
the work later.

See [RG007](../../governance/rules/RG007-governance-execution.md).

---

## Manifest snapshot in force

This work was carried out under the governance manifest at:

- **manifest-version**: 1.0.0
- **effective-as-of**: 2026-09-05
- **path**: `governance/manifest.json`

If the manifest is regenerated later with a new version, this record is left
explicit as the historical snapshot. It is not overwritten to match whatever
the current manifest says.

---

## Governing artifacts

The following artifacts governed the design of EXP001. They are referenced by
stable identity and version, not by file path alone.

| Artifact ID | Title | Version | Status | Path |
|-------------|-------|---------|--------|------|
| G001 | Research Governance | 1.0 | active | governance/G001-research-governance.md |
| G003 | Artifact Model | 1.0 | active | governance/G003-artifact-model.md |
| G004 | Artifact Lifecycle | 1.1 | active | governance/G004-artifact-lifecycle.md |
| G005 | Traceability Model | 1.1 | active | governance/G005-traceability.md |
| G006 | Relationships Model | 1.0 | active | governance/G006-relationships.md |
| RG001 | Automation Follows Stable Manual Practice | 1.0 | active | governance/rules/RG001-automation-follows-stability.md |
| RG002 | Use Normative Keywords | 1.0 | active | governance/rules/RG002-normative-keywords.md |
| RG003 | Stable Artifact Identity | 1.0 | active | governance/rules/RG003-artifact-identity.md |
| RG004 | Relationships are First-Class | 1.0 | active | governance/rules/RG004-first-class-relationships.md |
| RG005 | Benchmark Before Innovation | 1.0 | active | governance/rules/RG005-benchmark-before-invention.md |
| RG007 | Governed Work Records Its Governance | 1.0 | active | governance/rules/RG007-governance-execution.md |

## How each governing artifact was satisfied

| Artifact | How it applies to EXP001 |
|----------|--------------------------|
| G001 | The experiment references hypotheses (H001, H000), defines success and failure criteria, records assumptions and methodology, and designates immutable evidence storage. |
| G003 | EXP001 is a typed artifact with stable identity, metadata, relationships, and declared representations. |
| G004 | Current lifecycle state is `draft` (design written, not executed). Transition to `active` requires execution and review. |
| G005 | The chain research-001 → H001 → EXP001 → evidence → decision is declared and reconstructable. |
| G006 | Relationships use only the canonical vocabulary; the not-yet-existing evidence link is marked `[planned]`. |
| RG001 | Execution is manual, spreadsheet-only. No software is written. |
| RG002 | MUST / MUST NOT / SHOULD are used normatively in the design. |
| RG003 | Identity `EXP001` is fixed and independent of the filename. |
| RG004 | Relationships are declared under `# Relationships` with type and identity. |
| RG005 | A published, widely replicated anomaly is used as the benchmark before any original signal is proposed. |
| RG007 | This record. |

---

## Referenced but not governing

These artifacts are referenced by EXP001 as subject matter or context, not as
governance:

| Artifact ID | Role in EXP001 |
|-------------|----------------|
| H001 | Hypothesis under test (via sub-claim C1) |
| H000 | Hypothesis informed by the process metrics |
| research-001 | Source of the problem decomposition referenced in assumptions |
| research-002 | Conceptual definition of edge |
| research-003 | Methodology whose loop the experiment exercises |
| DEC001 | Decision that constrains the experiment to manual execution |

DEC001 is listed here rather than above because it is a decision, not a
governance artifact; it is made operational by RG001, which is listed as
governing.

---

## Artifact resolution

If a file listed above is renamed or moved, resolve it through
`governance/artifact-registry.json` by artifact ID. Do not assume the file is
gone.

---

## Exceptions and deliberate out-of-scope items

Record here any exception, waiver, or deliberate decision to operate outside a
governing rule, including what was excepted, why, and who authorized it if
authorization is required.

- **Deliberate scope limit, not an exception:** EXP001 tests sub-claim C1, not
  H001 in full. H001 is a system-level claim and no single experiment can settle
  it. This is recorded so that a later reader does not mistake a C1 result for
  an H001 verdict.
- No waivers against any governing rule at this time.

---

## Notes

- This record is updated when the work itself is reviewed under a new manifest
  version, or when the governing set changes in a way that affects this work.
- This record is not updated silently to match a newer manifest without an
  explicit note. Historical records remain historical records.

---

## Last updated

- **date**: 2026-09-06
- **by**: S002 — first experiment design
- **manifest-version**: 1.0.0
