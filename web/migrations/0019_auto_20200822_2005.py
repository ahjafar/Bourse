# Generated by Django 3.0.8 on 2020-08-22 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_auto_20200822_1934'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Stocks',
            new_name='Stock',
        ),
        migrations.RenameModel(
            old_name='StocksError',
            new_name='StockError',
        ),
    ]
