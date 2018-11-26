#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://www.lioman.de'
RELATIVE_URLS = False

OUTPUT_PATH = 'public'

FEED_DOMAIN = SITEURL

FEED_ALL_ATOM = 'feed/atom/index.html'
CATEGORY_FEED_ATOM = 'category/%s/feed/atom/index.html'
TAG_FEED_ATOM = 'tag/%s/feed/atom/index.html'

FEED_ALL_RSS = 'feed/index.html'
CATEGORY_FEED_RSS = 'category/%s/feed/index.html'
TAG_FEED_RSS = 'tag/%s/feed/index.html'

RSS_FEED_SUMMARY_ONLY = False

DELETE_OUTPUT_DIRECTORY = True
