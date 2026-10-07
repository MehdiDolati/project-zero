# EXP002 Derived Evidence Area

This directory holds the derived artifacts for the gold trend-following
question ([Q003](../../../../questions/Q003-long-only-gold-trend-following.md)).
Everything here is produced deterministically from the immutable raw master
([PR003](../../../../principles/PR003-raw-data-immutable-derived-traceable.md));
nothing here is hand-edited.

Provenance of this record
([RG008](../../../../governance/rules/RG008-authorship-provenance.md)):

| Field | Value |
|-------|-------|
| `created-by-type` | `agent` |
| `created-by` | AI assistant (Cline) |
| `created-by-version` | not available |
| `production-tools` | VS Code, AI assistant (Cline), Python 3; versions not available |
| `created-at` | 2026-10-07T23:55:00+03:30 |

> **Disclosure — mandatory caveats (DEC002, Q003).** The naive `DateTime` time
> zone, the meaning of the single `Volume` column, and the internal
> gap/empty-day structure of the source master remain **unverified**. Fixed
> UTC+02 bucketing is applied as a frozen research convention, not a verified
> exchange-calendar fact. No strategy result here is evidence that gold always
> rises, that trend following is profitable, or that any edge exists.

---

## Contents

| File | What it is |
|------|------------|
| `daily-bars-utc02.csv` | Daily bars built from the raw master under the frozen fixed-UTC+02 convention |
| `daily-bars-summary.json` | Machine-readable build summary |
| `backtest-summary.json` | Machine-readable backtest summary (frozen baseline) |
| `backtest-trades.csv` | Per-trade log of the frozen baseline |
| `verification-report.json`, `verification.log` | Raw-master structural verification (2026-10-02) |

---

## 1. Daily bars (`daily-bars-utc02.csv`)

Built with `../../tools/build_daily_bars.py` from the raw master
`../raw/XAUUSD-TICK-full.csv` (32,121,180,517 bytes; SHA-256
`4921484ac6a70654c187e0b097c66dedca26c21f2eb398bce5e4bcfbcead17d4`).

- **Convention:** each instant converted to fixed **UTC+02**, bucketed into
  `[00:00, 00:00 next day)`. Per side (`Bid`, `Ask`) independently: first row =
  Open, maximum = High, minimum = Low, last row = Close. Source row order
  preserved for duplicate timestamps. Days with no records omitted (no
  forward-fill).
- **Output:** `Date,Bid_Open,Bid_High,Bid_Low,Bid_Close,Ask_Open,Ask_High,Ask_Low,Ask_Close,Volume,RowCount`
- **Rows:** 2,260 daily bars, `2018-01-02` → `2026-10-02`.
- **Integrity:** SHA-256 `57c5b63e62bf52d0e1f395afcdff7e15491870e83bdeef25e179de229fda1f5b`,
  218,864 bytes.
- **Build summary:** 732,112,910 source rows; 0 malformed; 0 bad numerics;
  469,066,104 rows within emitted bars; min 4,732 / max 843,111 rows per bar.
  Bars are emitted from `2018-01-01` so the first in-window signal has a full
  200-bar warm-up.

## 2. Frozen baseline backtest (`backtest-summary.json`, `backtest-trades.csv`)

Run with `../../tools/backtest_sma200.py`, implementing **exactly** the Locked
Baseline Strategy frozen in Q003 (approved 2026-09-29, before any
evaluation-period returns were examined). Window `2020-09-28`–`2026-09-28`
inclusive (1,549 daily bars).

| Metric | Strategy | Buy-and-hold benchmark |
|--------|----------|------------------------|
| Final equity (start 1.0) | **1.099101** | 2.210240 |
| Total return | **+9.91%** | +121.02% |
| CAGR | **+1.59%** | +14.14% |
| Max drawdown | **-25.92%** | -26.60% |

Activity: 32 trades; avg holding 31.1 days; max 365 days; 45.19% of time
invested; exits 31 signal / 1 time_stop / 0 window_end.

## 3. Cost inventory (commission and financing/swap)

The frozen rule "include historical commissions and financing/swap charges
where reliable records are available" was actioned as follows:

- **Commission records:** none located in the repository or supplied by the
  researcher for the evaluation period.
- **Financing/swap records:** none located; no broker/account statement was
  provided for XAU/USD carry over `2020-09-28`–`2026-09-28`.
- **Outcome:** no reliable cost records exist, so commission and
  financing/swap charges are **excluded** and the result is **net of quoted
  spread only** (Ask entries / Bid exits). Per Q003, results MUST NOT be
  described as fully net of costs.

**Why this matters for interpretation.** After the 2024-10-18 time stop the
rule stayed flat through gold's largest advance until the 2026-08-20 re-entry,
so the strategy captured little of the move. A +9.9% spread-only total over six
years (~+1.59% CAGR) is small enough that unmodelled commissions and any
overnight financing would plausibly erase it, and it is dwarfed by the
buy-and-hold benchmark. **This baseline does not establish a profitable
edge**; it is a negative/weak result recorded as evidence, not a green light.

## 4. How to reproduce

```
python experiments/EXP002-gold-trend-following/tools/build_daily_bars.py
python experiments/EXP002-gold-trend-following/tools/backtest_sma200.py
```

Both tools read the local raw master and write only into this directory. The
raw master is not committed (see `../raw/README.md`); its recorded SHA-256 is
the anchor that detects substitution or corruption.