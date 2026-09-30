---
id: PR005
type: document
title: AI Is Part of the Operating Model

status: active
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
created-at: 2026-09-30T11:12:00+03:30
---

# Purpose

Establish that AI agents are a structural part of how Project Zero operates,
not an optional automation layer, while keeping responsibility and final
authority with a human owner.

---

# Context

Project Zero is a research and engineering effort that deliberately delegates
specialized cognitive and engineering work to AI agents. This is a design
choice, not a convenience. The project therefore treats AI as part of its
operating model, with the same governance obligations as any other actor that
produces artifacts.

---

# Content

- **AI is part of the operating model.** AI agents are not an optional
  automation layer bolted onto the project. They are actors within it.
- **Delegation, not abdication.** The project assumes a human owner MAY delegate
  specialized cognitive and engineering work to AI agents.
- **Retained responsibility.** The human owner retains responsibility for
  decisions, provenance, and final outcomes. Delegating work never delegates
  accountability.
- **Governed participation.** AI-produced artifacts MUST follow the same
  provenance, authorship, and traceability rules as human-produced artifacts
  (see RG008, RG009, G005).

---

# Rationale

Treating AI as optional automation leads to ungoverned work that cannot be
attributed or trusted. Treating AI as an operating actor, under the same rules
as any contributor and under human accountability, makes delegation safe and
auditable. The distinction between delegating work and retaining responsibility
is what keeps provenance meaningful in an AI-assisted project.

---

# Relationships

- related-to: governance/G001-research-governance.md (G001)
- related-to: governance/rules/RG008-authorship-provenance.md (RG008)
- related-to: governance/rules/RG009-claim-provenance.md (RG009)
- related-to: governance/rules/RG001-automation-follows-stability.md (RG001)
- related-to: governance/G005-traceability.md (G005)
- related-to: principles/repository-as-source-of-truth.md (PR001)
- related-to: principles/PR002-data-provenance-and-fitness.md (PR002)

---

# References

This principle does not rely on external claims.

> None.

---

# Representations

- Markdown

---

# Constraints

> None.

---

# Review

This principle SHOULD be reviewed whenever the provenance rules (RG008, RG009)
or the automation rule (RG001) change.

---

# Revision History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | 2026-09-30 | Initial version. Defines AI as part of the operating model under human responsibility. |