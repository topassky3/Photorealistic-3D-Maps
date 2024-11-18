# registor/views.py

from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta ha sido creada exitosamente. Puedes iniciar sesión ahora.')
            return redirect('login:login')
        else:
            messages.error(request, 'Por favor, corrige los errores a continuación.')
    else:
        form = RegistroForm()
    return render(request, 'registor/register.html', {'form': form})
