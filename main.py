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


def main() -> int:
    if not ENTRY.strip() or len(ENTRY) > 159:
        print("entry fails the 1-159 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
