# Generated by Django 3.0.8 on 2020-08-16 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0004_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp_user',
            name='code',
            field=models.CharField(default='', max_length=48),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temp_user',
            name='request_date',
            field=models.DateField(),
            preserve_default=False,
        ),
    ]