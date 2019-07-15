from django.db import models

class Article(models.Model):
    headline = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    sentiment = models.CharField(max_length=250, blank=True, default='NA')
    def __str__(self):
        return str(self.headline) + '->' + self.url

class Homicide(models.Model):
    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other or Unknown'),
    )
 
    date = models.DateField()
    time = models.TimeField(blank=True, default='01:00')
    street = models.CharField(max_length=80, blank=True, default='')
    intersection = models.CharField(max_length=120, blank=True, default='')
    zipcode = models.CharField(max_length=5, blank=True, default='')
    gender = models.CharField(max_length=1, choices=GENDERS, default='M')
    age = models.IntegerField(blank=True, default=0)
    name = models.CharField(max_length=80, blank=True, default='')
    count = models.IntegerField(blank=True, default=0)
    articles = models.ManyToManyField(Article, blank=True)

    def get_articles(self):
        return self.articles.all()

    def __str__(self):
        return str(self.date) + ' ' + self.street + ', Articles: ' + str(self.articles)

