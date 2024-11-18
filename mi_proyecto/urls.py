from django.contrib import admin
from django.urls import path, include  # Asegúrate de importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),  # Incluye las URLs de la app login
    path('', include('core.urls')),  # Incluye las URLs de 'core'
]
