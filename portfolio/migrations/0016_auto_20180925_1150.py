# Generated by Django 2.1.1 on 2018-09-25 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_auto_20180109_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='engineerproduct',
            name='engineer_product_background_concept',
            field=models.TextField(blank=True, default='', max_length=30),
        ),
        migrations.AddField(
            model_name='engineerproduct',
            name='engineer_product_background_detail',
            field=models.TextField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='engineerproduct',
            name='engineer_product_creation_time',
            field=models.TextField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='engineerproduct',
            name='engineer_product_development_environment',
            field=models.TextField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='engineerproduct',
            name='engineer_product_development_language',
            field=models.TextField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='engineerproduct',
            name='engineer_product_feature_concept',
            field=models.TextField(blank=True, default='', max_length=30),
        ),
        migrations.AddField(
            model_name='engineerproduct',
            name='engineer_product_feature_detail',
            field=models.TextField(blank=True, default='', max_length=300),
        ),
    ]