# registor/views.py

from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib import messages
from django.contrib.auth.models import Group

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Asignar automáticamente al grupo "Usuario Anunciante"
            try:
                grupo = Group.objects.get(name='Usuario Anunciante')
                user.groups.add(grupo)
                user.save()
            except Group.DoesNotExist:
                messages.error(request, 'El grupo "Usuario Anunciante" no existe. Contacta al administrador.')
                return redirect('registor:register')

            messages.success(request, 'Tu cuenta ha sido creada exitosamente. Puedes iniciar sesión ahora.')
            return redirect('login:login')
        else:
            messages.error(request, 'Por favor, corrige los errores a continuación.')
    else:
        form = RegistroForm()
    return render(request, 'registor/register.html', {'form': form})
