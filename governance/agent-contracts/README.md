# Agent Contracts

Agent contracts specify the responsibilities, boundaries, inputs, outputs, and
review criteria of a defined Project Zero agent role. They are not executable
agents, active governance rules, or approval to automate work.

Contracts use the stable `AC` identity family and the filename form:

```text
governance/agent-contracts/ACNNN-<kebab-case-role>.md
```

Each contract begins as `draft`. It is tested through repeated manual use,
reviewed for omissions and harmful ambiguity, and only then considered for an
automation decision under [RG001](../rules/RG001-automation-follows-stability.md).

| ID | Title | Status |
|----|-------|--------|
| AC001 | Question Formulation Agent Contract | draft (v1.1) |
