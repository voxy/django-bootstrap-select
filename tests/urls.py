# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from bootstrap_select.urls import urlpatterns as bootstrap_select_urls

urlpatterns = [
    url(r'^', include(bootstrap_select_urls, namespace='bootstrap_select')),
]
