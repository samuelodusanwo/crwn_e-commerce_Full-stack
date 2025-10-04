from django.contrib import admin
from .models import Category, Product, Shop, Payment

admin.site.register(Shop)
admin.site.register(Payment)
admin.site.register(Category)
admin.site.register(Product)