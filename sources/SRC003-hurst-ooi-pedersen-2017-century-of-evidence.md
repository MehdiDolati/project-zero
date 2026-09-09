---
id: SRC003
type: source

title: A Century of Evidence on Trend-Following Investing (Hurst, Ooi & Pedersen, 2017)

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
| Authors | Brian Hurst, Yao Hua Ooi, Lasse Heje Pedersen |
| Title | A Century of Evidence on Trend-Following Investing |
| Venue | The Journal of Portfolio Management |
| Year | 2017 (Fall) |
| Volume / Issue / Pages | 44 (1), 15–29 |
| Identifier | SSRN 2993026 |
| URL (publisher) | https://www.pm-research.com/content/iijpormgmt/44/1/15 |
| URL (SSRN) | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2993026 |

---

# What the Source Claims

The paper evaluates trend-following (time-series momentum) performance over
roughly a century of data across multiple asset classes and reports that the
strategy delivered positive performance in every decade examined, with
substantial drawdown reduction relative to equities. It documents the effect
over a period that long predates its formal academic naming (SRC001, 2012).

---

# How the Project Uses It

- [EXP001](../experiments/EXP001/EXP001-momentum-replication.md) cites this as
  the support for its claim that the effect is "documented in academic and
  practitioner literature for decades", and for the framing that its in-sample
  window covers an era in which the effect was already documented.
- It is also the reason the IS/OOS split is anchored to the specification
  source (SRC002, 2013) rather than to the earliest documentation: the effect's
  documentation predates the exact specification being replicated.

---

# Verification

Citation metadata (authors, venue, year, volume, issue, pages, SSRN identifier)
verified on 2026-09-09 against the publisher listing and the SSRN record via
web search. The content claims above are based on the abstract and widely
published summaries; the full text has not been read during registration and is
not archived in this repository. If the full text is later read and used
directly, record that here.

---

# Relationships

- cited-by: experiments/EXP001/EXP001-momentum-replication.md (EXP001)
- related-to: sources/SRC001-moskowitz-ooi-pedersen-2012-time-series-momentum.md (SRC001)
- related-to: sources/SRC002-antonacci-2013-absolute-momentum.md (SRC002)
- created-in: governance/GOVPROV-2026-09-09-claim-provenance.md
