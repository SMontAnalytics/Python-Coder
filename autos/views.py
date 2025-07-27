
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q 
from .models import Auto
from .forms import AutoForm



def vista_inicio(request):
    """Vista de inicio del concesionario."""
    return render(request, 'autos/inicio.html', {'titulo': 'Bienvenido al Concesionario'})

def acerca_de(request):
    """Vista 'Acerca de mi' o 'About'."""
    return render(request, 'autos/acerca_de.html')

#  Vistas basadas en clases 

class AutoListView(ListView):
    """Vista de listado de autos."""
    model = Auto
    template_name = 'autos/lista_autos.html'
    context_object_name = 'autos' 
    paginate_by = 10 

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            
            queryset = queryset.filter(
                Q(marca__icontains=query) |
                Q(modelo__icontains=query) |
                Q(anio__icontains=query)
            ).distinct()
            if not queryset.exists():
                self.no_results_message = "No se encontraron autos con su búsqueda."
            else:
                self.no_results_message = None
        else:
            self.no_results_message = None 

        if not queryset.exists() and not query: 
             self.no_results_message = "Aún no hay autos registrados en nuestro concesionario."
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['no_results_message'] = getattr(self, 'no_results_message', None)
        return context


class AutoDetailView(DetailView):
    """Vista de detalle de un auto."""
    model = Auto
    template_name = 'autos/detalle_auto.html'
    context_object_name = 'auto'


class AutoCreateView(LoginRequiredMixin, CreateView):
    """Vista para crear un nuevo auto."""
    model = Auto
    form_class = AutoForm 
    template_name = 'autos/crear_auto.html'
    success_url = reverse_lazy('lista_autos') 
    


class AutoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Vista para editar un auto existente."""
    model = Auto
    form_class = AutoForm
    template_name = 'autos/editar_auto.html'
    context_object_name = 'auto'
    success_url = reverse_lazy('lista_autos')

   
    def test_func(self):
        
        return self.request.user.is_authenticated 


class AutoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Vista para borrar un auto."""
    model = Auto
    template_name = 'autos/borrar_auto.html' 
    success_url = reverse_lazy('lista_autos')

    
    def test_func(self):
       
        return self.request.user.is_authenticated