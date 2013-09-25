#!/usr/bin/env python
# encoding: utf-8
"""
urls.py

"""

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('brewkeeper.views',
    url(r'^$', 'home', name='home'),
)
