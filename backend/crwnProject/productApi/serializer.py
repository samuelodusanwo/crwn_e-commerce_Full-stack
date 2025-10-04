from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Category, Shop, Payment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.SlugRelatedField(slug_field="title", read_only=True, source="category")
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'imageUrl', 'price', 'description', 'title']
        

class NewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "image", "category", "description", "price", "shop"]

    
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id','title', 'image']


class CategoryOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title', 'imageUrl']
        
    
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ["id", "name", "phone_number", "logo"]
        

class GetShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ["id", "name"]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['quantity', 'product', 'total_price']
        read_only_field = ['total_price']