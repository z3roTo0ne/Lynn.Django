# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-14 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0003_auto_20160412_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u51fa\u7248'),
        ),
        migrations.AddField(
            model_name='historicalbook',
            name='published',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u51fa\u7248'),
        ),
    ]
