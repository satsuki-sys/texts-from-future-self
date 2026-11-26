#!/usr/bin/env python3
"""Texts From Your Future Self — writes one funny text from your future self
to /output/entry.txt (1-200 characters, UTF-8)."""

import os

ENTRY = (
    "Future you here. That password you just changed? You'll forget it by "
    "Thursday, and the reset email goes to an inbox you deleted in 2021. "
    "Godspeed."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
