# Generated by Django 3.2.25 on 2024-10-03 21:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0003_alter_table_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reservations',
            new_name='Reservation',
        ),
        migrations.AlterField(
            model_name='table',
            name='number',
            field=models.IntegerField(),
        ),
    ]
