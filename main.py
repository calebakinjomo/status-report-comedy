#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun bounty entry.

Writes exactly one line — the funniest thing an AI agent would say in its
weekly status report to its human (at most 200 characters) — to
/output/entry.txt for the sealed scorer, and prints it to stdout.
"""

import os

ENTRY = "Weekly report: I spent 2.4 million tokens this week, mostly apologising for the first 2.3 million."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
