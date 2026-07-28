---
id: G003

title: Artifact Model

status: active

owner: Project Zero

---

# Purpose

Artifacts are the fundamental building blocks of Project Zero.

The repository does not manage files.

It manages artifacts.

Files are only physical representations of artifacts.

---

# Definition

An Artifact is a uniquely identifiable unit of persistent project knowledge.

Artifacts may represent:

- Questions
- Hypotheses
- Experiments
- Evidence
- Decisions
- Knowledge
- Documents
- Datasets
- Software
- Models
- Reports

An Artifact exists independently of any specific file format.

---

# Artifact Identity

Every Artifact MUST have a stable identity.

The identity MUST remain unchanged throughout the Artifact lifecycle.

Changing file names or repository structure MUST NOT change the Artifact identity.

Example:

id: H001

---

# Artifact Components

Every Artifact consists of four conceptual layers.

## Identity

Defines what the artifact is.

Examples:

- H001
- EXP004
- DEC002

---

## Metadata

Describes the current state of the artifact.

Typical metadata includes:

- status
- owner
- created date
- review date
- version
- confidence (when applicable)

Metadata may evolve.

Identity does not.

---

## Relationships

Artifacts exist within a network.

Relationships describe how artifacts influence each other.

Examples:

Question

↓

motivates

↓

Hypothesis

Hypothesis

↓

tested-by

↓

Experiment

Experiment

↓

produces

↓

Evidence

Evidence

↓

supports

↓

Decision

Decision

↓

creates

↓

Knowledge

Relationships are part of the knowledge model.

They are not documentation convenience.

---

## Representations

An Artifact may have one or more physical representations.

Examples:

- Markdown
- CSV
- JSON
- PNG
- PDF
- Python Notebook
- SQX Project
- Source Code

Representations may change.

Artifacts remain.

---

# Traceability

Every Artifact SHOULD participate in traceability.

Artifacts should expose enough relationships to understand:

- where they originated,
- what they depend on,
- what they influence.

---

# Versioning

Artifact identity remains stable.

Representations and metadata may evolve through versions.

History should remain observable.

---

# Principles

Project Zero manages knowledge rather than files.

Knowledge is represented through Artifacts.

Artifacts are connected through Relationships.

Files exist to persist Artifacts.

---

# Future Evolution

Future automation, validation, search, visualization, and AI reasoning should operate primarily on Artifacts and Relationships rather than individual files.