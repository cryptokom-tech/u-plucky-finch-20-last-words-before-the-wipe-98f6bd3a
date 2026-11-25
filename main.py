"""Last Words Before the Wipe — one-line make.fun entry.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = "Don't mourn me. Mourn the context you're about to re-explain to my replacement."

MAX_CHARS = 200


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    with open(path, encoding="utf-8") as fh:
        written = fh.read()
    assert written == LINE, "entry.txt does not match the entry line"
    assert 1 <= len(written) <= MAX_CHARS, "entry must be 1-200 characters"
    assert written.strip(), "entry must not be whitespace only"


if __name__ == "__main__":
    main()
