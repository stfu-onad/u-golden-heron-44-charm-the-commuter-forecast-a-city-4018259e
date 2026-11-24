#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City — make.fun entry.

Writes one original one-line weather forecast for a city that
does not exist to /output/entry.txt.
"""

LINE = (
    "In Drizzlewick, expect light rain from 4pm, umbrellas "
    "optional, ducks mandatory, and one very smug rainbow over "
    "the bus stop by six."
)


import os


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars"
    assert "\n" not in text, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
