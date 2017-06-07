#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eloi Vanderbeken'
SITENAME = u'IDA Suck Less'
SITEURL = 'https://idasuckless.github.io'
RELATIVE_URLS = True
THEME = 'theme'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['slides','favicon.png', 'CNAME']
READERS = {'html': None}

# <a class="twitter-timeline" href="https://twitter.com/IDASuckLess">Tweets by IDASuckLess</a> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

TWITTER_WIDGET_ID = u'1'
TWITTER_USERNAME = u'IDASuckLess'
MARKDOWN = {
	'extension_configs': {
		'markdown.extensions.codehilite': {'css_class': 'highlight'},
		'markdown.extensions.extra': {},
		'markdown.extensions.meta': {},
	},
	'output_format': 'html5'
}
DEFAULT_PAGINATION = 10

FAVICON = u'favicon.png'
SUMMARY_MAX_LENGTH = 100
PAGINATED_DIRECT_TEMPLATES = []
