from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('products/', views.product_list, name='product-list'),
    path('pricing/', views.pricing, name='pricing-discounts'),
    path('orders/', views.orders, name='orders'),
    path('customers/', views.customers, name='customers'),
    path('marketing/', views.marketing, name='marketing'),
    path('omnichannel/', views.omnichannel, name='omnichannel'),
    path('events/', views.events, name='events'),
    path('reports/', views.reports, name='reports'),
    path('edit/<int:pk>/', views.edit_product, name='edit-product'),
    path('delete/<int:pk>/', views.delete_product, name='delete-product'),
    path('shop/', views.customer_view, name='customer-view'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove-from-cart'),
]
