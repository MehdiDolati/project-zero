---
id: SRC001
type: source

title: Time Series Momentum (Moskowitz, Ooi & Pedersen, 2012)

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
| Authors | Tobias J. Moskowitz, Yao Hua Ooi, Lasse Heje Pedersen |
| Title | Time Series Momentum |
| Venue | Journal of Financial Economics |
| Year | 2012 |
| Volume / Issue / Pages | 104 (2), 228–250 |
| DOI | 10.1016/j.jfineco.2011.11.003 |
| Access | Open access (CC BY-NC-ND) |
| URL (DOI) | https://doi.org/10.1016/j.jfineco.2011.11.003 |
| URL (publisher) | https://www.sciencedirect.com/science/article/pii/S0304405X11002613 |
| URL (author copy) | https://w4.stern.nyu.edu/facdir/lpederse/papers/TimeSeriesMomentum.pdf |

---

# What the Source Claims

The paper documents significant "time series momentum": the past 12-month own
return positively predicts an instrument's own future returns across 58 liquid
equity index, currency, commodity, and bond futures. The paper names the effect
and establishes it as a distinct, academically documented anomaly, separate
from cross-sectional momentum.

---

# How the Project Uses It

- [EXP001](../experiments/EXP001/EXP001-momentum-replication.md) cites this as
  the canonical academic naming of the time-series momentum effect that the
  experiment replicates.
- It supports the claim that the rule under test is published in the
  peer-reviewed literature.

The project does not rely on this source for the exact rule specification; the
published specification closest to EXP001's is registered as
[SRC002](SRC002-antonacci-2013-absolute-momentum.md).

---

# Verification

Citation metadata (authors, venue, year, volume, pages, DOI) verified on
2026-09-09 against the publisher page and the RePEc bibliographic record via
web search. The content claims above are based on the paper's abstract as
published; the full text has not been read during registration and is not
archived in this repository. If the full text is later read and used directly,
record that here.

---

# Relationships

- cited-by: experiments/EXP001/EXP001-momentum-replication.md (EXP001)
- related-to: sources/SRC002-antonacci-2013-absolute-momentum.md (SRC002)
- related-to: sources/SRC003-hurst-ooi-pedersen-2017-century-of-evidence.md (SRC003)
- created-in: governance/GOVPROV-2026-09-09-claim-provenance.md
