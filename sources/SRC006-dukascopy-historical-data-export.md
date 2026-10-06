---
id: SRC006
type: source
title: Dukascopy Bank Historical Data Export
status: active
version: 2.3

owner: Project Zero

created: 2026-09-28
last-reviewed: 2026-10-06

created-by-type: human + agent
created-by: |
  Primary: Mehdi (provider selection)
  Agent-assisted by: AI assistant (Copilot SDK in VS Code) (official-page verification)
created-by-version: not available
production-tools: VS Code, AI assistant (Copilot SDK), browser; versions not available
---

# Purpose

Register Dukascopy Bank's official Historical Data Export page and the
researcher-reported Tick-selected Bid/Ask OHLCV exports for Q003.

---

# Citation

| Field | Value |
|-------|-------|
| Kind | website / historical-data export tool |
| Publisher | Dukascopy Bank SA |
| Title | Forex Historical Data Export |
| URL | https://www.dukascopy.com/swiss/english/marketwatch/historical/ |
| Embedded tool | https://widgets.dukascopy.com/en/historical-data-export |
| Retrieved | 2026-09-28 |
| Page update shown | 2026-09-27 |

---

# Publisher Claims Verified

On the official page, Dukascopy describes the Historical Data Export tool as
providing historical prices for financial instruments including Forex,
commodities, and indices. Its FAQ states that data are downloadable in CSV and
timeframes range from tick-by-tick to monthly.

The embedded official selector displayed `XAU/USD — Gold vs US Dollar` on
2026-09-28.

In the export dialog observed that day, selectable offer sides were `Bid` and
`Ask`, and the visible period choices were `Tick`, `Second`, `Minute`, and
`Hour`. The dialog did not establish that the public widget directly exports
daily bars or both quote sides in one file.

The page FAQ points users to JForex's Historical Data Manager for more custom
timeframes. The project has not independently verified the JForex route; the
researcher's shared examples for Q003 are from separate public-page exports.

The researcher provided small Bid and Ask excerpts downloaded separately
from the public page after selecting `Tick` and one quote side at a time. The
observed columns are `Europe/Amsterdam`, `Open`, `High`, `Low`, `Close`, and
`Volume`. A Bid excerpt shared in text showed a timestamp such as
`2026-09-28T12:00:00+02:00`; an Ask screenshot showed distinct OHLC prices
within a row. The researcher reports the Bid and Ask timestamp sequences
match and that the displayed coverage is `5/5/2003` through `28/9/2026`.

The researcher confirms that each `Tick`-selected row represents one tick
and its timestamp marks when that tick was recorded. The researcher corrected
the previously shared Ask excerpt: in the corrected sample, Open, High, Low,
and Close are equal in each row, consistent with one price per tick. Multiple
ticks share the same second-level timestamp. This user-provided example is
consistent with, but does not independently verify, the row and timestamp
semantics. The full files have not been provided or parsed in Project Zero;
the meaning of `Volume` and complete Bid/Ask alignment remain unverified.

The researcher confirmed the inclusive six-year evaluation window
`2020-09-28` through `2026-09-28` and approved fixed UTC+02 daily intervals
`[00:00, 00:00 next day)`. For each side, aggregate first row Open, maximum
High, minimum Low, and last row Close; the corrected sample has equal OHLC
values per tick. Interpret timestamps using the export's `Europe/Amsterdam`
context and explicit offsets where present, then convert instants to fixed
UTC+02 for bucketing. Preserve source row order for ticks sharing a timestamp.
Omit empty days and do not forward-fill. This is a project-defined method, not
a verified Dukascopy daily-bar convention; full-file timestamp conventions
and Bid/Ask alignment remain unverified.

---

# How the Project Uses It

- Q003 identifies the Dukascopy public historical export as the intended
  source for separate Bid and Ask OHLCV records selected with `Tick`; the
  researcher reports one tick per row and the corrected sample has equal
  OHLC values per tick. Full-file validation is still required before daily
  bars are generated.
- On 2026-10-02 the researcher delivered the full-range dataset for EXP002 as
  `XAUUSD-TICK-full.csv` in `experiments/EXP002-gold-trend-following/evidence/raw/`.
  Its observed structure is a **single combined CSV** with header
  `DateTime,Bid,Ask,Volume` — both quote sides on one row, a single `Volume`
  column, and **no OHLC columns** — with naive timestamps and no time-zone
  field. It was obtained by a **manual SQX download**, not the public-site
  widget described above. A full streaming pass over 732,112,910 rows found no
  malformed rows, bad timestamps, bad numerics, crossed quotes, or ordering
  violations; observed coverage `2003-05-05`–`2026-10-02` spans the frozen
  `2020-09-28`–`2026-09-28` window. See
  `experiments/EXP002-gold-trend-following/evidence/raw/provenance.md`. The
  format and route this source now delivers therefore differ from the
  Bid/Ask OHLCV public-site exports registered here; per RG009 these
  deviations were recorded explicitly. On 2026-10-06 decision DEC002 accepted
  the amended EXP002 registration, reconciling Q003 with this delivered
  format/route: EXP002 consumes the single combined `DateTime,Bid,Ask,Volume`
  tick CSV from the manual SQX download, not the public-site Bid/Ask OHLCV
  exports described in the earlier sections above. The public-site export
  description is retained here as the source's originally registered form.

---

# Known Limitations

- The official page and selector establish that XAU/USD is listed and that
  the public tool offers historical exports. The researcher supplied small
  excerpts from separate Bid and Ask downloads; the full files are not in
  Project Zero.
- The page FAQ says timeframes range from tick-by-tick to monthly, but the
  observed export dialog listed only Tick, Second, Minute, and Hour. Q003
  will construct daily bars from the Tick-selected export using its specified
  aggregation rule; no direct daily export is assumed.
- The public widget offers Bid and Ask as separate selections. The researcher
  reports matching timestamps across the two downloads; this has not been
  verified from the full files.
- The sample identifies `Europe/Amsterdam` and includes an ISO timestamp
  ending `+02:00`. The researcher reports each row is one tick and the
  timestamp is the tick's record time; the corrected sample has equal OHLC
  values per row and repeated second-level timestamps. These observations
  have not been verified against the full files. Historical offset behavior,
  volume meaning, row ordering, coverage, missing records, and account-feed
  match remain unverified.
- Do not treat this source as validated experiment data until the full exports
  and their structure are checked.

---

# Verification

The official Dukascopy Bank page and its embedded historical-data selector
were opened on 2026-09-28. The live selector displayed XAU/USD; the public
export dialog showed separate Bid/Ask selections and Tick/Second/Minute/Hour
periods. An earlier user report about JForex daily Bid/Ask availability was
not independently verified and is not the source route currently specified
for Q003. On 2026-09-29, the researcher shared small OHLCV excerpts from
separate Tick-selected Bid and Ask downloads, reported matching timestamps
and displayed coverage `5/5/2003`–`28/9/2026`, and showed a `Europe/Amsterdam`
time label with a sample timestamp ending `+02:00`. The researcher confirms
one tick per row and timestamp-at-tick-time semantics, then corrected the
Ask sample to show equal OHLC values per row and repeated second-level
timestamps. The researcher confirmed Q003's inclusive evaluation window
`2020-09-28`–`2026-09-28` and approved fixed-UTC+02 daily boundaries and
aggregation. The full files, timestamp conventions, and Bid/Ask alignment
have not been independently verified in Project Zero.

---

# Relationships

- cited-by: questions/Q003-long-only-gold-trend-following.md (Q003)
- related-to: sources/README.md

---

# Revision History

| Version | Date | Summary |
| ------- | ---- | ------- |
| 1.0 | 2026-09-28 | Registered the official page and verified the XAU/USD listing. |
| 1.1 | 2026-09-28 | Recorded live widget offer-side and period controls; daily export and simultaneous bid/ask availability remain unverified. |
| 1.2 | 2026-09-28 | Recorded the publisher FAQ's JForex Historical Data Manager reference; daily XAU/USD support there remains unverified. |
| 1.3 | 2026-09-28 | Recorded the researcher's initial, unverified report of JForex daily XAU/USD and combined Bid/Ask; later samples are from the public export page. |
| 1.4 | 2026-09-29 | Recorded the researcher's report of viewing Bid/Ask file data beginning `5/5/2003`; file details and latest date remain unverified in Project Zero. |
| 1.5 | 2026-09-29 | Recorded the researcher-reported latest file date `28/9/2026` and a proposed latest six-year window pending confirmation. |
| 1.6 | 2026-09-29 | Recorded the researcher's confirmation of the inclusive evaluation window `2020-09-28`–`2026-09-28`; file conventions remain unverified. |
| 1.7 | 2026-09-29 | Recorded the researcher's preliminary daily-bar timezone/boundary report; superseded by the tick-file clarification in 1.8. |
| 1.8 | 2026-09-29 | Recorded an intermediate tick-data characterization; superseded by the OHLCV export samples and row-unit uncertainty in 1.9. |
| 1.9 | 2026-09-29 | Recorded separate Tick-selected Bid/Ask OHLCV excerpts, matching-timestamp report, Europe/Amsterdam header, unresolved row unit, and fixed-UTC+02 daily resampling. |
| 2.0 | 2026-09-29 | Recorded the researcher's one-tick-per-row and timestamp-time report, flagged its conflict with the Ask OHLC sample, and put daily aggregation on hold pending quote-field semantics. |
| 2.1 | 2026-09-29 | Recorded the corrected Ask sample with equal OHLC values per tick and repeated second-level timestamps; reinstated the approved daily aggregation pending full-file validation. |
| 2.2 | 2026-10-02 | Recorded the delivered full-range EXP002 dataset `XAUUSD-TICK-full.csv`: a single combined `DateTime,Bid,Ask,Volume` CSV (no OHLC, naive timestamps) obtained via manual SQX download, coverage `2003-05-05`–`2026-10-02` verified by a full streaming pass. Format and route differ from the pre-registered public-site Bid/Ask tick OHLCV exports; deviations recorded per RG009 pending Q003 reconciliation. |
| 2.3 | 2026-10-06 | Reconciled per DEC002: Q003 amended to align with the delivered combined `DateTime,Bid,Ask,Volume` tick CSV route; deviations closed and the public-site Bid/Ask OHLCV description retained as the originally registered form. |
