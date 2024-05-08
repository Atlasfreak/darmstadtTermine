# Generated by Django 4.2.11 on 2024-05-07 00:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "darmstadt_termine",
            "0017_rename_appointment_type_appointment_appointment_types",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="appointment_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="appointments",
                to="darmstadt_termine.appointmenttype",
                verbose_name="Termintyp",
            ),
        ),
        migrations.AlterField(
            model_name="appointment",
            name="appointment_types",
            field=models.ManyToManyField(
                related_name="appointments_old",
                to="darmstadt_termine.appointmenttype",
                verbose_name="Termine",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="appointment",
            unique_together=set(),
        ),
    ]