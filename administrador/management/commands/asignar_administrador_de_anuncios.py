# administrador/management/commands/asignar_administrador_de_anuncios.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from core.models import Anunciate

class Command(BaseCommand):
    help = 'Asigna un usuario Anunciate al grupo Administrador de Anuncios'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Nombre de usuario de Anunciate')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        try:
            user = Anunciate.objects.get(username=username)
            group = Group.objects.get(name='Administrador de Anuncios')
            user.groups.add(group)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Usuario "{username}" asignado al grupo "Administrador de Anuncios" exitosamente.'))
        except Anunciate.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'El usuario "{username}" no existe.'))
        except Group.DoesNotExist:
            self.stdout.write(self.style.ERROR('El grupo "Administrador de Anuncios" no existe.'))
