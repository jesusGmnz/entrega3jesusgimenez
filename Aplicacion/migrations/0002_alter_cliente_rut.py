# Generated by Django 4.2.5 on 2023-10-01 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.IntegerField(max_length=10),
        ),
    ]
