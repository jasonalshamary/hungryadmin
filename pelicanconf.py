#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Forrest Alvarez'
SITENAME = u'Hungry Admin'
SITEURL = 'https://hungryadmin.com'

TIMEZONE = 'GMT'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Bandcamp', 'https://bandcamp.com/metalfunk'),
         ('Bitcoin tip', 'https://blockchain.info/qr?data=1PpdFh9LkTsjtG2AAcrWqk6RiFrC2iTCxj'),
         ('Bulk Eats', 'https://bulkeats.com'),
         ('GitHub', 'https://github.com/gravyboat'),
        )

# Social widget
#SOCIAL = (('github', 'https://github.com/gravyboat'),
#          )


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PAGE_PATHS = ['content/pages']

# Theme
THEME = "themes/pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = "sandstone"

# Code block theme
PYGMENTS_STYLE = 'solarizeddark'

# Custom css
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['extra/custom.css', 'images']

# Other
PLUGINS = ['minification']
GITHUB_URL = 'https://github.com/gravyboat'
MENUITEMS = (('Talks', 'https://speakerdeck.com/gravyboat'),)
READERS = {'html': None}
IGNORE_FILES = ['README.rst', 'LISEZ-MOI.rst']
