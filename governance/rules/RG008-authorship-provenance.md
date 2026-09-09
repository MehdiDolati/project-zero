---
id: RG008
type: rule

title: Artifact Authorship and Production-Tool Provenance

status: active
version: 1.0

owner: Project Zero

created: 2026-09-09
last-reviewed: 2026-09-09

created-by-type: agent
created-by: AI assistant using Copilot SDK in VS Code
created-by-version: not available
production-tools: VS Code, Copilot SDK, apply_patch
created-at: 2026-09-09T08:52:45+03:30

---

# Purpose

Make authorship and production methods traceable at the artifact level.

This rule ensures that:

- every artifact or evidence record declares whether it was created by a human
  or an agent,
- agent authorship identifies the agent, its provider, and its version,
- the tools used to produce the artifact are recorded,
- missing version information is stated explicitly rather than guessed.

This rule does not replace the artifact owner field (who is responsible for the
artifact's content) or the governance record (what rules applied to its
creation). It adds a production-layer trace that answers: who or what built
this, when, and using what tools?

---

# Statement

Every artifact and evidence record MUST declare authorship and production-tool
metadata using the following fields:

| Field | Required | Value |
|-------|----------|-------|
| `created-by-type` | Yes | `human` or `agent` |
| `created-by` | Yes | Person's name, or agent name and provider (e.g., "AI assistant using Copilot SDK in VS Code") |
| `created-by-version` | Conditional | Agent/model version if applicable; `not available` if it cannot be observed. MUST be present if `created-by-type: agent` |
| `production-tools` | Yes | Tool names and versions when available (e.g., "VS Code 1.95.0", "Python 3.11.2", "ripgrep 14.1.0"). Can be a list. Include `not available` if version cannot be determined. |
| `created-at` | Yes | Timestamp in ISO 8601 format with timezone (e.g., `2026-09-09T08:52:45+03:30`) |

These fields MUST appear in:

- Artifact front matter (YAML header), or
- The top of evidence documents (marked section or header), or
- The `GOVERNANCE.md` record for governed work

### Multi-contributor artifacts

If multiple people or agents contributed:

- Record each contributor separately,
- Distinguish the primary producer from reviewers or editors,
- Use clear language: "primary author:", "reviewed by:", "agent-assisted by:", etc.

### Examples

#### Human-created artifact

```yaml
created-by-type: human
created-by: Mehdi Dolati
created-by-version: N/A
production-tools: VS Code 1.95.0, Markdown
created-at: 2026-09-09T08:00:00+03:30
```

#### Agent-created artifact

```yaml
created-by-type: agent
created-by: AI assistant using Copilot SDK in VS Code
created-by-version: not available
production-tools: VS Code, Copilot SDK, apply_patch
created-at: 2026-09-09T08:52:45+03:30
```

#### Mixed-contributor artifact

```yaml
created-by-type: human + agent
created-by: |
  Primary: AI assistant using Copilot SDK in VS Code
  Reviewed by: Mehdi Dolati
created-by-version: agent version not available
production-tools: VS Code, Copilot SDK, apply_patch, Python 3.11.2
created-at: 2026-09-09T08:52:45+03:30
```

---

# Rationale

Without authorship records, later reviewers cannot distinguish:

- human-created artifacts from agent-created ones,
- artifacts created by newer agent versions from older ones,
- tools that may have introduced subtle behaviors or biases.

This is particularly important when:

- an agent makes a claim in an artifact (evidence, findings, conclusions),
- artifact contents will be used to make decisions,
- future maintenance or audits need to understand the origin of a piece of work.

Recording the tools (VS Code, ripgrep, Python, etc.) makes it possible to:

- understand what capabilities were available to the producer,
- reproduce or audit the work in the same environment,
- track when tool changes might affect artifact quality or interpretation.

This rule applies to all artifacts, not just evidence, because the production
method affects credibility and reproducibility at every level.

---

# Applies To

- All research artifacts (hypotheses, experiments, evidence)
- All governance artifacts (rules, decisions, records)
- All discovery and knowledge artifacts
- Execution logs and session records

---

# Exceptions

None. If an artifact's authorship or tools cannot be determined, that absence
MUST be recorded explicitly in the fields (e.g., `created-by-version: not
available`). Do not omit the fields or guess.

---

# Relationships

- enforces: governance/G001-research-governance.md (Evidence requirements)
- enforces: governance/rules/RG007-governance-execution.md (governed-work records)
- enforces: governance/templates/artifact-template.md (artifact front matter)
- related-to: governance/G005-traceability.md (G005)
- related-to: experiments/README.md (authorship guidance for experiments)

---

# Review

This rule SHOULD be reviewed when:

- new agent providers or tools become common in the project workflow,
- the artifact template changes,
- a real case shows that the fields do not actually answer the authorship
  question,
- evidence emerges that authorship records improve or fail to improve
  artifact quality or reproducibility.

---

# Revision History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | 2026-09-09 | Initial version. Defines authorship and tool provenance fields for all artifacts. |
