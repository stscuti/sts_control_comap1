from django.db import models
from WF.models import ModeloBaseRegistro
from Usuarios.models import Usuario
from Base.models import *

# Create your models here.

class DomicilioBaseRegistro(ModeloBaseRegistro):
	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, help_text='Departamento', verbose_name='Departamento')
	localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, help_text='Localidad', verbose_name='Localidad')
	#departamento = models.CharField(max_length=150, help_text='Departamento', verbose_name='Departamento')
	#localidad = models.CharField(max_length=150, help_text='Localidad', verbose_name='Localidad')
	direccion = models.CharField(max_length=150, help_text='Direccion', verbose_name='Direccion')
	numero = models.CharField(max_length=20, help_text='Numero', verbose_name='Numero')
	ampliacion_descripcion = models.CharField(max_length=250, help_text='Ampliar Descripcion de la Direccion', verbose_name='Ampliacion Descripcion')

	class Meta:
		abstract = True

class PropietariosDirectoresRepresentatesBaseRegistro(ModeloBaseRegistro):
	tipo_documento = models.ForeignKey(Tipo_Documento, on_delete=models.CASCADE, help_text='Tipo de Documento', verbose_name='Tipo de Documento')
	numero_documento = models.BigIntegerField(help_text='Numero de Documento', verbose_name='Numero de Documento')
	pais = models.ForeignKey(Pais, on_delete=models.CASCADE, help_text='Pais', verbose_name='Pais')
	primer_nombre = models.CharField(max_length=40, help_text='Primer Nombre', verbose_name='Primer Nombre')
	segundo_nombre = models.CharField(max_length=40, help_text='Segundo Nombre', verbose_name='Segundo Nombre')
	primer_apellido = models.CharField(max_length=40, help_text='Primer Apellido', verbose_name='Primer Apellido')
	segundo_apellido = models.CharField(max_length=40, help_text='Segundo Apellido', verbose_name='Segundo Apellido')

	class Meta:
		abstract = True

class Contribuyente(models.Model):
	identificador = models.OneToOneField(Usuario, on_delete=models.CASCADE, help_text='Identificador numerico del Contribuyente: RUT', verbose_name='Identificador')
	validado = models.BooleanField(default=False, help_text='Refiere a si fue validado por la Administracion', verbose_name='Contribuyente Validado')
	estado = models.BooleanField(default=True)
	fc = models.DateTimeField(auto_now_add=True)
	fm = models.DateTimeField(auto_now=True)
	#uc = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	um = models.BigIntegerField(blank=True, null=True)	
	class Meta:
		verbose_name = 'Contribuyente'
		verbose_name_plural = 'Contribuyentes'
		#unique_together = ('identificador')
	def __str__(self):
		return str(self.identificador)

class Domicilio_Fiscal(DomicilioBaseRegistro):
	identificador = models.OneToOneField(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	class Meta:
		verbose_name = 'Domicilio Fiscal'
		verbose_name_plural = 'Domicilio Fiscal'
	def __str__(self):
		return str(self.direccion)	+ ' - ' + str(self.departamento) + ' - ' + str(self.localidad)		

class Domicilio_Constituido(DomicilioBaseRegistro):
	identificador = models.OneToOneField(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	class Meta:
		verbose_name = 'Domicilio Constituido'
		verbose_name_plural = 'Domicilio Constituido'
	def __str__(self):
		return str(self.direccion)	+ ' - ' + str(self.departamento) + ' - ' + str(self.localidad)

class Propietarios(PropietariosDirectoresRepresentatesBaseRegistro):
	identificador = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	class Meta:
		verbose_name = 'Propietario'
		verbose_name_plural = 'Propietarios'
		unique_together = ('identificador','tipo_documento','numero_documento','pais')
	def __str__(self):
		return str(self.primer_nombre) + ' ' + str(self.segundo_nombre) + '-' + str(self.primer_apellido) + ' ' + str(self.segundo_apellido)
	def save(self):
		self.primer_nombre = self.primer_nombre.title()
		self.segundo_nombre = self.segundo_nombre.title()
		self.primer_apellido = self.primer_apellido.title()
		self.segundo_apellido = self.segundo_apellido.title()
		super(Propietarios, self).save()

class Representantes(PropietariosDirectoresRepresentatesBaseRegistro):
	identificador = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	class Meta:
		verbose_name = 'Representante'
		verbose_name_plural = 'Representantes'
		unique_together = ('identificador','tipo_documento','numero_documento','pais')
	def __str__(self):
		return str(self.primer_nombre) + ' ' + str(self.segundo_nombre) + '-' + str(self.primer_apellido) + ' ' + str(self.segundo_apellido)
	def save(self):
		self.primer_nombre = self.primer_nombre.title()
		self.segundo_nombre = self.segundo_nombre.title()
		self.primer_apellido = self.primer_apellido.title()
		self.segundo_apellido = self.segundo_apellido.title()
		super(Representantes, self).save()

class Directores(PropietariosDirectoresRepresentatesBaseRegistro):
	identificador = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	class Meta:
		verbose_name = 'Director'
		verbose_name_plural = 'Directores'
		unique_together = ('identificador','tipo_documento','numero_documento','pais')
	def __str__(self):
		return str(self.primer_nombre) + ' ' + str(self.segundo_nombre) + '-' + str(self.primer_apellido) + ' ' + str(self.segundo_apellido)
	def save(self):
		self.primer_nombre = self.primer_nombre.title()
		self.segundo_nombre = self.segundo_nombre.title()
		self.primer_apellido = self.primer_apellido.title()
		self.segundo_apellido = self.segundo_apellido.title()
		super(Directores, self).save()