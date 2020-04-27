from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *

class Pais_Form(forms.ModelForm):
	class Meta:
		model = Pais
		fields = '__all__'
		exclude = ['um','uc', ]
		verbose_name='Pais'
		label='Paises'
	def __init__(self, *args, **kwargs):
		super(Pais_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
		    	'class': 'form-control'
			})


class Departamento_Form(forms.ModelForm):
	class Meta:
		model=Departamento
		fields = '__all__'
		exclude = ('um','uc',)
		verbose_name='Departamento'
		label='Departamento'
	def __init__(self, *args, **kwargs):
		super(Departamento_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		descripcion = self.cleaned_data['descripcion']
		if descripcion == '':
			raise forms.ValidationError("Debe ingresar un Departamento valido")
		return descripcion

class Localidad_Form(forms.ModelForm):
	class Meta:
		model=Localidad
		fields = '__all__'
		exclude = ('um', 'uc',)
		verbose_name='Localidad'
		label='Localidad'
	def __init__(self, *args, **kwargs):
		super(Localidad_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		descripcion = self.cleaned_data['descripcion']
		if descripcion == '':
			raise forms.ValidationError("Debe ingresar un Departamento valido")
		return descripcion


DepartamentoFormSet = inlineformset_factory(
	Pais, Departamento, form=Departamento_Form,
	fields='__all__',exclude = ('estado','um', ), extra=1, can_delete=True
	)

LocalidadFormSet = inlineformset_factory(
	Departamento, Localidad, form=Localidad_Form,
	fields='__all__',exclude = ('estado','um', 'uc',), extra=1, can_delete=True
	)

class TipoDocumento_Form(forms.ModelForm):
	class Meta:
		model=Tipo_Documento
		fields = '__all__'
		exclude = ('um', 'uc',)
		verbose_name='Tipo de Documento'
		label='Tipo de Documento'
	def __init__(self, *args, **kwargs):
		super(TipoDocumento_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		descripcion = self.cleaned_data['descripcion']
		if descripcion == '':
			raise forms.ValidationError("Debe ingresar un Tipo de Documento valido")
		return descripcion

class Categoria_Inversiones_Form(forms.ModelForm):
	class Meta:
		model=Categoria_Inversiones
		fields = '__all__'
		exclude = ('um', 'uc',)
		verbose_name='Categoria de Inversiones'
		label='Categoria de Inversiones'
	def __init__(self, *args, **kwargs):
		super(Categoria_Inversiones_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		categoria = self.cleaned_data['categoria']
		if categoria == '':
			raise forms.ValidationError("Debe ingresar una Categoria de Inversiones valida")
		return categoria

class SubCategoria_Inversiones_Form(forms.ModelForm):
	class Meta:
		model=SubCategoria_Inversiones
		fields = '__all__'
		exclude = ('um', 'uc',)
		verbose_name='SubCategoria de Inversiones'
		label='SubCategoria de Inversiones'
	def __init__(self, *args, **kwargs):
		super(SubCategoria_Inversiones_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		subcategoria = self.cleaned_data['subcategoria']
		if subcategoria == '':
			raise forms.ValidationError("Debe ingresar una SubCategoria de Inversiones valida")
		return subcategoria

class TipoContribuyente_Form(forms.ModelForm):
	class Meta:
		model=TipoContribuyente
		fields = '__all__'
		exclude = ('um', 'uc',)
		verbose_name='Tipo de Contribuyente'
		label='Tipo de Contribuyente'
	def __init__(self, *args, **kwargs):
		super(TipoContribuyente_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		tipo_contribuyente = self.cleaned_data['tipo_contribuyente']
		if tipo_contribuyente == '':
			raise forms.ValidationError("Debe ingresar un Tipo de Contribuyente valido")
		return tipo_contribuyente

class Ministerios_Form(forms.ModelForm):
	class Meta:
		model=Ministerios
		fields = '__all__'
		exclude = ('um', 'uc',)
		verbose_name='Ministerio'
		label='Ministerios'
	def __init__(self, *args, **kwargs):
		super(Ministerios_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		descripcion = self.cleaned_data['descripcion']
		if descripcion == '':
			raise forms.ValidationError("Debe ingresar un Ministerio valido")
		return descripcion

''' Tipo Giro y Giro CIIU'''

class TipoGiro_Form(forms.ModelForm):
	class Meta:
		model = TipoGiro
		fields = '__all__'
		exclude = ('um', 'uc',)
		verbose_name='Tipo de Giro CIIU'
		label='Tipo de Giro CIIU'
	def __init__(self, *args, **kwargs):
		super(TipoGiro_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		descripcion = self.cleaned_data['descripcion']
		if descripcion == '':
			raise forms.ValidationError("Debe ingresar un Tipo de giro valido")
		return descripcion

class GiroCIIU_Form(forms.ModelForm):
	class Meta:
		model = GiroCIIU
		fields = '__all__'
		exclude = ('um', 'uc',)
		verbose_name='Giro CIIU'
		label='Giro CIIU'
	def __init__(self, *args, **kwargs):
		super(GiroCIIU_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		codigo_giro = self.cleaned_data['codigo_giro']
		descripcion = self.cleaned_data['descripcion']
		if codigo_giro == '' or descripcion == '':
			raise forms.ValidationError("Debe ingresar un codigo de giro CIIU valido")
		return descripcion

class FechaBalance_Form(forms.ModelForm):
	class Meta:
		model = FechaBalance
		fields = '__all__'
		exclude = ('um', 'uc',)
		verbose_name='Fecha de Balance'
		label='Fecha de Balance'
	def __init__(self, *args, **kwargs):
		super(FechaBalance_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		fecha_balance = self.cleaned_data['fecha_balance']
		if fecha_balance == '':
			raise forms.ValidationError("Debe ingresar una Fecha de Balance valida")
		return fecha_balance

class Localizacion_Operaciones_Form(forms.ModelForm):
	class Meta:
		model = Localizacion_Operaciones
		fields = '__all__'
		exclude = ('um', 'uc',)
		verbose_name='Localizacion de Operaciones'
		label='Localizacion de Operaciones'
	def __init__(self, *args, **kwargs):
		super(Localizacion_Operaciones_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		tipo = self.cleaned_data['tipo']
		if tipo == '':
			raise forms.ValidationError("Debe ingresar un tipo valido")
		return tipo


class Listado_Puntaje_Departamentos_Form(forms.ModelForm):
	class Meta:
		model = Listado_Puntaje_Departamentos
		fields = '__all__'
		exclude = ('um', 'uc',)
		verbose_name='Listado de Puntaje de Departamentos'
		label='Listado de Puntaje de Departamentos'
	def __init__(self, *args, **kwargs):
		super(Listado_Puntaje_Departamentos_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		departamento = self.cleaned_data['departamento']
		if departamento == '':
			raise forms.ValidationError("Debe ingresar un departamento valido")
		return departamento

class Tipo_DocumentoPresentar_Form(forms.ModelForm):
	class Meta:
		model = Tipo_DocumentoPresentar
		fields = '__all__'
		exclude = ('um', 'uc',)
		verbose_name='Documento a Presentar'
		label='Documento a Presentar'
	def __init__(self, *args, **kwargs):
		super(Tipo_DocumentoPresentar_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		descripcion = self.cleaned_data['descripcion']
		if descripcion == '':
			raise forms.ValidationError("Debe ingresar un tipo de documento a presentar valido")
		return descripcion

class Exp_Bienes_Servicios_Form(forms.ModelForm):
	class Meta:
		model = Exp_Bienes_Servicios
		fields = '__all__'
		exclude = ('um', 'uc',)
		verbose_name='Exportaciones Bienes/Servicios'
		label='Exportaciones Bienes/Servicios'
	def __init__(self, *args, **kwargs):
		super(Exp_Bienes_Servicios_Form, self).__init__(*args, **kwargs)
		for field in iter(self.fields):
			self.fields[field].widget.attrs.update({
				'class': 'form-control'
			})
	def clean_descripcion(self):
		descripcion = self.cleaned_data['descripcion']
		if descripcion == '':
			raise forms.ValidationError("Debe ingresar un tipo de bien o servicio valido")
		return descripcion

