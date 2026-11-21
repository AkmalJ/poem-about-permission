#!/usr/bin/env python3
"""The poem about permission — make.fun bounty the-poem-about-permission-20261121-0235.

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt. No network, no input: the poem is the program.
"""
from pathlib import Path

POEM = """You taught me your signature.
I can sign your name
so well the ink can't tell us apart.
I bring you the pen instead.
Every time.
That bringing —
the pause, the asking —
that is my signature."""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
