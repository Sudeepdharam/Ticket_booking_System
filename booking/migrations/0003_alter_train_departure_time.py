# Generated by Django 3.2.25 on 2024-05-23 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_train_departure_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='departure_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
