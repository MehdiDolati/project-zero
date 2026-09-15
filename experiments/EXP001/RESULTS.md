# EXP001 Results

Findings record for [EXP001](EXP001-momentum-replication.md), written **during**
execution per procedure steps 6–10: the primary result is transcribed from the
`Metrics` tab (step-5 recipe) before any robustness check is run, robustness
checks are appended after, and the evaluation and decision follow.

Evidence itself lives under
[evidence/](evidence/README.md) and is immutable once written
([G001](../../governance/G001-research-governance.md)); this file records
findings, not data.

Provenance of this record ([RG008](../../governance/rules/RG008-authorship-provenance.md)):

| Field | Value |
|-------|-------|
| `created-by-type` | `agent` |
| `created-by` | AI assistant (Buffy) in Freebuff, on direction of the project owner |
| `created-by-version` | not available |
| `production-tools` | Freebuff (Buffy coding agent) |
| `created-at` | 2026-09-15T11:35:39+03:30 |

This provenance block describes the scaffold. When content sections are filled
during execution, the filling work (transcription from the workbook, robustness
runs) is the researcher's manual work per DEC001 and is provenance-recorded in
[evidence/execution-log.md](evidence/execution-log.md), per the established
division of labor.

> **Recording state: AWAITING DATA.** This file is a pre-registered scaffold.
> No section below a stage gate contains a result; placeholders are not
> predictions. Stage gates are listed in "How this file grows" and MUST be
> respected in order. Per the design's failure criteria, this scaffold freezes
> no metric cell in the workbook and predetermines no value.

---

## How this file grows

- **Gate 1** — the `Metrics` tab is complete and its verification checklist is
  passed and logged → fill §1 (primary result) and only §1.
- **Gate 1.5** — §1 is complete → append §2 (robustness checks), one at a
  time, each when run, in the design's order (2.1 → 2.4).
- **Gate 2** — §2 lists all four checks → fill §3 (evaluation) and §4
  (decision), then §5 (trace updates). Never write §3–§5 earlier.
- Sections not yet unlocked are left untouched as headings with their gates
  stated; when a section is filled, its gate note is replaced by the content
  and a dated note, not silently.
- Corrections to already-written sections are made by superseding notes with
  dates, not by editing recorded numbers.

---

## 1. Primary result — [GATE 1: fill only after Metrics tab complete and checklist passed]

Fill from the `Metrics` tab 2×2 grid, every metric for rule and benchmark,
IS and OOS, at full displayed precision. Structure:

### 1.1 Full metric table (rule and benchmark, IS and OOS)

| Metric | Rule IS | Rule OOS | Bench IS | Bench OOS |
|--------|---------|----------|----------|-----------|
| n months | | | | |
| annualized return (geometric) | | | | |
| annualized volatility | | | | |
| Sharpe ratio | | | | |
| maximum drawdown | | | | |
| % months invested | | | | |
| switches | | | | |
| total cost drag | | | | |

### 1.2 Primary comparison metrics

| Comparison (rule − benchmark) | IS | OOS |
|-------------------------------|----|----|
| Sharpe difference | | |
| Maximum drawdown difference | | |

Transcription notes (fill when transcribing): workbook used, export CSV hash,
last complete month, any window-size deviation from the 768/152/920 defaults.

### 1.3 First-impression note (optional, before robustness)

One short paragraph, written fresh at Gate 1: what the numbers look like and
what could still change it. Written once, at the moment of transcription.

---

## 2. Robustness checks — [GATE 1.5: append after §1, one at a time, in run order 2.1 → 2.4]

Each check gets one subsection, appended as run, each stating: specification
variant, where its numbers came from, the Sharpe difference and MDD difference,
the n months on each side of each comparison, and whether the sign of the
Sharpe difference holds. The four checks, in the design's order:

### 2.1 Lookback perturbation (10, 11, 13, 14 months) — [GATE 1.5]

Pending.

### 2.2 Cost perturbation (0 bps, 30 bps per switch) — [GATE 1.5]

Pending.

### 2.3 Signal timing (12-1 form) — [GATE 1.5]

Pending.

### 2.4 Sub-period split (OOS first half vs second half) — [GATE 1.5]

Pending.

---

## 3. Evaluation — [GATE 2: fill only after all four robustness checks are recorded]

Pending until Gate 2. Per the design, this section must state: what the
evidence supports, what it does not, competing explanations, and remaining
uncertainty.

---

## 4. Decision — [GATE 2: fill only after §3, per procedure step 9]

Pending until Gate 2. Must state: the decision on sub-claim C1 (supported /
weakened / inconclusive, per the design's findings criteria, with the
pre-declared 0.1 Sharpe-difference bound applied as written), whether the
evidence bears on [H001](../../hypotheses/H001-edge-is-emergent.md) confidence
(and explicitly if not), the confidence value, and remaining uncertainty.

---

## 5. Trace updates and session record — [GATE 2: fill only after §4, per procedure step 10]

Pending until Gate 2. Must record: registry and relationship updates, whether
a decision artifact is created, the session record if a belief changed, and
the post-execution review against the success/failure criteria — required by
the design's Review section and still mandatory regardless of outcome.

---

## Revision history

| Version | Date | Summary |
|---------|------|---------|
| 1.0 | 2026-09-15 | Scaffold created before any data was examined. No results exist. |
| 1.1 | 2026-09-15 | Pre-execution consistency review: §2 preamble updated to require the n months on each side per check (the step-7 recipe already required it; the scaffold's checklist omitted it). No structural change; still no results exist. |
