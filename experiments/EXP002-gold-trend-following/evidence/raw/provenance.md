# EXP002 Raw Data Provenance

Files in `raw/` are stored exactly as received and are immutable
([PR003](../../../../principles/PR003-raw-data-immutable-derived-traceable.md),
[G001](../../../../governance/G001-research-governance.md)). This file records
what was received, when, from where, by what means, and how it was verified.
Nothing here is edited after writing; corrections are appended as new dated
entries.

Provenance of this record
([RG008](../../../../governance/rules/RG008-authorship-provenance.md)):

| Field | Value |
|-------|-------|
| `created-by-type` | `agent` |
| `created-by` | AI assistant (Cline) |
| `created-by-version` | not available |
| `production-tools` | VS Code, AI assistant (Cline); PowerShell 7 `Get-FileHash` (SHA256); Python 3 stdlib |
| `created-at` | 2026-09-30T23:55:00+03:30 |

---

## File 1 — `XAUUSD-TICK.csv` (spot gold; [Q003](../../../../questions/Q003-long-only-gold-trend-following.md), [SRC006](../../../../sources/SRC006-dukascopy-historical-data-export.md))

| Field | Value |
|-------|-------|
| Instrument | XAU/USD (spot gold quoted in US dollars) |
| Supplied by | the researcher, manually, placed into `raw/` |
| Acquisition channel | **manual download via SQX** — NOT the Dukascopy public-site widget named in Q003/S005/SRC006 |
| File format | CSV text, comma-separated (`DateTime,Bid,Ask,Volume`); naive timestamps, no time-zone field |
| Size | 864,476,202 bytes |
| SHA-256 | `a3bf035c857dde9193b12973ab65e99bdaa5e11c757809ffad19d3d415f84fb1` (compare case-insensitively) |
| Coverage (observed) | 2003-05-05 through 2005-12-30 |
| Data rows | 20,561,312 (excluding header) |

### Verification performed (on the stored bytes)

- **Identity** — byte size and SHA-256 computed from the file as stored
  (`Get-FileHash -Algorithm SHA256`).
- **Structure** — 20,561,312 data rows; **0 rows** with a field count other
  than 4.
- **Header** — exactly `DateTime,Bid,Ask,Volume`.
- **DateTime** — format `YYYYMMDD HH:MM:SS.mmm` (e.g.
  `20030505 03:01:03.421`); naive (no offset/label column).
- **Bid/Ask coherence** — both fields present on every row; **0 rows** with
  `Ask < Bid` (no crossed/impossible quotes).
- **Coverage** — 697 distinct calendar days; first `20030505`, last `20051230`;
  the day sequence is non-decreasing in file order.

### Findings requiring reconciliation ([RG009](../../../../governance/rules/RG009-claim-provenance.md))

1. **Coverage deviation — blocker.** Observed coverage is **2003-05-05 to
   2005-12-30**. The pre-registered export is reported in S005/SRC006/Q003 as
   `5/5/2003`–`28/9/2026`. The supplied file covers only roughly the first two
   and a half years and **does not reach the fixed holdout window
   `2020-09-28`–`2026-09-28`**. As supplied, this file cannot support the
   pre-registered six-year out-of-sample test and is **not** the pre-registered
   dataset.
2. **Format deviation.** Pre-registered: two separate `Tick`-selected exports
   (Bid and Ask), each carrying `Open, High, Low, Close, Volume`, matched by
   timestamp. Supplied: one combined CSV with `Bid` and `Ask` on the same row
   and a **single `Volume`** column; **no OHLC columns**.
3. **Route deviation.** Pre-registered: Dukascopy public-site widget export.
   Supplied: manual SQX download.
4. **Time zone unresolved.** Pre-registered rows reportedly carry a
   `Europe/Amsterdam` label. The supplied file has a **naive `DateTime` with no
   time-zone field**; the zone the timestamps are expressed in is unconfirmed.

### Not yet verified

- Full within-day timestamp monotonicity/ordering (only day-level ordering was
  checked).
- Handling of second-level duplicate timestamps.
- Internal gap structure and empty periods; whether the observed 2003–2005 span
  is itself complete or a partial slice of a larger export.
- Whether `Volume` is meaningful for this instrument.
- The time zone of the naive timestamps.

### Disposition

The file is stored as the **raw master** under the Option-1 storage decision
(see `README.md`) and is immutable from now on. It **MUST NOT** be treated as
the pre-registered EXP002 dataset: the coverage deviation alone prevents the
frozen `2020-09-28`–`2026-09-28` holdout test. Reconciliation of the
coverage/format/route deviations in `Q003`, `S005`, `SRC006`, and the Artifact
Registry — and a decision on obtaining the full `2003`–`2026` export — are
required **before** any derived series or backtest is produced.

---

## File 2 — `XAUUSD-TICK-full.csv` (full-range spot gold) — received 2026-10-02

A second, **full-range** combined tick export was placed in `raw/` on
2026-10-02. It supersedes File 1 as the *coverage-complete* raw master; File 1
remains immutable and is retained as the earlier partial slice. This entry is
appended, not edited in place ([G001](../../../../governance/G001-research-governance.md)).

| Field | Value |
|-------|-------|
| Instrument | XAU/USD (spot gold quoted in US dollars) |
| Supplied by | the researcher, manually, placed into `raw/` |
| Acquisition channel | manual download via SQX (same channel as File 1) |
| File format | CSV text, comma-separated (`DateTime,Bid,Ask,Volume`); naive timestamps, no time-zone field |
| Size | 32,121,180,517 bytes (29.92 GiB) |
| SHA-256 | `4921484ac6a70654c187e0b097c66dedca26c21f2eb398bce5e4bcfbcead17d4` (compare case-insensitively) |
| Coverage (observed) | 2003-05-05 03:01:03.421 through 2026-10-02 02:59:57.675 |
| Data rows | 732,112,910 (excluding header) |
| Distinct calendar days | 6,089 |

Provenance of this record
([RG008](../../../../governance/rules/RG008-authorship-provenance.md)):

| Field | Value |
|-------|-------|
| `created-by-type` | `agent` |
| `created-by` | AI assistant (Cline) |
| `created-by-version` | not available |
| `production-tools` | VS Code, AI assistant (Cline); PowerShell 7; Python 3 stdlib (`tools/verify_full.py`) |
| `created-at` | 2026-10-02T23:39:00+03:30 |

### Verification performed (on the stored bytes)

Full, streaming pass over the entire file — **no strategy signal or return was
computed** (Q003 freeze discipline). Machine-readable report:
[`evidence/derived/verification-report.json`](../derived/verification-report.json);
raw log: [`evidence/derived/verification.log`](../derived/verification.log).

- **Identity** — two independent full reads: binary SHA-256
  (`4921484a…ad17d4`) over all 32,121,180,517 bytes, and a byte count matching
  the on-disk size.
- **Header** — exactly `DateTime,Bid,Ask,Volume` (passed).
- **Rows** — 732,112,910 data rows; **0** rows with a field count other than 4.
- **DateTime** — every row matches `YYYYMMDD HH:MM:SS.mmm`; **0** malformed.
- **Numeric fields** — Bid/Ask/Volume present and parseable on every row;
  **0** bad rows; **0** non-positive prices.
- **Bid/Ask coherence** — **0** crossed quotes (`Ask < Bid`).
- **Ordering** — timestamps are **monotonically non-decreasing in file order**
  (0 violations), i.e. the fixed-width zero-padded format sorts chronologically.
- **Duplicate second-level timestamps** — 487,749,622 rows share the same
  whole second as the preceding row (different milliseconds). This is **expected
  for tick data** (many ticks per second), not an error; within-second ordering
  is captured by the monotonicity check above.
- **Coverage** — 2003-05-05 through 2026-10-02; 6,089 distinct calendar days;
  day sequence non-decreasing. This **spans the frozen
  `2020-09-28`–`2026-09-28` holdout window**.

Per-year row counts:

| Year | Rows | Year | Rows |
|------|------|------|------|
| 2003 | 2,814,818 | 2015 | 25,767,278 |
| 2004 | 7,313,843 | 2016 | 46,186,146 |
| 2005 | 10,475,251 | 2017 | 45,837,010 |
| 2006 | 12,836,627 | 2018 | 35,920,345 |
| 2007 | 5,370,861 | 2019 | 36,813,971 |
| 2008 | 3,757,600 | 2020 | 55,804,045 |
| 2009 | 4,111,100 | 2021 | 53,099,638 |
| 2010 | 13,117,589 | 2022 | 53,849,099 |
| 2011 | 17,581,570 | 2023 | 36,422,900 |
| 2012 | 23,133,883 | 2024 | 56,217,145 |
| 2013 | 23,175,738 | 2025 | 71,415,016 |
| 2014 | 21,567,492 | 2026 | 69,523,945 |

### Findings ([RG009](../../../../governance/rules/RG009-claim-provenance.md))

1. **Coverage deviation — RESOLVED.** Observed coverage 2003-05-05 to
   2026-10-02 now spans the pre-registered `5/5/2003`–`28/9/2026` window and the
   frozen `2020-09-28`–`2026-09-28` holdout. The tail extends slightly past the
   reported end date (to 2026-10-02), which is noted but immaterial to the frozen
   windows.
2. **Format deviation — still open.** Supplied is one combined CSV with `Bid`
   and `Ask` on the same row and a **single `Volume`** column; **no OHLC
   columns**. Pre-registered: two separate `Tick`-selected exports (Bid and Ask),
   each carrying `Open, High, Low, Close, Volume`, matched by timestamp.
3. **Route deviation — still open.** Pre-registered: Dukascopy public-site
   widget export. Supplied: manual SQX download.
4. **Time zone unresolved.** The `DateTime` is naive (no time-zone field); the
   zone the timestamps are expressed in remains unconfirmed (pre-registered rows
   reportedly carry a `Europe/Amsterdam` label).

### Not yet verified

- The time zone of the naive `DateTime` (same open item as File 1).
- Internal gap structure and empty periods (weekends/holidays); whether the
  observed span is continuous.
- Whether `Volume` is meaningful for this instrument.

### Disposition

The file is stored as the **full-range raw master** under the Option-1 storage
decision (see `README.md`) and is immutable from now on. It is the
**coverage-complete** dataset for EXP002. The format and route deviations in
`Q003`/`S005`/`SRC006` and the Artifact Registry must still be reconciled per
[RG009](../../../../governance/rules/RG009-claim-provenance.md) before any derived
series or backtest is produced.

---

## Immutability

From this point the file MUST NOT be modified, renamed, or re-downloaded in
place ([G001](../../../../governance/G001-research-governance.md)). If a
refreshed or full-range copy is obtained, it is stored as a **new file with its
own provenance entry**; any `derived/` regeneration instruction must then
reference the exact file it used. Because the raw master is not committed (see
`README.md`), the recorded SHA-256 is the anchor that detects any substitution
or corruption.