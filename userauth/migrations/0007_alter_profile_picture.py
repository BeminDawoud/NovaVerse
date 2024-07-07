# Generated by Django 5.0.6 on 2024-07-07 12:01

import userauth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0006_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='img/default.jpg', null=True, upload_to=userauth.models.user_directory_path, verbose_name='profile-Picture'),
        ),
    ]