# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housepoints', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housepoints',
            name='datesubmitted',
        ),
        migrations.AlterField(
            model_name='housepoints',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
