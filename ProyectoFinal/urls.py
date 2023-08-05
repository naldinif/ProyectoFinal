# urls.py del proyecto
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('APPRegistro/', include('APPRegistro.urls')),
    path('APPLogin/', include('APPLogin.urls')), 
    path('APPPerfiles/', include('APPPerfiles.urls')), # Cambia esta línea
]
