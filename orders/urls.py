from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),        # For listing all orders
    path('create/', views.order_create, name='order_create'),  # For creating a new order
    path('edit/<int:pk>/', views.order_edit, name='order_edit'),  # For editing an order by ID 
    path('delete/<int:pk>/', views.order_delete, name='order_delete'),  # For deleting an order by ID 
]