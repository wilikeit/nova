# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-01-19 10:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0071_api'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Api',
        ),
    ]
