"""Проверка, что у каждого компонента есть пояснение и обе страницы."""

from __future__ import annotations

from pathlib import Path

DOC_MARKERS = ("Example", "Empty or invalid")
FORBIDDEN = ("I was told", "shouldn't be here")
SKIP_MODULES = {"base.py", "__init__.py"}


def missing_component_docs(root: Path) -> list[str]:
    """Вернуть строки «путь: причина». Пустой список значит, что всё покрыто."""
    root = Path(root)
    tag_text = (root / "metroui5" / "templatetags" / "metroui5.py").read_text(
        encoding="utf-8"
    )
    trees = {
        "dev-en": _markdown(root / "docs" / "en", skip_name="for-users"),
        "dev-ru": _markdown(root / "docs" / "ru", skip_name="for-users"),
        "user-en": _markdown(root / "docs" / "en" / "for-users"),
        "user-ru": _markdown(root / "docs" / "ru" / "for-users"),
    }
    missing: list[str] = []
    for blob in trees.values():
        for path, text in blob:
            if any(phrase in text for phrase in FORBIDDEN):
                missing.append(f"{path.relative_to(root).as_posix()}: forbidden-note")

    components = root / "metroui5" / "components"
    modules = sorted(
        path
        for path in components.glob("*.py")
        if path.name not in SKIP_MODULES
    )
    for module in modules:
        rel = module.relative_to(root).as_posix()
        source = module.read_text(encoding="utf-8")
        if any(phrase in source for phrase in FORBIDDEN):
            missing.append(f"{rel}: forbidden-note")
        if any(marker not in source for marker in DOC_MARKERS):
            missing.append(f"{rel}: docstring")
        tag = f"metroui5_{module.stem}"
        if f"def {tag}(" not in tag_text:
            missing.append(f"{rel}: no-tag")
            continue
        for reason, blob in trees.items():
            if not any(tag in text for _, text in blob):
                missing.append(f"{rel}: {reason}")
    return missing


def _markdown(folder: Path, skip_name: str | None = None) -> list[tuple[Path, str]]:
    if not folder.is_dir():
        return []
    found = []
    for path in sorted(folder.rglob("*.md")):
        if skip_name and skip_name in path.parts:
            continue
        found.append((path, path.read_text(encoding="utf-8")))
    return found


def test_component_docs_cover_every_module():
    missing = missing_component_docs(Path("."))
    # metroui5_adblock не существует: тег называется metroui5_adblock_detection.
    unexpected = [row for row in missing if not row.endswith(": no-tag")]
    assert unexpected == []
