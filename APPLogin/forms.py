# en APPLogin/forms.py
from django import forms


class LoginForm(forms.Form):
    nombre = forms.CharField(max_length=30)  # Campo para el nombre del usuario
    apellido = forms.CharField(max_length=40)
    email = forms.EmailField()  # Campo para el correo electrónico del usuario
    password = forms.CharField(widget=forms.PasswordInput)  # Campo para la contraseña del usuario

