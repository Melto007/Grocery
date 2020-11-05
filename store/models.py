from django.db import models
from datetime import datetime
from django.contrib.auth.models import auth,User

class Categories(models.Model):
    cat_name = models.CharField(max_length=100,null=True,blank=False)
    status = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.cat_name

class Cuisine(models.Model):
    cuisine_name = models.CharField(max_length=100,null=True,blank=True)
    status = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.cuisine_name

class Foods(models.Model):
    STATUS =(
        ('Vegetarian','Vegetarian'),
        ('Non-Vegetarian','Non-Vegetarian'),
        ('Other','Other'),
    )
    category_id = models.ForeignKey(Categories,null=True,on_delete=models.CASCADE)
    cuisine_id = models.ForeignKey(Cuisine,null=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,null=True,blank=True)
    preference = models.CharField(max_length=100,null=True,blank=True,choices=STATUS)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    discount = models.IntegerField(blank=True,null=True)
    image = models.ImageField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(blank=True,null=True)
    
    def __str__(self):
        return self.name

class Add_Cart(models.Model):
    food_id = models.ForeignKey(Foods,null=True,on_delete=models.SET_NULL)
    customer_id = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    food_price = models.DecimalField(max_digits=7,decimal_places=2)
    quantity = models.IntegerField(null=True,blank=True)
    status = models.IntegerField(null=True,blank=True)

class OrderItem(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    address = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    zipcode = models.IntegerField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100,null=True,blank=True,choices=STATUS)

class Contact(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    message = models.TextField()
    status = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

