# EXP001 Step 2 — Spreadsheet Recipe (Monthly Table)

Procedure step 2 of [EXP001](../../EXP001-momentum-replication.md): build the
single monthly table in a spreadsheet, manually, with no custom software
([DEC001](../../../../decisions/DEC001-no-software-before-method.md),
[RG001](../../../../governance/rules/RG001-automation-follows-stability.md)).

This recipe is a **derived-series record**: the column definitions and formulas
below, followed exactly, regenerate the table from `raw/` data. Any deviation
from this recipe during execution MUST be recorded as a discretionary choice in
[execution-log.md](../execution-log.md).

Provenance of this record ([RG008](../../../../governance/rules/RG008-authorship-provenance.md)):

| Field | Value |
|-------|-------|
| `created-by-type` | `agent` |
| `created-by` | AI assistant (Buffy) in Freebuff, on direction of the project owner |
| `created-by-version` | not available |
| `production-tools` | Freebuff (Buffy coding agent) |
| `created-at` | 2026-09-15T10:48:55+03:30 |

---

## Requirements

- Raw files are immutable; all values in the workbook are copied from them, never
  recalculated from any other source.
- **Every formula that produces a derived value MUST remain visible as a formula**
  in the saved workbook (not paste-valued). The formulas ARE the derivation record
  required by [SRC004](../../../../sources/SRC004-shiller-ie-data-monthly-stock.md)
  and [SRC005](../../../../sources/SRC005-fred-tb3ms-monthly.md).
- The monthly table MUST contain 1948-12 through the last complete month.
  1948-12 through 1949-12 exist only so that the first IS row (1950-01) has a
  full 12-month return; they are excluded from every IS/OOS computation.
- Workbook saved to `evidence/derived/` as `.xlsx` (plus CSV export of the
  `Data` tab per procedure step 5).

## Row anchors

With header in row 1 and first data row 2 = 1948-12 (verified: 933 months from
1948-12 to 2026-08 inclusive):

| Row | Month | Role |
|-----|-------|------|
| 2 | 1948-12 | Pad start; needed as P_{t−12} for the first IS signal |
| 14 | 1949-12 | Pad end |
| 15 | 1950-01 | **IS start** (highlight) |
| 782 | 2013-12 | IS end |
| 783 | 2014-01 | OOS start |
| 934 | 2026-08 | Last complete month (933 data rows, rows 2–934) |

If step 2a finds the last complete month is not 2026-08, recount: data rows =
months from 1948-12 to the last complete month inclusive, and shift the OOS
anchors accordingly. Pad rows and row numbering do not change.

**Alignment rule:** the `TB3MS` and `Price` tabs are laid out with the same row
numbering (their row 2 = 1948-12), so `Data` row *n* always reads
`Price!B*n*` and `TB3MS!B*n*` with the same *n*. No offset arithmetic anywhere.

## Workbook setup

Five tabs, in this order:

| Tab | Purpose |
|-----|---------|
| `README` | One screen: recipe ID, date, raw-file SHA-256 values (copied from `raw/provenance.md`), and the **constants zone** below |
| `TB3MS` | Cash series extracted from `raw/TB3MS.csv` |
| `Price` | Equity series extracted from `raw/ie_data.xls` |
| `Data` | The monthly table (columns A–K) |
| `Checks` | Verification checklist with pass/fail cells |

## Constants zone (on the `README` tab)

All tunable experiment constants live here once, so the `Data` tab formulas
reference single cells and nothing is hard-coded twice:

| Cell | Value | Meaning |
|------|-------|---------|
| `B4` | 1950-01 | IS start (enter as the same kind of date value as `Data` column A) |
| `B5` | 2013-12 | IS end (OOS is everything after; no second constant needed) |
| `B6` | 0.001 | Cost per switch (10 bps, per the frozen specification) |

After entering them, sanity-test the comparison type: `=README!B4<=README!B5`
MUST be TRUE, and once the `Data` tab exists, `=A15>=README!B4` on the
1950-01 row MUST be TRUE while the same formula on the 1949-12 row MUST be
FALSE. If Excel is comparing text against dates (both yield wrong answers),
re-enter the constants as real dates like column A. Record the outcome of
this test in `Checks`.

## Step 2a — Workbook content verification (do this FIRST)

Open `raw/ie_data.xls` in Excel. Before copying anything, record in
`Checks` and then in [execution-log.md](../execution-log.md):

1. The sheet containing the monthly data (normally the first sheet).
2. The exact column letters holding: date/decimal-date, **P** (price),
   **D** (dividend), **E** (earnings), **CPI**, the real total-return price,
   and the nominal **total-return price** series.
3. First data month (expect 1871-01) and last complete month (the workbook is
   updated monthly and may include a partial current month — identify the last
   **complete** month, expect 2026-08).
4. Whether the total-return price column is nominal or real — the EXP001
   assumption states the nominal TR price is derived from the real TR series
   and CPI; verify which form the workbook actually stores and record it.
5. The date encoding. Expect year.decimal-month (e.g. `1948.12` = 1948-12);
   note that October may *display* as `1948.1`. Do not re-key dates by hand;
   identify rows by position and by known spot values instead.
6. Any notes rows or blank cells inside 1950-01 onward.

This closes the equity-leg coverage gate open since step 1. If any expected
column is missing or coverage does not reach 1950-01, STOP — that is a
versioned change to EXP001, not a workaround.

## Step 2b — `TB3MS` tab

The retrieved H.15 package is a 30-series CSV; the series is the column with
unique identifier `H15/H15/RIFSGFSM03_N.M` ("3-month Treasury bill secondary
market rate, discount basis") — 12th header field, column K of the raw CSV.

1. Copy from `raw/TB3MS.csv`: rows 1948-12 through the last complete month,
   two columns only — `Time Period`, `RIFSGFSM03_N.M`. Paste as values into
   `TB3MS!A:B`, with row 2 = 1948-12 (alignment rule above). This is a **copy
   of raw data**, allowed; it is not a derived value.
2. Keep the pasted values text-like (do not reformat dates); Excel parses
   `1948-12` as a date — that is fine, format as `yyyy-mm`.

## Step 2c — `Price` tab

1. From the opened workbook, copy the date and the **nominal total-return
   price** column for 1948-12 through the last complete month into
   `Price!A:B`, row 2 = 1948-12 (alignment rule above). Do not re-key dates.
2. In `Price!C`, monthly dividend yield = dividend column ÷ price column per
   row, using the workbook's own cell addresses found in step 2a (e.g.
   `=D*cell*/P*cell*`), filled down for the copied rows. Dividends in the
   workbook are a monthly rate already; see Assumption 4 of EXP001. (Column C
   is recorded for completeness; the `Data` tab reads the TR price directly.)

## Step 2d — `Data` tab

Header row 1: the column names below. Formulas are shown for row 15
(= 1950-01); fill down from there unless noted. Pad rows 2–14 carry only the
columns marked "from row 2/3".

| Col | Header | Formula (row 15 = 1950-01) | Notes |
|-----|--------|---------------------------|-------|
| A | `month` | paste/sorted date | Format `yyyy-mm`; row 2 = 1948-12 |
| B | `index_level_tr` | `=Price!B15` | Nominal total-return price per SRC004; from row 2 |
| C | `m_ret` | `=B15/B14-1` | Monthly return; from row 3 (row 2 blank) |
| D | `tbill_annual` | `=TB3MS!B15` | Annual %, discount basis; from row 2 |
| E | `tbill_monthly` | `=D15/12` | Conversion recorded as discretionary choice #2; from row 2 |
| F | `R12_prev` | `=B14/B2-1` | **Trailing 12-month total return as of the prior month-end**: P_{t−1}/P_{t−13} − 1; from row 15 |
| G | `position` | `=IF(F15>0,1,0)` | 1 = invested in month of this row; from row 15 |
| H | `switch` | `=ABS(G15-G14)` | 1 on entry and on exit; from row 15. G14 is genuinely blank (G starts at 15), so H15 = G15: the flat book "enters" the first position and pays the cost iff it is long — record this convention in the discretionary-choices log |
| I | `rule_ret` | `=G15*C15+(1-G15)*E15-H15*README!$B$6` | Cost applied on switches only; from row 15 |
| J | `benchmark_ret` | `=C15` | Same series, no switches, no costs (per spec: "same cost model, no switches" — nothing to charge); from row 15 |
| K | `rule_ret_IS` | `=IF(AND(A15>=README!$B$4,A15<=README!$B$5),I15,"")` | Blank outside IS so the IS window is carried, not recomputed later; from row 15 |

Column F exists to make look-ahead visible and correct: the position in row *t*
is set by the return through month *t−1*, computed from prices *t−1* and
*t−13*, never by row *t*'s own return.

---

## Verification checklist (all boxes recorded in `Checks`, then logged)

1. **Row count**: data rows = 933 for 1948-12 → 2026-08 (rows 2–934; recount
   per Row anchors if the last complete month differs).
2. **Hand row 1950-01** on a calculator, from the raw pasted values, not the
   formulas: C = B15/B14 − 1; F = B14/B2 − 1; G from F; then
   if G = 1, I = C − H×0.001, and if G = 0, I = E − H×0.001 (H = 1 iff this
   first position is an entry from the flat book, i.e. iff G = 1).
3. **TB3MS anchors** (from the raw file): 1948-12 = 1.16, 1950-01 = 1.07,
   2007-12 = 3.00, 2020-03 = 0.29, 2026-08 = 3.72.
4. **Workbook anchors**: after step 2a, copy three spot values (first IS month,
   one mid-window month, last complete month) from the workbook into `Checks`
   and re-enter them by hand from the screen — a two-person-style independent
   re-read, self-administered.
5. **No look-ahead**: scan 10 random rows — `F` uses only prices through
   month *t−1*; `G` changes only after `F` changes; `I` uses month *t*'s own
   return only because the position was fixed at *t−1*.
6. **Cost only on switches**: filter `H = 1` and check every `I` deduction;
   spot-check one `H = 0` row for zero deduction.
7. **IS boundary**: `K` is non-blank exactly for rows 15–782 (1950-01 →
   2013-12; 768 rows).

Each check that **fails** is a finding, not a nuisance: record it in the
execution log, fix the table, and re-run the check.

---

## Process metrics

- Start the phase clock (paper, or the `README` tab) at the first action on the
  workbook. Log minutes under **Computation** in
  [execution-log.md](../execution-log.md) when this step closes.
- Log every discretionary choice (including any deviation from this recipe, and
  the H15 flat-book entry-cost convention) in the log's discretionary-choices
  table, per procedure and the v1.2 watch item 2.

## What this step does NOT include

Columns for metrics, Sharpe inputs, or drawdowns; those are procedure step 5
and will get their own recipe or a direct extension of this one. The OOS
window is carried in the same table from the start so that nothing is
rebuilt later.

---

## Correction record

Made before the recipe was first used; nothing was computed from the
superseded text.

| # | Date | Correction |
|---|------|------------|
| 1 | 2026-09-15 | Initial authoring correction: the `rule_ret_IS` (K) formula was first written with a placeholder condition and constants placed in `Data!A2:A3`/`B2`, which collide with data rows. Fixed to the README constants zone and the `AND(...)` IS-window condition. |
| 2 | 2026-09-15 | Row anchors corrected: formula examples and tests first said "row 13/14 = 1950-01"; with row 2 = 1948-12 the first IS row is row 15, IS end row 782, last row 934. All formulas, checks, and the constants sanity test updated. |
| 3 | 2026-09-15 | Column F (`R12_prev`) was first written as `=C13`, a single-month return — not R12. Corrected to the prior-month-end 12-month price ratio `=B14/B2-1` (P_{t−1}/P_{t−13} − 1), and the fill-start rows (G, H, I, J, K from row 15) plus the flat-book entry-cost convention at H15 were made explicit. |
