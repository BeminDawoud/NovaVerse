# Generated by Django 5.0.6 on 2024-07-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0002_profile_created_profile_first_name_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='url',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]