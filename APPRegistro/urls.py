from django.urls import path
from . import views

urlpatterns = [
    # Otras URL patterns si las tienes...
    path('inicio/', views.inicio, name='inicio'),  # Agrega una barra al final de 'inicio'
    path('signup/', views.signup, name='signup'),  # Cambia 'Signup' a 'signup'
    path('about/', views.about, name='about'),  # Agrega una barra al final de 'about'
]
