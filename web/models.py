from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from jdatetime import date,datetime
from django.contrib.auth.models import User

MONTH_CHOICES=[]
for i in range(len(date.j_months_short_en)):
    tup=(date.j_months_short_en[i],date.j_months_en[i])
    MONTH_CHOICES.append(tup)


class Stock(models.Model):
    def __str__(self):
        return '{}'.format(self.name)
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    group=models.CharField(max_length=255)
    url=models.CharField(max_length=255)



class StockError(models.Model):
    def __str__(self):
        return '{}'.format(self.url)
    url=models.CharField(max_length=255)
    

class Buy(models.Model):
    def __str__(self):
        return "{},{},{}".format(self.user,self.stock.name,self.price)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #name=models.CharField(max_length=255)
    stock=models.ForeignKey(Stock,on_delete=models.CASCADE)
    price=models.BigIntegerField()
    quantity=models.BigIntegerField()
    year=models.PositiveIntegerField(default=date.today().year)
    month=models.CharField(max_length=3,choices=MONTH_CHOICES,default=date.today().strftime("%b"))
    day=models.PositiveIntegerField(default=date.today().day,validators=[MaxValueValidator(31)])

class Sell(models.Model):
    def __str__(self):
        return "{},{}".format(self.stock.name,self.price)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #name=models.CharField(max_length=255)
    stock=models.ForeignKey(Stock,on_delete=models.CASCADE)
    price=models.BigIntegerField()
    quantity=models.BigIntegerField()
    year=models.PositiveIntegerField(default=date.today().year)
    month=models.CharField(max_length=3,choices=MONTH_CHOICES,default=date.today().strftime("%b"))
    day=models.PositiveIntegerField(default=date.today().day,validators=[MaxValueValidator(31)])

class Property(models.Model):
    def __str__(self):
        return "{},{},{}".format(self.user,self.stock.name,self.price)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    #description=models.CharField(max_length=255)
    #name=models.CharField(max_length=255)
    stock=models.ForeignKey(Stock,on_delete=models.CASCADE)
    price=models.BigIntegerField()
    quantity=models.BigIntegerField()


