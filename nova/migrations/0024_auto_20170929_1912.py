# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-29 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0023_auto_20170926_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appconfig',
            name='files',
            field=models.CharField(max_length=300, verbose_name='\u914d\u7f6e\u6587\u4ef6'),
        ),
        migrations.AlterField(
            model_name='appconfig',
            name='svn_url',
            field=models.CharField(max_length=200, null=True, verbose_name='SVN\u8def\u5f84'),
        ),
    ]
