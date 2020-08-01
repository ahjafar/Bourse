from django.db import models
from jdatetime import date,datetime

class Buy(models.Model):
    def __str__(self):
        return "{},{}".format(self.name,self.price)
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price=models.BigIntegerField()
    year=models.IntegerField(default=date.today().year)
    month=models.CharField(max_length=40,default=date.today().strftime("%B"))
    day=models.IntegerField(default=date.today().day)

class Sell(models.Model):
    def __str__(self):
        return "{},{}".format(self.name,self.price)
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price=models.BigIntegerField()
    year=models.IntegerField(default=date.today().year)
    month=models.CharField(max_length=40,default=date.today().strftime("%B"))
    day=models.IntegerField(default=date.today().day)
