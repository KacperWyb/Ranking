from django.db import models


# Create your models here.
class Fighter(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    club = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Payment(models.Model):
    fighter = models.ForeignKey(Fighter, on_delete=models.CASCADE)
    value = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

    def __str__(self):
        return f'ID {self.id}'
