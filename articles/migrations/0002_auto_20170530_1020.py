# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 10:20
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='canComment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='digest',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='ellipsisTitle',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='keywords',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='timeOfFirstComment',
            field=models.DateTimeField(default=timezone.now()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='timeOfLastComment',
            field=models.DateTimeField(default=timezone.now()),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='updateTime',
            field=models.DateTimeField(),
        ),
    ]