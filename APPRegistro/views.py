# en APPRegistro/views.py
from django.http import HttpResponse
from django.shortcuts import render
from APPRegistro.models import Usuario
from APPRegistro.forms import Signup

def inicio(request):
    return render(request, 'inicio.html')

def signup(request):
    if request.method == 'POST':
        miFormulario = Signup(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion['nombre']
            apellido = informacion.get('apellido', '')
            email = informacion['email']
            password = informacion['password']  # Agrega el campo de contraseña

            usuario = Usuario(nombre=nombre, apellido=apellido, email=email, password=password)  # Incluye el campo de contraseña al crear el objeto Usuario
            usuario.save()
            return render(request, 'inicio.html')

    else:
        miFormulario = Signup()

    return render(request, 'signup.html', {'miFormulario': miFormulario})

def about(request):
    return render(request, 'about.html')
