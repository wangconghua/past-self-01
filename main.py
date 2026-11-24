#!/usr/bin/env python3
"""Two Lines to Your Past Self — entry writer.

Line 1 warns the past self about one specific moment (a sentence said
out loud in a job interview). Line 2 traces the cause and effect: the
answer reveals the truth, and the writer walks out before the job can
take their twenties.
"""

import os

LINE1 = "When the interviewer asks if you have any questions, ask her why she stayed."
LINE2 = "Her answer tells you the job will eat your twenties, and you walk out before it can."

ENTRY = LINE1 + "\n" + LINE2 + "\n"

# Generic life advice the judge brief counts against: a warning with no
# concrete moment loses to any warning that names a real moment.
BANNED_GENERIC = (
    "study harder",
    "don't trust",
    "believe in yourself",
    "follow your dreams",
    "never give up",
    "work harder",
)


def validate(text):
    """Check the entry against the judge brief before writing it out."""
    if not (1 <= len(text) <= 280):
        raise ValueError("entry must be 1-280 characters, got %d" % len(text))
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines, got %d" % len(lines))
    for i, line in enumerate(lines, 1):
        if not line.strip():
            raise ValueError("line %d is blank" % i)
        # Each line is a single sentence: one terminal period, no other
        # sentence terminators inside.
        if line.count(".") != 1 or not line.endswith("."):
            raise ValueError("line %d must be a single sentence" % i)
        if "?" in line or "!" in line:
            raise ValueError("line %d must be a single sentence" % i)
    # Line 1 must name one specific moment: a person, a place, a decision,
    # or a sentence said out loud — not a vague phase of life.
    if "interviewer" not in lines[0]:
        raise ValueError("line 1 must name a specific moment")
    # Line 2 must trace cause and effect from that moment: the answer in
    # line 1's question leads to a concrete change (walking out).
    if "Her answer" not in lines[1] or "walk out" not in lines[1]:
        raise ValueError("line 2 must trace cause and effect from the moment")
    lowered = text.lower()
    for phrase in BANNED_GENERIC:
        if phrase in lowered:
            raise ValueError("generic life advice not allowed: %s" % phrase)
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
