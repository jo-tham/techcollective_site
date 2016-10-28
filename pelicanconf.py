#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Site info
AUTHOR = u'Tech Collective'
SITENAME = u'Tech Collective'
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
STATIC_PATHS = ['images']


# Locale stuff
TIMEZONE = 'Canada/Pacific'
DEFAULT_LANG = u'en'


# Markdown extensions
MD_EXTENSIONS = ['codehilite(linenums=False,\
                 css_class=highlight,guess_lang=False)']

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['gravatar']

# Theme settings
THEME = "pelican-themes/pure"
TAGLINE = ('Monthly Tech Meetup in Whitehorse, YT')

DISQUS_ON_PAGES = False
COVER_IMG_URL = '/images/sidebar.jpg'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links for sidebar
LINKS = (
    ('MAILING LIST', 'http://eepurl.com/cl7rMP'),
    ('ARCHIVES', 'tech-collective.com/archives.html'),
)
