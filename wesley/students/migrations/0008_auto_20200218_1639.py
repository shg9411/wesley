# Generated by Django 3.0.3 on 2020-02-18 07:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20200218_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='time',
            field=models.TimeField(choices=[(datetime.time(15, 0), '3 PM')]),
        ),
    ]
