from django.db import models

class Buy(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=255)
    price=models.BigIntegerField()
    date=models.DateTimeField()
