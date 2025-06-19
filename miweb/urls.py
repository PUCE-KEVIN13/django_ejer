# miweb/urls.py

from django.contrib import admin
from django.urls import path, include  # <- include es la clave

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientes.urls')),  # <- NO usar "from clientes import urls"
]

