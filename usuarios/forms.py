
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
   
    password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
       

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['avatar', 'biografia']