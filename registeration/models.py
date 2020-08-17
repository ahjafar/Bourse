from django.db import models

# Create your models here.

# class User(models.Model):
#     def __str__(self):
#         return self.username,self.email
#     username=models.CharField(max_length=255)
#     email=models.EmailField()
#     password=models.CharField(max_length=255)

class Temp_user(models.Model):
    def __str__(self):
        return self.username+self.email
    username=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    code=models.CharField(max_length=48)
    request_date=models.DateField()