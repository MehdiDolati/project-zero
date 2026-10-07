#!/usr/bin/env python3
"""Build fixed-UTC+02 daily bars from the accepted EXP002 master (Q003/DEC002).

Frozen construction (Q003 "Locked Baseline Strategy" + DEC002 decision 3):
  - bucket each tick into a fixed UTC+02 calendar day [00:00, 00:00 next day);
  - per side (Bid and Ask independently, from the tick Bid/Ask fields):
      first row -> Open, maximum -> High, minimum -> Low, last row -> Close;
  - preserve source file order for ticks sharing a timestamp;
  - omit days with no records; do not forward-fill.

Time-zone caveat (DEC002 decision 5): the delivered master's DateTime is naive
and its time zone is UNVERIFIED. With no offset present, this tool treats the
naive timestamp's calendar date as the fixed UTC+02 day. This assumption is
disclosed in every derived artifact.

This tool computes NO strategy signal or return (freeze discipline).

Usage:
  python build_daily_bars.py [--path CSV] [--out CSV] [--emit-from YYYYMMDD]
                             [--summary JSON] [--progress N]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.abspath(os.path.join(HERE, os.pardir, "evidence", "raw"))
DERIVED_DIR = os.path.abspath(os.path.join(HERE, os.pardir, "evidence", "derived"))
CSV_PATH = os.path.join(RAW_DIR, "XAUUSD-TICK-full.csv")
OUT_PATH = os.path.join(DERIVED_DIR, "daily-bars-utc02.csv")
EXPECTED_HEADER = "DateTime,Bid,Ask,Volume"
CHUNK = 8 * 1024 * 1024


def build(path, out_path, emit_from, progress_every):
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    stats = {
        "source": path, "header_ok": False, "data_rows": 0,
        "skipped_before_emit": 0, "bars_written": 0, "first_bar": None,
        "last_bar": None, "min_rows_per_bar": None, "max_rows_per_bar": 0,
        "sum_rows_in_bars": 0, "malformed_rows": 0, "bad_numeric_rows": 0,
        "emit_from": emit_from,
    }
    cur_date = None
    b_o = b_h = b_l = b_c = None
    a_o = a_h = a_l = a_c = None
    vol = 0
    nrows = 0

    def flush(fh):
        nonlocal b_o, b_h, b_l, b_c, a_o, a_h, a_l, a_c, vol, nrows
        if cur_date is None:
            return
        fh.write(
            f"{cur_date},{b_o:.10g},{b_h:.10g},{b_l:.10g},{b_c:.10g},"
            f"{a_o:.10g},{a_h:.10g},{a_l:.10g},{a_c:.10g},{vol:.10g},{nrows}\n"
        )
        stats["bars_written"] += 1
        stats["sum_rows_in_bars"] += nrows
        if stats["min_rows_per_bar"] is None or nrows < stats["min_rows_per_bar"]:
            stats["min_rows_per_bar"] = nrows
        if nrows > stats["max_rows_per_bar"]:
            stats["max_rows_per_bar"] = nrows
        if stats["first_bar"] is None:
            stats["first_bar"] = cur_date
        stats["last_bar"] = cur_date

    t0 = time.time()
    with open(path, "r", encoding="ascii", newline="", buffering=CHUNK) as f, \
            open(out_path, "w", encoding="ascii", newline="\n") as out:
        header = f.readline().rstrip("\r\n")
        stats["header_ok"] = header == EXPECTED_HEADER
        out.write("Date,Bid_Open,Bid_High,Bid_Low,Bid_Close,"
                  "Ask_Open,Ask_High,Ask_Low,Ask_Close,Volume,RowCount\n")

        for line in f:
            line = line.rstrip("\r\n")
            if not line:
                continue
            stats["data_rows"] += 1
            n = stats["data_rows"]
            if n % progress_every == 0:
                dt = time.time() - t0
                print(f"  [build] {n:,} rows  date={cur_date}  "
                      f"bars={stats['bars_written']:,}  "
                      f"({n / dt / 1e6:.2f}M rows/s)", flush=True)

            parts = line.split(",")
            if len(parts) != 4:
                stats["malformed_rows"] += 1
                continue
            ts, bid_s, ask_s, vol_s = parts
            date = ts[:8]
            if date < emit_from:
                stats["skipped_before_emit"] += 1
                continue
            try:
                bid = float(bid_s)
                ask = float(ask_s)
            except ValueError:
                stats["bad_numeric_rows"] += 1
                continue
            try:
                v = float(vol_s)
            except ValueError:
                v = 0.0

            if date != cur_date:
                flush(out)
                cur_date = date
                b_o = b_h = b_l = b_c = bid
                a_o = a_h = a_l = a_c = ask
                vol = v
                nrows = 1
            else:
                b_c = bid
                a_c = ask
                if bid > b_h:
                    b_h = bid
                if bid < b_l:
                    b_l = bid
                if ask > a_h:
                    a_h = ask
                if ask < a_l:
                    a_l = ask
                vol += v
                nrows += 1
        flush(out)

    stats["elapsed_s"] = round(time.time() - t0, 1)
    return stats


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default=CSV_PATH)
    ap.add_argument("--out", default=OUT_PATH)
    ap.add_argument("--emit-from", default="20180101")
    ap.add_argument("--summary", default=os.path.join(
        DERIVED_DIR, "daily-bars-summary.json"))
    ap.add_argument("--progress", type=int, default=50_000_000)
    args = ap.parse_args()

    if not os.path.exists(args.path):
        print(f"NOT FOUND: {args.path}")
        return 1
    size = os.path.getsize(args.path)
    print(f"Source: {args.path}  ({size/1e9:.2f} GB)")
    print(f"Output: {args.out}")
    print(f"Emit from: {args.emit_from} (warm-up starts here)")

    stats = build(args.path, args.out, args.emit_from, args.progress)
    print("--- SUMMARY ---")
    for k in ("header_ok", "data_rows", "skipped_before_emit", "bars_written",
              "malformed_rows", "bad_numeric_rows", "first_bar", "last_bar",
              "min_rows_per_bar", "max_rows_per_bar", "sum_rows_in_bars",
              "elapsed_s"):
        print(f"{k:20s}: {stats[k]}")
    os.makedirs(os.path.dirname(os.path.abspath(args.summary)), exist_ok=True)
    with open(args.summary, "w", encoding="utf-8") as jf:
        json.dump(stats, jf, indent=2, sort_keys=True)
    print(f"Summary written: {args.summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())