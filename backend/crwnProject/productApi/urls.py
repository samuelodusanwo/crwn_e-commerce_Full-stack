from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.CreateListProduct.as_view(), name='create_product'),
    path('user/me/', views.LoggedInUser.as_view(), name='user_me'),
    path('category-only/', views.CategoryOnly.as_view(), name="category_only"),
    path('categories/', views.Categories.as_view(), name="categories"),
    path('collections/', views.ListCollections.as_view(), name='all_collections'),
    path('new-store/', views.ShopCreateView.as_view(), name='create_new_shop'),
    path('list-store/', views.ListShopView.as_view(), name='list_all_shop'),
    path('user/shop/', views.GetShopView.as_view(), name="user_shop"),
    path('product/create/', views.NewProductView.as_view(), name='new_product'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('productByShop/<int:pk>/', views.ProductByShop.as_view(), name="product_by_Shop"),
    path('category/<int:pk>/', views.ProductByCategory.as_view(), name="product_by_category"),
]