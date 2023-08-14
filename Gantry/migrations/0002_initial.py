# Generated by Django 4.2.4 on 2023-08-14 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('Gantry', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.profile'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='vehicle_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.vehicles'),
        ),
    ]