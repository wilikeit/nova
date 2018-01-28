# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-09 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0030_sql'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('env', models.CharField(max_length=20, verbose_name='\u73af\u5883')),
                ('ip', models.CharField(max_length=20, verbose_name='ip')),
                ('port', models.CharField(max_length=20, verbose_name='\u7aef\u53e3')),
                ('db_name', models.CharField(max_length=20, verbose_name='\u6570\u636e\u5e93\u540d\u79f0')),
                ('username', models.CharField(max_length=20, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=20, verbose_name='\u5bc6\u7801')),
            ],
        ),
    ]
