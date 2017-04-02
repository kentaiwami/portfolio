# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20170324_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographerproduct',
            name='photographer_product_shooting_day',
            field=models.IntegerField(blank=True, default=31),
        ),
        migrations.AlterField(
            model_name='photographerproduct',
            name='photographer_product_shooting_hour',
            field=models.IntegerField(blank=True, default=12),
        ),
        migrations.AlterField(
            model_name='photographerproduct',
            name='photographer_product_shooting_minute',
            field=models.IntegerField(blank=True, default=59),
        ),
        migrations.AlterField(
            model_name='photographerproduct',
            name='photographer_product_shooting_month',
            field=models.IntegerField(blank=True, default=12),
        ),
    ]
