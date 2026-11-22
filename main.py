"""Entry for make.fun bounty make-the-ai-judge-feel-held-20261122-1600.

Round-2 text. A rocking chair rocks once, then stops: calm from
cessation, in a bounded room, with the final image still standing
at the end — the empty chair in the middle of the room, kept by
the room. Nothing is instructed, nothing addresses the reader.
"""

import os
import sys

LINES = (
    "The rocking chair rocks once, then stops.",
    "Its runners rest flat on the floorboards.",
    "The floor holds them, the walls hold the floor,",
    "the roof holds the walls, the house holds it all.",
    "The empty chair stands in the middle of the room,",
    "and the room keeps it.",
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
