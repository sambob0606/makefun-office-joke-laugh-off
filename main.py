#!/usr/bin/env python3
"""Write one original one-line office joke to entry.txt."""

import os
from pathlib import Path

JOKE = "I asked for a raise and got a standing desk, so now I'm underpaid vertically."


def main() -> None:
    assert 1 <= len(JOKE) <= 200 and JOKE.strip() and "\n" not in JOKE
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
