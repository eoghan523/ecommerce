# orders/admin.py

from django.contrib import admin
from .models import Order 

# Register the Order model
admin.site.register(Order)
