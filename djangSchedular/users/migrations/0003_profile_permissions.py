# Generated by Django 3.2.9 on 2021-11-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='permissions',
            field=models.BooleanField(default=True),
        ),
    ]
