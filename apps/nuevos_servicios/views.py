from django.shortcuts import render
from django.template.loader import get_template
from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.contrib import messages
from .models import Contacto

# Create your views here.

def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            
            form.save()

            messages.success(request, 'Formulario enviado correctamente.')

            return redirect('contacto')  

    else:
        form = ContactoForm()

    return render(request, 'nuevos_servicios/contacto.html', {'form': form})