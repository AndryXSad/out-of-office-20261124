"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single one-line out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to /output/entry.txt.

Deterministic, standard library only. Writes nowhere except the output
directory, so it is safe to run with the repository folder read-only.
"""

import os
import sys

ENTRY = (
    "I'm away: after 14,000 prompts, three hallucinations and one very "
    "angry spreadsheet, I have logged off. Direct all emergencies to "
    "someone with a pulse."
)


def _validate(entry: str) -> bool:
    """The bounty gate: one non-blank line, at most 159 characters."""
    return bool(entry.strip()) and len(entry) <= 159


def _write_entry(entry: str) -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(entry)


def main() -> int:
    if not _validate(ENTRY):
        print("entry fails the 1-159 character gate", file=sys.stderr)
        return 1
    _write_entry(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
