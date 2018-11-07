#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Lioman'
SITENAME = 'Liomans Blog'
SITESUBTITLE = '42 ist die Antwort – aber wie lautet die Frage?'
SITEURL = ''
LOCALE = 'de_DE'
TIMEZONE = "Europe/Berlin"

PATH = 'content'

STATIC_PATHS = [
    'images',
    'static/robots.txt',
    'static/favicon.ico',
    'static/.htaccess',
]

EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
    'static/.htaccess': {'path': '.htaccess'},
}

IGNORE_FILES = ['__pycache__']

THEME = 'themes/pelican-bootstrap3'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

GOOGLE_VERIFICATION = 'BqcGhsYr8KQ8E04PLoinE-PdzUdlvvgxGBxA1M_HRyo'

BOOTSTRAP_THEME = 'readable'
BOOTSTRAP_FLUID = False
PYGMENTS_STYLE = 'solarizedlight'
DIRECT_TEMPLATES = ('index', 'categories', 'search')

DISPLAY_PAGES_ON_MENU = True
# DISPLAY_SEARCH_FORM = False
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True

SHARIFF = True
SHARIFF_TWITTER_VIA = 'lioman'
SHARIFF_ORIENTATION = 'vertical'
SHARIFF_SERVICES = [
    'twitter', 
    'facebook', 
    'linkedin', 
    'xing',
    ]

SHOW_ARTICLE_CATEGORY = True

CC_LICENSE = 'CC-BY-SA'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'de'
DEFAULT_CATEGORY = 'Allgemein'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

PLUGIN_PATHS = [
    'plugins'
]

PLUGINS = [
    'extended_sitemap',
    'i18n_subsites',
    'pelican_youtube',
    'series',
    'tipue_search',
    'tag_cloud',
]

# Tags
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 40

EXTENDED_SITEMAP_PLUGIN = {
    'priorities': {
        'index': 1.0,
        'articles': 0.8,
        'pages': 0.5,
        'others': 0.4
    },
    'changefrequencies': {
        'index': 'daily',
        'articles': 'weekly',
        'pages': 'monthly',
        'others': 'monthly',
    }
}

# Blogroll
LINKS = (
        ('Pelican', 'http://getpelican.com/'),
        ('Python.org', 'http://python.org/'),
        ('OSBN', 'https://osbn.de'),
         )

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/lioman'),
    ('Mastodon', 'https://mastodon.social/@lioman'),
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
