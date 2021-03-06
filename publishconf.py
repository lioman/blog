#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = "https://www.lioman.de"
RELATIVE_URLS = False

OUTPUT_PATH = "public"

FEED_DOMAIN = SITEURL

FEED_ALL_ATOM = "feed/atom/index.html"
CATEGORY_FEED_ATOM_URL = "category/{slug}/feed/atom/index.html"
TAG_FEED_ATOM_URL = "tag/{slug}/feed/atom/index.html"

FEED_ALL_RSS = "feed/index.html"
CATEGORY_FEED_RSS_URL = "category/{slug}/feed/index.html"
TAG_FEED_RSS_URL = "tag/{slug}/feed/index.html"

RSS_FEED_SUMMARY_ONLY = False

DELETE_OUTPUT_DIRECTORY = True

SEARCH_INPUT_OPTIONS = f"""stemming = "German"
                url_prefix = "{SITEURL}/"
"""

PRECOMPRESS_GZIP = True
PRECOMPRESS_ZOPFLI = True
PRECOMPRESS_BROTLI = True

LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False
