# Generated by Django 3.0.3 on 2020-02-19 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0025_auto_20200219_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problem', to='students.Student'),
        ),
    ]