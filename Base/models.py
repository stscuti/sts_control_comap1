from django.db import models
from Usuarios.models import Usuario
from WF.models import ModeloBaseRegistro
# Create your models here.

class Pais(ModeloBaseRegistro):
	descripcion = models.CharField(max_length=100, help_text='Pais', verbose_name='Pais', unique=True)

	class Meta:
		verbose_name = 'Pais'
		verbose_name_plural = 'Paises'
		#unique_together = ('descripcion')
	def __str__(self):
		#return str(self.descripcion)
		return '{}'.format(self.descripcion)
	def save(self):
		self.descripcion = self.descripcion.upper()
		super(Pais, self).save()
	

class Departamento(ModeloBaseRegistro):
	pais = models.ForeignKey(Pais, related_name="has_paises", on_delete=models.CASCADE, help_text='Pais', verbose_name='Pais')
	descripcion = models.CharField(max_length=100, help_text='Departamento', verbose_name='Departamento')

	class Meta:
		verbose_name = 'Departamento'
		verbose_name_plural = 'Departamento'
		unique_together = ('pais','descripcion')
	def __str__(self):
		return str(self.pais) + " - " + str(self.descripcion) 
	def save(self):
		self.descripcion = self.descripcion.upper()
		self.uc = self.uc
		super(Departamento, self).save()

class Localidad(ModeloBaseRegistro):
	departamento = models.ForeignKey(Departamento, related_name="has_departamento", on_delete=models.CASCADE, help_text='Departamento', verbose_name='Departamento')
	descripcion = models.CharField(max_length=100, help_text='Localidad', verbose_name='Localidad')

	class Meta:
		verbose_name = 'Localidad'
		verbose_name_plural = 'Localidad'
		unique_together = ('departamento','descripcion')
	def __str__(self):
		return str(self.departamento) + ' - ' + str(self.descripcion)
	def save(self):
		self.descripcion = self.descripcion.title()
		super(Localidad, self).save()

class Tipo_Documento(ModeloBaseRegistro):
	descripcion = models.CharField(max_length=50, help_text='Tipo de Documento', verbose_name='Tipo de Documento')
	class Meta:
		verbose_name = 'Tipo de Documento'
		verbose_name_plural = 'Tipo de Documento'
		#unique_together = ('descripcion')
	def __str__(self):
		#return str(self.descripcion)
		return '{}'.format(self.descripcion)
	def save(self):
		self.descripcion = self.descripcion.upper()
		super(Tipo_Documento, self).save()

class Ministerios(ModeloBaseRegistro):
	descripcion = models.CharField(max_length=100, help_text='Ministerios', verbose_name='Ministerios')
	class Meta:
		verbose_name = 'Ministerio'
		verbose_name_plural = 'Ministerios'
		#unique_together = ('descripcion')
	def __str__(self):
		#return str(self.descripcion)
		return '{}'.format(self.descripcion)
	def save(self):
		self.descripcion = self.descripcion.upper()
		super(Ministerios, self).save()

class TipoGiro(ModeloBaseRegistro):
	
	descripcion = models.CharField(max_length=100, help_text='Descripcion del Giro', verbose_name='Descripcion del Giro')
	class Meta:
		verbose_name = 'Tipo del Giro'
		verbose_name_plural = 'Tipo del Giro'
		#unique_together = ('descripcion')
	def __str__(self):
		#return str(self.descripcion)
		return '{}'.format(self.descripcion)
	def save(self):
		self.descripcion = self.descripcion.upper()
		super( TipoGiro, self).save()

class GiroCIIU(ModeloBaseRegistro):
	tipo_giro = models.ForeignKey(TipoGiro, related_name="has_giro", on_delete=models.CASCADE, help_text='Tipo Giro CIIU', verbose_name='Tipo Giro CIIU')
	codigo_giro = models.BigIntegerField(help_text='Codigo giro del CIIU', verbose_name='Codigo giro del CIIU')
	descripcion = models.CharField(max_length=100, help_text='Descripcion del Giro', verbose_name='Descripcion del Giro')
	class Meta:
		verbose_name = 'Descripcion del Giro'
		verbose_name_plural = 'Descripcion del Giro'
		#unique_together = ('descripcion')
	def __str__(self):
		#return str(self.descripcion)
		return '{}'.format(self.descripcion)
	def save(self):
		self.descripcion = self.descripcion.upper()
		super(GiroCIIU, self).save()

class FechaBalance(ModeloBaseRegistro):
	tupla_fecha_balance = (('31/01','Enero - 31/01'),('28/02','Febrero - 28/02'),('31/03','Marzo - 31/03'),('30/04','Abril - 30/04'),('31/05','Mayo - 31/05'),('30/06','Junio - 30/06'),('31/07','Julio - 31/07'),('31/08','Agosto - 31/08'),('30/09','Septiembre - 30/09'),('31/10','Octubre - 31/10'),('30/11','Noviembre - 30/11'),('31/12','Diciembre - 31/12'))
	fecha_balance = models.CharField(choices=tupla_fecha_balance, max_length=50, help_text='Fecha de Cierre de Balance', verbose_name='Fecha Balance', unique=True)
	class Meta:
		verbose_name = 'Fecha de Balance'
		verbose_name_plural = 'Fecha de Balance'
		#unique_together = ('descripcion')
	def __str__(self):
		#return str(self.descripcion)
		return '{}'.format(self.fecha_balance)
	def save(self):
		self.fecha_balance = self.fecha_balance.upper()
		super( FechaBalance, self).save()

class TipoContribuyente(ModeloBaseRegistro):
	
	tipo_contribuyente = models.CharField(max_length=50, help_text='Tipo de Contribuyente', verbose_name='Tipo de Contribuyente')
	class Meta:
		verbose_name = 'Tipo de Contribuyente'
		verbose_name_plural = 'Tipo de Contribuyente'
		#unique_together = ('descripcion')
	def __str__(self):
		#return str(self.descripcion)
		return '{}'.format(self.tipo_contribuyente)
	def save(self):
		self.tipo_contribuyente = self.tipo_contribuyente.upper()
		super( TipoContribuyente, self).save()

class Categoria_Inversiones(ModeloBaseRegistro):
	
	categoria = models.CharField(max_length=50, help_text='Categoria de Inversiones', verbose_name='Categoria de Inversiones', unique=True)
	class Meta:
		verbose_name = 'Categoria de Inversiones'
		verbose_name_plural = 'Categoria de Inversiones'
		#unique_together = ('descripcion')
	def __str__(self):
		#return str(self.descripcion)
		return '{}'.format(self.categoria)
	def save(self):
		self.categoria = self.categoria.upper()
		super(Categoria_Inversiones, self).save()

class SubCategoria_Inversiones(ModeloBaseRegistro):
	categoria = models.ForeignKey(Categoria_Inversiones, related_name="has_categorias", on_delete=models.CASCADE, help_text='Categorias de Inversiones', verbose_name='Categorias de Inversiones')
	subcategoria = models.CharField(max_length=50, help_text='SubCategoria de Inversiones', verbose_name='SubCategoria de Inversiones')
	class Meta:
		verbose_name = 'SubCategoria de Inversiones'
		verbose_name_plural = 'SubCategoria de Inversiones'
		unique_together = ('categoria','subcategoria',)
	def __str__(self):
		#return str(self.descripcion)
		return '{}'.format(self.subcategoria)
	def save(self):
		self.subcategoria = self.subcategoria.upper()
		super(SubCategoria_Inversiones, self).save()

class Exp_Bienes_Servicios(ModeloBaseRegistro):
	tupla_BsScios = (('Bienes','Bienes'),('Servicios','Servicios'))
	tipo = models.CharField(choices=tupla_BsScios, max_length=100, default='Bienes', verbose_name='Bienes/Servicios')
	descripcion = models.CharField(max_length=200, verbose_name='Descripcion de Exportacion')
	porcentaje = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Porcentaje')

	def __str__(self):
		return self.tipo + '_' + self.descripcion
	class Meta:
		unique_together = ('tipo','descripcion')
		verbose_name = 'Tipo de Exportaciones de Bienes y Servicios'
		verbose_name_plural = 'Tipo de Exportaciones de Bienes y Servicios'

class Localizacion_Operaciones(ModeloBaseRegistro):
	tupla_operaciones=(('Nueva Localidad','Nueva Localidad'),('Localidad donde ya se realizan operaciones','Localidad donde ya se realizan operaciones'))
	tipo = models.CharField(choices=tupla_operaciones, max_length=100, unique=True, default='Nueva Localidad', verbose_name='Localidad Nueva/Anterior')
	def __str__(self):
		return self.tipo
	class Meta:
		verbose_name = "Opciones Localizacion"
		verbose_name_plural = "Opciones Localizacion"

class Listado_Puntaje_Departamentos(ModeloBaseRegistro):
	tupla_departamentos=sorted((('Montevideo','Montevideo'),('Canelones','Canelones'),('Artigas','Artigas'),('Cerro Largo','Cerro Largo'),('Salto','Salto'),('Durazno','Durazno'),('Tacuarembo','Tacuarembo'),('Rivera','Rivera'),('Treinta y Tres','Treinta y Tres'),('Paysandu','Paysandu'),('Lavalleja','Lavalleja'),('Soriano','Soriano'),('Rocha','Rocha'),('Florida','Florida'),('Rio Negro','Rio Negro'),('San Jose','San Jose'),('Flores','Flores'),('Colonia','Colonia'),('Maldonado','Maldonado')))
	tupla_capital_resto=(('Capital','Capital'),('Resto','Resto'))
	departamento = models.CharField(choices=tupla_departamentos, max_length=100, default='Montevideo', verbose_name='Departamentos de Uruguay')
	cap_int = models.CharField(choices=tupla_capital_resto, max_length=100, default='Capital', verbose_name='Capital/Interior')
	puntaje = models.PositiveIntegerField(verbose_name='Puntaje Asignado')
	def __str__(self):
		return self.departamento + '_' + self.cap_int
	class Meta:
		unique_together = ('departamento', 'cap_int')
		verbose_name = "Listado de Departamentos y Puntajes"
		verbose_name_plural = "Listado de Departamentos y Puntajes"

class Tipo_DocumentoPresentar(ModeloBaseRegistro):
	descripcion = models.CharField(max_length=50, help_text='Tipo de Documento', verbose_name='Tipo de Documento')
	class Meta:
		verbose_name = 'Tipo de Documento a Presentar'
		verbose_name_plural = 'Tipo de Documento a Presentar'
		#unique_together = ('descripcion')
	def __str__(self):
		#return str(self.descripcion)
		return '{}'.format(self.descripcion)
	def save(self):
		self.descripcion = self.descripcion.upper()
		super(Tipo_DocumentoPresentar, self).save()