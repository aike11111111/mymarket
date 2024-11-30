from django.shortcuts import render

# Create your views here.

def catalogo(request):
    return render(request, 'catalogo/catalogo.html', {})

def torta_view(request):
    return render(request, 'catalogo/base_tortas.html', {})

def helados(request):
    return render(request, 'catalogo/base_helados.html', {})

def energeticas(request):
    return render(request, 'catalogo/base_energeticas.html', {})