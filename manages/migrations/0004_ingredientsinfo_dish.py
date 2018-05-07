# Generated by Django 2.0.4 on 2018-05-06 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manages', '0003_ingredientsinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredientsinfo',
            name='dish',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dish_id', to='manages.DishInfo'),
        ),
    ]