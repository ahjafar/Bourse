# Generated by Django 3.0.8 on 2020-08-17 13:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20200816_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='day',
            field=models.PositiveIntegerField(default=27, validators=[django.core.validators.MaxValueValidator(31)]),
        ),
        migrations.AlterField(
            model_name='sell',
            name='day',
            field=models.PositiveIntegerField(default=27, validators=[django.core.validators.MaxValueValidator(31)]),
        ),
    ]
