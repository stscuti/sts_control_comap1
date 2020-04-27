from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractUser)



class ManejadorUsuario(BaseUserManager):
# crea y guarda a un usuario con el correo y contraseñas dadas
	def create_user(self, identificador, correo, password=None):
		
		if not identificador:
			raise ValueError('Usuarios deben tener un identificador de Empresas o Persona Física')
		if not correo:
			raise ValueError('Usuarios deben tener un correo electronico valido')

		usuario = self.model(
			identificador=identificador,
			correo=self.normalize_email(correo),
		)

		usuario.set_password(password)
		usuario.save(using=self._db)
		return usuario

# crea y guarda un usuario staff
	def create_staffuser(self, identificador, correo, password):
		usuario = self.create_user(
			identificador,
			correo,
			password=password,
		)
		usuario.staff = True
		usuario.save(using=self._db)
		return usuario

# crea y guarda a un super-usuario
	def create_superuser(self, identificador, correo, password):
		usuario = self.create_user(
			identificador=identificador,
			correo=correo,
			password = password,
		)
		usuario.staff = True
		usuario.admin = True
		usuario.is_superuser = True
		usuario.save(using=self._db)
		return usuario


class Usuario(AbstractUser):
	username = None
	first_name = None
	last_name = None
	email = None
	identificador = models.BigIntegerField(primary_key=True, help_text='Para Empresas es el numero de RUT, para Personas Fisicas es el numero de CI')
	correo = models.EmailField(verbose_name='correo electronico', max_length=100, help_text='Correo Electronico para comunicaciones') #unique=True
	direccion = models.CharField(max_length=100, null=True, blank=True, help_text='Direccion')
	telefono = models.CharField(max_length=50, null=True, blank=True, help_text='Telefono Fijo')
	celular = models.CharField(max_length=50, help_text='Celular')
	opciones_tipo_usuarios = (
	        ('Contribuyente', 'Contribuyente'),
	        ('Consultor', 'Consultor'),
	        ('Funcionario', 'Funcionario'),
	        ('Administrador', 'Administrador'),
	    )
	tipo_usuario = models.CharField(max_length=20, choices=opciones_tipo_usuarios, default='Contribuyente', help_text='Tipo de Usuario') 

	active = models.BooleanField('Activo', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
	staff = models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')
	admin = models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')

	solicitante = models.BooleanField(default=True)
	ventanilla_unica = models.BooleanField(default=False)
	coordinador_ventanilla_unica = models.BooleanField(default=False)
	evaluador = models.BooleanField(default=False)
	evaluador_sectorial = models.BooleanField(default=False)
	coordinador_evaluador_sectorial = models.BooleanField(default=False)
	aprobador_sectorial = models.BooleanField(default=False)
	coordinador_aprobador_sectorial = models.BooleanField(default=False)
	evaluador_comap = models.BooleanField(default=False)
	control_contable = models.BooleanField(default=False)
	coordinador_control_contable = models.BooleanField(default=False)
	control_obra_civil = models.BooleanField(default=False)
	coordinador_control_obra_civil = models.BooleanField(default=False)
	control_juridico = models.BooleanField(default=False)
	responsable_mef = models.BooleanField(default=False)
	responsable_miem = models.BooleanField(default=False)
	responsable_mgap = models.BooleanField(default=False)
	responsable_mintur = models.BooleanField(default=False)
	responsable_mtss = models.BooleanField(default=False)
	coordinacion = models.BooleanField(default=False)
	coordinacion_general = models.BooleanField(default=False)

	ministerio_mef = models.BooleanField(default=False)
	ministerio_miem = models.BooleanField(default=False)
	ministerio_mgap = models.BooleanField(default=False)
	ministerio_mintur = models.BooleanField(default=False)
	ministerio_mtss = models.BooleanField(default=False)

	#Establecer Manejador del modelo
	objects = ManejadorUsuario()

	USERNAME_FIELD = 'identificador'
	REQUIRED_FIELDS = ['correo']

	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'


	def get_full_name(self):
		return str(self.identificador)

	def get_short_name(self):
		return str(self.identificador)

	def has_perm(self, perm, obj=None):
		"¿El usuario cuenta con un permiso especifico?"
		return True

	def has_module_perms(self, app_label):
		"¿El usuario cuenta con los permisos para ver una app en especifico?"
		return True

	@property
	def is_staff(self):
		"¿El usuario es staff (no super-usuario)?"	
		return self.staff

	@property
	def is_admin(self):
		"¿El usuario es un administrador (super-usuario)?"
		return self.admin
	
	@property
	def is_active(self):
		"¿El usuario esta activo?"	
		return self.active

	def __str__(self):
		return str(self.identificador)

class Usuario_Contribuyente(models.Model):
	identificador = models.OneToOneField('Usuario', on_delete=models.CASCADE, help_text='Para Empresas es el numero de RUT')
	razon_social = models.CharField(max_length=150, help_text='Razon Social')
	nombre_comercial = models.CharField(max_length=150, help_text='Nombre Comercial')
	domicilio_fiscal = models.CharField(max_length=150, help_text='Domicilio Fiscal')
	domicilio_constituido = models.CharField(max_length=150, help_text='Domicilio Constituido')
	n_bps = models.IntegerField(help_text='Numero de registro en BPS')
	n_mtss = models.IntegerField(help_text='Numero de registro en MTSS')

	class Meta:
		verbose_name = 'Contribuyente'
		verbose_name_plural = 'Contribuyentes'

	def __str__(self):
		return self.identificador + ' ' + self.razon_social

class Usuario_Personas_Fisicas(models.Model):
	identificador = models.OneToOneField('Usuario', on_delete=models.CASCADE, help_text='Para Personas Fisicas es el numero de CI')
	nombre1 = models.CharField(max_length=50, help_text='Primer Nombre')
	nombre2 = models.CharField(max_length=50, null=True, blank=True, help_text='Segundo Nombre')
	apellido1 = models.CharField(verbose_name='Primer Apellido',max_length=50, help_text='Primer Apellido')
	apellido2 = models.CharField(verbose_name='Segundo Apellido',max_length=50, help_text='Segundo Apellido')

	class Meta:
		verbose_name = 'Persona_Fisica'
		verbose_name_plural = 'Personas_Fisicas'

	def __str__(self):
		return self.identificador + ' ' + self.nombre1 + ' ' + self.apellido1

class Activacion(models.Model):
    identificador = models.OneToOneField(Usuario, related_name='Activacion', on_delete=models.CASCADE) #1 to 1 link with Django User
    activation_key = models.CharField(max_length=200)
    key_expires = models.DateTimeField()

