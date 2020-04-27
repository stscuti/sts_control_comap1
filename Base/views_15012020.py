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
	success_url = reverse_lazy('Base:Listado_Paises')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class Paises_UpdateView(LoginRequiredMixin, UpdateView):
	model = Pais
	template_name = 'actualizar_pais_individual.html'
	context_object_name = 'paises'
	form_class = Pais_Form
	success_url = reverse_lazy('Base:Listado_Paises')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class Paises_DeleteView(LoginRequiredMixin, DeleteView):
	model = Pais
	template_name = 'eliminar_pais_individual.html'
	context_object_name = 'paises'
	form_class = Pais_Form
	success_url = reverse_lazy('Base:Listado_Paises')
	login_url = "Usuarios:Login"

class Paises_DetailView(DetailView):
	model = Pais
	template_name = 'detalle_pais_individual.html'
	context_object_name = 'paises'


class CrearPais(CreateView):
	model = Pais
	template_name = 'crear_pais.html'
	form_class = Pais_Form
	success_url = reverse_lazy('Base:Listado_Paises')

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
		'''
		for formulario in departamento_formset.forms:
			formulario.initial['uc'] = user.pk
		#departamento_formset.fields['uc'].initial = '9999'
		'''
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
	success_url = reverse_lazy('Base:Listado_Paises')

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
		self.object = form.save()
		#Utilizamos el atributo instance del formset para asignarle el valor del objeto Compra creado y que nos indica el modelo Foráneo
		departamento_form_set.instance = self.object
		#Finalmente guardamos el formset para que tome los valores que tiene
		departamento_form_set.save()
		#Redireccionamos a la ventana del listado de compras
		return HttpResponseRedirect(self.success_url)

	def form_invalid(self, form, departamento_form_set):
		#Si es inválido el form de Compra o el formset renderizamos los errores
		return self.render_to_response(self.get_context_data(form=form, departamento_form_set = departamento_form_set))

