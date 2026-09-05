---
id: RG007
type: rule

title: Governed Work Records Its Governance

status: active
version: 1.0

owner: Project Zero

created: 2026-09-05
last-reviewed: 2026-09-05

---

# Purpose

Make governance traceable at the level that matters: an individual piece of
work and the exact artifacts that governed it at the time it was done.

This rule closes the gap between "we have governance" and "we can reconstruct
what governed a specific task in the future." Without it, governance exists as
documents, but governed work does not necessarily record which documents
applied, at which version, or against which manifest snapshot.

---

# Statement

Every piece of governed work MUST record the governance that applied to it.

- The governance record MUST reference governing artifacts by stable identity
  and version, not by filename or folder.
- The governance record MUST reference the governance manifest snapshot that
  was in force at the time the work was done.
- The governance record MUST be stored with the work it governs, not only in
  the governance folder.
- The governance record SHOULD distinguish governing artifacts from artifacts
  that the work merely references.
- When a piece of governed work is later reviewed or superseded, the governance
  record SHOULD be updated to reflect the then-current governance, or left
  explicit as historical record with a note, not silently overwritten.

---

# Rationale

Git commit hashes give point-in-time reproducibility of files, but they are a
poor interface for governance.

A commit can touch unrelated files. "This work was governed by commit
abc123" is therefore ambiguous: it does not tell you which rules applied, at
which version, or whether those rules were active at all.

The practical question this rule exists to answer is: "what version of which
rule governed this work when it was implemented?" That question must be
answerable without archaeology, by any person or agent taking over later.

This rule is one half of a pair. The other half is the governance manifest
(`governance/manifest.json`), which is the effective rulebook — the set of
artifact identities and versions that are currently active. This rule says that
work records what governed it. The manifest says what the current rulebook is.
Together they make point-in-time reconstruction real.

---

# Applies To

- Experiments
- Implementations
- Any artifact whose content is intended to be governed by project rules,
  policies, or other governance artifacts

---

# How It Works

## The governance manifest

The governance manifest is a machine-readable snapshot of the current active
governance. It is maintained in `governance/manifest.json`.

It records, for each active artifact identity, the current version and status.

It is the reference point that governed work points to. A governed-work record
says, in effect: "this work was done under the rulebook captured by manifest
version X, and specifically under these artifacts at these versions."

## The governed-work record

Each governed piece of work carries a governance record. For experiments, this
is the `GOVERNANCE.md` file in the experiment's folder.

A governance record minimally records:

- the governing artifact identities and versions that applied,
- the governance manifest version or snapshot reference in force at the time,
- whether any exceptions, waivers, or deliberate out-of-scope items apply,
- and a pointer to where the full governing artifacts live.

A governance record does not need to restate the contents of the governing
artifacts. It needs to make them reconstructable and bounded.

## Version pins, not path pins

Governance records pin artifacts by identity and version, for example:

- `RG002` at version `1.0`
- `G005` at version `1.1`

They do not pin by file path alone. A file may be renamed or relocated later.
The identity and version are what survive.

## Deprecation and supersession

When an artifact is deprecated or superseded, the replacing artifact SHOULD be
recorded. Historical governance records that point to the superseded version
remain valid as historical record. They do not need to be rewritten, but they
SHOULD be left explicit rather than silently changed.

Deprecated artifacts remain available for traceability. This is not optional;
silently removing or rewriting the artifact that an earlier governance record
points to is exactly what this rule exists to prevent.

## Exception and waiver recording

If a piece of work deliberately operates outside a governing rule, or with an
exception, that exception MUST be recorded in the governance record, including
what was excepted, why, and who authorized it if authorization is required.

---

# Relationships

- enforces-by:
  - governance/manifest.json (manifest) — the current effective rulebook
- applies-to:
  - experiments/EXP001/GOVERNANCE.md — expected shape of a governed-work record
- related-to:
  - governance/G003-artifact-model.md (G003)
  - governance/G005-traceability.md (G005)
  - governance/G004-artifact-lifecycle.md (G004)
- derives-from:
  - governance/G000-governance-model.md (G000)

---

# Exceptions

None.

---

# Enforcement

Current enforcement:

- Manual

Compliance is verified by checking that governed work carries a governance
record that pins artifacts by identity and version and references the manifest
snapshot in force at the time.

Future automation MAY validate:

- absence of a governance record on governed work,
- references to artifact identities that are not in the registry,
- references to versions that do not match the manifest at the time claimed,
- superseded artifacts referenced without noting the supersession.

---

# Review

This rule SHOULD be reviewed when:

- the manifest format changes,
- the registry format changes,
- the governed-work record format changes,
- a real case shows that the rule does not actually answer the traceability
  question it exists for.

---

# Revision History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | 2026-09-05 | Initial version. |
