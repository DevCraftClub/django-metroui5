"""Проверка, что каждая страница документации закрыта кодом или списком."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = Path("/home/maxim/Dev/GIT/metroui-docs/src/content/docs/components")
EXAMPLES = Path("/home/maxim/Dev/GIT/metroui/examples")
COMPONENTS = ROOT / "metroui5" / "components"
GAPS = ROOT / "COMPONENT_GAPS.md"

ALIASES = {
    "badges": "badge",
    "cards": "card",
    "breadcrumbs": "breadcrumb",
    "buttons": "button",
    "lists": "list",
    "shortcuts": "shortcut",
    "dropmenu": "drop-menu",
    "input-material": "material-input",
    "material-tabs": "tabs-material",
    "time-picker": "timepicker",
}

GUIDES = {
    "any",
    "code",
    "color-palette",
    "colors",
    "gradients",
    "h-tag",
    "i18n",
    "icons",
    "jquery",
    "load-metro",
    "log",
    "model",
    "multicolor-gradients",
    "patterns",
    "quick-start",
    "shapes",
    "splashscreen",
    "stroke-color",
    "touch",
    "typography",
}


def implemented_slugs() -> set[str]:
    slugs: set[str] = set()
    for path in COMPONENTS.glob("*.py"):
        if path.stem in {"__init__", "base"}:
            continue
        slugs.add(path.stem.replace("_", "-"))
        text = path.read_text(encoding="utf-8")
        for match in re.finditer(r"^def render_([a-z0-9_]+)", text, re.M):
            slugs.add(match.group(1).replace("_", "-"))
    return slugs


def canon(slug: str) -> str:
    return ALIASES.get(slug, slug)


def is_covered(slug: str, implemented: set[str]) -> bool:
    target = canon(slug)
    return slug in implemented or target in implemented


def gap_rows() -> dict[str, str]:
    rows: dict[str, str] = {}
    for line in GAPS.read_text(encoding="utf-8").splitlines():
        if not line.startswith("- "):
            continue
        left, status, _note = (part.strip() for part in line[2:].split("|"))
        rows[left] = status
    return rows


def known_names(implemented: set[str]) -> set[str]:
    return {path.stem for path in DOCS.glob("*.mdx")} | implemented


def is_variant(stem: str, known: set[str], implemented: set[str]) -> bool:
    mapped = canon(stem)
    if mapped in known or is_covered(mapped, implemented):
        return True
    for base in sorted(known, key=len, reverse=True):
        if len(base) < 3:
            continue
        if stem.startswith(base + "-") or stem.startswith(base) and stem[len(base):].isdigit():
            return True
    return False


def example_only_slugs(implemented: set[str]) -> list[str]:
    known = known_names(implemented)
    found: list[str] = []
    seen: set[str] = set()
    for path in sorted(EXAMPLES.glob("*.html")):
        if is_variant(path.stem, known, implemented):
            continue
        mapped = canon(path.stem)
        if mapped in seen:
            continue
        seen.add(mapped)
        found.append(mapped)
    return found


def test_every_doc_page_is_closed() -> None:
    implemented = implemented_slugs()
    rows = gap_rows()
    missing = [
        path.stem
        for path in sorted(DOCS.glob("*.mdx"))
        if not is_covered(path.stem, implemented) and path.stem not in rows
    ]
    assert missing == []


def test_example_only_names_are_listed() -> None:
    implemented = implemented_slugs()
    rows = gap_rows()
    missing = [
        slug
        for slug in example_only_slugs(implemented)
        if not is_covered(slug, implemented) and slug not in rows
    ]
    assert missing == []


def test_gap_statuses_are_known() -> None:
    allowed = {"дописать", "не компонент", "спор", "ломающая"}
    unknown = sorted(status for status in gap_rows().values() if status not in allowed)
    assert unknown == []
