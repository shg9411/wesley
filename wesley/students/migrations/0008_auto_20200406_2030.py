# Generated by Django 3.0.5 on 2020-04-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_consulting_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulting',
            name='when_consult',
            field=models.DateField(auto_now=True),
        ),
    ]