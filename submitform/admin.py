from django.contrib import admin
from .models import contactEnquiry
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'first_name', 'last_name', 'email', 'country', 'state', 
        'zip_code', 'product_name', 'product_price'
    )
    search_fields = ('first_name', 'last_name', 'email', 'product_name')
    list_filter = ('country', 'state', 'payment_method')

@admin.register(contactEnquiry)
class ContactEnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message', 'id')
