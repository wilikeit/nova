# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-14 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0057_auto_20171214_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='itemid',
            field=models.BigIntegerField(verbose_name='\u670d\u52a1\u540d\u79f0'),
        ),
    ]
