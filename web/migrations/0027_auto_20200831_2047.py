# Generated by Django 3.0.8 on 2020-08-31 16:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0026_delete_teat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='day',
            field=models.PositiveIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(31)]),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='day',
            field=models.PositiveIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(31)]),
        ),
        migrations.AlterField(
            model_name='sell',
            name='day',
            field=models.PositiveIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(31)]),
        ),
        migrations.CreateModel(
            name='Withdraw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('year', models.PositiveIntegerField(default=1399)),
                ('month', models.CharField(choices=[('Far', 'Farvardin'), ('Ord', 'Ordibehesht'), ('Kho', 'Khordad'), ('Tir', 'Tir'), ('Mor', 'Mordad'), ('Sha', 'Shahrivar'), ('Meh', 'Mehr'), ('Aba', 'Aban'), ('Aza', 'Azar'), ('Dey', 'Dey'), ('Bah', 'Bahman'), ('Esf', 'Esfand')], default='Sha', max_length=3)),
                ('day', models.PositiveIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(31)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
