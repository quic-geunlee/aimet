# -*- coding: utf-8 -*-
# pylint: skip-file
# =============================================================================
#  @@-COPYRIGHT-START-@@
#
#  Copyright (c) 2020, Qualcomm Innovation Center, Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.
#
#  SPDX-License-Identifier: BSD-3-Clause
#
#  @@-COPYRIGHT-END-@@
# =============================================================================
""" Configuration file for the Sphinx documentation builder """

# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'AI Model Efficiency Toolkit'
copyright = '2020, Qualcomm Innovation Center, Inc.'
author = 'Qualcomm Innovation Center, Inc.'

# The short X.Y version
version = '2.0'
# The full version, including alpha/beta/rc tags
release = '2.0'
if "SW_VERSION" in os.environ:
    version = os.environ['SW_VERSION']
else:    
    sys.exit("Unable to set version. SOFTWARE_VERSION is NOT defined.")

included_features = []

def setup(app):
    app.add_config_value('included_features', included_features, 'env')


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '5.3.0'
needs_sphinx = '7.3.7'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_autodoc_typehints',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.ifconfig',
    'nbsphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_design',
    'sphinx_copybutton'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
# The TOC options are hard-coded in the _templates/navigator.html file.
# For some reason this theme doesn't seem to be setting user-defined config variables.

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
root_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# prefix each section label with the name of the document it is in, followed by a colon
autosectionlabel_prefix_document = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_title = 'AI Model Efficiency Toolkit v. ' + release
# html_short_title = 'AIMET Docs v. ' + version
# html_logo = 'images/brain_logo.png'
# html_favicon = 'images/brain_logo16.png'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    "sidebar_hide_name": False,                  # Default is False
    "top_of_page_buttons": [],
    "navigation_with_keys": True,
#    "announcement": "<em>Important</em> announcement!",
    "footer_icons": [                            # This is ugly. Will fix later.
        {
            "name": "GitHub",
            "url": "https://github.com/quic/aimet",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['aimet-furo.css']    # Changes from default theme file.

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# furo theme sidebars
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
#        "sidebar/search.html",
        "sidebar/scroll-end.html",
    ]
}
# Custom TOC settings


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'AIMETdoc'

# Use this section to define substitution patterns that get exported to each rst page
rst_epilog = """
.. |author| replace:: {author}
.. |project| replace:: {project}
.. |default-quantsim-config-file| replace:: aimet_common/quantsim_config/default_config.json
.. |version| replace:: {version}
""".format(project=project, author=author, version=version)

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (root_doc, 'AIMET.tex', 'AI Model Efficiency Toolkit Documentation',
     'Qualcomm Innovation Center, Inc.', 'manual')
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (root_doc, 'aimet', 'AI Model Efficiency Toolkit Documentation',
     author, 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (root_doc, 'AIMET', 'AI Model Efficiency Toolkit  Documentation',
     author, 'AIMET', 'One line description of project.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------
autoclass_content = 'both'

nbsphinx_allow_errors = True
nbsphinx_execute = 'never'

docs_root_url = "https://quic.github.io/aimet-pages/releases/latest/"

# Version here refers to the AIMET torch v1/v2 version, not the AIMET release number
html_context = {
  'current_version' : "Universal",
  'versions' : [["Universal", docs_root_url + "features/index.html"],
                ["PyTorch", docs_root_url + "torch_v2/torch_docs/index.html"]],
  'display_version_tab': False
}

docs_root_url = "https://quic.github.io/aimet-pages/releases/latest/"

# Version here refers to the AIMET torch v1/v2 version, not the AIMET release number
html_context = {
  'current_version' : "Universal",
  'versions' : [["Universal", docs_root_url + "features/index.html"],
                ["PyTorch", docs_root_url + "torch_v2/torch_docs/index.html"]],
  'display_version_tab': False
}

autosummary_generate = False

# contains a list of modules to be mocked up which are not available during docs build time
autodoc_mock_imports = []
# aimet_common
autodoc_mock_imports.append("aimet_common.libpymo")
# aimet_torch
# TODO (hitameht): remove ``onnxscript`` module once we build docs using separate environment
autodoc_mock_imports.extend(["aimet_common.aimet_tensor_quantizer", "aimet_common.AimetTensorQuantizer"])
# Mocking onnxscript with autodoc causes import failures with torch 2.0
from unittest import mock
sys.modules["onnxscript"] = mock.Mock()

# aimet_tensorflow
autodoc_mock_imports.append("aimet_common.libaimet_tf_ops")
# aimet_onnx
# TODO (hitameht): remove ``onnxruntime`` module once we build docs using separate environment
autodoc_mock_imports.extend(["aimet_common.libquant_info", "onnxruntime"])

from pygments.lexers.diff import DiffLexer
from sphinx.highlighting import lexers
lexers['diff'] = DiffLexer()