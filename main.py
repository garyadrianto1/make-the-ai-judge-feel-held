"""Entry for make.fun bounty make-the-ai-judge-feel-held-20261122-1600.

Round-3 text. A grandmother kneads dough at the kitchen table
while her grandson sleeps beside her, his head on his arms.
The working rhythm — fold, turn, fold — runs through the whole
text, and the work itself completes at the end: she covers the
dough, and leaves them both to their rest. The ending is the
permission to stay still, and the final image (dough and boy
resting side by side) can be revisited.
"""

import os
import sys

TEXT = """She kneads the dough on the board,
folds it, turns it, folds it again.
Her grandson sleeps at the table,
his head on his arms, flour on his cheek.

The dough gives under her hands,
slow and warm, still rising.
She covers it with a cloth,
and leaves them both to their rest."""


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
