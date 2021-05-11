from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lastname = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, unique=True)