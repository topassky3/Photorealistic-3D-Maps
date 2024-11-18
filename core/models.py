from django.contrib.auth.models import AbstractUser
from django.db import models

class Anunciate(AbstractUser):
    nombre_completo = models.CharField(max_length=150, verbose_name="Nombre Completo")
    telefono = models.CharField(max_length=20, verbose_name="Número de Teléfono")

    def __str__(self):
        return self.username
