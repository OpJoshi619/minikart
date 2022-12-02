from django.contrib import admin

from .models import category, seller_shop_details,products

admin.site.register(category)
admin.site.register(products)
admin.site.register(seller_shop_details)

