# Generated by Django 3.0.3 on 2020-02-17 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20200217_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='time',
            field=models.TimeField(default=datetime.datetime(2020, 2, 17, 19, 1, 46, 698039)),
        ),
    ]
