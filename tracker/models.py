from django.db import models

# Create your models here.
class Homicide(models.Model):
    date = models.DateField()
    street = models.CharField(max_length=80)
    intersection = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=5)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()

class Article(models.Model):
    headline = models.CharField(max_length=250)
    homicide = models.ManyToManyField(Homicide)


