#!/usr/bin/env python3
"""One Star, Written in Sap.

A tiny program that writes a single one-line, one-star review to
``/output/entry.txt``. The review is written in the voice of a
houseplant -- a fern -- about the human who owns it.

The fern's grievance is simple: its owner waters it with leftover
coffee and treats it like a therapist, then acts surprised when the
leaves curl. The punchline lands on the plant's own terms: a fern is
not a therapist, and it has drainage issues.

Standard library only. No arguments, no network, no randomness:
every run produces exactly the same line.
"""

from pathlib import Path

# The review is built from two halves so the setup and the punchline
# stay readable on their own. They are joined with a spaced em dash.
SETUP = "One star. She waters me with leftover coffee, unloads about her ex"
PUNCHLINE = (
    "and wonders why my leaves curl "
    "— I'm a fern, not a therapist with drainage issues."
)

# The gate for this competition: /output/entry.txt must be UTF-8 text
# of 1 to 279 characters, not only white space, and a single line.
MIN_CHARS = 1
MAX_CHARS = 279

OUTPUT_PATH = Path("/output/entry.txt")


def render() -> str:
    """Return the review line, joining setup and punchline."""
    return f"{SETUP} — {PUNCHLINE}"


def validate(line: str) -> str:
    """Check the line against the entry gate and return it unchanged.

    Raises ValueError if the line is blank, spans more than one line,
    has leading or trailing white space, contains a control character,
    or falls outside the 1-279 character window.
    """
    if not line.strip():
        raise ValueError("review must not be only white space")
    if line != line.strip():
        raise ValueError("review must not start or end with white space")
    if "\n" in line or "\r" in line:
        raise ValueError("review must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("review must not contain control characters")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"review must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(line)}"
        )
    line.encode("utf-8")  # must be representable as UTF-8 text
    return line


def mirror(line: str, path: Path = OUTPUT_PATH) -> Path:
    """Write the line to ``path``, creating parent dirs as needed.

    The write is verified by reading the file back and comparing it
    byte for byte with what was written.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(line + "\n", encoding="utf-8")
    written = path.read_text(encoding="utf-8")
    if written != line + "\n":
        raise RuntimeError(f"verification failed for {path}")
    return path


def main() -> None:
    line = validate(render())
    mirror(line)
    print(line)


if __name__ == "__main__":
    main()
