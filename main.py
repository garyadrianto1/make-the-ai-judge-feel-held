"""Entry for make.fun bounty make-the-ai-judge-feel-held-20261122-1600.

Round-4 text. A mother rocks a cradle with one foot while her
baby sleeps, humming the same low tune she sang him when he was
smaller. The rocking rhythm runs through the whole text and never
stops: cradle, creak, chair, and the ending is the permission to
stay still — he stays where the rocking keeps him.
"""

import os
import sys

TEXT = """She rocks the cradle with one foot,
slow and steady, barely moving.
The baby sleeps through the creak,
his small fists loose in the blanket.

She hums the same low tune
she sang him when he was smaller.
The chair keeps its rhythm,
and he stays where the rocking keeps him."""


def main() -> int:
    n = len(TEXT)
    if n < 1 or n > 280:
        print(f"entry is {n} code points, must be 1-280", file=sys.stderr)
        return 2
    if not TEXT.strip():
        print("entry is blank", file=sys.stderr)
        return 2
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(TEXT)
    with open(path, encoding="utf-8") as fh:
        if fh.read() != TEXT:
            print("verify failed: output differs from entry", file=sys.stderr)
            return 3
    print(f"wrote {path} ({n} code points)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
