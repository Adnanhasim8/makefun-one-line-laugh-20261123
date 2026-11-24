#!/usr/bin/env python3
"""The One-Line Laugh — make.fun entry.

Writes a single funny line (one sentence, at most 200 characters)
to /output/entry.txt. Python 3.13 standard library only, no network.
"""

import os

ENTRY = "The Wi-Fi died for ten minutes, and my family had to look at each other like strangers at a bus stop."


def main() -> None:
    # Gate: one line, 1-200 characters, not only whitespace.
    assert ENTRY, "entry must be non-empty"
    assert ENTRY.strip() == ENTRY, "entry must not have leading/trailing whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
