from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import UserCreate

class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()
    contraseña = forms.CharField(widget=forms.PasswordInput)
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)

class Meta:
    model = UserCreate
    fields = ['nombre', 'email', 'contraseña', 'confirmar_contraseña']



