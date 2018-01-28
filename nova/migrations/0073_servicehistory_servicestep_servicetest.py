# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-01-23 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0072_delete_api'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.BigIntegerField(blank=True, null=True, verbose_name='item_id')),
                ('clock', models.BigIntegerField(verbose_name='\u65f6\u95f4')),
                ('value', models.IntegerField(verbose_name='\u72b6\u6001\u503c')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u670d\u52a1\u540d\u79f0')),
                ('content', models.CharField(max_length=2000, verbose_name='\u670d\u52a1\u5185\u5bb9')),
                ('timeout', models.CharField(default=b'15s', max_length=20, verbose_name='\u8d85\u65f6\u65f6\u95f4')),
                ('required_item', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u8fd4\u56de\u9879')),
                ('required', models.CharField(blank=True, max_length=64, null=True, verbose_name='\u8fd4\u56de\u503c')),
                ('status_codes', models.CharField(max_length=100, verbose_name='\u8fd4\u56de\u72b6\u6001\u7801')),
                ('step_field', models.CharField(blank=True, max_length=2000, null=True, verbose_name='\u8bf7\u6c42\u53c2\u6570')),
                ('step_type', models.CharField(blank=True, max_length=20, null=True, verbose_name='\u8bf7\u6c42\u7c7b\u578b')),
                ('item_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='item_id')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u670d\u52a1\u540d\u79f0')),
                ('result', models.IntegerField(blank=True, verbose_name='\u670d\u52a1\u7ed3\u679c')),
                ('last_check_time', models.DateTimeField(auto_now=True, null=True, verbose_name='\u4e0a\u6b21\u68c0\u67e5\u65f6\u95f4')),
                ('next_check_time', models.DateTimeField(auto_now=True, null=True, verbose_name='\u4e0b\u6b21\u68c0\u67e5\u65f6\u95f4')),
                ('comment', models.CharField(blank=True, max_length=50, verbose_name='\u8bf4\u660e')),
                ('item_id', models.CharField(max_length=20, verbose_name='item_id')),
            ],
        ),
    ]
