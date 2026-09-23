---
id: PR001
type: document

title: Repository as Source of Truth

status: active
version: 1.0

owner: Project Zero

created: 2026-07-28
last-reviewed: 2026-09-04
---

# Repository as Source of Truth

## Principle

The repository is the long-term memory of Project Zero.

Conversations, brainstorming sessions, and temporary thoughts are not considered authoritative knowledge.

Any validated:
- principle
- hypothesis
- discovery
- decision
- methodology
- process

must be captured in the repository.

## Why

Human conversations are transient.
Context is fragile.
Memory is imperfect.

A sustainable research system requires explicit, versioned, and traceable knowledge.

## Implications

- If an idea exists only in conversation, it does not exist as project knowledge.
- Important decisions must include rationale and alternatives considered.
- Rejected ideas should be preserved with reasons.
- The evolution of thinking is part of the project artifact.

## Context Preservation Rule

Project Zero must always remain resumable.

Before pushing changes that affect the project, the current state must be recorded in `operating-system/CURRENT.md`.

At minimum, the current state should make clear:

* what was completed,
* what was learned,
* what important decisions were made,
* and what the next concrete action is.

This rule exists because Project Zero is intentionally a long-term, exploratory project. Changing direction, following a new idea, or temporarily leaving the project is allowed. Losing the project's current context is not.

> **Every interruption must leave the project resumable.**

The repository enforces this rule through the `pre-push` hook.

A push containing new commits is blocked when none of the commits being pushed updates `operating-system/CURRENT.md`.

The hook is an enforcement mechanism for context preservation, not a substitute for judgment. If a change genuinely does not require a change to the current state, the researcher must still explicitly update `CURRENT.md` before pushing so that the repository remains an accurate representation of the current project state.
