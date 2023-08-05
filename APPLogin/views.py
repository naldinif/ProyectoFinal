from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from APPLogin.forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            print(f"Email ingresado: {email}")  # Agrega este print statement
            if user is not None:
                login(request, user)
                return redirect('inicio_exitoso')
            else:
                error_msg = "Credenciales inválidas. Inténtalo de nuevo."
                return render(request, 'login.html', {'form': form, 'error_msg': error_msg})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def inicio_exitoso_view(request):
    return render(request, 'inicio_exitoso.html')
