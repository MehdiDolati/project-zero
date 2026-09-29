---
id: S005
type: session
title: Gold Question Formulation Test
status: completed
version: 2.1

owner: Project Zero

created: 2026-09-28
last-reviewed: 2026-09-29

created-by-type: human + agent
created-by: |
  Primary: Mehdi
  Agent-assisted by: AI assistant (Copilot SDK in VS Code)
created-by-version: not available
production-tools: VS Code, AI assistant (Copilot SDK); versions not available
created-at: 2026-09-28T15:35:35+03:30
---

# Session Objective

Apply AC001 to the researcher's second free-form research idea, preserve the
input verbatim, and test whether the contract distinguishes a reported
long-term market premise from a testable strategy question.

This session also records and corrects the invalid provenance of Q002 and
S004, which had been created from assistant-invented rather than
user-provided input.

---

# What Was Done

- Applied AC001 version 1.1 to the researcher's gold trend-following idea.
- Preserved the original Persian input verbatim in Q003.
- Recorded the researcher's selection of spot gold quoted in US dollars
  (XAU/USD) as Q003 version 1.1.
- Treated the statement that gold has always risen as user-reported, not as
  verified evidence.
- Recorded that one year was initially presented as an example, then
  confirmed by the researcher as the maximum for each position.
- Recorded positive net returns after costs as the primary success criterion,
  with buy-and-hold comparison reported separately.
- Recorded six years as the historical evaluation period selected by the
  researcher.
- Recorded a hard maximum holding period of one year for each position, as
  confirmed by the researcher.
- Selected a six-year historical backtest; inclusive start and end dates were
  later confirmed as `2020-09-28` through `2026-09-28`.
- Recorded that the six-year historical period is not automatically
  out-of-sample; the strategy rules must be frozen before its results are
  inspected for that label to be warranted.
- Confirmed the inclusive six-year evaluation dates
  `2020-09-28` through `2026-09-28` before inspecting any backtest results.
- Selected daily observations for the six-year historical backtest.
- Selected Dukascopy's public historical export as the intended source;
  Bid and Ask are chosen separately in the observed widget.
- Verified that Dukascopy Bank's official Historical Data Export page
  describes historical exports for Forex, commodities, and indices, with CSV
  and timeframes from tick to monthly; its live selector lists XAU/USD.
- Inspected the export dialog: the visible period options were Tick, Second,
  Minute, and Hour; Bid and Ask were separate selections. No file was
  downloaded.
- The official FAQ refers to JForex Historical Data Manager for more custom
  timeframes. Earlier descriptions in this log of a supplied daily file or
  individual raw tick records are superseded by the export-sample clarification
  below.
- The researcher reported that the latest date displayed in the file is
  `28/9/2026`. On 2026-09-29, the researcher confirmed the inclusive
  six-year evaluation window `2020-09-28` through `2026-09-28`. The file's
  timezone and daily bar conventions have not been independently verified.
- On 2026-09-29, the researcher shared small Bid and Ask excerpts downloaded
  separately from the public site with `Tick` selected. Both excerpts show
  `Open`, `High`, `Low`, `Close`, and `Volume`; the time-zone label is
  `Europe/Amsterdam`, and a supplied Bid timestamp ends in `+02:00`.
- The researcher reports matching timestamps between the separate Bid/Ask
  downloads and confirms that each row represents one tick whose timestamp
  marks when it was recorded. The researcher corrected the earlier Ask
  excerpt: the corrected sample has equal Open, High, Low, and Close values
  per row, consistent with one price per tick. Multiple rows share a
  second-level timestamp. These reports have not been independently verified
  against the full files.
- The researcher selected fixed UTC+02 daily boundaries and the approved
  aggregation: first Open, maximum High, minimum Low, and last Close per day
  for each side, preserving source order for records with duplicate
  timestamps. Use the timestamp's `Europe/Amsterdam` context and explicit
  offsets to convert instants to fixed UTC+02. Omit empty days and do not
  forward-fill.
- On 2026-09-29, the researcher approved and froze a single SMA200
  long-only baseline before examining evaluation-period returns, including
  signal prices, next-bar Bid/Ask execution, the one-year time stop,
  post-stop re-entry rule, 1x compounded exposure, cost treatment, and
  symmetric buy-and-hold benchmark.
- The researcher reports that no SMA200 returns from `2020-09-28` through
  `2026-09-28` were reviewed or used before the rules were frozen. The period
  is designated as a holdout subject to this report and later data validation.
- Registered the official page and the researcher-reported Tick-selected
  Bid/Ask OHLCV exports as SRC006. The full files, row semantics, timestamp
  interpretation, volume meaning, complete alignment, coverage, and
  missing-record pattern remain unverified.
- Separated the historical-trend premise, strategy performance, and risk
  criteria into a primary question and related independent questions.
- Deprecated Q002 and added provenance corrections to Q002 and S004 because
  their crypto idea was generated by the assistant, not supplied by the
  researcher.

---

# What Was Learned

## The contract needs exact-language preservation stated explicitly

AC001 already required verbatim preservation. This run made the requirement
operational by clarifying that language, script, informal wording, and
formatting must also remain unchanged and must not be translated or
normalized.

## An example can become a constraint only after confirmation

The original wording offered one year as an example. When asked directly, the
researcher confirmed it as the fixed maximum for each position. Q003 records
that follow-up decision rather than inferring it from the initial wording.

## A long-run premise and a strategy edge are distinct questions

The reported belief about gold's long-term direction does not establish that a
trend-following strategy can earn positive net returns or outperform a
benchmark over the proposed holding horizon. The artifact keeps these claims
separate.

## Provenance errors must be explicitly corrected

Q002 and S004 attributed invented crypto input to the researcher and falsely
recorded an AC001 validation. They are now marked as invalid for that purpose;
the actual second manual test is Q003/S005.

---

# Decisions

- Keep AC001 in draft; this run is additional manual validation, not approval
  for automation.
- Retain Q002 as deprecated for traceability, with an explicit provenance
  correction; do not use it as project knowledge or a valid AC001 test.
- Treat Q003 as the actual second user-provided Question / Observation
  artifact.
- Apply a one-year maximum holding period to each position, as selected by the
  researcher after clarifying that it had initially been offered only as an
  example.
- Define Q003's instrument as spot gold quoted in US dollars (XAU/USD), as
  selected by the researcher.
- Treat positive net returns after costs as the primary success criterion;
  report comparison with buy-and-hold separately.
- Set the historical evaluation horizon to six years.
- Use a historical six-year backtest for that evaluation.
- Designate the fixed evaluation period as the out-of-sample holdout, based on
  the researcher's report that no SMA200 returns were reviewed before the
  rules were frozen.
- Freeze the six-year inclusive evaluation dates at `2020-09-28` through
  `2026-09-28`, as confirmed by the researcher and before examining results.
- Record the researcher's report that each `Tick`-selected row is one tick
  and its timestamp marks the tick record time; the corrected Ask sample has
  equal OHLC values per row and repeated second-level timestamps. Validate
  these conventions against the full exports before computing results.
- Construct daily bars using fixed-UTC+02 boundaries and the approved OHLC
  aggregation, preserving source row order for duplicate timestamps; omit
  empty days and do not forward-fill.
- Freeze the SMA200 baseline rules before examining evaluation returns; do not
  tune them against this period.
- Use Ask for entries and Bid for exits; include historical commissions and
  financing/swap charges where reliable records exist, and disclose gaps
  rather than claiming full net returns when material costs are unavailable.
- Compare against a 1x buy-and-hold benchmark using the same evaluation
  boundaries and available cost treatment.
- Disclose material cost inputs that cannot be verified; do not describe
  incomplete-cost results as fully net.
- Use daily observations for the backtest.
- Use separate Tick-selected Bid and Ask OHLCV exports from the Dukascopy
  public historical page. The researcher reports matching timestamps and
  displayed coverage `5/5/2003`–`28/9/2026`; validate one tick per row,
  equal OHLC values within each tick, timestamp precision/order, and full
  Bid/Ask alignment before generating daily bars.
- Cite SRC006 for provider-page claims and distinguish shared sample
  observations and researcher reports from independently verified facts. Do
  not treat the exports as validated until timestamp semantics, coverage,
  and alignment are checked.
- Obtain or inspect the full Bid/Ask exports to validate timestamp semantics,
  coverage, and missing records; do not share account credentials.

---

# Artifacts Created

- questions/Q003-long-only-gold-trend-following.md (Q003) — second valid
  manual Question / Observation result, status draft.
- research/sessions/S005-gold-question-formulation-test.md (S005) — this
  session.

# Artifacts Modified

- governance/agent-contracts/AC001-question-formulation.md (AC001) — version
  1.1 clarifies exact preservation of multilingual and informal input.
- questions/Q002-crypto-relative-mean-reversion.md (Q002) — deprecated with
  provenance correction.
- questions/Q003-long-only-gold-trend-following.md (Q003) — updated with
  researcher clarifications through version 3.5.
- sources/SRC006-dukascopy-historical-data-export.md (SRC006) — registered the
  official Dukascopy Bank export page and recorded the shared public-export
  samples while retaining verification limitations; updated to version 2.1.
- research/sessions/S004-question-formulation-second-test.md (S004) — appended
  provenance correction.
- governance/artifact-registry.json — registered Q003 and updated artifact
  versions and status, including SRC006 v2.1 and Q003 v3.5.
- sources/README.md and README.md — registered SRC006 in the source indexes.
- questions/README.md and README.md — updated question and session indexes.
- operating-system/CURRENT.md — recorded the confirmed evaluation window and
  next validation steps.

---

# Outcome

The actual second manual application of AC001 produced Q003 without treating
the user's premise as verified evidence or assuming the one-year example was
already a fixed constraint. The contract's raw-input requirement was
clarified. No hypothesis, experiment, trading recommendation, or automation
was created.

In follow-up, the researcher selected spot gold quoted in US dollars
(XAU/USD), positive net returns after costs as the primary success criterion,
a separate buy-and-hold comparison, a six-year historical evaluation period,
daily observations, and a hard one-year maximum holding period for each
position. The researcher shared small Bid and Ask OHLCV excerpts from
separate public-site downloads with `Tick` selected, reporting matching
timestamps and displayed coverage `5/5/2003` through `28/9/2026`. The excerpt
labels time `Europe/Amsterdam` and includes a sample timestamp at `+02:00`.
The researcher confirms each row is one tick and the timestamp marks when it
was recorded, then corrects the Ask sample: OHLC values are equal within each
row, with multiple ticks sharing second-level timestamps. The researcher
approved fixed-UTC+02 daily boundaries and OHLC aggregation, preserving row
order for repeated timestamps; empty days are to be omitted and not
forward-filled. The full files and these conventions still require validation.
The researcher
confirmed the inclusive
evaluation window `2020-09-28` through `2026-09-28` and approved a single
SMA200 long-only baseline, its next-bar Ask/Bid execution, position sizing,
time stop, cost treatment, and buy-and-hold benchmark before examining
returns. The researcher reports that no SMA200 returns from the evaluation
period were reviewed before rule freeze; the period is designated as a
holdout subject to that report and subsequent data validation. Full files
have not been inspected in Project Zero. Q003 was updated to version 3.5.

---

# Relationships

- related-to: questions/Q003-long-only-gold-trend-following.md (Q003)
- related-to: governance/agent-contracts/AC001-question-formulation.md (AC001)
- related-to: research/sessions/S004-question-formulation-second-test.md (S004)
- derives-from: research/003-research-methodology.md (research-003)
- related-to: governance/rules/RG001-automation-follows-stability.md (RG001)
- related-to: governance/rules/RG008-authorship-provenance.md (RG008)
