# Generated by Django 3.1.5 on 2021-02-05 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210202_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='schedule_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
