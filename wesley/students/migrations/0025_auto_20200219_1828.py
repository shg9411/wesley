# Generated by Django 3.0.3 on 2020-02-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0024_auto_20200219_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]