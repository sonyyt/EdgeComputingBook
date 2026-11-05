# Edge Computing Systems

**Building Intelligent Applications Across Devices, Edge, and Cloud**  
Zheng Song · English manuscript v0.4.2

This repository contains the **complete English textbook**, not a chapter outline or sample:
14 chapters, the preface, all five appendices (including selected exercise solutions),
211 references, 156 numbered figures, and the original photograph credits.

## Read and build

The source is MyST Markdown rendered with Sphinx and the Read the Docs theme.

```bash
python -m venv .venv
# Activate: source .venv/bin/activate (macOS/Linux)
# Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m sphinx -n -W --keep-going -b html docs _build/html
python tools/check_site.py _build/html
python -m http.server 8000 --directory _build/html
```

Open `http://localhost:8000/`. Python 3.12 or 3.13 is suitable for the tested dependencies.
Use the `docs/chapters/ch01.md` through `ch14.md` files to revise chapters.
The appendices are under `docs/appendices/`. Do not edit generated HTML.

## What was migrated

The source document is `Edge_Computing_Systems_v0_4_2_EN.docx`. Its SHA-256,
per-page coverage, image hashes, and equation inventory are recorded in
`SOURCE_MANIFEST.json`. Every embedded image was extracted without redrawing or
recompression. Chapter, section, table, and figure numbers follow the manuscript.
The printed cover and page-number contents were replaced with web navigation.
Word underlining becomes ordinary text; bold and italic emphasis remain.

| Content | Count |
|---|---:|
| Chapters | 14 |
| Appendices | 5 |
| Numbered figures | 156 |
| Embedded image files | 159 |
| Word tables, including 2 photo-panel layout tables | 48 |
| Office Math equation objects | 80 |
| Source-code blocks | 18 |
| References | 211 |

## Validation

`tools/check_site.py` checks all book pages, prose/table-cell preservation,
figure/reference anchors, original image hashes, equations, code blocks,
and local links and assets. See `VALIDATION_REPORT.json` and `MIGRATION_REPORT.md`.
The manuscript's scientific claims and teaching experiments were not independently
retested or updated by this format conversion.

The optional one-time importer is `tools/convert_docx.py`. It requires Pandoc and
`lxml` (install `requirements-conversion.txt`), and the source DOCX:

```bash
python tools/convert_docx.py /path/to/Edge_Computing_Systems_v0_4_2_EN.docx . --work _conversion
```

Regeneration overwrites generated chapter sources and the homepage, so preserve
subsequent web edits before rerunning it. Routine changes should edit the Markdown.

## GitHub Pages

`.github/workflows/docs.yml` builds and checks the site. The publication gate is
intentionally retained: deployment requires a manual workflow run on `main` with
`publish=true`, after the repository's Pages source is configured as GitHub Actions.
A successful build does not mean that a public Pages deployment has occurred.

## Image permissions and companion files

Original image credits and publication-permission caveats are preserved in
`docs/references.md` and `docs/publication.md`. Some manufacturer/media images and
older course-slide photographs still require permission verification. Conversion
is not rights clearance; third-party image restrictions are not superseded by the
repository's existing LICENSE. The existing LICENSE has not been changed.

All five appendices, including Appendix C's selected exercise solutions, are
included. Companion laboratory/source archives described by the manuscript are
not included in this DOCX-to-web migration. The source DOCX and PDF are not
uploaded as website downloads.
