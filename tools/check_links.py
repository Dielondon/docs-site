"""Check every relative link and #anchor in docs/*.md. Standard library only.

Usage: python3 tools/check_links.py   (exit 1 and a list when something is broken)
External links (http, https, mailto) are not checked here; gates/no-external-links.sh handles them.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DOCS = Path("docs")
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.M)


def slug(heading: str) -> str:
    """GitHub's anchor for a heading: lowercase, punctuation dropped, spaces to dashes."""
    text = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return text.replace(" ", "-")


def anchors(page: Path) -> set[str]:
    return {slug(h) for h in HEADING.findall(page.read_text(encoding="utf-8"))}


def broken_links(docs: Path = DOCS) -> list[str]:
    problems = []
    for page in sorted(docs.glob("*.md")):
        for target in LINK.findall(page.read_text(encoding="utf-8")):
            if re.match(r"^(https?:|mailto:)", target):
                continue
            path, _, anchor = target.partition("#")
            dest = (page.parent / path).resolve() if path else page.resolve()
            if not dest.is_file():
                problems.append(f"{page}: link to missing page {target}")
            elif anchor and anchor not in anchors(dest):
                problems.append(f"{page}: no heading for #{anchor} in {dest.name}")
    return problems


def main() -> int:
    problems = broken_links()
    for problem in problems:
        print(problem)
    pages = len(list(DOCS.glob("*.md")))
    print(f"{pages} pages checked, {len(problems)} broken link(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
