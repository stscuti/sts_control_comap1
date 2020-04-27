from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm, UserChangeForm
from .models import Usuario, Usuario_Contribuyente, Usuario_Personas_Fisicas
from betterforms.multiform import MultiModelForm

'''
# crear usuario en consola
class FormRegistro(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmar Password',widget=forms.PasswordInput)

	class Meta:
		model = Usuario
		fields = ('correo',)

	def clean_email(self):
		correo = self.cleaned_data.get('correo')
		qs = Usuario.objects.filter(correo=correo)
		if qs.exists():
			raise forms.ValidationError("Correo ya Registrado")
		return correo

	def clean_password2(self):
		# Chequear que contraseñas coincidan
		password1=self.cleaned_data.get("password1")
		password2=self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Contraseñas no coinciden")
		return password2
	
# Formulario para crear nuevos usuarios. Incluye todos los campos requeridos mas contraseñas repetidas para confirmacion
class AdminFormCreacionUsuario(forms.ModelForm):
	password1 = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmar Contrasena', widget=forms.PasswordInput)

	class Meta:
		model = Usuario
		fields = ('correo', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'direccion', 'telefono', 'celular')

	def clean_password2(self):
		#Chequear que las contraseñas coincidan
		password1=self.cleaned_data.get("password1")
		password2=self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Contraseñas no coinciden")
		return password2
	def save(self, commit=True):
		#Guardar contraseña en formato Hash
		usuario = super(AdminFormCreacionUsuario, self).save(commit=False)
		usuario.set_password(self.cleaned_data["password1"])
		if commit:
			usuario.save()
		return usuario


# formulario para actualizar usuarios. Incluye todos los campos requeridos, pero reemplaza el campo de contraseña
# con el hash guardado en el admin de Django.
class AdminFormActualizar(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = Usuario
		fields = ('correo', 'nombre1', 'nombre2', 'apellido1', 'apellido2', 'direccion', 'telefono', 'celular')

	def clean_password(self):
	# regresa el valor inicial, sin importar lo que el usuario escriba
	# se realiza ya que el campo no tiene acceso al valor inicial,
	# las contraseñas en Django requieren un formato especifico
		return self.initial['password']

'''

# crear usuario en consola
class FormRegistro(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmar Password',widget=forms.PasswordInput)

	class Meta:
		model = Usuario
		fields = ('identificador','correo',)

	def clean_email(self):
		identificador = self.cleaned_data.get('identificador')
		qs_identificador = Usuario.objects.filter(identificador=identificador)
		if qs_identificador.exists():
			raise forms.ValidationError("Identificador ya Registrado")
		return identificador
		correo = self.cleaned_data.get('correo')
		qs = Usuario.objects.filter(correo=correo)
		if qs.exists():
			raise forms.ValidationError("Correo ya Registrado")
		return correo

	def clean_password2(self):
		# Chequear que contraseñas coincidan
		password1=self.cleaned_data.get("password1")
		password2=self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Contraseñas no coinciden")
		return password2

# Formulario para crear nuevos usuarios. Incluye todos los campos requeridos mas contraseñas repetidas para confirmacion
class AdminFormCreacionUsuario(UserCreationForm):
	password1 = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirmar Contrasena', widget=forms.PasswordInput)
	#identificador = forms.IntegerField(unique=True)

	class Meta(UserCreationForm):
		model = Usuario
		fields = ('identificador','correo', 'direccion', 'telefono', 'celular', 'tipo_usuario')

	def clean_password2(self):
		#Chequear que las contraseñas coincidan
		password1=self.cleaned_data.get("password1")
		password2=self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Contraseñas no coinciden")
		return password2
	def save(self, commit=True):
		#identificador = str(identificador)
		#Guardar contraseña en formato Hash
		usuario = super(AdminFormCreacionUsuario, self).save(commit=False)
		'''
		usuario = self.model(
			identificador=identificador,
			correo=self.normalize_email(correo),
		)
		'''
		usuario.set_password(self.cleaned_data["password1"])
		if commit:
			usuario.save()
		return usuario

# formulario para actualizar usuarios. Incluye todos los campos requeridos, pero reemplaza el campo de contraseña
# con el hash guardado en el admin de Django.
class AdminFormActualizar(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = Usuario
		fields = ('identificador','correo', 'direccion', 'telefono', 'celular', 'tipo_usuario')

	def clean_password(self):
	# regresa el valor inicial, sin importar lo que el usuario escriba
	# se realiza ya que el campo no tiene acceso al valor inicial,
	# las contraseñas en Django requieren un formato especifico
		return self.initial['password']		


class FormUsuario(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = '__all__'
		exclude = ['last_login','is_superuser','date_joined','active','staff','admin','tramitador','ventanilla','evaluador','control_contable','control_obra','control_juridico','coordinacion','coordinacion_general','groups','user_permissions']

class FormContribuyente_sid(forms.ModelForm):
	class Meta:
		model = Usuario_Contribuyente
		exclude = ['identificador']

class FormPersonaFisica_sid(forms.ModelForm):
	class Meta:
		model = Usuario_Personas_Fisicas
		exclude = ['identificador']


class MultiContribuyenteModelForm(MultiModelForm):
    form_classes = {
        'UsuarioMain': FormUsuario,
        'Contribuyente': FormContribuyente_sid,
    }