#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'FAB'
SITENAME = u'\b\b帆布\'Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'

THEME = "plumage"

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
         )

# Social widget
SOCIAL = (('Github', 'https://github.com/ForrestAlfred'),
          )

DISQUS_SITENAME = 'Fabricblog'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#plumage settings
SITE_THUMBNAIL = '/pic/8122371.jpg'
SITE_THUMBNAIL_TEXT = 'GNU iOS Helper From China'

SITESUBTITLE = "Open-Source iOS Software Engineer"

MENUITEMS = (
    ('Home', '/'),
    ('Reverse','/'),
    ('Smart House','/'),
    ('Robert','/'),
    ('Swift','/'),
    ('C/C++','/'),
    ('Python','/'),
    ('Prolog','/'),
    ('About', '/pages/about-me.html'),
)

GOOGLE_SEARCH = '006364432850422186161:7vbi34hyqyq'

GOOGLE_ANALYTICS = 'UA-66013225-1'
