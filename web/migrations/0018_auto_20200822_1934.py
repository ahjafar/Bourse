# Generated by Django 3.0.8 on 2020-08-22 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_auto_20200822_1926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocks',
            old_name='uel',
            new_name='url',
        ),
    ]