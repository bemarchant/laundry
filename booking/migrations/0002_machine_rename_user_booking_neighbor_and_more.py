# Generated by Django 4.2.5 on 2023-09-20 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1)),
            ],
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='user',
            new_name='neighbor',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='hour',
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(),
        ),
        migrations.DeleteModel(
            name='AvailableHour',
        ),
        migrations.DeleteModel(
            name='Date',
        ),
        migrations.AddField(
            model_name='booking',
            name='machine',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='booking.machine'),
        ),
    ]
