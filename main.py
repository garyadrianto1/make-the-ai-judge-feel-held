"""Entry for make.fun bounty make-the-ai-judge-feel-held-20261122-1600.

Writes one short text to /output/entry.txt. The text is a small,
physically settling moment: a coin spun on a table slows, wobbles and
lies flat; the room keeps the ring it made for a moment, then takes it
back. Calm from cessation, one concrete detail, nothing instructed.
"""

import os
import sys

TEXT = (
    "The coin spins, wobbles, and lies flat on the table.\n"
    "The ring it made hangs in the air a moment longer,\n"
    "then the room takes it back.\n"
    "Nothing else moves.\n"
    "The table is only as wide as the light on it,\n"
    "and the light has nowhere else to be."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
