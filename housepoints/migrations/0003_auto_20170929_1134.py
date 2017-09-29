# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 09:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('housepoints', '0002_auto_20170929_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housepoints',
            name='firman',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Firman'),
        ),
        migrations.AlterField(
            model_name='housepoints',
            name='goodman',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Goodman'),
        ),
        migrations.AlterField(
            model_name='housepoints',
            name='pantlin',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Pantlin'),
        ),
    ]