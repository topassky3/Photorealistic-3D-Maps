# registor/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import Anunciate

class RegistroForm(UserCreationForm):
    nombre_completo = forms.CharField(
        max_length=150,
        required=True,
        label='Nombre Completo',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Juan Pérez'})
    )
    email = forms.EmailField(
        required=True,
        label='Correo Electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'nombre@ejemplo.com'})
    )
    telefono = forms.CharField(
        max_length=20,
        required=True,
        label='Número de Teléfono',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+1 234 567 890'})
    )
    terminos = forms.BooleanField(
        required=True,
        label='Acepto los términos y condiciones y la política de privacidad'
    )

    class Meta:
        model = Anunciate
        fields = ['username', 'nombre_completo', 'email', 'telefono', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Anunciate.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        # Aquí puedes agregar validaciones adicionales para el teléfono si lo deseas
        return telefono
