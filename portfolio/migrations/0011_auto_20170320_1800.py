# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_productdetail_product_creation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='product_creation_time',
            field=models.TextField(default='', max_length=100),
        ),
    ]