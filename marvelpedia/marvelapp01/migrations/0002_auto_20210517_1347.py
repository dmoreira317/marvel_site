# Generated by Django 3.2 on 2021-05-17 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marvelapp01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
