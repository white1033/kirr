# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20161217_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]