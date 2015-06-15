from django.db import models
from django.contrib.postgres.fields import ArrayField

class Bookmark(models.Model):
    url = models.URLField(max_length=1000)
    title = models.CharField(max_length=200)
    tags =  ArrayField(models.CharField(max_length=100))