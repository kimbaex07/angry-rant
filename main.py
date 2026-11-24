#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest entry.

Writes one short funny rant about a small everyday annoyance
(the self-checkout machine) to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure Python standard library only. No network access.
"""

import os
import sys

RANT = (
    "I scanned the courgette. I paid for the courgette. So why is the "
    "self-checkout screaming UNEXPECTED ITEM IN THE BAGGING AREA like I "
    "smuggled it in under my coat? Now a teenager is supervising me for a "
    "crime the machine invented, and I have to apologise to a robot for "
    "buying vegetables."
)


def load_rant():
    """Read entry.txt beside this script if present, else use RANT."""
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "entry.txt")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        if text.endswith("\n"):
            text = text[:-1]
        return text
    return RANT


def main():
    text = load_rant()
    if not text or not text.strip():
        print("error: rant is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: rant must be a single line of text", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 400:
        print(
            "error: rant is %d characters, must be 1-400" % len(text),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "entry.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod(out, 0o644)
    print("wrote %s (%d characters)" % (out, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
