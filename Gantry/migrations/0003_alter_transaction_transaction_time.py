# Generated by Django 4.2.4 on 2023-09-18 04:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Gantry', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
