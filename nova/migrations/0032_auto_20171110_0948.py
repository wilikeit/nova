# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-10 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0031_database'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sql',
            old_name='name',
            new_name='db_name',
        ),
        migrations.AddField(
            model_name='sql',
            name='submit_user',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='\u63d0\u4ea4\u4eba'),
        ),
    ]
