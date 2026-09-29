---
id: SRC006
type: source
title: Dukascopy Bank Historical Data Export
status: active
version: 1.6

owner: Project Zero

created: 2026-09-28
last-reviewed: 2026-09-28

created-by-type: human + agent
created-by: |
  Primary: Mehdi (provider selection)
  Agent-assisted by: AI assistant (Copilot SDK in VS Code) (official-page verification)
created-by-version: not available
production-tools: VS Code, AI assistant (Copilot SDK), browser; versions not available
---

# Purpose

Register Dukascopy Bank's official Historical Data Export page as the intended
candidate source for daily XAU/USD bid/ask data for Q003.

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
timeframes, but does not enumerate whether daily XAU/USD Bid and Ask bars are
available there.

On 2026-09-28, the researcher reported checking JForex Historical Data
Manager and finding daily XAU/USD history available from 2003, with Bid and
Ask available together in one output. On 2026-09-29, the researcher reported
viewing the file and seeing both Bid and Ask data beginning at the displayed
date `5/5/2003`. The file has not been provided to or independently inspected
in Project Zero; retain the date exactly as displayed until its format and
other file conventions are confirmed.
The researcher also reported that the latest date displayed in the file is
`28/9/2026` (2026-09-28).
On 2026-09-29, the researcher confirmed the inclusive six-year evaluation
window `2020-09-28` through `2026-09-28`, based on that reported latest date.

---

# How the Project Uses It

- Q003 identifies Dukascopy Bank as the intended provider for daily XAU/USD
  bid/ask history. The researcher reports viewing both Bid and Ask data from
  `5/5/2003` and latest date `28/9/2026`; the file itself and its feed
  conventions have not been independently verified in Project Zero.

---

# Known Limitations

- The official page and selector establish that an XAU/USD instrument is
  listed and that the public tool offers historical data exports. The
  researcher reports viewing a JForex file with daily Bid and Ask data
  beginning at `5/5/2003` and latest date `28/9/2026`; Project Zero has not
  inspected the file.
- The page FAQ says timeframes range from tick-by-tick to monthly, but the
  observed export dialog listed only Tick, Second, Minute, and Hour. The
  researcher reports daily bars through JForex; the exported file is still
  needed to verify that route's data and conventions.
- The public widget offers Bid and Ask as separate UI selections. The
  researcher reports that the JForex file contains both; its columns and
  format have not been independently inspected.
- Daily bar construction, timezone, treatment of missing periods, and whether
  the downloadable series matches the researcher's intended trading account
  remain unverified.
- The researcher reports viewing an exported file, but it has not been
  supplied to or independently inspected in Project Zero. The reported latest
  covered date is `28/9/2026`; exact JForex bar construction, timezone, and
  account-feed match remain unverified. Do not treat this source as validated
  experiment data.

---

# Verification

The official Dukascopy Bank page and its embedded historical-data selector
were opened on 2026-09-28. The live selector displayed XAU/USD; the public
export dialog showed separate Bid/Ask selections and Tick/Second/Minute/Hour
periods. On the same date, the researcher reported that JForex Historical
Data Manager offers daily XAU/USD history from 2003 and a combined Bid/Ask
output. On 2026-09-29, the researcher reported viewing the file and seeing Bid
and Ask data beginning at `5/5/2003`, with latest date `28/9/2026`. The file
was not supplied to Project Zero, so its contents and conventions have not
been independently verified. The researcher confirmed the inclusive six-year window
`2020-09-28`–`2026-09-28` for Q003. The JForex file itself and its bar
conventions have not been independently verified in Project Zero.

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
| 1.3 | 2026-09-28 | Recorded the researcher's JForex report of daily XAU/USD from 2003 and combined Bid/Ask output; sample-file details remain unverified. |
| 1.4 | 2026-09-29 | Recorded the researcher's report of viewing Bid/Ask file data beginning `5/5/2003`; file details and latest date remain unverified in Project Zero. |
| 1.5 | 2026-09-29 | Recorded the researcher-reported latest file date `28/9/2026` and a proposed latest six-year window pending confirmation. |
| 1.6 | 2026-09-29 | Recorded the researcher's confirmation of the inclusive evaluation window `2020-09-28`–`2026-09-28`; file conventions remain unverified. |
