# encoding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('blog.views',
<<<<<<< HEAD
    url(r'^$', 'home', name='home'),
=======
    url(r'^$', 'home'),
>>>>>>> d44f324b1a5eb179f6418777b59e2892a1ab4cc8
    url(r'^about/$', 'about_me', name='about_me'),
    url(r'^404', 'page_not_found', name='page_not_found'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
)
