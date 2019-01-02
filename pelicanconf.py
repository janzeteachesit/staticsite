#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'janzeteachesit'
SITENAME = 'Python Programming for Templeton STEM'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Vancouver'

DEFAULT_LANG = 'en'

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
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#pelicanconf.py - changes for pelican-bootstrap3 - 20190101
PLUGIN_PATHS = ['pelican-plugins']
MARKUP = ('md', 'ipynb')

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

PLUGIN_PATHS = ['./pelican-plugins']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGINS = ['i18n_subsites', 'series', 'tag_cloud', 'liquid_tags.youtube', 'liquid_tags.notebook', 'liquid_tags.include_code', 'render_math', 'pelican-ipynb.markup', 'ipynb.markup' ]
IGNORE_FILES = ['.ipynb_checkpoints', 'post_template' ]

I18N_TEMPLATES_LANG = 'en'

