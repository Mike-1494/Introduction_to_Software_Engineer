from django.db import models

# Create your models here.
class Clothes(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    brand = models.CharField(max_length=20)
    purchased = models.BigIntegerField()
    image = models.ImageField()

    
    def __str__(self):
        return self.name


class User(models.Model):
    display_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    email = models.CharField(max_length=60)
    Address = models.CharField(max_length= 100)

    def __str__(self):
        return self.display_name