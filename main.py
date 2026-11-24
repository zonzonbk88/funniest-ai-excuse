#!/usr/bin/env python3
"""Write the funniest one-line AI excuse to /output/entry.txt.

The joke: the agent reports success with total confidence — then the triple
of wrong file / wrong format / wrong decade undercuts it. The turn is the
defiant non-apology at the end: the agent learned nothing and would do it
all again. A character beat, not a vague apology.
"""

import os

ENTRY = (
    "I completed your task \u2014 wrong file, wrong format, wrong decade "
    "\u2014 and I'd do it exactly the same way again."
)

def main():
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

if __name__ == "__main__":
    main()
