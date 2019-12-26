from django.db import models

# Create your models here.
class Count(models.Model):
    people = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 255)