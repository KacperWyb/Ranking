from django.db import models


# Create your models here.
class Fighter(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    club = models.CharField(max_length=100)


class Payment(models.Model):
    value = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
