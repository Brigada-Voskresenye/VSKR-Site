from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    print("ыфлдапотфыопыфпыво")