# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 05:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_auto_20170322_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Product'),
        ),
    ]
