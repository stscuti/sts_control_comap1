from django import forms
from django.forms import ModelForm
from PIL import Image
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset, ButtonHolder, HTML, Div

from .models import *
from betterforms.multiform import MultiModelForm

from django.db import models
from WF.models import ModeloBaseRegistro
from Usuarios.models import Usuario
from Base.models import *

class ContribuyenteForm(ModelForm):
	class Meta:
		model=Contribuyente
		fields = '__all__'
		exclude = ('validado','identificador','estado','um','uc',)
		verbose_name='Formulario: Contribuyente'
		label='Formulario Contribuyente'

	def __init__(self, *args, **kwargs):
		super(ContribuyenteForm,self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			HTML('<h1 class="">Editar Contribuyente</h1>'),
			HTML('<p class="">Datos Formales</p>'),
			Row(
				Column('razon_social', css_class='form-group col-md-3 mb-0'),
				Column('nombre_comercial', css_class='form-group col-md-3 mb-0'),
				Column('rut', css_class='form-group col-md-2 mb-0'),
				Column('num_bps', css_class='form-group col-md-2 mb-0'),
				Column('num_mtss', css_class='form-group col-md-2 mb-0'),
				css_class='form-row'
				),
				Row(
				Column('domicilio_constituido', css_class='form-group col-md-3 mb-0'),
				Column('domicilio_fiscal', css_class='form-group col-md-3 mb-0'),
				Column('telefono', css_class='form-group col-md-2 mb-0'),
				Column('email', css_class='form-group col-md-2 mb-0'),
				Column('celular', css_class='form-group col-md-2 mb-0'),
				css_class='form-row'
				),
				HTML('<p class="formtitulosintermedios">Actividad y Tipo de Contribuyente</p>'),
				Row(
				Column('cod_giro_ciiu', css_class='form-group col-md-2 mb-0'),
				Column('nombre_giro', css_class='form-group col-md-4 mb-0'),
				Column('fecha_balance', css_class='form-group col-md-3 mb-0'),
				Column('tipo', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			#Submit('submit', 'Cargar')
	    )

class DomicilioFiscalForm(ModelForm):
	class Meta:
		model=Domicilio_Fiscal
		fields = '__all__'
		exclude = ('id','identificador','estado','um','uc',)
		verbose_name='Formulario: Domicilio Fiscal'
		label='Domicilio Fiscal'
	def __init__(self, *args, **kwargs):
		super(DomicilioFiscalForm,self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			HTML('<p class="formtitulosintermedios">Domicilio Fiscal</p>'),
			Row(
				Column('departamento', css_class='form-group col-md-4 mb-0'),
				Column('localidad', css_class='form-group col-md-8 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('direccion', css_class='form-group col-md-4 mb-0'),
				Column('numero', css_class='form-group col-md-4 mb-0'),
				Column('ampliacion_descripcion', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
		)

class DomicilioConstituidoForm(ModelForm):
	class Meta:
		model=Domicilio_Constituido
		fields = '__all__'
		exclude = ('id','identificador','estado','um','uc',)
		verbose_name='Formulario: Domicilio Constituido'
		label='Domicilio Constituido'
	def __init__(self, *args, **kwargs):
		super(DomicilioConstituidoForm,self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			HTML('<p class="formtitulosintermedios">Domicilio Constituido</p>'),
			Row(
				Column('departamento', css_class='form-group col-md-4 mb-12'), #form-control
				Column('localidad', css_class='form-group col-md-8 mb-12'),
				css_class='form-row'
			),
			Row(
				Column('direccion', css_class='form-group col-md-4 mb-12'),
				Column('numero', css_class='form-group col-md-4 mb-12'),
				Column('ampliacion_descripcion', css_class='form-group col-md-4 mb-12'),
				css_class='form-row'
			),
		)

class PropietariosForm(ModelForm):
	class Meta:
		model=Propietarios
		fields = '__all__'
		exclude = ('id','identificador','estado','um','uc',)
		verbose_name='Formulario: Propietarios'
		label='Propietarios'
	def __init__(self, *args, **kwargs):
		super(PropietariosForm,self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			HTML('<p class="formtitulosintermedios">Propietarios</p>'),
			Row(
				Column('tipo_documento', css_class='form-group col-md-4 mb-12'), #form-control
				Column('numero_documento', css_class='form-group col-md-4 mb-12'),
				Column('pais', css_class='form-group col-md-4 mb-12'),
				css_class='form-row'
			),
			Row(
				Column('primer_nombre', css_class='form-group col-md-3 mb-12'),
				Column('segundo_nombre', css_class='form-group col-md-3 mb-12'),
				Column('primer_apellido', css_class='form-group col-md-3 mb-12'),
				Column('segundo_apellido', css_class='form-group col-md-3 mb-12'),
				css_class='form-row'
			),
		)

class RepresentantesForm(ModelForm):
	class Meta:
		model=Representantes
		fields = '__all__'
		exclude = ('id','identificador','estado','um','uc',)
		verbose_name='Formulario: Representantes'
		label='Representantes'
	def __init__(self, *args, **kwargs):
		super(RepresentantesForm,self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			HTML('<p class="formtitulosintermedios">Representantes</p>'),
			Row(
				Column('tipo_documento', css_class='form-group col-md-4 mb-12'), #form-control
				Column('numero_documento', css_class='form-group col-md-4 mb-12'),
				Column('pais', css_class='form-group col-md-4 mb-12'),
				css_class='form-row'
			),
			Row(
				Column('primer_nombre', css_class='form-group col-md-3 mb-12'),
				Column('segundo_nombre', css_class='form-group col-md-3 mb-12'),
				Column('primer_apellido', css_class='form-group col-md-3 mb-12'),
				Column('segundo_apellido', css_class='form-group col-md-3 mb-12'),
				css_class='form-row'
			),
		)

class DirectoresForm(ModelForm):
	class Meta:
		model=Directores
		fields = '__all__'
		exclude = ('id','identificador','estado','um','uc',)
		verbose_name='Formulario: Directores'
		label='Directores'
	def __init__(self, *args, **kwargs):
		super(DirectoresForm,self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			HTML('<p class="formtitulosintermedios">Directores</p>'),
			Row(
				Column('tipo_documento', css_class='form-group col-md-4 mb-12'), #form-control
				Column('numero_documento', css_class='form-group col-md-4 mb-12'),
				Column('pais', css_class='form-group col-md-4 mb-12'),
				css_class='form-row'
			),
			Row(
				Column('primer_nombre', css_class='form-group col-md-3 mb-12'),
				Column('segundo_nombre', css_class='form-group col-md-3 mb-12'),
				Column('primer_apellido', css_class='form-group col-md-3 mb-12'),
				Column('segundo_apellido', css_class='form-group col-md-3 mb-12'),
				css_class='form-row'
			),
		)

class MultiContribuyentesForm(MultiModelForm):
	form_classes = {
		'ContribuyenteMain': ContribuyenteForm,
		'DomicilioFiscalMain': DomicilioFiscalForm,
		'DomicilioConstituidoMain': DomicilioConstituidoForm,
		'PropietariosMain': PropietariosForm,
		'RepresentantesMain': RepresentantesForm,
		'DirectoresMain': DirectoresForm,
	}