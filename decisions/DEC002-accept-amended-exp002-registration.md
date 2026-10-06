---
id: DEC002
type: decision

title: Accept Amended EXP002 Dataset Registration

status: accepted
version: 1.0

owner: Project Zero

created: 2026-10-06
last-reviewed: 2026-10-06
---

# Decision

Accept an amended registration for EXP002's dataset: the delivered single
combined `DateTime,Bid,Ask,Volume` CSV master (`XAUUSD-TICK-full.csv`),
obtained via a manual SQX download, is accepted as the EXP002 dataset in place
of the originally pre-registered two separate Dukascopy public-site
`Tick`-selected Bid/Ask OHLCV exports.

---

# Context

Q003, S005, and SRC006 pre-registered EXP002's data as **two separate**
Dukascopy public-site exports (Bid and Ask), each `Tick`-selected, each
carrying `Open, High, Low, Close, Volume` per row, matched by timestamp, with a
reported `Europe/Amsterdam` time-zone label and displayed coverage
`5/5/2003`–`28/9/2026`.

The dataset actually delivered is a **single combined** CSV with header
`DateTime,Bid,Ask,Volume` — one `Volume` column, **no OHLC columns**, and a
naive timestamp with no time-zone field — obtained through a **manual SQX
download** rather than the public-site widget.

Per RG009, substitutions of route or specification are recorded explicitly and
are not silently accepted. The deviation was therefore held open as a blocker
in `operating-system/CURRENT.md` until the researcher decided how to reconcile
it.

---

# Problem

Two dimensions of the delivered dataset differ from the pre-registration:

- **Format** — one combined Bid/Ask CSV with a single `Volume` and no OHLC,
  versus two separate per-side OHLCV tick exports.
- **Route** — a manual SQX download, versus the Dukascopy public-site widget.

The coverage deviation that previously blocked use (a partial slice through
2005-12-30) has already been resolved: the delivered full master spans
`2003-05-05`–`2026-10-02`, covering the pre-registered range and the frozen
`2020-09-28`–`2026-09-28` holdout. Its structure passed a full independent
streaming verification — 732,112,910 rows, 0 malformed rows, 0 bad timestamps,
0 bad numerics, 0 crossed quotes, 0 ordering violations.

The open question was whether to amend the registration to the delivered
format/route, or to obtain conforming exports.

---

# Decision Drivers

- Data before method: the delivered master is verified, coverage-complete, and
  spans the frozen holdout, so the analysis can proceed without delay.
- Provenance before convenience: the modification is recorded explicitly, with
  the original pre-registration preserved for traceability.
- Fixed holdout discipline: the strategy rules were frozen before any returns
  were examined; changing the data source must not change the frozen rules.
- Traceability: the delivered file's identity (byte size, SHA-256) anchors the
  substitution.

---

# Decision

1. **Accept an amended registration.** The delivered single combined
   `DateTime,Bid,Ask,Volume` CSV master
   (`XAUUSD-TICK-full.csv`, 32,121,180,517 bytes, SHA-256
   `4921484ac6a70654c187e0b097c66dedca26c21f2eb398bce5e4bcfbcead17d4`,
   732,112,910 rows, coverage `2003-05-05`–`2026-10-02`) is accepted as the
   EXP002 dataset via a manual SQX acquisition route.

2. **Preserve the original pre-registration.** The two-file public-site Tick
   OHLCV description remains recorded in Q003/S005/SRC006 history and in the
   EXP002 raw `provenance.md`; it is superseded, not erased.

3. **Derive daily bars from the offered fields.** With no source OHLC, the
   frozen fixed-UTC+02 daily aggregation is applied per side directly to the
   tick fields: first `Bid`/`Ask` as the day's open, maximum as high, minimum as
   low, last as close, preserving file order for records with duplicate
   timestamps, omitting empty days, and not forward-filling.

4. **Keep the backtest rules unchanged.** The frozen SMA200 long-only baseline,
   its next-bar Ask-entry/Bid-exit execution, position sizing, one-year time
   stop, cost treatment, and the buy-and-hold benchmark remain exactly as
   frozen. The amended dataset does not relax the rule freeze.

5. **Carry residual unknowns as explicit caveats.** The naive `DateTime` time
   zone, the meaning of the single `Volume`, and the internal gap/empty-day
   structure remain unverified against the pre-registration and MUST be
   disclosed in any derived evidence.

---

# Consequences

Positive:

- unblocks daily-bar construction and the frozen baseline backtest;
- preserves the pre-registration and the exact delivered-file identity for
  audit;
- keeps the holdout label intact by not altering the frozen rules.

Negative:

- EXP002's dataset is no longer byte-identical to its stated
  pre-registration, so results carry an amended-registration caveat;
- the naive timestamp means the fixed-UTC+02 daily boundaries rest on an
  unverified time-zone assumption;
- the single `Volume` column replaces per-side volume, limiting volume-based
  diagnostics.

These costs are accepted because the delivered master is the only
coverage-complete, verified corpus available and the deviations are recorded
rather than concealed.

---

# Review Criteria

This decision should be revisited if:

- a conforming two-file public-site Tick OHLCV export is later obtained and the
  researcher chooses to re-run against the original registration;
- the naive `DateTime` time zone is resolved in a way that contradicts the
  fixed-UTC+02 daily boundaries;
- the single `Volume` column proves unsuitable for any required diagnostic.

---

# Relationships

- decides: questions/Q003-long-only-gold-trend-following.md (Q003)
- related-to: sources/SRC006-dukascopy-historical-data-export.md (SRC006)
- related-to: research/sessions/S005-gold-question-formulation-test.md (S005)
- enforced-by: governance/rules/RG009-claim-provenance.md (RG009)
- governed-by: governance/G001-research-governance.md (G001)
- related-to: experiments/EXP002-gold-trend-following/evidence/raw/provenance.md
- derives-from: research/003-research-methodology.md (research-003)