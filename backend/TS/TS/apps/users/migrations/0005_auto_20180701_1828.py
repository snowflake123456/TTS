# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-01 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180701_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='UserProFilebg/avatar/%y/%d/b67d8192cd6448ec96997f727c2a2e9f'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='background',
            field=models.ImageField(blank=True, default='/default/default.jpg', null=True, upload_to='UserProFilebg/%Y/%m/b67d8192cd6448ec96997f727c2a2e9f', verbose_name='背景图'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_bh',
            field=models.CharField(default='8eda1c37dfea4bbd9799217bd450fb56', max_length=50, unique=True, verbose_name='用户唯一ID'),
        ),
    ]
