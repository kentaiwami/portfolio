# Generated by Django 2.1.1 on 2018-09-26 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_auto_20180925_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_id', models.IntegerField(default=0, unique=True)),
                ('information', models.TextField(blank=True, default='', max_length=1000)),
                ('usage', models.TextField(blank=True, default='', max_length=1000)),
                ('engineer_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.EngineerProduct')),
            ],
        ),
    ]