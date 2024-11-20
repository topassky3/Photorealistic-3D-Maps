# anuncio/views.py

from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from core.models import Anuncio
from .forms import CrearAnuncioForm

class AdministradorAnuncioMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.groups.filter(
            name='Administrador de Anuncios').exists()

class CrearAnuncioView(LoginRequiredMixin, AdministradorAnuncioMixin, CreateView):
    model = Anuncio
    form_class = CrearAnuncioForm
    template_name = 'anuncio/crear_anuncio.html'
    success_url = reverse_lazy('anuncio:crear_anuncio')  # Puedes cambiar esto si quieres redirigir a otra página

    def form_valid(self, form):
        # Asignar el usuario creador antes de guardar
        anuncio = form.save(commit=False)
        anuncio.usuario_creador = self.request.user
        anuncio.save()
        messages.success(self.request, 'Anuncio creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Por favor, corrige los errores a continuación.')
        return super().form_invalid(form)
