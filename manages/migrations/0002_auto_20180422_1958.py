# Generated by Django 2.0.4 on 2018-04-22 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishinfo',
            name='dishEnergy',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='dishinfo',
            name='dishPrice',
            field=models.FloatField(),
        ),
    ]
