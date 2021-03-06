# encoding: utf-8
from django.conf.urls import patterns, url

# URLconf的本质是URL以及视图函数的映射表
# 当patterns只包含''的时候，'127.0.0.1:8000'自动显示congrate.不然就进行匹配
urlpatterns = patterns('mysite.apps.blog.views',
    url(r'^$', 'home', name='home'),
    url(r'^posts/$', 'all_posts', name='all_posts'),
    url(r'^about/$', 'about_me', name='about_me'),
    url(r'^(?P<blog_id>\d+)/(?P<link>[\w,-]*)/$', 'article', name='article'),
    # url(r'^write-new-post/$', 'add_article', name='add_article'),
    # url(r'^create-new-post/$', 'create_article', name='create_article'),  
)
