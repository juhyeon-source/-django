from django.contrib import admin
from django.urls import path
from django.urls.conf import include

app_name = 'products'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls'))
]
