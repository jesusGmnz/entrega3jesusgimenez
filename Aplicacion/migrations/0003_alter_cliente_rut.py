# Generated by Django 4.2.5 on 2023-10-01 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicacion', '0002_alter_cliente_rut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.IntegerField(),
        ),
    ]
