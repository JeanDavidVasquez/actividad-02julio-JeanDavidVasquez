from django.forms import ModelForm
from django import forms
from .models import Estudiante
from .models import Modulo


from administrativo.models import Matricula, Modulo, Estudiante

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario', 'costo']
        widgets = {
            'estudiante': forms.Select(attrs={
                'class': 'form-control'
            }),
            'modulo': forms.Select(attrs={
                'class': 'form-control'
            }),
            'comentario': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Comentario'
            }),
            'costo': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Costo'
            }),
        }

class MatriculaEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(MatriculaEditForm, self).__init__(*args, **kwargs)
        self.initial['estudiante'] = self.instance.estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()
        self.initial['modulo'] = self.instance.modulo
        self.fields["modulo"].widget = forms.widgets.HiddenInput()

        # Solo agregar clases aquí sin modificar la estructura
        self.fields['comentario'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['costo'].widget.attrs.update({
            'class': 'form-control',
        })

    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario', 'costo']  
        widgets = {
            'comentario': forms.Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'placeholder': 'Escribe aquí tu comentario...'
            }),
        }

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['nombre']
        widgets = {
            'nombre': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
        

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cédula'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
            'tipo_estudiante': forms.Select(attrs={'class': 'form-control'}),
        }


