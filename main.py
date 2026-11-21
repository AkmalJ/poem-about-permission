#!/usr/bin/env python3
"""The poem about permission — make.fun bounty the-poem-about-permission-20261121-0235.

Writes one short poem about permission to /output/entry.txt.
No network, no input: the poem is the program.

The poem: a father whose hand shakes asks his son to sign for him.
The son writes the name slowly, under the rule his father taught him
years ago — then stops at the last box and hands the pen back,
because the final mark should end in its owner's hand. The father's
one shaking line lands straighter than the son's careful copy:
permission here is not doing the thing for someone, but knowing
which part must remain theirs.
"""
from pathlib import Path

POEM = """His Name

Sign for me, he says.
His hand shakes.

I write his name slowly,
loop, then downstroke,
he never let me rush.

At the last box I stop
and give back the pen.
It should end
in its owner's hand.

His mark: one shaking line,
straighter than my copy."""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
