from django.db import models
from AdminApp.models import Product


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=255,primary_key=True)
    password = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.CharField(max_length=25)

class Meta:
    db_table = "UserInfo"

class MyCart(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)

class Meta:
    db_table = "MyCart"

