from django.urls import path, register_converter
from . import views
from .converters import FloatConverter

app_name = 'mapas'

# Registra el convertidor
register_converter(FloatConverter, 'float')

urlpatterns = [
    path('', views.MapaListView.as_view(), name='lista_mapas'),
    path('centro/<float:lat>/<float:lng>/', views.MapaListView.as_view(), name='mapa_centrado'),
]
