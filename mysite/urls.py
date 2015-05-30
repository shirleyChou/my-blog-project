# encoding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('blog.views',
    url(r'^$', 'home'),
    url(r'^about/$', 'about_me', name='about_me'),
    url(r'^404', 'page_not_found', name='page_not_found'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^blog/', include('blog.urls', namespace='blog')),
)

