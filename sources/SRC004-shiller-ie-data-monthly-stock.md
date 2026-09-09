---
id: SRC004
type: source

title: Shiller US Stock Market Data (ie_data.xls)

status: active
version: 1.0

owner: Project Zero

created: 2026-09-09
last-reviewed: 2026-09-09

created-by-type: agent
created-by: AI assistant (Buffy) in Freebuff
created-by-version: not available
production-tools: Freebuff (Buffy coding agent), web search (Serper Google API), read_url
created-at: 2026-09-09T16:47:36+03:30

---

# Purpose

Register an external dataset as a first-class artifact so that project
artifacts can cite it by stable identity
([G003](../governance/G003-artifact-model.md),
[RG009](../governance/rules/RG009-claim-provenance.md)).

---

# Citation

| Field | Value |
|-------|-------|
| Kind | dataset (monthly spreadsheet workbook) |
| Creator | Robert J. Shiller, Yale University |
| Title | US Stock Markets and CAPE Ratio (monthly stock price, dividends, earnings, interest rates) |
| Coverage | 1871-01 to present, monthly |
| Site | https://shillerdata.com/ |
| File | `ie_data.xls` (linked from the site; historically also at http://www.econ.yale.edu/~shiller/data/ie_data.xls) |
| Revision cadence | Updated monthly; workbook is volatile |

Contents per the publisher's page: monthly stock price, dividends, and earnings
data plus interest rates and CPI starting January 1871. As of September 2018 it
includes a total-return price series (Bunn & Shiller 2014; Jivraj & Shiller
2017) that reinvests dividends into the price index.

---

# How the Project Uses It

- [EXP001](../experiments/EXP001/EXP001-momentum-replication.md) uses this as
  the equity index series: index level and dividends for the trailing
  12-month total return signal, and the total-return price series for the
  rule and benchmark return legs, for 1950-01 onward.

## Known limitations recorded at selection

- The S&P Composite price column is a **monthly average of daily closing
  prices**, not a month-end close. Signal and drawdown computations on this
  series deviate slightly from the "month-end close" ideal in EXP001's
  specification; the deviation and its direction (smoothing; average-based
  drawdowns understate month-end drawdowns) are recorded as an EXP001
  assumption.
- Pre-1957 the index is the S&P Composite (smaller constituent set; Cowles
  reconstruction before 1926), used here as the long-history proxy for a US
  broad equity index. Post-1957 it is the S&P 500.
- The nominal total-return price series is derived from the workbook's real
  total-return price and CPI columns; the derivation is recorded in
  `evidence/derived/` and is regenerable.

---

# Verification

Publisher page read on 2026-09-09 (shillerdata.com); coverage claim (1871-01
onward, monthly) and file name confirmed from the publisher's own description.

Retrieved 2026-09-09T13:33:09Z for
[EXP001](../experiments/EXP001/EXP001-momentum-replication.md): 1,674,752
bytes, SHA-256 `46a7fd194c53a5bd81b374e59f8a058ecf9ce15f94068a3b80d00efdf094f3e2`,
server `Last-Modified: 2026-09-02` (consistent with the monthly update
cadence). File format verified (OLE2 Excel compound document) together with
embedded publisher metadata (Author `RShiller`). Full retrieval record in the
experiment's `evidence/raw/provenance.md`. Cell contents are not yet
programmatically verified (no legacy-Excel reader available; none installed
per DEC001); content verification is assigned to EXP001 execution step 2, when
the workbook is first opened manually in Excel, before any derived series is
built. The workbook is volatile (monthly updates); the downloaded copy is the
evidence, not the live file.

---

# Relationships

- cited-by: experiments/EXP001/EXP001-momentum-replication.md (EXP001)
- related-to: sources/SRC005-fred-tb3ms-monthly.md (SRC005)
- related-to: sources/SRC003-hurst-ooi-pedersen-2017-century-of-evidence.md (SRC003)
