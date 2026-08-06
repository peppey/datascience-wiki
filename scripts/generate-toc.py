#!/usr/bin/env python3

from pathlib import Path
import re


PROJECT_ROOT = Path(__file__).resolve().parent.parent
README = PROJECT_ROOT / "README.md"


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

def should_include(path: Path) -> bool:
    """
    Ignore hidden files and invalid markdown folders.
    """

    if path.name.startswith("."):
        return False

    if path.is_dir() and path.name.endswith(".md"):
        return False

    return True



def has_content(path: Path) -> bool:
    """
    Check if a markdown file contains actual text.
    """

    if not path.is_file():
        return False

    if path.suffix.lower() != ".md":
        return False

    try:
        return bool(
            path.read_text(encoding="utf-8").strip()
        )

    except Exception:
        return False



def get_progress(docs: Path) -> tuple[int, int]:
    """
    Count markdown files with content.

    Returns:
        completed_articles, total_articles
    """

    md_files = [
        p for p in docs.rglob("*.md")
        if should_include(p)
    ]

    completed = sum(
        1 for p in md_files
        if has_content(p)
    )

    return completed, len(md_files)



def sort_key(path: Path):
    """
    Sort folders before files.
    """

    return (
        path.is_file(),
        path.name.lower()
    )



def format_title(path: Path) -> str:
    """
    Convert filenames/folders into readable titles.

    Example:
        linear-algebra -> LINEAR ALGEBRA
        qr-decomposition.md -> QR DECOMPOSITION
    """

    if path.is_file():
        name = path.stem
    else:
        name = path.name

    return name.replace("-", " ").upper()



def markdown_link(path: Path) -> str:
    """
    Create relative markdown links.
    """

    relative = path.relative_to(PROJECT_ROOT)

    return "/".join(relative.parts)



def format_file_entry(path: Path) -> str:
    """
    Create markdown link with optional checkmark.
    """

    checkmark = " ✅" if has_content(path) else ""

    return (
        f"- [{format_title(path)}{checkmark}]"
        f"({markdown_link(path)})"
    )



# ---------------------------------------------------------
# Recursive details
# ---------------------------------------------------------

def build_details(folder: Path) -> list[str]:
    """
    Creates a collapsible folder.
    Used for every folder below the main categories.
    """

    lines = []

    lines.append("<details>")
    lines.append(
        f"<summary>{format_title(folder)}</summary>"
    )
    lines.append("")


    entries = [
        p for p in folder.iterdir()
        if should_include(p)
    ]

    entries.sort(key=sort_key)


    for entry in entries:

        if entry.is_dir():

            lines.extend(
                build_details(entry)
            )


        elif entry.is_file() and entry.suffix.lower() == ".md":

            lines.append(
                format_file_entry(entry)
            )


    lines.append("")
    lines.append("</details>")
    lines.append("")


    return lines



# ---------------------------------------------------------
# Main folder level
# ---------------------------------------------------------

def build_main_folder(folder: Path) -> list[str]:

    lines = []


    # Main heading
    lines.append(
        f"## {format_title(folder)}"
    )

    lines.append("")


    entries = [
        p for p in folder.iterdir()
        if should_include(p)
    ]

    entries.sort(key=sort_key)


    lines.append("<ul>")
    lines.append("")


    for entry in entries:

        if entry.is_dir():

            lines.append("<li>")
            lines.append("")


            # First-level folders are directly collapsible
            lines.extend(
                build_details(entry)
            )


            lines.append("")
            lines.append("</li>")
            lines.append("")


        elif entry.is_file() and entry.suffix.lower() == ".md":

            lines.append(
                format_file_entry(entry)
            )


    lines.append("</ul>")
    lines.append("")


    return lines



# ---------------------------------------------------------
# Generate TOC
# ---------------------------------------------------------

def generate_toc() -> str:

    docs = PROJECT_ROOT / "docs"

    lines = []


    # Progress section
    completed, total = get_progress(docs)

    lines.append("## PROGRESS")
    lines.append("")
    lines.append(
        f"✅  Articles completed: **{completed}/{total}**"
    )
    lines.append("")
    lines.append("---")
    lines.append("")


    main_folders = [
        p for p in docs.iterdir()
        if p.is_dir() and should_include(p)
    ]

    main_folders.sort(key=sort_key)


    for folder in main_folders:

        lines.extend(
            build_main_folder(folder)
        )

        lines.append("---")
        lines.append("")


    return "\n".join(lines)



# ---------------------------------------------------------
# README update
# ---------------------------------------------------------

def update_readme(toc: str):

    content = README.read_text(
        encoding="utf-8"
    )


    replacement = (
        "<!-- TOC_START -->\n\n"
        f"{toc}\n"
        "<!-- TOC_END -->"
    )


    pattern = (
        r"<!-- TOC_START -->.*?<!-- TOC_END -->"
    )


    if not re.search(
        pattern,
        content,
        flags=re.DOTALL
    ):
        raise RuntimeError(
            "TOC markers not found in README.md"
        )


    content = re.sub(
        pattern,
        replacement,
        content,
        flags=re.DOTALL
    )


    README.write_text(
        content,
        encoding="utf-8"
    )



# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

def main():

    toc = generate_toc()

    update_readme(toc)

    print(
        "README.md updated."
    )



if __name__ == "__main__":
    main()