from django.shortcuts import render, redirect
from APPRegistro.models import Usuario
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        try:
            usuario = Usuario.objects.get(nombre=nombre)
            if usuario:
                request.session['user_id'] = usuario.id  # Almacena el ID del usuario en la sesión
                return redirect('dashboard')  # Redirige a la página del panel de control
            else:
                error_message = "Autenticación fallida."
                return render(request, 'login.html', {'error_message': error_message})
        except Usuario.DoesNotExist:
            error_message = "Nombre no encontrado. Verifique que el nombre ingresado corresponda con el registrado"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def dashboard_view(request):
    user_id = request.session.get('user_id')
    usuario = Usuario.objects.get(id=user_id)
    return render(request, 'dashboard.html', {'usuario': usuario})