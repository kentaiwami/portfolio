# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_auto_20170316_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='add_date',
            field=models.DateTimeField(blank=True, verbose_name='date published'),
        ),
    ]