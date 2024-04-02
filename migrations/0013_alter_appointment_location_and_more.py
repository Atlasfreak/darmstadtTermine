# Generated by Django 4.2.11 on 2024-04-02 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('darmstadtTermine', '0012_department_location_appointment_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='darmstadtTermine.location', verbose_name='Ort'),
        ),
        migrations.AlterField(
            model_name='appointmentcategory',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointment_categories', to='darmstadtTermine.department', verbose_name='Abteilung'),
        ),
        migrations.AlterField(
            model_name='appointmenttype',
            name='location',
            field=models.ManyToManyField(related_name='appointment_types', to='darmstadtTermine.location', verbose_name='Ort'),
        ),
    ]
