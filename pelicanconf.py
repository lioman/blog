#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lioman'
SITENAME = 'Liomans Blog'
SITEURL = ''

PATH = 'content'

STATIC_PATHS = [
    'images',
    'static/robots.txt',
    'static/favicon.ico',
]

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
}

THEME = 'themes/pelican-bootstrap3'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
BOOTSTRAP_THEME = 'readable'
PYGMENTS_STYLE = 'solarizedlight'

DIRECT_TEMPLATES = ('index', 'categories', 'search')

DISPLAY_PAGES_ON_MENU = True
DISPLAY_SEARCH_FORM = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
SHARIFF = True
SHARIFF_TWITTER_VIA = 'lioman'

# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = False

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'
DEFAULT_CATEGORY = 'Allgemein'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'

PLUGIN_PATHS = [
    'plugins'
]

PLUGINS = [
    'i18n_subsites',
    'pelican_youtube',
    'subcategory',
    'tipue_search',
]

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/lioman'),
    ('Github', 'https://github.com/lioman'),
    ('Stack overflow', 'http://stackoverflow.com/users/3114491/lioman'),
)

TWITTER_USERNAME = 'lioman'

DEFAULT_PAGINATION = False

TYPOGRIFY = True
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
