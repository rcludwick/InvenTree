# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0017_auto_20180417_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitemtracking',
            name='system',
            field=models.BooleanField(default=False),
        ),
    ]