from django.contrib import admin
from .models import Restaurant, Product, Order, OrderItem, Review

admin.site.register(Restaurant)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
