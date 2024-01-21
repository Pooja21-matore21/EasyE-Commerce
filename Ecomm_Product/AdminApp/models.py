from django.db import models

# Create your models here.

class Category(models.Model):
        cat_name = models.CharField(max_length=255)

        def __str__(self):
            return self.cat_name

class Meta:
    db_table = "Category"

class Product(models.Model):
    
    #id = models.CharField(max_length = 20, primary_key = True)
    product_name = models.CharField(max_length=255)
    shape = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    price = models.CharField(max_length=225)
    Img = models.ImageField(upload_to = "images",default="abc.jpg")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Meta:
    db_table = "Product"

class Recommendation(models.Model):
    prod_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Meta:
    db_table = "Recommendation"
