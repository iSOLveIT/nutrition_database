# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from fileinput import filename

CURDIR = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, CURDIR)

# -- Project information -----------------------------------------------------

project = 'USDA Nutrition Database'
copyright = '2015, Ontomatica'
author = 'Ontomatica'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.exceltable',
    'sphinxcontrib.napoleon',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.httpdomain',
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_immaterial",
]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# Turns on numbered figures for HTML output
number_figures = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'epilog.rst',
                    '_sphinx_lib']

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = None

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_logo = '_static/$_01-USDA-ARS-small_.png'
html_favicon = '_static/onto-favicon.svg'
html_title = "Nutrition Database"

html_theme = 'sphinx_immaterial'

# material theme options (see theme.conf for more information)
html_theme_options = {
    "icon": {
        "repo": "fontawesome/brands/github-square",
    },
    "site_url": "https://isolveit.github.io/nutrition_database/",
    "repo_url": "https://github.com/iSOLveIT/nutrition_database/",
    "repo_name": "Nutrition Database",
    "repo_type": "github",
    "edit_uri": "blob/main/docs/",
    "globaltoc_collapse": True,
    "features": [
        "navigation.top",
        "search.share",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "blue",
            "accent": "teal",
            "toggle": {
                "icon": "material/weather-night",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "blue",
            "accent": "teal",
            "toggle": {
                "icon": "material/weather-sunny",
                "name": "Switch to light mode",
            },
        },
    ],
    "toc_title_is_page_title": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ["custom.css"]

# Options for the linkcheck builder
# linkcheck_ignore = [
#     'https://w3id.org/linkml/*',
# ]

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright Ontomatica" is shown in the HTML footer. Default is True.
html_show_copyright = False

# This is the file name suffix for HTML files (e.g. ".xhtml").
html_file_suffix = '.html'

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr'
html_search_language = 'en'

# Output file base name for HTML help builder.
htmlhelp_basename = 'htmlhelpoutput'

mathjax_path = 'http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

# -- Intersphinx ---------------------------------------------------------------

intersphinx_cache_limit = 10  # days to keep the cached inventories
intersphinx_mapping = {
    'sphinx': ('http://sphinx.pocoo.org', None),
    'python': ('http://docs.python.org/3.2', None),
    'matplotlib': ('http://matplotlib.sourceforge.net', None),
    'numpy': ('http://docs.scipy.org/doc/numpy', None),
}
references = []
bibtex_path = os.path.join(".", "references")

if os.path.exists(bibtex_path):
    for bib_file in os.listdir(bibtex_path):
        if bib_file.endswith(".bib"):
            filename = os.path.basename(bib_file)
            references.append("./references/{}".format(filename))

bibtex_bibfiles = references

# -- Options for Napoleon Extension --------------------------------------------

# Parse Google style docstrings.
# See http://google-styleguide.googlecode.com/svn/trunk/pyguide.html
napoleon_google_docstring = True

# Parse NumPy style docstrings.
# See https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
napoleon_numpy_docstring = False

# Should special members (like __membername__) and private members (like _membername) members be included
# in the documentation if they have docstrings.
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

# If True, docstring sections will use the ".. admonition::" directive.
# If False, docstring sections will use the ".. rubric::" directive.
# One may look better than the other depending on what HTML theme is used.
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False

# If True, use Sphinx :ivar: directive for instance variables:
#     :ivar attr1: Description of attr1.
#     :type attr1: type
# If False, use Sphinx .. attribute:: directive for instance variables:
#     .. attribute:: attr1
#
#        *type*
#
#        Description of attr1.
napoleon_use_ivar = False

# If True, use Sphinx :param: directive for function parameters:
#     :param arg1: Description of arg1.
#     :type arg1: type
# If False, output function parameters using the :parameters: field:
#     :parameters: **arg1** (*type*) -- Description of arg1.
napoleon_use_param = True

# If True, use Sphinx :rtype: directive for the return type:
#     :returns: Description of return value.
#     :rtype: type
# If False, output the return type inline with the return description:
#     :returns: *type* -- Description of return value.
napoleon_use_rtype = True

# -- Autodoc configuration -----------------------------------------------------------------

autoclass_content = 'class'

autodoc_member_order = 'bysource'

autodoc_default_flags = ['members']

# -- Options for LaTeX output ---------------------------------------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': '',

# Latex figure (float) alignment
'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto, manual, or own class]).
latex_documents = [
                  ('index', 'sample_doc.tex', 'sample\\_doc Documentation', 'hidepy', 'manual'),
                  ]

# The name of an image file (relative to this directory) to place at the top of the title page.
latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts, not chapters.
latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output -----------------------------------------------------------

# One entry per manual page.
# List of tuples (source start file, name, description, authors, manual section).
man_pages = [
            ('index', 'sample_doc', 'sample_doc Documentation', ['hidepy'], 1)
            ]

# If true, show URL addresses after external links.
#man_show_urls = False

# -- Options for Texinfo output ---------------------------------------------------------------

# Grouping the document tree into Texinfo files.
# List of tuples (source start file, target name, title, author, dir menu entry, description, category)
texinfo_documents = [
                    ('index', 'sample_doc', 'sample_doc Documentation', 'hidepy',
                    'sample_doc', 'One line description of project.', 'Miscellaneous'),
                    ]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

