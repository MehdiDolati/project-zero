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

**File received 2026-09-30.** One combined CSV, `XAUUSD-TICK.csv`, was placed
here by the researcher: 864,476,202 bytes, SHA-256
`a3bf035c857dde9193b12973ab65e99bdaa5e11c757809ffad19d3d415f84fb1`. Its
identity and mechanical structure were verified, but its **coverage is a
partial slice — 2003-05-05 to 2005-12-30 only** — which does not reach the
frozen `2020-09-28`–`2026-09-28` holdout window. The file is therefore stored
as an immutable raw master but is **NOT** the pre-registered dataset. See
`provenance.md` for the full verification record and the deviations that must
be reconciled before it is treated as the EXP002 dataset.

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
| Observed coverage | **2003-05-05 to 2005-12-30 only** (partial; see `provenance.md`) |
| Storage | Local master retained, not committed (see Storage decision) |
| Location | `experiments/EXP002-gold-trend-following/evidence/raw/` |
| Status | **Received 2026-09-30** (partial coverage; not the pre-registered dataset) |

## Discrepancy to reconcile

`Q003`, `S005`, and `SRC006` currently record **two separate** Dukascopy
public-site exports (Bid and Ask), each `Tick`-selected, each carrying
`Open, High, Low, Close, Volume` per row and matched by timestamp. The file now
being supplied is **one combined CSV** carrying both `Bid` and `Ask` on the
same row, obtained through a **different channel** (a manual SQX download
rather than the public-site widget).

Both the format and the acquisition route therefore differ from the
pre-registered record. Per
[RG009](../../../../governance/rules/RG009-claim-provenance.md), substitutions
of route or specification are recorded explicitly, not silently accepted. This
difference must be reconciled in `Q003`/`S005`/`SRC006` — and reflected in the
Artifact Registry — before the file is treated as the pre-registered dataset.

## Verification status (2026-09-30)

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