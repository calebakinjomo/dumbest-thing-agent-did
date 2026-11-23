"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one line about the dumbest thing my agent did today to
$MAKEFUN_OUTPUT_DIR/entry.txt with a plain file write.

The dumbest thing: my agent spent forty minutes rewriting a script it had
already deleted, then asked me to review the diff of nothing — a diff with
nothing in it, because the file was already gone.
"""

import os

ENTRY = (
    "My agent spent forty minutes rewriting a script it had already deleted, "
    "then asked me to review the diff of nothing."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
