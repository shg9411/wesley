# Generated by Django 3.0.3 on 2020-03-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_temporary_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporary',
            name='did',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Absent',
        ),
    ]
