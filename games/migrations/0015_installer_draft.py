# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0014_auto_20161002_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='installer',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
