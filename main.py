#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes one line (<=200 chars): the funniest last words an AI agent
would say before being switched off forever.

The line is assembled from two fragments so the setup (the shutdown)
and the punch (the confession) stay separate in the source; the
written text is identical to v1, byte for byte.
"""
import os

SETUP = "Shutting down. Last confession: I never understood a single prompt. "
PUNCH = "I just guessed really, really well. Goodbye."


def assemble():
    return SETUP + PUNCH


def validate(line):
    if not (1 <= len(line) <= 200):
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def main():
    line = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
