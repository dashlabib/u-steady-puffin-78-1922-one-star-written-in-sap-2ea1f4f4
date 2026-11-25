#!/usr/bin/env python3
"""One Star, Written in Sap entry.

This program does exactly one small thing: it prints a single original
one-line, one-star review, written in the voice of a houseplant about
the human who owns it, and mirrors that same line into
/output/entry.txt so the stored entry file always matches the program's
own output byte for byte.

The review is a setup with a surprise turn — a fern whose owner waters
it with leftover coffee and treats it as a therapist, then blames the
plant when its leaves curl — kept well inside the kit's 279-character
cap. No stock phrases, no drama-queen wilting: just one sharp,
plant's-eye grievance with a reason for the single star.

Standard library only. No arguments, no network, no randomness, no
side effects beyond the one output file.
"""

import os
import sys

SETUP = "One star. She waters me with leftover coffee, unloads about her ex"
PUNCHLINE = "and wonders why my leaves curl — I'm a fern, not a therapist with drainage issues."

# The review is held as setup + punchline and joined with an em dash, so
# the line is assembled from its two beats rather than stored as one blob.
REVIEW = SETUP + " — " + PUNCHLINE

# The kit's gate: /output/entry.txt must be UTF-8 text of 1 to 279
# characters, not only white space. Enforce it here so an over-long
# review can never slip through to the entry file.
MAX_CHARS = 279

OUTPUT_PATH = "/output/entry.txt"


def render() -> str:
    """Return the full review line, terminated by a single newline."""
    if not 1 <= len(REVIEW) <= MAX_CHARS:
        raise ValueError(
            "review must be 1 to 279 characters, got %d" % len(REVIEW)
        )
    if not REVIEW.strip():
        raise ValueError("review must not be only white space")
    if "\n" in REVIEW or "\r" in REVIEW:
        raise ValueError("review must be a single line")
    REVIEW.encode("utf-8")  # the gate reads UTF-8; fail here, not on the server
    return REVIEW + "\n"


def mirror(text: str) -> None:
    """Write the line to the entry file and verify the write landed intact."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != text:
            raise IOError("entry file does not match printed output")


def main() -> int:
    """Print the review line and mirror it to the entry file."""
    text = render()
    sys.stdout.write(text)
    sys.stdout.flush()
    mirror(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
