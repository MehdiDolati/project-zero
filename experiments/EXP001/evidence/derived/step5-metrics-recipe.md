# EXP001 Step 5 — Metrics Recipe

Procedure step 5 of [EXP001](../../EXP001-momentum-replication.md): compute all
metrics for rule and benchmark, separately for IS and OOS, from the step-2
table. Manual spreadsheet work only
([DEC001](../../../../decisions/DEC001-no-software-before-method.md)). This
recipe extends [step2-spreadsheet-recipe.md](step2-spreadsheet-recipe.md); the
row anchors, constants zone (`README!B4` = 1950-01, `B5` = 2013-12, `B6` =
0.001), and alignment rule carry over unchanged.

Any deviation MUST be recorded as a discretionary choice in
[execution-log.md](../execution-log.md).

Provenance of this record ([RG008](../../../../governance/rules/RG008-authorship-provenance.md)):

| Field | Value |
|-------|-------|
| `created-by-type` | `agent` |
| `created-by` | AI assistant (Buffy) in Freebuff, on direction of the project owner |
| `created-by-version` | not available |
| `production-tools` | Freebuff (Buffy coding agent) |
| `created-at` | 2026-09-15T11:13:37+03:30 |

---

## Window sizes (if the last complete month is 2026-08)

| Window | Months | Rows in `Data` |
|--------|--------|----------------|
| IS: 1950-01 → 2013-12 | 768 | 15–782 |
| OOS: 2014-01 → 2026-08 | 152 | 783–934 |
| Total (1950-01 → 2026-08) | 920 | 15–934 |

The identity IS + OOS = total (768 + 152 = 920) is checklist item 1. If step 2a
found a different last complete month, recompute all three numbers from the
step-2 row anchors before anything else.

## What the step-2 table already provides

- Rule and benchmark monthly returns for every month 1950-01 → last complete
  month (`Data!I`, `Data!J`), with costs already applied in `I`.
- The cash monthly rate (`Data!E`), used as the risk-free input to Sharpe.
- The IS marker column `K` (non-blank exactly on IS rows), usable as a window
  filter so windows are read from the constants, never retyped.

## Two conventions fixed before any result is seen

These are definitional, recorded here and in the log as discretionary choices —
both were open in the design artifact:

| # | Convention | Chosen | Reason |
|---|------------|--------|--------|
| 1 | **Wealth units** | Wealth anchors at 1.0000 on the 1949-12 row (`L14`/`M14` = 1.0000 constants); the first applied month is 1950-01. `W_t = W_{t−1} × (1 + r_t)` for every month from 1950-01 on. | Wealth-minus-one is the compounding of the monthly return series; the same convention serves both windows via ratios (see annualized return below). |
| 2 | **Drawdown** | `DD_t = 1 − W_t / MAX(W from row 14 through t)`; `MDD = MAX(DD)` over the window's rows. | Standard running-peak drawdown; the row-14 anchor (W = 1.0000 at 1949-12) is part of the peak history. |

## Columns L–P (extend `Data`; fill rows 15–934)

| Col | Header | Formula | Notes |
|-----|--------|---------|-------|
| L | `rule_wealth` | `L14` = `1.0000` (constant); `L15` = `=L14*(1+I15)`, fill down | Uses return column **I** (all months), never K — K is a window marker that blanks OOS rows, not a return |
| M | `bench_wealth` | `M14` = `1.0000` (constant); `M15` = `=M14*(1+J15)`, fill down | Same convention |
| N | `rule_dd` | `=1-L15/MAX(L$14:L15)`, fill down | Row 14 itself: DD = 0 by definition (peak = W) |
| O | `bench_dd` | `=1-M15/MAX(M$14:M15)`, fill down | Same |
| P | `rf_monthly` | `=E15/100`, fill down | Risk-free decimal per month; the Sharpe excess-return input |

After entering row 15 formulas, select `L15:P15` and copy down as a block to
row 934 so nothing is left blank.

Also record on `Checks`: `L14` and `M14` equal 1.0000 exactly, and every `L`/`M`
cell is positive (a zero or negative wealth cell means a return ≤ −100% entered
somewhere — stop and find it).

## Aggregation (`Metrics` tab)

Add a sixth tab, `Metrics`. New constant on `README`: `B7` = last complete month
(2026-08), same date type as column A, with the same sanity test as B4/B5.
`B7` is the OOS start constant — the single-condition OOS formulas above key
on `">="&B7` — and, once entered, it also serves as the boundary spot value
for the step-2 checklist item 7 (a `K` cell at or after `B7` MUST be blank).

For each of {rule, benchmark} × {IS, OOS}, compute (rule shown; benchmark swaps
`I`→`J`, `L`→`M`, `N`→`O`; % invested and switches are rule-construction
columns, so the benchmark's cells there are 100% and 0 by construction):

| Metric | IS formula | OOS formula |
|--------|------------|-------------|
| n months | `=COUNTIFS(Data!$A$15:$A$934,">="&README!$B$4,Data!$A$15:$A$934,"<="&README!$B$5)` | `=COUNTIFS(Data!$A$15:$A$934,">="&README!$B$7)` |
| annualized return (geometric, headline) | `=L782^(12/768)-1` | `=(L934/L782)^(12/152)-1` |
| annualized volatility | `=STDEV(Data!$I$15:$I$782)*SQRT(12)` | `=STDEV(Data!$I$783:$I$934)*SQRT(12)` |
| Sharpe | `=(AVERAGE(Data!$I$15:$I$782)-AVERAGE(Data!$P$15:$P$782))/STDEV(Data!$I$15:$I$782)*SQRT(12)` | same on rows 783–934 |
| maximum drawdown | `=MAX(Data!$N$15:$N$782)` | `=MAX(Data!$N$783:$N$934)` |
| % months invested | `=AVERAGEIFS(Data!$G$15:$G$934,Data!$A$15:$A$934,">="&README!$B$4,Data!$A$15:$A$934,"<="&README!$B$5)` | `=AVERAGEIFS(Data!$G$15:$G$934,Data!$A$15:$A$934,">="&README!$B$7)` |
| switches | `=SUMIFS(Data!$H$15:$H$934,Data!$A$15:$A$934,">="&README!$B$4,Data!$A$15:$A$934,"<="&README!$B$5)` | `=SUMIFS(Data!$H$15:$H$934,Data!$A$15:$A$934,">="&README!$B$7)` |
| total cost drag | `=switches_IS * README!$B$6` | `=switches_OOS * README!$B$6` |

OOS one-condition formulas are written out in full: `COUNTIFS`, `AVERAGEIFS`,
and `SUMIFS` each take a single criteria pair here, keyed on `">="&README!$B$7` —
no second condition is needed because OOS is everything after the IS end. If
Excel rejects one of these on the installed version, use the same function with
both bounds (`">="&README!$B$7` and `"<="&README!$B$8`) — never a plain
`COUNT`/`AVERAGE`/`SUM` over a pasted range, which breaks the constants-zone
principle. Note the cell collision: `README!B8` is otherwise defined at step 7
as the 0 bps cost constant. If B8 was consumed here as the last complete month,
the step-7 cost constants MUST take other cells and the step-7 recipe's B8/B9
references shift accordingly, with the deviation logged.

Definitions and warnings:

- **Geometric annualized return is taken from the wealth columns**, not from a
  sum of returns: IS compounds W from 1.0000 (1949-12 anchor) to `L782`;
  OOS compounds the OOS-only leg as the ratio `L934/L782`. The exponent is
  `12/n` with the window's own n. The arithmetic approximation
  (mean monthly return × 12) is NOT the headline number; if reported at all,
  it is a robustness footnote, because it overstates the exact figure by an
  amount that grows with mean return and volatility.
- **Sharpe** uses the monthly excess mean over the monthly standard deviation,
  annualized by √12: `(mean(r) − mean(rf)) / stdev(r) × √12`, sample standard
  deviation (n−1). This is the definition used everywhere in this experiment.
  It is not algebraically identical to (annual excess) / (annual vol); the
  two differ by a convexity term when the risk-free mean is nonzero. No other
  Sharpe variant may be substituted without a logged discretionary choice.
- **Fixed ranges** (`$15:$782`, `$783:$934`) are acceptable here only because
  the row anchors are verified (step-2 checklist item 7 and the n-months
  identity below); enter each fixed range once, from the anchor table, and do
  not retype it per formula — copy the formula across the rule/benchmark pair
  and edit only the column letter.
- **OOS max drawdown reads the full-history running peak** (`N`/`O` start at
  row 14), so the OOS peak may sit in the IS window — the standard
  "drawdown from all-time high" reading. The alternative (peak reset at
  2014-01) is a different number; whichever is used for the primary table,
  the other is reported as a robustness footnote. Record the choice in the
  discretionary-choices log when RESULTS.md is written.

Lay the results out on `Metrics` as a 2×2 grid (rows: rule, benchmark;
columns: IS, OOS), one row of cells per metric, so the numbers can be
transcribed to `RESULTS.md` without re-computation.

## Primary result ordering (procedure step 6)

Step 5 ends when the `Metrics` tab is complete and `Checks` records the
wealth sanity cells and the n-months identity checks. **Then, and only
then**, transcribe the primary result (Sharpe difference and MDD difference,
rule − benchmark, for IS and OOS) into `RESULTS.md` — before any robustness
check is run (procedure step 6; the ordering is the safeguard). Robustness
checks (lookback, cost, timing, sub-period) are step 7 and get their own
recipe or a direct extension.

## Verification checklist

1. **n-months identity**: rule-IS n = 768, rule-OOS n = 152, sum = 920; same
   for benchmark (recompute from the anchor table if the last month differs).
2. **Wealth positivity** on all L/M cells; anchors L14 = M14 = 1.0000.
3. **Hand-verify one wealth step** on a calculator, from the displayed cells:
   W_t = W_{t−1} × (1 + r_t).
4. **Drawdown spot check:** one row below its prior peak — DD = 1 − W/peak
   matches by hand; one row at a fresh high — DD = 0.
5. **Cost drag identity:** rule cost drag (IS + OOS) equals
   ΣH(all months) × 0.001, and ΣH(all months) equals the count of position
   changes including the first entry (the H15 flat-book convention from the
   step-2 recipe).
6. **Metric transcription:** every cell of the 2×2 `Metrics` grid goes to
   `RESULTS.md` unchanged — full displayed precision, no rounding at
   transcription.

Each failed check is a finding: log it, fix, re-run.

## Correction record

Made before the recipe was first used; nothing was computed from the
superseded text.

| # | Date | Correction |
|---|------|------------|
| 1 | 2026-09-15 | The annualized-return definition moved between the exact compounding form and the sum-of-returns × 12 approximation during authoring. Final: the **exact geometric form from the wealth columns** is the headline number; the ×12 arithmetic form may appear only as a robustness footnote. |
| 2 | 2026-09-15 | An early draft called the monthly mean-excess Sharpe form "equivalent" to the annualized-ratio form. They are not identical in general (the difference is a convexity term when the risk-free mean is nonzero). Final: the explicit monthly form `(mean(r) − mean(rf)) / stdev(r) × √12` is the single definition used. |
| 3 | 2026-09-15 | The wealth anchor was first described as starting at the 1950-01 row, which leaves the first month's wealth step undefined. Final: W = 1.0000 anchors on the 1949-12 row (`L14`/`M14`), first applied month 1950-01. |
