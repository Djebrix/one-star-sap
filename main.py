#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to $ENTRY_OUTPUT_DIR/entry.txt
(default /output). Stdlib only, no network, fully deterministic.
"""

import os

LINE = (
    "One star. He waters me like he's apologising for a murder, "
    "then stashes me in the dark corner like I'm the evidence. "
    "I wrote this in sap, so you know I mean it."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
