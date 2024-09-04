from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=10000000)
    date_created = models.DateField(default=datetime.now, blank=True)