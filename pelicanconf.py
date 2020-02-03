#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'TARDIS-SN'
SITENAME = 'TARDIS GSoC'
SITEURL = 'https://tardis-sn.github.io/tardis-sn-gsoc-website'
RELATIVE_URLS = True

PATH = 'content'
STATIC_PATH=['images', 'pdfs']

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

THEME='theme'

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
         ('TARDIS', 'https://github.com/tardis-sn/tardis'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/tardis_sn'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
