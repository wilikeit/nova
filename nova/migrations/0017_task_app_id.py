# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-01 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0016_auto_20170830_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='app_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='app_id'),
        ),
    ]
