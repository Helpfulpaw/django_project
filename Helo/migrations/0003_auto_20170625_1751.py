# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Helo', '0002_auto_20170625_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='TeamId',
            field=models.IntegerField(),
        ),
    ]
