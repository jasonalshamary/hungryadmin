#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Forrest Alvarez'
SITENAME = u'Hungry Admin'
SITEURL = 'http://hungryadmin.com'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('SaltStack', 'http://saltstack.org'),)

# Social widget
SOCIAL = (('github', 'http://github.com/gravyboat'),
          ('twitter', 'http://twitter.com/failvarez'),
          ('stackoverflow', 'http://stackoverflow.com/users/1263015/forrest'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme
THEME = "themes/pelican-bootstrap3"
