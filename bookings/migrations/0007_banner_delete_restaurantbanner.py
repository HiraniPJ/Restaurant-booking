# Generated by Django 5.1.1 on 2024-10-09 19:01

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_remove_restaurantbanner_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('banner_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
            ],
        ),
        migrations.DeleteModel(
            name='RestaurantBanner',
        ),
    ]
