from django.contrib import admin
from products.models import Product
from products.models import Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_desc', 'product_price', 'product_image')

admin.site.register(Product,ProductAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_rev', 'stars','product_rate','review_des', 'product_image')

admin.site.register(Review,ReviewAdmin)


