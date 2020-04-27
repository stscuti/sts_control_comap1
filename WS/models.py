from django.db import models
from Usuarios.models import Usuario, Usuario_Contribuyente, Usuario_Personas_Fisicas
from django_pandas.managers import DataFrameManager


# Create your models here.

class ModeloBase(models.Model):
	estado = models.BooleanField(default=True)
	fc = models.DateTimeField(auto_now_add=True)
	fm = models.DateTimeField(auto_now=True)
	uc = models.BigIntegerField(blank=True, null=True)
	um = models.BigIntegerField(blank=True, null=True)

	class Meta:
		abstract = True

class Cotizaciones(ModeloBase):
	identificador = models.ForeignKey('Usuarios.Usuario', on_delete=models.CASCADE, verbose_name='Usuarios')
	fecha = models.DateField(help_text='Es la Fecha de la Cotizacion', verbose_name='Fecha')
	moneda = models.IntegerField(help_text='Es el codigo BCU de la Moneda', verbose_name='Moneda')
	nombre = models.CharField(max_length=50, help_text='Es el Nombre de la Moneda', verbose_name='Nombre')
	codigo_ISO = models.CharField(max_length=4, help_text='Es el codigo ISO de la Moneda', verbose_name='CodigoISO')
	emisor = models.CharField(max_length=20, help_text='Es el Pais Emisor de la Moneda', verbose_name='Emisor')
	tcc = models.DecimalField(max_digits=20, decimal_places=6, help_text='Es la cotizacion del Tipo de Cambio Comprador', verbose_name='TCC')
	tcv = models.DecimalField(max_digits=20, decimal_places=6, help_text='Es la cotizacion del Tipo de Cambio Vendedor', verbose_name='TCV')
	arbact = models.DecimalField(max_digits=20, decimal_places=6, help_text='Arbitraje', verbose_name='ArbAct')
	forma_arbitrar = models.IntegerField(help_text='Forma de Arbitrar: 0 = Unidad de Moneda por Dolares EEUU 1 = Dolares de EEUU por Unidad de Moneda', verbose_name='FormaArbitrar')

	objects = models.Manager()
	pdobjects = DataFrameManager()  # Pandas-Enabled Manager



	class Meta:
		verbose_name = 'Cotizacion'
		verbose_name_plural = 'Cotizaciones'
		unique_together = ('fecha','moneda','nombre')

	def __str__(self):
		return self.fecha + ' ' + self.moneda + ' ' + self.nombre