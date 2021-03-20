from django.db import models


# Create your models here.
class Fighter(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    club = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Payment(models.Model):
    #payer = models.ForeignKey(Fighter, on_delete=models.CASCADE)
    value = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

