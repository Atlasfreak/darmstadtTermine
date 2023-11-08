# Generated by Django 4.2.7 on 2023-11-08 22:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("darmstadtTermine", "0005_alter_notification_token_selector_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="appointment",
            options={"verbose_name": "Termin", "verbose_name_plural": "Termine"},
        ),
        migrations.AlterModelOptions(
            name="appointmentcategory",
            options={
                "verbose_name": "Anliegenkategorie",
                "verbose_name_plural": "Anliegenkategorien",
            },
        ),
        migrations.AlterModelOptions(
            name="appointmenttype",
            options={"verbose_name": "Anliegen", "verbose_name_plural": "Anliegen"},
        ),
        migrations.AlterModelOptions(
            name="notification",
            options={
                "verbose_name": "Benachrichtigung",
                "verbose_name_plural": "Benachrichtigungen",
            },
        ),
        migrations.AlterField(
            model_name="notification",
            name="appointment_type",
            field=models.ManyToManyField(
                blank=True,
                related_name="notifications",
                to="darmstadtTermine.appointmenttype",
                verbose_name="Anliegen",
            ),
        ),
        migrations.AlterField(
            model_name="notification",
            name="last_sent",
            field=models.DateTimeField(
                default=datetime.datetime(1, 1, 1, 0, 0),
                verbose_name="Zuletzt gesendet",
            ),
        ),
    ]
