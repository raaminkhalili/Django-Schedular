# Generated by Django 3.2.9 on 2021-11-25 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('tasks', '0002_task_pre_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
