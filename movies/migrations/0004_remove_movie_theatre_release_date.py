# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 17:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_movie_synopsis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='theatre_release_date',
        ),
    ]
