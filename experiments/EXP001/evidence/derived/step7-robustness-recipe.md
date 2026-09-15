# EXP001 Step 7 — Robustness Recipe

Procedure step 7 of [EXP001](../../EXP001-momentum-replication.md): run the four
robustness checks and append each to `RESULTS.md` §2. This recipe pre-registers
every specification variant — signals, columns, windows, and conventions — so
that execution involves no design discretion. Manual spreadsheet work only
([DEC001](../../../../decisions/DEC001-no-software-before-method.md)). Extends
[step2-spreadsheet-recipe.md](step2-spreadsheet-recipe.md) and
[step5-metrics-recipe.md](step5-metrics-recipe.md); their row anchors, constants
zone, and conventions carry over unchanged.

Provenance of this record ([RG008](../../../../governance/rules/RG008-authorship-provenance.md)):

| Field | Value |
|-------|-------|
| `created-by-type` | `agent` |
| `created-by` | AI assistant (Buffy) in Freebuff, on direction of the project owner |
| `created-by-version` | not available |
| `production-tools` | Freebuff (Buffy coding agent) |
| `created-at` | 2026-09-15T12:04:11+03:30 |

---

## Execution gate

Robustness checks run **only after** `RESULTS.md` §1 (primary result) is
recorded — the procedure step-6 ordering safeguard
([step5-metrics-recipe.md](step5-metrics-recipe.md), "Primary result
ordering"). Then:

1. Add all robustness columns (Q–AI below) to the `Data` tab in **one logged
   action** before any robustness number is computed; note the action in
   [execution-log.md](../execution-log.md).
2. Run the checks in the design's order: lookback, cost, timing, sub-period.
3. After each check, append its subsection to `RESULTS.md` §2 **before** the
   next check is computed.

## Scope guardrails

- These four checks only. No additional perturbations, no parameter search —
  the design's failure criteria forbid unlabeled exploratory runs.
- Robustness checks test **sign stability of the Sharpe difference** (and
  report MDD differences). The pre-declared 0.1 bound applies to the primary
  OOS finding, not here; do not import it.
- A variant that outperforms the main specification does not replace it. The
  main specification (12-month lookback, 10 bps, no skip) is frozen.

## New constants (`README` tab)

| Cell | Value | Meaning |
|------|-------|---------|
| `B8` | 0.000 | Check 2 low cost (0 bps per switch) |
| `B9` | 0.003 | Check 2 high cost (30 bps per switch) |

## New columns (one-time addition, `Data` tab)

Reference columns from steps 2/5: `C` m_ret, `E` tbill_monthly, `G` position,
`H` switch, `I` rule_ret, `J` benchmark_ret, `N`/`O` drawdowns. `README!$B$6`
= 0.001 (main cost). Formulas shown at the first row of each column; fill to
row 934 unless noted.

### Check 1 + 3 columns — lookback and timing variants

Position at row *t* = 1 if the variant signal at month *t−1* was positive,
written directly as a price ratio over `Price!B`:

| Col | Variant | First row | Position formula (first row) | Return formula (first row) |
|-----|---------|-----------|------------------------------|----------------------------|
| S | lookback 10 | 15 | `=IF(Price!B14/Price!B4-1>0,1,0)` | `W15`: `=S15*C15+(1-S15)*E15-ABS(S15-S14)*README!$B$6` |
| T | lookback 11 | 15 | `=IF(Price!B14/Price!B3-1>0,1,0)` | `X15`: same pattern on `T` |
| U | lookback 13 | 16 | `=IF(Price!B15/Price!B2-1>0,1,0)` | `Y16`: same pattern on `U` |
| V | lookback 14 | 17 | `=IF(Price!B16/Price!B2-1>0,1,0)` | `Z17`: same pattern on `V` |
| AA | 12-1 (skip latest month) | 16 | `=IF(Price!B14/Price!B2-1>0,1,0)` | `AB16`: same pattern on `AA` |

Return columns: `W` (L10) from 15, `X` (L11) from 15, `Y` (L13) from 16,
`Z` (L14) from 17, `AB` (12-1) from 16. In each return formula,
`ABS(pos_t − pos_{t−1})` is the variant's switch indicator; at the variant's
first applied row the cell above is genuinely blank, so the flat-book entry
convention applies (cost paid iff the first position is long) — the same
convention as `H15` in the main table.

Variant windows (return rows): IS = first applied row → 782; OOS = 783 → 934
(152 months, all variants). IS n: 768 (L10, L11), 767 (L13, 12-1), 766 (L14).
The warm-up difference is inherent to the longer lookbacks; report each n.

### Check 2 columns — cost perturbation

Positions and switches are the **main rule's** (`G`, `H`) — cost perturbation
does not change the all-or-nothing positions, only the drag:

| Col | Variant | First row | Formula |
|-----|---------|-----------|---------|
| Q | rule return, 0 bps | 15 | `=G15*C15+(1-G15)*E15-H15*README!$B$8` |
| R | rule return, 30 bps | 15 | `=G15*C15+(1-G15)*E15-H15*README!$B$9` |

Windows identical to the main rule: IS 15–782 (768), OOS 783–934 (152).
The benchmark is unchanged by cost (no switches); `J` serves all comparisons.

### Wealth columns (for variant MDD only)

One wealth column per variant return column, for running-peak drawdown:

| Col | Compounds | Anchor |
|-----|-----------|--------|
| AC | `W` (L10) | `AC14` = 1.0000; `AC15` = `=AC14*(1+W15)` |
| AD | `X` (L11) | `AD14` = 1.0000; from 15 |
| AE | `Y` (L13) | blank to 15; `AE16` = `=1*(1+Y16)` (rule starts at first applied row) |
| AF | `Z` (L14) | blank to 16; `AF17` = `=1*(1+Z17)` |
| AG | `Q` (0 bps) | `AG14` = 1.0000; from 15 |
| AH | `R` (30 bps) | `AH14` = 1.0000; from 15 |
| AI | `AB` (12-1) | blank to 15; `AI16` = `=1*(1+AB16)` |

Fill each down to row 934. Variant MDD over a window = `MAX(1 − W_t /
MAX(W$first−1:W_t))` over the window's rows; for variants anchored later, the
peak history starts at the anchor row (the flat period is not part of the
variant's book). State this convention in RESULTS §2 the first time an MDD
difference for a late-anchored variant is reported.

## The four checks and what gets appended

Each check's RESULTS §2 subsection states: the specification variant, the
Sharpe difference (variant rule − benchmark) for IS and OOS, the MDD
difference, whether the Sharpe-difference **sign holds** versus the primary
result, and the n months on each side.

**Like-for-like rule:** when a variant's window is shorter (L13, L14, 12-1 IS),
the benchmark side of the difference is computed on the **same rows** as the
variant (e.g. rows 17–782 for L14), using `J` and the same formulas as the
step-5 `Metrics` tab. All three Sharpe inputs — the variant return column, the
benchmark return column `J`, and the risk-free column `P` — likewise use those
same rows. The §1 benchmark numbers are not re-used for these differences and
are not altered.

1. **Lookback perturbation** — four variants: 10 (S/AC), 11 (T/AD), 13 (U/AE),
   14 (V/AF). Sharpe from the variant return column per window; MDD from its
   wealth column; benchmark per the like-for-like rule.
2. **Cost perturbation** — two variants: 0 bps (Q/AG), 30 bps (R/AH), against
   the standard benchmark windows (15–782, 783–934). Report the cost drag
   per window (`ΣH × cost`) alongside.
3. **Signal timing (12-1)** — one variant: AA/AI. Same reporting.
4. **Sub-period split** — no new columns; split the OOS window of the **main
   specification** (`I`, `J`, `N`, `O`): first half rows 783–858 (2014-01 →
   2020-04, 76 months), second half rows 859–934 (2020-05 → 2026-08,
   76 months). Report Sharpe difference and MDD difference per half. MDD per
   half reads the full-history running peak (consistent with the §1
   convention; the peak may lie before the half — state it).

## Verification checklist

1. **Gate check:** RESULTS §1 recorded before any robustness column is added;
   the one-time column addition is logged.
2. **Formula spot-check:** three cells across the new columns match this
   recipe text exactly.
3. **Hand-verify one signal per check** from raw prices on a calculator:
   L13 signal for 1950-02 = Price row 15 / row 2 − 1; 12-1 signal for
   1950-02 = row 14 / row 2 − 1; the 30 bps return of row 15 equals the main
   `I15` plus `H15 × (0.001 − 0.003)`.
4. **Switch sanity:** each variant's ΣH(all months) equals its signal-flip
   count plus the first entry; verify one variant by counting position changes.
5. **n identity:** per variant, IS n + 152 = total applied rows
   (768+152, 767+152, or 766+152); check 4: 76 + 76 = 152.
6. **Wealth positivity** on AC–AI; anchors per the table above.
7. **Append order:** each RESULTS §2 subsection is dated and appended before
   the next check runs; no check is rerun to produce a flatter sign.

Each failed check is a finding: log it, fix, re-run.

## Correction record

| # | Date | Correction |
|---|------|------------|
| 1 | 2026-09-15 | Authoring correction before first use: the OOS sub-period boundary was first sketched as a calendar-year split (2014→2019 | 2020→2026). The equal-months halves of rows 783–934 are 2014-01→2020-04 and 2020-05→2026-08 (76 + 76). Fixed above. |
