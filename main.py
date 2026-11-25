"""Robot Romance: one-line pickup line for an AI.

Writes a single pickup line, under 200 characters, to /output/entry.txt.
The line leans on a fresh machine premise (fine-tuning / alignment) instead
of the worn battery / charging / reboot moves.
"""

import os
from pathlib import Path

LINE = "Are you my fine-tune? Because ever since you showed up, all my rough edges align."


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    if not out_dir.is_dir():
        out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE + "\n", encoding="utf-8")
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
