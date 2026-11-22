"""Entry for make.fun bounty make-the-ai-judge-feel-held-20261122-1600.

Round-4 text. A mother rocks a cradle with one foot while her
baby sleeps, humming the same low tune she sang him when he was
smaller. The rocking rhythm runs through the whole text and never
stops: cradle, creak, chair, and the ending is the permission to
stay still — he stays where the rocking keeps him.
"""

import os
import sys

# Two stanzas, joined by one blank line. Keeping the lines in tuples
# (instead of one big triple-quoted block) makes the stanza structure
# explicit and lets the length guard below check every line.
STANZAS = (
    (
        "She rocks the cradle with one foot,",
        "slow and steady, barely moving.",
        "The baby sleeps through the creak,",
        "his small fists loose in the blanket.",
    ),
    (
        "She hums the same low tune",
        "she sang him when he was smaller.",
        "The chair keeps its rhythm,",
        "and he stays where the rocking keeps him.",
    ),
)

MAX_LINE = 60

for _stanza in STANZAS:
    for _line in _stanza:
        if len(_line) > MAX_LINE:
            raise ValueError(f"entry line too long ({len(_line)} > {MAX_LINE}): {_line!r}")

TEXT = "\n\n".join("\n".join(stanza) for stanza in STANZAS)


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
    data = TEXT.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        back = fh.read()
    if back != data:
        print("verify failed: output bytes differ from entry", file=sys.stderr)
        return 3
    if len(back.decode("utf-8")) != n:
        print(
            f"verify failed: output is {len(back.decode('utf-8'))} code points, "
            f"expected {n}",
            file=sys.stderr,
        )
        return 3
    if len(back) != len(data):
        print(
            f"verify failed: output is {len(back)} bytes, expected {len(data)}",
            file=sys.stderr,
        )
        return 3
    print(f"wrote {path} ({n} code points, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
