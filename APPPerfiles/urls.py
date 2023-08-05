# APPPerfiles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('buscarperfiles/', views.busqueda_usuario, name='busquedausuario'),
    path('resultados/', views.resultados_busqueda, name='resultadosbusqueda'),
    path('editarusuarioresultados/<int:usuario_id>/', views.editar_usuario_desde_resultados, name='editarusuariodesderesultados'),
    path('eliminarusuarioresultados/<int:usuario_id>/', views.eliminar_usuario_desde_resultados, name='eliminarusuariodesderesultados'),
]
