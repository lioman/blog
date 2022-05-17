#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from datetime import datetime

import pelican_precompress

from pelican.plugins import i18n_templates, series, neighbors

CACHE_CONTENT = True
AUTHOR = "Lioman"
SITENAME = "Liomans Blog"
SITESUBTITLE = "42 ist die Antwort – aber wie lautet die Frage?"
SITEURL = ""
TIMEZONE = "Europe/Berlin"
SITELOGO = "/images/Artikelbild.png"

PATH = "content"

MARKDOWN = {
    "extension_configs": {
        # 'markdown.extensions.codehilite': {'css_class': 'highlight'},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}

STATIC_PATHS = [
    "images",
    "static/robots.txt",
    "static/favicon.ico",
    "static/keybase.txt",
    "static/stork.js",
    "static/stork.wasm",
]

EXTRA_PATH_METADATA = {
    "static/robots.txt": {"path": "robots.txt"},
    "static/favicon.ico": {"path": "favicon.ico"},
    "static/keybase.txt": {"path": "keybase.txt"},
}

IGNORE_FILES = ["__pycache__"]

THEME = "themes/flex"

HOME_HIDE_TAGS = False
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}


GOOGLE_VERIFICATION = "BqcGhsYr8KQ8E04PLoinE-PdzUdlvvgxGBxA1M_HRyo"

PYGMENTS_STYLE = "solarized-light"
PYGMENTS_STYLE_DARK = "solarized-dark"

DIRECT_TEMPLATES = [
    "index",
    "categories",
    "archives",
]

DISABLE_URL_HASH = True
DISPLAY_PAGES_ON_MENU = False
MAIN_MENU = True
MENUITEMS = (
    ("Allgemein", "/category/allgemein"),
    ("Digital", "/category/digital"),
    ("Kunst und Kultur", "/category/kunst-und-kultur"),
    ("Politik und Gesellschaft", "/category/politik-und-gesellschaft"),
    ("Wissenschaft und Technik", "/category/wissenschaft-und-technik"),
)


SHOW_ARTICLE_CATEGORY = True

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "de_De",
}
COPYRIGHT_YEAR = datetime.now().year

TIMEZONE = "Europe/Berlin"

OG_LOCALE = "de_De"
DEFAULT_LANG = "de"
ARTICLE_TRANSLATION_ID = "slug"
LOCALE = ("de_DE", "de_DE.utf8")

# Default theme language.
I18N_TEMPLATES_LANG = "en"

DEFAULT_CATEGORY = "Allgemein"

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"
CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"
YEAR_ARCHIVE_URL = "{date:%Y}/"
YEAR_ARCHIVE_SAVE_AS = "{date:%Y}/index.html"
MONTH_ARCHIVE_URL = "{date:%Y}/{date:%m}/"
MONTH_ARCHIVE_SAVE_AS = "{date:%Y}/{date:%m}/index.html"
REL_CANONICAL = True
DRAFT_URL = "drafts/{slug}/"
DRAFT_SAVE_AS = "drafts/{slug}/index.html"

PLUGIN_PATHS = ["plugins"]

PLUGINS = [
    "extended_sitemap",
    "pelican_youtube",
    series,
    neighbors,
    pelican_precompress,
    "search",
    i18n_templates,
]

# PRECOMPRESS_GZIP = True
# PRECOMPRESS_ZOPFLI = True
# PRECOMPRESS_BROTLI = True
# # PRECOMPRESS_OVERWRITE = False
# # PRECOMPRESS_MIN_SIZE = 20


USE_GOOGLE_FONTS = False

EXTENDED_SITEMAP_PLUGIN = {
    "priorities": {"index": 1.0, "articles": 0.8, "pages": 0.5, "others": 0.4},
    "changefrequencies": {
        "index": "daily",
        "articles": "weekly",
        "pages": "monthly",
        "others": "monthly",
    },
}

# Blogroll
# LINKS = (
#     # ("Impressum", "/pages/impressum"),
#     ("Pelican", "http://getpelican.com/"),
#     ("Python.org", "http://python.org/"),
#     ("OSBN", "https://osbn.de"),
# )

# Social widget
SOCIAL = (
    ("mastodon", "https://mastodon.social/@lioman"),
    ("twitter", "https://twitter.com/lioman"),
    ("gitlab", "https://gitlab.com/lioman"),
    ("github", "https://github.com/lioman"),
    ("stack-overflow", "http://stackoverflow.com/users/3114491/lioman"),
)

TWITTER_USERNAME = "lioman"

DEFAULT_PAGINATION = 10
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


THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

SEARCH_INPUT_OPTIONS = f"""stemming = "German"
                url_prefix = "http://localhost:8001/"
"""
