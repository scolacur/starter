# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20160222_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rotten_tomatoes_id',
            field=models.DecimalField(decimal_places=0, max_digits=255),
        ),
    ]