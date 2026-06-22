from django import forms
from .models import RegistroLoteria

# ModelForm genera automáticamente el formulario basado en el modelo
class RegistroLoteriaForm(forms.ModelForm):

    class Meta:
        # Le decimos a Django en qué modelo se basa este formulario
        model = RegistroLoteria

        # Qué campos del modelo incluir en el formulario
        fields = ['numero', 'fecha']

        # Personalizar los widgets (cómo se renderiza cada campo en HTML)
        widgets = {
            'numero': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 4521'
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'  # Activa el selector de fecha del navegador
            }),
        }
