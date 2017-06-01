# -*- coding: utf-8 -*-
"""from django import template
 register = template.Library()

 @register.filter(name='cut')
 def cut(value, arg):
 　　return value.replace(arg, '')
 使用方法： {{ somevariable|cut:" " }}
 这里的somevariable便是cut中的value，“ ”便是arg，整个filter的作用是将somevariable中的“ ”（空格）替换成''，也即去掉somevariable中的空格
"""
from django import template
from django.core.serializers import serialize
from django.db.models.query import QuerySet
register = template.Library()


@register.filter(name="jsonify")
def jsonify(value):
    if isinstance(value, QuerySet):
        return serialize("json", value)
    else:
        return value
