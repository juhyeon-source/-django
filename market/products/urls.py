from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    
]