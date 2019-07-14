from django.db import models

# Create your models here.
class Homicide(models.Model):
    date = models.DateField()
    time = models.TimeField(blank=True, default='01:00')
    street = models.CharField(max_length=80, blank=True, default='')
    intersection = models.CharField(max_length=120, blank=True, default='')
    zipcode = models.CharField(max_length=5, blank=True, default='')
    gender = models.CharField(max_length=5, blank=True, default='M')
    age = models.IntegerField(blank=True, default=0)

class Article(models.Model):
    headline = models.CharField(max_length=250)
    homicide = models.ManyToManyField(Homicide)


