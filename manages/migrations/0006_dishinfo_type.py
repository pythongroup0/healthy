# Generated by Django 2.0.4 on 2018-05-06 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manages', '0005_auto_20180506_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='dishinfo',
            name='type',
            field=models.CharField(default='', max_length=20),
        ),
    ]