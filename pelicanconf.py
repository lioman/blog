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
BOOTSTRAP_FLUID = False
PYGMENTS_STYLE = 'solarizedlight'


DIRECT_TEMPLATES = ('index', 'categories', 'search')

DISPLAY_PAGES_ON_MENU = True
DISPLAY_SEARCH_FORM = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SUBMENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True

SHARIFF = True
SHARIFF_TWITTER_VIA = 'lioman'

SHOW_ARTICLE_CATEGORY = True

CC_LICENSE = 'CC-BY-SA'

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
    'tipue_search',
]

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/lioman'),
    ('Github', 'https://github.com/lioman'),
    ('Stackoverflow', 'http://stackoverflow.com/users/3114491/lioman', 'stack-overflow'),
)

TWITTER_USERNAME = 'lioman'

DEFAULT_PAGINATION = 5
USE_PAGER = True

TYPOGRIFY = True
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
