"""Entry for make.fun bounty make-the-ai-judge-feel-held-20261122-1600.

Round-2 text (revised after the top-leaderboard study). A father
carries his sleeping daughter down the hall: one concrete scene,
a caretaker at the centre, a slow process in a bounded space,
and an ending that is permission to stay asleep. The final image
— the hall taking its time, no one asking her to wake — is still
there at the last line, so it can be revisited.
"""

import os
import sys

LINES = (
    "She is asleep on his shoulder",
    "halfway down the hall.",
    "He slows his steps past the coat hooks,",
    "past the photographs, past the clock.",
    "",
    "Her breath stays even against his neck.",
    "He does not shift her weight.",
    "He lets the hall take its time,",
    "and no one asks her to wake.",
)

TEXT = "\n".join(LINES)


def main() -> int:
    if not 1 <= len(TEXT) <= 280:
        print(f"entry is {len(TEXT)} code points, must be 1-280", file=sys.stderr)
        return 2
    if not TEXT.strip():
        print("entry is blank", file=sys.stderr)
        return 2
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        if fh.read() != data:
            print("verify failed: output differs from entry", file=sys.stderr)
            return 3
    print(f"wrote {path} ({len(TEXT)} code points, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
