from django.contrib import admin

from .models import customer, state, city, order

admin.site.register(customer)
admin.site.register(state)
admin.site.register(city)
admin.site.register(order)

