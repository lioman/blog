#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://www.lioman.de'
RELATIVE_URLS = False

OUTPUT_PATH = 'public'

FEED_DOMAIN = SITEURL

FEED_ALL_ATOM = 'feed/atom/'
CATEGORY_FEED_ATOM = '%s/feed/atom/'
TAG_FEED_ATOM = '%s/feed/atom/'

FEED_ALL_RSS = 'feed/'
CATEGORY_FEED_RSS = '%s/feed/'
TAG_FEED_RSS = '%s/feed/'

RSS_FEED_SUMMARY_ONLY = False

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
