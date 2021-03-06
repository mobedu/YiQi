# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-03 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180702_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='UserProFilebg/avatar/%y/%d/fbe6eb8212be4b2db0127b287d1fd4d3'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='background',
            field=models.ImageField(blank=True, default='/default/default.jpg', null=True, upload_to='UserProFilebg/%Y/%m/fbe6eb8212be4b2db0127b287d1fd4d3', verbose_name='背景图'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('2', '女'), ('1', '男')], default='1', max_length=10, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_bh',
            field=models.CharField(default='fedfde98805943349ac97d3e328cfdf5', max_length=50, unique=True, verbose_name='用户唯一ID'),
        ),
    ]
