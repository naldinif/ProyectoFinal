from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('inicio_exitoso/', views.inicio_exitoso_view, name='inicio_exitoso'),
]
