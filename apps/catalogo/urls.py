from django.urls import path
from . import views

urlpatterns = [
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo_tortas/', views.torta_view, name='torta_view'),
    path('catalogo_helados/', views.helados, name='helados'),
    path('catalogo_energeticas/', views.energeticas, name='energeticas'),
]