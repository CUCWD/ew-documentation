# -*- coding: utf-8 -*-
#

import sys, os
from datetime import date

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

master_doc = 'index'

# The suffix of source filenames.
source_suffix = '.rst'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

extensions = ['sphinx.ext.ifconfig']

tags.add('EducateWorkforce')

product = 'EducateWorkforce'

def setup(app):
    app.add_config_value('product', '', True)


# General information about the project.
project = u'EducateWorkforce User\'s Guide'
copyright = u'{copyright_year}, EducateWorkforce'.format(copyright_year="2009 - " + str(date.today().year))

# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# html_theme = 'default'
html_theme = 'ew_theme'

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []
html_theme_path = ['../../_themes']

html_favicon = '../../_themes/ew_theme/static/css/favicon.ico'

#html_use_smartypants = True
html_use_smartypants = True

if on_rtd:
    html_context = {
       "on_rtd" : on_rtd,
       "google_analytics_id" : '',
       "disqus_shortname" : 'cucwd',
       "github_base_account" : 'cucwd',
       "github_project" : 'ew-documentation',
    }