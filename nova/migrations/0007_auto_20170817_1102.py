# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-17 03:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0006_auto_20170817_1100'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='apps',
            new_name='App',
        ),
    ]
