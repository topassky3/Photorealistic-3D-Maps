# core/views.py

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import Anuncio
from django.conf import settings
import json

class MapaListView(LoginRequiredMixin, TemplateView):
    template_name = 'mapas/mapa_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Filtrar anuncios según el rol del usuario
        if user.groups.filter(name='Administrador de Anuncios').exists():
            anuncios = Anuncio.objects.filter(usuario_creador=user)
        elif user.groups.filter(name='Usuario Anunciante').exists():
            anuncios = Anuncio.objects.all()
        else:
            anuncios = Anuncio.objects.none()

        # Obtener datos de anuncios para el mapa
        anuncios_data = []
        for anuncio in anuncios:
            anuncios_data.append({
                'titulo': anuncio.titulo,
                'descripcion': anuncio.descripcion,
                'imagen_url': anuncio.imagen.url if anuncio.imagen else '',
                'enlace': anuncio.enlace,
                'latitud': float(anuncio.latitud) if anuncio.latitud else 0.0,
                'longitud': float(anuncio.longitud) if anuncio.longitud else 0.0,
                'modelo_3d_url': anuncio.modelo_3d.url if anuncio.modelo_3d else '',
            })
        print(anuncios_data)
        context['anuncios'] = anuncios_data  # Pasar como lista de diccionarios
        context['google_maps_api_key'] = settings.GOOGLE_MAPS_API_KEY

        # Obtener coordenadas para centrar el mapa si están en la URL
        lat = self.kwargs.get('lat')
        lng = self.kwargs.get('lng')
        context['centro'] = {'lat': lat, 'lng': lng} if lat and lng else None

        return context
