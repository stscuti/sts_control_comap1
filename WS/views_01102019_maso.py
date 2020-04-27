from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView
from .forms import FormCotizaciones
from .models import Cotizaciones
from Usuarios.models import Usuario

from django.views import View
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import get_user_model

from django.template.loader import render_to_string
from datetime import datetime, timedelta, tzinfo, time, date
from dateutil import relativedelta
import calendar
import pytz
from django.utils import timezone


#Para WS
from zeep import Client as Client_zeep, Settings
from requests import Session
from requests.auth import HTTPBasicAuth
from lxml import etree

from suds.client import Client
from suds.sudsobject import asdict

# Create your views here.

class CotizacionesCreateView(CreateView):
	form_class = FormCotizaciones
	template_name = 'cotizaciones.html'

	def setup(self, request, *args, **kwargs):
		"""Initialize attributes shared by all view methods."""
		wsdl = "https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl"
		settings = Settings(strict=False, xml_huge_tree=True)
		client2 = Client_zeep(wsdl=wsdl, settings=settings)
		#fdesde = datetime(2019,7,15)
		#fhasta = datetime(2019,7,31)
		fdesde = datetime(datetime.now().year,datetime.now().month-8,1)
		fhasta = datetime(datetime.now().year,datetime.now().month,calendar.monthrange(datetime.now().year,datetime.now().month)[1])   	
		grupo=2
		moneda=[0]
		status_zeep_anidado = []
		cotizaciones_zeep_anidado = []
		if fhasta >= fdesde:
			while datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) <= fhasta or datetime(fdesde.year,fdesde.month,1) <= fhasta:
				#meses = relativedelta.relativedelta(fhasta,fdesde)
				finicial = fdesde
				ffinal = datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1])
				if datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) > fhasta:
					ffinal = fhasta
				fdesde = ffinal + timedelta(days=1)
				request_zeep = {'Entrada' :	{
					'Moneda': {'item' : moneda},
					'FechaDesde': finicial.isoformat(),
					'FechaHasta': ffinal.isoformat(),
					'Grupo': '0',}}
				respuesta_ws_cotiza_zeep = client2.service.Execute(**request_zeep)
				#for objeto_cotizaciones in respuesta_ws_cotiza_zeep['datoscotizaciones']['datoscotizaciones.dato']:
					#Cotizaciones = objeto_cotizaciones.save()				
				status_zeep = respuesta_ws_cotiza_zeep['respuestastatus'] #Diccionario con 'status', 'codigoerror', 'mensaje'
				status_zeep_anidado.extend(status_zeep)
				#Lista con Diccionarios, cada diccionario contiene: 'Fecha', 'Moneda', 'Nombre', 'CodigoISO', 'Emisor', 'TCC', 'TCV', 'ArbAct', 'FormaArbitrar'
				cotizaciones_zeep = respuesta_ws_cotiza_zeep['datoscotizaciones']['datoscotizaciones.dato']

									
				cotizaciones_zeep_anidado.extend(cotizaciones_zeep)




		self.request = request
		self.args = args
		self.kwargs = {'cotizaciones_zeep': cotizaciones_zeep_anidado, 'status_zeep': status_zeep_anidado}
	

	'''
	def consultar_cotizaciones_suds(self, request, fdesde=datetime(2019,7,1), fhasta=datetime(2019,7,15), grupo=2, moneda=0):
		wsdl = "https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl"
		client = suds.Client(wsdl)
		cotiza_obj = client.factory.create("wsbcucotizacionesin")
		cotiza_obj.FechaDesde = fdesde
		cotiza_obj.FechaHasta = fhasta
		cotiza_obj.Grupo  = 2
		cotiza_obj.Moneda = {'item' : 0}
		obtener_ws = client.service.Execute(cotiza_obj)
		cotizacion_lista = asdict(obtener_ws.datoscotizaciones)['datoscotizaciones.dato'] #Esto es una lista donde cada elemento es un diccionario
		cotizacion_lista_convertida = []
		for cotizacion in cotizacion_lista:
			if not asdict(cotizacion) in cotizacion_lista_convertida:
				cotizacion_lista_convertida.append(asdict(cotizacion))
		return cotizacion_lista_convertida
		#return render(request, 'cotizaciones.html', {'form': form, 'cotizaciones': cotizacion_lista_convertida})
	'''
	def consultar_cotizaciones_zeep(self, request, fdesde, fhasta, grupo, moneda):
		wsdl = "https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl"
		settings = Settings(strict=False, xml_huge_tree=True)
		client2 = zeep.Client(wsdl=wsdl, settings=settings)
		request_zeep = {'Entrada' :	{
			'Moneda': {'item' : moneda},
			'FechaDesde': fdesde.isoformat(),
			'FechaHasta': fhasta.isoformat(),
			'Grupo': '0',}}
		respuesta_ws_cotiza_zeep = client2.service.Execute(**request_zeep)
		status_zeep = respuesta_ws_cotiza_zeep['respuestastatus'] #Diccionario con 'status', 'codigoerror', 'mensaje'
		#Lista con Diccionarios, cada diccionario contiene: 'Fecha', 'Moneda', 'Nombre', 'CodigoISO', 'Emisor', 'TCC', 'TCV', 'ArbAct', 'FormaArbitrar'
		cotizaciones_zeep = respuesta_ws_cotiza_zeep['datoscotizaciones']['datoscotizaciones.dato']
		return {'status_zeep': status_zeep, 'cotizaciones_zeep': cotizaciones_zeep}



	def get(self, request, *args, **kwargs):

		form = FormCotizaciones()
		return render(request, 'cotizaciones.html', {'form': form, 'cotizaciones': self.kwargs['cotizaciones_zeep']})

	def form_valid(self, form):
		form.save()
		return HttpResponseRedirect(reverse('WS:Cotizaciones'))
	'''
	def post(self, request): #, *args, **kwargs
		if request.method == "POST":
			
			User = get_user_model()
			id_usuario = User.objects.get(pk=request.user.id)
			salvar_formulario = form.save(commit=false)
			salvar_formulario.identificador = id_usuario
			salvar_formulario.save()
			
			form = FormCotizaciones()
		return render(request, 'cotizaciones.html', {'form': form})
	'''
class EscogerCotizacionesAutomaticas(View):	

	form_class = FormCotizaciones
	template_name = 'cotizaciones2.html'
	'''
	def setup(self, request, *args, **kargs):
		
		wsdl = "https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl"
		settings = Settings(strict=False, xml_huge_tree=True)
		client_1 = Client_zeep(wsdl=wsdl, settings=settings)
		
		if request.method == 'GET' and request.GET.getlist('fdesde[]') is not None and request.GET.getlist('fhasta[]') is not None:
			fdesde = datetime(datetime.now().year,datetime.now().month-7,1) # datetime.strptime(request.GET.getlist('fdesde')[0], '%Y-%m-%d') # 
			fhasta = datetime(datetime.now().year,datetime.now().month,calendar.monthrange(datetime.now().year,datetime.now().month)[1]) # datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d') # 
		else:
			fdesde = datetime(datetime.now().year,datetime.now().month-6,1)
			fhasta = datetime(datetime.now().year,datetime.now().month,calendar.monthrange(datetime.now().year,datetime.now().month)[1])
		grupo=2
		moneda=[0]
		status_zeep_anidado = []
		cotizaciones_zeep_anidado = []

		if fhasta >= fdesde:
			
			while datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) <= fhasta or datetime(fdesde.year,fdesde.month,1) <= fhasta:
				#meses = relativedelta.relativedelta(fhasta,fdesde)
				finicial = fdesde
				ffinal = datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1])
				if datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) > fhasta:
					ffinal = fhasta
				fdesde = ffinal + timedelta(days=1)
				request_zeep = {'Entrada' :	{
					'Moneda': {'item' : moneda},
					'FechaDesde': finicial.isoformat(),
					'FechaHasta': ffinal.isoformat(),
					'Grupo': '0',}}
				respuesta_ws_cotiza_zeep = client_1.service.Execute(**request_zeep)
				status_zeep = respuesta_ws_cotiza_zeep['respuestastatus'] #Diccionario con 'status', 'codigoerror', 'mensaje'
				status_zeep_anidado.extend(status_zeep)
				#Lista con Diccionarios, cada diccionario contiene: 'Fecha', 'Moneda', 'Nombre', 'CodigoISO', 'Emisor', 'TCC', 'TCV', 'ArbAct', 'FormaArbitrar'
				cotizaciones_zeep_a1 = respuesta_ws_cotiza_zeep['datoscotizaciones']['datoscotizaciones.dato']
				cotizaciones_zeep_anidado.extend(cotizaciones_zeep_a1)	
		self.request = request
		self.args = args
		self.kwargs = {'cotizaciones_zeep': cotizaciones_zeep_anidado, 'status_zeep': status_zeep_anidado, 'fdesde': fdesde, 'fhasta': fhasta}
		'''
		

	def get(self, request, *args, **kwargs):

		form = FormCotizaciones()
		if request.method == 'GET' and request.GET.getlist('fdesde[]') is not None and request.GET.getlist('fhasta[]') is not None:
			fdesde = datetime(datetime.now().year,datetime.now().month-4,1) #datetime.strptime(request.GET.getlist('fdesde')[0], '%Y-%m-%d') # datetime(datetime.now().year,datetime.now().month-4,1)
			#fdesde = datetime(2019, 8, 1, 0, 0)
			final_year = datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d').year
			final_month = datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d').month
			final_day = datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d').day
			fhasta = datetime(2019, 8, 25, 0, 0)
			#fhasta = datetime.strptime(request.GET.getlist('ffinalizacion')[0], '%Y-%m-%d')
		else:
			fdesde = datetime(datetime.now().year,datetime.now().month-2,1)
			fhasta = datetime(datetime.now().year,datetime.now().month,calendar.monthrange(datetime.now().year,datetime.now().month)[1])

		wsdl = "https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl"
		settings = Settings(strict=False, xml_huge_tree=True)
		client_1 = Client_zeep(wsdl=wsdl, settings=settings)
		grupo=2
		moneda=[0]
		status_zeep_anidado = []
		cotizaciones_zeep_anidado = []
		'''
		if fhasta >= fdesde:
			
			while datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) <= fhasta or datetime(fdesde.year,fdesde.month,1) <= fhasta:
				#meses = relativedelta.relativedelta(fhasta,fdesde)
				finicial = fdesde
				ffinal = datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1])
				if datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) > fhasta:
					ffinal = fhasta
				fdesde = ffinal + timedelta(days=1)
				request_zeep = {'Entrada' :	{
					'Moneda': {'item' : moneda},
					'FechaDesde': finicial.isoformat(),
					'FechaHasta': ffinal.isoformat(),
					'Grupo': '0',}}
				respuesta_ws_cotiza_zeep = client_1.service.Execute(**request_zeep)
				status_zeep = respuesta_ws_cotiza_zeep['respuestastatus'] #Diccionario con 'status', 'codigoerror', 'mensaje'
				status_zeep_anidado.extend(status_zeep)
				#Lista con Diccionarios, cada diccionario contiene: 'Fecha', 'Moneda', 'Nombre', 'CodigoISO', 'Emisor', 'TCC', 'TCV', 'ArbAct', 'FormaArbitrar'
				cotizaciones_zeep_a1 = respuesta_ws_cotiza_zeep['datoscotizaciones']['datoscotizaciones.dato']
				cotizaciones_zeep_anidado.extend(cotizaciones_zeep_a1)
		'''
		

		self.request = request
		self.args = args
		self.kwargs = {'cotizaciones_zeep': cotizaciones_zeep_anidado, 'status_zeep': status_zeep_anidado, 'fdesde': fdesde, 'fhasta': fhasta}
		
		fdesde = datetime.strptime(request.GET.getlist('fdesde')[0], '%Y-%m-%d')
		fhasta = datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d')

		return render(request, 'cotizaciones2.html', {'form': form, 'cotizaciones': self.kwargs['cotizaciones_zeep'], 'fdesde': fdesde, 'fhasta': fhasta, 'final_year': final_year, 'final_month': final_month, 'final_day': final_day})		
	'''
	def get(self, request, *args, **kwargs):

		form = FormCotizaciones()
		if request.method == 'GET' and request.GET.getlist('fdesde[]') is not None and request.GET.getlist('fhasta[]') is not None:
			fdesde = datetime.strptime(request.GET.getlist('fdesde')[0], '%Y-%m-%d') # datetime(datetime.now().year,datetime.now().month-4,1)
			fhasta = datetime(datetime.now().year,datetime.now().month,calendar.monthrange(datetime.now().year,datetime.now().month)[1]) # datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d') # datetime(datetime.now().year,datetime.now().month,calendar.monthrange(datetime.now().year,datetime.now().month)[1])

		else:
			fdesde = datetime(datetime.now().year,datetime.now().month-2,1)
			fhasta = datetime(datetime.now().year,datetime.now().month,calendar.monthrange(datetime.now().year,datetime.now().month)[1])

		wsdl = "https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl"
		settings = Settings(strict=False, xml_huge_tree=True)
		client_1 = Client_zeep(wsdl=wsdl, settings=settings)
		grupo=2
		moneda=[0]
		status_zeep_anidado = []
		cotizaciones_zeep_anidado = []

		if fhasta >= fdesde:
			
			while datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) <= fhasta or datetime(fdesde.year,fdesde.month,1) <= fhasta:
				#meses = relativedelta.relativedelta(fhasta,fdesde)
				finicial = fdesde
				ffinal = datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1])
				if datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) > fhasta:
					ffinal = fhasta
				fdesde = ffinal + timedelta(days=1)
				request_zeep = {'Entrada' :	{
					'Moneda': {'item' : moneda},
					'FechaDesde': finicial.isoformat(),
					'FechaHasta': ffinal.isoformat(),
					'Grupo': '0',}}
				respuesta_ws_cotiza_zeep = client_1.service.Execute(**request_zeep)
				status_zeep = respuesta_ws_cotiza_zeep['respuestastatus'] #Diccionario con 'status', 'codigoerror', 'mensaje'
				status_zeep_anidado.extend(status_zeep)
				#Lista con Diccionarios, cada diccionario contiene: 'Fecha', 'Moneda', 'Nombre', 'CodigoISO', 'Emisor', 'TCC', 'TCV', 'ArbAct', 'FormaArbitrar'
				cotizaciones_zeep_a1 = respuesta_ws_cotiza_zeep['datoscotizaciones']['datoscotizaciones.dato']
				cotizaciones_zeep_anidado.extend(cotizaciones_zeep_a1)
		

		self.request = request
		self.args = args
		self.kwargs = {'cotizaciones_zeep': cotizaciones_zeep_anidado, 'status_zeep': status_zeep_anidado, 'fdesde': fdesde, 'fhasta': fhasta}

		fdesde = datetime.strptime(request.GET.getlist('fdesde')[0], '%Y-%m-%d')
		fhasta = datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d')

		return render(request, 'cotizaciones2.html', {'form': form, 'cotizaciones': self.kwargs['cotizaciones_zeep'], 'fdesde': fdesde, 'fhasta': fhasta})		
'''


class CotizacionesAutomaticasUpdateView(UpdateView):
	#form_class = FormCotizaciones
	template_name = 'cotizaciones.html'
	'''
	def setup(self, request, *args, **kwargs):
		"""Initialize attributes shared by all view methods.""" 
		
		wsdl = "https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl"
		settings = Settings(strict=False, xml_huge_tree=True)
		client2 = Client_zeep(wsdl=wsdl, settings=settings)
		fdesde = datetime(datetime.now().year,datetime.now().month,1)
		fhasta = datetime(datetime.now().year,datetime.now().month,calendar.monthrange(datetime.now().year,datetime.now().month)[1])
		grupo=2
		moneda=[0]
		status_zeep_anidado = []
		cotizaciones_zeep_anidado = []
		if fhasta >= fdesde:
			while datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) <= fhasta or datetime(fdesde.year,fdesde.month,1) <= fhasta:
				#meses = relativedelta.relativedelta(fhasta,fdesde)
				finicial = fdesde
				ffinal = datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1])
				if datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) > fhasta:
					ffinal = fhasta
				fdesde = ffinal + timedelta(days=1)
				request_zeep = {'Entrada' :	{
					'Moneda': {'item' : moneda},
					'FechaDesde': finicial.isoformat(),
					'FechaHasta': ffinal.isoformat(),
					'Grupo': '0',}}
				respuesta_ws_cotiza_zeep = client2.service.Execute(**request_zeep)
				status_zeep = respuesta_ws_cotiza_zeep['respuestastatus'] #Diccionario con 'status', 'codigoerror', 'mensaje'
				status_zeep_anidado.extend(status_zeep)
				#Lista con Diccionarios, cada diccionario contiene: 'Fecha', 'Moneda', 'Nombre', 'CodigoISO', 'Emisor', 'TCC', 'TCV', 'ArbAct', 'FormaArbitrar'
				cotizaciones_zeep = respuesta_ws_cotiza_zeep['datoscotizaciones']['datoscotizaciones.dato']
				cotizaciones_zeep_anidado.extend(cotizaciones_zeep)
				



		self.request = request
		self.args = args
		self.kwargs = kwargs
		'''

	def get(self, request, *args, **kwargs):
		wsdl = "https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl"
		settings = Settings(strict=False, xml_huge_tree=True)
		client2 = Client_zeep(wsdl=wsdl, settings=settings)
		if request.method == 'GET' and request.GET.getlist('fdesde[]') is not None and request.GET.getlist('fhasta[]') is not None:
			fdesde = datetime.strptime(request.GET.getlist('fdesde')[0], '%Y-%m-%d')
			fhasta = datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d')
		else:
			fdesde = datetime(datetime.now().year,datetime.now().month-2,1)
			fhasta = datetime(datetime.now().year,datetime.now().month,calendar.monthrange(datetime.now().year,datetime.now().month)[1])    		
		grupo=2
		moneda=[0]
		status_zeep_anidado = []
		cotizaciones_zeep_anidado = []
		if fhasta >= fdesde:
			while datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) <= fhasta or datetime(fdesde.year,fdesde.month,1) <= fhasta:
				#meses = relativedelta.relativedelta(fhasta,fdesde)
				finicial = fdesde
				ffinal = datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1])
				if datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) > fhasta:
					ffinal = fhasta
				fdesde = ffinal + timedelta(days=1)
				request_zeep = {'Entrada' :	{
					'Moneda': {'item' : moneda},
					'FechaDesde': finicial.isoformat(),
					'FechaHasta': ffinal.isoformat(),
					'Grupo': '0',}}
				respuesta_ws_cotiza_zeep = client2.service.Execute(**request_zeep)
				status_zeep = respuesta_ws_cotiza_zeep['respuestastatus'] #Diccionario con 'status', 'codigoerror', 'mensaje'
				status_zeep_anidado.extend(status_zeep)
				#Lista con Diccionarios, cada diccionario contiene: 'Fecha', 'Moneda', 'Nombre', 'CodigoISO', 'Emisor', 'TCC', 'TCV', 'ArbAct', 'FormaArbitrar'
				cotizaciones_zeep = respuesta_ws_cotiza_zeep['datoscotizaciones']['datoscotizaciones.dato']
				cotizaciones_zeep_anidado.extend(cotizaciones_zeep)

		return render(request, 'cotizaciones.html', {'cotizaciones': cotizaciones_zeep_anidado, 'fdesde': fdesde, 'fhasta': fhasta})
	
	def post(self, request, *args, **kwargs):
		
		wsdl = "https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl"
		settings = Settings(strict=False, xml_huge_tree=True)
		client3 = Client_zeep(wsdl=wsdl, settings=settings)
		if request.method == 'POST' and request.POST['fdesde'] is not None and request.POST['fhasta'] is not None:
			
			inicio = request.POST['fdesde']
			final = request.POST['fhasta']
			'''
			#fdesde = datetime.combine(datetime.strptime(request.POST['fdesde'], '%Y-%m-%d').date(), datetime.min.time())
			#fhasta = datetime.combine(datetime.strptime(request.POST['fhasta'], '%Y-%m-%d').date(), datetime.min.time())
			fdesde = datetime(datetime.strptime(request.POST['fdesde'], '%Y-%m-%d').date().year,datetime.strptime(request.POST['fdesde'], '%Y-%m-%d').date().month, datetime.strptime(request.POST['fdesde'], '%Y-%m-%d').date().day)
			fhasta = datetime(datetime.strptime(request.POST['fhasta'], '%Y-%m-%d').date().year,datetime.strptime(request.POST['fhasta'], '%Y-%m-%d').date().month, datetime.strptime(request.POST['fhasta'], '%Y-%m-%d').date().day)
			fini = datetime(2019,7,16)
			ffin = datetime(2019,7,16)
			grupo=2
			moneda=[0]
			status_zeep_anidado3 = []
			cotizaciones_zeep_anidado3 = []
			if ffin >= fini:
				while datetime(fini.year,fini.month,calendar.monthrange(fini.year,fini.month)[1]) <= ffin or datetime(fini.year,fini.month,1) <= ffin:
					finicial = fini
					ffinal = datetime(fini.year,fini.month,calendar.monthrange(fini.year,fini.month)[1])
					if datetime(fini.year,fini.month,calendar.monthrange(fini.year,fini.month)[1]) > ffin:
						ffinal = ffin
					fini = ffinal + timedelta(days=1)
					request_zeep3 = {'Entrada' : {
						'Moneda': {'item' : moneda},
						'FechaDesde': '2019-06-30T00:00:00', #finicial,#.isoformat(),
						'FechaHasta': '2019-06-30T00:00:00', #ffinal,#.isoformat(),
						'Grupo': '0',}}
					respuesta_ws_cotiza_zeep3 = client3.service.Execute(**request_zeep3)
					status_zeep3 = respuesta_ws_cotiza_zeep3['respuestastatus'] #Diccionario con 'status', 'codigoerror', 'mensaje'
					status_zeep_anidado3.extend(status_zeep3)
					#Lista con Diccionarios, cada diccionario contiene: 'Fecha', 'Moneda', 'Nombre', 'CodigoISO', 'Emisor', 'TCC', 'TCV', 'ArbAct', 'FormaArbitrar'
					cotizaciones_zeep3 = respuesta_ws_cotiza_zeep3['datoscotizaciones']['datoscotizaciones.dato']
					cotizaciones_zeep_anidado3.extend(cotizaciones_zeep3)
		return render(request, 'cotizaciones2.html', {'cotizaciones': cotizaciones_zeep_anidado3, 'fdesde': inicio, 'fhasta': final})
		'''
		return render(request, 'cotizaciones2.html', {'fdesde': inicio, 'fhasta': final})