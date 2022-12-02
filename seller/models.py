from django.db import models
from costomer.models import *

class category(models.Model):
    shop_category = models.CharField(max_length=50)
    def __str__(self):
        return self.shop_category

 
class seller_shop_details(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    shop_description = models.TextField(default="")
    phone_number = models.CharField(max_length=50)
    state = models.ForeignKey(state, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(city, on_delete=models.DO_NOTHING)
    zip_code = models.CharField(max_length=50)
    shop_address = models.CharField(max_length=100)
    shop_category =  models.CharField(max_length=50)
    seller_image = models.ImageField(upload_to="seller", blank=True , null = True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)


    def __str__(self):  
        return self.full_name

class products(models.Model):
    product_name = models.CharField(max_length=50)
    product_price  = models.IntegerField()
    shop_name = models.ForeignKey(seller_shop_details, on_delete=models.CASCADE)
    product_description =  models.TextField()
    product_image = models.ImageField(upload_to="product", blank = True , null = True)

    def __str__(self):
        return self.product_name