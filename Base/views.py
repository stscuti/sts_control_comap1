from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DeleteView, DetailView, View
from .forms import *
from .models import *
from django.db import transaction
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
''' Vistas de Ejemplo
class FormPaisViewCreate(CreateView):
	model = Pais
	template_name = "paises.html"
	form_class = Pais_Form
	success_url = None

	def get_context_data(self, **kwargs):
		data = super(FormPaisViewCreate, self).get_context_data(**kwargs)
		if self.request.POST:
			data['descripcion'] = DepartamentoFormSet(self.request.POST)
		else:
			data['descripcion'] = DepartamentoFormSet()
		return data

	def form_valid(self, form):
		context = self.get_context_data()
		descripcion = context['descripcion']
		with transaction.atomic():
			form.instance.created_by = self.request.user
			self.object = form.save()
			if descripcion.is_valid():
				descripcion.instance = self.object
				descripcion.save()
		return super(FormPaisViewCreate, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('Base:Paises', kwargs={'pk': self.object.pk})

class FormPaisViewUpdate(UpdateView):
	model = Pais
	template_name = "paises.html"
	form_class = Pais_Form
	success_url = None

	def get_context_data(self, **kwargs):
		data = super(FormPaisViewUpdate, self).get_context_data(**kwargs)
		if self.request.POST:
			data['descripcion'] = DepartamentoFormSet(self.request.POST, instance=self.object)
		else:
			data['descripcion'] = DepartamentoFormSet(instance=self.object)
		return data

	def form_valid(self, form):
		context = self.get_context_data()
		descripcion = context['descripcion']
		with transaction.atomic():
			form.instance.created_by = self.request.user
			self.object = form.save()
			if descripcion.is_valid():
				descripcion.instance = self.object
				descripcion.save()
		return super(FormPaisViewUpdate, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('Base:Paises', kwargs={'pk': self.object.pk})
Fin Vistas de Ejemplo '''

class Paises_Departamentos_Localidades_TemplateView(LoginRequiredMixin, View):
	template_name = 'template_paises_departamentos_localidades.html'
	login_url = "Usuarios:Login"
	def get(self, request, *args, **kwargs):
		
		qs_paises = Pais.objects.all()
		qs_departamento = Departamento.objects.all()
		qs_localidad = Localidad.objects.all()
		context = {'paises':qs_paises, 'departamentos':qs_departamento, 'localidades':qs_localidad}

		return render(request, 'template_paises_departamentos_localidades.html', context=context)

class ListadoPaises(LoginRequiredMixin, ListView):
	model = Pais
	template_name = 'paises.html'
	context_object_name = 'paises'
	login_url = "Usuarios:Login"

class Paises_CreateView(LoginRequiredMixin, CreateView):
	model = Pais
	template_name = 'crear_pais_individual.html'
	context_object_name = 'paises'
	form_class = Pais_Form
	success_url = reverse_lazy('Base:Template_Paises_Departamentos_Localidades')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class Paises_UpdateView(LoginRequiredMixin, UpdateView):
	model = Pais
	template_name = 'actualizar_pais_individual.html'
	context_object_name = 'paises'
	form_class = Pais_Form
	success_url = reverse_lazy('Base:Template_Paises_Departamentos_Localidades')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class Paises_DeleteView(LoginRequiredMixin, DeleteView):
	model = Pais
	template_name = 'eliminar_pais_individual.html'
	context_object_name = 'paises'
	form_class = Pais_Form
	success_url = reverse_lazy('Base:Template_Paises_Departamentos_Localidades')
	login_url = "Usuarios:Login"

class Paises_DetailView(DetailView):
	model = Pais
	template_name = 'detalle_pais_individual.html'
	context_object_name = 'paises'

class ListadoDepartamentos(LoginRequiredMixin, ListView):
	model = Departamento
	template_name = 'departamentos.html'
	context_object_name = 'departamentos'
	login_url = "Usuarios:Login"

class Departamentos_CreateView(LoginRequiredMixin, CreateView):
	model = Departamento
	template_name = 'crear_departamento_individual.html'
	context_object_name = 'departamentos'
	form_class = Departamento_Form
	success_url = reverse_lazy('Base:Template_Paises_Departamentos_Localidades')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class Departamentos_UpdateView(LoginRequiredMixin, UpdateView):
	model = Departamento
	template_name = 'actualizar_departamento_individual.html'
	context_object_name = 'departamentos'
	form_class = Departamento_Form
	success_url = reverse_lazy('Base:Template_Paises_Departamentos_Localidades')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class Departamentos_DeleteView(LoginRequiredMixin, DeleteView):
	model = Departamento
	template_name = 'eliminar_departamento_individual.html'
	context_object_name = 'departamentos'
	form_class = Departamento_Form
	success_url = reverse_lazy('Base:Template_Paises_Departamentos_Localidades')
	login_url = "Usuarios:Login"

class Departamentos_DetailView(DetailView):
	model = Departamento
	template_name = 'detalle_departamento_individual.html'
	context_object_name = 'departamentos'

class ListadoLocalidades(LoginRequiredMixin, ListView):
	model = Localidad
	template_name = 'localidades.html'
	context_object_name = 'localidades'
	login_url = "Usuarios:Login"

class Localidades_CreateView(LoginRequiredMixin, CreateView):
	model = Localidad
	template_name = 'crear_localidad_individual.html'
	context_object_name = 'localidades'
	form_class = Localidad_Form
	success_url = reverse_lazy('Base:Template_Paises_Departamentos_Localidades')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class Localidades_UpdateView(LoginRequiredMixin, UpdateView):
	model = Localidad
	template_name = 'actualizar_localidad_individual.html'
	context_object_name = 'localidades'
	form_class = Localidad_Form
	success_url = reverse_lazy('Base:Template_Paises_Departamentos_Localidades')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class Localidades_DeleteView(LoginRequiredMixin, DeleteView):
	model = Localidad
	template_name = 'eliminar_localidad_individual.html'
	context_object_name = 'localidades'
	form_class = Localidad_Form
	success_url = reverse_lazy('Base:Template_Paises_Departamentos_Localidades')
	login_url = "Usuarios:Login"

class Localidades_DetailView(DetailView):
	model = Localidad
	template_name = 'detalle_localidad_individual.html'
	context_object_name = 'localidades'


class CrearPais(CreateView):
	model = Pais
	template_name = 'crear_pais.html'
	form_class = Pais_Form
	success_url = reverse_lazy('Base:Template_Paises_Departamentos_Localidades')

	def get(self, request, *args, **kwargs):
		"""Primero ponemos nuestro object como nulo, se debe tener en
		cuenta que object se usa en la clase CreateView para crear el objeto"""
		self.object = None
		#Instanciamos el formulario de la Compra que declaramos en la variable form_class
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		#form.fields['uc'].initial = request.user

		#Instanciamos el formset
		#departamento_formset=DepartamentoFormSet(form_kwargs={'descripcion': request.user})
		departamento_formset=DepartamentoFormSet()
		
		user = request.user
		
		for formulario in departamento_formset.forms:
			formulario.initial['uc'] = user.pk
		#departamento_formset.fields['uc'].initial = '9999'
		
		#Renderizamos el formulario de la compra y el formset
		return self.render_to_response(self.get_context_data(form=form, departamento_form_set=departamento_formset))

	def get_context_data(self, **kwargs):
		data = super(CrearPais, self).get_context_data(**kwargs)
		if self.request.POST:
			data['descripcion'] = DepartamentoFormSet(self.request.POST)
		else:
			data['descripcion'] = DepartamentoFormSet()
		return data

	def post(self, request, *args, **kwargs):
		"""Primero ponemos nuestro object como nulo, se debe tener en
		cuenta que object se usa en la clase CreateView para crear el objeto"""
		self.object = None

		#Obtenemos nuevamente la instancia del formulario de Compras
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		#Obtenemos el formset pero ya con lo que se le pasa en el POST
		departamento_form_set = DepartamentoFormSet(request.POST)
		"""Llamamos a los métodos para validar el formulario de Compra y el formset, si son válidos ambos se llama al método
		form_valid o en caso contrario se llama al método form_invalid"""
		if form.is_valid() and departamento_form_set.is_valid():
			return self.form_valid(form, departamento_form_set)
		else:
			return self.form_invalid(form, departamento_form_set)

	def form_valid(self, form, departamento_form_set, *args, **kwargs):
		#Aquí ya guardamos el object de acuerdo a los valores del formulario de Compra
		form.instance.uc = self.request.user
		self.object = form.save()
		#Utilizamos el atributo instance del formset para asignarle el valor del objeto Compra creado y que nos indica el modelo Foráneo
		
		departamento_form_set.instance = self.object
		departamento_form_set.instance.uc = self.request.user
		#Finalmente guardamos el formset para que tome los valores que tiene
		departamento_form_set.save()
		#Redireccionamos a la ventana del listado de compras
		return HttpResponseRedirect(self.success_url)

	def form_invalid(self, form, departamento_form_set, *args, **kwargs):
		#Si es inválido el form de Compra o el formset renderizamos los errores
		return self.render_to_response(self.get_context_data(form=form, departamento_form_set = departamento_form_set))

class ActualizarPais(UpdateView):
	model = Pais
	template_name = 'actualizar_pais.html'
	form_class = Pais_Form
	success_url = reverse_lazy('Base:Template_Paises_Departamentos_Localidades')

	def get(self, request, *args, **kwargs):
		"""Primero ponemos nuestro object como nulo, se debe tener en
		cuenta que object se usa en la clase CreateView para crear el objeto"""
		self.object = None
		#Instanciamos el formulario de la Compra que declaramos en la variable form_class
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		form.fields['uc'].initial = request.user

		#Instanciamos el formset
		#departamento_formset=DepartamentoFormSet(form_kwargs={'descripcion': request.user})
		departamento_formset=DepartamentoFormSet()
		
		user = request.user
		for formulario in departamento_formset.forms:
			formulario.initial['uc'] = user.pk
		#departamento_formset.fields['uc'].initial = '9999'
		
		#Renderizamos el formulario de la compra y el formset
		return self.render_to_response(self.get_context_data(form=form, departamento_form_set=departamento_formset))

	def get_context_data(self, **kwargs):
		data = super(ActualizarPais, self).get_context_data(**kwargs)
		if self.request.POST:
			data['descripcion'] = DepartamentoFormSet(self.request.POST, instance=self.object)
		else:
			data['descripcion'] = DepartamentoFormSet(instance=self.object)
		return data

	def post(self, request, *args, **kwargs):
		"""Primero ponemos nuestro object como nulo, se debe tener en
		cuenta que object se usa en la clase CreateView para crear el objeto"""
		self.object = None

		#Obtenemos nuevamente la instancia del formulario de Compras
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		#Obtenemos el formset pero ya con lo que se le pasa en el POST
		departamento_form_set = DepartamentoFormSet(request.POST)
		"""Llamamos a los métodos para validar el formulario de Compra y el formset, si son válidos ambos se llama al método
		form_valid o en caso contrario se llama al método form_invalid"""
		if form.is_valid() and departamento_form_set.is_valid():
			return self.form_valid(form, departamento_form_set)
		else:
			return self.form_invalid(form, departamento_form_set)

	def form_valid(self, form, departamento_form_set):
		#Aquí ya guardamos el object de acuerdo a los valores del formulario de Compra
		form.instance.uc = self.request.user
		self.object = form.save()
		#Utilizamos el atributo instance del formset para asignarle el valor del objeto Compra creado y que nos indica el modelo Foráneo
		departamento_form_set.instance = self.object
		departamento_form_set.instance.uc = self.request.user
		#Finalmente guardamos el formset para que tome los valores que tiene
		departamento_form_set.save()
		#Redireccionamos a la ventana del listado de compras
		return HttpResponseRedirect(self.success_url)

	def form_invalid(self, form, departamento_form_set):
		#Si es inválido el form de Compra o el formset renderizamos los errores
		return self.render_to_response(self.get_context_data(form=form, departamento_form_set = departamento_form_set))

class ListadoTipoDocumento(LoginRequiredMixin, ListView):
	model = Tipo_Documento
	template_name = 'listado_tipo_documento.html'
	context_object_name = 'tipodocumento'
	login_url = "Usuarios:Login"

class TipoDocumento_CreateView(LoginRequiredMixin, CreateView):
	model = Tipo_Documento
	template_name = 'crear_tipo_documento.html'
	context_object_name = 'tipodocumento'
	form_class = TipoDocumento_Form
	success_url = reverse_lazy('Base:Listado_Tipo_Documento')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class TipoDocumento_UpdateView(LoginRequiredMixin, UpdateView):
	model = Tipo_Documento
	template_name = 'actualizar_tipo_documento.html'
	context_object_name = 'tipodocumento'
	form_class = TipoDocumento_Form
	success_url = reverse_lazy('Base:Listado_Tipo_Documento')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class TipoDocumento_DeleteView(LoginRequiredMixin, DeleteView):
	model = Tipo_Documento
	template_name = 'eliminar_tipo_documento.html'
	context_object_name = 'tipodocumento'
	form_class = TipoDocumento_Form
	success_url = reverse_lazy('Base:Listado_Tipo_Documento')
	login_url = "Usuarios:Login"

class TipoDocumento_DetailView(DetailView):
	model = Tipo_Documento
	template_name = 'detalle_tipo_documento.html'
	context_object_name = 'tipodocumento'


''' Categoria y SubCategoria de Inversiones '''

class Categoria_SubCategoria_Inversiones_TemplateView(LoginRequiredMixin, View):
	template_name = 'template_categorias_subcategorias.html'
	login_url = "Usuarios:Login"
	def get(self, request, *args, **kwargs):
		
		qs_categorias = Categoria_Inversiones.objects.all()
		qs_subcategorias = SubCategoria_Inversiones.objects.all()
		context = {'categorias':qs_categorias, 'subcategorias':qs_subcategorias}

		return render(request, 'template_categorias_subcategorias.html', context=context)


class ListadoCategoriaInversiones(LoginRequiredMixin, ListView):
	model = Categoria_Inversiones
	template_name = 'listado_categoria_inversiones.html'
	context_object_name = 'categoria_inversiones'
	login_url = "Usuarios:Login"

class Categoria_Inversiones_CreateView(LoginRequiredMixin, CreateView):
	model = Categoria_Inversiones
	template_name = 'crear_categoria_inversiones.html'
	context_object_name = 'categoria_inversiones'
	form_class = Categoria_Inversiones_Form
	success_url = reverse_lazy('Base:Listado_Categoria_SubCategoria_Inversiones')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class Categoria_Inversiones_UpdateView(LoginRequiredMixin, UpdateView):
	model = Categoria_Inversiones
	template_name = 'actualizar_categoria_inversiones.html'
	context_object_name = 'categoria_inversiones'
	form_class = Categoria_Inversiones_Form
	success_url = reverse_lazy('Base:Listado_Categoria_SubCategoria_Inversiones')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class Categoria_Inversiones_DeleteView(LoginRequiredMixin, DeleteView):
	model = Categoria_Inversiones
	template_name = 'eliminar_categoria_inversiones.html'
	context_object_name = 'categoria_inversiones'
	form_class = Categoria_Inversiones_Form
	success_url = reverse_lazy('Base:Listado_Categoria_SubCategoria_Inversiones')
	login_url = "Usuarios:Login"

class Categoria_Inversiones_DetailView(DetailView):
	model = Categoria_Inversiones
	template_name = 'detalle_categoria_inversiones.html'
	context_object_name = 'categoria_inversiones'

''' SubCategoria '''

class ListadoSubCategoriaInversiones(LoginRequiredMixin, ListView):
	model = SubCategoria_Inversiones
	template_name = 'listado_subcategoria_inversiones.html'
	context_object_name = 'subcategoria_inversiones'
	login_url = "Usuarios:Login"

class SubCategoria_Inversiones_CreateView(LoginRequiredMixin, CreateView):
	model = SubCategoria_Inversiones
	template_name = 'crear_subcategoria_inversiones.html'
	context_object_name = 'subcategoria_inversiones'
	form_class = SubCategoria_Inversiones_Form
	success_url = reverse_lazy('Base:Listado_Categoria_SubCategoria_Inversiones')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class SubCategoria_Inversiones_UpdateView(LoginRequiredMixin, UpdateView):
	model = SubCategoria_Inversiones
	template_name = 'actualizar_subcategoria_inversiones.html'
	context_object_name = 'subcategoria_inversiones'
	form_class = SubCategoria_Inversiones_Form
	success_url = reverse_lazy('Base:Listado_Categoria_SubCategoria_Inversiones')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class SubCategoria_Inversiones_DeleteView(LoginRequiredMixin, DeleteView):
	model = SubCategoria_Inversiones
	template_name = 'eliminar_subcategoria_inversiones.html'
	context_object_name = 'subcategoria_inversiones'
	form_class = SubCategoria_Inversiones_Form
	success_url = reverse_lazy('Base:Listado_Categoria_SubCategoria_Inversiones')
	login_url = "Usuarios:Login"

class SubCategoria_Inversiones_DetailView(DetailView):
	model = SubCategoria_Inversiones
	template_name = 'detalle_subcategoria_inversiones.html'
	context_object_name = 'subcategoria_inversiones'


''' Tipo de Contribuyente '''

class ListadoTipoContribuyente(LoginRequiredMixin, ListView):
	model = TipoContribuyente
	template_name = 'listado_tipo_contribuyente.html'
	context_object_name = 'tipo_contribuyente'
	login_url = "Usuarios:Login"

class Tipo_Contribuyente_CreateView(LoginRequiredMixin, CreateView):
	model = TipoContribuyente
	template_name = 'crear_tipo_contribuyente.html'
	context_object_name = 'tipo_contribuyente'
	form_class = TipoContribuyente_Form
	success_url = reverse_lazy('Base:Listado_Tipo_Contribuyente')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class Tipo_Contribuyente_UpdateView(LoginRequiredMixin, UpdateView):
	model = TipoContribuyente
	template_name = 'actualizar_tipo_contribuyente.html'
	context_object_name = 'tipo_contribuyente'
	form_class = TipoContribuyente_Form
	success_url = reverse_lazy('Base:Listado_Tipo_Contribuyente')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class Tipo_Contribuyente_DeleteView(LoginRequiredMixin, DeleteView):
	model = TipoContribuyente
	template_name = 'eliminar_tipo_contribuyente.html'
	context_object_name = 'tipo_contribuyente'
	form_class = TipoContribuyente_Form
	success_url = reverse_lazy('Base:Listado_Tipo_Contribuyente')
	login_url = "Usuarios:Login"

class Tipo_Contribuyente_DetailView(DetailView):
	model = TipoContribuyente
	template_name = 'detalle_tipo_contribuyente.html'
	context_object_name = 'tipo_contribuyente'

''' Ministerios '''

class ListadoMinisterios(LoginRequiredMixin, ListView):
	model = Ministerios
	template_name = 'listado_ministerios.html'
	context_object_name = 'ministerios'
	login_url = "Usuarios:Login"

class Ministerios_CreateView(LoginRequiredMixin, CreateView):
	model = Ministerios
	template_name = 'crear_ministerio.html'
	context_object_name = 'ministerios'
	form_class = Ministerios_Form
	success_url = reverse_lazy('Base:Listado_Ministerios')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class Ministerios_UpdateView(LoginRequiredMixin, UpdateView):
	model = Ministerios
	template_name = 'actualizar_ministerio.html'
	context_object_name = 'ministerios'
	form_class = Ministerios_Form
	success_url = reverse_lazy('Base:Listado_Ministerios')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class Ministerios_DeleteView(LoginRequiredMixin, DeleteView):
	model = Ministerios
	template_name = 'eliminar_ministerio.html'
	context_object_name = 'ministerios'
	form_class = Ministerios_Form
	success_url = reverse_lazy('Base:Listado_Ministerios')
	login_url = "Usuarios:Login"

class Ministerios_DetailView(DetailView):
	model = Ministerios
	template_name = 'detalle_ministerio.html'
	context_object_name = 'ministerios'


''' Tipo de Giro '''

class TipoGiro_GiroCIIU_TemplateView(LoginRequiredMixin, View):
	template_name = 'template_tipogiro_girociiu.html'
	login_url = "Usuarios:Login"
	def get(self, request, *args, **kwargs):
		
		qs_tipogiro = TipoGiro.objects.all()
		qs_girociiu = GiroCIIU.objects.all()
		context = {'tipo_giro':qs_tipogiro, 'giro_ciiu':qs_girociiu}

		return render(request, 'template_tipogiro_girociiu.html', context=context)


class ListadoTipoGiro(LoginRequiredMixin, ListView):
	model = TipoGiro
	template_name = 'listado_tipo_giro.html'
	context_object_name = 'tipo_giro'
	login_url = "Usuarios:Login"

class TipoGiro_CreateView(LoginRequiredMixin, CreateView):
	model = TipoGiro
	template_name = 'crear_tipo_giro.html'
	context_object_name = 'tipo_giro'
	form_class = TipoGiro_Form
	success_url = reverse_lazy('Base:Listado_TipoGiro_GiroCIIU')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class TipoGiro_UpdateView(LoginRequiredMixin, UpdateView):
	model = TipoGiro
	template_name = 'actualizar_tipo_giro.html'
	context_object_name = 'tipo_giro'
	form_class = TipoGiro_Form
	success_url = reverse_lazy('Base:Listado_TipoGiro_GiroCIIU')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class TipoGiro_DeleteView(LoginRequiredMixin, DeleteView):
	model = TipoGiro
	template_name = 'eliminar_tipo_giro.html'
	context_object_name = 'tipo_giro'
	form_class = TipoGiro_Form
	success_url = reverse_lazy('Base:Listado_TipoGiro_GiroCIIU')
	login_url = "Usuarios:Login"

class TipoGiro_DetailView(DetailView):
	model = TipoGiro
	template_name = 'detalle_tipo_giro.html'
	context_object_name = 'tipo_giro'

''' Giro CIIU '''

class ListadoGiroCIIU(LoginRequiredMixin, ListView):
	model = GiroCIIU
	template_name = 'listado_giro_ciiu.html'
	context_object_name = 'giro_ciiu'
	login_url = "Usuarios:Login"

class Giro_CIIU_CreateView(LoginRequiredMixin, CreateView):
	model = GiroCIIU
	template_name = 'crear_giro_ciiu.html'
	context_object_name = 'giro_ciiu'
	form_class = GiroCIIU_Form
	success_url = reverse_lazy('Base:Listado_TipoGiro_GiroCIIU')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class Giro_CIIU_UpdateView(LoginRequiredMixin, UpdateView):
	model = GiroCIIU
	template_name = 'actualizar_giro_ciiu.html'
	context_object_name = 'giro_ciiu'
	form_class = GiroCIIU_Form
	success_url = reverse_lazy('Base:Listado_TipoGiro_GiroCIIU')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class Giro_CIIU_DeleteView(LoginRequiredMixin, DeleteView):
	model = GiroCIIU
	template_name = 'eliminar_giro_ciiu.html'
	context_object_name = 'giro_ciiu'
	form_class = GiroCIIU_Form
	success_url = reverse_lazy('Base:Listado_TipoGiro_GiroCIIU')
	login_url = "Usuarios:Login"

class Giro_CIIU_DetailView(DetailView):
	model = GiroCIIU
	template_name = 'detalle_giro_ciiu.html'
	context_object_name = 'giro_ciiu'

''' Fecha de Balance '''

class ListadoFechaBalance(LoginRequiredMixin, ListView):
	model = FechaBalance
	template_name = 'listado_fecha_balance.html'
	context_object_name = 'fecha_balance'
	login_url = "Usuarios:Login"

class Fecha_Balance_CreateView(LoginRequiredMixin, CreateView):
	model = FechaBalance
	template_name = 'crear_fecha_balance.html'
	context_object_name = 'fecha_balance'
	form_class = FechaBalance_Form
	success_url = reverse_lazy('Base:Listado_Fecha_Balance')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class Fecha_Balance_UpdateView(LoginRequiredMixin, UpdateView):
	model = FechaBalance
	template_name = 'actualizar_fecha_balance.html'
	context_object_name = 'fecha_balance'
	form_class = FechaBalance_Form
	success_url = reverse_lazy('Base:Listado_Fecha_Balance')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class Fecha_Balance_DeleteView(LoginRequiredMixin, DeleteView):
	model = FechaBalance
	template_name = 'eliminar_fecha_balance.html'
	context_object_name = 'fecha_balance'
	form_class = FechaBalance_Form
	success_url = reverse_lazy('Base:Listado_Fecha_Balance')
	login_url = "Usuarios:Login"

class Fecha_Balance_DetailView(DetailView):
	model = FechaBalance
	template_name = 'detalle_fecha_balance.html'
	context_object_name = 'fecha_balance'


class ListadoLocalizacionOperaciones(LoginRequiredMixin, ListView):
	model = Localizacion_Operaciones
	template_name = 'listado_localizacion_operaciones.html'
	context_object_name = 'localizacion_operaciones'
	login_url = "Usuarios:Login"

class LocalizacionOperaciones_CreateView(LoginRequiredMixin, CreateView):
	model = Localizacion_Operaciones
	template_name = 'crear_localizacion_operaciones.html'
	context_object_name = 'localizacion_operaciones'
	form_class = Localizacion_Operaciones_Form
	success_url = reverse_lazy('Base:Listado_Localizacion_Operaciones')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class LocalizacionOperaciones_UpdateView(LoginRequiredMixin, UpdateView):
	model = Localizacion_Operaciones
	template_name = 'actualizar_localizacion_operaciones.html'
	context_object_name = 'localizacion_operaciones'
	form_class = Localizacion_Operaciones_Form
	success_url = reverse_lazy('Base:Listado_Localizacion_Operaciones')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class LocalizacionOperaciones_DeleteView(LoginRequiredMixin, DeleteView):
	model = Localizacion_Operaciones
	template_name = 'eliminar_localizacion_operaciones.html'
	context_object_name = 'localizacion_operaciones'
	form_class = Localizacion_Operaciones_Form
	success_url = reverse_lazy('Base:Listado_Localizacion_Operaciones')
	login_url = "Usuarios:Login"

class LocalizacionOperaciones_DetailView(DetailView):
	model = Localizacion_Operaciones
	template_name = 'detalle_localizacion_operaciones.html'
	context_object_name = 'localizacion_operaciones'

class Listado_Puntaje_Departamentos(LoginRequiredMixin, ListView):
	model = Listado_Puntaje_Departamentos
	template_name = 'listado_puntaje_departamentos.html'
	context_object_name = 'listado_puntaje_departamentos'
	login_url = "Usuarios:Login"

class Listado_Puntaje_Departamentos_CreateView(LoginRequiredMixin, CreateView):
	model = Listado_Puntaje_Departamentos
	template_name = 'crear_listado_puntaje_departamentos.html'
	context_object_name = 'listado_puntaje_departamentos'
	form_class = Listado_Puntaje_Departamentos_Form
	success_url = reverse_lazy('Base:Listado_Puntaje_Departamentos')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class Listado_Puntaje_Departamentos_UpdateView(LoginRequiredMixin, UpdateView):
	model = Listado_Puntaje_Departamentos
	template_name = 'actualizar_listado_puntaje_departamentos.html'
	context_object_name = 'listado_puntaje_departamentos'
	form_class = Listado_Puntaje_Departamentos_Form
	success_url = reverse_lazy('Base:Listado_Puntaje_Departamentos')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class Listado_Puntaje_Departamentos_DeleteView(LoginRequiredMixin, DeleteView):
	model = Listado_Puntaje_Departamentos
	template_name = 'eliminar_listado_puntaje_departamentos.html'
	context_object_name = 'listado_puntaje_departamentos'
	form_class = Listado_Puntaje_Departamentos_Form
	success_url = reverse_lazy('Base:Listado_Puntaje_Departamentos')
	login_url = "Usuarios:Login"

class Listado_Puntaje_Departamentos_DetailView(DetailView):
	model = Listado_Puntaje_Departamentos
	template_name = 'detalle_listado_puntaje_departamentos.html'
	context_object_name = 'listado_puntaje_departamentos'



class ListadoTipo_DocumentoPresentar(LoginRequiredMixin, ListView):
	model = Tipo_DocumentoPresentar
	template_name = 'listado_documento_presentar.html'
	context_object_name = 'documentoapresentar'
	login_url = "Usuarios:Login"

class Tipo_DocumentoPresentar_CreateView(LoginRequiredMixin, CreateView):
	model = Tipo_DocumentoPresentar
	template_name = 'crear_documento_presentar.html'
	context_object_name = 'documentoapresentar'
	form_class = Tipo_DocumentoPresentar_Form
	success_url = reverse_lazy('Base:Listado_Documentacion_Presentar')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class Tipo_DocumentoPresentar_UpdateView(LoginRequiredMixin, UpdateView):
	model = Tipo_DocumentoPresentar
	template_name = 'actualizar_documento_presentar.html'
	context_object_name = 'documentoapresentar'
	form_class = Tipo_DocumentoPresentar_Form
	success_url = reverse_lazy('Base:Listado_Documentacion_Presentar')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class Tipo_DocumentoPresentar_DeleteView(LoginRequiredMixin, DeleteView):
	model = Tipo_DocumentoPresentar
	template_name = 'eliminar_documento_presentar.html'
	context_object_name = 'documentoapresentar'
	form_class = Tipo_DocumentoPresentar_Form
	success_url = reverse_lazy('Base:Listado_Documentacion_Presentar')
	login_url = "Usuarios:Login"

class Tipo_DocumentoPresentar_DetailView(DetailView):
	model = Tipo_DocumentoPresentar
	template_name = 'detalle_documento_presentar.html'
	context_object_name = 'documentoapresentar'


class ListadoExp_Bienes_Servicios(LoginRequiredMixin, ListView):
	model = Exp_Bienes_Servicios
	template_name = 'listado_exp_bienes_servicios.html'
	context_object_name = 'exp_bienes_servicios'
	login_url = "Usuarios:Login"

class Exp_Bienes_Servicios_CreateView(LoginRequiredMixin, CreateView):
	model = Exp_Bienes_Servicios
	template_name = 'crear_exp_bienes_servicios.html'
	context_object_name = 'exp_bienes_servicios'
	form_class = Exp_Bienes_Servicios_Form
	success_url = reverse_lazy('Base:Listado_Exportaciones_Bienes_Servicios')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class Exp_Bienes_Servicios_UpdateView(LoginRequiredMixin, UpdateView):
	model = Exp_Bienes_Servicios
	template_name = 'actualizar_exp_bienes_servicios.html'
	context_object_name = 'exp_bienes_servicios'
	form_class = Exp_Bienes_Servicios_Form
	success_url = reverse_lazy('Base:Listado_Exportaciones_Bienes_Servicios')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class Exp_Bienes_Servicios_DeleteView(LoginRequiredMixin, DeleteView):
	model = Exp_Bienes_Servicios
	template_name = 'eliminar_exp_bienes_servicios.html'
	context_object_name = 'exp_bienes_servicios'
	form_class = Exp_Bienes_Servicios_Form
	success_url = reverse_lazy('Base:Listado_Exportaciones_Bienes_Servicios')
	login_url = "Usuarios:Login"

class Exp_Bienes_Servicios_DetailView(DetailView):
	model = Exp_Bienes_Servicios
	template_name = 'detalle_exp_bienes_servicios.html'
	context_object_name = 'exp_bienes_servicios'