# Generated by Django 3.0.3 on 2020-02-19 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0016_auto_20200219_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='days_of_week',
            field=models.CharField(choices=[('monday', 5), ('tuesday', 4), ('wednesday', 3), ('thursday', 2), ('friday', 1)], max_length=10),
        ),
    ]
