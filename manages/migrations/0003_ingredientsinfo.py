# Generated by Django 2.0.4 on 2018-04-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manages', '0002_auto_20180422_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredientsName', models.CharField(max_length=40)),
                ('water', models.FloatField(default=0.0)),
                ('energy', models.IntegerField(default=0)),
                ('protein', models.FloatField(default=0.0)),
                ('fat', models.FloatField(default=0.0)),
                ('saccharides', models.FloatField(default=0.0)),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
    ]
