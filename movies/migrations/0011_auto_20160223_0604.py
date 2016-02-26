# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_movie_extrathing'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='audience_score',
            field=models.IntegerField(default='-1'),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.CharField(default='#', max_length=255),
        ),
    ]