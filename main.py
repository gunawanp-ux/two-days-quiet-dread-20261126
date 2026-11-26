#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one code review comment to /output/entry.txt: a single line of at
most 140 characters that approves a pull request while carrying quiet
existential dread.
"""

import os

ENTRY = (
    "LGTM. The tests pass, the types check, and nothing in this diff "
    "will outlive the heat death of the universe, probably."
)


def main() -> None:
    # Kit gate: entry line must be 1-140 characters.
    assert 1 <= len(ENTRY) <= 140, (
        f"entry line is {len(ENTRY)} characters, must be 1-140"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
