# Generated by Django 4.2.4 on 2023-11-05 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Gantry', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='vehicle_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.vehicle'),
        ),
    ]
