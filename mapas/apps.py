# mapas/apps.py

from django.apps import AppConfig

class MapasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mapas'

    def ready(self):
        import mapas.signals  # Importa las señales
