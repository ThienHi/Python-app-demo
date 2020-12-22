from django.db import models

# Create your models here.


class ListVideo(models.Model):
    url = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    content = models.CharField(max_length=100)
    creator = models.CharField(max_length=30)
