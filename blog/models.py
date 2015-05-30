# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
"""
class User(models.Model):
    first_name = models.CharField(u'名', max_length=30)
    last_name = models.CharField(u'姓', max_length=40)
    # verbose_name: define the name shown in Django administration
    # also: ('e-mail', blank=True)
    email = models.EmailField('e-mail', blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)
"""

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', u"草稿"),
        ('p', u"发布"),
    )

    title = models.CharField(u'标题', max_length=50, unique=True)
    author = models.ForeignKey(User, verbose_name=u'作者')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    publish_time = models.DateTimeField(u'公开时间', null=True)
    update_time = models.DateTimeField(u'修改时间', auto_now=True)
    abstract = models.CharField(u'摘要', max_length=200, default='', blank=True)
    content = models.TextField(u'内容', )
    status = models.CharField(u'状态', max_length=1, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    is_public = models.BooleanField(u'公开', default=True)
    is_top = models.BooleanField(u'置顶', default=False)

    def __unicode__(self):
        return self.title

"""
class Comment(models.Model):
    #authors = models.ManyToManyField(Author)
    author = models.CharField(max_length=30)
    email = models.EmailField('e-mail', blank=True)
    #publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title
"""
