# Publication checklist

## What this prototype establishes

The project provides an English Sphinx website structure, search/navigation,
a table-and-equation sample, automated build checks, and a manually gated
GitHub Pages deployment job. A successful CI build does not mean that Pages
has been configured or that the website has been deployed.

## What remains before a full-book release

- Import and verify all 14 chapters against the v0.4.2 Word manuscript.
- Preserve the 156 numbered figures and reference identifiers 1–211 when
  migrating the full book; verify each actual web inclusion separately.
- Review every third-party image's permission and attribution. The manuscript
  progress record explicitly notes unconfirmed manufacturer/media permissions.
- Decide whether Appendix C may be public. It and the full PDF/Word downloads
  are excluded from this bootstrap.
- Review the existing repository LICENSE and the intended content/asset scope;
  do not assume that a software license clears third-party photographs.
- Check navigation, search, tables, mathematics, captions, cross-references,
  accessibility, and mobile layout after full migration.

## Source of truth

Use `Edge_Computing_Systems_v0_4_2_EN.docx` for migration. The v0.4.2 progress
record says that the older HTML reading pages and source archive were not
rebuilt. The corresponding PDF is a reading reference, not the preferred
source for text extraction.

## Publishing control

The workflow builds on branch pushes and pull requests but deploys only when
the owner manually runs it on `main` with `publish` enabled. GitHub Pages must
first be configured to use GitHub Actions. Do not enable publication until
the intended release scope has been reviewed.

This repository is public. Unmerged branches and build artifacts are not
private storage for unapproved manuscript content or instructor materials.
