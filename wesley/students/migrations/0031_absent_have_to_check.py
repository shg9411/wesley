# Generated by Django 3.0.3 on 2020-02-24 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0030_absent'),
    ]

    operations = [
        migrations.AddField(
            model_name='absent',
            name='have_to_check',
            field=models.BooleanField(default=False),
        ),
    ]