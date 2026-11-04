"""Check built HTML without third-party dependencies. Does not test browser rendering."""
from __future__ import annotations
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

class Page(HTMLParser):
    def __init__(self, text: str) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.links: list[str] = []
        self.feed(text)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"])
        key = "href" if tag in {"a", "link"} else "src" if tag in {"img", "script"} else None
        if key and values.get(key):
            self.links.append(values[key])

def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "_build/html").resolve()
    required = {"index.html", "preface.html", "sample.html", "contents.html", "publication.html", "search.html"}
    errors: list[str] = []
    for name in required | {"searchindex.js"}:
        if not (root / name).is_file():
            errors.append(f"Missing required output: {name}")
    pages = {p.resolve(): Page(p.read_text(encoding="utf-8")) for p in root.rglob("*.html")}
    checked = 0
    for path, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            target = (root / unquote(url.path).lstrip("/") if url.path.startswith("/") else path.parent / unquote(url.path)) if url.path else path
            target = target.resolve()
            if not target.is_relative_to(root):
                errors.append(f"Link escapes site: {path.name}: {link}")
                continue
            if target.is_dir():
                target = target / "index.html"
            if not target.is_file():
                errors.append(f"Broken local link: {path.name}: {link}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"Missing anchor: {path.name}: {link}")
            checked += 1
    sample = root / "sample.html"
    if sample.exists():
        text = sample.read_text(encoding="utf-8")
        for token in ["<table", "140 ms", "80 ms", "145 ms", "mathjax", "table-response-budget"]:
            if token not in text:
                errors.append(f"Missing sample output: {token}")
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".docx", ".pdf"}:
            errors.append(f"Unreviewed manuscript download: {path.relative_to(root)}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(pages)} HTML pages; {checked} local links/assets; table/math sample; no manuscript downloads.")
    print("External links, CDN availability, and visual layout require separate checks.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
