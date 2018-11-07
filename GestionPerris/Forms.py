from django import forms
from .models import *

class perroForm(forms.ModelForm):
    class Meta:
        model = perro
        fields = ('nombre_perro','foto','raza_predominante','descripcion','estado',)

class adoptanteForm(forms.ModelForm):
    class Meta:
        model = adoptante
        fields = ('email_usuario','run_usuario','nombre_usuario','fono_usuario',
        'fechanac_usuario','regiones','comunas','tipo_vivienda',)

class usuarioUwuForm(forms.ModelForm):
    class Meta:
        model = usuarioUwu
        fields = ('email_usuario','uname','psw',)
