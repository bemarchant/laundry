# Generated by Django 4.2.5 on 2023-10-02 21:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_apartment_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]