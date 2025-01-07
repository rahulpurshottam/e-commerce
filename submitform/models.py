from django.db import models

class contactEnquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    address2 = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=20)
    card_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiration = models.CharField(max_length=5)
    cvv = models.CharField(max_length=4)
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_charges = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)