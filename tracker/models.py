from django.db import models

class Article(models.Model):
    headline = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    sentiment = models.CharField(max_length=250, blank=True, default='NA')
    def __str__(self):
        return str(self.headline) + '->' + self.url

class Homicide(models.Model):
    GENDERS = (        ('F', 'Female'),('M', 'Male'),('U', 'Other or Unknown'),    )
    MOTIVES = (        ('D', 'Dispute'),('G', 'Gang'),('F', 'Family/Domestic'), ('O', 'Other or Unknown'),    )
    MEANS = (        ('S', 'Stabbing'),('G', 'Gun'),('O', 'Other or Unknown'),    )
    SOLVED = (('S','Solved'),('U','Unsolved'),)
    ETHNICITIES = (('A','Asian'),('W','White'),('B','Black'),('H','Hispanic'),('O','Other'),('U','Unknown'), )
 
    date = models.DateField()
    time = models.TimeField(blank=True, default='01:00')
    street = models.CharField(max_length=80, blank=True, default='')
    intersection = models.CharField(max_length=120, blank=True, default='')
    maplink = models.CharField(max_length=180, blank=True, default='')
    mapiframe = models.TextField(blank=True, default='')
    zipcode = models.CharField(max_length=5, blank=True, default='')
    gender = models.CharField(max_length=1, choices=GENDERS, default='M')
    age = models.IntegerField(blank=True, default=0)
    name = models.CharField(max_length=80, blank=True, default='')
    ethnicity = models.CharField(max_length=80, choices=ETHNICITIES, default='U')
    motive = models.CharField(max_length=1, choices=MOTIVES, default='O')
    means = models.CharField(max_length=1, choices=MEANS, default='O')
    solved = models.CharField(max_length=1, choices=SOLVED, default='N')
    count = models.IntegerField(blank=True, default=0)
    killergender = models.CharField(max_length=1, choices=GENDERS, default='U')
    killerage = models.IntegerField(blank=True, default=0)
    killername = models.CharField(max_length=80, blank=True, default='')
    killerethnicity = models.CharField(max_length=80, choices=ETHNICITIES, default='U')
    articles = models.ManyToManyField(Article, blank=True)

    def get_articles(self):
        return self.articles.all()

    def __str__(self):
        return str(self.date) + ' ' + self.street + ', Articles: ' + str(self.articles)

