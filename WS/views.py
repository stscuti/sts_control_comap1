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
import dateutil.relativedelta


#Para WS
from zeep import Client as Client_zeep, Settings
from requests import Session
from requests.auth import HTTPBasicAuth
from lxml import etree

from suds.client import Client
from suds.sudsobject import asdict

import pandas as pd
from django_pandas.managers import DataFrameManager
import numpy as np

# Create your views here.

class CotizacionesCreateView(LoginRequiredMixin, CreateView):
	form_class = FormCotizaciones
	template_name = 'cotizaciones.html'
	login_url = 'Usuarios:Login'
	model = Cotizaciones

	def get(self, request, *args, **kwargs):
		form = FormCotizaciones()
		"""Initialize attributes shared by all view methods."""
		wsdl = "https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl"
		settings = Settings(strict=False, xml_huge_tree=True)
		client2 = Client_zeep(wsdl=wsdl, settings=settings)
		#fdesde = datetime(2019,7,15)
		#fhasta = datetime(2019,7,31)
		fdesde = datetime((datetime.now()-dateutil.relativedelta.relativedelta(months=1)).year,(datetime.now()-dateutil.relativedelta.relativedelta(months=1)).month,1)
		fhasta = datetime(datetime.now().year,datetime.now().month,calendar.monthrange(datetime.now().year,datetime.now().month)[1])
		factual = datetime.now()
		fecha_finalizacion = datetime(datetime.now().year,datetime.now().month,calendar.monthrange(datetime.now().year,datetime.now().month)[1])
		grupo=2
		moneda=[0]
		status_zeep_anidado = []
		cotizaciones_zeep_anidado = []
		cotizaciones_filtradas = []
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
		#Grabar cotizaciones en BD
		for cotiza in cotizaciones_zeep_anidado:
			if cotiza['Fecha'] <= datetime.date(fecha_finalizacion):
				cotizaciones_filtradas.append(cotiza)
				#Cotizaciones_1 = []
				try:
					User = get_user_model()
					id_usuario = User.objects.get(pk=request.user.identificador) # 9999
					Cotizaciones.identificador_id = id_usuario # request.GET.getlist('user.identificador')[0]
					Cotizaciones.fecha = cotiza['Fecha']
					Cotizaciones.moneda = cotiza['Moneda']
					Cotizaciones.nombre = cotiza['Nombre']
					Cotizaciones.codigo_ISO = cotiza['CodigoISO']
					Cotizaciones.emisor = cotiza['Emisor']
					Cotizaciones.tcc = cotiza['TCC']
					Cotizaciones.tcv = cotiza['TCV']
					Cotizaciones.arbact = cotiza['ArbAct']
					Cotizaciones.forma_arbitrar = cotiza['FormaArbitrar']
										
					super(self.Cotizaciones, self).save()
					self.kwargs = {'cotizaciones_zeep': cotizaciones_zeep_anidado, 'status_zeep': status_zeep_anidado, 'Cotizaciones': Cotizaciones}
				except Exception as e:
					pass
					#raise e
		return render(request, 'cotizaciones.html', {'form': form, 'cotizaciones': self.kwargs['cotizaciones_zeep'], 'factual': factual}) #, 'e': e
	

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
class EscogerCotizacionesAutomaticas(LoginRequiredMixin, CreateView):	
	
	model = Cotizaciones
	fields = ['fecha','moneda','nombre','codigo_ISO','emisor','tcc','tcv','arbact','forma_arbitrar']
	form_class = FormCotizaciones
	template_name = 'cotizaciones2.html'
	login_url = 'Usuarios:Login'
	
	class Meta:
		model = Cotizaciones
	

	
	def get(self, request, *args, **kwargs):

		form = FormCotizaciones()
		if request.method == 'GET' and request.GET.getlist('fdesde[]') is not None and request.GET.getlist('fhasta[]') is not None:
			fdesde = datetime.strptime(request.GET.getlist('fdesde')[0], '%Y-%m-%d') # datetime(datetime.now().year,datetime.now().month-4,1)
			if fdesde < datetime(2000,1,1):
				fdesde = datetime(2000,1,1)
			fhasta = datetime(datetime.now().year,datetime.now().month,calendar.monthrange(datetime.now().year,datetime.now().month)[1]) #datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d') # 
			final_year = datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d').year
			final_month = datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d').month
			final_day = datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d').day
			fecha_finalizacion = datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d')
			if fecha_finalizacion >= datetime.now():
				fecha_finalizacion = datetime(datetime.now().year,datetime.now().month,datetime.now().day)
			mis_meses2 = (fhasta.month - fdesde.month + 1)*(fhasta.year - fdesde.year + 1)
			mis_meses3 = relativedelta.relativedelta(fhasta,fdesde)
			
		else:
			fdesde = datetime((datetime.now()- dateutil.relativedelta.relativedelta(months=1)).year,(datetime.now()- dateutil.relativedelta.relativedelta(months=1)).month-2,1)
			fhasta = datetime(datetime.now().year,datetime.now().month,calendar.monthrange(datetime.now().year,datetime.now().month)[1])

		wsdl = "https://cotizaciones.bcu.gub.uy/wscotizaciones/servlet/awsbcucotizaciones?wsdl"
		settings = Settings(strict=False, xml_huge_tree=True)
		client_1 = Client_zeep(wsdl=wsdl, settings=settings)
		grupo=2
		moneda=[0]
		status_zeep_anidado = []
		cotizaciones_zeep_anidado = []
		cotizaciones_filtradas = []
		control = 0

		if fhasta >= fdesde:
			
			while datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) <= fecha_finalizacion or datetime(fdesde.year,fdesde.month,1) <= fecha_finalizacion:
				#meses = relativedelta.relativedelta(fhasta,fdesde)
				finicial = fdesde
				ffinal = datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1])
				if datetime(fdesde.year,fdesde.month,calendar.monthrange(fdesde.year,fdesde.month)[1]) > fhasta:
					ffinal = fhasta
				fdesde = ffinal + timedelta(days=1)
				control += 1
				request_zeep = {'Entrada' :	{
					'Moneda': {'item' : moneda},
					'FechaDesde': finicial.isoformat(),
					'FechaHasta': ffinal.isoformat(),
					'Grupo': '0',}}
				respuesta_ws_cotiza_zeep_a1 = client_1.service.Execute(**request_zeep)
				status_zeep = respuesta_ws_cotiza_zeep_a1['respuestastatus'] #Diccionario con 'status', 'codigoerror', 'mensaje'
				status_zeep_anidado.extend(status_zeep)
				#Lista con Diccionarios, cada diccionario contiene: 'Fecha', 'Moneda', 'Nombre', 'CodigoISO', 'Emisor', 'TCC', 'TCV', 'ArbAct', 'FormaArbitrar'
				cotizaciones_zeep_a1 = respuesta_ws_cotiza_zeep_a1['datoscotizaciones']['datoscotizaciones.dato']
				cotizaciones_zeep_anidado.extend(cotizaciones_zeep_a1)
				
		#cotizaciones_filtradas = cotizaciones_zeep_anidado
		mis_meses4 = len(cotizaciones_zeep_anidado)
		mis_meses5 = (cotizaciones_zeep_anidado[0]['Fecha'])

		fdesde = datetime.strptime(request.GET.getlist('fdesde')[0], '%Y-%m-%d')
		fhasta = datetime.strptime(request.GET.getlist('fhasta')[0], '%Y-%m-%d')
		mis_meses6 = (mis_meses5 < datetime.date(fhasta))
		for cotiza in cotizaciones_zeep_anidado:
			if cotiza['Fecha'] <= datetime.date(fhasta):
				cotizaciones_filtradas.append(cotiza)
				try:
					User = get_user_model()
					id_usuario = User.objects.get(pk=request.user.identificador) # 9999
					Cotizaciones.identificador_id = id_usuario # request.GET.getlist('user.identificador')[0]
					Cotizaciones.fecha = cotiza['Fecha']
					Cotizaciones.moneda = cotiza['Moneda']
					Cotizaciones.nombre = cotiza['Nombre']
					Cotizaciones.codigo_ISO = cotiza['CodigoISO']
					Cotizaciones.emisor = cotiza['Emisor']
					Cotizaciones.tcc = cotiza['TCC']
					Cotizaciones.tcv = cotiza['TCV']
					Cotizaciones.arbact = cotiza['ArbAct']
					Cotizaciones.forma_arbitrar = cotiza['FormaArbitrar']
					Cotizaciones.objects.create(uc=request.user.identificador, um=request.user.identificador, identificador_id=request.user.identificador, fecha=Cotizaciones.fecha, moneda=Cotizaciones.moneda, nombre=Cotizaciones.nombre, codigo_ISO=Cotizaciones.codigo_ISO, emisor=Cotizaciones.emisor, tcc=Cotizaciones.tcc, tcv=Cotizaciones.tcv, arbact=Cotizaciones.arbact, forma_arbitrar=Cotizaciones.forma_arbitrar)
				except Exception as e:
					pass
					#raise e
		
		mis_meses7 = len(cotizaciones_filtradas)

		qs = Cotizaciones.pdobjects.all().order_by('moneda','fecha')
		df = qs.to_dataframe()
		df2 = pd.DataFrame()
		for Moneda in df.nombre.unique():
			df1 = df[df['nombre'] == Moneda]
			df1 = df1.set_index('fecha').asfreq('d')
			df1 = df1.fillna(method="ffill")
			df2 = pd.concat([df1, df2])
		for i in range(0, len(df2)):
			try:
				Cotizaciones.objects.create(uc=request.user.identificador, um=request.user.identificador, identificador_id=request.user.identificador, fecha=df2.iloc[i]['fecha'], moneda=df2.iloc[i]['moneda'], nombre=df2.iloc[i]['nombre'], codigo_ISO=df2.iloc[i]['codigo_ISO'], emisor=df2.iloc[i]['emisor'], tcc=df2.iloc[i]['tcc'], tcv=df2.iloc[i]['tcv'], arbact=df2.iloc[i]['arbact'], forma_arbitrar=df2.iloc[i]['forma_arbitrar'])
			except Exception as e:
				pass
				#raise e
					


		df3 = pd.DataFrame()
		df3 = pd.concat([df, df2])
		df3.drop_duplicates(subset=['fecha','nombre','tcc'], keep=False)


		self.request = request
		self.args = args
		self.kwargs = {'mis_cotizaciones_zeep': cotizaciones_filtradas, 'mis_status_zeep': status_zeep_anidado, 'fdesde': fdesde, 'fhasta': fhasta}

		return render(request, 'cotizaciones2.html', {'form': form, 'cotizaciones_a1': self.kwargs['mis_cotizaciones_zeep'], 'fdesde': fdesde, 'fhasta': fhasta, 'final_year': final_year, 'final_month': final_month, 'final_day': final_day, 'control': control, 'fecha_finalizacion':fecha_finalizacion, 'mis_meses2':mis_meses2, 'mis_meses3':mis_meses3, 'mis_meses4':mis_meses4, 'mis_meses5':mis_meses5, 'mis_meses6':mis_meses6, 'mis_meses7':mis_meses7}) #'mis_meses6':mis_meses6
	

	def save(self, request, *args, **kwargs):
		super(Cotizaciones, self).save()
