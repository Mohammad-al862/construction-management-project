# Generated by Django 5.1.2 on 2024-10-29 07:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.supervisor'),
        ),
        migrations.AddField(
            model_name='task',
            name='estimated_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='task_picture',
            field=models.ImageField(default='exit', upload_to='tasks/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='workers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]