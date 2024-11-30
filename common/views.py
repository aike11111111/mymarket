from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterForm
from .models import Profile


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # Usar 'email' como nombre de usuario para autenticación
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)  # Inicia sesión al usuario
            return redirect('home')  # Redirigir a la página principal después de iniciar sesión
        else:
            messages.error(request, 'Las credenciales no son correctas.')  # Mensaje de error
            return redirect('login')  # Redirige de nuevo al login en caso de error

    return render(request, 'login.html')
    
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda tanto el User como el Profile
            return redirect('login')  # Redirige al login después de un registro exitoso
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})