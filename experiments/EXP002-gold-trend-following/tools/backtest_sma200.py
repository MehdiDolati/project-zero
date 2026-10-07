#!/usr/bin/env python3
"""Frozen EXP002 baseline backtest: SMA200 long-only trend following on XAU/USD.

Implements EXACTLY the "Locked Baseline Strategy" frozen in
questions/Q003-long-only-gold-trend-following.md (approved 2026-09-29, before
any evaluation returns were examined) over the fixed inclusive window
2020-09-28 through 2026-09-28. Rules are NOT tuned here.

Frozen rules implemented:
  - Signal: SMA of the latest 200 completed daily Bid Close prices, including
    the current signal bar. Pre-window bars are warm-up only.
  - Entry: while flat, a daily Bid Close ABOVE the SMA200 -> long entry at the
    NEXT daily bar's Open Ask. At most one position; never short.
  - Signal exit: a daily Bid Close AT OR BELOW the SMA200 -> exit at the NEXT
    daily bar's Open Bid.
  - Max holding: one calendar year from entry. If no signal exit occurs first,
    close at the Bid Close of the last available daily bar ending on or before
    the one-year anniversary.
  - Re-entry after a time stop: stay flat until a daily Bid Close <= SMA200 is
    followed by a subsequent daily Bid Close > SMA200; enter at the next Open
    Ask after the renewed above-SMA signal.
  - Exposure: 100% of equity, 1x, compounded; cash earns zero while flat.
  - Costs: quoted spread captured via Ask entry / Bid exit. Commissions and
    financing/swap are NOT included (no reliable historical records); results
    are NET OF SPREAD ONLY and must not be described as fully net of costs.
  - Window end: any open position is closed at the final evaluation bar's Bid
    Close.
  - Benchmark: buy-and-hold, same capital/1x, entry at first evaluation bar's
    Open Ask, liquidation at final bar's Bid Close, same cost treatment.

Usage:
  python backtest_sma200.py [--bars CSV] [--trades CSV] [--summary JSON]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
DERIVED_DIR = os.path.abspath(os.path.join(HERE, os.pardir, "evidence", "derived"))
BARS_PATH = os.path.join(DERIVED_DIR, "daily-bars-utc02.csv")
TRADES_PATH = os.path.join(DERIVED_DIR, "backtest-trades.csv")
SUMMARY_PATH = os.path.join(DERIVED_DIR, "backtest-summary.json")

WINDOW_START = date(2020, 9, 28)
WINDOW_END = date(2026, 9, 28)
SMA_LEN = 200


def parse_date(s):
    return date(int(s[0:4]), int(s[4:6]), int(s[6:8]))


def add_year(d, n):
    try:
        return d.replace(year=d.year + n)
    except ValueError:
        return d.replace(year=d.year + n, day=28)  # 29 Feb -> 28 Feb


def load_bars(path):
    header = None
    rows = []
    with open(path, "r", encoding="ascii", newline="") as f:
        header = f.readline().rstrip("\r\n")
        for line in f:
            line = line.rstrip("\r\n")
            if not line:
                continue
            p = line.split(",")
            if len(p) != 11:
                continue
            rows.append((
                p[0],
                float(p[1]), float(p[2]), float(p[3]), float(p[4]),   # bid O H L C
                float(p[5]), float(p[6]), float(p[7]), float(p[8]),   # ask O H L C
            ))
    return header, rows


def max_drawdown(curve):
    peak = curve[0]
    mdd = 0.0
    for v in curve:
        if v > peak:
            peak = v
        dd = v / peak - 1.0
        if dd < mdd:
            mdd = dd
    return mdd


def run(rows):
    n = len(rows)
    dates = [parse_date(r[0]) for r in rows]
    bc = [r[4] for r in rows]   # Bid Close
    bo = [r[1] for r in rows]   # Bid Open
    ao = [r[5] for r in rows]   # Ask Open

    # SMA200 on Bid Close
    sma = [None] * n
    s = 0.0
    for i in range(n):
        s += bc[i]
        if i >= SMA_LEN:
            s -= bc[i - SMA_LEN]
        if i >= SMA_LEN - 1:
            sma[i] = s / SMA_LEN

    # window indices
    w0 = next(i for i in range(n) if dates[i] >= WINDOW_START)
    w1 = max(i for i in range(n) if dates[i] <= WINDOW_END)

    def ts_index(entry_date):
        ann = add_year(entry_date, 1)
        idx = None
        for i in range(w0, w1 + 1):
            if dates[i] <= ann:
                idx = i
            else:
                break
        return idx if idx is not None else w0

    equity = 1.0
    units = 0.0
    state = 0            # 0 flat, 1 long
    pending = None       # None | 'enter' | 'exit'
    entry_date = None
    entry_ts_idx = None
    reentry_blocked = False
    saw_below = False
    trades = []
    eq_curve = []
    invested = 0

    for k in range(w0, w1 + 1):
        # 1) execute any order scheduled at this bar's open
        if pending == "enter":
            px = ao[k]
            units = equity / px
            state = 1
            entry_date = dates[k]
            entry_ts_idx = ts_index(entry_date)
            reentry_blocked = False
            saw_below = False
            trades.append({"entry_date": dates[k].isoformat(), "entry_px": px,
                           "exit_date": None, "exit_px": None, "reason": None})
            pending = None
        elif pending == "exit":
            px = bo[k]
            equity = units * px
            units = 0.0
            state = 0
            trades[-1]["exit_date"] = dates[k].isoformat()
            trades[-1]["exit_px"] = px
            trades[-1]["reason"] = "signal"
            pending = None

        # 2) time stop at end of bar
        if state == 1 and pending is None and k >= entry_ts_idx:
            equity = units * bc[k]
            units = 0.0
            state = 0
            trades[-1]["exit_date"] = dates[k].isoformat()
            trades[-1]["exit_px"] = bc[k]
            trades[-1]["reason"] = "time_stop"
            reentry_blocked = True
            saw_below = False
            eq_curve.append(equity)
            continue

        # 3) end-of-bar signal decisions
        if sma[k] is not None:
            if state == 0 and pending is None:
                if bc[k] > sma[k]:
                    if not reentry_blocked:
                        if k < w1:
                            pending = "enter"
                    elif saw_below:
                        reentry_blocked = False
                        if k < w1:
                            pending = "enter"
                else:
                    if reentry_blocked:
                        saw_below = True
            elif state == 1 and pending is None:
                if bc[k] <= sma[k] and k < w1:
                    pending = "exit"

        # 4) mark to market at close
        if state == 1:
            eq_curve.append(units * bc[k])
            invested += 1
        else:
            eq_curve.append(equity)

    # window-end liquidation of any open position
    if state == 1:
        equity = units * bc[w1]
        trades[-1]["exit_date"] = dates[w1].isoformat()
        trades[-1]["exit_px"] = bc[w1]
        trades[-1]["reason"] = "window_end"
        units = 0.0

    # benchmark: buy-and-hold over the window
    bh_units = 1.0 / ao[w0]
    bh_curve = [bh_units * bc[k] for k in range(w0, w1 + 1)]
    bh_final = bh_units * bc[w1]

    # trade stats
    n_trades = len(trades)
    holding_days = []
    for t in trades:
        if t["exit_date"]:
            holding_days.append((parse_date(t["exit_date"].replace("-", ""))
                                 - parse_date(t["entry_date"].replace("-", ""))).days)
    years = (WINDOW_END - WINDOW_START).days / 365.25
    total_ret = equity - 1.0
    cagr = equity ** (1.0 / years) - 1.0 if equity > 0 else -1.0
    bh_total = bh_final - 1.0
    bh_cagr = bh_final ** (1.0 / years) - 1.0 if bh_final > 0 else -1.0

    return {
        "window_start": WINDOW_START.isoformat(),
        "window_end": WINDOW_END.isoformat(),
        "bars_in_window": w1 - w0 + 1,
        "first_bar": dates[w0].isoformat(),
        "last_bar": dates[w1].isoformat(),
        "starting_capital": 1.0,
        "strategy_final_equity": round(equity, 6),
        "strategy_total_return": round(total_ret, 6),
        "strategy_cagr": round(cagr, 6),
        "strategy_max_drawdown": round(max_drawdown(eq_curve), 6),
        "benchmark_final_equity": round(bh_final, 6),
        "benchmark_total_return": round(bh_total, 6),
        "benchmark_cagr": round(bh_cagr, 6),
        "benchmark_max_drawdown": round(max_drawdown(bh_curve), 6),
        "n_trades": n_trades,
        "avg_holding_days": round(sum(holding_days) / len(holding_days), 1)
        if holding_days else 0.0,
        "max_holding_days": max(holding_days) if holding_days else 0,
        "bars_invested": invested,
        "pct_time_invested": round(100.0 * invested / (w1 - w0 + 1), 2),
        "exit_reasons": {
            r: sum(1 for t in trades if t["reason"] == r)
            for r in ("signal", "time_stop", "window_end")
        },
        "cost_treatment": "spread_only (Ask entry / Bid exit); commissions and "
                          "financing/swap NOT included (no reliable records)",
        "rules_frozen": "Q003 Locked Baseline Strategy, approved 2026-09-29",
    }, eq_curve, trades, dates, w0, w1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bars", default=BARS_PATH)
    ap.add_argument("--trades", default=TRADES_PATH)
    ap.add_argument("--summary", default=SUMMARY_PATH)
    args = ap.parse_args()

    if not os.path.exists(args.bars):
        print(f"NOT FOUND: {args.bars}")
        return 1
    header, rows = load_bars(args.bars)
    print(f"Bars loaded: {len(rows):,}  (header={header!r})")
    if not rows:
        print("No bars; aborting.")
        return 1

    summary, eq_curve, trades, dates, w0, w1 = run(rows)

    print("--- BACKTEST SUMMARY (net of spread only) ---")
    for k in ("window_start", "window_end", "bars_in_window", "first_bar",
              "last_bar", "strategy_final_equity", "strategy_total_return",
              "strategy_cagr", "strategy_max_drawdown", "benchmark_final_equity",
              "benchmark_total_return", "benchmark_cagr",
              "benchmark_max_drawdown", "n_trades", "avg_holding_days",
              "max_holding_days", "pct_time_invested", "exit_reasons"):
        print(f"{k:24s}: {summary[k]}")

    os.makedirs(os.path.dirname(os.path.abspath(args.summary)), exist_ok=True)
    with open(args.summary, "w", encoding="utf-8") as jf:
        json.dump(summary, jf, indent=2, sort_keys=True)
    print(f"Summary written: {args.summary}")

    with open(args.trades, "w", encoding="ascii", newline="\n") as tf:
        tf.write("entry_date,entry_px,exit_date,exit_px,reason\n")
        for t in trades:
            tf.write(f"{t['entry_date']},{t['entry_px']:.6g},"
                     f"{t['exit_date']},{t['exit_px']:.6g},{t['reason']}\n")
    print(f"Trades written: {args.trades}  ({len(trades)} trades)")
    return 0


if __name__ == "__main__":
    sys.exit(main())