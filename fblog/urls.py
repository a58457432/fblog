#!/usr/bin/env python
# encoding: utf-8

from django.conf.urls import url,patterns
from . import views
from django.views.generic.base import RedirectView
from django.contrib import admin


urlpatterns = [
    url(r'^home$', views.blogindex.as_view(), name='index'),
    url(r'^blog/article/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name='detail'),
    url(r'^category/(?P<cate_id>\d+)$', views.CategoryView.as_view(), name='category'),
    url(r'^category/(?P<fk_cate_id>\d+)$', views.Fk_CategoryView.as_view(), name='fk_category'),
    url(r'^test$', views.test, name='test'),
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/favicon.ico')),
    url(r'^qrcode/(.+)$', views.generate_qrcode, name='qrcode'),
    url(r'^admin/', admin.site.urls),
#    url(r'^list/$', views.BlogListView.as_view(), name='list'),
#    url(r'^detail/(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name='detail'),
]

