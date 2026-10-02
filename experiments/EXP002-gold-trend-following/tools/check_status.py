#!/usr/bin/env python3
"""Quick status check for the detached EXP002 verification run.

Prints:
  - whether the given PID is alive (best-effort)
  - whether the JSON report exists (and its size)
  - the tail of the verification log

Usage:
  python check_status.py [PID]
"""
from __future__ import annotations

import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DERIVED = os.path.abspath(os.path.join(HERE, os.pardir, "evidence", "derived"))
LOG = os.path.join(DERIVED, "verification.log")
ERR = os.path.join(DERIVED, "verification.err")
REPORT = os.path.join(DERIVED, "verification-report.json")


def pid_alive(pid: int) -> bool:
    if os.name == "nt":
        try:
            out = subprocess.run(
                ["tasklist", "/FI", f"PID eq {pid}"],
                capture_output=True, text=True, timeout=30,
            ).stdout
        except Exception as exc:  # pragma: no cover
            return f"ERROR: {exc}"  # type: ignore[return-value]
        return str(pid) in out
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def tail(path: str, n: int = 15) -> str:
    if not os.path.exists(path):
        return f"(missing: {path})"
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    return "".join(lines[-n:])


def main() -> int:
    pid = int(sys.argv[1]) if len(sys.argv) > 1 else None
    if pid is not None:
        print(f"pid {pid} alive: {pid_alive(pid)}")

    if os.path.exists(REPORT):
        print(f"report: EXISTS ({os.path.getsize(REPORT):,} bytes)")
    else:
        print("report: MISSING")

    print("--- log tail ---")
    print(tail(LOG), end="")
    if os.path.exists(ERR) and os.path.getsize(ERR) > 0:
        print("--- err tail ---")
        print(tail(ERR, 10), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())