# Generated by Django 3.2 on 2021-05-20 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marvelapp01', '0008_alter_newuser_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='password1',
        ),
    ]