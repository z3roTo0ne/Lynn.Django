# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your models here.
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User
from django.utils.timezone import now


class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name=u"出版社名")
    address = models.CharField(max_length=50, verbose_name=u"地址")
    city = models.CharField(max_length=60, verbose_name=u"城市")
    state_province = models.CharField(max_length=30, verbose_name=u"省份")
    country = models.CharField(max_length=50, verbose_name=u"国家")
    website = models.URLField(verbose_name=u"站点")
    history = HistoricalRecords()

    def __repr__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = u"出版社"


class Author(models.Model):
    salutation = models.CharField(max_length=10, verbose_name=u"称呼")
    first_name = models.CharField(max_length=30, verbose_name=u"名")
    last_name = models.CharField(max_length=40, verbose_name=u"姓")
    email = models.EmailField(verbose_name=u"电子邮件")
    history = HistoricalRecords()

    def __repr__(self):
        return self.salutation

    def __unicode__(self):
        return self.salutation

    class Meta:
        verbose_name_plural = u"作者"


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"书名")
    authors = models.ManyToManyField(Author, verbose_name=u"作者")
    publisher = models.ForeignKey(Publisher, verbose_name=u"出版社")
    publication_date = models.DateField(verbose_name=u"出版日期")
    published = models.BooleanField(default=True, verbose_name=u"是否出版")
    history = HistoricalRecords()

    def __repr__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_authors(self):
        """
        对于多对多的字段需要这样处理一下
        """
        return ",".join([str(p) for p in self.authors.all()])
    get_authors.short_description = u'作者'   # 改变后台显示名称

    class Meta:
        verbose_name_plural = "书籍列表"

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value


class Notify(models.Model):
    user = models.ForeignKey(User, verbose_name=u"用户")
    add_time = models.DateTimeField(default=now, verbose_name=u"消息获取时间")
    message = models.CharField(max_length=50, verbose_name=u"消息内容")
    read = models.BooleanField(default=False, verbose_name=u"是否已读")

    def __unicode__(self):
        return self.message

    class Meta:
        verbose_name_plural = u"消息推送表"


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# 代码片段保存
class Snippet(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets')
    highlighted = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)


