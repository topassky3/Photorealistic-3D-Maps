# anuncio/urls.py

from django.urls import path
from . import views

app_name = 'anuncio'

urlpatterns = [
    path('crear/', views.CrearAnuncioView.as_view(), name='crear_anuncio'),
    # Puedes añadir más rutas aquí en el futuro
]
