# Generated by Django 2.0.13 on 2019-04-18 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutters', '0003_remove_cutter_job_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='cutter',
            name='job_no',
            field=models.IntegerField(default=0),
        ),
    ]
