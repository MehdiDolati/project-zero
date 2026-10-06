# EXP002 Raw Evidence Area

This directory holds the raw data for the gold trend-following question
([Q003](../../../../questions/Q003-long-only-gold-trend-following.md)).

Files placed here are stored exactly as received and are immutable
([PR003](../../../../principles/PR003-raw-data-immutable-derived-traceable.md),
[G001](../../../../governance/G001-research-governance.md)). They must not be
edited, renamed, or re-downloaded in place. If a refreshed copy is ever needed,
it is stored as a new file with its own provenance entry, and any `derived/`
regeneration instruction must reference the exact file it used.

Provenance of this record
([RG008](../../../../governance/rules/RG008-authorship-provenance.md)):

| Field | Value |
|-------|-------|
| `created-by-type` | `agent` |
| `created-by` | AI assistant (Cline) |
| `created-by-version` | not available |
| `production-tools` | VS Code, AI assistant (Cline); versions not available |
| `created-at` | 2026-09-30T22:39:00+03:30 |

---

## Status

**File 2 received 2026-10-02 — full-range master.** A second combined CSV,
`XAUUSD-TICK-full.csv`, was placed here by the researcher: 32,121,180,517 bytes
(29.92 GiB), SHA-256
`4921484ac6a70654c187e0b097c66dedca26c21f2eb398bce5e4bcfbcead17d4`. A full
streaming pass over all 732,112,910 rows found **0** malformed rows, **0** bad
timestamps, **0** bad numerics, **0** crossed quotes, and **0** ordering
violations. Its coverage — **2003-05-05 to 2026-10-02** — now **spans the frozen
`2020-09-28`–`2026-09-28` holdout window**, resolving the coverage deviation
that blocked File 1. It is now the **coverage-complete** raw master for EXP002.
The **format** (single combined CSV, one `Volume`, no OHLC) and **route**
(manual SQX download) deviations were **accepted** by the researcher on
2026-10-06 in
[DEC002](../../../../decisions/DEC002-accept-amended-exp002-registration.md);
`Q003`/`SRC006` and the Artifact Registry are being reconciled to it. See
`provenance.md` for the full record.

**File 1 received 2026-09-30 — partial slice (superseded).** One combined CSV,
`XAUUSD-TICK.csv`, 864,476,202 bytes, SHA-256
`a3bf035c857dde9193b12973ab65e99bdaa5e11c757809ffad19d3d415f84fb1`. Its
identity and mechanical structure were verified, but its **coverage is a
partial slice — 2003-05-05 to 2005-12-30 only** — which does not reach the
frozen `2020-09-28`–`2026-09-28` holdout window. The file is retained as an
immutable raw master but is **NOT** the pre-registered dataset. See
`provenance.md` for the full verification record.

## Storage decision (raw master kept local, not committed)

The full `5/5/2003`–`28/9/2026` spot XAU/USD tick export is far larger than is
practical to store in Git. The researcher chose **Option 1** on 2026-09-30:

- the full raw export is preserved **locally** under this directory as the
  untouched, immutable master and is **not committed**;
- a root [`.gitignore`](../../../../.gitignore) rule excludes everything in this
  directory except this `README.md` and `provenance.md`, so only the non-data
  record files are tracked;
- the raw master's identity (filename, byte size, SHA-256) is recorded in
  `provenance.md`, so any holder of the master can verify it byte-for-byte;
- only the **derived** daily bars and their derivation recipe are committed.

This deviates from EXP001, where the raw files themselves are committed. It is
recorded here per
[RG009](../../../../governance/rules/RG009-claim-provenance.md) as a reasoned
substitution: the raw is preserved and identified, not discarded; the repository
carries the provenance anchor and the traceable derivation rather than the bulk
bytes.

**Durability caveat.** Because the raw master is not committed, reproducibility
depends on the researcher retaining a backed-up copy of it. If that copy is lost,
the raw cannot be re-verified from the repository alone. The recorded SHA-256 is
the anchor that detects any substitution or corruption.

## Expected file

| Field | Value |
|-------|-------|
| Instrument | XAU/USD (spot gold quoted in US dollars) — Q003 |
| Acquisition channel | Manual download from Dukascopy by the researcher (via SQX) |
| Format | CSV, comma-separated |
| Header | `DateTime, Bid, Ask, Volume` |
| Reported coverage | `5/5/2003`–`28/9/2026` (researcher-reported) |
| Observed coverage | **2003-05-05 to 2026-10-02** (full range; see File 2 in `provenance.md`) |
| Storage | Local master(s) retained, not committed (see Storage decision) |
| Location | `experiments/EXP002-gold-trend-following/evidence/raw/` |
| Status | **File 2 received 2026-10-02** (full coverage; coverage-complete master). File 1 (2026-09-30) retained as partial slice. |

## Discrepancy — resolved by DEC002 (2026-10-06)

`Q003`, `S005`, and `SRC006` originally recorded **two separate** Dukascopy
public-site exports (Bid and Ask), each `Tick`-selected, each carrying
`Open, High, Low, Close, Volume` per row and matched by timestamp. The file
supplied is **one combined CSV** carrying both `Bid` and `Ask` on the same row,
obtained through a **different channel** (a manual SQX download rather than the
public-site widget).

Both the format and the acquisition route therefore differed from the
pre-registered record. Per
[RG009](../../../../governance/rules/RG009-claim-provenance.md), substitutions
of route or specification are recorded explicitly, not silently accepted. On
2026-10-06 the researcher accepted the amended registration in
[DEC002](../../../../decisions/DEC002-accept-amended-exp002-registration.md):
the single combined `DateTime,Bid,Ask,Volume` CSV master (manual SQX download)
is now the EXP002 dataset. `Q003`/`SRC006` and the Artifact Registry are being
reconciled to it, and the residual unknowns (naive time zone, single `Volume`,
gap structure) are carried as explicit caveats.

## Verification status (2026-10-02) — File 2, full-range

The full-range file arrived and was checked **without examining strategy
returns**. Full record in `provenance.md`; machine-readable report in
`evidence/derived/verification-report.json`. Summary:

- **Verified** — identity (byte size, SHA-256); header
  `DateTime,Bid,Ask,Volume`; **732,112,910 data rows**; 0 malformed rows;
  0 bad timestamps; 0 bad numerics; 0 non-positive prices; 0 crossed quotes
  (`Ask < Bid`); timestamps monotonically non-decreasing in file order.
- **Observed coverage** — 2003-05-05 to 2026-10-02 (6,089 distinct days), which
  **spans the frozen `2020-09-28`–`2026-09-28` window**. Coverage deviation from
  File 1 is **resolved**.
- **Still unverified** — time zone of the naive `DateTime`; internal gap/empty
  structure; whether `Volume` is meaningful here.
- **Deviations — accepted by DEC002 (2026-10-06)** — format (single combined
  CSV, one `Volume`, no OHLC, vs two OHLC tick exports) and route (manual SQX
  download vs the public-site widget named in Q003/SRC006) were accepted as an
  amended registration; the original pre-registration is preserved.

## Verification status (2026-09-30) — File 1, partial slice

The file has arrived and was checked **without examining strategy returns**.
Full record in `provenance.md`; summary:

- **Verified** — file identity (byte size, SHA-256); header
  `DateTime,Bid,Ask,Volume`; 20,561,312 data rows; 0 malformed rows; Bid/Ask
  present on every row with no crossed quotes (`Ask < Bid`: 0).
- **Observed coverage** — 2003-05-05 to 2005-12-30 (697 distinct days), a
  **partial slice** that does **not** reach the frozen `2020-09-28`–`2026-09-28`
  window.
- **Still unverified** — full within-day timestamp ordering; duplicate-timestamp
  handling; gap/empty-period structure; whether `Volume` is meaningful here;
  and the time zone of the naive `DateTime`.
- **Deviations to reconcile before use** — coverage (partial vs
  `5/5/2003`–`28/9/2026`), format (single combined CSV with one `Volume`, no
  OHLC, vs two OHLC tick exports), and route (manual SQX download vs the
  public-site widget named in Q003/S005/SRC006).

The immutable `provenance.md` for the file was written on arrival, following
the convention used in
[EXP001 raw provenance](../../EXP001/evidence/raw/provenance.md).

## Immutability

From the moment a data file is placed here it MUST NOT be modified, renamed, or
re-downloaded in place ([G001](../../../../governance/G001-research-governance.md)).
Corrections or refreshed copies are appended as new, separately-provenanced
files.