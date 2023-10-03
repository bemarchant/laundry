# Generated by Django 4.2.5 on 2023-10-03 18:22

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_remove_neighbor_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuperNeighbor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('login.neighbor',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
