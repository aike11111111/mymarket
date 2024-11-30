from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    rut = forms.CharField(max_length=12, required=True)
    nombre = forms.CharField(max_length=100, required=True)
    apellido_paterno = forms.CharField(max_length=100, required=True)
    apellido_materno = forms.CharField(max_length=100, required=True)
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    celular = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']  # Puedes añadir más campos si lo deseas.

    def save(self, commit=True):
        user = super().save(commit=False)  # Crea el usuario
        if commit:
            user.save()
        
        # Crear y guardar el perfil
        profile = Profile.objects.create(
            user=user,
            rut=self.cleaned_data['rut'],
            nombre=self.cleaned_data['nombre'],
            apellido_paterno=self.cleaned_data['apellido_paterno'],
            apellido_materno=self.cleaned_data['apellido_materno'],
            fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
            celular=self.cleaned_data['celular']
        )
        
        return user
