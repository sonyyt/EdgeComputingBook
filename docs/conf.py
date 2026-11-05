"""English web edition of the complete v0.4.2 manuscript."""
project = 'Edge Computing Systems'
author = 'Zheng Song'
copyright = '2026, Zheng Song'
version = '0.4.2'
release = '0.4.2'
language = 'en'
extensions = ['myst_parser', 'sphinx.ext.mathjax']
source_suffix = {'.md': 'markdown'}
root_doc = 'index'
exclude_patterns = ['_build', '.DS_Store', 'Thumbs.db']
html_theme = 'sphinx_rtd_theme'
html_title = 'Edge Computing Systems'
html_theme_options = {
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 3,
    'includehidden': True,
    'titles_only': False,
    'prev_next_buttons_location': 'both',
    'style_external_links': True,
}
html_static_path = ['_static']
html_css_files = ['book.css']
html_js_files = ['book.js']
myst_enable_extensions = ['dollarmath', 'colon_fence']
myst_heading_anchors = 4
myst_dmath_allow_digits = False
# Printed chapter, table and figure identifiers are preserved verbatim.
numfig = False
html_show_sourcelink = True
html_show_sphinx = True
html_baseurl = 'https://sonyyt.github.io/EdgeComputingBook/'
html_context = {
    'display_github': True,
    'github_user': 'sonyyt',
    'github_repo': 'EdgeComputingBook',
    'github_version': 'full-book-v042',
    'conf_py_path': '/docs/',
}
mathjax3_config = {'tex': {'tags': 'none'}}

# Keep identifiers and URLs identical to the source.
smartquotes = False
