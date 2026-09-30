---
id: PR002
type: document
title: Data Provenance and Fitness Evidence

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

State the project's non-negotiable requirement that a research result cannot
exist without recorded provenance and evidence that its data is fit for the
question it is used to answer.

---

# Context

Project Zero produces results from data. A result is only as trustworthy as the
data behind it and the traceability of that data. This principle makes the
precondition explicit: provenance and fitness are not optional niceties added
after a result is produced — they are part of what makes something a result at
all.

---

# Content

No research result may be produced, accepted, or cited without both:

- **Data provenance** — where the data came from, who or what produced it, when
  it was obtained, and how it was transformed along the way.
- **Fitness evidence** — why this data is adequate for this question: coverage,
  resolution, semantics, known limitations, and any validation performed.

A result whose inputs cannot be traced, or whose data has not been shown fit for
the question, is not a result. It remains an unresolved uncertainty and MUST be
labelled as such.

---

# Rationale

Without provenance, a result cannot be reproduced, challenged, or attributed.
Without fitness evidence, a result may be precise but answer the wrong question
with unsuitable data. Both failures are silent and fatal to the research
methodology. This principle prevents them by making provenance and fitness
preconditions rather than afterthoughts.

---

# Relationships

- related-to: governance/G001-research-governance.md (G001)
- related-to: governance/rules/RG008-authorship-provenance.md (RG008)
- related-to: governance/rules/RG009-claim-provenance.md (RG009)
- related-to: governance/G005-traceability.md (G005)
- related-to: principles/repository-as-source-of-truth.md (PR001)

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

This principle SHOULD be reviewed whenever the provenance or evidence rules
that operationalize it (RG008, RG009, G001) change.

---

# Revision History

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | 2026-09-30 | Initial version. Establishes provenance and fitness as preconditions for any research result. |