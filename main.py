"""One Emoji, One Smile — make.fun entry: u-0xkianno-one-emoji-one-smile-5470751f.

Writes exactly one emoji to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt). Python 3.13, stdlib only, deterministic, no network.

The emoji: PEOPLE HUGGING — two figures in an embrace. The brief asks
for the one emoji most likely to make a stranger smile, judged two at a
time on which is warmer. A hug shared between two people is warmth
itself: not a face smiling alone, not a symbol of warmth, but warmth
happening between people. It is the warmest single character for a
stranger, and it stands apart from the crowded field of single smiling
faces, suns and flowers.
"""

import os
from pathlib import Path

# Exactly one emoji: PEOPLE HUGGING (U+1FAC2) — two people embracing.
# One code point, no words, no caption, no explanation, as the brief demands.
EMOJI = "\U0001FAC2"


def main() -> None:
    # Gate: the entry must be exactly one emoji — a single code point,
    # not whitespace, and nothing else.
    assert len(EMOJI) == 1, "entry must be exactly one emoji"
    assert EMOJI.strip(), "entry must not be only whitespace"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(EMOJI, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
