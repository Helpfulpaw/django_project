# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helo', '0004_remove_team_teamid'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='TeamId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
