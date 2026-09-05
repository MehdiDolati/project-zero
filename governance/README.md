# Governance

Governance defines how Project Zero preserves consistency, quality, and
long-term integrity. Its purpose is not controlling contributors; it is
protecting the research process ([G000](G000-governance-model.md)).

Governance distinguishes layers of different strength:

- **Principles** — timeless beliefs (e.g., repository as source of truth).
- **Policies** — high-level operational intentions.
- **Rules** — concrete, verifiable requirements written with normative
  keywords ([RG002](rules/RG002-normative-keywords.md)).
- **Constraints** — non-negotiable boundaries.
- **Recommendations** — good practices that are not mandatory.

Governance is not exempt from evidence. Governance changes follow the same
research methodology as everything else.

---

# Governance Documents (G000-G006)

| ID | Title | Purpose |
|----|-------|---------|
| [G000](G000-governance-model.md) | Governance Model | Layers of governance and how governance evolves |
| [G001](G001-research-governance.md) | Research Governance | Minimum standards for research artifacts (hypotheses, experiments, evidence, decisions) |
| [G002](G002-documentation-governance.md) | Documentation Governance | Ownership, lifecycle, and update rules for documentation |
| [G003](G003-artifact-model.md) | Artifact Model | Artifacts as the fundamental unit of project knowledge |
| [G004](G004-artifact-lifecycle.md) | Artifact Lifecycle | Common lifecycle states and transitions for all artifacts |
| [G005](G005-traceability.md) | Traceability Model | How knowledge chains are traced to origin and evidence |
| [G006](G006-relationships.md) | Relationships Model | Canonical relationship types and representation rules |

---

# Rules (RG001-RG007)

| ID | Title | Requirement |
|----|-------|-------------|
| [RG001](rules/RG001-automation-follows-stability.md) | Automation Follows Stable Manual Practice | Automation MUST only follow a validated manual process |
| [RG002](rules/RG002-normative-keywords.md) | Use Normative Keywords | Governance MUST use MUST / SHOULD / MAY consistently |
| [RG003](rules/RG003-artifact-identity.md) | Stable Artifact Identity | Knowledge MUST be an artifact with stable identity |
| [RG004](rules/RG004-first-class-relationships.md) | Relationships are First-Class | Relationships MUST be explicit and typed |
| [RG005](rules/RG005-benchmark-before-invention.md) | Benchmark Before Innovation | Established practice SHOULD be studied first |
| [RG006](rules/RG006-persist-agreed-rules.md) | Persist Agreed Rules | Accepted rules MUST be persisted in the repository |
| [RG007](rules/RG007-governance-execution.md) | Governed Work Records Its Governance | Every implementation MUST record the governance that applied to it |

---

# Templates

- [artifact-template.md](templates/artifact-template.md) — starting point for any new artifact
- [rule-template.md](templates/rule-template.md) — starting point for a new governance rule

Templates define the required frontmatter (id, type, title, status, version,
owner, created, last-reviewed) and the body sections expected of a complete
artifact. A new artifact copies the template and fills it; it is never created
from memory alone.

---

# The Artifact Lifecycle at a Glance

Every artifact moves through the same states
([G004](G004-artifact-lifecycle.md)):

Draft → Review → Active → Deprecated → Archived

- Identity never changes.
- Transition from draft to active requires acceptance.
- Deprecated and archived artifacts remain available for traceability.

---

# Reading This Repository Without Prior Context

This governance layer exists so that any person or agent can take over any
piece of work without relying on undocumented convention or tribal knowledge.

The entry points are, in order:

1. The task's own **governance record** (for experiments, the
   `GOVERNANCE.md` inside the experiment folder). That record says what the
   work is governed by.
2. The **governance manifest** (`governance/manifest.json`), which resolves
   the governing artifact identities to their current versions and status.
3. The **artifact registry** (`governance/artifact-registry.json`), which
   resolves artifact identities to their canonical files.
4. The governing **artifacts themselves**, read in full.

The single most important convention is that governance is addressed by
**stable identity + version**, never by filename or folder alone. Files move;
identities and versions do not. If a file you are looking for has been
renamed or relocated, resolve it through the registry or the manifest rather
than assuming it vanished.

---

# How Governance Changes

1. **Propose** the change as a draft artifact or rule (use the templates).
2. **Benchmark** existing practice before inventing a new rule
   ([RG005](rules/RG005-benchmark-before-invention.md)).
3. **Review** against evidence.
4. **Accept** the change (move to active) and update this README, the root
   [artifact registry](../README.md#artifact-registry), and the
   [governance manifest](manifest.json).
5. **Record** the change in a session, since governance changes are always
   significant project events ([G001](G001-research-governance.md)).

---

# Effective Rulebook

The [governance manifest](manifest.json) is the machine-readable snapshot of
the current active governance.

It records which artifact identities are active and at which version.
It is the reference point that governed work uses to declare what governed it.

When a new agent or person takes over a task, they read the task's governance
record first. That record points to the manifest snapshot that was in force at
the time, which in turn resolves every governing artifact by stable identity
and version. The underlying files may move or be reorganized; the identities
and versions in the manifest and the governed-work record are what preserve
traceability ([G005](G005-traceability.md)).

The manifest is updated whenever active governance changes. It is not
a substitute for reading the governing artifacts themselves; it is the index
that makes reading them reproducible and bounded. For the operational rules
that govern how governance changes, version bumps, deprecation, and
enforcement work, see [RG007](rules/RG007-governance-execution.md).
