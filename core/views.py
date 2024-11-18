from django.views.generic import TemplateView

class BaseTemplateView(TemplateView):
    template_name = 'core/base.html'  # Asegúrate de que el nombre coincide con tu plantilla
