from django.contrib import admin

from .models import Product,Order,Client,Review


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Client)
admin.site.register(Review)

