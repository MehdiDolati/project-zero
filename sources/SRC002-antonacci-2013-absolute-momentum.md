---
id: SRC002
type: source

title: Absolute Momentum (Antonacci, 2013)

status: active
version: 1.0

owner: Project Zero

created: 2026-09-09
last-reviewed: 2026-09-09

created-by-type: agent
created-by: AI assistant (Buffy) in Freebuff
created-by-version: not available
production-tools: Freebuff (Buffy coding agent), web search (Serper Google API)
created-at: 2026-09-09T15:52:19+03:30

---

# Purpose

Register an external published source as a first-class artifact so that project
artifacts can cite it by stable identity
([G003](../governance/G003-artifact-model.md),
[RG009](../governance/rules/RG009-claim-provenance.md)).

---

# Citation

| Field | Value |
|-------|-------|
| Author | Gary Antonacci |
| Title | Absolute Momentum: A Simple Rule-Based Strategy and Universal Trend-Following Overlay |
| Venue | SSRN working paper |
| Year | 2013 (April) |
| Identifier | SSRN 2244633 |
| DOI | 10.2139/ssrn.2244633 |
| URL | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2244633 |

---

# What the Source Claims

The paper proposes "absolute momentum" — the author's term for time-series
momentum applied to a single asset: when the trailing 12-month return of the
asset is positive, hold the asset; otherwise hold cash (T-bills). It examines
this rule on broad equity indexes, including the S&P 500 against T-bills, and
reports risk-adjusted improvement over buy-and-hold with reduced drawdowns.

This is the published form closest to the exact rule specified in EXP001:
12-month lookback, broad US equity index, T-bill cash proxy, all-or-nothing
monthly switching.

---

# How the Project Uses It

- [EXP001](../experiments/EXP001/EXP001-momentum-replication.md) cites this as
  the source defining the replicated specification, and anchors its
  out-of-sample period to this paper's publication year (2013).

---

# Verification

Citation metadata (author, title, year, SSRN identifier, DOI) verified on
2026-09-09 against the SSRN listing and secondary bibliographic references via
web search. The content claims above are based on the abstract and widely
published summaries of the paper; the full text has not been read during
registration and is not archived in this repository. If the full text is later
read and used directly — in particular to confirm the exact S&P 500 / T-bill
configuration and publication month — record that here.

---

# Relationships

- cited-by: experiments/EXP001/EXP001-momentum-replication.md (EXP001)
- related-to: sources/SRC001-moskowitz-ooi-pedersen-2012-time-series-momentum.md (SRC001)
- related-to: sources/SRC003-hurst-ooi-pedersen-2017-century-of-evidence.md (SRC003)
- created-in: governance/GOVPROV-2026-09-09-claim-provenance.md
