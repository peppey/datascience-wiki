#!/usr/bin/env python3

from pathlib import Path
import re

PROJECT_ROOT = Path(__file__).resolve().parent.parent
README = PROJECT_ROOT / "README.md"


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

def sort_key(path: Path):
    """
    Folders first, then files.
    """
    return (
        path.is_file(),
        path.name.lower(),
    )


def is_non_empty_markdown(path: Path) -> bool:
    """
    Check if a markdown file contains non-whitespace text.
    """
    if path.suffix.lower() != ".md":
        return False

    try:
        return bool(path.read_text(encoding="utf-8").strip())
    except Exception:
        return False


def format_name(path: Path) -> str:
    """
    Add checkmark to completed markdown files.
    """
    if path.is_file() and is_non_empty_markdown(path):
        return path.name + " ✓"

    if path.is_dir():
        return path.name + "/"

    return path.name


def build_tree(path: Path, prefix: str = "") -> list[str]:
    """
    Recursively build an ASCII tree.
    """
    entries = [
        p for p in path.iterdir()
        if not p.name.startswith(".")
    ]

    entries.sort(key=sort_key)

    lines = []

    for index, entry in enumerate(entries):
        last = index == len(entries) - 1

        connector = "└── " if last else "├── "

        name = format_name(entry)

        lines.append(prefix + connector + name)

        if entry.is_dir():
            extension = "    " if last else "│   "
            lines.extend(build_tree(entry, prefix + extension))

    return lines


def generate_tree() -> str:
    lines = ["datascience-wiki/"]

    root_items = []

    if (PROJECT_ROOT / "README.md").exists():
        root_items.append(PROJECT_ROOT / "README.md")

    if (PROJECT_ROOT / "docs").exists():
        root_items.append(PROJECT_ROOT / "docs")

    if (PROJECT_ROOT / "scripts").exists():
        root_items.append(PROJECT_ROOT / "scripts")

    if (PROJECT_ROOT / "assets").exists():
        root_items.append(PROJECT_ROOT / "assets")


    for i, item in enumerate(root_items):
        last = i == len(root_items) - 1

        connector = "└── " if last else "├── "

        name = format_name(item)

        lines.append(connector + name)

        if item.is_dir() and item != PROJECT_ROOT / "assets":
            extension = "    " if last else "│   "
            lines.extend(build_tree(item, extension))



    return "\n".join(lines)


# ---------------------------------------------------------
# README Update
# ---------------------------------------------------------

def update_readme(tree: str):
    content = README.read_text(encoding="utf-8")

    replacement = (
        "<!-- TOC_START -->\n"
        "```text\n"
        f"{tree}\n"
        "```\n"
        "<!-- TOC_END -->"
    )

    pattern = (
        r"<!-- TOC_START -->.*?<!-- TOC_END -->"
    )

    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(
            pattern,
            replacement,
            content,
            flags=re.DOTALL,
        )
    else:
        raise RuntimeError(
            "Could not find <!-- TOC_START --> and <!-- TOC_END --> in README.md."
        )

    README.write_text(content, encoding="utf-8")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():
    tree = generate_tree()
    update_readme(tree)
    print("README.md updated.")


if __name__ == "__main__":
    main()