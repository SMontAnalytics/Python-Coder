
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_inicio, name='inicio'), 
    path('acerca-de/', views.acerca_de, name='acerca_de'), 
    path('autos/', views.AutoListView.as_view(), name='lista_autos'), 
    path('autos/<int:pk>/', views.AutoDetailView.as_view(), name='detalle_auto'), 
    path('autos/nuevo/', views.AutoCreateView.as_view(), name='crear_auto'),
    path('autos/<int:pk>/editar/', views.AutoUpdateView.as_view(), name='editar_auto'), 
    path('autos/<int:pk>/borrar/', views.AutoDeleteView.as_view(), name='borrar_auto'), 
]
