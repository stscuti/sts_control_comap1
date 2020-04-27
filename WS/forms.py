from django import forms
from Usuarios.models import Usuario, Usuario_Contribuyente, Usuario_Personas_Fisicas
from betterforms.multiform import MultiModelForm
from .models import Cotizaciones


class FormCotizaciones(forms.ModelForm):
	
	class Meta:
		model = Cotizaciones
		fields = '__all__'
		#exclude = ('identificador',)
		verbose_name = 'Formulario: Cotizaciones'
		label = 'Formulario de Cotizaciones'