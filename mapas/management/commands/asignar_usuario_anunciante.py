# mapas/management/commands/asignar_usuario_anunciante.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from core.models import Anunciate

class Command(BaseCommand):
    help = 'Asigna un usuario Anunciate al grupo Usuario Anunciante'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Nombre de usuario de Anunciate')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        try:
            user = Anunciate.objects.get(username=username)
            group = Group.objects.get(name='Usuario Anunciante')
            user.groups.add(group)
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Usuario "{username}" asignado al grupo "Usuario Anunciante" exitosamente.'))
        except Anunciate.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'El usuario "{username}" no existe.'))
        except Group.DoesNotExist:
            self.stdout.write(self.style.ERROR('El grupo "Usuario Anunciante" no existe.'))
