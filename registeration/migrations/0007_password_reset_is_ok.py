# Generated by Django 3.0.8 on 2020-08-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0006_password_reset'),
    ]

    operations = [
        migrations.AddField(
            model_name='password_reset',
            name='is_ok',
            field=models.BooleanField(default=False),
        ),
    ]