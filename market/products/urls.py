from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/like/', views.like, name='like'),
    
]