from django.db import models
from datetime import datetime


class NonProfit(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    establishedDate = models.DateField()
    operatingBudget = models.CharField(max_length=200)
    numberOfEmployees = models.CharField(max_length=200)



    def __str__(self):
        return self.name