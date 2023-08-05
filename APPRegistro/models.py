from django.db import models
from django.contrib.auth.hashers import make_password

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=128, default='default_hashed_password')  # Establece un valor predeterminado seguro

    def save(self, *args, **kwargs):
        if not self.id:  # Solo aplicamos el hash si es un nuevo usuario
            self.password = make_password(self.password)  # Aplicamos el hash a la contraseña antes de guardarla
        super(Usuario, self).save(*args, **kwargs)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"
