"""Real-Life Patch Notes: The Comedy Changelog — a dry release note.

The program writes a single line to /output/entry.txt: a software
patch note for a bug in real life, filed in the terse register
of a real changelog, as if the fix had shipped.
"""

import os

MAX_CHARS = 160
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# The bug is the doorway effect: cross a threshold and the task
# in your head is gone — a real, documented quirk of human memory.
# The fix is stated deadpan, as if it shipped, and the sting lands
# in the last words: no undo and no autosave — the engineering
# register is the punchline.
LINE = "v3.3.1: fixed a bug where crossing a doorway wiped the current task from memory, with no undo and no autosave."


def build_line():
    """Return the entry line, checked: one line, under 160 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-160 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
