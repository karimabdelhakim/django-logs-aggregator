# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-11 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0004_auto_20181011_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='server_name',
            field=models.SlugField(),
        ),
    ]
