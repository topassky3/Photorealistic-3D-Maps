# core/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Anunciate(AbstractUser):
    nombre_completo = models.CharField(max_length=150, verbose_name="Nombre Completo")
    telefono = models.CharField(max_length=20, verbose_name="Número de Teléfono")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Puedes ajustar esto según tus necesidades

    def __str__(self):
        return self.email

class Anuncio(models.Model):
    titulo = models.CharField(max_length=255, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    imagen = models.ImageField(upload_to='anuncios/', verbose_name="Imagen del Anuncio")
    enlace = models.URLField(verbose_name="Enlace del Anuncio")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    # Campos adicionales para datos de Places Insights (opcional)
    tipo_lugar = models.CharField(max_length=100, verbose_name="Tipo de Lugar")
    nivel_precio = models.CharField(max_length=50, verbose_name="Nivel de Precio")
    calificacion = models.FloatField(verbose_name="Calificación")
    area_interes = models.CharField(max_length=255, verbose_name="Área de Interés")
    radio = models.IntegerField(verbose_name="Radio (km)")

    # Campos para ubicación
    latitud = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitud", null=True, blank=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitud", null=True, blank=True)

    # Nuevo campo para el modelo 3D
    modelo_3d = models.FileField(
        upload_to='modelos_3d/',
        null=True,
        blank=True,
        verbose_name="Modelo 3D (glTF)"
    )

    usuario_creador = models.ForeignKey(Anunciate, on_delete=models.CASCADE, related_name='anuncios')

    def __str__(self):
        return self.titulo
