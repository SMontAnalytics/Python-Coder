
from django.db import models
from django.utils import timezone

class Auto(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField() 
    imagen = models.ImageField(upload_to='autos_imagenes/')
    fecha_publicacion = models.DateField(default=timezone.now)
    descripcion = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"
    