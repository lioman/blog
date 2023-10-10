#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = os.environ.get("BLOG_DEPLOY_URL", "https://lioman.de")
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


STORK_INPUT_OPTIONS["url_prefix"] = SITEURL

PRECOMPRESS_GZIP = True
PRECOMPRESS_ZOPFLI = True
PRECOMPRESS_BROTLI = True

PRECOMPRESS_TEXT_EXTENSIONS = {
    ".atom",
    ".css",
    ".htm",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".py",
    ".rss",
    ".txt",
    ".xml",
    ".xsl",
    ".st",
    ".wasm",
}

LOAD_CONTENT_CACHE = False
CACHE_CONTENT = False
