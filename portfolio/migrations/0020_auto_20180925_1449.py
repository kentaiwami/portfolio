# Generated by Django 2.1.1 on 2018-09-25 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0019_photographerproduct_shooting_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographerproduct',
            name='shooting_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]