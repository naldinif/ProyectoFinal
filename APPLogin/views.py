# APPLogin/views.py
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']  # Asegúrate de que el atributo 'name' coincida con el campo en tu formulario
        user = authenticate(request, username=email, password=email)
        print(f"Email ingresado: {email}")
        if user is not None:
            print("Usuario autenticado correctamente")
            login(request, user)
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('perfilusuario')
        else:
            print("Error en la autenticación")
            messages.error(request, 'Error en las credenciales de inicio de sesión.')
    return render(request, 'login.html')
