# EXP001 Execution Log

This log is written **during** execution, not reconstructed afterwards. It exists
to make the process itself observable, because the process is one of the two
objects under study in EXP001.

Append-only. Entries are not edited once written. Corrections are made by
adding a new entry that supersedes the old one, with a note
([G001](../../../governance/G001-research-governance.md)).

---

| Field | Value |
|-------|-------|
| `created-by-type` | `agent` (log scaffold and step-1 entries) |
| `created-by` | AI assistant (Buffy) in Freebuff, on direction of the project owner |
| `created-by-version` | not available |
| `production-tools` | Freebuff (Buffy coding agent), web search (Serper Google API), read_url |
| `created-at` | 2026-09-09T16:47:36+03:30 |

---

## Step 1 record — 2026-09-09 — Data sources identified and verified (pre-download)

Per procedure step 1 and the v1.2 pre-execution review watch item, candidate
free sources for both series were identified and their coverage verified
against publisher records **before** any file was downloaded. Nothing has been
retrieved yet; `raw/` is empty.

**Equity series — [SRC004](../../../sources/SRC004-shiller-ie-data-monthly-stock.md)**
(Shiller `ie_data.xls`, https://shillerdata.com/):

- Publisher page read directly; workbook confirmed to contain monthly US stock
  price, dividends, earnings, interest rates, and CPI from 1871-01, including
  a total-return price series (per Bunn & Shiller 2014; Jivraj & Shiller 2017).
- Coverage requirement (from 1950-01): satisfied with 79 years of headroom.

**Cash series — [SRC005](../../../sources/SRC005-fred-tb3ms-monthly.md)**
(FRED TB3MS, https://fred.stlouisfed.org/series/TB3MS):

- FRED's data page read directly; title, source (Federal Reserve Board),
  release (H.15), frequency (monthly), units (percent), and date range
  (1934-01-01 to 2026-08-01) confirmed from the publisher record.
- Coverage requirement (from 1950-01): satisfied with 16 years of headroom.

**Conclusion:** the coverage gate from the pre-execution review passes for
both series. The data-source substitution risk flagged at review is closed
for the IS window as specified.

**Verification method:** publisher pages read via HTTP; no third-party
mirrors relied on. Workbook and CSV contents themselves are unverified until
retrieval; verification-at-retrieval is mandatory per SRC004 and SRC005
registration notes.

**Division of labor:** this step was performed agent-assisted (source search
and verification). The manual execution phases that feed the process metrics —
spreadsheet construction, computation, analysis, write-up — remain the
researcher's, per DEC001 and the experiment's design.

---

## Discretionary choices

Every point where judgement was required and the design artifact did not
determine the answer. Record the choice, the alternatives considered, and the
reason. Include choices that were tempting and rejected.

| # | Date | Choice made | Alternatives | Reason |
|---|------|-------------|--------------|--------|
| 1 | 2026-09-09 | Use Shiller monthly-average-of-daily-closes price column as-is | Splice in a month-end-close series from another source; switch to an ETF-based series | A spliced series introduces a structural break at the splice date and complicates reproducibility more than the smoothing does; ETF inception is far too late for the IS window. Deviation recorded as an EXP001 assumption (v1.3). |
| 2 | 2026-09-09 | Derive monthly cash return from TB3MS with a stated simple conversion (discount-basis rate ÷ 12) | Use a different risk-free series; compound the discount rate to a bond-equivalent yield first | TB3MS is the official long free series; the discount-to-yield gap is small and directionally known. Conversion will be recorded in `evidence/derived/`. |
| 3 | 2026-09-09 | Retrieve TB3MS from federalreserve.gov (H.15 Data Download Program) after FRED connection failures | Keep retrying FRED; use a third-party mirror (DBnomics); defer retrieval | federalreserve.gov is the **primary** source of the series FRED redistributes; mirrors add a layer without adding authority. Substitution and anchor-match check (1934-01 = 0.72 identical on both routes) recorded in `raw/provenance.md`. |

---

## Shortcuts prevented by methodology

Points where the documented method stopped something that would otherwise have
been done. These are the evidence for the project creating value.

| # | Date | Shortcut that was tempting | What prevented it |
|---|------|----------------------------|-------------------|
| 1 | 2026-09-09 | Download the first apparently-suitable dataset from a search and discover coverage problems mid-build | The v1.2 pre-execution review's coverage gate: sources must be verified against the full IS window before the first download |

---

## Governance overhead with no research value

Points where following governance produced work that caught nothing and improved
nothing. Recording these honestly is required. They are evidence for
[H000](../../../hypotheses/H000-project-should-not-exist.md).

| # | Date | What was required | Why it added no value |
|---|------|-------------------|-----------------------|

None recorded at execution step 1: the SRC registrations for the datasets
doubled as the provenance scaffolding procedure step 1 requires anyway, and
produced the data-shape assumptions above, which are research-relevant.

---

## Retrieval record — 2026-09-09 — Step 1 completed: files retrieved, hashed, verified

Both files were retrieved once, stored byte-for-byte in `raw/`, and hashed
(SHA-256). Full details, URLs, HTTP headers, and the route substitution for
TB3MS are in [raw/provenance.md](raw/provenance.md). Summary:

| File | Size | SHA-256 (first 12) | Content verification |
|------|------|--------------------|----------------------|
| `ie_data.xls` (SRC004) | 1,674,752 B | `46a7fd194c53` | Format + publisher metadata verified; **cell contents pending** (no legacy-Excel reader available; no package installed per DEC001). Verification assigned to step 2, when the workbook is first opened manually in Excel. |
| `TB3MS.csv` (SRC005, via federalreserve.gov) | 115,160 B | `edd3c63effb2` | **PASSED**: 920 months 1950-01→2026-08, 0 missing, 0 calendar gaps; 1934-01 anchor matches FRED's published table; spot values plausible. |

Notes:

- The coverage gate (watch item 1 from the pre-execution review) is now
  **closed with retrieved data for the cash leg**; the equity leg closes at
  step 2 when the workbook is opened.
- FRED was unreachable from the execution network (repeated connection
  resets); retrieval used the series' primary source instead. Recorded as
  discretionary choice #3 and in provenance.
- Agent-assisted time (search, retrieval, verification) is not counted in the
  manual-effort table below, which measures the researcher's manual execution
  per the experiment's process-metric design. Agent-assisted steps are
  timestamped in provenance instead.

---

| Phase | Minutes |
|-------|---------|
| Data retrieval and provenance | |
| Computation | |
| Analysis | |
| Write-up and registration | |
| **Total** | |

---

## Status

Updated 2026-09-09 after retrieval. Step 1 complete: sources verified
pre-download (above), both files retrieved once, hashed, and provenance
recorded in `raw/provenance.md`. TB3MS content fully verified (coverage,
continuity, anchor match). `ie_data.xls` contents verify at step 2 on first
manual open in Excel, before any derived series is built. `derived/` remains
empty. Next: build the monthly table (procedure step 2), record the workbook
content verification in this log, and start the effort clock for the manual
phases.
