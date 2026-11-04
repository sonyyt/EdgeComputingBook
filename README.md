# Edge Computing Systems

*Building Intelligent Applications Across Devices, Edge, and Cloud*  
Zheng Song

## Status: Sphinx bootstrap, not the complete online book

This branch establishes the English website infrastructure for manuscript **v0.4.2**.
It contains the original preface, a clearly marked excerpt from section 1.6.1,
and a roadmap showing the complete chapter structure. It does **not** contain
the full textbook, photographs, instructor solutions, or downloadable manuscripts.
The existing repository `LICENSE` is preserved without modification.

### Build locally

Python 3.12 is recommended. From the repository root:

```bash
python -m venv .venv
# macOS / Linux:
source .venv/bin/activate
# Windows PowerShell instead:
# .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m sphinx -n -W --keep-going -b html docs _build/html
python tools/check_site.py _build/html
python -m http.server 8000 --directory _build/html
```

Open `http://localhost:8000/`. Stop the server with Ctrl+C.

### Automated validation and preview

The `Textbook website` workflow builds pushes to `main` and `sphinx-bootstrap`,
and pull requests targeting `main`. Warnings fail the build. The checker
validates local page/asset links, anchors, and the table/math sample.
The workflow uploads the built HTML as the `github-pages` artifact.

A successful build is **not** a website deployment. Normal pushes and pull
requests do not deploy this bootstrap.

### Publish only when approved

1. Review the pull request; merge only when the content is ready.
2. In repository **Settings > Pages**, set **Source** to **GitHub Actions**.
3. In **Actions > Textbook website > Run workflow**, select `main` and enable
   the `publish` input. Deployment is blocked for every other branch.
4. Confirm the deploy job succeeds before advertising the website.

The intended project-site URL is `https://sonyyt.github.io/EdgeComputingBook/`.
It is not evidence that a deployment already exists.

### Editing and migration

- `docs/index.md`: landing page and navigation.
- `docs/preface.md`: verbatim preface from v0.4.2.
- `docs/sample.md`: limited table/equation excerpt, not a complete chapter.
- `docs/contents.md`: manuscript outline and migration status.
- `docs/publication.md`: public-release checklist.
- `docs/conf.py`: Sphinx / MyST / Read the Docs theme configuration.
- `docs/_static/book.css`: responsive reading adjustments.
- `tools/check_site.py`: dependency-free HTML checks.
- `.github/workflows/docs.yml`: CI and explicitly requested Pages deployment.
- `SOURCE_MANIFEST.json`: manuscript fingerprint and extraction scope.

The v0.4.2 Word manuscript is authoritative for migration. The earlier HTML
and source archive were not rebuilt in v0.4.2. Keep instructor-only answers,
unreviewed photographs, credentials, and full source manuscripts out of this
public repository. A branch in a public repository is also public.

The public book's content licensing and third-party asset permissions must be
reviewed before full import; this bootstrap does not replace the owner's LICENSE
or grant rights to third-party materials. Dependencies retain their own licenses.
