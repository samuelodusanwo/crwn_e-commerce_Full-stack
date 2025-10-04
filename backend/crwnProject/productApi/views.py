from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category, Payment, Shop
from .serializer import UserSerializer, CategorySerializer, CategoryOnlySerializer, ProductSerializer, PaymentSerializer, NewProductSerializer, ShopSerializer, GetShopSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny


# function for creating of users
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
  

# fetching logged in user
class LoggedInUser(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


# create Shop
class ShopCreateView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# List all shop
class ListShopView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [AllowAny]


# creating of product
class CreateListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    

# list all products
class ListCollections(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


# listing only categories
class CategoryOnly(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryOnlySerializer
    permission_classes = [AllowAny]


# listing all category
class Categories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


# products by category
class ProductByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        category_id = self.kwargs['pk']
        return Product.objects.filter(category__id=category_id)


# products by store
class ProductByShop(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self):
        store_id = self.kwargs['pk']
        return Product.objects.filter(shop__id=store_id)


# Creating of new product
class NewProductView(generics.CreateAPIView):
    serializer_class = NewProductSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('.......', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# fetch user shop
class GetShopView(generics.ListAPIView):
    serializer_class = GetShopSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Shop.objects.filter(user=user)


# payment views
class PaymentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user = request.user
        items = request.data.get('items', [])
        
        for item in items:
            product = Product.objects.get(id=item['product'])
            quantity = item['quantity']
            total_price = product.price * quantity
            
            Payment.objects.create(
                user=user,
                quantity=quantity,
                product=product,
                total_price=total_price
            )
        
        return Response({"Message" : "Payment successful"}, status=201)