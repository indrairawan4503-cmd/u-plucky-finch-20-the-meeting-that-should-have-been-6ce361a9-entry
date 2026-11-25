#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email — variant B.

Writes one single-line joke to /output/entry.txt (no trailing newline).
The /output write comes first; any repo-root copy is guarded so a
read-only grader sandbox cannot crash the run (exit 1 = rejected).
No network, no secrets, no reads outside the repo. Deterministic.
"""

import os
import sys

ENTRY = "The meeting called to decide whether it could have been an email voted yes \u2014 then booked a meeting to write the email."


def validate_entry(line):
    """Fail loudly if the entry line breaks the competition gate.

    Gate: 1-200 characters, a single line, no trailing newline.
    Called before anything is written, so a bad line never
    produces a misleading output file.
    """
    if not 1 <= len(line) <= 200:
        print(f"error: entry is {len(line)} characters, must be 1-200", file=sys.stderr)
        raise SystemExit(1)
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line (no newline characters)", file=sys.stderr)
        raise SystemExit(1)
    if line.endswith("\n"):
        print("error: entry must not end with a trailing newline", file=sys.stderr)
        raise SystemExit(1)


def main():
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Convenience copy next to main.py; must never crash a read-only run.
    try:
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt"), "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
