# Generated by Django 3.1.3 on 2020-11-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diseases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='slug',
            field=models.SlugField(default='qwe', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='pill',
            name='slug',
            field=models.SlugField(default='abs', max_length=255, unique=True),
        ),
    ]
