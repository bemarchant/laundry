# Generated by Django 4.2.5 on 2023-10-03 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_neighbor_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbor',
            name='full_name',
        ),
    ]
