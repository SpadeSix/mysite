#!/usr/bin/python
# -*- coding: utf-8 -*-


from django.contrib import admin
from django.conf.urls import *
from . import views, testdb,search,search2,contect



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello$', views.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
    url(r'^time$', views.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
    url(r'^test1$', views.test1),
    url(r'^contect$',contect.contact)
]
