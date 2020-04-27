from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import AdminFormCreacionUsuario, AdminFormActualizar
from .models import Usuario


# Register your models here.

class UserAdmin(BaseUserAdmin):
	# Fromulario para crear y actualizar instancias de usuario
	form = AdminFormActualizar
	add_form = AdminFormCreacionUsuario

	# Los campos que seran utilizados para mostrar el modelo de Usuario.
	list_display = ('correo', 'admin')
	list_filter = ('admin',)
	fieldsets = (
		(None, {'fields': ('correo', 'password')}),
		('Informacion Personal', {'fields': ('nombre1', 'nombre2', 'apellido1', 'apellido2', 'direccion', 'telefono', 'celular')}),
		('Permisos Django', {'fields': ('admin', 'staff', 'active', 'tramitador', 'ventanilla', 'evaluador', 'coordinacion', 'control_contable', 'control_obra')}),
	)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('correo', 'password1', 'password2')}
		),
	)
	search_fields = ('correo',)
	ordering = ('correo',)
	filter_horizontal = ()

admin.site.register(Usuario, UserAdmin)
