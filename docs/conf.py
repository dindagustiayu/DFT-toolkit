# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DFT Toolkit'
copyright = '2026, Dinda Gusti Ayu'
author = 'Dinda Gusti Ayu'
release = '2026'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

# templates_path = ['source/_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/.ipynb_checkpoints']

language = 'en'

# source_suffix = {
#    ".rst": "restructuredtext",
#   ".md": "markdown",
# }

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['source']

# Sidebar and navigation options
html_theme_options = {
    "navigation_depth": 2,    
    "collapse_navigation": True,
    "sticky_navigation": True,
    "titles_only": False,
}

# link at the top right of each page
html_context = {
    "display_github": True,
    "github_user": "dindagustiayu",
    "github_repo": "DTF-toolkit",
    "github_version": "main",  
    "conf_py_path": "/docs/",
}

