from django.db import models
from WF.models import ModeloBaseRegistro
from Base.models import *
from Contribuyentes.models import Contribuyente

from PIL import Image
from django.db import models
from django.utils import timezone
from model_utils import Choices
from unittest.util import _MAX_LENGTH
import os
from django.utils.deconstruct import deconstructible
import uuid
# Create your models here.
'''
    1 - Datos básicos
    2 - Ministerio evaluador e indicadores
    3 - Inversiones
    4 - Datos de indicadores
    5 - Beneficios tributarios solicitados
    6 - Contacto
    7 - Documentos
    8 - Evaluación
   ''' 
class Solicitud143_Step1(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	estado_solicitud = models.CharField(max_length=50, help_text='Es el Estado de la Solicitud', verbose_name='Estado de la Solicitud', null=True, blank=True)
	asignado_solicitud = models.CharField(max_length=50, help_text='A quien esta Asignada la Solicitud', verbose_name='Solicitud: Asignado a:', null=True, blank=True)
	observacion_solicitud = models.CharField(max_length=50, help_text='Observacion de la Solicitud', verbose_name='Observacion de la Solicitud', null=True, blank=True)
	tipo_giro_datoseconomicos = models.ForeignKey('Base.TipoGiro', on_delete=models.CASCADE, verbose_name='Tipo de Giro', null=True, blank=True)
	fecha_balance_datoseconomicos = models.ForeignKey('Base.FechaBalance', on_delete=models.CASCADE, verbose_name='Fecha de Balance', null=True, blank=True)
	tipo_contribuyente_datoseconomicos = models.ForeignKey('Base.TipoContribuyente', on_delete=models.CASCADE, verbose_name='Tipo de Contribuyente', null=True, blank=True)
	actividad_agropecuaria_datoseconomicos = models.BooleanField(default=False, help_text='¿La Empresa tiene Actividad Agropecuaria?', verbose_name='¿La Empresa tiene Actividad Agropecuaria?')
	proyectos_previos_datoseconomicos = models.BooleanField(default=False, help_text='Ya cuenta con proyectos de inversión presentados ante la COMAP', verbose_name='Ya cuenta con proyectos de inversión presentados ante la COMAP')

	empresa_nueva_empresanueva = models.BooleanField(default=False, help_text='¿Es empresa nueva?', verbose_name='¿Es empresa nueva?')
	sin_facturacion_ult3ej_empresanueva = models.BooleanField(default=False, help_text='¿Sin facturación ultimos 3 ejercicios?', verbose_name='¿Sin facturación ultimos 3 ejercicios?')
	empresa_vinculada_empresanueva = models.BooleanField(default=False, help_text='¿Se encuentra vinculada con otras empresas?', verbose_name='¿Se encuentra vinculada con otras empresas?')
	empresa_vinculada_sin_factult3ej_empresanueva = models.BooleanField(default=False, help_text='¿Empresas vinculadas sin facturación en los últimos 3 ejercicios?', verbose_name='¿Empresas vinculadas sin facturación en los últimos 3 ejercicios?')

	pyme_mype = models.BooleanField(default=False, help_text='¿Es PYME?', verbose_name='¿Es PYME?')
	cantidad_empleados_mype = models.DecimalField(max_digits=20, decimal_places=6, help_text='Cantidad de Empleados', verbose_name='Cantidad de Empleados')
	ventas_netas_UI_mype = models.DecimalField(max_digits=20, decimal_places=6, help_text='Ventas Netas en UI', verbose_name='Ventas Netas en UI')
	ventas_netas_pesos_mype = models.DecimalField(max_digits=20, decimal_places=6, help_text='Ventas Netas en $', verbose_name='Ventas Netas en $')
	controlada_mype = models.BooleanField(default=False, help_text='¿Esta Controlada?', verbose_name='¿Esta Controlada?')
	controlada_superamyoe_mype = models.BooleanField(default=False, help_text='¿Empresa Controlante Supera los limites de MYPE?', verbose_name='¿Empresa Controlante Supera los limites de MYPE?')
	grupo_economico_mype = models.BooleanField(default=False, help_text='¿Pertenece a un Grupo Económico?', verbose_name='¿Pertenece a un Grupo Económico?')
	grupo_economico_supera_mype = models.BooleanField(default=False, help_text='¿El Grupo Económico supera los limites de MYPE?', verbose_name='¿El Grupo Económico supera los limites de MYPE?')
	proyeccion_cantidad_empleados_mype = models.DecimalField(max_digits=20, decimal_places=6, help_text='Proyección de Cantidad de empleos ejercicio siguiente a inicio de actividad', verbose_name='Proyección de Cantidad de empleos ejercicio siguiente a inicio de actividad')
	proyeccion_ventas_netas_UI_mype = models.DecimalField(max_digits=20, decimal_places=6, help_text='Proyección de Ventas netas en UI ejercicio siguiente inicio de actividad', verbose_name='Proyección de Ventas netas en UI ejercicio siguiente inicio de actividad')
	credito_fiscal_aportes_patronales_mype = models.BooleanField(default=False, help_text='¿Aplica crédito fiscal por aportes patronales de artículo 28º?', verbose_name='¿Aplica crédito fiscal por aportes patronales de artículo 28º?')
	usuario_parque_industrial_mype = models.BooleanField(default=False, help_text='¿Usuario de Parque Industrial?', verbose_name='¿Usuario de Parque Industrial?')

	objetivo_proyecto = models.CharField(max_length=50, help_text='Objetivo del Proyecto', verbose_name='Objetivo del Proyecto', null=True, blank=True)
	informacion_ampliada_proyecto = models.TextField(max_length=50, help_text='Informacion ampliada del Proyecto', verbose_name='Informacion ampliada del Proyecto', null=True, blank=True)
	extension_plazo_proyecto = models.BooleanField(default=False, help_text='¿Solicita extensión de plazo por lit a) artículo 4º?', verbose_name='¿Solicita extensión de plazo por lit a) artículo 4º?')
	anos_ejecucion_inversion_proyecto = models.IntegerField(help_text='Años de ejecución de inversión', verbose_name='Años de ejecución de inversión')

	class Meta:
		verbose_name = 'Solicitud143_Step1'
		verbose_name_plural = 'Solicitud143_Step1'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step1b(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	direccion = models.CharField(max_length=50, help_text='Direccion de la Localizacion', verbose_name='Direccion', null=True, blank=True)
	numero_padron = models.CharField(max_length=50, help_text='Numero de Padron', verbose_name='Numero de Padron', null=True, blank=True)
	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, help_text='Departamento', verbose_name='Departamento')
	localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE, help_text='Localidad', verbose_name='Localidad')
	localidad_ya_operaciones = models.BooleanField(default=False, help_text='¿Localidad donde ya se realizaban operaciones?', verbose_name='¿Localidad donde ya se realizaban operaciones?')
	mejoras_fijas = models.BooleanField(default=False, help_text='¿Tiene mejoras fijas?', verbose_name='¿Tiene mejoras fijas?')
	plazo_remanente_proyecto = models.IntegerField(help_text='Plazo remanente del contrato', verbose_name='Plazo remanente del contrato')
	vinculacion_juridica_proyecto = models.CharField(max_length=50, help_text='Vinculacion Juridica', verbose_name='Vinculacion Juridica', null=True, blank=True)

	class Meta:
		verbose_name = 'Solicitud143_Step1b'
		verbose_name_plural = 'Solicitud143_Step1b'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ministerio_evaluador = models.ForeignKey(Ministerios, on_delete=models.CASCADE, help_text='Ministerio Evaluador', verbose_name='Ministerio Evaluador', null=True, blank=True)
	
	class Meta:
		verbose_name = 'Solicitud143_Step2'
		verbose_name_plural = 'Solicitud143_Step2'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ministerio_evaluador = models.ForeignKey(Ministerios, on_delete=models.CASCADE, help_text='Ministerio Evaluador', verbose_name='Ministerio Evaluador', null=True, blank=True)
	
	class Meta:
		verbose_name = 'Solicitud143_Step2'
		verbose_name_plural = 'Solicitud143_Step2'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2b(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_gral_empleo = models.BooleanField(default=False, help_text='Generación de empleo', verbose_name='Generación de empleo')
	ind_gral_exportaciones = models.BooleanField(default=False, help_text='Aumento de exportaciones (en US$)', verbose_name='Aumento de exportaciones (en US$)')
	ind_gral_descentralizacion = models.BooleanField(default=False, help_text='Descentralización', verbose_name='Descentralización')
	ind_gral_TL = models.BooleanField(default=False, help_text='Utilización de tecnologías limpias', verbose_name='Utilización de tecnologías limpias')
	ind_gral_IDi = models.BooleanField(default=False, help_text='Incremento de investigación, desarrollo e innovación (I+D+i)', verbose_name='Incremento de investigación, desarrollo e innovación (I+D+i)')
	
	class Meta:
		verbose_name = 'Solicitud143_Step2b'
		verbose_name_plural = 'Solicitud143_Step2b'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2c(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_sect_FCC = models.BooleanField(default=False, help_text='Formación continua y capacitación', verbose_name='Formación continua y capacitación')
	ind_sect_DPP = models.BooleanField(default=False, help_text='Diferenciación de productos y procesos', verbose_name='Diferenciación de productos y procesos')
	ind_sect_ERV = models.BooleanField(default=False, help_text='Energías renovables de vanguardia', verbose_name='Energías renovables de vanguardia')
	ind_sect_DMC = models.BooleanField(default=False, help_text='Desarrollo de mercado de capitales', verbose_name='Desarrollo de mercado de capitales')
	
	class Meta:
		verbose_name = 'Solicitud143_Step2c'
		verbose_name_plural = 'Solicitud143_Step2c'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2d(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_sect_NTPE = models.BooleanField(default=False, help_text='Nivel Tecnológico del producto elaborado', verbose_name='Nivel Tecnológico del producto elaborado')
	ind_sect_STE = models.BooleanField(default=False, help_text='Sectores y tecnologías estrategicos', verbose_name='Sectores y tecnologías estrategicos')
	ind_sect_SIN = models.BooleanField(default=False, help_text='Sello de la Industria Nacional', verbose_name='Sello de la Industria Nacional')
	ind_sect_FCC = models.BooleanField(default=False, help_text='Formación continua y capacitación', verbose_name='Formación continua y capacitación')
	ind_sect_ERV = models.BooleanField(default=False, help_text='Energías renovables de vanguardia', verbose_name='Energías renovables de vanguardia')
	ind_sect_DMC = models.BooleanField(default=False, help_text='Desarrollo de mercado de capitales', verbose_name='Desarrollo de mercado de capitales')
	
	class Meta:
		verbose_name = 'Solicitud143_Step2d'
		verbose_name_plural = 'Solicitud143_Step2d'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2e(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_sect_SI = models.BooleanField(default=False, help_text='Servicios e Infraestructura', verbose_name='Servicios e Infraestructura')
	ind_sect_CES = models.BooleanField(default=False, help_text='Certificación de edificios sostenibles', verbose_name='Certificación de edificios sostenibles')
	ind_sect_FCC = models.BooleanField(default=False, help_text='Formación continua y capacitación', verbose_name='Formación continua y capacitación')
	ind_sect_ERV = models.BooleanField(default=False, help_text='Energías renovables de vanguardia', verbose_name='Energías renovables de vanguardia')
	ind_sect_DMC = models.BooleanField(default=False, help_text='Desarrollo de mercado de capitales', verbose_name='Desarrollo de mercado de capitales')
	
	class Meta:
		verbose_name = 'Solicitud143_Step2e'
		verbose_name_plural = 'Solicitud143_Step2e'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step2f(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_sect_ACC = models.BooleanField(default=False, help_text='Inversiones en adaptación al cambio climático', verbose_name='Inversiones en adaptación al cambio climático')
	ind_sect_DPP = models.BooleanField(default=False, help_text='Diferenciación de productos y procesos', verbose_name='Diferenciación de productos y procesos')
	ind_sect_FCC = models.BooleanField(default=False, help_text='Formación continua y capacitación', verbose_name='Formación continua y capacitación')
	ind_sect_ERV = models.BooleanField(default=False, help_text='Energías renovables de vanguardia', verbose_name='Energías renovables de vanguardia')
	ind_sect_DMC = models.BooleanField(default=False, help_text='Desarrollo de mercado de capitales', verbose_name='Desarrollo de mercado de capitales')
	
	class Meta:
		verbose_name = 'Solicitud143_Step2f'
		verbose_name_plural = 'Solicitud143_Step2f'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step3(ModeloBaseRegistro):
	tupla_ej=(('Factura','Factura'),('Presupuesto','Presupuesto'))
	tupla_imp=(('Importado','Importado'),('Plaza','Plaza'))
	tupla_nuevo=(('Nuevo','Nuevo'),('Usado','Usado'))
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	
	inv_categoria = models.ForeignKey(Categoria_Inversiones, on_delete=models.CASCADE, help_text='Categoria de Inversiones', verbose_name='Categoria de Inversiones')
	inv_subcategoria = models.ForeignKey(SubCategoria_Inversiones, on_delete=models.CASCADE, help_text='Categoria de Inversiones', verbose_name='Categoria de Inversiones')
	inv_descripcion=models.CharField(max_length=200, verbose_name='Descripcion Inversion')

	inv_ejecucion=models.CharField(choices=tupla_ej, max_length=30, default='Presupuesto', help_text='Ejecutado/Presupuesto', verbose_name='Ejecutado/Presupuesto')
	inv_numero_documento=models.CharField(max_length=100, help_text='Nº de Comprobante', verbose_name='Numero de Documento de Comprobante',null=True, blank=True)
	indicador_relacionado=models.CharField(max_length=100, help_text='Indicador Relacionado', verbose_name='Indicador Relacionado',null=True, blank=True) #Poner Listado y clave foranea
	inv_fecha=models.DateField(default=timezone.now, help_text='Fecha Documento', verbose_name='Fecha')
	inv_compra=models.CharField(choices=tupla_imp, max_length=30, default='Plaza', help_text='Plaza/Importado', verbose_name='Plaza/Importado')
	inv_nuevo_usado=models.CharField(choices=tupla_nuevo, max_length=30, default='Nuevo', help_text='Nuevo/Usado', verbose_name='Nuevo/Usado')
	inv_cantidad=models.DecimalField(max_digits=10, decimal_places=0, help_text='Cantidad', verbose_name='Cantidad', default=1)
	inv_proveedor_rut=models.CharField(max_length=200, help_text='RUT Proveedor', verbose_name='RUT Proveedor')
	inv_proveedor_nombre=models.CharField(max_length=200, help_text='Nombre Proveedor', verbose_name='Nombre Proveedor')
	inv_moneda_origen=models.CharField(max_length=200, help_text='Moneda Origen', verbose_name='Moneda Origen') #Poner Lista y asociar a cotizaciones
	inv_costo_moneda_origen=models.DecimalField(max_digits=20, decimal_places=4, help_text='Costo Moneda Origen', verbose_name='Costo Moneda Origen')
	inv_total_inversiones_UI=models.DecimalField(max_digits=20, decimal_places=4, help_text='Total de Inversion en UI',verbose_name='Total de Inversion en UI')
	inv_vida_util_anos=models.PositiveIntegerField(help_text='Vida Util en Años', verbose_name='Vida Util en Años',null=True, blank=True)
	inv_UI_utilizada=models.DecimalField(max_digits=8, decimal_places=4, help_text='UI utilizada', verbose_name='UI utilizada')
	inv_cotizacion_utilizada=models.DecimalField(max_digits=8, decimal_places=4, help_text='Cotización Utilizada', verbose_name='Cotización Utilizada')
	inv_USD_utilizado=models.DecimalField(max_digits=8, decimal_places=4, help_text='USD utilizada', verbose_name='USD utilizado')
	inv_EUR_utilizado=models.DecimalField(max_digits=8, decimal_places=4, help_text='EURO utilizado', verbose_name='EURO utilizado',null=True, blank=True)
	
	class Meta:
		verbose_name = 'Solicitud143_Step3'
		verbose_name_plural = 'Solicitud143_Step3'
		unique_together = ('contribuyente','num_expediente','inv_subcategoria','inv_descripcion','inv_numero_documento')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente + ' / ' + self.inv_subcategoria + ' / ' + self.inv_descripcion + ' / ' + self.inv_numero_documento

class Solicitud143_Step4a(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_gral_empleo_extension = models.BooleanField(default=False, help_text='Por naturaleza de inversiones requiere extensión del comienzo del período de cumplimiento', verbose_name='Extensión de Periodo')
	ind_gral_empleo_cantidad_extension = models.DecimalField(max_digits=4, decimal_places=0, help_text='Cantidad de años de extensión', verbose_name= 'Cantidad de Extensión de Periodo')
	ind_gral_empleo_motivos_extension = models.TextField(help_text='Motivos que originan la solicitud de extensión', verbose_name='Motivos que originan la solicitud de extensión')
	ano0_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en la situacion inicial', default=0)
	ano0_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en la situacion inicial', default=0)
	ano0_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en la situacion inicial', default=0)
	ano0_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en la situacion inicial', default=0)
	ano0_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en la situacion inicial', default=0)
	ano1_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 1', default=0)
	ano1_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 1', default=0)
	ano1_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 1', default=0)
	ano1_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 1', default=0)
	ano1_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 1', default=0)
	ano2_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 2', default=0)
	ano2_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 2', default=0)
	ano2_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 2', default=0)
	ano2_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 2', default=0)
	ano2_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 2', default=0)
	ano3_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 3', default=0)
	ano3_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 3', default=0)
	ano3_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 3', default=0)
	ano3_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 3', default=0)
	ano3_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 3', default=0)
	ano4_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 4', default=0)
	ano4_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 4', default=0)
	ano4_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 4', default=0)
	ano4_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 4', default=0)
	ano4_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 4', default=0)
	ano5_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 5', default=0)
	ano5_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 5', default=0)
	ano5_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 5', default=0)
	ano5_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 5', default=0)
	ano5_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 5', default=0)	
	ano6_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 6', default=0)
	ano6_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 6', default=0)
	ano6_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 6', default=0)
	ano6_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 6', default=0)
	ano6_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 6', default=0)
	ano7_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 7', default=0)
	ano7_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 7', default=0)
	ano7_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 7', default=0)
	ano7_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 7', default=0)
	ano7_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 7', default=0)
	ano8_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 8', default=0)
	ano8_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 8', default=0)
	ano8_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 8', default=0)
	ano8_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 8', default=0)
	ano8_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 8', default=0)
	ano9_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 9', default=0)
	ano9_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 9', default=0)
	ano9_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 9', default=0)
	ano9_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 9', default=0)
	ano9_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 9', default=0)
	ano10_eq40hs = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Cantidad de Personas equivalente a 40hs en el ano 10', default=0)
	ano10_men25 = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Menores de 25 anos en al ano 10', default=0)
	ano10_muj = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Mujeres en el ano 10', default=0)
	ano10_discap = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Discapacitados en el ano 10', default=0)
	ano10_rural = models.DecimalField(max_digits=8, decimal_places=4, verbose_name='Trabajadores Rurales en el ano 10', default=0)

	class Meta:
		verbose_name = 'Solicitud143_Step4_a'
		verbose_name_plural = 'Solicitud143_Step4_a'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step4b(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_gral_exportaciones_extension = models.BooleanField(default=False, help_text='Por naturaleza de inversiones requiere extensión del comienzo del período de cumplimiento', verbose_name='Extensión de Periodo')
	ind_gral_exportaciones_cantidad_extension = models.DecimalField(max_digits=4, decimal_places=0, help_text='Cantidad de años de extensión', verbose_name= 'Cantidad de Extensión de Periodo')
	ind_gral_exportaciones_motivos_extension = models.TextField(help_text='Motivos que originan la solicitud de extensión', verbose_name='Motivos que originan la solicitud de extensión')
	descripcion = models.CharField(max_length=200, verbose_name='Descripcion de Exportacion')
	ano0 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 0', default=0)
	ano1 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 1', default=0)
	ano2 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 2', default=0)
	ano3 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 3', default=0)
	ano4 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 4', default=0)
	ano5 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 5', default=0)
	ano6 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 6', default=0)
	ano7 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 7', default=0)
	ano8 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 8', default=0)
	ano9 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 9', default=0)
	ano10 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Exportaciones Ano 10', default=0)


	class Meta:
		verbose_name = 'Solicitud143_Step4_b'
		verbose_name_plural = 'Solicitud143_Step4_b'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step4c(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_gral_descentralizacion_extension = models.BooleanField(default=False, help_text='Por naturaleza de inversiones requiere extensión del comienzo del período de cumplimiento', verbose_name='Extensión de Periodo', blank=True, null=True)
	#localizacion=models.OneToOneField(Solicitud143_Step1b, on_delete=models.CASCADE, verbose_name='Localizacion')
	operaciones=models.ForeignKey(Localizacion_Operaciones, on_delete=models.CASCADE, verbose_name='Ya tenia Operaciones:')
	departamento=models.ForeignKey(Listado_Puntaje_Departamentos, on_delete=models.CASCADE, verbose_name='Departamento')
	inversion_UI=models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Inversion Total en UI')

	def _get_empleo_requerido(self):
		if self.operaciones == "Nueva Localidad":
			return 0
		else:
			return 1
	empleo_requerido = property(_get_empleo_requerido)

	class Meta:
		verbose_name = 'Solicitud143_Step4_c'
		verbose_name_plural = 'Solicitud143_Step4_c'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step4d(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_gral_TL_extension = models.BooleanField(default=False, help_text='Por naturaleza de inversiones requiere extensión del comienzo del período de cumplimiento', verbose_name='Extensión de Periodo')
	ind_gral_TL_cantidad_extension = models.DecimalField(max_digits=4, decimal_places=0, help_text='Cantidad de años de extensión', verbose_name= 'Cantidad de Extensión de Periodo')
	ind_gral_TL_motivos_extension = models.TextField(help_text='Motivos que originan la solicitud de extensión', verbose_name='Motivos que originan la solicitud de extensión')
	detalle=models.CharField(max_length=100, verbose_name='Descripcion de Inversion en Tecnologias Limpias')
	ano1 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Inversiones en Tecnologias Limpias Ano 1 en UI')
	ano2 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Inversiones en Tecnologias Limpias Ano 2 en UI')


	class Meta:
		verbose_name = 'Solicitud143_Step4_d'
		verbose_name_plural = 'Solicitud143_Step4_d'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step4e(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	


	class Meta:
		verbose_name = 'Formulario adicional: Tecnologías limpias'
		verbose_name_plural = 'Formulario adicional: Tecnologías limpias'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step4f(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	ind_gral_IDi_extension = models.BooleanField(default=False, help_text='Por naturaleza de inversiones requiere extensión del comienzo del período de cumplimiento', verbose_name='Extensión de Periodo')
	ind_gral_IDi_cantidad_extension = models.DecimalField(max_digits=4, decimal_places=0, help_text='Cantidad de años de extensión', verbose_name= 'Cantidad de Extensión de Periodo')
	ind_gral_IDi_motivos_extension = models.TextField(help_text='Motivos que originan la solicitud de extensión', verbose_name='Motivos que originan la solicitud de extensión')
	detalle=models.CharField(max_length=100, verbose_name='Descripcion de Inversion en I+D+i')
	ano1 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Inversiones en I+D+i Ano 1 en UI')
	ano2 = models.DecimalField(max_digits=20, decimal_places=4, verbose_name='Inversiones en I+D+i Ano 2 en UI')


	class Meta:
		verbose_name = 'Solicitud143_Step4_f'
		verbose_name_plural = 'Solicitud143_Step4_f'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step4g(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)


	class Meta:
		verbose_name = 'Formulario adicional: Formulario ANII'
		verbose_name_plural = 'Formulario adicional: Formulario ANII'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

# Faltan Indicadores Sectoriales

'''
'''

class Solicitud143_Step5(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	beneficios_solicitados_IRAE = models.BooleanField(default=False, help_text='Solicita IRAE', verbose_name='Solicita IRAE')
	beneficios_solicitados_PATRIMONIO = models.BooleanField(default=False, help_text='Solicita IPAT', verbose_name='Solicita IPAT')
	beneficios_solicitados_IVA = models.BooleanField(default=False, help_text='Solicita IVA', verbose_name='Solicita IVA')
	beneficios_solicitados_IMPORTADOS = models.BooleanField(default=False, help_text='Solicita Tasas y tributos a la Importación', verbose_name='Solicita Tasas y tributos a la Importación')
	beneficios_solicitados_Transitorios21808 = models.BooleanField(default=False, help_text='Solicita Beneficios Transitorios del Dec 218/08', verbose_name='Solicita Beneficios Transitorios del Dec 218/08')


	class Meta:
		verbose_name = 'Beneficios tributarios solicitados'
		verbose_name_plural = 'Beneficios tributarios solicitados'
		unique_together = ('contribuyente','num_expediente')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente

class Solicitud143_Step6a(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	
	contacto_tipo_documento=models.ForeignKey(Tipo_Documento, on_delete=models.CASCADE, verbose_name='Tipo de Documento')
	contacto_numero_documento=models.DecimalField(max_digits=20, decimal_places=0, verbose_name='Número de Documento')
	contacto_nombre=models.CharField(max_length=100, verbose_name='Nombre del Contacto para el Proyecto')
	contacto_apellido=models.CharField(max_length=100, verbose_name='Apellido del Contacto para el Proyecto')
	contacto_direccion=models.CharField(max_length=200, verbose_name='Direccion')
	contacto_telefono=models.DecimalField(max_digits=12, decimal_places=0, verbose_name='Telefono de Contacto')
	contacto_mail=models.EmailField(max_length=200, verbose_name='Email de Contacto')


	class Meta:
		verbose_name = 'Contacto autorizado por el proyecto'
		verbose_name_plural = 'Contacto autorizado por el proyecto'
		unique_together = ('contribuyente','num_expediente', 'contacto_tipo_documento', 'contacto_numero_documento')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente + ' / ' + self.contacto_tipo_documento + ' / ' + self.contacto_numero_documento

class Solicitud143_Step6b(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	
	notificaciones_tipo_documento=models.ForeignKey(Tipo_Documento, on_delete=models.CASCADE, verbose_name='Tipo de Documento')
	notificaciones_numero_documento=models.DecimalField(max_digits=20, decimal_places=0, verbose_name='Número de Documento')
	notificaciones_nombre=models.CharField(max_length=100, verbose_name='Nombre del Contacto para el Proyecto')
	notificaciones_apellido=models.CharField(max_length=100, verbose_name='Apellido del Contacto para el Proyecto')
	notificaciones_direccion=models.CharField(max_length=200, verbose_name='Direccion')
	notificaciones_telefono=models.DecimalField(max_digits=12, decimal_places=0, verbose_name='Telefono de Contacto')
	notificaciones_mail=models.EmailField(max_length=200, verbose_name='Email de Contacto')

	class Meta:
		verbose_name = 'Contacto para notificaciones por el proyecto'
		verbose_name_plural = 'Contacto para notificaciones por el proyecto'
		unique_together = ('contribuyente','num_expediente', 'notificaciones_tipo_documento', 'notificaciones_numero_documento')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente + ' / ' + self.notificaciones_tipo_documento + ' / ' + self.notificaciones_numero_documento

class Solicitud143_Step7(ModeloBaseRegistro):
	contribuyente = models.ForeignKey(Contribuyente, on_delete=models.CASCADE, help_text='Contribuyente', verbose_name='Contribuyente')
	#num_expediente=models.ForeignKey(Solicitud143_Step1, on_delete=models.CASCADE, help_text='Numero de Expediente', verbose_name='Numero de Expediente')
	def Incrementar():
		ultimo = Solicitud143_Step1.objects.all().order_by('num_expediente').last()
		start = 80000
		if not ultimo:
				return int(start)
		registro = ultimo.num_expediente
		registro_int = ultimo.num_expediente
		nuevo_registro_int = registro_int + 1
		return nuevo_registro_int
	def get_expediente_url(self, filename): 
		return "media/Expedientes/%(numero_expediente)s/%(filename)s" % {
			'numero_expediente': self.num_expediente.num_expediente,
			'filename': filename,
		}
	num_expediente=models.BigIntegerField(default=Incrementar, verbose_name='Numero de Expediente',primary_key=True)
	
	documentacion_tipo_documento=models.ForeignKey(Tipo_DocumentoPresentar, on_delete=models.CASCADE, verbose_name='Tipo de Documento a Presentar')
	documentacion_descripcion=models.CharField(max_length=200, verbose_name='Descripción')
	#documentacion_documento=models.FileField(verbose_name='Documentos',null=True, blank=True,upload_to=get_expediente_url)

	class Meta:
		verbose_name = 'Contacto para notificaciones por el proyecto'
		verbose_name_plural = 'Contacto para notificaciones por el proyecto'
		unique_together = ('contribuyente','num_expediente', 'documentacion_tipo_documento', 'documentacion_descripcion')

	def __str__(self):
		return self.contribuyente + ' / ' + self.num_expediente + ' / ' + self.documentacion_tipo_documento + ' / ' + self.documentacion_descripcion