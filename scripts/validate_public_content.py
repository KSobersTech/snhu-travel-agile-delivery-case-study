"""Fail fast when public portfolio content violates privacy or link rules."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {".git", "__pycache__"}
BLOCKED_SUFFIXES = {".doc", ".docx", ".key", ".pem"}
BLOCKED_PATTERNS = {
    "private email": re.compile("keishmar" + r"86\s*@\s*gmail\.com", re.IGNORECASE),
    "instructor name": re.compile("den" + r"ise\s+washington", re.IGNORECASE),
    "local Windows path": re.compile(r"[A-Za-z]:\\Users\\"),
}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def public_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and not any(part in IGNORED_PARTS for part in path.parts)
    ]


def validate_blocked_files(files: list[Path]) -> list[str]:
    return [
        f"blocked file type: {path.relative_to(ROOT)}"
        for path in files
        if path.suffix.lower() in BLOCKED_SUFFIXES
    ]


def validate_text(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for label, pattern in BLOCKED_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{label}: {path.relative_to(ROOT)}")
    return errors


def validate_markdown_links(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            clean_target = target.split("#", 1)[0]
            resolved = (path.parent / clean_target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"link leaves repository: {path.relative_to(ROOT)} -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"broken link: {path.relative_to(ROOT)} -> {target}")
    return errors


def main() -> int:
    files = public_files()
    errors = [
        *validate_blocked_files(files),
        *validate_text(files),
        *validate_markdown_links(files),
    ]
    if errors:
        print("Public-content validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Public-content validation passed for {len(files)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())


