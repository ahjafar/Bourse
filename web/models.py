from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from jdatetime import date,datetime

class Buy(models.Model):
    def __str__(self):
        return "{},{}".format(self.name,self.price)
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price=models.BigIntegerField()
    number=models.BigIntegerField()
    year=models.PositiveIntegerField(default=date.today().year)
    month=models.CharField(max_length=40,default=date.today().strftime("%B"))
    day=models.PositiveIntegerField(default=date.today().day,validators=[MaxValueValidator(31)])

class Sell(models.Model):
    def __str__(self):
        return "{},{}".format(self.name,self.price)
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price=models.BigIntegerField()
    number=models.BigIntegerField()
    year=models.PositiveIntegerField(default=date.today().year)
    month=models.CharField(max_length=40,default=date.today().strftime("%B"))
    day=models.PositiveIntegerField(default=date.today().day,validators=[MaxValueValidator(31)])
