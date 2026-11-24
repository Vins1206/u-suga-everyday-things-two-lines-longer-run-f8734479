"""Everyday Things, Two Lines -- toaster entry (program/v1, pure stdlib).

Writes exactly two lines to /output/entry.txt (UTF-8, under 400 chars):
  Line 1 -- one vivid sentence explaining a toaster to a 10-year-old,
            built on a single analogy (a tiny lift for bread).
  Line 2 -- one sentence on why the analogy works: what it maps
            (down, hot, pop back up) and what it leaves out
            (the glowing wires, and that browning is burning starting).

Deterministic: the text is a fixed constant; no input, no randomness,
no network, no clock. Two runs produce byte-identical output.
"""

import os

ENTRY = (
    "A toaster is a tiny lift that carries your bread down into a hot "
    "little room, turns it brown, and brings it straight back up.\n"
    "The lift shows the bread going down, getting hot, and popping back "
    "up, but it leaves out the glowing electric wires that make the heat "
    "and the fact that brown toast is really bread just beginning to burn.\n"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 400, f"entry is {len(text)} chars, gate is 1-400"
    assert text.strip(), "entry must not be only whitespace"
    lines = text.rstrip("\n").split("\n")
    assert len(lines) == 2, f"entry must be exactly 2 lines, got {len(lines)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {OUTPUT_PATH} ({len(text)} chars, {len(lines)} lines)")


if __name__ == "__main__":
    main()
