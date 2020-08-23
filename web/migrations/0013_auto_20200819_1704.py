# Generated by Django 3.0.8 on 2020-08-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20200819_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='month',
            field=models.CharField(choices=[('Far', 'Farvardin'), ('Ord', 'Ordibehesht'), ('Kho', 'Khordad'), ('Tir', 'Tir'), ('Mor', 'Mordad'), ('Sha', 'Shahrivar'), ('Meh', 'Mehr'), ('Aba', 'Aban'), ('Aza', 'Azar'), ('Dey', 'Dey'), ('Bah', 'Bahman'), ('Esf', 'Esfand')], default='Mor', max_length=3),
        ),
        migrations.AlterField(
            model_name='sell',
            name='month',
            field=models.CharField(choices=[('Far', 'Farvardin'), ('Ord', 'Ordibehesht'), ('Kho', 'Khordad'), ('Tir', 'Tir'), ('Mor', 'Mordad'), ('Sha', 'Shahrivar'), ('Meh', 'Mehr'), ('Aba', 'Aban'), ('Aza', 'Azar'), ('Dey', 'Dey'), ('Bah', 'Bahman'), ('Esf', 'Esfand')], default='Mor', max_length=3),
        ),
    ]
