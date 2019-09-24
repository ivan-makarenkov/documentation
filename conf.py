# -*- coding: utf-8 -*-
#
# The OroPlatform documentation build configuration file, created by
# sphinx-quickstart on Fri Mar 28 09:32:08 2014.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
import time

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('./sphinx'))

# adding PhpLexer
from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
# https://github.com/nyergler/hieroglyph
#https://pypi.python.org/pypi/sphinxcontrib-images
extensions = [
    'sphinxcontrib.phpdomain',
    'sensio.sphinx.configurationblock',
    'sensio.sphinx.phpcode',
    'oro.integrity_check',
    'builders.orohtml',
    'ext.orotoc',
    'ext.sitemap',
    'ext.sitemap-index'
]

spelling_lang='en_US'
spelling_word_list_filename='spelling_wordlist.txt'
spelling_show_suggestions=True


# set url for API links
api_url = 'http://phpdoc.orocrm.com/platform/%s'
api_url_pattern = 'http://phpdoc.orocrm.com/platform/{namespace}namespaces{/namespace}{class}classes{/class}{method}classes{/method}/%(namespace)s{class}.%(class)s{/class}{method}.%(class)s{/method}.html{method}#method_%(method)s{/method}'
namespace_separator = '.'

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'OroCommerce'
copyright = u'2017, Oro Team'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version = '1.0'
# The full version, including alpha/beta/rc tags.
# release = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', 'completeReference/overview', 'sphinx', '_themes']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Use PHP syntax highlighting in code examples by default
highlight_language='php'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# -- Settings for symfony doc extension ---------------------------------------------------

# enable highlighting for PHP code not between ``<?php ... ?>`` by default
lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)

# use PHP as the primary domain
primary_domain = 'php'

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes", ]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
#'fixed_sidebar': False,
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {
#   '**': ['localtoc.html', 'globaltoc.html'],
#   'using/windows': ['windowssidebar.html'],
#}
# hidden for local preview: , 'relations.html', 'searchbox.html'
# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {'index': 'index.html', 'error-page': 'error-page.html'}

# A list of paths that contain extra files not directly related to the documentation, such as robots.txt or .htaccess.
# Relative paths are taken as relative to the configuration directory. They are copied to the output directory.
# They will overwrite any existing file of the same name.
# As these files are not meant to be built, they are automatically excluded from source files.
html_extra_path = ['robots.txt']

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'TheOroCommercedoc'

def setup(app):
    app.add_stylesheet('https://use.fontawesome.com/releases/v5.2.0/css/all.css')
#    app.add_stylesheet('css/custom.css')

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'TheOroCommerce.tex', u'The OroCommerce Documentation',
   u'Oro Team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'theorocommerce', u'The OroCommerce Documentation',
     [u'Oro Team'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'TheOroCommerce', u'The OroCommerce Documentation',
   u'Oro Team', 'TheOroCommerce', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'The OroCommerce'
epub_author = u'OroTeam'
epub_publisher = u'OroTeam'
epub_copyright = u'2017, OroTeam'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 5

# Allow duplicate toc entries.
#epub_tocdup = True

# List of document titles which are related to developers documentation but placed not in the developer directory
# All this documents and their children will get additional level to developer root document in the breadcrumbs
developer_titles = ['Backend Developer Guide', 'Frontend Developer Guide', 'Community Guide']

# current_timestamp is used to prevent chaching of assets in case of new build
# it's added to all css/js files as GET parameter
html_context = {
    'current_timestamp': time.time(),
    'developer_titles': developer_titles
}

# Base URL of the website.
# Required by sphinx_sitemap extension
html_baseurl = 'https://doc.oroinc.com/'

# ORO settings
# Sphinx versioning (scv) config
# Mappings of git branches and directory name for this branch in build directory
scv_version_dirs = {
    # Development dirs
    'epic/DOC-1216_doc_3.1': '3.1',
    'epic/DOC-1216_doc_2.6': '1.6',
    'doc/3.1': '3.1',
    'doc/2.6': '1.6',

    # Test dirs from public rep
    'doc-3.1': '3.1',
    'doc-2.6': '1.6',
}
