from django import forms
from . models import Contacto, Comuna, validate_telefono
from django.core.exceptions import ValidationError
import re

class ContactoForm(forms.ModelForm):
    apaterno = forms.CharField(label='Apellido Paterno', max_length=30)
    amaterno = forms.CharField(label='Apellido Materno', max_length=30)
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.all(), 
                                    empty_label='Selecciona una comuna...')
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu mensaje aquí...'}))
    rut = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '12345678-2', 'class': 'form-control'}))
    
    class ContactoForm(forms.ModelForm):
        class Meta:
            model = Contacto 
            fields = ['comuna']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comuna'].label = 'Comuna'

    class Meta:
        model = Contacto
        fields = ['nombre', 'apaterno', 'amaterno', 'rut','telefono', 'direccion', 'comuna', 'mensaje']

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()  
        if len(nombre) < 3:
            raise forms.ValidationError(
                ('El nombre debe tener al menos 3 caracteres.')
            )
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$', nombre):
            raise forms.ValidationError(
                ('El nombre debe contener solo letras.')
            )
        if len(nombre) > 30:
            raise forms.ValidationError(
                ('El nombre debe tener máximo 30 caracteres.')
            )
        return nombre
    
    def clean_apaterno(self):
        apaterno = self.cleaned_data.get('apaterno', '').strip() 
        if len(apaterno) < 3:
            raise forms.ValidationError(
                ('El apellido paterno debe tener al menos 3 caracteres.')
            )
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s-]+$', apaterno):
            raise forms.ValidationError(
                ('El apellido paterno debe contener solo letras.')
            )
        if len(apaterno) > 30:
            raise forms.ValidationError(
                ('El apellido paterno debe tener máximo 30 caracteres.')
            )
        return apaterno
    
    def clean_amaterno(self):
        amaterno = self.cleaned_data.get('amaterno', '').strip() 
        if len(amaterno) < 3:
            raise forms.ValidationError(
                ('El apellido materno debe tener al menos 3 caracteres.')
            )
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s-]+$', amaterno):
            raise forms.ValidationError(
                ('El apellido materno debe contener solo letras.')
            )
        if len(amaterno) > 30:
            raise forms.ValidationError(
                ('El apellido materno debe tener máximo 30 caracteres.')
            )
        return amaterno
    
        
    def clean_telefono(self):
        telefono = self.cleaned_data['telefono']
        validate_telefono(telefono)  
        return telefono
    
    def clean_direccion(self):
        direccion = self.cleaned_data.get('direccion')
        if len(direccion) < 10:
            raise forms.ValidationError('La dirección debe tener minimo 10 caracteres.')
        return direccion
        
    def clean_comuna(self):
        comuna = self.cleaned_data.get('comuna')
        if not Comuna.objects.filter(pk=comuna.pk).exists():
            raise forms.ValidationError('Seleccione una comuna válida.')
        return comuna
        
    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')
        if len(mensaje) < 10:
            raise forms.ValidationError('La ocupación debe tener al menos 10 caracteres.')
        return mensaje
        

