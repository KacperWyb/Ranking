from django.db import models


# Create your models here.
class Fighter(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    club = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Payment(models.Model):
    payer1 = models.CharField(max_length=30)
    payer = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    def __str__(self):
        return f'ID {self.id}'
