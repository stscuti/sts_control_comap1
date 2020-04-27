from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import *
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.mixins import LoginRequiredMixin


#Para API
from rest_framework import generics
from .models import *
from .serializers import *

from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DeleteView, DetailView, View
from django.urls import reverse, reverse_lazy


# Create your views here.
class FormWizardView(LoginRequiredMixin, SessionWizardView):
	template_name = "solicitudes.html"
	form_list = [SolicitudesStep1_Form, SolicitudesStep1b_Form, SolicitudesStep2_Form, SolicitudesStep2b_Form, SolicitudesStep2c_Form, SolicitudesStep2d_Form, SolicitudesStep2e_Form, SolicitudesStep2f_Form, SolicitudesStep3_Form, SolicitudesStep4a_Form, SolicitudesStep4b_Form, SolicitudesStep4c_Form, SolicitudesStep4d_Form, SolicitudesStep4e_Form, SolicitudesStep4f_Form, SolicitudesStep4g_Form, SolicitudesStep5_Form, SolicitudesStep6a_Form, SolicitudesStep6b_Form, SolicitudesStep7_Form]
	login_url = "Usuarios:Login"
	#def done(self, form_list, **kwargs):
	def done(self, form_list, form_dict, **kwargs):
		#SolicitudesStep1 = SolicitudesStep1_Form.save(commit=False)
		#SolicitudesStep1.save()
		#[form.save(commit=True) for form in form_list]
		for form in form_list:
			form.save(commit=False)
			form.instance.uc = self.request.user
			#form.instance.contribuyente = self.request.user
			form.save()
		#SolicitudesStep1b = SolicitudesStep1b_Form.save(commit=False)
		#SolicitudesStep1b.user = self.request.user
		#SolicitudesStep1b.SolicitudesStep1 = SolicitudesStep1
		#SolicitudesStep1b.save()

		return render(self.request, 'solicitud_ok.html', {
			'form_data': [form.cleaned_data for form in form_list],
		})

class UpdateFormWizardView(LoginRequiredMixin, SessionWizardView):
	template_name = "solicitudes.html"
	form_list = [SolicitudesStep1_Form, SolicitudesStep1b_Form, SolicitudesStep2_Form, SolicitudesStep2b_Form, SolicitudesStep2c_Form, SolicitudesStep2d_Form, SolicitudesStep2e_Form, SolicitudesStep2f_Form, SolicitudesStep3_Form, SolicitudesStep4a_Form, SolicitudesStep4b_Form, SolicitudesStep4c_Form, SolicitudesStep4d_Form, SolicitudesStep4e_Form, SolicitudesStep4f_Form, SolicitudesStep4g_Form, SolicitudesStep5_Form, SolicitudesStep6a_Form, SolicitudesStep6b_Form, SolicitudesStep7_Form]
	login_url = "Usuarios:Login"
	# def get_form_initial(self, step):
	# 	initial = {}
	# 	print(self, step)
	# 	return self.initial_dict.get(step, initial)

	def dispatch(self, request, pk, *args, **kwargs):
		try:
			form_1 = Solicitud143_Step1.objects.get(num_expediente=pk)
		except Exception as e:
			form_1 = {}		
		try:
			form_2 = Solicitud143_Step1b.objects.get(num_expediente=pk)
		except Exception as e:
			form_2 = {}
		try:
			form_3 = Solicitud143_Step2.objects.get(num_expediente=pk)
		except Exception as e:
			form_3 = {}
		try:
			form_4 = Solicitud143_Step2b.objects.get(num_expediente=pk)
		except Exception as e:
			form_4 = []
		try:
			form_5 = Solicitud143_Step2c.objects.get(num_expediente=pk)
		except Exception as e:
			form_5 = {}
		try:
			form_6 = Solicitud143_Step2d.objects.get(num_expediente=pk)
		except Exception as e:
			form_6 = {}
		try:
			form_7 = Solicitud143_Step2e.objects.get(num_expediente=pk)
		except Exception as e:
			form_7 = {}
		try:
			form_8 = Solicitud143_Step2f.objects.get(num_expediente=pk)
		except Exception as e:
			form_8 = {}

		self.instance_dict = {
			'0': form_1,
			'1': form_2,
			'2': form_3,
			'3': form_4,
			'4': form_5,
			'5': form_6,
			'6': form_7,
			'7': form_8,
		}
		return super(UpdateFormWizardView, self).dispatch(request, *args, **kwargs)
	
	# def get_form_initial(self, step):
	# 	if 'num_expediente' in self.kwargs:
	# 		return {}
	# 	return self.initial_dict.get(step, {})

	# def get_form_instance(self, step):
	# 	if not self.instance:
	# 		if 'num_expediente' in self.kwargs:
	# 			num_expediente = self.kwargs['num_expediente']
	# 			self.instance = form_list.objects.get(id=num_expediente)
	# 		else:
	# 			self.instance = form_list()
	# 	return self.instance 
    
	#def done(self, form_list, **kwargs):
	def done(self, form_list, form_dict, **kwargs):
		#SolicitudesStep1 = SolicitudesStep1_Form.save(commit=False)
		#SolicitudesStep1.save()
		#[form.save(commit=True) for form in form_list]
		for form in form_list:
			form.save(commit=False)
			form.instance.uc = self.request.user
			form.save()
		#SolicitudesStep1b = SolicitudesStep1b_Form.save(commit=False)
		#SolicitudesStep1b.user = self.request.user
		#SolicitudesStep1b.SolicitudesStep1 = SolicitudesStep1
		#SolicitudesStep1b.save()

		return render(self.request, 'solicitud_ok.html', {
			'form_data': [form.cleaned_data for form in form_list],
		})

class SolicitudesList(generics.ListCreateAPIView):
	queryset = Solicitud143_Step1.objects.all()
	serializer_class = SolicitudesSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk = self.kwargs['pk'],
		)
		return obj

class SolicitudesLocalizacionesList(generics.ListCreateAPIView):
	queryset = Solicitud143_Step1b.objects.all()
	serializer_class = SolicitudesLocalizacionesSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk = self.kwargs['pk'],
		)
		return obj

class ListadoSolicitudes(LoginRequiredMixin, ListView):
	model = Solicitud143_Step1
	template_name = 'solicitudes.html'
	context_object_name = 'listadosolicitudes'
	login_url = "Usuarios:Login"

class Solicitudes_CreateView(LoginRequiredMixin, CreateView):
	model = Solicitud143_Step1
	template_name = 'solicitudes.html'
	context_object_name = 'listadosolicitudes'
	form_class = SolicitudesStep1_Form
	success_url = reverse_lazy('Solicitudes:Solicitudes')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class Solicitudes_UpdateView(LoginRequiredMixin, UpdateView):
	model = Solicitud143_Step1
	template_name = 'solicitudes.html'
	context_object_name = 'listadosolicitudes'
	form_class = SolicitudesStep1_Form
	success_url = reverse_lazy('Solicitudes:Solicitudes')
	login_url = "Usuarios:Login"

	def form_valid(self, form):
		form.instance.um = int(str(self.request.user))
		return super().form_valid(form)

class Solicitudes_DeleteView(LoginRequiredMixin, DeleteView):
	model = Solicitud143_Step1
	template_name = 'solicitudes.html'
	context_object_name = 'listadosolicitudes'
	form_class = SolicitudesStep1_Form
	success_url = reverse_lazy('Solicitudes:Solicitudes')
	login_url = "Usuarios:Login"

class Solicitudes_DetailView(DetailView):
	model = Solicitud143_Step1
	template_name = 'solicitudes.html'
	context_object_name = 'listadosolicitudes'