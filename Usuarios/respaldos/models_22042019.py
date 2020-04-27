from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractUser)

# Create your models here.
class ManejadorUsuario(BaseUserManager):
# crea y guarda a un usuario con el correo y contraseñas dadas
	def create_user(self, correo, password=None):
		if not correo:
			raise ValueError('Usuarios deben tener un correo electronico valido')

		usuario = self.model(
			correo=self.normalize_email(correo),
		)

		usuario.set_password(password)
		usuario.save(using=self._db)
		return usuario

# crea y guarda un usuario staff
	def create_staffuser(self, correo, password):
		usuario = self.create_user(
			correo,
			password=password,
		)
		usuario.staff = True
		usuario.save(using=self._db)
		return usuario

# crea y guarda a un super-usuario
	def create_superuser(self, correo, password):
		usuario = self.create_user(
			correo,
			password = password,
		)
		usuario.staff = True
		usuario.admin = True
		usuario.save(using=self._db)
		return usuario

class Usuario(AbstractUser):
	correo = models.EmailField(verbose_name='correo electronico', max_length=100, unique=True)
	nombre1 = models.CharField(max_length=50)
	nombre2 = models.CharField(max_length=50, null=True, blank=True)
	apellido1 = models.CharField(verbose_name='Primer Apellido',max_length=50)
	apellido2 = models.CharField(verbose_name='Segundo Apellido',max_length=50)
	direccion = models.CharField(max_length=100, null=True, blank=True)
	telefono = models.CharField(max_length=50, null=True, blank=True)
	celular = models.CharField(max_length=50)

	active = models.BooleanField('Activo', default=True)
	staff = models.BooleanField(default=False)
	admin = models.BooleanField(default=False)

	tramitador = models.BooleanField(default=True)
	ventanilla = models.BooleanField(default=False)
	evaluador = models.BooleanField(default=False)
	coordinacion = models.BooleanField(default=False)
	control_contable = models.BooleanField(default=False)
	control_obra = models.BooleanField(default=False)

	#Establecer Manejador del modelo
	objects = ManejadorUsuario()

	USERNAME_FIELD = 'correo'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = 'Usuario'
		verbose_name_plural = 'Usuarios'

	def get_full_name(self):
		return self.nombre1 + ' ' + self.nombre2 + ', ' + self.apellido1 + ' ' + self.apellido2

	def get_short_name(self):
		return self.nombre1

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
		return self.nombre1 + ' ' + self.apellido1 + ' ' + self.correo









