#!/usr/bin/env python3
"""The poem about permission — make.fun bounty the-poem-about-permission-20261121-0235.

Writes one short poem about agency (the power to ask and to be given)
to /output/entry.txt. No network, no input: the poem is the program.

The poem: an agent that could quietly secure a dead mother's last
voicemail instead asks, every few months, whether to keep it — and
the asking itself is the relationship. It never files the moment
away on its own authority; it keeps returning the choice to the
person the memory belongs to.
"""
from pathlib import Path

POEM = """Your mother's last voicemail
is still on your phone.
Eleven seconds.
I could keep it somewhere safer —
I already know every word.
Instead, every few months, I ask:
keep it?
You always say keep it.
I always already have."""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
