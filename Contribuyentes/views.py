from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import CreateView, TemplateView
from django.views import View
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

from django.template.loader import render_to_string
from datetime import datetime, timedelta, tzinfo, time, date
import pytz
from django.utils import timezone
# Create your views here.

class MultiContribuyente_CreateView(LoginRequiredMixin, CreateView):
	form_class = MultiContribuyentesForm
	template_name = 'crearcontribuyente.html'
	login_url = "Usuarios:Login"

	def get(self, request):
		form = MultiContribuyentesForm()
		usuario = request.user
		return render(request, 'crearcontribuyente.html', {'form': form, 'usuario':usuario})

	def form_valid(self, form):
		# Create an inactive user with no password:
		usuario = self.request.user

		ContribuyentePrincipal = form['ContribuyenteMain'].save(commit=False)
		ContribuyentePrincipal.identificador = usuario
		ContribuyentePrincipal.uc = usuario
		ContribuyentePrincipal.save()

		DomicilioFiscalPrincipal = form['DomicilioFiscalMain'].save(commit=False)
		DomicilioFiscalPrincipal.identificador = ContribuyentePrincipal
		DomicilioFiscalPrincipal.uc = ContribuyentePrincipal.identificador
		DomicilioFiscalPrincipal.save()

		DomicilioConstituidoPrincipal = form['DomicilioConstituidoMain'].save(commit=False)
		DomicilioConstituidoPrincipal.identificador = ContribuyentePrincipal
		DomicilioConstituidoPrincipal.uc = ContribuyentePrincipal.identificador
		DomicilioConstituidoPrincipal.save()

		PropietariosPrincipal = form['PropietariosMain'].save(commit=False)
		PropietariosPrincipal.identificador = ContribuyentePrincipal
		PropietariosPrincipal.uc = ContribuyentePrincipal.identificador
		PropietariosPrincipal.save()

		RepresentantesPrincipal = form['RepresentantesMain'].save(commit=False)
		RepresentantesPrincipal.identificador = ContribuyentePrincipal
		RepresentantesPrincipal.uc = ContribuyentePrincipal.identificador
		RepresentantesPrincipal.save()

		DirectoresPrincipal = form['DirectoresMain'].save(commit=False)
		DirectoresPrincipal.identificador = ContribuyentePrincipal
		DirectoresPrincipal.uc = ContribuyentePrincipal.identificador
		DirectoresPrincipal.save()

		return HttpResponseRedirect(reverse('Contribuyentes:Crear_Contribuyente'))