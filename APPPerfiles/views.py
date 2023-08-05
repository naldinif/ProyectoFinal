# APPPerfiles/views.py
from django.shortcuts import render, redirect
from APPRegistro.models import Usuario

def busqueda_usuario(request):
    return render(request, 'busquedausuario.html')


def editar_usuario_desde_resultados(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)

    if request.method == 'POST':
        nuevo_nombre = request.POST.get('nombre')
        if nuevo_nombre:
            usuario.nombre = nuevo_nombre
            usuario.save()
            return redirect('resultadosbusqueda')

    return render(request, 'editarusuario.html', {'usuario': usuario})

    

def resultados_busqueda(request):
    nombre = request.GET.get('nombre', '')
    usuarios = Usuario.objects.filter(nombre__icontains=nombre)
    return render(request, 'resultadosbusqueda.html', {'usuarios': usuarios, 'nombre': nombre})



def eliminar_usuario_desde_resultados(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    
    if request.method == 'POST':
        usuario.delete()
        return redirect('resultadosbusqueda')
    
    return render(request, 'eliminarusuario.html', {'usuario': usuario})
