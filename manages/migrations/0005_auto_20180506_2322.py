# Generated by Django 2.0.4 on 2018-05-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manages', '0004_ingredientsinfo_dish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredientsinfo',
            name='dish',
        ),
        migrations.AddField(
            model_name='dishinfo',
            name='ingredients',
            field=models.ManyToManyField(to='manages.IngredientsInfo'),
        ),
    ]