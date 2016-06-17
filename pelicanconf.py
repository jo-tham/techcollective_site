#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site info
AUTHOR = u'TechCollective'
SITENAME = u'TechCollective'
SITEURL = ''


# Do not use cache
LOAD_CONTENT_CACHE = False


# Page and article slugs
# changing these has ramifications for back links
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'


# Blogroll pagination
DEFAULT_PAGINATION = 3


# Path settings
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['blog']
STATIC_PATHS = ['images', 'downloads', 'resume']


# Locale stuff
TIMEZONE = 'Canada/Pacific'
DEFAULT_LANG = u'en'


# Markdown extensions
MD_EXTENSIONS = ['codehilite(linenums=False,\
                 css_class=highlight,guess_lang=False)']


# Theme settings
THEME = "pelican-themes/pure"
TAGLINE = ('TODO')

DISQUS_ON_PAGES = False
PROFILE_IMG_URL = '/images/favicon.png'

CC_LICENSE = "CC-BY-SA"
# CC_LICENSE_DERIVATIVES = "yes"
# CC_LICENSE_COMMERCIAL = "yes"
# CC_ATTR_MARKUP = true


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
