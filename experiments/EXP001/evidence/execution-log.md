# EXP001 Execution Log

This log is written **during** execution, not reconstructed afterwards. It exists
to make the process itself observable, because the process is one of the two
objects under study in EXP001.

Append-only. Entries are not edited once written. Corrections are made by
adding a new entry that supersedes the old one, with a note
([G001](../../../governance/G001-research-governance.md)).

---

| Field | Value |
|-------|-------|
| `created-by-type` | `agent` (log scaffold and step-1 entries) |
| `created-by` | AI assistant (Buffy) in Freebuff, on direction of the project owner |
| `created-by-version` | not available |
| `production-tools` | Freebuff (Buffy coding agent), web search (Serper Google API), read_url |
| `created-at` | 2026-09-09T16:47:36+03:30 |

---

## Step 1 record — 2026-09-09 — Data sources identified and verified (pre-download)

Per procedure step 1 and the v1.2 pre-execution review watch item, candidate
free sources for both series were identified and their coverage verified
against publisher records **before** any file was downloaded. Nothing has been
retrieved yet; `raw/` is empty.

**Equity series — [SRC004](../../../sources/SRC004-shiller-ie-data-monthly-stock.md)**
(Shiller `ie_data.xls`, https://shillerdata.com/):

- Publisher page read directly; workbook confirmed to contain monthly US stock
  price, dividends, earnings, interest rates, and CPI from 1871-01, including
  a total-return price series (per Bunn & Shiller 2014; Jivraj & Shiller 2017).
- Coverage requirement (from 1950-01): satisfied with 79 years of headroom.

**Cash series — [SRC005](../../../sources/SRC005-fred-tb3ms-monthly.md)**
(FRED TB3MS, https://fred.stlouisfed.org/series/TB3MS):

- FRED's data page read directly; title, source (Federal Reserve Board),
  release (H.15), frequency (monthly), units (percent), and date range
  (1934-01-01 to 2026-08-01) confirmed from the publisher record.
- Coverage requirement (from 1950-01): satisfied with 16 years of headroom.

**Conclusion:** the coverage gate from the pre-execution review passes for
both series. The data-source substitution risk flagged at review is closed
for the IS window as specified.

**Verification method:** publisher pages read via HTTP; no third-party
mirrors relied on. Workbook and CSV contents themselves are unverified until
retrieval; verification-at-retrieval is mandatory per SRC004 and SRC005
registration notes.

**Division of labor:** this step was performed agent-assisted (source search
and verification). The manual execution phases that feed the process metrics —
spreadsheet construction, computation, analysis, write-up — remain the
researcher's, per DEC001 and the experiment's design.

---

## Discretionary choices

Every point where judgement was required and the design artifact did not
determine the answer. Record the choice, the alternatives considered, and the
reason. Include choices that were tempting and rejected.

| # | Date | Choice made | Alternatives | Reason |
|---|------|-------------|--------------|--------|
| 1 | 2026-09-09 | Use Shiller monthly-average-of-daily-closes price column as-is | Splice in a month-end-close series from another source; switch to an ETF-based series | A spliced series introduces a structural break at the splice date and complicates reproducibility more than the smoothing does; ETF inception is far too late for the IS window. Deviation recorded as an EXP001 assumption (v1.3). |
| 2 | 2026-09-09 | Derive monthly cash return from TB3MS with a stated simple conversion (discount-basis rate ÷ 12) | Use a different risk-free series; compound the discount rate to a bond-equivalent yield first | TB3MS is the official long free series; the discount-to-yield gap is small and directionally known. Conversion will be recorded in `evidence/derived/`. |
| 3 | 2026-09-09 | Retrieve TB3MS from federalreserve.gov (H.15 Data Download Program) after FRED connection failures | Keep retrying FRED; use a third-party mirror (DBnomics); defer retrieval | federalreserve.gov is the **primary** source of the series FRED redistributes; mirrors add a layer without adding authority. Substitution and anchor-match check (1934-01 = 0.72 identical on both routes) recorded in `raw/provenance.md`. |

---

## Shortcuts prevented by methodology

Points where the documented method stopped something that would otherwise have
been done. These are the evidence for the project creating value.

| # | Date | Shortcut that was tempting | What prevented it |
|---|------|----------------------------|-------------------|
| 1 | 2026-09-09 | Download the first apparently-suitable dataset from a search and discover coverage problems mid-build | The v1.2 pre-execution review's coverage gate: sources must be verified against the full IS window before the first download |

---

## Governance overhead with no research value

Points where following governance produced work that caught nothing and improved
nothing. Recording these honestly is required. They are evidence for
[H000](../../../hypotheses/H000-project-should-not-exist.md).

| # | Date | What was required | Why it added no value |
|---|------|-------------------|-----------------------|

None recorded at execution step 1: the SRC registrations for the datasets
doubled as the provenance scaffolding procedure step 1 requires anyway, and
produced the data-shape assumptions above, which are research-relevant.

---

## Retrieval record — 2026-09-09 — Step 1 completed: files retrieved, hashed, verified

Both files were retrieved once, stored byte-for-byte in `raw/`, and hashed
(SHA-256). Full details, URLs, HTTP headers, and the route substitution for
TB3MS are in [raw/provenance.md](raw/provenance.md). Summary:

| File | Size | SHA-256 (first 12) | Content verification |
|------|------|--------------------|----------------------|
| `ie_data.xls` (SRC004) | 1,674,752 B | `46a7fd194c53` | Format + publisher metadata verified; **cell contents pending** (no legacy-Excel reader available; no package installed per DEC001). Verification assigned to step 2, when the workbook is first opened manually in Excel. |
| `TB3MS.csv` (SRC005, via federalreserve.gov) | 115,160 B | `edd3c63effb2` | **PASSED**: 920 months 1950-01→2026-08, 0 missing, 0 calendar gaps; 1934-01 anchor matches FRED's published table; spot values plausible. |

Notes:

- The coverage gate (watch item 1 from the pre-execution review) is now
  **closed with retrieved data for the cash leg**; the equity leg closes at
  step 2 when the workbook is opened.
- FRED was unreachable from the execution network (repeated connection
  resets); retrieval used the series' primary source instead. Recorded as
  discretionary choice #3 and in provenance.
- Agent-assisted time (search, retrieval, verification) is not counted in the
  manual-effort table below, which measures the researcher's manual execution
  per the experiment's process-metric design. Agent-assisted steps are
  timestamped in provenance instead.

---

## Step 2 preparation record — 2026-09-15 — Spreadsheet recipe written; execution not started

To make procedure step 2 reproducible before it begins, the column
definitions and formulas for the monthly table were written out in advance as
[step2-spreadsheet-recipe.md](derived/step2-spreadsheet-recipe.md)
(agent-assisted, per the established division of labor; the researcher
performs the actual manual build per DEC001). The recipe:

- defines the `Data` tab columns A–K with visible formulas (the derivation
  record that SRC004 and SRC005 require in `evidence/derived/`),
- fronts the workbook-content verification of `ie_data.xls` as recipe step 2a,
  which closes the equity-leg coverage gate open since step 1,
- sets row anchors (1948-12 pad month; first IS row 1950-01; 933 data rows if
  the last complete month is 2026-08) and TB3MS spot anchors taken from the
  raw file,
- fixes the experiment constants (IS window 1950-01→2013-12, 10 bps per
  switch) in a single constants zone referenced by all formulas.

One authoring correction was made to the recipe before it was first used:
the initial `rule_ret_IS` formula and constants placement collided with data
rows. It is declared in the recipe's own correction record. Nothing was
computed from the earlier text; no manual effort time elapsed.

## Superseding note to the step 2 preparation record — 2026-09-15

The step 2 preparation entry above states "one authoring correction". The
recipe's correction record, as finalized before first use, lists three:
correction 1 (rule_ret_IS formula and constants placement), correction 2
(row-anchor offsets), correction 3 (the R12_prev column formula, which was
first written as a single-month return). The earlier entry understates the
count; the recipe's own correction record is authoritative. Nothing was
computed from any superseded text, and no manual effort time elapsed.

---

## Step 5 preparation record — 2026-09-15 — Metrics recipe written; execution not started

To keep the computation phase fully specified before any data is touched, the
metric definitions were written out in advance as
[step5-metrics-recipe.md](derived/step5-metrics-recipe.md) (agent-assisted;
the researcher performs the manual build per DEC001). The recipe:

- extends the step-2 table with columns L–P: rule/benchmark wealth (anchored
  at 1.0000 on the 1949-12 row), running-peak drawdowns, and the monthly
  risk-free decimal,
- fixes two conventions that were open in the design artifact — wealth-unit
  anchoring, and the OOS drawdown read against the full-history peak — both
  to be entered in the discretionary-choices table when applied,
- defines the eight metrics per window with exact formulas: geometric
  annualized return taken from the wealth columns (the ×12 arithmetic form is
  a robustness footnote only), a single Sharpe definition
  `(mean(r) − mean(rf)) / stdev(r) × √12`, and window sizes 768 IS + 152 OOS
  = 920 months if the last complete month is 2026-08,
- preserves the procedure step-6 ordering safeguard: the primary result is
  transcribed to RESULTS.md before any robustness check is run.

Three authoring corrections were made to the recipe before first use,
recorded in its own correction record. Execution and the effort clock have
not started.

---

## Step 7 preparation record — 2026-09-15 — Robustness recipe pre-registered; execution not started

To complete the pre-registered computation-phase pipeline, the four robustness
checks were specified in advance as
[step7-robustness-recipe.md](derived/step7-robustness-recipe.md)
(agent-assisted; the researcher runs them per DEC001). The recipe:

- fixes every variant specification before any data is examined: four lookback
  variants (10/11/13/14 months, positions written directly as price ratios),
  two cost variants (0 and 30 bps, positions unchanged from the main rule),
  the 12-1 timing variant, and the OOS sub-period split,
- pre-computes all window arithmetic from the committed row anchors: variant
  warm-up rows, first-applied rows, IS/OOS windows (IS n of 768, 767, or 766
  by variant; OOS 152 for all; halves of 76 + 76 months, boundary
  2020-04/2020-05),
- binds the execution gate and append order of the RESULTS.md scaffold:
  checks run only after the primary result (§1) is recorded, columns are
  added in one logged action, and each check's subsection is appended before
  the next check is computed,
- fixes reporting conventions: like-for-like windows (benchmark and risk-free
  computed on the variant's own rows), per-variant wealth anchors, and the
  full-history running peak for sub-period MDDs,
- restates the design's scope guards: no additional perturbations, no
  parameter search, no import of the 0.1 bound into robustness, and no
  replacement of the frozen main specification by a better-performing
  variant.

One authoring correction was made before first use (the sub-period boundary
is the equal-months split, not a calendar-year split); it is recorded in the
recipe's correction record. No robustness number exists; execution and the
effort clock have not started.

---

## Step 6 preparation record — 2026-09-15 — RESULTS.md scaffold created; no result exists

To make procedure step 6 executable without discretionary formatting
decisions under results-pressure, the findings record was scaffolded in
advance as [RESULTS.md](../../RESULTS.md) (agent-assisted; the researcher
fills it during execution per DEC001). The scaffold:

- fixes the section structure in procedure order: primary result (§1, from
  the `Metrics` tab 2×2 grid), robustness checks (§2, in the design's order),
  evaluation (§3), decision (§4), trace and session updates (§5),
- declares stage gates: §1 is filled only after the `Metrics` tab passes its
  verification checklist; robustness checks are appended one at a time after
  §1; §3–§5 are written only after all four checks are recorded,
- contains no result-shaped content: no placeholder carries a value, no
  metric cell in the workbook is frozen by the scaffold, and the
  pre-declared 0.1 Sharpe-difference bound quoted in §4's decision criteria
  comes from the design artifact, not from this scaffold,
- routes corrections through superseding dated notes rather than edits to
  recorded numbers.

The design's Representations section lists `RESULTS.md` as written on
execution; the scaffold holds structure only, and findings content still
appears only on execution. The scaffold predates any data examination.
Execution and the effort clock have not started.

---

## End-to-end consistency review record — 2026-09-15 — Four pre-registered documents reviewed; five pre-use corrections

Before the manual build starts, the four pre-registered documents (step-2,
step-5, and step-7 recipes; RESULTS.md scaffold) were reviewed against each
other, the frozen design artifact (EXP001 v1.3), the registered raw evidence,
and the source registrations. The review was agent-assisted; the researcher's
manual build remains the independent check.

**Verified consistent (no action):**

- Row anchors and window arithmetic agree across all four documents and the
  committed step-2 anchors: row 2 = 1948-12; IS rows 15–782 (768); OOS rows
  783–934 (152); total 920; variant first-applied rows 15/15/16/17/16 (IS n
  768/767/766); sub-period halves 76 + 76 with boundary rows 858/859
  (2020-04/2020-05).
- Constants map is collision-free: `README!B4/B5/B6` (step 2), `B7` (step 5),
  `B8/B9` (step 7); `Data` columns A–AI with no letter reused.
- TB3MS spot anchors in the step-2 checklist match the raw file exactly
  (1948-12 = 1.16, 1950-01 = 1.07, 2007-12 = 3.00, 2020-03 = 0.29,
  2026-08 = 3.72).
- Gate and append order is consistent across the step-5 recipe, the step-7
  recipe, and the RESULTS.md scaffold: §1 before any robustness run, one §2
  subsection per check before the next runs, §3–§5 only after all four.
- Formulas re-derived independently: F = P_{t−1}/P_{t−13} − 1 (no look-ahead),
  the variant signal ratios, the cost-perturbation identity
  (main return + H×(0.001 − 0.003)), the wealth recursion, and the
  running-peak drawdown forms.

**Findings and dispositions** (all corrections pre-use; nothing was computed
from superseded text; no data examined; effort clock not started):

| # | Finding | Disposition |
|---|---------|-------------|
| 1 | Step-5 recipe: three OOS formulas abbreviated as "same with `>=README!$B$7`" are not valid as abbreviated — `COUNTIFS`/`AVERAGEIFS`/`SUMIFS` need the criteria range restated; a literal reading yields a broken or wrong formula | Formulas written out in full; `B7`'s role stated (OOS start constant); an Excel-version fallback fixed (never a plain COUNT/AVERAGE/SUM over a pasted range). Step-5 correction record updated. |
| 2 | Step-5 recipe: implied that % months invested and switches are computed for the benchmark too; they are rule-construction quantities (benchmark: 100% / 0 by construction) | Clarified in the step-5 recipe. |
| 3 | Step-2 recipe: TB3MS series locator said "column K" of the raw CSV; the series is the 12th header field = column L (raw file and `raw/provenance.md` agree) | Locator corrected; step-2 correction record updated. The series identifier was correct throughout. |
| 4 | Step-7 recipe: the only one of the four documents without an explicit anchor-shift contingency for a last complete month other than 2026-08 | Contingency added, including the odd-OOS split rule; correction record updated. No expected row number changed. |
| 5 | Execution log: the step-7 preparation entry was inserted before the step-6 entry, so the preparation records read 2 → 5 → 7 → 6 | Left as written (append-only); this note supersedes the implied order. All three entries are dated 2026-09-15 and no substantive claim depends on their order. |

RESULTS.md scaffold: §2 preamble updated to require the n months on each side
per robustness subsection (the step-7 recipe already required it; the
scaffold's checklist omitted it) — scaffold revision 1.1, recorded in its
revision history. No structural change; still no results exist.

**Honesty note:** the defects were introduced and caught by the same
agent-assisted preparation process. A self-review is weaker evidence than an
independent review; this record exists because the corrections are real and
pre-use, not as evidence that the pipeline is validated. Validation remains
the researcher's manual execution, checklist by checklist.

---

| Phase | Minutes |
|-------|---------|
| Data retrieval and provenance | |
| Computation | |
| Analysis | |
| Write-up and registration | |
| **Total** | |

---

## Status

Updated 2026-09-15. Step 1 complete: sources verified pre-download, both
files retrieved once, hashed, and provenance recorded in `raw/provenance.md`;
TB3MS content fully verified (coverage, continuity, anchor match).
Step 2 is **prepared, not started**: the manual spreadsheet recipe
(columns, formulas, verification checklist, constants zone) is at
[derived/step2-spreadsheet-recipe.md](derived/step2-spreadsheet-recipe.md),
including recipe step 2a — the `ie_data.xls` workbook verification that
closes the equity-leg coverage gate on first manual open in Excel, before
any derived series is built. The effort clock has not started. Next: the
researcher executes recipe steps 2a–2d, records the workbook verification
and checklist results in this log, and starts the effort clock for the
manual phases. The step-5 metrics recipe, the pre-registered RESULTS.md
scaffold (procedure step 6), and the pre-registered step-7 robustness recipe
together complete the computation-phase preparation; the primary result is
transcribed to RESULTS.md only after the `Metrics` tab passes its checklist,
and robustness checks run only after that. An end-to-end consistency review
of the four pre-registered documents (2026-09-15, record above) found and
corrected five defects before use; the documents are internally consistent
and execution-ready.
