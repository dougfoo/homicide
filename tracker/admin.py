from django.contrib import admin

# Register your models here.
from .models import Homicide, Article

admin.site.register(Homicide)
admin.site.register(Article)