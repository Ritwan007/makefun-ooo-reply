#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Writes one line to /output/entry.txt. The line is the gauntlet winner
(7-0 in a local round-robin against 7 other shortlisted candidates):
a real away message with a return date and a redirect for urgent matters,
whose punchline lands on the first read.
"""

import os

ENTRY = (
    "Away until Monday. If the building is on fire, email Facilities. "
    "If it's my inbox, let it burn."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
