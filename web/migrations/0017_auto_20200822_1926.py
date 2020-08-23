# Generated by Django 3.0.8 on 2020-08-22 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_stocks'),
    ]

    operations = [
        migrations.CreateModel(
            name='StocksError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='stocks',
            name='uel',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]