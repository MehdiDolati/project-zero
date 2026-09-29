# Project Zero — Current State

## Current Direction

Continue the manual Question / Observation workflow with clear input
provenance, then resolve the open scope decisions in Q003 before proposing any
hypothesis or experiment.

## Current Objective

Verify JForex daily-bar conventions and freeze the strategy rules before
examining results from the confirmed six-year evaluation window.

## NEXT ACTION

Verify the timezone and daily bar conventions in the researcher-viewed JForex
file; freeze strategy rules before examining the confirmed evaluation window.

## Why This Matters

The actual second manual AC001 test is now recorded in Q003 and S005. The
selected instrument is spot XAU/USD, and the evaluation is a six-year
historical backtest. It only qualifies as out of sample if the strategy rules
are frozen before examining its results. Positive net returns after costs are
the primary success criterion, with comparison to buy-and-hold reported
separately. Each position must be closed no later than one year after entry.
The researcher reports viewing a JForex file with daily XAU/USD Bid and Ask
data from `5/5/2003` through `28/9/2026`. The researcher confirmed the
inclusive six-year window `2020-09-28`–`2026-09-28`. The file was not provided
to Project Zero; timezone, daily bar conventions, and account-feed match
remain unverified. The period is out of sample only if the strategy rules are
frozen before results are examined.

## Blockers

- None

## Last Session

[S005 — Gold Question Formulation Test](../research/sessions/S005-gold-question-formulation-test.md)

## EXIT CHECK

- [x] What did I actually do? Applied AC001 to the researcher's gold
  trend-following idea and created Q003; corrected Q002/S004, whose input had
  been invented by the assistant.
- [x] What did I learn? Daily observations are selected for the six-year
  historical backtest; each position has a one-year maximum.
- [x] What changed? Added Q003 and S005, clarified AC001 v1.1, deprecated Q002,
  corrected S004 provenance, registered Q003, and updated the indexes and
  registry.
- [ ] What is the exact next action? Verify the JForex timezone and daily bar
  conventions, then freeze strategy rules before examining results from the
  confirmed evaluation window.
