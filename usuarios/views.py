
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserEditForm, PerfilUsuarioForm
from .models import PerfilUsuario
from django.contrib.auth.models import User

class CustomLoginView(LoginView):
    """Vista de login personalizada."""
    template_name = 'usuarios/login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True 

    def get_success_url(self):
        return reverse_lazy('perfil') 

class CustomLogoutView(LogoutView):
    """Vista de logout."""
    next_page = reverse_lazy('inicio') 

def registro(request):
    """Vista para el registro de nuevos usuarios."""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
           
            PerfilUsuario.objects.create(user=user)
            login(request, user) 
            return redirect('perfil') 
    else:
        form = UserRegisterForm()
    return render(request, 'usuarios/registro.html', {'form': form})

@login_required
def perfil(request):
    """Vista de perfil del usuario."""
    try:
        perfil_usuario = request.user.perfilusuario
    except PerfilUsuario.DoesNotExist:
        
        perfil_usuario = PerfilUsuario.objects.create(user=request.user)

    return render(request, 'usuarios/perfil.html', {'perfil_usuario': perfil_usuario})

class EditarPerfilView(LoginRequiredMixin, UpdateView):
    """Vista para editar los datos del usuario y su perfil."""
    model = User
    form_class = UserEditForm
    template_name = 'usuarios/editar_perfil.html'
    success_url = reverse_lazy('perfil') 

    def get_object(self, queryset=None):
        return self.request.user 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['perfil_form'] = PerfilUsuarioForm(self.request.POST, self.request.FILES, instance=self.request.user.perfilusuario)
        else:
            context['perfil_form'] = PerfilUsuarioForm(instance=self.request.user.perfilusuario)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        perfil_form = context['perfil_form']
        if perfil_form.is_valid():
            self.object = form.save() 
            perfil_form.save() 
            return super().form_valid(form)
        else:
            return self.form_invalid(form) 