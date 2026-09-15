# EXP001 Evidence

Evidence for EXP001. Immutable once written
([G001](../../../governance/G001-research-governance.md)): evidence MUST NOT be
modified after creation. Corrections are made by adding a new file that
supersedes the old one, with a note explaining why. Nothing here is edited in
place.

---

## Layout

| Path | Contents |
|------|----------|
| `raw/` | Data exactly as downloaded. Never edited, never reformatted. |
| `raw/provenance.md` | Source URL, retrieval timestamp, file hash for every raw file. |
| `derived/` | Computation workbook and CSV exports, regenerable from `raw/`. |
| `derived/step2-spreadsheet-recipe.md` | Column definitions, formulas, constants zone, and verification checklist for procedure step 2; written before execution. |
| `derived/step5-metrics-recipe.md` | Wealth/drawdown columns, per-window metric formulas, Sharpe definition, and verification checklist for procedure step 5; written before execution. |
| `derived/step7-robustness-recipe.md` | Pre-registered specification variants, windows, reporting conventions, and gates for the four robustness checks of procedure step 7; written before execution. |
| `execution-log.md` | Discretionary choices and process metrics recorded during execution. |

---

## Status

Step 1 complete: `raw/` holds `ie_data.xls`, `TB3MS.csv`, their HTTP header
captures, and [raw/provenance.md](raw/provenance.md) with SHA-256 hashes and
verification results. TB3MS content verified (coverage, continuity, anchor
match); workbook cell contents verify at execution step 2 on first manual
open. `derived/` holds the step-2 spreadsheet recipe, the step-5 metrics
recipe, and the pre-registered step-7 robustness recipe (all written
2026-09-15, before execution; no derived data yet). Log:
[execution-log.md](execution-log.md).
