from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_products, name='products'),
    path('<str:pk>/',views.getProduct,name="product"),
    path('create/', views.create_product, name='product-create'),
    path('update/<str:pk>/', views.update_product, name='product-update'),
    path('delete/<str:pk>/', views.delete_product, name='product-delete'),
]