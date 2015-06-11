# encoding: utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'^', include('mysite.apps.home.urls')),
    # url(r'^account/', include('mysite.apps.account.urls')),
    url(r'^$', 'mysite.apps.blog.views.home'),
    url(r'^blog/', include('mysite.apps.blog.urls', namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),  
    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)
