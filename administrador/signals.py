# administrador/signals.py

from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_administrador_de_anuncios_group(sender, **kwargs):
    if sender.name == 'administrador':
        group, created = Group.objects.get_or_create(name='Administrador de Anuncios')
        if created:
            # Asigna permisos específicos al grupo
            # Por ejemplo, permisos relacionados con la app 'anuncios'
            # Asegúrate de que la app 'anuncios' y sus modelos existan
            permisos = Permission.objects.filter(codename__in=[
                'add_anuncio',
                'change_anuncio',
                'delete_anuncio',
                'view_anuncio',
            ])
            group.permissions.set(permisos)
            group.save()
