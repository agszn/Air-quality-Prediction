# Generated by Django 5.0.3 on 2024-05-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AirPollution", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AirQuality",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("District", models.CharField(max_length=100)),
                ("CO", models.FloatField()),
                ("NMHC", models.FloatField()),
                ("C6H6", models.FloatField()),
                ("NO2", models.FloatField()),
                ("temp", models.FloatField()),
                ("humidity", models.FloatField()),
            ],
        ),
    ]