# Generated by Django 3.0.8 on 2020-08-01 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200801_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]