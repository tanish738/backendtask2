from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('login/', views.loginpage,name="login"),
    path('register/', views.register,name="register"),
    path('products/', views.products,name="products"),
    path('productscreate/', views.products_create,name="products_create"),
    path('customer/<str:pk>/', views.customer,name="customer"),
    path('createorder/<str:pk>/',views.createOrder,name="create_order"),
    path('updateorder/<str:pk>/',views.updateOrder,name="update_order"),
    path('deleteorder/<str:pk>/',views.deleteOrder,name="delete_order"),
    path('customerlist/',views.CustomerList.as_view(),name="customer_list"),
    path('customerlists/',views.SnippetList.as_view(),name="customer_lists"),
    path('customerdetail/<str:pk>/',views.CustomerDetail.as_view(),name="customer_detail"),
]