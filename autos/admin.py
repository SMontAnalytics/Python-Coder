
from django.contrib import admin
from .models import Auto

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'anio', 'fecha_publicacion')
    list_filter = ('marca', 'anio')
    search_fields = ('marca', 'modelo', 'descripcion')

    