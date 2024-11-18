from django.urls import path
from .views import BaseTemplateView

urlpatterns = [
    path('', BaseTemplateView.as_view(), name='home'),  # La URL raíz de la aplicación 'core'
]
