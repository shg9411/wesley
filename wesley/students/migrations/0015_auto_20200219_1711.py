# Generated by Django 3.0.3 on 2020-02-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_auto_20200219_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='days_of_week',
            field=models.CharField(choices=[(5, 'Monday'), (4, 'Tuesday'), (3, 'Wednesday'), (2, 'Thursday'), (1, 'Friday')], max_length=10),
        ),
    ]
