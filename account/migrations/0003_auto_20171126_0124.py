# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20171126_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='last_updated',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='time_created',
            field=models.DateTimeField(),
        ),
    ]
