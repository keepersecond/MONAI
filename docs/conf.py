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
import subprocess
sys.path.insert(0, os.path.abspath('..'))
print(sys.path)



# -- Project information -----------------------------------------------------

project = 'MONAI'
copyright = '2020, MONAI Consortium'
author = 'MONAI Consortium'

# The full version, including alpha/beta/rc tags
release = 'v0.1'
version = 'v0.1'

def generate_apidocs(*args):
    """Generate API docs automatically by trawling the available modules"""
    module_path = os.path.abspath('..')
    output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'apidocs'))
    apidoc_command_path = 'sphinx-apidoc'
    if hasattr(sys, 'real_prefix'):  # called from a virtualenv
        apidoc_command_path = os.path.join(sys.prefix, 'bin', 'sphinx-apidoc')
        apidoc_command_path = os.path.abspath(apidoc_command_path)
    print('output_path {}'.format(output_path))
    print('module_path {}'.format(module_path))
    subprocess.check_call(
        [apidoc_command_path, '-f'] +
        ['-o', output_path] +
        [module_path])


def setup(app):
    # Hook to allow for automatic generation of API docs
    # before doc deployment begins.
    app.connect('builder-inited', generate_apidocs)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
source_suffix = {
        '.rst': 'restructuredtext',
        '.txt': 'restructuredtext',
        '.md': 'markdown',
}

extensions = [
        'recommonmark',
        'sphinx.ext.intersphinx',
        'sphinx.ext.mathjax',
        'sphinx.ext.napoleon',
        'sphinx.ext.autodoc',
        'sphinx.ext.viewcode',
        'sphinx.ext.autosectionlabel'
]

autoclass_content = 'both'
add_module_names = False
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme_options = {
        'collapse_navigation': True,
        'display_version': True,
        # 'navigation_depth': 4,
        'sticky_navigation': True,  # Set to False to disable the sticky nav while scrolling.
        # 'logo_only': True,  # if we have a html_logo below, this shows /only/ the logo with no title text
}
html_scaled_image_link = False
html_show_sourcelink = True 
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
