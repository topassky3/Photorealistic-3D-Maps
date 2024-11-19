from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirige a 'home' si el usuario ya está autenticado

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        try:
            user = authenticate(request, username=email, password=password)  # Ahora 'username' es 'email'
            if user is not None:
                login(request, user)
                if not remember:
                    request.session.set_expiry(0)  # La sesión expira al cerrar el navegador
                return redirect('home')  # Redirige a 'home' después de iniciar sesión
            else:
                messages.error(request, 'Correo electrónico o contraseña incorrectos.')
        except Exception as e:
            messages.error(request, 'Ocurrió un error al intentar iniciar sesión.')

    return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    return redirect('login:login')  # Redirige a la página de login después de cerrar sesión

