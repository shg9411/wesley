# Generated by Django 3.0.5 on 2020-04-07 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20200406_2030'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='school',
            unique_together={('name', 'grade')},
        ),
    ]