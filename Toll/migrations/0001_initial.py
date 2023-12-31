# Generated by Django 4.2.4 on 2023-11-08 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toll_name', models.CharField(max_length=30)),
                ('toll_location', models.CharField(max_length=30)),
                ('toll_price_collected', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
