"""Drop empty CSV rows. Blank lines are currently kept."""


def clean(text: str) -> str:
    kept = []
    for line in text.splitlines():
        kept.append(line)
    if not kept:
        return ""
    return "\n".join(kept) + "\n"


def main() -> None:
    import pathlib
    import sys

    path = pathlib.Path(sys.argv[1])
    path.write_text(clean(path.read_text(encoding="utf-8")), encoding="utf-8")


if __name__ == "__main__":
    main()
