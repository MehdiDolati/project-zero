# How to Use This Framework

A step-by-step guide to doing work in Project Zero — from framing a question to
persisting knowledge. This guide summarizes the rules; the governance documents
it cites are authoritative wherever the two disagree.

Who this is for: any contributor, human or AI, picking up work in this
repository. Nothing here requires software. In fact, the founding decision
[DEC001](decisions/DEC001-no-software-before-method.md) prohibits custom
software until the manual method proves itself, and
[RG001](governance/rules/RG001-automation-follows-stability.md) requires
automation to follow validated manual practice.

The one mental model to internalize first: **this repository does not manage
files, it manages artifacts** ([G003](governance/G003-artifact-model.md)).
An artifact is a uniquely identified, typed, versioned unit of knowledge
connected to other artifacts by explicit relationships. Every step below is a
variation on: create an artifact, connect it, register it.

---

## The Big Picture

Work flows through the research loop
([research-003](research/003-research-methodology.md)):

```
Question → Hypothesis → Experiment → Evidence → Decision → Knowledge → New Question
```

and artifacts live in directories by maturity:

```
research/     foundational concepts and sessions
hypotheses/   testable claims
experiments/  executed investigations
discoveries/  evidence-backed findings
decisions/    operational and architectural decisions
governance/   long-term project rules
```

Every artifact carries frontmatter metadata (id, type, title, status, version,
owner, created, last-reviewed), moves through one lifecycle
([G004](governance/G004-artifact-lifecycle.md)):

```
Draft → Review → Active → Deprecated → Archived
```

and declares relationships under a `# Relationships` heading using the
canonical vocabulary in [G006](governance/G006-relationships.md).

---

## Step 0 — Read the Foundation

Before creating anything, read the foundation in this order
([README.md](README.md#reading-order)):

1. [research/000-north-star.md](research/000-north-star.md) — why the project exists
2. [research/001-problem-definition.md](research/001-problem-definition.md) — what problem it addresses
3. [research/002-edge.md](research/002-edge.md) — how trading edge is understood
4. [research/003-research-methodology.md](research/003-research-methodology.md) — how research is conducted
5. [governance/README.md](governance/README.md) — how knowledge is governed
6. [hypotheses/H000-project-should-not-exist.md](hypotheses/H000-project-should-not-exist.md) — the kill-switch hypothesis
7. [hypotheses/H001-edge-is-emergent.md](hypotheses/H001-edge-is-emergent.md) — the central research hypothesis
8. [decisions/DEC001-no-software-before-method.md](decisions/DEC001-no-software-before-method.md) — the founding architectural decision

If you are taking over a specific task rather than onboarding, start instead
with that task's governance record (for experiments, the `GOVERNANCE.md` inside
the experiment folder), then resolve artifacts through
[governance/manifest.json](governance/manifest.json) and
[governance/artifact-registry.json](governance/artifact-registry.json).
Artifacts are addressed by **stable identity + version**, never by file path —
files move, identities do not ([RG003](governance/rules/RG003-artifact-identity.md),
[RG007](governance/rules/RG007-governance-execution.md)).

---

## Step 1 — Frame the Question or Hypothesis

Every piece of work starts from uncertainty worth reducing. Do not create an
artifact to satisfy process — artifacts exist to reduce uncertainty
([G002](governance/G002-documentation-governance.md)).

1. **Check existing knowledge first.** Search the artifact registry and
   existing hypotheses. Does a hypothesis already cover this? Is your idea a
   new hypothesis, or evidence for an existing one?
2. **Benchmark before inventing** ([RG005](governance/rules/RG005-benchmark-before-invention.md)).
   Study established practice before proposing something novel.
3. **Assign an identity.** ID families are: `research-NNN` (documents),
   `PR` (principles), `H` (hypotheses), `EXP` (experiments), `DEC` (decisions),
   `S` (sessions), `G` (governance), `RG` (rules). Take the next free number
   (e.g., `H002`). Identity is stable forever — it never changes, even if the
   file is renamed or moved.
4. **Name the file** `<ID>-<kebab-case-title>.md`, e.g.
   `hypotheses/H002-example-claim.md`, and place it in the directory matching
   its maturity.
5. **Copy the template** from
   [governance/templates/artifact-template.md](governance/templates/artifact-template.md)
   (or [rule-template.md](governance/templates/rule-template.md) for a rule) and
   fill in all required metadata:

   ```yaml
   ---
   id: H002
   type: hypothesis
   title: Example Claim
   status: draft
   version: 1.0
   owner: Project Zero
   created: 2026-09-06
   last-reviewed: 2026-09-06
   ---
   ```

6. **Make the hypothesis falsifiable** ([G001](governance/G001-research-governance.md)).
   A hypothesis MUST have a unique identifier, a falsifiable claim, at least
   one falsification criterion, a stated confidence, and a reference to the
   motivating question. See [H001](hypotheses/H001-edge-is-emergent.md) for the
   expected shape (Statement, Motivation, Predictions, Falsification Criteria,
   Current Confidence).

Two discovery paths are valid ([research-003](research/003-research-methodology.md)):
hypothesis-driven (the default) and serendipity-driven (an unexpected
observation). Serendipitous findings follow the exact same validation path —
an observation is not evidence, and evidence is not knowledge.

---

## Step 2 — Design the Experiment

The experiment is the atomic unit of learning. No claim becomes project
knowledge without experimental evidence ([research-003](research/003-research-methodology.md)).

1. Create `experiments/EXP00NN-<kebab-case-title>.md` from the artifact
   template, starting in `status: draft`.
2. Satisfy the experiment requirements ([G001](governance/G001-research-governance.md),
   [experiments/README.md](experiments/README.md)). The experiment MUST:
   - reference one or more hypotheses,
   - define success criteria,
   - define failure criteria,
   - preserve raw evidence,
   - record assumptions,
   - record methodology,
   - be reproducible.
3. **Record what governs the work** ([RG007](governance/rules/RG007-governance-execution.md)).
   Add a `GOVERNANCE.md` file inside the experiment folder containing:
   - the governing artifact identities and versions that applied (e.g.,
     `G001` at version `1.0`, `RG007` at version `1.0`),
   - the governance manifest snapshot in force at the time
     ([governance/manifest.json](governance/manifest.json) records
     `governance-version` and `effective-as-of`),
   - any exceptions or waivers, with justification,
   - pointers to where the governing artifacts live.

   Pin by identity + version, never by file path alone.

4. **Declare relationships** in the experiment body under `# Relationships`,
   using the canonical vocabulary from [G006](governance/G006-relationships.md):

   ```markdown
   # Relationships

   - tested-by: experiments/EXP001-proposal.md (EXP001)
   - depends-on: hypotheses/H001-edge-is-emergent.md (H001)
   - created-in: research/sessions/S002-example-session.md (S002) [planned]
   ```

   Format per entry: relationship type, relative path, stable identity in
   parentheses. Mark targets that do not exist yet with `[planned]`.

The first experiment must be executed manually — no automation
([DEC001](decisions/DEC001-no-software-before-method.md)).

---

## Step 3 — Execute and Record Evidence

1. Run the experiment as designed, following the recorded methodology.
2. **Preserve raw evidence** alongside the experiment. Evidence MUST originate
   from the experiment, remain immutable after creation, and preserve
   provenance ([G001](governance/G001-research-governance.md)). Never edit
   evidence after the fact — record corrections as new artifacts or notes.
3. Record negative results too. A failed experiment is a successful research
   outcome when preserved with its reasoning; it reduces uncertainty and
   prevents repeated mistakes.
4. Keep assumptions and deviations from the methodology explicit in the
   experiment record.

---

## Step 4 — Decide and Persist Knowledge

With evidence in hand, move up the knowledge maturity ladder
([research-003](research/003-research-methodology.md)):
Observation → Evidence → Claim → Knowledge.

1. **Evaluate** the evidence against the pre-declared success and failure
   criteria of the experiment. Resist post-hoc reframing of criteria.
2. **Update the hypothesis.** Revise its stated confidence and note which
   evidence supports or challenges it. A hypothesis that is rejected should be
   moved toward `deprecated` (not deleted) with its replacement referenced —
   rejecting a weak idea is successful research.
3. **Record a decision artifact** if the evidence justifies a decision.
   Every research decision MUST reference supporting evidence, explain
   rejected alternatives when applicable, state confidence, and identify
   remaining uncertainty ([G001](governance/G001-research-governance.md)).
4. **Record a discovery** when a claim has survived repeated evaluation and is
   trusted enough to influence future decisions. A discovery references its
   supporting experiments/evidence and decisions, states confidence and
   remaining uncertainty, and remains open to challenge
   ([discoveries/README.md](discoveries/README.md)).
5. **Update backward relationships.** Add or update links in the artifacts
   this work touched (e.g., the hypothesis gains
   `tested-by: experiments/EXP001-... (EXP001)`, replacing any `[planned]`
   marker). Backward traceability MUST always be possible
   ([G005](governance/G005-traceability.md)), and removing an artifact MUST NOT
   silently break relationships it participates in.

---

## Step 5 — Register Everything

An artifact that is not registered is not project knowledge. After creating or
materially changing an artifact:

1. **Register it in the root README's
   [Artifact Registry](README.md#artifact-registry)** — add a row to the table
   for its type (ID, title, status, confidence if applicable, location).
2. **Add it to [governance/artifact-registry.json](governance/artifact-registry.json)**
   (id, type, title, path, version, status) and bump `updated`.
3. **If it is an active governance artifact or rule**, add it to
   [governance/manifest.json](governance/manifest.json) as well, and update
   `effective-as-of` / `governance-version`. The manifest is the
   machine-readable effective rulebook that governed work points to.
4. **Check for orphans.** Every artifact SHOULD declare at least one
   relationship; an artifact with none is a governance issue
   ([G006](governance/G006-relationships.md)).

---

## Step 6 — Record a Session

Record a session under `research/sessions/` (next free `S` number) whenever any
of the following occurred ([G001](governance/G001-research-governance.md),
[G002](governance/G002-documentation-governance.md)):

- a major assumption changed,
- a governance rule changed,
- the methodology changed,
- a significant hypothesis was accepted or rejected,
- a strategic project decision was made.

A session is a snapshot of project evolution, not meeting minutes. It records:
important insights, changed beliefs, created artifacts, significant decisions,
and unresolved questions. Sessions preserve reasoning, not conversation.

---

## Step 7 — Close the Loop

1. **Set the artifact's status.** Move it `Draft → Review → Active` only when
   it has been evaluated and accepted ([G004](governance/G004-artifact-lifecycle.md)).
   Active artifacts may be referenced by others; deprecated and archived
   artifacts remain available for traceability and archived artifacts must not
   be modified.
2. **Ask the next question.** The evaluation should surface new uncertainty —
   that becomes the next question, hypothesis, or experiment.
3. **Review affected artifacts.** Artifacts SHOULD be reviewed whenever related
   artifacts change, new evidence arrives, governance evolves, or assumptions
   are invalidated; update `last-reviewed` when you do.

---

## Changing Governance Itself

Governance is not exempt from evidence. To change a rule or add one
([governance/README.md](governance/README.md#how-governance-changes)):

1. **Propose** it as a draft rule using
   [governance/templates/rule-template.md](governance/templates/rule-template.md).
   Write requirements with normative keywords MUST / SHOULD / MAY
   ([RG002](governance/rules/RG002-normative-keywords.md)).
2. **Benchmark** existing practice before inventing a new rule
   ([RG005](governance/rules/RG005-benchmark-before-invention.md)).
3. **Review** against evidence.
4. **Accept** it (status → active) and update the governance README, the root
   artifact registry, and the manifest.
5. **Record** the change in a session — governance changes are always
   significant project events.

---

## Cheat Sheet

**Creating a new artifact, end to end:**

- [ ] Checked the registry — this is genuinely new knowledge, not duplication
- [ ] Benchmarked established practice first (RG005)
- [ ] Stable identity assigned from the right ID family (RG003)
- [ ] File created from the template with complete frontmatter
- [ ] Content meets type-specific requirements (G001)
- [ ] Relationships declared under `# Relationships` with types and identities (RG004, G006)
- [ ] Governance record added for governed work (RG007)
- [ ] Registered in root README and `artifact-registry.json`
- [ ] Registered in `manifest.json` if governance (RG007)
- [ ] Backward links updated in affected artifacts (G005)
- [ ] Session recorded if triggers were hit (G001, G002)
- [ ] Status moved to active only after review (G004)

**Relationship vocabulary at a glance** ([G006](governance/G006-relationships.md)):

| Type | Points | Typical use |
|------|--------|-------------|
| motivates | source → target | Question → Hypothesis |
| derives-from | dependent → origin | Hypothesis → Research document |
| depends-on | dependent → dependency | Experiment → Hypothesis |
| tested-by | source → examiner | Hypothesis → Experiment |
| produces | source → output | Experiment → Evidence |
| supports | source → claim | Evidence → Decision |
| challenges | source → claim | Evidence → Hypothesis |
| supersedes | replacement → prior | Decision → Prior Decision |
| creates | source → created | Decision → Rule |
| enforced-by | source → enforcer | Rule → Governance |
| related-to | either direction | anything else |

**What NOT to do:**

- Do not build software before the manual method proves itself (DEC001, RG001).
- Do not create artifacts to satisfy process rather than reduce uncertainty (G002).
- Do not modify evidence after creation (G001).
- Do not delete outdated documents — deprecate them and reference the replacement (G002, G004).
- Do not change an artifact's identity, ever (RG003).
- Do not treat observations as knowledge — everything passes through experimentation (research-003).

---

## Where Things Live

| Need | Go to |
|------|-------|
| Why the project exists | [research/000-north-star.md](research/000-north-star.md) |
| How research works | [research/003-research-methodology.md](research/003-research-methodology.md) |
| What an artifact is | [governance/G003-artifact-model.md](governance/G003-artifact-model.md) |
| Lifecycle states | [governance/G004-artifact-lifecycle.md](governance/G004-artifact-lifecycle.md) |
| Relationship vocabulary | [governance/G006-relationships.md](governance/G006-relationships.md) |
| Starting template | [governance/templates/artifact-template.md](governance/templates/artifact-template.md) |
| Current effective rules | [governance/manifest.json](governance/manifest.json) |
| Resolve an artifact ID | [governance/artifact-registry.json](governance/artifact-registry.json) |
| How to change governance | [governance/README.md](governance/README.md#how-governance-changes) |
