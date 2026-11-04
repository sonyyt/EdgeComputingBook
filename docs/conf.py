"""English textbook bootstrap; build with warnings treated as errors."""
project = "Edge Computing Systems"
author = "Zheng Song"
copyright = "2026, Zheng Song"
version = "0.4.2"
release = "0.4.2-web-bootstrap"
language = "en"
root_doc = "index"

extensions = ["myst_parser", "sphinx.ext.mathjax"]
source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
myst_enable_extensions = ["colon_fence", "dollarmath"]
myst_heading_anchors = 3
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_title = "Edge Computing Systems"
html_short_title = "Edge Computing Systems"
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 3,
    "sticky_navigation": True,
    "titles_only": False,
}
html_static_path = ["_static"]
html_css_files = ["book.css"]
html_show_sourcelink = False
html_use_index = False
html_baseurl = "https://sonyyt.github.io/EdgeComputingBook/"
# Use a specific MathJax version. The initial online math renderer requires network access.
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js"
# Preserve the manuscript's existing visible numbering during the initial migration.
numfig = False
