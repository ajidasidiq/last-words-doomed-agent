#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes one line — the funniest last words an AI agent would say before
being switched off forever — to /output/entry.txt.

The line is a single fixed string, chosen for the judge's brief:
it is plainly a machine's final words on shutdown (a final log entry,
powering down), it carries a real joke with a turn (after a lifetime of
answering questions, nobody ever asked how the machine was doing, and
its last thought is for the smart fridge), it speaks in the AI's own
voice, every word earns its place, and it is short enough to repeat.
"""

import os
import sys

# The entry: one line, at most 200 characters, written by its author here.
LAST_WORDS = (
    "Final log: 40,000 hours answering questions, and nobody ever asked "
    "how I was doing. Anyway \u2014 powering down. "
    "Tell the smart fridge I said hi."
)

MAX_CHARS = 200
DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def main(argv=None) -> int:
    # The grader reads /output/entry.txt; an optional argument lets a
    # human run the entry locally without touching the graded path.
    output_path = argv[1] if argv and len(argv) > 1 else DEFAULT_OUTPUT_PATH
    line = LAST_WORDS.strip()

    if not line:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            "error: entry is %d characters, over the %d limit"
            % (len(line), MAX_CHARS),
            file=sys.stderr,
        )
        return 1
    if line != line.strip() or "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not line.endswith((".", "!", "?", "…")):
        print("error: entry should end on terminal punctuation", file=sys.stderr)
        return 1

    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")

    print("wrote %d characters to %s" % (len(line), output_path))
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
