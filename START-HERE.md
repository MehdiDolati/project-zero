# Project Zero — Start Here

> **If you have been away from Project Zero for a while, start here.**
>
> This document is a re-entry path, not a documentation index.
> Its job is to restore the context needed to continue the project without redesigning it from scratch.

---

## 1. What is Project Zero?

Project Zero is a long-term research project for answering one question:

> **How can a solo researcher systematically discover, validate, deploy, monitor, and retire trading edge to achieve sustainable financial freedom?**

The goal is **not** to build a trading platform.

The goal is **not** to find a magical strategy.

The goal is **not** to prove that a particular strategy will remain profitable.

The goal is to build a repeatable process for discovering and managing trading edge under uncertainty.

Software, automation, AI, and infrastructure are tools that may support this process when they provide real leverage. They are not the project itself.

---

## 2. The North Star

Before doing anything else, read:

**[`research/000-north-star.md`](research/000-north-star.md)**

The North Star defines the long-horizon question and keeps local decisions connected to the actual purpose of Project Zero.

Do not replace the North Star with today's task.

Today's task is temporary.

The North Star is the reason the task exists.

---

## 3. The Core Idea

Project Zero treats trading as a **continuous edge-discovery and management problem**.

An edge may be:

* discovered,
* tested,
* rejected,
* refined,
* validated,
* deployed,
* monitored,
* degraded,
* retired,
* or replaced.

Therefore:

> **A failed hypothesis is not wasted work if it improves the research process or eliminates a false path.**

The objective is not certainty.

The objective is to make better decisions with evidence.

---

## 4. What We Believe

These are working principles, not eternal truths.

### 4.1 Research comes before software

Do not build software merely because software can be built.

First establish that a research or operational activity is sufficiently understood and repeatable to justify automation.

> **No software before method.**

This is especially important because building infrastructure can create the illusion of progress while avoiding the difficult research question.

---

### 4.2 Edge discovery is the primary activity

The central challenge is not constructing a sophisticated trading platform.

It is discovering whether useful, persistent, exploitable patterns exist—and understanding the conditions under which they may or may not persist.

Strategy generation and research are therefore first-class activities.

---

### 4.3 Backtests are evidence, not truth

A backtest does not establish that an edge is real.

Results must be interpreted in the context of:

* data quality,
* assumptions,
* sample selection,
* parameter choices,
* transaction costs,
* robustness,
* out-of-sample behavior,
* regime dependence,
* and other sources of false discovery.

The question is not merely:

> "Did this strategy make money?"

The better question is:

> "What evidence do we have, and what alternative explanations could produce this result?"

---

### 4.4 Simplicity is a feature

Project Zero is a solo research effort.

Complexity has a cost.

Do not introduce:

* unnecessary governance,
* unnecessary abstractions,
* unnecessary automation,
* unnecessary infrastructure,
* or documentation that does not improve research quality.

When in doubt, prefer the smallest mechanism that solves the actual problem.

---

### 4.5 The repository is the source of truth

If an important decision, rule, hypothesis, result, or change in direction matters to Project Zero, it should eventually exist in the repository.

> **If it is not in the repository, it does not exist.**

Chat conversations, temporary thoughts, and memory are not substitutes for project knowledge.

---

## 5. What Project Zero Is NOT

Do not let the project drift into these goals without an explicit decision to change direction:

* Building a generic trading platform.
* Building an AI system for its own sake.
* Automating research before the research process is understood.
* Optimizing backtests indefinitely.
* Collecting tools instead of generating evidence.
* Creating governance for governance's sake.
* Turning documentation into the primary activity.
* Assuming that past profitability implies future profitability.
* Treating a single successful strategy as the destination.

If you notice the project moving in one of these directions, stop and return to the North Star.

---

## 6. Where Are We Now?

Project Zero is intentionally being developed from the **research process outward**.

The current priority is to establish a practical research and decision-making process before building a larger software system around it.

That means the immediate question is not:

> "What platform should I build?"

It is:

> "What research process actually works, and which parts are worth systematizing?"

The current state of the project is always represented by:

**[`operating-system/CURRENT.md`](operating-system/CURRENT.md)**

Do not infer the current state from this document.

`CURRENT.md` is the operational source for **where we are now**.

---

## 7. How We Work

The basic loop is:

```text
QUESTION / OBSERVATION
        ↓
HYPOTHESIS
        ↓
RESEARCH
        ↓
EVIDENCE
        ↓
DECISION
        ↓
NEXT ACTION
        ↓
REPEAT
```

Over time, promising ideas may move through a broader lifecycle:

```text
IDEA
  ↓
RESEARCH
  ↓
TEST
  ↓
VALIDATION
  ↓
DEPLOYMENT
  ↓
MONITORING
  ↓
RETIREMENT / CONTINUATION
```

The exact process should evolve from real experience.

Do not design the perfect process in advance.

---

## 8. How To Continue After Returning

You do **not** need to reread the entire repository.

Follow this order:

### Step 1 — Reconnect with the purpose

Read:

**[`research/000-north-star.md`](research/000-north-star.md)**

If you remember the project well, this can be a quick refresh.

If you do not remember anything, read it carefully.

---

### Step 2 — Reconnect with the current state

Open:

**[`operating-system/CURRENT.md`](operating-system/CURRENT.md)**

This tells you:

* what we are currently doing,
* what happened in the previous session,
* what was learned,
* what decisions were made,
* and most importantly:

> **What is the next action?**

---

### Step 3 — Follow the existing direction

Do the `NEXT ACTION`.

Do not redesign Project Zero before completing the work that is already in front of you.

Do not open the Parking Lot just because an interesting idea appears.

Capture the idea and continue.

---

### Step 4 — If something no longer makes sense

Stop and investigate the mismatch.

Do not silently change the project's direction.

If the North Star, assumptions, or current approach genuinely need to change:

1. understand why,
2. record the evidence,
3. make the decision explicit,
4. update the relevant source-of-truth document,
5. then continue.

---

## 9. The Daily Interface

For normal work, there is one operational file:

**[`operating-system/CURRENT.md`](operating-system/CURRENT.md)**

### At the beginning of a session

Open `CURRENT.md`.

Read the current context.

Find:

> **NEXT ACTION**

Start there.

---

### During the session

Work.

When new ideas appear, do not automatically switch direction.

Put them in the Parking Lot and continue with the current objective.

---

### At the end of the session

Update `CURRENT.md` with:

* what was completed,
* what was learned,
* important decisions,
* and the next concrete action.

The goal is simple:

> **Make it easy for Future Me to continue exactly where Present Me stopped.**

---

## 10. When You Feel Lost

Use this sequence:

```text
CURRENT.md
    ↓
What is the NEXT ACTION?
    ↓
Why are we doing it?
    ↓
North Star
    ↓
Relevant research / decision
    ↓
Continue
```

Do not respond to confusion by creating more process.

First recover context.

---

## One Rule You Must Not Forget

Project Zero is allowed to change direction.

You are allowed to follow an interesting idea, stop a line of research, or leave the project for a while.

But before leaving a meaningful piece of work behind, make the project resumable.

Update:

**[`operating-system/CURRENT.md`](operating-system/CURRENT.md)**

The repository enforces this with a pre-push check.

If your push is blocked, it is not asking you to do more bureaucracy. It is asking one question:

> **If Future Me came back now, would he know exactly where the project stands and what to do next?**


## 11. The Most Important Rules

If you remember nothing else, remember these:

1. **Follow the North Star.**
2. **Work from the current state, not from memory.**
3. **One concrete NEXT ACTION at a time.**
4. **Research before unnecessary software.**
5. **Evidence over belief.**
6. **Failed hypotheses are useful evidence.**
7. **Capture distractions instead of following them.**
8. **Keep the system as simple as possible.**
9. **Record important decisions in the repository.**
10. **Optimize for continuous edge discovery, not certainty.**

---

## 12. Now Start

If you have read this document, you have enough context to begin.

Open:

**[`operating-system/CURRENT.md`](operating-system/CURRENT.md)**

Find:

> **NEXT ACTION**

And continue.

Do not build anything else until the current work tells you that something else is needed.

---

> **Think big. Take small steps. Start now.**
