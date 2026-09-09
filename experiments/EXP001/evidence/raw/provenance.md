# EXP001 Raw Data Provenance

Files in `raw/` are stored exactly as retrieved and are immutable
([G001](../../../../governance/G001-research-governance.md)). This file records
what was retrieved, when, from where, by what means, and how each file was
verified. Nothing here is edited after writing; corrections are appended as
new dated entries.

Provenance of this record ([RG008](../../../../governance/rules/RG008-authorship-provenance.md)):

| Field | Value |
|-------|-------|
| `created-by-type` | `agent` |
| `created-by` | AI assistant (Buffy) in Freebuff |
| `created-by-version` | not available |
| `production-tools` | Freebuff (Buffy coding agent), curl (schannel/Windows), sha256sum, Python 3 stdlib (csv) |
| `created-at` | 2026-09-09T13:45:00Z |

---

## File 1 — `ie_data.xls` (equity series; [SRC004](../../../../sources/SRC004-shiller-ie-data-monthly-stock.md))

| Field | Value |
|-------|-------|
| Retrieved at | 2026-09-09T13:33:09Z |
| Source page | https://shillerdata.com/ |
| Download URL | https://img1.wsimg.com/blobby/go/e5e77e0b-59d1-44d9-ab25-4763ac982e53/downloads/70fec4f5-727f-4e53-b5f1-179af109c5fa/ie_data.xls?ver=1788371540009 (the workbook link as served from shillerdata.com at retrieval time; URL recorded verbatim) |
| Size | 1,674,752 bytes |
| SHA-256 | `46a7fd194c53a5bd81b374e59f8a058ecf9ce15f94068a3b80d00efdf094f3e2` |
| HTTP result | 200 OK; server `Last-Modified: Wed, 02 Sep 2026 17:51:53 GMT` (full headers preserved in `ie_data.headers.txt`) |
| File format | Legacy Excel (OLE2 compound document, magic `d0cf11e0a1b11ae1`); embedded metadata: Author `RShiller`, Last Saved `2026-09-02` — consistent with the publisher's monthly update cadence |
| Retrieval notes | One earlier attempt failed with a connection reset; second attempt succeeded. File stored byte-for-byte as downloaded. |

Verification status: file identity, format, and publisher metadata verified.
**Workbook cell contents NOT yet verified** — no legacy-Excel reader was
available in the execution environment, and per DEC001 no package installation
was performed for the research pipeline. Content verification (columns, first
month, last month, coverage of 1950-01 onward) is assigned to execution step 2,
when the workbook is first opened manually in Excel. Verification MUST be
recorded in `evidence/execution-log.md` before any derived series is built.

---

## File 2 — `TB3MS.csv` (cash series; [SRC005](../../../../sources/SRC005-fred-tb3ms-monthly.md))

| Field | Value |
|-------|-------|
| Retrieved at | 2026-09-09T13:40:22Z (response `Date` header) |
| Publisher | Board of Governors of the Federal Reserve System (US), H.15 release |
| Download URL | https://www.federalreserve.gov/datadownload/Output.aspx?rel=H15&series=d7e27b7b09a3a7feae95b9c61781fcd8&lastobs=&from=&to=&filetype=csv&label=include&layout=seriescolumn&type=package |
| Size | 115,160 bytes |
| SHA-256 | `edd3c63effb2100e5b2a7e47ae10aa8e04289d3910b1823f32125be1b8e93308` |
| HTTP result | 200 OK; `Content-Type: text/csv` (full headers preserved in `TB3MS.headers.txt`) |
| File format | CSV text; full monthly H.15 package (30 series), 1,112 data rows, 1934-01 through 2026-08 |

**Route substitution, recorded per RG009:** [SRC005](../../../../sources/SRC005-fred-tb3ms-monthly.md)
names FRED as the access route, but fred.stlouisfed.org was unreachable from
the execution network (repeated connection resets over ~10 minutes). The file
was retrieved instead from federalreserve.gov — the **primary source** of the
same series (FRED redistributes the H.15 release). The H.15 package's
`RIFSGFSM03_N.M` column (3-month Treasury bill secondary market rate, discount
basis) is the series SRC005 describes. SRC005 remains the registered source
artifact; this record documents the actual retrieval route. No re-download
from FRED is required, but one MAY be appended later for redundancy.

### Content verification (performed on the retrieved file)

- Series column located: `RIFSGFSM03_N.M` at column index 11 ("3-month Treasury
  bill secondary market rate discount basis").
- Rows: 1,112 data rows spanning 1934-01 to 2026-08, monthly.
- Window required by EXP001 (1950-01 onward): 920 months, 920 filled values,
  **0 missing**, **0 calendar gaps** (month continuity verified programmatically).
- Spot values: 1950-01 = 1.07; 2007-12 = 3.00; 2020-03 = 0.29; 2026-08 = 3.72
  (percent, discount basis).
- Anchor match: 1934-01 = 0.72, identical to the value published on FRED's
  TB3MS table page read on 2026-09-09 — confirms the two routes serve the
  same series.

**Result: coverage and continuity PASSED for the full IS and OOS windows.**

---

## Immutability

From this point, the two data files MUST NOT be modified, renamed, or
re-downloaded in place ([G001](../../../../governance/G001-research-governance.md)).
If a refreshed copy is ever needed (e.g., the OOS window extends), it is stored
as a new file with its own provenance entry; `derived/` regeneration
instructions must then reference the exact file this record describes.
