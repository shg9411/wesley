# Generated by Django 3.0.3 on 2020-02-19 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_auto_20200219_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='days_of_week',
            field=models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday')], max_length=10),
        ),
    ]
