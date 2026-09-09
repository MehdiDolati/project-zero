# Sources

Registered external sources: the published papers, websites, and datasets that
project artifacts rely on and cite.

Project Zero's traceability chain ([G005](../governance/G005-traceability.md))
connects project artifacts to each other. Sources extend that chain to knowledge
that originates outside the repository
([RG009](../governance/rules/RG009-claim-provenance.md)).

Sources are first-class artifacts ([G003](../governance/G003-artifact-model.md)):
stable `SRC` identity, lifecycle, relationships, and registry entry. A source
artifact records what the source claims and how this project uses it. It does
not mirror the source's content.

---

# Conventions

- ID family: `SRC` (SRC001, SRC002, ...). Identity is stable forever
  ([RG003](../governance/rules/RG003-artifact-identity.md)).
- File name: `SRCNNN-<authors>-<year>-<short-title>.md`.
- Template:
  [governance/templates/artifact-template.md](../governance/templates/artifact-template.md).
- Required metadata: full citation (authors, title, venue or site, year, and DOI
  or URL where available), what the source claims, and how the project uses it.
- Record the source kind: `paper`, `preprint`, `book`, `video`, `blog`,
  `website`, `dataset`, `forum`, or other (stated explicitly). Sources do not
  need to be academic; a video or blog post that an artifact relies on belongs
  here just as a paper does.
- For volatile sources (videos, posts, pages that may change or disappear),
  record the retrieval date and, where practical, an archival snapshot URL.
- Citation metadata SHOULD be verified against the publisher's page or an
  equivalent authoritative record at registration time, and the verification
  method recorded in the artifact.
- Register in the root [artifact registry](../README.md#artifact-registry) and
  in [governance/artifact-registry.json](../governance/artifact-registry.json).
- Artifacts cite sources with the `cites` relationship type registered in
  [G006](../governance/G006-relationships.md).
- A source that becomes unavailable SHOULD be marked `deprecated`, not deleted.
  Artifacts citing it keep their `cites` relationships
  ([G005](../governance/G005-traceability.md)).

---

# Registry

| ID | Title | Kind | Status | Location |
|----|-------|------|--------|----------|
| SRC001 | Time Series Momentum (Moskowitz, Ooi & Pedersen, 2012) | paper | active | [SRC001-moskowitz-ooi-pedersen-2012-time-series-momentum.md](SRC001-moskowitz-ooi-pedersen-2012-time-series-momentum.md) |
| SRC002 | Absolute Momentum (Antonacci, 2013) | paper | active | [SRC002-antonacci-2013-absolute-momentum.md](SRC002-antonacci-2013-absolute-momentum.md) |
| SRC003 | A Century of Evidence on Trend-Following Investing (Hurst, Ooi & Pedersen, 2017) | paper | active | [SRC003-hurst-ooi-pedersen-2017-century-of-evidence.md](SRC003-hurst-ooi-pedersen-2017-century-of-evidence.md) |
| SRC004 | Shiller US Stock Market Data (ie_data.xls), 1871–present | dataset | active | [SRC004-shiller-ie-data-monthly-stock.md](SRC004-shiller-ie-data-monthly-stock.md) |
| SRC005 | FRED TB3MS — 3-Month Treasury Bill Secondary Market Rate, Monthly, 1934–present | dataset | active | [SRC005-fred-tb3ms-monthly.md](SRC005-fred-tb3ms-monthly.md) |

Original project ideas are not sources and do not belong in this directory;
they live under `research/` and `hypotheses/` with no citation required
([RG009](../governance/rules/RG009-claim-provenance.md), "Original work").

---

# Status

Created 2026-09-09 with the first three registered sources, cited by
[EXP001](../experiments/EXP001/EXP001-momentum-replication.md).
