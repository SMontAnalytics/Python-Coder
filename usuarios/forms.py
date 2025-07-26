# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import PerfilUsuario

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class UserEditForm(UserChangeForm):
    # Elimina el campo de password para no mostrarlo directamente aquí
    password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        # Si no quieres que se cambie el username directamente aquí, quítalo
        # fields = ['email', 'first_name', 'last_name']


class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['avatar', 'biografia']