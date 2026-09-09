---
id: SRC005
type: source

title: FRED TB3MS — 3-Month Treasury Bill Secondary Market Rate, Monthly

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
| Kind | dataset (official statistics time series) |
| Series ID | TB3MS |
| Title | 3-Month Treasury Bill Secondary Market Rate, Discount Basis |
| Source | Board of Governors of the Federal Reserve System (US) |
| Release | H.15 Selected Interest Rates |
| Frequency / Units | Monthly / Percent, not seasonally adjusted |
| Coverage | 1934-01-01 to present (verified 1934-01 to 2026-08 on 2026-09-09) |
| URL (series) | https://fred.stlouisfed.org/series/TB3MS |
| URL (table) | https://fred.stlouisfed.org/data/TB3MS |
| URL (CSV) | https://fred.stlouisfed.org/graph/fredgraph.csv?id=TB3MS |
| Notes | Averages of business days, discount basis |

---

# How the Project Uses It

- [EXP001](../experiments/EXP001/EXP001-momentum-replication.md) uses this as
  the cash leg: the risk-free rate for cash months and the risk-free input to
  Sharpe ratios, for 1950-01 onward (16 years of headroom below the IS start).

## Known limitations recorded at selection

- The series is a **discount-basis** annual rate of business-day averages. The
  monthly cash return derived from it (division by 12, simple annualization)
  and the discount-basis convention both introduce small, directionally
  conservative biases relative to a true compounded T-bill holding return;
  the conversion formula is recorded in `evidence/derived/` and flagged as a
  discretionary choice in `evidence/execution-log.md`.

---

# Verification

FRED's own data page read on 2026-09-09; title, source, release, frequency,
units, and date range (1934-01-01 to 2026-08-01, last updated 2026-09-01)
confirmed directly from the publisher record.

Retrieved 2026-09-09 for
[EXP001](../experiments/EXP001/EXP001-momentum-replication.md) from the
series' **primary source** (federalreserve.gov, H.15 Data Download Program)
after FRED endpoints proved unreachable from the execution network; the H.15
column `RIFSGFSM03_N.M` is this series. Retrieved file verified: 1,112 monthly
rows spanning 1934-01 to 2026-08; the window required by EXP001 (1950-01
onward) is complete — 920 months, 0 missing values, 0 calendar gaps; anchor
value 1934-01 = 0.72 is identical to FRED's published table, confirming route
equivalence. SHA-256
`edd3c63effb2100e5b2a7e47ae10aa8e04289d3910b1823f32125be1b8e93308`; full
retrieval record in the experiment's `evidence/raw/provenance.md`. The
downloaded copy is the evidence regardless of route.

---

# Relationships

- cited-by: experiments/EXP001/EXP001-momentum-replication.md (EXP001)
- related-to: sources/SRC004-shiller-ie-data-monthly-stock.md (SRC004)
