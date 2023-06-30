from django.db import models
from django.contrib.auth.forms import UserCreationForm

class UserCreate(UserCreationForm):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    contraseña = models.CharField(max_length=10)
    confirmar_contraseña = models.CharField(max_length=10)
    
    def __str__(self):
        return self.nombre