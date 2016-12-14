#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yuya Kusakabe'
SITENAME = u'higeblog'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = u'ja'
DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'jp': '%Y-%m-%d(%a)',
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('vyos-users.jp', 'http://www.vyos-users.jp/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/higebu'),
          ('facebook', 'http://www.facebook.com/higebu'),
          ('github', 'http://github.com/higebu'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = (['images', 'extra/CNAME'])
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}
FAVICON = 'images/favicon.ico'

BOOTSTRAP_THEME = 'cosmo'
GITHUB_USER = 'higebu'
CODERWALL_USER = 'higebu'
ADDTHIS_PROFILE = 'ra-53123bf42910d399'

PATH = 'content'
REVERSE_CATEGORY_ORDER = True
TAG_CLOUD_MAX_ITEMS = 10

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

THEME = 'theme'

PLUGIN_PATHS = ['plugins']

PLUGINS = [
    'pelican_gist',
    'liquid_tags.img',
    'liquid_tags.video',
    'liquid_tags.youtube',
    'liquid_tags.include_code',
    'liquid_tags.notebook',
    'tag_cloud'
]

MD_EXTENSIONS = (['del_ins', 'fenced_code', 'codehilite(css_class=highlight)', 'tables', 'toc'])
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}
