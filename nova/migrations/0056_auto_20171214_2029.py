# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-14 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0055_auto_20171214_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemid', models.BigIntegerField(max_length=50, verbose_name='\u670d\u52a1\u540d\u79f0')),
                ('clock', models.BigIntegerField(verbose_name='\u65f6\u95f4')),
                ('value', models.IntegerField(verbose_name='\u72b6\u6001\u503c')),
            ],
        ),
        migrations.AddField(
            model_name='httpstep',
            name='itemid',
            field=models.ManyToManyField(to='nova.History', verbose_name='itemid'),
        ),
    ]
