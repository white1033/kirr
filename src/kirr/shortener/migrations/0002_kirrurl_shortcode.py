# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 04:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(default='cdeshorturlcode', max_length=15, unique=True),
            preserve_default=False,
        ),
    ]
