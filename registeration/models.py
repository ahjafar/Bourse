from django.db import models

# Create your models here.


class Temp_user(models.Model):
    def __str__(self):
        return self.username+self.email
    username=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    code=models.CharField(max_length=48)
    request_date=models.DateField()

class Password_reset(models.Model):
    def __str__(self):
        return str(self.request_date)
    email=models.EmailField()
    code=models.CharField(max_length=48)
    request_date=models.DateField()
    Is_ok=models.BooleanField(default=False)
    
