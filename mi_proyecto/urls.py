from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar 'include'
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),      # Incluye las URLs de la app login
    path('register/', include('registor.urls')), # Incluye las URLs de la app registor
    path('anuncio/', include('anuncio.urls')),
    path('mapas/', include('mapas.urls')),
    path('', include('core.urls')),             # Incluye las URLs de 'core'
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)