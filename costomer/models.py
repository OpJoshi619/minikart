
from django.db import models
from django.db.models.fields.files import FileField

class state(models.Model):
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name 

class city(models.Model):
    city_name = models.CharField(max_length=50)
    state_id = models.ForeignKey(state, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name

class customer(models.Model): 
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    costomer_img = models.ImageField(upload_to="costomer", blank=True , null = True)
    state = models.ForeignKey(state,on_delete=models.DO_NOTHING)
    city = models.ForeignKey(city,on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=50)
    land_mark = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

 
class order(models.Model):
    
    quantity = models.IntegerField(default=0)
    delivery_address = models.CharField(max_length=100)
    costomer_name = models.CharField(max_length=50)
    costomer_phone_number = models.CharField(max_length=50)
    seller_name = models.CharField(max_length=50)
    seller_phone_number = models.CharField(max_length=50, default="")
    product_price = models.IntegerField(default=0)
    order_price = models.IntegerField(default=0) 
    order_date_time = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.costomer_name  

