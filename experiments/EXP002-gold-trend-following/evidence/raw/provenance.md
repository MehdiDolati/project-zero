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

## Immutability

From this point the file MUST NOT be modified, renamed, or re-downloaded in
place ([G001](../../../../governance/G001-research-governance.md)). If a
refreshed or full-range copy is obtained, it is stored as a **new file with its
own provenance entry**; any `derived/` regeneration instruction must then
reference the exact file it used. Because the raw master is not committed (see
`README.md`), the recorded SHA-256 is the anchor that detects any substitution
or corruption.