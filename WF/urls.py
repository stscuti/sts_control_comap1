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


urlpatterns = [
	
    #path('cotizaciones/', Vistas_WS.CotizacionesCreateView.as_view(template_name='cotizaciones.html'), name='Cotizaciones'),



]