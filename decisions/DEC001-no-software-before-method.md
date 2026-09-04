---
id: DEC001
type: decision

title: No Software Before Method

status: accepted
version: 1.0

owner: Project Zero

created: 2026-07-28
last-reviewed: 2026-09-04
---

# Decision

No custom software will be developed until the underlying research methodology has demonstrated value through repeated manual execution.

---

# Context

The project aims to discover a repeatable process for identifying and managing sustainable trading edge.

There is a significant risk that software development becomes a substitute for solving the actual research problem.

Building tools before understanding the process creates the illusion of progress while increasing complexity and maintenance cost.

---

# Problem

Software is easy to justify.

Methodology is difficult.

Without a validated methodology, software merely automates assumptions.

If those assumptions are wrong, automation amplifies the wrong process.

---

# Decision Drivers

The decision is based on the following principles:

- Method before automation.
- Evidence before implementation.
- Simplicity before complexity.
- Research before engineering.

---

# Decision

The project will initially operate as a manual research system.

Existing commercial and open-source tools should be preferred whenever they sufficiently support the research process.

Custom software is justified only when:

- a manual process exists,
- the process has demonstrated value,
- automation clearly reduces cost or increases quality,
- existing tools cannot reasonably solve the problem.

---

# Consequences

Positive:

- prevents premature engineering,
- focuses effort on discovering truth,
- reduces maintenance burden,
- encourages process validation,
- avoids building unnecessary infrastructure.

Negative:

- slower manual execution,
- repeated manual work,
- less convenience during early research.

These costs are considered acceptable because they reduce the risk of optimizing an invalid process.

---

# Review Criteria

This decision should be revisited only if evidence demonstrates that manual execution has become the primary bottleneck.

The burden of proof is on automation, not on manual work.

---

# Relationships

- derives-from: research/003-research-methodology.md (research-003)
- enforced-by: governance/rules/RG001-automation-follows-stability.md (RG001)
- related-to: hypotheses/H000-project-should-not-exist.md (H000)
- related-to: research/000-north-star.md (research-000)
- created-in: research/sessions/S000-project-zero.md (S000)