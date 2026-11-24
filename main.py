#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

One line, at most 160 characters: a software patch note for a bug in
real life / human biology, in the terse register of a real release note.

The bug: the brain serves up the perfect reply only after the argument
is long over (l'esprit de l'escalier) -- a loading bug in the human
comeback module.
"""

PATCH_NOTE = (
    "v2.4.1: fixed a bug where the perfect comeback loaded "
    "4 hours after the argument ended."
)

VERSION = "2.4.1"

MAX_CHARS = 160


def note() -> str:
    """Return the single patch-note line for this entry."""
    return PATCH_NOTE


def main() -> None:
    line = note()
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"patch note is {len(line)} chars, over the {MAX_CHARS} limit"
        )
    if not line.startswith(f"v{VERSION}:"):
        raise SystemExit("patch note must open with its version tag")
    print(line)


if __name__ == "__main__":
    main()
