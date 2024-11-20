# anuncio/forms.py

from django import forms
from core.models import Anuncio

class CrearAnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = [
            'titulo',
            'descripcion',
            'imagen',
            'enlace',
            'tipo_lugar',
            'nivel_precio',
            'calificacion',
            'area_interes',
            'radio',
            'latitud',
            'longitud',
            'modelo_3d',  # Nuevo campo para el modelo 3D
        ]
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título del Anuncio'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción del Anuncio',
                'rows': 5
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'enlace': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL del Anuncio'
            }),
            'tipo_lugar': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tipo de Lugar (e.g., Restaurante, Cafetería)'
            }),
            'nivel_precio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nivel de Precio (e.g., $, $$, $$$)'
            }),
            'calificacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Calificación (0.0 - 5.0)',
                'step': '0.1'
            }),
            'area_interes': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Área de Interés (e.g., Ciudad, Código Postal)'
            }),
            'radio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Radio (km)'
            }),
            'latitud': forms.HiddenInput(),    # Campo oculto para latitud
            'longitud': forms.HiddenInput(),   # Campo oculto para longitud
            'modelo_3d': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),  # Widget para el modelo 3D
        }
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'imagen': 'Imagen del Anuncio',
            'enlace': 'Enlace del Anuncio',
            'tipo_lugar': 'Tipo de Lugar',
            'nivel_precio': 'Nivel de Precio',
            'calificacion': 'Calificación',
            'area_interes': 'Área de Interés',
            'radio': 'Radio (km)',
            'latitud': 'Latitud',
            'longitud': 'Longitud',
            'modelo_3d': 'Modelo 3D (glTF)',
        }

    def clean_modelo_3d(self):
        modelo = self.cleaned_data.get('modelo_3d', False)
        if modelo:
            if not modelo.name.endswith(('.gltf', '.glb')):
                raise forms.ValidationError("Solo se permiten archivos glTF (.gltf, .glb).")
            if modelo.size > 50 * 1024 * 1024:
                raise forms.ValidationError("El archivo es demasiado grande (máximo 5MB).")
        return modelo