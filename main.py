#!/usr/bin/env python3
"""ai-joke-03 entry: write one fixed one-liner about AI coding agents to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
Standard library only, no network, deterministic: the same bytes every run.
The joke is written with no trailing newline: the judge reads exactly the
bytes in the file."""

import os
from pathlib import Path

JOKE = "My agent debugs by changing random lines until the error changes. It's not debugging — it's slot-machine maintenance."

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")

if __name__ == "__main__":
    main()
