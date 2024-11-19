# core/templatetags/grupos.py

from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    """
    Verifica si el usuario pertenece al grupo especificado.

    Uso en la plantilla:
    {% if user|has_group:"Nombre del Grupo" %}
        <!-- Código exclusivo para miembros del grupo -->
    {% endif %}
    """
    return user.groups.filter(name=group_name).exists()
