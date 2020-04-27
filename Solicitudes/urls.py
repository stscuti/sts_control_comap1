from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from Control_Coordinacion import views as Vistas_Control_Coordinacion
from Control_Seguimiento_Contable import views as Vistas_Control_Seguimiento_Contable
from Control_Seguimiento_Obra import views as Vistas_Control_Seguimiento_Obra
from Control_VU import views as Vistas_Control_VU
from Evaluacion import views as Vistas_Evaluacion
from Usuarios import views as Vistas_Usuarios
from Contribuyentes import views as Vistas_Contribuyentes
from Solicitudes import views as Vistas_Solicitudes
from Mensajeria import views as Vistas_Mensajeria
from COMAP_Control import views as Vistas_COMAP_Control
from WS import views as Vistas_WS
from WF import views as Vistas_WF
from Base import views as Vistas_Base
from .forms import * 

form_list = [SolicitudesStep1_Form, SolicitudesStep1b_Form, SolicitudesStep2_Form, SolicitudesStep2b_Form, SolicitudesStep2c_Form, SolicitudesStep2d_Form, SolicitudesStep2e_Form, SolicitudesStep2f_Form]

urlpatterns = [
	
	path('solicitudes/', Vistas_Solicitudes.FormWizardView.as_view(template_name='solicitudes.html'), name='Solicitudes'),
	path('listadosolicitudes/', Vistas_Solicitudes.ListadoSolicitudes.as_view(template_name='solicitudes.html'), name='ListadoSolicitudes'),
	path('solicitudes/edit/<int:pk>', Vistas_Solicitudes.UpdateFormWizardView.as_view(form_list), name='Edit_Solicitudes'),
	#path('cotizaciones_automaticas/', Vistas_WS.CotizacionesAutomaticasUpdateView.as_view(template_name='cotizaciones.html'), name='Cotizaciones_Automaticas'),
	##path('escoger_cotizaciones_automaticas/', Vistas_WS.EscogerCotizacionesAutomaticas.as_view(), name='Escoger_Cotizaciones_Automaticas'),
	#path('cotizaciones_automaticas/<uuid:csrfmiddlewaretoken>/<slug:fdesde>/<slug:fhasta>/', Vistas_WS.CotizacionesAutomaticasCreateView.as_view(template_name='cotizaciones.html'), name='Cotizaciones_Automaticas_Fechas'),
	#<slug:fdesde>/<slug:fhasta>/<uuid:csrfmiddlewaretoken> <slug:uidb64>/<slug:token>/<slug:key>/
	path('api/solicitudes/', Vistas_Solicitudes.SolicitudesList.as_view(), name='SolicitudesList'),
	path('api/localizaciones_solicitudes/', Vistas_Solicitudes.SolicitudesLocalizacionesList.as_view(), name='SolicitudesLocalizacionesList'),


]