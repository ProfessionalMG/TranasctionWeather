# Create your models here.
from django.db import models


class Weather(models.Model):
    address = models.CharField(max_length=255)
    date = models.DateField()
    feels_like = models.IntegerField()

    def __str__(self):
        return f'{self.address} on {self.date}'


class Keys(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)

    def __str__(self):
        return self.name
