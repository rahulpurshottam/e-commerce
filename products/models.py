from django.db import models
from tinymce.models import HTMLField

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_desc = HTMLField() 
    product_price = models.FloatField(max_length=10) 
    product_image = models.ImageField(upload_to='product_images/')

class Review(models.Model):
    product_name = models.CharField(max_length=50)
    product_rev = models.CharField(max_length=100)
    stars = models.CharField(max_length=10) 
    product_rate = models.FloatField(max_length=10) 
    review_des= HTMLField() 
    product_image = models.ImageField(upload_to='review_images/')

