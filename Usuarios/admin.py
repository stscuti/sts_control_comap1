from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import AdminFormCreacionUsuario, AdminFormActualizar
from .models import Usuario, Usuario_Contribuyente, Usuario_Personas_Fisicas


# Register your models here.

class UserAdmin(BaseUserAdmin):
	# Fromulario para crear y actualizar instancias de usuario
	form = AdminFormActualizar
	add_form = AdminFormCreacionUsuario

	# Los campos que seran utilizados para mostrar el modelo de Usuario.
	list_display = ('identificador','correo', 'admin')
	list_filter = ('admin',)
	fieldsets = (
		(None, {'fields': ('identificador','correo', 'password')}),
		('Informacion Comun', {'fields': ('direccion', 'telefono', 'celular','tipo_usuario')}),
		('Permisos Django', {'fields': ('admin', 'staff', 'active')}),
		('Permisos Aplicacion', {'fields': ('solicitante',	'ventanilla_unica', 'coordinador_ventanilla_unica', 'evaluador', 'evaluador_sectorial', 'coordinador_evaluador_sectorial', \
				'aprobador_sectorial', 'coordinador_aprobador_sectorial', 'evaluador_comap', 'control_contable', 'coordinador_control_contable', \
					'control_obra_civil', 'coordinador_control_obra_civil', 'control_juridico', 'responsable_mef', 'responsable_miem', 'responsable_mgap', \
						'responsable_mintur', 'responsable_mtss', 'coordinacion', 'coordinacion_general', 'ministerio_mef', 'ministerio_miem', 'ministerio_mgap', \
							'ministerio_mintur', 'ministerio_mtss','groups','user_permissions')}),
	)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('identificador','correo', 'password1', 'password2')}
		),

		('Informacion Comun', {'fields': ('direccion', 'telefono', 'celular','tipo_usuario')}),
		('Permisos Django', {'fields': ('admin', 'staff', 'active')}),
		('Permisos Aplicacion', {'fields': ('tramitador', 'ventanilla', 'evaluador', 'control_contable', 'control_obra','control_juridico','coordinacion','coordinacion_general')}),
		
	)
	search_fields = ('identificador',)
	ordering = ('identificador',)
	filter_horizontal = ()

admin.site.register(Usuario, UserAdmin)