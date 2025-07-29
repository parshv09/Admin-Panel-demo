from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('edit/<int:pk>/', views.edit_product, name='edit-product'),
    path('delete/<int:pk>/', views.delete_product, name='delete-product'),
]
