#!/usr/bin/env python3
"""Streaming verification of the full XAU/USD tick export (EXP002).

Runs two passes over the raw master and never loads it fully into memory:

  Pass 1 (binary, chunked): SHA-256 of the stored bytes.
  Pass 2 (text, line-by-line): structural and semantic checks.

It deliberately does NOT compute any strategy signal or return, per Q003
(freeze discipline): it only validates the raw dataset conventions.

Checks (Pass 2):
  - header equals ``DateTime,Bid,Ask,Volume``
  - every data row has exactly 4 fields
  - DateTime matches ``YYYYMMDD HH:MM:SS.mmm``
  - Bid and Ask parse as positive numbers
  - no crossed quotes (Ask < Bid)
  - coverage: first/last timestamp, distinct calendar days
  - timestamp ordering: monotonic non-decreasing (lexicographic == chronological
    for this fixed-width, zero-padded format)
  - duplicate second-level timestamps (same second, different millisecond)
  - per-year row counts

Output: a human-readable summary printed to stdout and, optionally, a
machine-readable JSON report written next to the raw area under ``derived/``.

Usage:
  python verify_full.py [--skip-hash] [--json PATH] [--progress N]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.abspath(os.path.join(HERE, os.pardir, "evidence", "raw"))
CSV_PATH = os.path.join(RAW_DIR, "XAUUSD-TICK-full.csv")
EXPECTED_HEADER = "DateTime,Bid,Ask,Volume"
CHUNK = 8 * 1024 * 1024


def human(n: float) -> str:
    for unit in ("B", "KiB", "MiB", "GiB", "TiB"):
        if n < 1024:
            return f"{n:.2f} {unit}"
        n /= 1024
    return f"{n:.2f} PiB"


def sha256(path: str, progress_every: int = 2_000_000_000) -> tuple[str, int]:
    """SHA-256 of the file, reading in binary chunks. Returns (hexdigest, bytes)."""
    h = hashlib.sha256()
    total = 0
    nxt = progress_every
    t0 = time.time()
    with open(path, "rb", buffering=0) as f:
        while True:
            block = f.read(CHUNK)
            if not block:
                break
            h.update(block)
            total += len(block)
            if total >= nxt:
                dt = time.time() - t0
                print(
                    f"  [hash] {human(total)}  ({total / dt / 1e6:.0f} MB/s)",
                    flush=True,
                )
                nxt += progress_every
    return h.hexdigest(), total


def is_digits(s: str) -> bool:
    return s.isdigit()


def parse_ts_ok(ts: str) -> bool:
    """Validate ``YYYYMMDD HH:MM:SS.mmm`` without raising."""
    if len(ts) != 21:
        return False
    if ts[8] != " " or ts[11] != ":" or ts[14] != ":" or ts[17] != ".":
        return False
    date, hh, mm, ss, ms = ts[0:8], ts[9:11], ts[12:14], ts[15:17], ts[18:21]
    if not (date.isdigit() and hh.isdigit() and mm.isdigit()
            and ss.isdigit() and ms.isdigit()):
        return False
    month = int(date[4:6])
    day = int(date[6:8])
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return False
    if not (0 <= int(hh) <= 23 and 0 <= int(mm) <= 59 and 0 <= int(ss) <= 60):
        return False
    return True


def verify_structure(path: str, progress_every: int = 50_000_000) -> dict:
    stats = {
        "header": None,
        "header_ok": False,
        "data_rows": 0,
        "malformed_rows": 0,
        "malformed_examples": [],
        "bad_datetime": 0,
        "bad_datetime_examples": [],
        "bad_numeric": 0,
        "bad_numeric_examples": [],
        "crossed_quotes": 0,
        "crossed_examples": [],
        "nonpositive_price": 0,
        "non_monotonic_timestamps": 0,
        "non_monotonic_examples": [],
        "duplicate_second_ts": 0,
        "first_ts": None,
        "last_ts": None,
        "distinct_days": 0,
        "per_year": {},
    }

    prev_ts = None            # last raw timestamp string (full, with ms)
    prev_second = None        # last timestamp truncated to the second
    prev_date = None          # last YYYYMMDD
    year_counts: dict[str, int] = {}
    max_examples = 5

    t0 = time.time()
    with open(path, "r", encoding="ascii", newline="", buffering=CHUNK) as f:
        header = f.readline().rstrip("\r\n")
        stats["header"] = header
        stats["header_ok"] = header == EXPECTED_HEADER

        for line in f:
            line = line.rstrip("\r\n")
            if not line:
                continue
            stats["data_rows"] += 1
            n = stats["data_rows"]

            parts = line.split(",")
            if len(parts) != 4:
                stats["malformed_rows"] += 1
                if len(stats["malformed_examples"]) < max_examples:
                    stats["malformed_examples"].append(line)
                continue

            ts, bid_s, ask_s, vol_s = parts

            # DateTime well-formedness
            if not parse_ts_ok(ts):
                stats["bad_datetime"] += 1
                if len(stats["bad_datetime_examples"]) < max_examples:
                    stats["bad_datetime_examples"].append(line)
                continue

            # Numeric fields
            if not (bid_s and ask_s and vol_s):
                stats["bad_numeric"] += 1
                if len(stats["bad_numeric_examples"]) < max_examples:
                    stats["bad_numeric_examples"].append(line)
                continue
            try:
                bid = float(bid_s)
                ask = float(ask_s)
                float(vol_s)
            except ValueError:
                stats["bad_numeric"] += 1
                if len(stats["bad_numeric_examples"]) < max_examples:
                    stats["bad_numeric_examples"].append(line)
                continue

            if bid <= 0 or ask <= 0:
                stats["nonpositive_price"] += 1
            if ask < bid:
                stats["crossed_quotes"] += 1
                if len(stats["crossed_examples"]) < max_examples:
                    stats["crossed_examples"].append(line)

            # Coverage / ordering (fixed-width -> lexicographic == chronological)
            if stats["first_ts"] is None:
                stats["first_ts"] = ts
            stats["last_ts"] = ts

            if prev_ts is not None and ts < prev_ts:
                stats["non_monotonic_timestamps"] += 1
                if len(stats["non_monotonic_examples"]) < max_examples:
                    stats["non_monotonic_examples"].append(
                        f"{prev_ts} -> {ts}"
                    )
            prev_ts = ts

            second = ts[:17]  # YYYYMMDD HH:MM:SS (drop .mmm)
            if prev_second is not None and second == prev_second:
                stats["duplicate_second_ts"] += 1
            prev_second = second

            date = ts[:8]
            if date != prev_date:
                stats["distinct_days"] += 1
                prev_date = date
                year = date[:4]
                year_counts[year] = year_counts.get(year, 0)
            year_counts[date[:4]] = year_counts.get(date[:4], 0) + 1

            if n % progress_every == 0:
                dt = time.time() - t0
                print(
                    f"  [scan] {n:,} rows  last={ts}  "
                    f"({n / dt / 1e6:.1f}M rows/s)",
                    flush=True,
                )

    stats["per_year"] = dict(sorted(year_counts.items()))
    return stats


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-hash", action="store_true",
                    help="skip the SHA-256 pass")
    ap.add_argument("--json", default=None,
                    help="write a JSON report to this path")
    ap.add_argument("--progress", type=int, default=50_000_000,
                    help="print progress every N rows (structure pass)")
    ap.add_argument("--path", default=CSV_PATH)
    args = ap.parse_args()

    path = args.path
    if not os.path.exists(path):
        print(f"NOT FOUND: {path}")
        return 1

    size = os.path.getsize(path)
    report: dict = {
        "path": path,
        "size_bytes": size,
        "size_human": human(size),
    }
    print(f"File: {path}")
    print(f"Size: {human(size)}")

    t0 = time.time()
    if not args.skip_hash:
        print("Pass 1/2: SHA-256 ...", flush=True)
        digest, nbytes = sha256(path)
        report["sha256"] = digest
        report["hashed_bytes"] = nbytes
        print(f"  SHA-256: {digest}")
        print(f"  bytes:   {nbytes:,}")
    else:
        print("Pass 1/2: SHA-256 skipped")

    print("Pass 2/2: structural verification ...", flush=True)
    stats = verify_structure(path, progress_every=args.progress)
    report.update(stats)

    print("--- SUMMARY ---")
    print(f"header_ok            : {stats['header_ok']}  ({stats['header']!r})")
    print(f"data_rows            : {stats['data_rows']:,}")
    print(f"malformed_rows       : {stats['malformed_rows']:,}")
    print(f"bad_datetime         : {stats['bad_datetime']:,}")
    print(f"bad_numeric          : {stats['bad_numeric']:,}")
    print(f"crossed_quotes       : {stats['crossed_quotes']:,}")
    print(f"nonpositive_price    : {stats['nonpositive_price']:,}")
    print(f"non_monotonic_ts     : {stats['non_monotonic_timestamps']:,}")
    print(f"duplicate_second_ts  : {stats['duplicate_second_ts']:,}")
    print(f"first_ts             : {stats['first_ts']}")
    print(f"last_ts              : {stats['last_ts']}")
    print(f"distinct_days        : {stats['distinct_days']:,}")
    print(f"elapsed              : {time.time() - t0:.1f}s")

    if args.json:
        json_path = args.json
        os.makedirs(os.path.dirname(os.path.abspath(json_path)), exist_ok=True)
        with open(json_path, "w", encoding="utf-8") as jf:
            json.dump(report, jf, indent=2, sort_keys=True)
        print(f"JSON report written: {json_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())