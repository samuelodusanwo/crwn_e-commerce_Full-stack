from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=50)
    # imageUrl = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='categoryImages/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    

class Shop(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shop')
    logo = models.ImageField(upload_to='storeLogos/', default="storeLogos/default-img")
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='productImages/', null=True, blank=True)
    imageUrl = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    
    def __str__(self):
        return self.name if self.name else f"Product id - {self.id}"
    

class Payment(models.Model):
    quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    
    def __str__(self):
        return f"{self.product.name} X {self.quantity} (PRODUCT ID: {self.product.id})"