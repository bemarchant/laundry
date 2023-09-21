# Generated by Django 4.2.5 on 2023-09-21 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_booking_slot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='slot',
        ),
        migrations.AlterField(
            model_name='booking',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.machine'),
        ),
    ]
