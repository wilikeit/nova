# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-11 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0027_task_execute_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='comment',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='\u5907\u6ce8'),
        ),
    ]
