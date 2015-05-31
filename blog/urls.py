# encoding: utf-8
from django.conf.urls import patterns, url

# URLconf的本质是URL以及视图函数的映射表
# 当patterns只包含''的时候，'127.0.0.1:8000'自动显示congrate.不然就进行匹配
urlpatterns = patterns('blog.views',
    # url(r'^$', 'home'),
    url(r'^posts/$', 'all_posts', name='all_posts'),
    url(r'^(?P<blog_id>\d+)/(?P<blog_link>[\w,-]*)$', 'article', name='article'),
)
