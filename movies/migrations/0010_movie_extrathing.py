# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_remove_movie_audience_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='extrathing',
            field=models.CharField(default='N/A', max_length=255),
        ),
    ]
