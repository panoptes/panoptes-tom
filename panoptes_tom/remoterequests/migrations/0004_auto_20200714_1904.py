# Generated by Django 3.0.8 on 2020-07-14 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remoterequests', '0003_auto_20200714_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
