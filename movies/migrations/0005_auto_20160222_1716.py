# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_remove_movie_theatre_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='movie',
            name='theatre_release_date',
            field=models.DateField(null=True),
        ),
    ]
