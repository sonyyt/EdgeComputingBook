# English v0.4.2 complete-manuscript migration

## Scope

Converted the supplied English v0.4.2 Word manuscript into editable MyST Markdown.
All 14 chapter bodies, all five appendices, the preface, 211 reference entries,
and original photo/product-image credits are included. This replaces the earlier
prototype. No substantive content rewrite or external fact refresh was performed.

## Checks executed

- Strict Sphinx HTML build: `python -m sphinx -n -W --keep-going -b html docs _build/html`.
- 25 generated HTML pages (21 manuscript content pages, homepage, publication note,
  generated index, and search).
- Rendered text checks: 2,329 nonempty prose/heading blocks and 851 table cells.
- Source Word and Pandoc body text agreed after removing whitespace and excluding
  equation objects, the printed cover/contents, and Part headings relocated to navigation.
- 159 image occurrences and 159 unique original image hashes matched.
- 156 unique figure anchors and 211 reference anchors matched the source inventory.
- 48 table objects, including two photo-panel layout tables; 80 Office Math objects;
  18 source-code blocks with preserved line breaks.
- 2,756 local link/asset checks passed, including target anchors.
- All 80 Office Math objects (76 distinct TeX expressions) rendered through MathJax's
  SVG output without reported formula errors.
- Browser structure checks on 21 reading/navigation pages at 1440px and 390px
  widths: 42 page/viewport cases; no broken images, reported MathJax errors,
  or horizontal page overflow. Selected chapter, table, and figure views were
  visually inspected.

## Browser-test boundary

The browser test used the generated Sphinx HTML with its actual local CSS/JavaScript
and images inlined through `set_content`. System fallback fonts were used; equations
were prerendered from the identical TeX using MathJax for the offline test.
The editing environment blocks browser navigation to file/HTTP URLs. Consequently,
this is not certification of live URL navigation, CDN requests, or live search behavior.
The search index and search page were generated, and local resource paths were checked.
No live Pages deployment is claimed by this report.

## Preserved limitations

Original photograph publication-permission caveats remain. The conversion does not
clear third-party rights, rerun course experiments, verify hardware/platform behavior,
or provide the companion laboratory archive. Word underlining is ordinary text in
the web edition. Manual source numbering was deliberately preserved.
