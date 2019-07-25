from django.db import models

class Article(models.Model):
    url = models.CharField(max_length=250)
    headline = models.CharField(max_length=250)
    content = models.TextField(blank=True, default='')
    sentiment = models.CharField(max_length=250, blank=True, default='NA')
    def __str__(self):
        return str(self.headline) + '->' + self.url

class Homicide(models.Model):
    GENDERS = (        ('F', 'Female'),  ('M', 'Male'),('O', 'Other or Unknown'),    )
    MOTIVES = (        ('D', 'Dispute'), ('G', 'Gang'),('F', 'Family/Domestic'), ('R','Robbery'),('O', 'Other or Unknown'),    )
    MEANS = (          ('S', 'Stabbing'),('G', 'Gun'), ('O', 'Other or Unknown'),    )
    ETHNICITIES = (    ('A','Asian'),    ('W','White'),('B','Black'), ('H','Hispanic'),('O','Other or Unknown'), )
    LOCATIONS = (      ('H', 'Home'),    ('C', 'Car'), ('S', 'Street'), ('O','Other/Unknown'),    )

    date = models.DateField()
    time = models.TimeField(blank=True, default='01:00')
    street = models.CharField(max_length=80, blank=True, default='')
    intersection = models.CharField(max_length=120, blank=True, default='')
    mapiframe = models.TextField(blank=True, default='')
    gender = models.CharField(max_length=1, choices=GENDERS, default='O')
    age = models.IntegerField(blank=True, default=0)
    name = models.CharField(max_length=80, blank=True, default='')
    ethnicity = models.CharField(max_length=1, choices=ETHNICITIES, default='O')
    motive = models.CharField(max_length=1, choices=MOTIVES, default='O')
    means = models.CharField(max_length=1, choices=MEANS, default='O')
    count = models.IntegerField(blank=True, default=0)
    killergender = models.CharField(max_length=1, choices=GENDERS, default='O')
    killerage = models.IntegerField(blank=True, default=0)
    killername = models.CharField(max_length=80, blank=True, default='')
    killerethnicity = models.CharField(max_length=1, choices=ETHNICITIES, default='O')
    location = models.CharField(max_length=1, choices=LOCATIONS, default='O')
    articles = models.ManyToManyField(Article, blank=True)

    def get_articles(self):
        return self.articles.all()

    def __str__(self):
        return str(self.date) + ' ' + self.street + ' age:' + str(self.age) + ' seq#:'+str(self.count)

