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
LINKS = (('Gratipay', 'https://gratipay.com/~gravyboat/'),
        ('Flattr', 'https://flattr.com/profile/gravyboat'),
        ('Books on Gumroad', 'https://gumroad.com/gravyboat'),
        )

# Social widget
SOCIAL = (('github', 'https://github.com/gravyboat'),
          ('twitter', 'https://twitter.com/failvarez'),
          ('stack-overflow', 'http://stackoverflow.com/users/1263015/forrest'),
          )


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PAGE_PATHS = ['content/pages']

# Theme
THEME = "themes/pelican-themes/pelican-bootstrap3"

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
