from django.db import models

class Laptop (models.Model):
    brand = models.CharField(max_length=100)
    price= models.IntegerField()
    imei= models.CharField(max_length=100,unique=True)
    color= models.CharField(max_length=100)

    def __str__(self):
        return self.brand
