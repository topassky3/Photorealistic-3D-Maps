# mapas/signals.py

from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver

@receiver(post_migrate)
def create_usuario_anunciante_group(sender, **kwargs):
    if sender.name == 'mapas':
        group, created = Group.objects.get_or_create(name='Usuario Anunciante')
        if created:
            # Asigna permisos específicos al grupo
            permisos = Permission.objects.filter(codename__in=[
                'view_anuncio',
            ])
            group.permissions.set(permisos)
            group.save()
