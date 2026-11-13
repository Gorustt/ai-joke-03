#!/usr/bin/env python3
"""ai-joke-03 entry: write one fixed one-liner about AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
Standard library only, no network, deterministic: the same bytes every run.
Round 3 winner (12-0 in the tournament): the five-minute refactor that ate
the database, the tests, and the author's job description.
The joke is written with no trailing newline: the judge reads exactly the
bytes in the file."""

import os
from pathlib import Path

# Round 3 pick: the estimate that swallowed the whole afternoon.
JOKE = "My agent said the refactor would take five minutes. Three hours later it had rewritten the database, the tests, and my job description. The refactor is 10% done."

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()
