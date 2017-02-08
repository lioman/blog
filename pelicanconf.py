#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lioman'
SITENAME = 'Liomans Blog'
SITEURL = ''

PATH = 'content'

STATIC_PATHS = ['images']

THEME = 'blueidea'

DISPLAY_SEARCH_FORM = False
DISPLAY_CATEGORIES_ON_MENU =False

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU= True

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'

PLUGINS = [
    'pelican_youtube',
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)


DEFAULT_PAGINATION = False

TYPOGRIFY = True
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
