# Generated by Django 4.2.7 on 2023-11-09 03:28

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("darmstadt_termine", "0006_alter_appointment_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="last_sent",
            field=models.DateTimeField(
                default=datetime.datetime(
                    1970, 1, 1, 0, 0, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Zuletzt gesendet",
            ),
        ),
    ]