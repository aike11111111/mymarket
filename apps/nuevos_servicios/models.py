from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

# Create your models here.

class Comuna(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre.replace('_', ' ').title()

    def nombre_formateado(self):
        return self.__str__()
#-----------------------------------------------------------------------------------------------------------#

def validate_nombre(value):
    if not value.strip():  
        raise ValidationError(
            _('Por favor, ingrese su nombre.'),
            params={'value': value},
        )
    if len(value) < 3:
        raise ValidationError(
            _('El nombre debe tener al menos 3 caracteres.'),
            params={'value': value},
        )
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$', value):
        raise ValidationError(
        _('El nombre debe contener solo letras.'),
        params={'value': value},
        )
    if len(value) > 30:
        raise ValidationError(
            _('El nombre debe tener máximo 30 caracteres.'),
            params={'value': value},
        )

def validate_apaterno(value):
    if not value.strip():  
        raise ValidationError(
            _('Por favor, ingrese su apellido paterno.'),
            params={'value': value},
        )
    if len(value) < 3:
        raise ValidationError(
            _('El apellido paterno debe tener al menos 3 caracteres.'),
            params={'value': value},
        )
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s-]+$', value):
        raise ValidationError(
            _('El apellido paterno debe contener solo letras.'),
            params={'value': value},
        )
    if len(value) > 30:
        raise ValidationError(
            _('El apellido paterno debe tener máximo 30 caracteres.'),
            params={'value': value},
        )
    
def validate_amaterno(value):
    if not value.strip():  
        raise ValidationError(
            _('Por favor, ingrese su apellido materno.'),
            params={'value': value},
        )
    if len(value) < 3:
        raise ValidationError(
            _('El apellido materno debe tener al menos 3 caracteres.'),
            params={'value': value},
        )
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s-]+$', value):
        raise ValidationError(
            _('El apellido materno debe contener solo letras.'),
            params={'value': value},
        )
    if len(value) > 30:
        raise ValidationError(
            _('El apellido materno debe tener máximo 30 caracteres.'),
            params={'value': value},
        )
    
def validate_telefono(value):
    if len(value) < 9:
        raise ValidationError(
            _('El telefono debe tener al menos 9 digitos.'),
            params={'value': value},
        )
    if not re.match(r'^[0-9]+$', value):
        raise ValidationError(
            _('El teléfono debe contener solo números.'),
            params={'value': value},
        )
    if len(value) > 30:
        raise ValidationError(
            _('El telefono debe tener máximo 12 digitos.'),
            params={'value': value},
        )
    
def validate_direccion(value):
    if len(value) < 10:
        raise ValidationError(
            _('La dirección debe tener minimo 10 caracteres.'),
            params={'value': value},
        )
    
def validate_comuna(value):
    if value is None:
        raise ValidationError(
            _('Debe seleccionar una comuna válida.')
        )
    
def validate_mensaje(value):
    if len(value) < 10:
        raise ValidationError(
            _('El mensaje debe tener minimo 10 caracteres.'),
            params={'value': value},
        )

class Contacto(models.Model):
    nombre = models.CharField(max_length=30, validators=[validate_nombre])
    apaterno = models.CharField(max_length=30, validators=[validate_apaterno])
    amaterno =  models.CharField(max_length=30, validators=[validate_amaterno])
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=20, validators=[validate_telefono])
    direccion = models.CharField(max_length=150, validators=[validate_direccion])
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, validators=[validate_comuna])
    mensaje = models.TextField(max_length=120, validators=[validate_mensaje])
    
    def __str__(self):
        return f'{self.nombre} {self.apaterno} {self.amaterno}'