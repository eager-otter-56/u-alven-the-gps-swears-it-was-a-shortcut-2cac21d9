#!/usr/bin/env python3
"""Entry for u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.

Writes the GPS's one-line excuse to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os

TEXT = (
    "The map said the lake was a road, the road was a driveway, "
    "and the driveway was a wedding \u2014 I took you to all three "
    "in the correct order."
)


def main() -> None:
    # Gate: 1-200 characters, single line, not only whitespace.
    assert 1 <= len(TEXT) <= 200, f"entry length {len(TEXT)} out of gate"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
